# Backend OpenTelemetry Facade Reference (Rust + Axum + Tokio over OTLP/HTTP)

## 1. `Cargo.toml` Dependencies (`http-proto` + `reqwest`, No `tonic` Needed)

Use `opentelemetry-otlp` with `http-proto` and `reqwest-client` so Rust exports over OTLP/HTTP (`:4318`) and shares `reqwest` with the pass-through relay:

```toml
[dependencies]
axum = "0.8"
bytes = "1"
http = "1"
opentelemetry = "0.28"
opentelemetry_sdk = { version = "0.28", features = ["rt-tokio"] }
opentelemetry-otlp = { version = "0.28", default-features = false, features = ["trace", "metrics", "logs", "http-proto", "reqwest-client"] }
reqwest = { version = "0.12", default-features = false, features = ["rustls-tls"] }
tokio = { version = "1", features = ["full"] }
tracing = "0.1"
tracing-opentelemetry = "0.29"
tracing-subscriber = { version = "0.3", features = ["env-filter", "json"] }
```

## 2. Single Modular Facade & Bounded `mpsc` Relay (`src/telemetry/mod.rs`)

All `opentelemetry*` imports live inside `src/telemetry/mod.rs`. Handlers and services use only `crate::telemetry::Telemetry` or standard `tracing::info_span!` macros:

```rust
use axum::{
    body::Bytes,
    extract::{DefaultBodyLimit, Path, State},
    http::{HeaderMap, StatusCode},
    routing::post,
    Router,
};
use std::{env, sync::Arc, time::Duration};
use tokio::sync::mpsc;

pub struct RelayBatch {
    pub signal: String,
    pub body: Bytes,
    pub content_type: String,
    pub content_encoding: Option<String>,
}

#[derive(Clone)]
pub struct Telemetry {
    pub enabled: bool,
    tx: Option<mpsc::Sender<RelayBatch>>,
}

impl Telemetry {
    pub fn init(project_name: &str, version: &str, environment: &str) -> Self {
        let enabled = env::var("TELEMETRY_ENABLED")
            .unwrap_or_else(|_| "true".to_string())
            .eq_ignore_ascii_case("true");

        if !enabled {
            return Self { enabled: false, tx: None };
        }

        let otel_http_base = env::var("OTEL_EXPORTER_OTLP_ENDPOINT")
            .unwrap_or_else(|_| "http://otel-collector:4318".to_string());

        let (tx, mut rx) = mpsc::channel::<RelayBatch>(1000);
        let client = reqwest::Client::builder()
            .timeout(Duration::from_secs(5))
            .build()
            .expect("Failed to build reqwest client");
        let base_url = Arc::new(otel_http_base.trim_end_matches('/').to_string());

        tokio::spawn(async move {
            while let Some(batch) = rx.recv().await {
                let url = format!("{}/v1/{}", base_url, batch.signal);
                let mut req = client
                    .post(&url)
                    .header("Content-Type", batch.content_type)
                    .body(batch.body);
                if let Some(enc) = batch.content_encoding {
                    req = req.header("Content-Encoding", enc);
                }
                if let Err(err) = req.send().await {
                    tracing::warn!(signal = %batch.signal, error = %err, "OTel HTTP relay forward failed");
                }
            }
        });

        let _ = (project_name, version, environment);
        Self { enabled: true, tx: Some(tx) }
    }

    pub fn router(&self) -> Router {
        Router::new()
            .route("/api/telemetry/v1/{signal}", post(relay_handler))
            .layer(DefaultBodyLimit::max(512 * 1024)) // 512 KB cap
            .with_state(self.clone())
    }
}

async fn relay_handler(
    State(telemetry): State<Telemetry>,
    Path(signal): Path<String>,
    headers: HeaderMap,
    body: Bytes,
) -> StatusCode {
    if !matches!(signal.as_str(), "traces" | "metrics" | "logs") {
        return StatusCode::NOT_FOUND;
    }

    if !telemetry.enabled {
        return StatusCode::ACCEPTED;
    }

    let content_type = headers
        .get(axum::http::header::CONTENT_TYPE)
        .and_then(|v| v.to_str().ok())
        .unwrap_or("application/json")
        .split(';')
        .next()
        .unwrap_or("application/json")
        .trim()
        .to_ascii_lowercase();

    if content_type != "application/json" && content_type != "application/x-protobuf" {
        return StatusCode::UNSUPPORTED_MEDIA_TYPE;
    }

    let content_encoding = headers
        .get(axum::http::header::CONTENT_ENCODING)
        .and_then(|v| v.to_str().ok())
        .map(str::to_owned);

    if let Some(tx) = &telemetry.tx {
        let batch = RelayBatch {
            signal,
            body,
            content_type,
            content_encoding,
        };
        if tx.try_send(batch).is_err() {
            tracing::warn!("Telemetry relay channel full; dropping browser OTLP batch");
        }
    }

    StatusCode::ACCEPTED
}
```

## 3. Low-Cardinality `http.route` via `MatchedPath`

* In Axum middleware, always extract `matched_path: Option<axum::extract::MatchedPath>` and record `http.route = matched_path.as_ref().map(|m| m.as_str()).unwrap_or("UNMATCHED")`.
* Never pass `req.uri().path()` to metric attributes.
