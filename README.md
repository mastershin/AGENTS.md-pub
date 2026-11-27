# Agent rules

Enterprise and government agent policy, split so stack rules load by file type, plus enterprise AI architecture reference guides. Works with Cursor, VS Code / Copilot, Antigravity, Claude Code, Gemini CLI, and any tool that reads `AGENTS.md`.

Edit policy in **one place**. Adapters only attach it.

| Role | Path |
|------|------|
| Always-on (AAIF) | [`AGENTS.md`](./AGENTS.md) |
| Stack bodies | [`rules/`](./rules/) — [`python`](./rules/python.md), [`typescript`](./rules/typescript.md), [`rust`](./rules/rust.md), [`shell`](./rules/shell.md), [`ci`](./rules/ci.md) |
| On-demand skills | [`skills/`](./skills/) — [`jae-resume-session`](./skills/jae-resume-session/SKILL.md), [`jae-close-session`](./skills/jae-close-session/SKILL.md), [`jae-learn-session`](./skills/jae-learn-session/SKILL.md), [`jae-extract-design-tokens`](./skills/jae-extract-design-tokens/SKILL.md), [`jae-implement-otel-observability`](./skills/jae-implement-otel-observability/SKILL.md), [`jae-map-features`](./skills/jae-map-features/SKILL.md), [`jae-modularize-features`](./skills/jae-modularize-features/SKILL.md) |
| Bootstrap & refactor meta-prompts | [`prompts/`](./prompts/) — [`install-session-skills`](./prompts/install-session-skills.md), [`vue-design-tokens-isolation`](./prompts/vue-design-tokens-isolation.md), [`vue-design-tokens-refactor`](./prompts/vue-design-tokens-refactor.md) |
| Compact single-file starter | [`examples/greenfield.md`](./examples/greenfield.md) |
| Architecture & AI stack guides | See [Reference Guides](#reference-guides) below |

Do not edit stack policy or skills in tool folders. Change `AGENTS.md`, `rules/<stack>.md`, or `skills/<skill>/SKILL.md` only.

## Reference Guides

Enterprise AI stack and domain architecture blueprints, each maintained in a **Commercial & Open Source** edition and a **100% Permissive Open Source** edition.

| Topic | Commercial & Open Source | 100% Permissive Open Source |
|-------|--------------------------|-----------------------------|
| **Enterprise AI Ecosystem (2026)** — LLMs, inference, RAG, agents, observability, graph DBs, ontologies, and enterprise context layers | [`enterprise_ai_ecosystem_commercial_and_open_source.md`](./enterprise_ai_ecosystem_commercial_and_open_source.md) | [`enterprise_ai_ecosystem_open_source.md`](./enterprise_ai_ecosystem_open_source.md) |
| **Enterprise Numerical Data Pipeline AI Stack** — IBM Docling, exact `NUMERIC`/`Decimal` storage, text-to-SQL, deterministic compute, and evals | [`enterprise_numerical_data_pipeline_ai_stack_commercial_open_source.md`](./enterprise_numerical_data_pipeline_ai_stack_commercial_open_source.md) | [`enterprise_numerical_data_pipeline_ai_stack_100_permissive_oss.md`](./enterprise_numerical_data_pipeline_ai_stack_100_permissive_oss.md) |
| **Clinical Imaging & EHR AI Architecture** — HL7/FHIR + PACS/DICOM operational triage vs. analytics/research pipelines | [`clinical_ops_analytics_commercial.md`](./clinical_ops_analytics_commercial.md) | [`clinical_ops_analytics_oss.md`](./clinical_ops_analytics_oss.md) |

## All Canonical Markdown Documents

- **Core Policy & Tool Entry Points:** [`AGENTS.md`](./AGENTS.md), [`CLAUDE.md`](./CLAUDE.md), [`GEMINI.md`](./GEMINI.md), [`examples/greenfield.md`](./examples/greenfield.md)
- **Stack Rules:** [`rules/python.md`](./rules/python.md), [`rules/typescript.md`](./rules/typescript.md), [`rules/rust.md`](./rules/rust.md), [`rules/shell.md`](./rules/shell.md), [`rules/ci.md`](./rules/ci.md)
- **Skills:**
  - [`skills/jae-resume-session/SKILL.md`](./skills/jae-resume-session/SKILL.md)
  - [`skills/jae-close-session/SKILL.md`](./skills/jae-close-session/SKILL.md)
  - [`skills/jae-learn-session/SKILL.md`](./skills/jae-learn-session/SKILL.md)
  - [`skills/jae-extract-design-tokens/SKILL.md`](./skills/jae-extract-design-tokens/SKILL.md)
  - [`skills/jae-implement-otel-observability/SKILL.md`](./skills/jae-implement-otel-observability/SKILL.md) (references: [`backend-python-fastapi.md`](./skills/jae-implement-otel-observability/references/backend-python-fastapi.md), [`backend-rust-axum.md`](./skills/jae-implement-otel-observability/references/backend-rust-axum.md), [`frontend-vue-react-vite.md`](./skills/jae-implement-otel-observability/references/frontend-vue-react-vite.md))
  - [`skills/jae-map-features/SKILL.md`](./skills/jae-map-features/SKILL.md)
  - [`skills/jae-modularize-features/SKILL.md`](./skills/jae-modularize-features/SKILL.md)
- **Meta-Prompts:** [`prompts/install-session-skills.md`](./prompts/install-session-skills.md), [`prompts/vue-design-tokens-isolation.md`](./prompts/vue-design-tokens-isolation.md), [`prompts/vue-design-tokens-refactor.md`](./prompts/vue-design-tokens-refactor.md)
- **Reference Guides:** [`enterprise_ai_ecosystem_commercial_and_open_source.md`](./enterprise_ai_ecosystem_commercial_and_open_source.md), [`enterprise_ai_ecosystem_open_source.md`](./enterprise_ai_ecosystem_open_source.md), [`enterprise_numerical_data_pipeline_ai_stack_commercial_open_source.md`](./enterprise_numerical_data_pipeline_ai_stack_commercial_open_source.md), [`enterprise_numerical_data_pipeline_ai_stack_100_permissive_oss.md`](./enterprise_numerical_data_pipeline_ai_stack_100_permissive_oss.md), [`clinical_ops_analytics_commercial.md`](./clinical_ops_analytics_commercial.md), [`clinical_ops_analytics_oss.md`](./clinical_ops_analytics_oss.md)

## How tools load this

| Tool | Always-on | Stack (by glob) | On-demand Skills |
|------|-----------|-----------------|------------------|
| Any AGENTS.md agent (Codex, Cursor, Copilot Agent, Windsurf, Zed, Aider, Jules, …) | `AGENTS.md` | Read `rules/<stack>.md` when that stack is in play | Read `skills/<skill>/SKILL.md` |
| VS Code / GitHub Copilot Chat | `AGENTS.md` + [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) | [`.github/instructions/*.instructions.md`](./.github/instructions/) (`applyTo`) | [`.github/prompts/*.prompt.md`](./.github/prompts/) |
| Cursor | `AGENTS.md` | [`.cursor/rules/*.mdc`](./.cursor/rules/) includes `rules/` | [`.cursor/rules/*.mdc`](./.cursor/rules/) (`alwaysApply: false`) |
| Antigravity | `AGENTS.md` + [`.agents/rules/`](./.agents/rules/) | glob `trigger` includes `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |
| Claude Code | [`CLAUDE.md`](./CLAUDE.md) imports `AGENTS.md` | same as generic: `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |
| Gemini CLI | [`GEMINI.md`](./GEMINI.md) points at `AGENTS.md` | same as generic: `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |

Copy into another repo: `AGENTS.md`, `rules/`, and the adapter directories your team actually uses. `AGENTS.md` plus `rules/` is enough for a generic agent.
