# /close-session (/save-session) Protocol (Parallel-Safe)

When triggered by the user via `/close-session`, `/save-session`, "close session", or "save session", execute the following phases deterministically:

## Phase 1: Scoped Change Inspection
- Identify ONLY the files and modules modified within THIS session's conversation scope.
- Run `git status -s` and `git diff --stat` to verify workspace state, but filter out unrelated dirty files from parallel sessions if sharing a working tree.
- Identify core architectural decisions, patterns established, or bug resolutions completed during this specific thread.

## Phase 2: Write Scoped Session Fragment (Collision-Free)
- Ensure `.ai/sessions/` exists.
- Generate a short, descriptive slug for this session's focus (e.g., `auth-refactor`, `ota-vertical-slice`, `db-migration`).
- Write `.ai/sessions/[YYYY-MM-DD]-[slug].md` using the exact high-density template below. Keep the fragment strictly under 200 words:

```markdown
# Session Fragment: [slug] ([YYYY-MM-DD HH:MM])

### 1. Completed in This Thread
- [Bullet points of exact accomplishments and resolved issues in this session only]

### 2. Scoped Touchpoints & Breaking Changes
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Thread-Specific Next Tasks (Priority Order)
1. [Next concrete task for this workstream]
2. [Follow-up task]

### 4. Critical Constraints & Gotchas
- [Subtle gotchas or non-obvious invariants discovered during this session that future agents must know]
```

## Phase 3: Conditional Global Sync & Compaction
Determine whether to run a local fragment save only or a full project consolidation:
- **If the user specifies `--fragment` (or notes other parallel sessions are still actively running):**
  - Stop after Phase 2. Do NOT overwrite global handoff files or prune `FEATURE_MAP.md` yet to avoid race conditions with active parallel agents.
- **If this is a standalone session, the final parallel session closing, or the user specifies `--consolidate` / "close all":**
  1. **Read All Fragments:** Scan all existing `.ai/sessions/*.md` files (including the one just created) and the previous `.ai/session-handoff.md`.
  2. **Documentation Sync:** Update `README.md` if public CLI commands, dependencies, or high-level setups changed. Update relevant files in `docs/` (API contracts, schema notes, design token guidelines).
  3. **Refresh Feature Map (`docs/FEATURE_MAP.md` or `FEATURE_MAP.md`):** Scan added, moved, or deleted modules in `src/` across all completed sessions. Update file paths, boundaries, and shared dependencies; prune obsolete paths.
  4. **Synthesize Master Handoff:** Overwrite `.ai/session-handoff.md` by merging all active `.ai/sessions/*.md` fragments into the canonical template below (keep strictly under 400 words):

```markdown
# Session Handoff: [YYYY-MM-DD]

### 1. Completed Across Recent Sessions
- **[Workstream/Slug A]:** [Summary of accomplishments & resolved issues]
- **[Workstream/Slug B]:** [Summary of accomplishments & resolved issues]

### 2. Current Architecture State & File Touchpoints
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order)
1. [Next concrete task]
2. [Follow-up task]

### 4. Critical Constraints & Gotchas
- [Combined gotchas discovered across sessions that the next agent must know]
```

  5. **Clean Up Fragments:** Delete the processed `.ai/sessions/*.md` files that were merged into `.ai/session-handoff.md` so the directory starts clean for the next cycle.
