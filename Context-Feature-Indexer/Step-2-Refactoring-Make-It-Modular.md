Use the `writing-plans` skill to design a safe, incremental modularization plan for this codebase. Do NOT move or edit code until I approve the plan.

**Objective:**
Reduce the number of files and directories we have to touch when adding, editing, or removing a feature. 

**Apply the Modularization Pattern that matches this project's stack:**

- **If PHP / Zen Cart / WordPress (Framework-Locked Directories):**
  - Do NOT break framework-required file paths (e.g., Zen Cart `includes/modules/`, `includes/templates/`, `includes/languages/` or WordPress hooks).
  - Instead, extract heavy inline business logic out of scattered templates/includes into self-contained domain classes/modules under a single custom namespace/folder (e.g., `includes/classes/domains/<feature>/` or `wp-content/mu-plugins/<feature>/`).
  - Keep framework template/hook files as ultra-thin 3-line wrappers that call the domain module, and document the exact 3–4 hook/template touchpoints per feature in `docs/FEATURE_MAP.md`.

- **If Vue.js / Frontend SPA:**
  - Keep `router/` or `pages/` as thin route definitions.
  - Consolidate feature-specific components, composables (`use*.ts`), API services, Pinia stores, and types into `src/features/<feature-name>/` with a single `index.ts` barrel export.
  - Keep `src/components/ui/` strictly for dumb, reusable UI primitives.

- **If Python (FastAPI / Django / Flask / Workers):**
  - Replace horizontal layers (`routers/`, `services/`, `models/`, `schemas/`) with domain packages (`src/domains/<feature_name>/` containing `router.py`, `service.py`, `models.py`, `schemas.py`, `__init__.py`).
  - Register domain routers/plugins centrally in the main app entrypoint.

**Deliverable:**
1. Identify the highest-friction "God files" or most scattered feature in the repo right now.
2. Propose a **Phase 1 Pilot Refactor** on ONE isolated feature to prove the pattern works without breaking builds or tests.
3. Show the exact before/after file tree and verification steps for Phase 1.
