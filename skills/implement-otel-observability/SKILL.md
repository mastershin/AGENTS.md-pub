---
name: implement-otel-observability
description: Implement, audit, upgrade, or refactor OpenTelemetry (OTLP/HTTP) instrumentation across any frontend (Vue 3, React, Vite, Router, Astryx) and backend (Python 3.14, Rust, Node, Go) using a modular single-class facade, first-party relay, current semantic conventions, and Collector fan-out. Use when asked to implement, review, upgrade, or migrate observability, OpenTelemetry SDKs, RED/USE/RUM metrics, traces, or logs, or build /api/telemetry relay endpoints.
---

# Implement OpenTelemetry Observability

Execute this language-neutral workflow when auditing, adding, or updating OpenTelemetry instrumentation across frontend, backend, and Collector layers so telemetry stays modular, secure, low-cardinality, and portable across SigNoz, OpenObserve, and Grafana.

## When to Use

* Auditing, upgrading, or refactoring existing telemetry or OpenTelemetry setups.
* Instrumenting browser apps (Vue 3, React, Vite, Router, Astryx) or backend APIs/workers (Python 3.14, Rust, Node, Go) with OpenTelemetry.
* Building `/api/telemetry/v1/{signal}` first-party relay endpoints.
* Configuring OpenTelemetry Collector pipelines, tail sampling, or multi-backend fan-out.

## Stack Detection & Reference Loading

Before writing code, inspect the project files (`package.json`, `pyproject.toml`, `Cargo.toml`, `docker-compose.yml`) and load ONLY the matching reference file(s):

* **Browser Frontend (Vue 3, React, Vite, Router, Astryx):** Read `references/frontend-vue-react-vite.md`
* **Python 3.14 / FastAPI Backend:** Read `references/backend-python-fastapi.md`
* **Rust (Axum / Actix / Tokio) Backend:** Read `references/backend-rust-axum.md`
* **OTel Collector & Multi-Backend Fan-Out:** Read `references/otel-collector-fanout.yaml`

## Core Architectural Rules

### Step 0: Audit & Classify Existing Telemetry (Before Writing Code)

Always scan the repository first to determine whether to **Implement (Greenfield)**, **Upgrade in Place**, or **Consolidate & Rewrite**:

1. **Run Discovery Scans:**
   * **Dependency & Exporter Scan:** Check `package.json`, `pyproject.toml`, `Cargo.toml`, and `docker-compose.yml` for existing OTel packages, `grpcio` / `tonic` gRPC exporters (`:4317`), or third-party SDKs (Sentry, Datadog, PostHog, Langfuse).
   * **Encapsulation Leak Scan:** Search for scattered SDK imports outside a dedicated telemetry module:
     `grep -rnE "from ['\"]@opentelemetry|from opentelemetry|import opentelemetry|tracing_opentelemetry" src/ app/ frontend/ backend/`
   * **Security & Anti-Pattern Scan:** Check for direct browser-to-collector URLs (`:4318`, `:5080`, `openobserve`, `signoz`), exposed `VITE_OTEL_*` / `NEXT_PUBLIC_OTEL_*` auth headers, synchronous `await client.post(...)` inside `/api/telemetry` routes, or high-cardinality metric labels (`user_id`, `request.url.path`).

2. **Select Execution Mode:**
   * **Mode A - Greenfield (No existing telemetry):** Scaffold the modular `TelemetryFacade`, non-blocking `/api/telemetry/v1/{signal}` relay, and Collector config from scratch following Steps 1-5.
   * **Mode B - Surgical Upgrade (Centralized module exists, minor gaps):** Preserve the existing facade and call sites, but upgrade internals to match current rules:
     * Migrate gRPC (`:4317`) exporters to `OTLP/HTTP` (`http/protobuf` on `:4318`).
     * Add the `TELEMETRY_ENABLED=false` / `VITE_TELEMETRY_ENABLED=false` No-Op kill-switch if missing.
     * Add missing Resource attributes (`service.name` `-web`/`-api` split, `app.layer`, `deployment.environment.name`) and upgrade deprecated Semantic Conventions (`db.system` -> `db.system.name`, `gen_ai.system` -> `gen_ai.provider.name`).
   * **Mode C - Consolidate & Rewrite (Scattered imports, direct browser exports, or blocking relay):**
     * Create the single modular `TelemetryFacade` (`src/telemetry/` or `app/core/telemetry.py`).
     * Replace all scattered `@opentelemetry/*` / `opentelemetry.*` imports across routes, services, and UI components with facade calls (`telemetry.span()`, `telemetry.count()`, `telemetry.record_error()`) or top-level middleware.
     * Remove duplicate `TracerProvider` / `MeterProvider` initializations so only one provider pair exists per process.
     * Reroute any direct browser exporters to `/api/telemetry/v1/{signal}` and remove client-side ingestion secrets.

