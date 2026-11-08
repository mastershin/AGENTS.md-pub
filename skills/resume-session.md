# /resume-session Protocol

When the user runs `/resume-session` or says "resume session":

## Phase 1: Auto-Consolidate Pending Fragments
1. Check if any `.ai/sessions/*.md` files exist.
2. **If fragments exist:**
   - Read all `.ai/sessions/*.md` files AND the existing `.ai/session-handoff.md` (if present).
   - Merge them into a single, updated `.ai/session-handoff.md` using the master template below (strictly under 400 words, pruning completed tasks and combining active workstreams).
   - Delete all merged `.ai/sessions/*.md` files so the folder is clean.

```markdown
# Master Session Handoff: [YYYY-MM-DD]

### 1. Completed in Last Cycle
- **[Workstream Slug]:** [Concise summary of completed work]

### 2. Active Touchpoints & Pending Migrations
- Key files recently modified: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Prioritized Task Queue
1. **[Workstream Slug]:** [Top priority concrete task]
2. **[Workstream Slug]:** [Next concrete task]

### 4. Active Constraints & Gotchas
- [Consolidated gotchas that current sessions must respect]
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
