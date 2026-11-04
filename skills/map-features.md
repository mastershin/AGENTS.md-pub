# /map-features Protocol: Vertical Feature Indexer

When triggered via `/map-features` or "update feature map":

## 1. Detect Stack & Structural Constraints
- Identify the project's primary stack and framework conventions.
- Distinguish **Framework-Locked Paths** (files that cannot move without breaking routing, autoloaders, or template overrides) from **Flexible Domain Paths**.

## 2. Map Vertical Feature Slices
Group the repository by **Business/Functional Features** rather than horizontal folder layers. For each feature slice, record:
- **Entry Points:** Routes, pages, CLI commands, jobs, or webhooks.
- **UI / Views:** Components (`.vue`, `.tsx`, templates, styles).
- **Business Logic & State:** Services, composables, stores, domain modules.
- **Data & Persistence:** Database tables, models, schemas, cache keys.
- **Tests & Verification:** Exact test file paths and isolated test command.
- **Blast Radius (Shared Dependencies):** Files touched by this feature that are also used by other features.

## 3. Write `docs/FEATURE_MAP.md`
- Create or update `docs/FEATURE_MAP.md` with the vertical slice index and a concise **"How to Add / Remove a Feature"** checklist.
- Prune deleted or moved file paths so future sessions locate target files in 1 hop before running broad `rg` or `fd` searches.