### Step 1: Enforce the Single-Facade Modularity & Kill-Switch Pattern

1. **Strict Encapsulation (Zero Direct OTel Imports Outside `telemetry/`):**
   * Application code (route handlers, business services, database repositories, Vue SFCs, React components) must never import `@opentelemetry/*`, `opentelemetry.*`, or `tracing_opentelemetry` directly.
   * Isolate all OpenTelemetry SDK imports, exporters, and middleware wiring inside a single dedicated module:
     * **Frontend:** `src/telemetry/index.ts` (exposing a singleton `telemetry` facade + framework plugin)
     * **Python Backend:** `app/core/telemetry.py` (exposing a singleton `telemetry` facade class)
     * **Rust Backend:** `src/telemetry/mod.rs` (exposing a `Telemetry` struct/trait facade)
2. **Unified Kill-Switch (`TELEMETRY_ENABLED=false`):**
   * Support `TELEMETRY_ENABLED=false` (backend) and `VITE_TELEMETRY_ENABLED=false` (frontend).
   * When disabled, `telemetry.init()` binds a **No-Op implementation** where `.span()`, `.count()`, and `.record_error()` execute as zero-allocation no-ops and the `/api/telemetry/v1/{signal}` relay immediately returns `202 Accepted` without queueing or forwarding.
3. **Middleware-First Instrumentation:**
   * Wire HTTP RED metrics, W3C `traceparent` propagation, and unhandled exception capture inside `telemetry.init(app)` so 90%+ of routes and UI components require zero manual telemetry calls.

### Step 2: Enforce the First-Party Relay & OTLP/HTTP (`:4318`) Standard

1. **Standardize on `OTLP/HTTP` (`:4318`) Everywhere:**
   * Default all backend SDK exporters (`opentelemetry-exporter-otlp-proto-http` in Python, `opentelemetry-otlp` with `http-proto` in Rust) and the `/api/telemetry` relay forwarder to `OTLP/HTTP` (`http/protobuf` on port `4318`) rather than gRPC (`:4317`).
   * Set standard environment variables across backend services:
     * `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`
     * `OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4318`
   * Why: Avoids `grpcio` C-extension build issues on Python 3.14, eliminates HTTP/2 load-balancer sticky connection traps, and allows zero-copy byte forwarding from the browser relay.
2. **Same-Origin Relative Browser Export:**
   * Browser JS must export OTLP exclusively to relative paths: `/api/telemetry/v1/traces`, `/api/telemetry/v1/metrics`, and `/api/telemetry/v1/logs`.
   * Never point browser code directly at OpenObserve, SigNoz, external collector ports, or third-party analytics domains.
3. **Zero Client Secrets:**
   * Never place `OTEL_EXPORTER_OTLP_HEADERS`, Basic Auth credentials, API keys, or collector URLs in browser bundles or `VITE_*` / `NEXT_PUBLIC_*` environment variables.
4. **Non-Blocking Pass-Through Relay (`/api/telemetry/v1/{signal}`):**
   * Accept `signal` in `{"traces", "metrics", "logs"}` and `Content-Type` in `{"application/json", "application/x-protobuf"}`.
   * Reject payloads exceeding 512 KB (`413`), enforce per-IP rate limits, and strip `Authorization`, `Cookie`, and client IP headers (`X-Forwarded-For`, `X-Real-IP`).
   * Push raw OTLP bytes onto a bounded in-memory async queue/channel (capacity 1000; drop with a rate-limited warning if full) and immediately return HTTP `202 Accepted`.
   * Forward raw bytes untouched to `${OTEL_EXPORTER_OTLP_ENDPOINT}/v1/${signal}` without re-parsing through the backend's `TracerProvider` or `LoggerProvider`, preserving the browser's `Resource` attributes.

### Step 3: Standardize Resource Identity & Context Propagation (SemConv v1.33+)

Initialize every SDK `Resource` with these exact attributes so SigNoz, OpenObserve, and Grafana separate frontend and backend layers identically:

| Attribute | Browser Frontend | Backend API / Worker |
| :--- | :--- | :--- |
| `service.name` | `<project>-web` | `<project>-api` (or `<project>-worker`) |
| `service.namespace` | `<project>` | `<project>` |
| `service.version` | Git SHA / release version | Git SHA / release version |
| `deployment.environment.name` | `prod` / `staging` / `dev` | `prod` / `staging` / `dev` |
| `app.layer` | `frontend` | `backend` |

