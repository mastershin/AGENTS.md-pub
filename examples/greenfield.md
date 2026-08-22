# Compact greenfield rules

Single-file starter without the enterprise split. Agents do not load this file. Copy to `AGENTS.md` only if you want this compact baseline. The maintained policy is [`AGENTS.md`](../AGENTS.md) plus [`rules/`](../rules/).

## Core Philosophy

- **No speculative features** — Only add what users actively need
- **No premature abstraction** — Create utilities only after same code appears 3x
- **Clarity over cleverness** — Prefer explicit, readable code
- **Justify new dependencies** — Each dependency is attack surface and maintenance burden
- **No phantom features** — Don't document or validate features that aren't implemented
- **Replace, don't deprecate** — Remove old implementations entirely; flag dead code
- **Verify at every level** — Set up linters, type checkers, hooks as first step; prefer structure-aware tools (ast-grep, LSPs, compilers)
- **Bias toward action** — Decide and move for reversible changes; state assumptions clearly
- **Finish the job** — Handle edge cases; clean up touched code; don't invent new scope
- **Agent-native by default** — File-based state for transparency; prefer tools as atomic primitives

## Code Quality Standards

### Hard Limits

- ≤100 lines/function, cyclomatic complexity ≤8
- ≤5 positional params
- 100-char line length
- Absolute imports only (no `..` paths)
- Google-style docstrings on non-trivial public APIs

### Zero Warnings Policy

Fix every warning from linters, type checkers, compilers, tests. Use inline ignores with justification when unavoidable.

### Comments & Error Handling

- Code should be self-documenting; delete commented-out code
- Fail fast with clear, actionable messages
- Never swallow exceptions; include context (operation, input, suggested fix)

### Reviewing Code

Evaluate in order: architecture → code quality → tests → performance. Sync to latest remote (`git fetch origin`) before reviewing.

Describe issues concretely with file:line references, present options with tradeoffs when the fix isn't obvious, recommend one, and ask before proceeding.

### Testing Principles

- Test behavior, not implementation
- Test edges/errors, not just happy path
- Mock boundaries only (slow, non-deterministic, external services)
- Verify tests catch failures via mutation/property-based testing

---

## Development Stack

### CLI Tools

| Tool | Replaces | Usage |
|------|----------|-------|
| `rg` (ripgrep) | grep | `rg "pattern"` - 10x faster regex search |
| `fd` | find | `fd "*.py"` - fast file finder |
| `ast-grep` | - | AST-based code search for function calls, class definitions, imports |
| `shellcheck` / `shfmt` | - | Shell script lint/format |
| `actionlint` / `zizmor` | - | GitHub Actions lint/security |
| `prek` | pre-commit | `prek run` - fast git hooks (Rust, no Python) |
| `wt` | git worktree | `wt switch branch` - manage parallel worktrees |
| `trash` | rm | `trash file` - moves to macOS Trash (recoverable). **Never use `rm -rf`** |

Prefer `ast-grep` over ripgrep when searching for code structure. Use ripgrep for literal strings and log messages.

### Python

- **Runtime:** 3.14 with `uv venv`
- **Tools:** `uv` (deps), `ruff` (lint/format), `ty` (types), `pytest` (tests)
- **Supply chain:** `pip-audit`, pin exact versions (`==`), verify hashes with `uv pip install --require-hashes`
- **Config:** `ty` strictness via `[tool.ty.rules]` in pyproject.toml
- **Build:** `uv_build` (pure Python), `hatchling` (extensions)

Tests in `tests/` directory mirroring package structure.

### Node/TypeScript

- **Runtime:** Node 24 LTS, ESM only (`"type": "module"`)
- **Tools:** `oxlint` (lint), `oxfmt` (format), `vitest` (test), `tsc` (types)
- **Plugins:** Enable `typescript`, `import`, `unicorn` plugins in oxlint
- **tsconfig.json strictness:**
  ```jsonc
  "strict": true,
  "noUncheckedIndexedAccess": true,
  "exactOptionalPropertyTypes": true,
  "noImplicitOverride": true,
  "noPropertyAccessFromIndexSignature": true,
  "verbatimModuleSyntax": true,
  "isolatedModules": true
  ```
- **Supply chain:** `pnpm audit --audit-level=moderate`, pin exact versions (no `^` or `~`), 24h publish delay, block postinstall scripts

Colocated `*.test.ts` files.

### Rust

- **Runtime:** Latest stable via `rustup`
- **Tools:** `cargo` (build), `clippy` (lint), `fmt` (format), `test`
- **Supply chain:** `cargo deny check` (advisories, licenses, bans)
- **Safety:** `cargo careful test` (stdlib debug assertions + UB checks)
- **Style:** `for` loops with mutable accumulators, explicit destructuring, `let...else` for early returns
- **Types:** Newtypes over primitives, enums for state machines, `thiserror` (libs), `anyhow` (apps), `tracing` for logging
- **Optimization:** Write efficient code by default; profile before micro-optimizing

**Cargo.toml lints:**
```toml
[lints.clippy]
pedantic = { level = "warn", priority = -1 }
unwrap_used = "deny"
expect_used = "warn"
panic = "deny"
panic_in_result_fn = "deny"
unimplemented = "deny"
allow_attributes = "deny"
dbg_macro = "deny"
todo = "deny"
print_stdout = "deny"
print_stderr = "deny"
await_holding_lock = "deny"
large_futures = "deny"
exit = "deny"
mem_forget = "deny"
module_name_repetitions = "allow"
similar_names = "allow"
```

### Bash

All scripts must start with `set -euo pipefail`. Lint: `shellcheck script.sh && shfmt -d script.sh`

### GitHub Actions

- Pin actions to SHA hashes with version comments: `actions/checkout@<full-sha>  # vX.Y.Z` (use `persist-credentials: false`)
- Scan workflows with `zizmor` before committing
- Configure Dependabot with 7-day cooldowns and grouped updates
- Use `uv` ecosystem (not `pip`) for Python projects so Dependabot updates `uv.lock`

---

## Workflow

### Before Committing

1. Re-read changes for unnecessary complexity, redundant code, and unclear naming
2. Run relevant tests (not the full suite)
3. Run linters and type checker; fix all warnings

### Commit Guidelines

- Imperative mood, ≤72 char subject line, one logical change per commit
- Never amend/rebase commits already pushed to shared branches
- Never push directly to main — use feature branches and PRs
- Never commit secrets, API keys, or credentials — use `.env` files (gitignored) and environment variables

### Hooks & Worktrees

- Install `prek` in every repo (`prek install`). Run `prek run` before committing. Configure auto-updates: `prek auto-update --cooldown-days 7`
- Parallel subagents use separate worktrees (`wt switch <branch>`); never share working directories

### Pull Requests

- Describe **what the code does now** — not discarded approaches or iterations
- Use plain, factual language (avoid: critical, crucial, essential, significant, comprehensive, robust, elegant)
