# ROLE & CONTEXT
You are an expert developer workflow architect specializing in AI coding agent tooling, token efficiency, and project state persistence.

# GOAL
Install and wire the canonical `jae-*` session, navigation, refactoring, design-token, and observability skills into the target repository so any coding agent (Antigravity, Cursor, VS Code / GitHub Copilot, Claude Code, Gemini CLI, Codex) shares one single source of truth with zero duplicated skill bodies.

# SPECIFIC TASKS TO EXECUTE

## 1. Scaffold Directories & Ignore Rules
- Ensure the following directories exist in the target repository:
  - `.agents/skills/`
  - `.ai/sessions/`
  - `docs/`
- Ensure `.ai/` is listed in `.gitignore` unless the repository intentionally tracks session handoffs in git.
- Initialize `docs/FEATURE_MAP.md` only if missing (populate it in Step 4 via `/jae-map-features`).

## 2. Sync Canonical Skills (Single Source of Truth)
Copy the canonical skill folders from `AGENTS.md-pub/skills/jae-*/` (including `SKILL.md`, `scripts/`, and `references/`) into `.agents/skills/` (or `skills/` + `.agents/skills/` if the repository separates canonical sources from tool adapters):
- `jae-resume-session` — snapshots & atomically consolidates `.ai/sessions/*.md` fragments into `.ai/session-handoff.md`
- `jae-close-session` — writes immutable `.ai/sessions/YYYY-MM-DD-HHMMSS-<rand4>-<slug>.md` fragments
- `jae-learn-session` — runs the 3-stage Discoverability & Noise Gate and persists rules via `scripts/merge_rule.py` (per-repo `flock` + `os.replace`)
- `jae-map-features` — maintains `docs/FEATURE_MAP.md` with `<!-- synced: <sha> -->` incremental diffing
- `jae-modularize-features` — stack-agnostic vertical-slice refactoring with boundary checks
- `jae-extract-design-tokens` — framework-agnostic two-tier CSS custom property tokens + theme overrides
- `jae-implement-otel-observability` — modular single-facade OTLP/HTTP (`:4318`) instrumentation

> **Never duplicate skill bodies** inside `.cursor/rules/` or `.github/prompts/`. If the repository uses Cursor or GitHub Copilot, create thin adapter files only:
> - `.cursor/rules/jae-<name>.mdc` (`alwaysApply: false`) pointing to `@../../.agents/skills/jae-<name>/SKILL.md` (or `@../../skills/jae-<name>/SKILL.md`)
> - `.github/prompts/jae-<name>.prompt.md` linking to `[jae-<name> skill](../../.agents/skills/jae-<name>/SKILL.md)`

## 3. Wire Root Policy Entrypoint
Ensure root `AGENTS.md` (and `CLAUDE.md` / `GEMINI.md` if used) includes a concise pointer telling agents:
1. Read `docs/FEATURE_MAP.md` before broad `rg` / `fd` searches; escalate to `ast-grep` or a code-graph MCP server for multi-hop call chains.
2. Run `/jae-resume-session` at session start if `.ai/session-handoff.md` or `.ai/sessions/` exists, `/jae-close-session` before ending, and `/jae-learn-session` when a non-obvious repo invariant surfaces.

## 4. Bootstrap `docs/FEATURE_MAP.md`
Run the `/jae-map-features` discovery workflow once against the target repository so future sessions navigate in 1 hop.
