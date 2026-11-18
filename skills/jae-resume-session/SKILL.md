---
name: jae-resume-session
description: Seamlessly boots a fresh coding session using the project handoff, checks git state, and presents the next queued action.
---

# /jae-resume-session (/resume-session) Protocol

When the user runs `/jae-resume-session`, `/resume-session`, or says "resume session":

## Phase 1: Auto-Consolidate Pending Fragments (NEVER Overwrite Without Merging)
1. Check if any `.ai/sessions/*.md` files exist.
2. **If fragments exist:**
   - Read all `.ai/sessions/*.md` files AND the existing `.ai/session-handoff.md` (if present).
   - Merge them comprehensively into `.ai/session-handoff.md` using the master template below (strictly under 400 words):
     - **Completed Items & Aging:** Prune older accomplishments done a while back; retain only the last few (3–5) important completed highlights across active workstreams.
     - **Unfinished Tasks:** Retain all in-flight and pending tasks across all sessions. If the user explicitly dropped a feature, omit it; if moved to a TODO list, preserve it under `TODO.md` or `### 5. Backlog / Deferred (TODO)`.
     - **Touchpoints & Migrations:** Combine all active touchpoints and pending migrations.
     - **Constraints & Gotchas:** Deduplicate and consolidate active constraints.
   - Delete all merged `.ai/sessions/*.md` files once successfully consolidated so the folder stays clean.

```markdown
# Master Session Handoff: [YYYY-MM-DD]

### 1. Completed Accomplishments (Last Few Important)
- **[Workstream / Topic]:** [Concise summary of key accomplishment]
- [Retains only last 3–5 important completed highlights]

### 2. Active Touchpoints & Pending Migrations
- Key files recently modified: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Prioritized Task Queue (All In-Flight / Unfinished Tasks)
1. **[Workstream / Topic]:** [Top priority concrete unfinished task]
2. **[Workstream / Topic]:** [Next concrete unfinished task]

### 4. Active Constraints & Gotchas
- [Consolidated invariants and gotchas across all workstreams]

### 5. Backlog / Deferred (TODO)
- [Deferred items or tasks moved to TODO list per user request; omit if none]
```

3. **If no fragments exist:**
   - Read `.ai/session-handoff.md` directly. (If missing, fallback to `git log -5 --oneline`).
4. Read `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`) if present to load module boundaries.

## Phase 2: Environment & Git Drift Check
- Run `git status -s`, `git branch --show-current`, and `git log -3 --oneline`.
- Note any uncommitted changes or commits made after the last fragment/handoff timestamp.

## Phase 3: Morning Briefing
Output a concise brief:
1. **Recap & Git State:** 1–2 sentences on what was completed last cycle (and how many parallel fragments were merged), plus current branch and working tree status.
2. **Active Gotchas:** Bullet points of critical constraints.
3. **Task Queue:** Numbered list of next tasks, highlighting **Task 1**.
4. **Prompt:** Ask: *"Ready to start **Task 1**, or which workstream should this session focus on?"*
