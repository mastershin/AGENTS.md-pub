---
name: jae-resume-session
description: Boots a coding session by atomically consolidating pending session fragments into .ai/session-handoff.md, checking git drift, and presenting the next queued task. Use when the user runs /jae-resume-session, /resume-session, or says 'resume session'.
---

# /jae-resume-session (/resume-session) Protocol

When the user runs `/jae-resume-session`, `/resume-session`, or says "resume session":

## Phase 1: Snapshot & Consolidate Pending Fragments (Parallel-Safe)
1. Snapshot the exact list of existing `.ai/sessions/*.md` fragment file paths (sorted chronologically).
2. **If pending fragments exist:**
   - Read **only that snapshotted list** of `.ai/sessions/*.md` files AND the existing `.ai/session-handoff.md` (if present).
   - Merge them comprehensively into `.ai/session-handoff.md` using the master template below (**strictly under 400 words**):
     - **Completed Items & Aging:** Prune older accomplishments done a while back; retain only the last few (3–5) important completed highlights across active workstreams.
     - **Unfinished Tasks (Zero Data-Loss):** Retain all in-flight and pending tasks across all fragments and the prior handoff. Omit only items explicitly dropped by the user; preserve deferred items in `TODO.md` or `### 5. Backlog / Deferred (TODO)`.
     - **Touchpoints & Migrations:** Union all active touchpoints and pending migrations.
     - **Constraints & Gotchas:** Deduplicate and consolidate active constraints.
   - Write the consolidated `.ai/session-handoff.md` first, then remove **only the exact fragment paths snapshotted in Step 1** (never run a blind wildcard `rm .ai/sessions/*.md`, so any fragment written mid-merge by a concurrent session is preserved).

```markdown
# Master Session Handoff: [YYYY-MM-DD]

### 1. Completed Accomplishments (Last Few Important)
- **[Workstream / Topic]:** [Concise summary of key accomplishment]

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
   - Read `.ai/session-handoff.md` directly.
   - **First-run / greenfield fallback:** If neither `.ai/session-handoff.md` nor `.ai/sessions/` exists, inspect `README.md`, `AGENTS.md` / `CLAUDE.md`, and `git log -5 --oneline` (if in a git repo) and report that no prior handoff was found.
4. Read `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`) if present to load module boundaries in 1 hop.

## Phase 2: Environment & Git Drift Check
- If inside a git repository, run `git status -s`, `git branch --show-current`, and `git log -3 --oneline`.
- Note any uncommitted changes or commits made after the last fragment/handoff timestamp.

## Phase 3: Morning Briefing
Output a concise brief:
1. **Recap & Git State:** 1–2 sentences on what was completed last cycle (and how many fragments were merged), plus current branch and working tree status.
2. **Active Gotchas:** Bullet points of critical constraints.
3. **Task Queue:** Numbered list of next tasks, highlighting **Task 1**.
4. **Prompt:** Ask: *"Ready to start **Task 1**, or which workstream should this session focus on?"*
