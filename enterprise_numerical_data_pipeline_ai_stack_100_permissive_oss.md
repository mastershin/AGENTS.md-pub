# Enterprise Numerical Data Pipeline AI Stack (100% Permissive Open Source)
### Built on IBM Docling for Exact Numerical Retrieval & Multi-Department Analytics

Designed for multi-department enterprises handling **financial/business tables, reports, fraud units, clinical/lab/trial metrics, and annotations/labels**, using **only 100% free, permissive open-source software (Apache 2.0, MIT, BSD-3-Clause, PostgreSQL)**.

> **Scale Tier Legend:**
> * **Tier 1 (Departmental):** $< 100\text{K}$ docs / $< 10\text{ GB}$ structured tables & facts
> * **Tier 2 (Mid-Enterprise):** $100\text{K} - 10\text{M}$ docs / $10\text{ GB} - 1\text{ TB}$
> * **Tier 3 (Global Enterprise):** $> 10\text{M}$ docs / $1\text{ TB} - 100\text{ TB}+$

---

## 1. Document Parsing, Unit/Footnote Preservation & Fact Normalization (Apache 2.0 / MIT)

| Layer & Tool | License | GitHub Repo | Multi-Department Numerical Role | Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Docling](https://img.shields.io/badge/IBM-Docling-054ADA?style=flat-square&logo=ibm&logoColor=white) **IBM Docling** | **MIT** | [docling-project/docling](https://github.com/docling-project/docling) | Preserves table grids, headers, captions, and layout hierarchy from PDFs, reports, and lab/trial tables into structured JSON/Markdown. | **Tier 1 – Tier 3** |
| ![Pydantic](https://img.shields.io/badge/Pydantic-Schema%20Validation-E92063?style=flat-square&logo=pydantic&logoColor=white) **Pydantic** | **MIT** | [pydantic/pydantic](https://github.com/pydantic/pydantic) | Validates extracted `Decimal` values, units (`$M`, `%`, `mg/dL`, fraud bps), dates, footnotes, and annotation label schemas before storage. | **Tier 1 – Tier 3** |
| ![Instructor](https://img.shields.io/badge/Instructor-Structured%20Extraction-10B981?style=flat-square) **Instructor** | **MIT** | [567-labs/instructor](https://github.com/567-labs/instructor) | Enforces structured Pydantic schemas during LLM normalization of messy table cells, footnotes, and clinical/fraud metrics. | **Tier 1 – Tier 3** |

---

## 2. Exact Numeric Storage, Analytical SQL & Deterministic Compute (Apache 2.0 / MIT / BSD / Postgres)

| Layer & Tool | License | GitHub Repo | Numerical Retrieval & Calculation Role | Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-NUMERIC%20%26%20pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL (`NUMERIC` + `pgvector`)** | **PostgreSQL** | [postgres/postgres](https://github.com/postgres/postgres) | Stores exact `NUMERIC`/`DECIMAL` fact rows (entity, metric, value, unit, period, source/footnote provenance) alongside metadata/embeddings. | **Tier 1 – Tier 3** |
| ![DuckDB](https://img.shields.io/badge/DuckDB-Analytical%20SQL-FFF000?style=flat-square&logo=duckdb&logoColor=black) **DuckDB** | **MIT** | [duckdb/duckdb](https://github.com/duckdb/duckdb) | Fast in-process OLAP SQL over Parquet/CSV/JSON fact tables for aggregations, cohort comparisons, and fraud/trial metric rollups. | **Tier 1 – Tier 3** |
| ![Pandas / Polars](https://img.shields.io/badge/Polars%20%26%20Pandas-Exact%20Math-2563EB?style=flat-square) **Polars & Pandas (`Decimal`)** | **MIT / BSD-3-Clause** | [pola-rs/polars](https://github.com/pola-rs/polars) | Deterministic Python calculations (ratios, deltas, unit conversions, label/annotation agreement metrics) instead of LLM mental math. | **Tier 1 – Tier 3** |
| ![E2B](https://img.shields.io/badge/E2B-Sandboxed%20Execution-F97316?style=flat-square) **E2B (OSS SDK/Infra)** | **Apache 2.0** | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | Isolated sandbox execution where agents run Python SQL/DataFrame scripts against exact numerical tables safely. | **Tier 1 – Tier 3** |

---

## 3. Text-to-SQL, Agent Routing, Evals & Pipeline Orchestration (Apache 2.0 / MIT)

| Category | Tool | License | GitHub Repo | Role & Scale |
| :--- | :--- | :--- | :--- | :--- |
| **Agent & Tool Routing** | **PydanticAI / LangGraph** | **MIT** | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | Routes numerical questions to SQL/Python tools vs. prose/document search (**Tier 1 – Tier 3**). |
| **Numeric & RAG Evals** | **Promptfoo & Ragas** | **MIT / Apache 2.0** | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Verifies exact numerical answers, SQL accuracy, and citation faithfulness in CI/CD (**Tier 1 – Tier 3**). |
| **Workflow Orchestration** | **Prefect / Apache Airflow / Temporal** | **Apache 2.0 / MIT** | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | Schedules Docling ingestion, schema validation, fact-table refreshes, and retries (**Tier 1 – Tier 3**). |