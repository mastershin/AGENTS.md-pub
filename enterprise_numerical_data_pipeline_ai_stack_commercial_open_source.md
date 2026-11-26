# Enterprise Numerical Data Pipeline AI Stack (Commercial & Open Source)
### Built on IBM Docling for Exact Numerical Retrieval & Multi-Department Analytics

Covers both **open-source** and **commercial/enterprise** offerings for ingesting **financial/business tables, reports, fraud units, clinical/lab/trial metrics, and annotations/labels** with exact numerical fidelity.

> **Scale Tier Legend:**
> * **Tier 1 (Departmental):** $< 100\text{K}$ docs / $< 10\text{ GB}$ structured tables & facts
> * **Tier 2 (Mid-Enterprise):** $100\text{K} - 10\text{M}$ docs / $10\text{ GB} - 1\text{ TB}$
> * **Tier 3 (Global Enterprise):** $> 10\text{M}$ docs / $1\text{ TB} - 100\text{ TB}+$

---

## 1. Document Parsing, Normalization & Structured Extraction

| Tool | Type & License | GitHub / Official Link | Multi-Department Numerical Role | Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Docling](https://img.shields.io/badge/IBM-Docling-054ADA?style=flat-square&logo=ibm&logoColor=white) **IBM Docling** | Open Source (**MIT**) | [docling-project/docling](https://github.com/docling-project/docling) | Extracts tables, headers, captions, and structured elements from reports, financial filings, and trial/lab tables. | **Tier 1 – Tier 3** |
| ![LlamaParse](https://img.shields.io/badge/LlamaIndex-LlamaParse-7C3AED?style=flat-square) **LlamaParse** | Commercial API / LlamaCloud | [run-llama/llama_cloud_services](https://github.com/run-llama/llama_cloud_services) | High-precision layout/table parsing for complex multi-page financial, clinical, and dense tabular PDFs. | **Tier 1 – Tier 3** |
| ![Pydantic / Instructor](https://img.shields.io/badge/Pydantic%20%2F%20Instructor-Schemas-E92063?style=flat-square) **Pydantic & Instructor** | Open Source (**MIT**) | [pydantic/pydantic](https://github.com/pydantic/pydantic) | Enforces `Decimal` types, units, currencies, time periods, footnotes, and annotation labels on extracted rows. | **Tier 1 – Tier 3** |

---

## 2. Exact Numerical Storage, Analytical Warehouses & Text-to-SQL

| Tool | Type & License | GitHub / Official Link | Numerical Retrieval & Analytics Role | Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![PostgreSQL / DuckDB](https://img.shields.io/badge/Postgres%20%2F%20DuckDB-Exact%20SQL-4169E1?style=flat-square) **PostgreSQL & DuckDB** | Open Source (**PostgreSQL / MIT**) | [duckdb/duckdb](https://github.com/duckdb/duckdb) | Exact `NUMERIC`/`DECIMAL` fact tables, joins, and fast OLAP queries across finance, fraud, trial, and label metrics. | **Tier 1 – Tier 3** |
| ![Snowflake / BigQuery](https://img.shields.io/badge/Cloud%20DWH-Snowflake%20%2F%20BigQuery-29B5E8?style=flat-square) **Snowflake / Google BigQuery** | Commercial Enterprise SaaS | *(Commercial Cloud)* | Enterprise-wide exact SQL analytics, governed multi-department metrics, and audit/lineage at massive scale. | **Tier 2 – Tier 3** |
| ![Wren AI / Vanna](https://img.shields.io/badge/Text--to--SQL-Wren%20AI%20%2F%20Vanna-0EA5E9?style=flat-square) **Wren AI / Vanna** | Open Source + Commercial Enterprise | [Canner/WrenAI](https://github.com/Canner/WrenAI) | Translates natural-language numerical questions into semantic-layer SQL against structured fact/table schemas. | **Tier 1 – Tier 3** |

---

## 3. Deterministic Compute, Agents, Observability & Orchestration

| Category | Tool | Type & License | GitHub / Official Link | Role & Scale |
| :--- | :--- | :--- | :--- | :--- |
| **Deterministic Compute** | **Polars / Pandas + E2B** | OSS (**MIT/BSD/Apache**) + Cloud | [pola-rs/polars](https://github.com/pola-rs/polars) | Exact `Decimal`/DataFrame math, unit normalization, and sandboxed script execution (**Tier 1 – Tier 3**). |
| **Agent Orchestration** | **LangGraph / PydanticAI** | OSS (**MIT**) + Enterprise | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Routes numerical queries to SQL/Python tools and synthesizes cited answers (**Tier 1 – Tier 3**). |
| **Observability & Evals** | **Langfuse / LangSmith / Promptfoo** | OSS (**MIT**) & Commercial | [langfuse/langfuse](https://github.com/langfuse/langfuse) | Tracks SQL/tool traces, numerical accuracy benchmarks, and regression checks (**Tier 1 – Tier 3**). |
| **Orchestration** | **Temporal / Airflow / Prefect** | OSS (**MIT/Apache**) + Cloud | [temporalio/temporal](https://github.com/temporalio/temporal) | Durable ingestion, schema validation, and fact-table updates across departments (**Tier 1 – Tier 3**). |