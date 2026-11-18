---
name: jae-close-session
description: Summarizes session progress, updates documentation, refreshes feature maps, and builds a compact handoff file for future sessions.
---

# /jae-close-session (/close-session, /save-session) Protocol

When triggered by the user via `/jae-close-session`, `/close-session`, `/save-session`, "close session", or "save session", execute the following phases deterministically without asking for flags or parameters:

## Phase 1: Scoped Change Inspection
- Identify ONLY the files and modules modified within THIS session's conversation scope.
- Run `git status -s` and `git diff --stat` to verify workspace state, ignoring unrelated dirty files from other parallel sessions.
- Identify core architectural decisions, patterns established, or bug resolutions completed during this specific thread.

## Phase 2: Targeted Doc & Feature Map Sync
- Update `README.md` or `docs/` ONLY if this session changed public CLI commands, dependencies, API contracts, or schema notes.
- If this session added, moved, or deleted modules in `src/`, update those specific entries in `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`).

## Phase 3: Read Existing State First (NEVER Overwrite)
**CRITICAL FOR PARALLEL SESSIONS:** Multiple parallel sessions may run against a single project. Never blindly overwrite existing session handoffs or state files.
1. **Read Existing Documents:**
   - Check if `.ai/session-handoff.md` and any existing `.ai/sessions/*.md` fragments exist.
   - If present, **read them first** to understand active workstreams, touchpoints, and queued tasks from parallel sessions or previous cycles.
2. **Merge Comprehensively:**
   - **Completed Accomplishments & Aging:**
     - Prune older completed items that were done a while back to keep the document lean and avoid token bloat.
     - Retain only the **last few (3–5) most important completed items** across recent cycles/workstreams, and merge in this session's accomplishments.
   - **Unfinished Tasks (Zero Data-Loss Guarantee):**
     - **ALWAYS preserve unfinished tasks:** Carry forward all pending, in-flight, or next tasks from the existing handoff AND combine them with this session's next tasks.
     - **Exception 1 (User Dropped):** If the user explicitly stated they don't want a feature or task, drop it.
     - **Exception 2 (Move to TODO List):** If the user asked to move items to a TODO list (or if lower-priority/backlog tasks should be deferred to keep the immediate queue focused), move them to `TODO.md` (or a dedicated `### 5. Backlog / Deferred (TODO)` section) instead of leaving them in the immediate task queue or deleting them.
   - **Active Touchpoints & Migrations:** Merge file touchpoints and pending migrations (preserve active touchpoints from other parallel threads).
   - **Constraints & Gotchas:** Merge non-obvious gotchas and constraints, deduplicating identical entries and preserving invariants discovered across all sessions.

## Phase 4: Write Auto-Named Session Fragment or Merged Handoff
- Ensure `.ai/sessions/` exists.
- Auto-generate a unique filename using the current date, time (`HHMM`), and a 2–3 word kebab-case slug describing this session's work: `.ai/sessions/[YYYY-MM-DD]-[HHMM]-[topic-slug].md`.
- Write the fragment (or update `.ai/session-handoff.md` if operating in consolidated mode) using the exact high-density template below (strictly under 350 words):

```markdown
# Session State: [topic-slug] ([YYYY-MM-DD HH:MM])

### 1. Completed Accomplishments (Last Few Important)
- **[Workstream / Topic]:** [Concise summary of key accomplishment]
- [Keep only last 3–5 important completed highlights; pruned older completed items]

### 2. Scoped Touchpoints & Breaking Changes
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order — Unfinished Tasks Preserved)
1. **[Workstream / Topic]:** [Top priority concrete unfinished task]
2. **[Workstream / Topic]:** [Next concrete unfinished task]

### 4. Critical Constraints & Gotchas
- [Consolidated non-obvious invariants and gotchas across sessions]

### 5. Backlog / Deferred (TODO)
- [Deferred items or tasks moved to TODO list per user request; omit if none]
```

## Phase 5: Confirm Close
- Output a 1-line confirmation: `Saved session state (merged with existing context). Ready to archive.`
