# /resume-session Protocol

When the user runs `/resume-session` or says "resume session":

## 1. Context Ingestion
- Read `./.ai/session-handoff.md`. If it does not exist, inspect git log (`git log -3 --oneline`) and report no handoff found.
- Read `./docs/FEATURE_MAP.md` (or `./FEATURE_MAP.md`) if available to locate relevant subdirectories in 1 hop.

## 2. Environment Verification
- Run `git status -s` and `git branch --show-current` to check for unexpected uncommitted changes or branch divergences since last close.
- Verify the active branch and git worktree state.

## 3. Plan Presentation & Next Action
Output a concise brief:
1. **Recap:** 1–2 sentences summarizing what was accomplished in the previous session.
2. **Current Gotchas:** Call out any constraints listed under "Critical Constraints & Gotchas".
3. **Task Queue:** List the queued tasks from `.ai/session-handoff.md`, highlighting **Task 1**.
4. **Immediate Prompt:** Ask: *"Ready to proceed with Task 1: [Task Title], or would you like to re-prioritize?"*
