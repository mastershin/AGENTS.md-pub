# ROLE & CONTEXT
You are an expert developer workflow architect specializing in AI coding agent tooling, token efficiency, and project state persistence.

# GOAL
Scaffold a cross-agent session continuity workflow (`/jae-resume-session` / `/resume-session`, `/jae-close-session` / `/close-session`, and `/jae-learn-session` / `/learn-session`) inside this repository so any coding agent (Cursor, VS Code, Antigravity, Claude Code) can summarize recent work, sync documentation, refresh feature maps, and generate a compact, low-token handoff file for future sessions.

# SPECIFIC TASKS TO EXECUTE

## 1. Scaffold Directories & Tracking Files
- Ensure the following directories exist:
  - `.agents/skills/`
  - `.cursor/rules/`
  - `.ai/`
  - `docs/`
- Initialize `.ai/session-handoff.md` with an empty skeleton template if it does not already exist.
- Initialize `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md` in the project root) if it does not already exist, structuring it with domain-sliced sections (Frontend, Backend, Design Tokens/Styles, Core Config).

## 2. Create `/jae-close-session` (`/close-session`, `/save-session`) Skill
Create `.agents/skills/jae-close-session/SKILL.md` (and `.cursor/rules/jae-close-session.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: jae-close-session
description: Summarizes session progress, updates documentation, refreshes feature maps, and builds a compact handoff file for future sessions.
triggers:
  - "/jae-close-session"
  - "close session"
  - "save session"
  - "/close-session"
  - "/save-session"
globs: ""
alwaysApply: false
---

# Session Closer & State Compressor Protocol

When triggered by the user via "/jae-close-session", "close session", "save session", "/close-session", or "/save-session", execute the following phases deterministically:

### Phase 1: Inspect Changes
- Run `git status` and `git diff --stat` (or examine recently modified files).
- Identify core architectural decisions, patterns established, or bug resolutions completed during this session.

### Phase 2: Documentation Sync
- Update `README.md` if public CLI commands, dependencies, or high-level setups changed.
- Update relevant files in `docs/` (API contracts, schema notes, design token guidelines).

### Phase 3: Refresh Feature Map (`docs/FEATURE_MAP.md` or `FEATURE_MAP.md`)
- Scan any added, moved, or deleted modules in `src/` (components, backend routes, token files).
- Update `FEATURE_MAP.md` so file paths, boundaries, and dependencies remain completely accurate.
- Prune obsolete paths.

### Phase 4: Read & Merge Session Handoff (`.ai/session-handoff.md`) — NEVER Overwrite
Multiple parallel sessions may operate on the same repository. Never blindly overwrite existing session handoffs.
1. Read `.ai/session-handoff.md` and any pending `.ai/sessions/*.md` fragments first.
2. Merge comprehensively:
   - **Completed accomplishments:** Prune older completed items done a while back; keep only the last 3–5 important highlights across active workstreams.
   - **Unfinished tasks (Zero Data-Loss):** Carry forward ALL pending/in-flight tasks from the existing handoff AND combine them with this session's next tasks. If user explicitly dropped a feature, drop it; if user asked to move tasks to a TODO list, preserve them in `TODO.md` or `### 5. Backlog / Deferred (TODO)`.
   - **Active touchpoints & gotchas:** Union of active touchpoints and deduplicated invariants.
3. Write back using the exact high-density template below (strictly under 350 words):

# Session Handoff: [YYYY-MM-DD]

### 1. Completed Accomplishments (Last Few Important)
- **[Workstream / Topic]:** [Concise summary of key accomplishment]
- [Retains only last 3–5 important completed highlights]

### 2. Current Architecture State & File Touchpoints
- Key files touched: `[path/to/file1]`, `[path/to/file2]`
- Breaking changes / Migrations pending: [None / Description]

### 3. Immediate Next Tasks (Priority Order — Unfinished Tasks Preserved)
1. **[Workstream / Topic]:** [Top priority concrete unfinished task]
2. **[Workstream / Topic]:** [Next concrete unfinished task]

### 4. Critical Constraints & Gotchas
- [Consolidated non-obvious invariants and gotchas across all workstreams]

### 5. Backlog / Deferred (TODO)
- [Deferred items or tasks moved to TODO list per user request; omit if none]
```

## 3. Create `/jae-resume-session` Skill
Create `.agents/skills/jae-resume-session/SKILL.md` (and `.cursor/rules/jae-resume-session.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: jae-resume-session
description: Seamlessly boots a fresh coding session using the project handoff, checks git state, and presents the next queued action.
triggers:
  - "/jae-resume-session"
  - "resume session"
  - "/resume-session"
globs: ""
alwaysApply: false
---

# /jae-resume-session Protocol

When the user runs `/jae-resume-session`, `/resume-session`, or says "resume session":

## 1. Context Ingestion
- Read `./.ai/session-handoff.md`. If it does not exist, inspect git log (`git log -3 --oneline`) and report no handoff found.
- Read `./docs/FEATURE_MAP.md` or `./FEATURE_MAP.md` if available to locate relevant subdirectories.

## 2. Environment Verification
- Run `git status -s` to ensure there are no unexpected uncommitted changes or branch divergences since last close.
- Verify existing branch and worktree.

## 3. Plan Presentation & Next Action
Output a brief:
1. **Recap:** 1–2 sentences summarizing what was accomplished in the previous session.
2. **Current Gotchas:** Call out any constraints listed under "Critical Constraints & Gotchas".
3. **Task Queue:** List the queued tasks from `.ai/session-handoff.md`, highlighting **Task 1**.
4. **Immediate Prompt:** Ask: *"Ready to proceed with Task 1: [Task Title], or would you like to re-prioritize?"*
```

## 4. Create `/jae-learn-session` Skill
Create `.agents/skills/jae-learn-session/SKILL.md` (and `.cursor/rules/jae-learn-session.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: jae-learn-session
description: Distills an edge case, user correction, or bug resolution into a concise, permanent rule in AGENTS.md or rules/.
triggers:
  - "/jae-learn-session"
  - "/learn-session"
  - "/learn"
  - "learn from this"
globs: ""
alwaysApply: false
---

# /jae-learn-session Protocol: Session Distillation & Concurrent Rule Merging

When the user runs `/jae-learn-session`, `/learn-session`, `/learn`, or says "learn from this":

1. **Trace the Correction:** Identify what failed or required correction in the current session and its technical root cause.
2. **Read Target First (Never Overwrite):** Re-read `AGENTS.md` and `rules/<stack>.md` directly from disk.
3. **Formulate Rule:** Write a 1–2 sentence constraint: *"When [context], DO NOT [anti-pattern]. Instead, ALWAYS [required action] because [reason]."*
4. **Check for Merging vs New Rule:**
   - If an existing rule already covers this tool or pattern, synthesize and merge into that rule in place rather than creating duplicate bullets.
   - If net-new, insert under the relevant section header without modifying unrelated rules.
5. **Atomic Persist:** Apply the rule using an atomic file lock script (`fcntl.flock`) upon user confirmation.
```
