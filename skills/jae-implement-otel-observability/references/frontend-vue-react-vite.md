# Frontend OpenTelemetry Facade Reference (Vue 3 & React + Vite + Router + Astryx)

## 1. Modular Frontend Telemetry Facade (`src/telemetry/index.ts`)

Install lightweight HTTP web packages:
```bash
npm install @opentelemetry/api @opentelemetry/sdk-trace-web @opentelemetry/exporter-trace-otlp-http @opentelemetry/instrumentation @opentelemetry/instrumentation-fetch @opentelemetry/instrumentation-document-load @opentelemetry/resources @opentelemetry/core web-vitals
```

All `@opentelemetry/*` imports are strictly isolated inside `src/telemetry/index.ts`. Components, stores, and views only import `telemetry` from `@/telemetry`:

```typescript
import { WebTracerProvider, BatchSpanProcessor } from '@opentelemetry/sdk-trace-web';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';
import { DocumentLoadInstrumentation } from '@opentelemetry/instrumentation-document-load';
import { registerInstrumentations } from '@opentelemetry/instrumentation';
import { W3CTraceContextPropagator } from '@opentelemetry/core';
import { resourceFromAttributes } from '@opentelemetry/resources';
import { trace, SpanStatusCode, type Tracer } from '@opentelemetry/api';
import { onCLS, onINP, onLCP, type Metric } from 'web-vitals';

export interface TelemetryConfig {
  projectName: string;
  version: string;
  env: string;
  enabled?: boolean;
  resolveRouteTemplate?: () => string;
}

class FrontendTelemetryFacade {
  private enabled = false;
  private provider: WebTracerProvider | null = null;
  private tracer: Tracer | null = null;
  private routeResolver: () => string = () => 'unknown';

  public init(config: TelemetryConfig): void {
    this.enabled = config.enabled ?? import.meta.env.VITE_TELEMETRY_ENABLED !== 'false';
    if (config.resolveRouteTemplate) {
      this.routeResolver = config.resolveRouteTemplate;
    }
    if (!this.enabled) return;

    const resource = resourceFromAttributes({
      'service.name': `${config.projectName}-web`,
      'service.namespace': config.projectName,
      'service.version': config.version,
      'deployment.environment.name': config.env,
      'app.layer': 'frontend',
    });

    const traceExporter = new OTLPTraceExporter({
      url: '/api/telemetry/v1/traces',
      headers: {},
    });

    this.provider = new WebTracerProvider({
      resource,
      spanProcessors: [
        new BatchSpanProcessor(traceExporter, {
          maxQueueSize: 200,
          maxExportBatchSize: 50,
          scheduledDelayMillis: 3000,
        }),
      ],
    });

    this.provider.register({
      propagator: new W3CTraceContextPropagator(),
    });

    this.tracer = trace.getTracer(`${config.projectName}-web-rum`);

    registerInstrumentations({
      instrumentations: [
        new DocumentLoadInstrumentation(),
        new FetchInstrumentation({
          propagateTraceHeaderCorsUrls: [/^\/api\/(?!telemetry)/],
          ignoreUrls: [/\/api\/telemetry/, /\/healthz?$/, /\/ready$/],
          clearTimingResources: true,
          applyCustomAttributesOnSpan: (span) => {
            span.setAttribute('url.template', this.routeResolver());
          },
        }),
      ],
    });

    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') {
        void this.flush();
      }
    });

    const reportVital = (metric: Metric) => {
      if (!this.tracer) return;
      const span = this.tracer.startSpan(`web_vital.${metric.name.toLowerCase()}`, {
        attributes: {
          'web_vital.name': metric.name,
          'web_vital.value': metric.value,
          'web_vital.rating': metric.rating,
          'web_vital.id': metric.id,
          'url.template': this.routeResolver(),
        },
      });
      span.end();
    };
    onLCP(reportVital);
    onINP(reportVital);
    onCLS(reportVital);

    window.addEventListener('error', (event) => {
      if (event.error) this.recordError(event.error, { 'error.source': 'window.onerror' });
    });

    window.addEventListener('unhandledrejection', (event) => {
      this.recordError(event.reason, { 'error.source': 'unhandledrejection' });
    });
  }

  public async withSpan<T>(
    name: string,
    attributes: Record<string, string | number | boolean>,
    fn: () => Promise<T>,
  ): Promise<T> {
    if (!this.enabled || !this.tracer) return fn();
    return this.tracer.startActiveSpan(name, { attributes }, async (span) => {
      try {
        return await fn();
      } catch (err) {
        span.recordException(err instanceof Error ? err : String(err));
        span.setStatus({ code: SpanStatusCode.ERROR });
        throw err;
      } finally {
        span.end();
      }
    });
  }

  public recordError(err: unknown, attributes: Record<string, string> = {}): void {
    if (!this.enabled || !this.tracer) return;
    const span = this.tracer.startSpan('browser.error', {
      attributes: { 'url.template': this.routeResolver(), ...attributes },
    });
    span.recordException(err instanceof Error ? err : String(err));
    span.setStatus({ code: SpanStatusCode.ERROR });
    span.end();
  }

  public async flush(): Promise<void> {
    if (this.enabled && this.provider) {
      await this.provider.forceFlush();
    }
  }
}

export const telemetry = new FrontendTelemetryFacade();
```

## 2. Vue 3 + Vue Router Wiring (`main.ts`)

```typescript
import { telemetry } from '@/telemetry';

telemetry.init({
  projectName: 'my-project',
  version: import.meta.env.VITE_APP_VERSION ?? '0.1.0',
  env: import.meta.env.MODE,
  resolveRouteTemplate: () => {
    const matched = router.currentRoute.value?.matched;
    return matched && matched.length > 0 ? matched[matched.length - 1].path : 'unmatched';
  },
});

app.config.errorHandler = (err, _instance, info) => {
  telemetry.recordError(err, { 'vue.error.info': info });
};
```

## 3. React + Vite + React Router / Astryx Wiring (`main.tsx`)

```tsx
import { createRoot } from 'react-dom/client';
import { matchRoutes } from 'react-router';
import { telemetry } from './telemetry';
import { routes } from './routes';

telemetry.init({
  projectName: 'my-project',
  version: import.meta.env.VITE_APP_VERSION ?? '0.1.0',
  env: import.meta.env.MODE,
  resolveRouteTemplate: () => {
    const matches = matchRoutes(routes, window.location.pathname);
    return matches?.map((m) => m.route.path).filter(Boolean).join('/') || 'unmatched';
  },
});

createRoot(document.getElementById('root')!, {
  onUncaughtError: (error, errorInfo) => {
    telemetry.recordError(error, { 'react.component_stack': errorInfo.componentStack ?? '' });
  },
  onCaughtError: (error, errorInfo) => {
    telemetry.recordError(error, { 'react.component_stack': errorInfo.componentStack ?? '' });
  },
});
```

## 4. Vite Dev Server Proxy (`vite.config.ts`)

```typescript
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
});
```