* **Context Propagation & Loop Prevention:**
  * Enable `W3CTraceContextPropagator` (`traceparent`, `tracestate`) on browser `fetch`/`XHR` strictly for same-origin `/api/*` routes.
  * Exclude `/api/telemetry` and health checks in browser fetch auto-instrumentation (`ignoreUrls: [/\/api\/telemetry/, /\/healthz?$/]`) to prevent infinite export loops.
  * Flush pending browser telemetry on `visibilitychange` (`hidden`) using `fetch` (`keepalive: true`) so tab-close errors survive page unload.

### Step 4: Instrument Lean Signal Scopes & Current Semantic Conventions

* **Frontend (Browser RUM & Errors Only):**
  * Collect Core Web Vitals (`LCP`, `INP`, `CLS`), document load timing, unhandled errors (`error`, `unhandledrejection`, Vue `errorHandler`, or React `ErrorBoundary`), and `/api/*` client spans tagged with the router's parameterized route pattern (`url.template`).
  * Do not emit API usage counters or business analytics from JS. Do not capture sub-resource asset waterfalls (images, fonts, CSS) or mouse/DOM spam.
* **Backend (RED + Exemplars + GenAI/DB SemConv + Correlated Logs):**
  * **HTTP RED Metrics:** Emit `http.server.request.duration` histograms (in seconds, with explicit latency buckets `[0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 10.0]` and **Exemplars** enabled) using `http.request.method`, parameterized `http.route` (never raw URL path), and `http.response.status_code`.
  * **Database & Cache Spans:** Use `db.system.name` (`postgresql`, `duckdb`, `redis`, `sqlite`, `qdrant`), `db.namespace`, and `db.operation.name`. Never attach raw query parameter literals containing PII.
  * **GenAI / LLM & MCP Spans:** Use `gen_ai.operation.name` (`chat`, `embeddings`, `execute_tool`), `gen_ai.provider.name` (`vllm`, `sglang`, `ollama`, `litellm`, `openai`), `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.response.time_to_first_chunk`, and `gen_ai.conversation.id`. Keep raw prompt/completion capture (`gen_ai.input.messages` / `gen_ai.output.messages`) disabled by default (`OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=false`).
  * **Structured Logs:** Emit JSON logs at `INFO`/`WARN`/`ERROR` with lowercase `trace_id`, `span_id`, `service.name`, and `app.layer` injected into every record.
  * **Infrastructure USE Metrics:** Collect host CPU, RAM, disk I/O, container stats, and GPU metrics via the OTel Collector (`hostmetrics`, `docker_stats`, Prometheus/DCGM receivers), never inside application threads.

### Step 5: Enforce Cardinality, Redaction & Sampling Guardrails

* **Zero High-Cardinality Metric Labels:** Never attach `user_id`, `request_id`, `trace_id`, `session_id`, `conversation_id`, or unparameterized URL paths (`url.path`) to metric attributes. Place high-cardinality IDs only on trace spans and log records.
* **Health-Check Exclusions:** Exclude `/health`, `/healthz`, `/ready`, `/live`, and `/metrics` from server trace generation.
* **Collector Pipeline Order:** Always configure Collector processors in the order: `memory_limiter` -> `filter` (drop health checks) -> `attributes` (redact secrets/PII) -> `tail_sampling` (100% errors & slow traces over 1s, 5-10% healthy `200 OK`) -> `batch`.

## Verification Checklist

Run these checks before completing any observability implementation:

1. `grep -rnE "from ['\"]@opentelemetry|from opentelemetry|import opentelemetry" --exclude-dir=telemetry --exclude=telemetry.py src/ app/` returns zero matches outside the dedicated telemetry module.
2. `grep -rnE "OTEL_EXPORTER|:4317|:4318|openobserve|signoz" src/ frontend/` returns zero matches in browser code.
3. Backend dependencies use `http/protobuf` exporters (`opentelemetry-exporter-otlp-proto-http` in Python; `opentelemetry-otlp` with `http-proto`/`reqwest-client` in Rust) pointing to port `4318`.
4. Frontend `Resource` sets `service.name="<project>-web"` and `app.layer="frontend"`; backend sets `service.name="<project>-api"` and `app.layer="backend"`.
5. Browser `FetchInstrumentation` includes `ignoreUrls: [/\/api\/telemetry/, /\/healthz?$/]`.
6. `/api/telemetry/v1/{signal}` enforces a 512 KB cap, strips auth/cookie/IP headers, supports `TELEMETRY_ENABLED=false` no-op bypass, and returns `202 Accepted` via a bounded background queue/channel.
7. Both frontend router hooks and backend HTTP middleware record parameterized route templates (`http.route` / `url.template`) rather than raw URLs with IDs.
