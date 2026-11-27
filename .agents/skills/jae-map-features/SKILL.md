---
name: jae-map-features
description: Generates and incrementally maintains a compact docs/FEATURE_MAP.md grouping any repository into vertical feature slices for 1-hop file navigation. Use when the user runs /jae-map-features, /map-features, asks to 'update feature map', or needs to orient in an unfamiliar repo.
---

# /jae-map-features (/map-features) Protocol: Vertical Feature Indexer

When triggered via `/jae-map-features`, `/map-features`, or "update feature map":

## 0. Low-Token Discovery Rule (Do Not Read Full Codebase)
Build or update the map using minimum tokens:
1. Inspect top-level directory trees (`fd` / `find`) and project manifests/entry files (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml` / `build.gradle`, `composer.json`, `Gemfile`, `Makefile` / `justfile`), route definitions, and DB schemas first.
2. If `docs/FEATURE_MAP.md` already exists:
   - Check its top `<!-- synced: <git-short-sha> -->` marker. If present, run `git diff --name-status <sha>..HEAD` plus `git status -s` to update ONLY changed, moved, or deleted paths rather than re-scanning the repository.
3. Only read inside implementation files if imports or wiring cannot be inferred from filenames, manifests, or route definitions.

## 1. Detect Stack & Wiring Touchpoints
- **Stack & Conventions:** Primary language(s)/framework(s), routing/CLI/worker style, state/ORM/migration tools.
- **Framework-Locked Paths:** Directories/files that cannot move without breaking autoloading, file-based routing, or packaging.
- **Global Wiring Registries:** Exact file paths that MUST be edited when adding or removing a feature (e.g., main router, nav config, DI container, barrel exports, permissions/RBAC enum, CLI subcommand registry, env config).

## 2. Map Vertical Feature Slices
Group the repository by **Business/Functional Feature** (not folder layer). Keep entries strictly to file paths/globs—no prose explanations. For each slice, list only applicable layers:
- **Entry:** Route URLs, API endpoints, event topics, or CLI commands -> handler/page paths.
- **UI:** View/component paths or globs (omit for backend-only/CLI/library repos).
- **Logic:** Services, domain modules, hooks, stores, background jobs.
- **Data:** Models, DB tables, migrations, cache keys.
- **Tests:** Exact test paths + single-line run command.
- **Blast Radius:** Shared utilities, schemas, or models touched by this feature that affect other slices.

## 3. Write Compact `docs/FEATURE_MAP.md`
- **Sync Stamp:** Start the file with `<!-- synced: <git-short-sha> -->` (via `git rev-parse --short HEAD` when in git).
- **Format Constraints:** Use ultra-dense bullet lists or tables. Use glob patterns (`*`) when a folder belongs 100% to one feature. Keep total file size under 250 lines so reading the map costs minimal tokens.
- **Lifecycle Playbooks:** Include a concise step-by-step checklist for:
  - **Adding a Feature:** Exact boilerplate files to create + Global Wiring Registries to update.
  - **Removing a Feature:** Slice paths to delete + Global Wiring Registries to clean up + safe deprecation steps.
- **Prune Stale Paths:** Verify listed paths exist; remove dead links so future sessions resolve targets in 1 hop.

## 4. Wire Navigation Escalation Protocol
Ensure root `AGENTS.md` (or `CLAUDE.md` if the repo uses it) documents this low-context navigation order (append if missing):
1. **Map Before Search:** Read `docs/FEATURE_MAP.md` first for 1-hop feature-to-file resolution.
2. **Structure-Aware Escalation:** For multi-hop symbol callers, type definitions, or large monorepos (50K+ LOC), use `ast-grep` or a configured code-graph MCP server (e.g., `codebase-memory-mcp`) before falling back to broad `rg` / `fd` scans.
3. **Vertical Slice Isolation:** Keep feature logic colocated (`features/<name>/` or `domains/<name>/`), with framework-locked entrypoints kept as thin 1–5 line adapters.
4. **Self-Maintaining Index:** Update `docs/FEATURE_MAP.md` (and its `<!-- synced: ... -->` SHA) whenever features or files are added, moved, or deleted.
