# /map-features Protocol: Vertical Feature Indexer

When triggered via `/map-features` or "update feature map":

## 0. Low-Token Discovery Rule (Do Not Read Full Codebase)
Build or update the map using minimum tokens:
1. Inspect directory trees (`fd`/`find`), `package.json`/`composer.json`, route definitions, and DB schemas first.
2. If `docs/FEATURE_MAP.md` already exists, use `git status` or `git diff --name-status` to update only changed/deleted paths rather than re-scanning the repository.
3. Only read inside implementation files if imports/wiring cannot be inferred from filenames or route definitions.

## 1. Detect Stack & Wiring Touchpoints
- **Stack & Conventions:** Primary framework, routing style, state/ORM tools.
- **Framework-Locked Paths:** Directories/files that cannot move without breaking autoloading or routing.
- **Global Wiring Registries:** Exact file paths that MUST be edited when adding or removing a feature (e.g., main router file, nav menu config, DI container, barrel exports, permissions enum, env config).

## 2. Map Vertical Feature Slices
Group the repository by **Business/Functional Feature** (not folder layer). Keep entries strictly to file paths/globs—no prose explanations. For each slice, list:
- **Entry:** Route URLs/CLI commands -> controller/page paths.
- **UI:** View/component paths or globs (e.g., `src/components/checkout/*`).
- **Logic:** Services, hooks, stores, jobs, domain modules.
- **Data:** Models, DB tables, migrations, cache keys.
- **Tests:** Exact test paths + single-line run command.
- **Blast Radius:** Shared utilities/models touched by this feature that affect other slices.

## 3. Write Compact `docs/FEATURE_MAP.md`
- **Format Constraints:** Use ultra-dense bullet lists or tables. Use glob patterns (`*`) when a folder belongs 100% to one feature. Keep total file size under 250 lines so reading the map costs minimal tokens.
- **Lifecycle Playbooks:** Include a concise step-by-step checklist for:
  - **Adding a Feature:** Exact boilerplate files to create + Global Wiring Registries to update.
  - **Removing a Feature:** Slice paths to delete + Global Wiring Registries to clean up + safe migration/deprecation steps.
- **Prune Stale Paths:** Verify listed paths exist; remove dead links so future sessions resolve targets in 1 hop without running broad `rg` or `fd` searches.
