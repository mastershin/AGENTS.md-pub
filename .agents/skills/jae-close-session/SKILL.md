---
name: jae-close-session
description: Summarizes session progress, syncs docs and feature maps, and writes an append-only session fragment for parallel-safe handoffs. Use when the user runs /jae-close-session, /close-session, /save-session, or says 'close session' or 'save session'.
---

# /jae-close-session (/close-session, /save-session) Protocol

When triggered by the user via `/jae-close-session`, `/close-session`, `/save-session`, "close session", or "save session", execute the following phases deterministically without asking for flags or parameters:

## Phase 1: Scoped Change Inspection
- Identify ONLY the files and modules modified within THIS session's conversation scope.
- Run `git status -s` and `git diff --stat` (if inside a git repository), ignoring unrelated dirty files from other parallel sessions.
- Identify core architectural decisions, patterns established, or bug resolutions completed during this specific thread.

## Phase 2: Targeted Doc & Feature Map Sync
- Update `README.md` or `docs/` ONLY if this session changed public CLI commands, dependencies, API contracts, or schema notes.
- If `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`) exists and this session added, moved, or deleted modules across source roots (`src/`, `app/`, `pkg/`, `crates/`, `lib/`, `cmd/`, `services/`), update those specific entries and refresh its `<!-- synced: <git-short-sha> -->` header.

## Phase 3: Read Existing State First (Zero Data-Loss Context)
**CRITICAL FOR PARALLEL SESSIONS:** Multiple parallel sessions may run against a single repository. Never blindly overwrite `.ai/session-handoff.md` from one session when writing a fragment.
1. **Read Existing State:**
   - Check if `.ai/session-handoff.md` and any pending `.ai/sessions/*.md` fragments exist.
   - If present, **read them first** to avoid duplicating tasks already closed or overwriting active workstreams from parallel threads.
2. **Scoped Fragment Consolidation Rules:**
   - **Completed Accomplishments & Aging:** Keep only the **last few (3–5) most important completed highlights** from this session/workstream so handoffs stay lean.
   - **Unfinished Tasks (Zero Data-Loss):** Record all remaining in-flight or next tasks for this session.
     - **Exception 1 (User Dropped):** Omit tasks the user explicitly dropped.
     - **Exception 2 (Move to TODO List):** If the user asked to defer lower-priority tasks to a backlog, place them in `TODO.md` or under `### 5. Backlog / Deferred (TODO)`.
   - **Active Touchpoints & Gotchas:** Record scoped file touchpoints, pending migrations, and non-obvious invariants discovered in this session.

## Phase 4: Write Immutable, Collision-Free Session Fragment
- Ensure `.ai/sessions/` exists.
- If the repository uses `.gitignore` and `.ai/` is neither tracked by git nor ignored yet, append `.ai/` to `.gitignore` (ask first only if the team intentionally commits `.ai/`).
- Generate a unique, collision-free fragment filename using the current timestamp with seconds, a 4-character hex suffix, and a 2–3 word kebab-case topic slug:
  `.ai/sessions/[YYYY-MM-DD]-[HHMMSS]-[rand4]-[topic-slug].md`
- **Always write a new append-only fragment file** (never overwrite `.ai/session-handoff.md` directly during close; `/jae-resume-session` atomically consolidates all fragments at next boot) using the high-density template below (**strictly under 350 words**):

```markdown
# Session State: [topic-slug] ([YYYY-MM-DD HH:MM:SS])

### 1. Completed Accomplishments (Last Few Important)
- **[Workstream / Topic]:** [Concise summary of key accomplishment]

### 2. Scoped Touchpoints & Breaking Changes
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order — Unfinished Tasks Preserved)
1. **[Workstream / Topic]:** [Top priority concrete unfinished task]
2. **[Workstream / Topic]:** [Next concrete unfinished task]

### 4. Critical Constraints & Gotchas
- [Non-obvious invariants and gotchas discovered in this session]

### 5. Backlog / Deferred (TODO)
- [Deferred items or tasks moved to TODO list per user request; omit if none]
```

## Phase 5: Confirm Close
- Output a 1-line confirmation: `Saved session fragment .ai/sessions/<filename> (safe for parallel sessions).`
