# Backend OpenTelemetry Facade Reference (Python 3.14 + FastAPI)

## 1. Dependencies (`uv` / `pyproject.toml`)

Use `opentelemetry-exporter-otlp-proto-http` (pure HTTP/Protobuf on port `4318`) to avoid `grpcio` C-extension build issues on Python 3.14:

```bash
uv add opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-instrumentation-fastapi opentelemetry-instrumentation-httpx opentelemetry-instrumentation-logging httpx
```

## 2. Single Modular Backend Facade & Non-Blocking Relay (`app/core/telemetry.py`)

All `opentelemetry.*` imports live inside `app/core/telemetry.py`. Application services and routes import only `from app.core.telemetry import telemetry`:

```python
import asyncio
from contextlib import asynccontextmanager, contextmanager
import logging
import os
import time
from typing import Any, AsyncIterator, Iterator, Literal

import httpx
from fastapi import APIRouter, FastAPI, Header, HTTPException, Request, Response

logger = logging.getLogger(__name__)

MAX_PAYLOAD_BYTES = 512 * 1024  # 512 KB cap
LATENCY_BUCKETS = (0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 10.0)

type RelayBatch = tuple[str, bytes, str, str | None]


class OTelTraceLogFilter(logging.Filter):
    """Injects lowercase trace_id and span_id into every Python log record."""

    def __init__(self, enabled: bool) -> None:
        super().__init__()
        self.enabled = enabled

    def filter(self, record: logging.LogRecord) -> bool:
        if not self.enabled:
            record.trace_id = ""
            record.span_id = ""
            return True
        from opentelemetry import trace

        span = trace.get_current_span()
        ctx = span.get_span_context()
        if ctx and ctx.is_valid:
            record.trace_id = f"{ctx.trace_id:032x}"
            record.span_id = f"{ctx.span_id:016x}"
        else:
            record.trace_id = ""
            record.span_id = ""
        return True


class TelemetryFacade:
    """Single modular facade for all backend tracing, RED metrics, and browser OTLP/HTTP relay."""

    def __init__(self) -> None:
        self.enabled: bool = os.getenv("TELEMETRY_ENABLED", "true").lower() == "true"
        self.endpoint: str = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector:4318").rstrip("/")
        self._tracer: Any = None
        self._meter: Any = None
        self._counters: dict[str, Any] = {}
        self._histograms: dict[str, Any] = {}
        self._relay_queue: asyncio.Queue[RelayBatch] = asyncio.Queue(maxsize=1000)
        self.router = self._build_relay_router()

    def init_app(self, app: FastAPI, project_name: str, version: str, env: str) -> None:
        app.include_router(self.router)
        logging.getLogger().addFilter(OTelTraceLogFilter(self.enabled))

        if not self.enabled:
            return

        from opentelemetry import metrics, trace
        from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
        from opentelemetry.sdk.metrics import MeterProvider
        from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
        from opentelemetry.sdk.metrics.view import ExplicitBucketHistogramAggregation, View
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        resource = Resource.create(
            {
                "service.name": f"{project_name}-api",
                "service.namespace": project_name,
                "service.version": version,
                "deployment.environment.name": env,
                "app.layer": "backend",
            }
        )

        tracer_provider = TracerProvider(resource=resource)
        tracer_provider.add_span_processor(
            BatchSpanProcessor(OTLPSpanExporter(endpoint=f"{self.endpoint}/v1/traces"))
        )
        trace.set_tracer_provider(tracer_provider)
        self._tracer = trace.get_tracer(f"{project_name}-api")

        metric_reader = PeriodicExportingMetricReader(
            OTLPMetricExporter(endpoint=f"{self.endpoint}/v1/metrics"),
            export_interval_millis=15000,
        )
        meter_provider = MeterProvider(
            resource=resource,
            metric_readers=[metric_reader],
            views=[
                View(
                    instrument_name="http.server.request.duration",
                    aggregation=ExplicitBucketHistogramAggregation(LATENCY_BUCKETS),
                )
            ],
        )
        metrics.set_meter_provider(meter_provider)
        self._meter = metrics.get_meter(f"{project_name}-api")

        req_duration = self._meter.create_histogram(
            name="http.server.request.duration",
            unit="s",
            description="Duration of HTTP server requests",
        )

        @app.middleware("http")
        async def red_metrics_middleware(request: Request, call_next: Any) -> Response:
            if request.url.path.startswith(("/api/telemetry", "/health", "/ready", "/metrics")):
                return await call_next(request)
            start = time.perf_counter()
            response: Response = await call_next(request)
            duration = time.perf_counter() - start
            route = request.scope.get("route")
            route_template = getattr(route, "path", "UNMATCHED")
            req_duration.record(
                duration,
                attributes={
                    "http.request.method": request.method,
                    "http.route": route_template,
                    "http.response.status_code": response.status_code,
                },
            )
            return response

        FastAPIInstrumentor.instrument_app(
            app,
            excluded_urls="api/telemetry/.*,health,healthz,ready,live,metrics",
        )

    @asynccontextmanager
    async def lifespan(self, _app: FastAPI) -> AsyncIterator[None]:
        if not self.enabled:
            yield
            return
        worker = asyncio.create_task(self._relay_worker())
        try:
            yield
        finally:
            worker.cancel()

    async def _relay_worker(self) -> None:
        async with httpx.AsyncClient(timeout=5.0) as client:
            while True:
                signal, body, content_type, content_encoding = await self._relay_queue.get()
                headers = {"Content-Type": content_type}
                if content_encoding:
                    headers["Content-Encoding"] = content_encoding
                try:
                    await client.post(
                        f"{self.endpoint}/v1/{signal}",
                        content=body,
                        headers=headers,
                    )
                except Exception as exc:
                    logger.warning("OTel HTTP relay forward failed for %s: %s", signal, exc)
                finally:
                    self._relay_queue.task_done()

    def _build_relay_router(self) -> APIRouter:
        router = APIRouter(prefix="/api/telemetry/v1", tags=["telemetry"])

        @router.post("/{signal}", status_code=202)
        async def relay_browser_telemetry(
            signal: Literal["traces", "metrics", "logs"],
            request: Request,
            content_type: str = Header(default="application/json"),
            content_encoding: str | None = Header(default=None),
        ) -> Response:
            if not self.enabled:
                return Response(status_code=202)
            media_type = content_type.split(";")[0].strip().lower()
            if media_type not in ("application/json", "application/x-protobuf"):
                raise HTTPException(status_code=415, detail="Unsupported OTLP Content-Type")

            body = await request.body()
            if len(body) > MAX_PAYLOAD_BYTES:
                raise HTTPException(status_code=413, detail="Telemetry payload exceeds 512KB limit")

            try:
                self._relay_queue.put_nowait((signal, body, media_type, content_encoding))
            except asyncio.QueueFull:
                logger.warning("Telemetry relay queue full; dropping %s batch", signal)

            return Response(status_code=202)

        return router

    @contextmanager
    def span(self, name: str, attributes: dict[str, Any] | None = None) -> Iterator[Any]:
        if not self.enabled or self._tracer is None:
            yield None
            return
        with self._tracer.start_as_current_span(name, attributes=attributes) as s:
            yield s

    def count(self, name: str, value: int = 1, attributes: dict[str, Any] | None = None) -> None:
        if not self.enabled or self._meter is None:
            return
        counter = self._counters.get(name)
        if counter is None:
            counter = self._meter.create_counter(name)
            self._counters[name] = counter
        counter.add(value, attributes=attributes or {})

    def record_error(self, exc: BaseException, attributes: dict[str, Any] | None = None) -> None:
        if not self.enabled or self._tracer is None:
            return
        from opentelemetry import trace
        from opentelemetry.trace import StatusCode

        span = trace.get_current_span()
        if span and span.is_recording():
            span.record_exception(exc, attributes=attributes)
            span.set_status(StatusCode.ERROR, str(exc))


telemetry = TelemetryFacade()
```
