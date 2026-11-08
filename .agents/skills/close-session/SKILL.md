---
name: close-session
description: Summarizes session progress, updates documentation, refreshes feature maps, and builds a compact handoff file for future sessions.
---

# /close-session (/save-session) Protocol

When triggered by the user via `/close-session`, `/save-session`, "close session", or "save session", execute the following phases deterministically without asking for flags or parameters:

## Phase 1: Scoped Change Inspection
- Identify ONLY the files and modules modified within THIS session's conversation scope.
- Run `git status -s` and `git diff --stat` to verify workspace state, ignoring unrelated dirty files from other parallel sessions.
- Identify core architectural decisions, patterns established, or bug resolutions completed during this specific thread.

## Phase 2: Targeted Doc & Feature Map Sync
- Update `README.md` or `docs/` ONLY if this session changed public CLI commands, dependencies, API contracts, or schema notes.
- If this session added, moved, or deleted modules in `src/`, update those specific entries in `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`).

## Phase 3: Write Auto-Named Session Fragment
- Ensure `.ai/sessions/` exists.
- Auto-generate a unique filename using the current date, time (`HHMM`), and a 2–3 word kebab-case slug describing this session's work: `.ai/sessions/[YYYY-MM-DD]-[HHMM]-[topic-slug].md`.
- Write the file using the exact high-density template below (strictly under 200 words):

```markdown
# Session Fragment: [topic-slug] ([YYYY-MM-DD HH:MM])

### 1. Completed in This Session
- [Bullet points of exact accomplishments and resolved issues in this thread]

### 2. Scoped Touchpoints & Breaking Changes
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order)
1. [Next concrete task for this workstream]
2. [Follow-up task]

### 4. Critical Constraints & Gotchas
- [Subtle gotchas or non-obvious invariants discovered during this session]
```

## Phase 4: Confirm Close
- Output a 1-line confirmation: `Saved session state to .ai/sessions/[filename]. Ready to archive.`
