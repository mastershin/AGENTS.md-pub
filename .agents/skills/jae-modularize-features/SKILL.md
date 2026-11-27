---
name: jae-modularize-features
description: Designs and executes an incremental, strangler-safe refactor from horizontal layers or God files into self-contained vertical feature slices across any stack. Use when the user runs /jae-modularize-features, /modularize-features, /refactor-modular, or asks to modularize features.
---

# /jae-modularize-features (/modularize-features) Protocol: Vertical Slice Refactoring

When triggered via `/jae-modularize-features`, `/modularize-features`, `/refactor-modular`, or "modularize features":

## 1. Safety & Planning Gate (Do Not Move Code First)
Do NOT move or edit application code until the user approves the Phase 1 Pilot plan.
1. Read `docs/FEATURE_MAP.md` first if it exists (or run `/jae-map-features` discovery first) to identify framework-locked paths and shared blast-radius dependencies.
2. Identify the highest-friction "God files" or the most scattered feature in the repository right now.

## 2. Apply Stack-Specific Vertical Slice Pattern
Select the modularization pattern matching the project's stack (keep public/published contracts backward-compatible via thin re-export or strangler adapters until callers migrate):

- **Frontend SPA / Meta-Frameworks (React, Vue, Svelte, Next.js, Nuxt, Angular, Astro):**
  - Keep framework routing (`app/`, `pages/`, `routes/`, `router/`) as thin route wrappers.
  - Consolidate feature-specific components, hooks/composables (`use*.ts`), API clients, state stores (Pinia/Zustand/Redux slices), and types into `src/features/<feature-name>/` with a single public `index.ts` barrel export.
  - Keep `src/components/ui/` (or `src/ui/`) strictly for stateless, domain-agnostic UI primitives.

- **Python / Node / TypeScript Backends (FastAPI, Django, Flask, Express, NestJS, Fastify):**
  - Replace horizontal layers (`routers/`, `services/`, `models/`, `schemas/`) with self-contained domain packages (`src/domains/<feature_name>/` or `src/features/<feature_name>/` containing `router`, `service`, `models`/`repository`, `schemas`, and tests).
  - Register domain routers/modules centrally in the application entrypoint.

- **Rust Services & Libraries:**
  - Group domain logic into `src/features/<feature_name>/mod.rs` (or workspace crates for large repos) with private internal submodules and narrow `pub` exports in `mod.rs`.
  - Keep HTTP/CLI handlers thin adapters calling domain services.

- **Go Services:**
  - Use `internal/<feature_name>/` packages to enforce compiler-level encapsulation, keeping `cmd/<app>/` entrypoints and shared `pkg/` surface minimal.

- **Convention-Locked / Legacy Frameworks (PHP, Laravel, Rails, WordPress, Zen Cart):**
  - Do NOT move framework-required paths (e.g., Zen Cart `includes/modules/`, `includes/templates/`, `includes/languages/`, WordPress hook entrypoints, or Rails/Laravel convention directories).
  - Extract inline business logic into a dedicated domain namespace/directory (e.g., `app/Domains/<Feature>/`, `includes/classes/domains/<feature>/`, or `wp-content/mu-plugins/<feature>/`), leaving framework files as thin 1–5 line delegating adapters.

## 3. Enforce Slice Boundaries
Add or recommend lightweight automated boundary checks matching the stack so slices do not regress into spaghetti imports:
- **JS/TS:** `oxlint` / ESLint `no-restricted-imports` disallowing deep imports into `features/<other>/*` (require public `index.ts` only).
- **Python:** `import-linter` or `ruff` banned-api / module boundary rules.
- **Rust / Go:** Module visibility (`pub(crate)` vs private) and `internal/` package boundaries.

## 4. Deliverable: Phase 1 Pilot Refactor Plan
Present a concrete plan for user approval before touching code:
1. **Target Feature & Friction Points:** The single isolated feature selected for the Phase 1 pilot and the scattered files/God objects it currently spans.
2. **Before / After File Tree:** Exact source paths being extracted or thinned and the new vertical slice directory layout.
3. **Blast Radius, Adapters & Rollback:** Shared utilities, imports, autoloaders, or route registries affected, plus temporary re-export adapters if external callers exist.
4. **Verification Steps:** Exact build, typecheck, linter, and isolated test commands to prove zero regressions, followed by updating `docs/FEATURE_MAP.md`.
