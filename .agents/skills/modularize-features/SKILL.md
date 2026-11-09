---
name: modularize-features
description: Designs and executes an incremental refactor from horizontal layers or scattered framework files into self-contained vertical feature/domain slices.
---

# /modularize-features Protocol: Vertical Slice Refactoring

When triggered via `/modularize-features`, `/refactor-modular`, or "modularize features":

## 1. Safety & Planning Gate (Do Not Move Code First)
Do NOT move or edit application code until the user approves the Phase 1 Pilot plan.
1. Read `docs/FEATURE_MAP.md` first if it exists (or run `/map-features` discovery first) to identify framework-locked paths and shared blast-radius dependencies.
2. Identify the highest-friction "God files" or the most scattered feature in the repository right now.

## 2. Apply Stack-Specific Vertical Slice Pattern
Select the modularization pattern matching the project's stack:

- **Convention-Locked / Legacy Frameworks (PHP, Zen Cart, WordPress, Pages Router):**
  - Do NOT move or break framework-required paths (e.g., Zen Cart `includes/modules/`, `includes/templates/`, `includes/languages/`, or WordPress hook entrypoints).
  - Extract heavy inline business logic out of scattered templates/includes into self-contained domain modules under a single custom namespace/directory (e.g., `includes/classes/domains/<feature>/` or `wp-content/mu-plugins/<feature>/`).
  - Keep framework template/hook files as thin 1–5 line adapters that delegate to the domain module, and record the exact touchpoints in `docs/FEATURE_MAP.md`.

- **Frontend SPA (Vue, React, TypeScript):**
  - Keep `router/` or `pages/` as thin route definitions.
  - Consolidate feature-specific components, composables/hooks (`use*.ts`), API clients, stores (Pinia/Zustand), and types into `src/features/<feature-name>/` with a single `index.ts` barrel export.
  - Keep `src/components/ui/` strictly for stateless, reusable UI primitives.

- **Backend Services (Python / FastAPI / Django / Flask / Workers):**
  - Replace horizontal layers (`routers/`, `services/`, `models/`, `schemas/`) with self-contained domain packages (`src/domains/<feature_name>/` containing `router.py`, `service.py`, `models.py`, `schemas.py`, `__init__.py`).
  - Register domain routers/plugins centrally in the main application entrypoint.

## 3. Deliverable: Phase 1 Pilot Refactor Plan
Present a concrete plan for user approval before touching code:
1. **Target Feature & Friction Points:** The single isolated feature selected for the Phase 1 pilot and the scattered files/God objects it currently spans.
2. **Before / After File Tree:** Exact source paths being extracted or thinned and the new vertical slice directory layout.
3. **Blast Radius & Wiring:** Shared utilities, imports, autoloaders, or route registries affected.
4. **Verification Steps:** Exact build, typecheck, and isolated test commands to prove the refactor introduces zero regressions, followed by updating `docs/FEATURE_MAP.md`.
