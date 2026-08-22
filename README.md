# Agent rules

Enterprise and government agent policy, split so stack rules load by file type. Works with Cursor, VS Code / Copilot, Antigravity, Claude Code, Gemini CLI, and any tool that reads `AGENTS.md`.

Edit policy in **one place**. Adapters only attach it.

| Role | Path |
|------|------|
| Always-on (AAIF) | [`AGENTS.md`](./AGENTS.md) |
| Stack bodies | [`rules/`](./rules/) — `python`, `typescript`, `rust`, `shell`, `ci` |

Do not edit stack policy in tool folders. Change `AGENTS.md` or `rules/<stack>.md` only.

A compact single-file starter (no enterprise split) is in [`examples/greenfield.md`](./examples/greenfield.md).

## How tools load this

| Tool | Always-on | Stack (by glob) |
|------|-----------|-----------------|
| Any AGENTS.md agent (Codex, Cursor, Copilot Agent, Windsurf, Zed, Aider, Jules, …) | `AGENTS.md` | Read `rules/<stack>.md` when that stack is in play |
| VS Code / GitHub Copilot Chat | `AGENTS.md` + [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) | [`.github/instructions/*.instructions.md`](./.github/instructions/) (`applyTo`) |
| Cursor | `AGENTS.md` | [`.cursor/rules/*.mdc`](./.cursor/rules/) includes `rules/` |
| Antigravity | `AGENTS.md` + [`.agents/rules/`](./.agents/rules/) | glob `trigger` includes `rules/` |
| Claude Code | [`CLAUDE.md`](./CLAUDE.md) imports `AGENTS.md` | same as generic: `rules/` |
| Gemini CLI | [`GEMINI.md`](./GEMINI.md) points at `AGENTS.md` | same as generic: `rules/` |

Copy into another repo: `AGENTS.md`, `rules/`, and the adapter directories your team actually uses. `AGENTS.md` plus `rules/` is enough for a generic agent.
