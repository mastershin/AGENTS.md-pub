# /close-session (/save-session) Protocol

When triggered by the user via `/close-session`, `/save-session`, "close session", or "save session", execute the following phases deterministically:

## Phase 1: Inspect Changes
- Run `git status` and `git diff --stat` (or examine recently modified files).
- Identify core architectural decisions, patterns established, or bug resolutions completed during this session.

## Phase 2: Documentation Sync
- Update `README.md` if public CLI commands, dependencies, or high-level setups changed.
- Update relevant files in `docs/` (API contracts, schema notes, design token guidelines).

## Phase 3: Refresh Feature Map (`docs/FEATURE_MAP.md` or `FEATURE_MAP.md`)
- Scan any added, moved, or deleted modules in `src/` (components, backend routes, domain modules, token files).
- Update the feature map so file paths, boundaries, and shared dependencies remain accurate.
- Prune obsolete paths.

## Phase 4: Overwrite Session Handoff (`.ai/session-handoff.md`)
Ensure `.ai/` exists and overwrite `.ai/session-handoff.md` using the exact high-density template below. Keep the total file strictly under 350 words:

```markdown
# Session Handoff: [YYYY-MM-DD]

### 1. Completed in Last Session
- [Bullet points of exact accomplishments and resolved issues]

### 2. Current Architecture State & File Touchpoints
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order)
1. [Next concrete task]
2. [Follow-up task]

### 4. Critical Constraints & Gotchas
- [Subtle gotchas discovered during this session that the next agent must know]
```
