# ROLE & CONTEXT
You are an expert developer workflow architect specializing in AI coding agent tooling, token efficiency, and project state persistence.

# GOAL
Scaffold a cross-agent session continuity workflow (`/resume-session`, `/close-session` / `/save-session`, and `/learn`) inside this repository so any coding agent (Cursor, VS Code, Antigravity, Claude Code) can summarize recent work, sync documentation, refresh feature maps, and generate a compact, low-token handoff file for future sessions.

# SPECIFIC TASKS TO EXECUTE

## 1. Scaffold Directories & Tracking Files
- Ensure the following directories exist:
  - `.agents/skills/`
  - `.cursor/rules/`
  - `.ai/`
  - `docs/`
- Initialize `.ai/session-handoff.md` with an empty skeleton template if it does not already exist.
- Initialize `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md` in the project root) if it does not already exist, structuring it with domain-sliced sections (Frontend, Backend, Design Tokens/Styles, Core Config).

## 2. Create `/close-session` (`/save-session`) Skill
Create `.agents/skills/close-session/SKILL.md` (and `.cursor/rules/close-session.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: close-session
description: Summarizes session progress, updates documentation, refreshes feature maps, and builds a compact handoff file for future sessions.
triggers:
  - "close session"
  - "save session"
  - "/close-session"
  - "/save-session"
globs: ""
alwaysApply: false
---

# Session Closer & State Compressor Protocol

When triggered by the user via "close session", "save session", "/close-session", or "/save-session", execute the following phases deterministically:

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

### Phase 4: Overwrite Session Handoff (`.ai/session-handoff.md`)
Overwrite `.ai/session-handoff.md` using the exact high-density template below. Keep the total file strictly under 350 words:

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

## 3. Create `/resume-session` Skill
Create `.agents/skills/resume-session/SKILL.md` (and `.cursor/rules/resume-session.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: resume-session
description: Seamlessly boots a fresh coding session using the project handoff, checks git state, and presents the next queued action.
triggers:
  - "resume session"
  - "/resume-session"
globs: ""
alwaysApply: false
---

# /resume-session Protocol

When the user runs `/resume-session` or says "resume session":

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

## 4. Create `/learn` Skill
Create `.agents/skills/learn/SKILL.md` (and `.cursor/rules/learn.mdc` if `.cursor` is used) with the following content:

```markdown
---
name: learn
description: Distills an edge case, user correction, or bug resolution into a concise, permanent rule in AGENTS.md or rules/.
triggers:
  - "/learn"
  - "learn from this"
globs: ""
alwaysApply: false
---

# /learn Protocol: Failure Autopsy & Rule Distillation

When the user runs `/learn` or says "learn from this":

1. **Trace the Correction:** Identify what failed or required correction in the current session and its technical root cause.
2. **Formulate Rule:** Write a 1–2 sentence constraint: *"When [context], DO NOT [anti-pattern]. Instead, ALWAYS [required action] because [reason]."*
3. **Persist:** Propose appending the rule to `rules/<stack>.md` or `AGENTS.md` and apply upon user confirmation.
```
