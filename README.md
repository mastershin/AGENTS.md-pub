# Agent rules

Enterprise and government agent policy, split so stack rules load by file type. Works with Cursor, VS Code / Copilot, Antigravity, Claude Code, Gemini CLI, and any tool that reads `AGENTS.md`.

Edit policy in **one place**. Adapters only attach it.

| Role | Path |
|------|------|
| Always-on (AAIF) | [`AGENTS.md`](./AGENTS.md) |
| Stack bodies | [`rules/`](./rules/) — `python`, `typescript`, `rust`, `shell`, `ci` |
| On-demand skills | [`skills/`](./skills/) — `resume-session`, `close-session`, `learn`, `extract-design-tokens`, `map-features` |
| Bootstrap & refactor meta-prompts | [`prompts/`](./prompts/) & [`Context-Feature-Indexer/`](./Context-Feature-Indexer/) |

Do not edit stack policy or skills in tool folders. Change `AGENTS.md`, `rules/<stack>.md`, or `skills/<skill>.md` only.

A compact single-file starter (no enterprise split) is in [`examples/greenfield.md`](./examples/greenfield.md).

## How tools load this

| Tool | Always-on | Stack (by glob) | On-demand Skills |
|------|-----------|-----------------|------------------|
| Any AGENTS.md agent (Codex, Cursor, Copilot Agent, Windsurf, Zed, Aider, Jules, …) | `AGENTS.md` | Read `rules/<stack>.md` when that stack is in play | Read `skills/<skill>.md` |
| VS Code / GitHub Copilot Chat | `AGENTS.md` + [`.github/copilot-instructions.md`](./.github/copilot-instructions.md) | [`.github/instructions/*.instructions.md`](./.github/instructions/) (`applyTo`) | [`.github/prompts/*.prompt.md`](./.github/prompts/) |
| Cursor | `AGENTS.md` | [`.cursor/rules/*.mdc`](./.cursor/rules/) includes `rules/` | [`.cursor/rules/*.mdc`](./.cursor/rules/) (`alwaysApply: false`) |
| Antigravity | `AGENTS.md` + [`.agents/rules/`](./.agents/rules/) | glob `trigger` includes `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |
| Claude Code | [`CLAUDE.md`](./CLAUDE.md) imports `AGENTS.md` | same as generic: `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |
| Gemini CLI | [`GEMINI.md`](./GEMINI.md) points at `AGENTS.md` | same as generic: `rules/` | [`.agents/skills/*/SKILL.md`](./.agents/skills/) |

Copy into another repo: `AGENTS.md`, `rules/`, and the adapter directories your team actually uses. `AGENTS.md` plus `rules/` is enough for a generic agent.
