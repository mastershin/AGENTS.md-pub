---
name: jae-learn-session
description: Distills an edge case, user correction, or bug resolution into a concise, permanent rule in AGENTS.md, CLAUDE.md, rules/, or docs/FEATURE_MAP.md. Use when the user runs /learn-session, /jae-learn-session, /learn, says 'learn from this', or corrects a recurring mistake.
---

# /jae-learn-session (/learn-session, /learn) Protocol: Session Distillation & Concurrent Rule Merging

When the user runs `/jae-learn-session`, `/learn-session`, `/learn`, or says "learn from this":

## 1. Synthesize Session Takeaways
Briefly summarize (3–5 bullets max) what was accomplished, debugged, or decided in the session:
- **Root Causes / Gotchas:** What broke, what the agent initially misjudged, or what environment quirk surfaced.
- **Architectural Decisions:** Key patterns, boundaries, or tool configurations locked in during this session.

## 2. Just-In-Time (JIT) Target Read (NEVER Overwrite)
**CRITICAL FOR PARALLEL SESSIONS:** Multiple parallel sessions may operate on the same project simultaneously. Never overwrite existing policy files (`AGENTS.md`, `CLAUDE.md`, `docs/FEATURE_MAP.md`, or `rules/*.md`).
- Inspect which policy files actually exist in the current repository (e.g., `AGENTS.md`, `CLAUDE.md`, `rules/<stack>.md`, `docs/FEATURE_MAP.md`). Never edit generated adapter folders (`.cursor/`, `.github/`, `.agents/`) if a canonical root file exists.
- Immediately before evaluating candidate rules, **re-read the target policy files directly from disk** to capture any rules appended or updated by parallel agent sessions while this session was running.

## 3. Run the Discoverability & Noise Gate
Evaluate every candidate takeaway against three strict filters using the freshly read policy files. **Drop any item that fails even one filter:**
1. **Static Discoverability Filter:** Can a fresh coding agent discover this in under 10 seconds on a new session by reading `pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, `compose.yaml`, `Makefile`, type definitions, or existing directory structure? *(If yes -> DROP).*
2. **Redundancy & Parallel-Session Filter:** Is this already covered in the freshly re-read `AGENTS.md`, `CLAUDE.md`, `docs/FEATURE_MAP.md`, or `rules/<stack>.md` (including rules just added by another parallel session), or is it standard framework knowledge? *(If yes -> DROP).*
3. **Generalizability Filter:** Was this a one-off typo, transient network/container state, or ephemeral debugging step rather than a recurring repo invariant? *(If yes -> DROP).*

> **No-Op Exit:** If zero items survive the gate, explicitly output:
> *"No new persistent rules needed—everything from this session is either already documented (or recently added by a parallel session) or immediately discoverable from the codebase."* and **STOP**.

## 4. Distill Deterministic Rules (0 to 3 Max)
For items that survive the gate, formulate a concise rule (1–2 sentences maximum):
- **Correction / Anti-Pattern:**
  > **When [specific context or trigger], DO NOT [anti-pattern]. Instead, ALWAYS [required action] because [technical reason].**
- **Architectural / Workflow Invariant:**
  > **When [specific context or trigger], ALWAYS [required action / command / boundary] because [non-obvious constraint].**

## 5. Check for Merging with Existing Rules vs. Adding New
Map each surviving rule to its canonical target file in the current repo (`rules/<stack>.md` if `rules/` exists, `docs/FEATURE_MAP.md` for navigation paths, or `AGENTS.md` / `CLAUDE.md` otherwise).
- **Inspect Target File for Existing Related Rules:**
  - Check if the target file already contains an existing rule or guideline covering the same tool, command, library, or pattern.
  - **If a related rule exists:** **Merge and synthesize.** Combine the new learning with the existing rule so the documentation remains unified, comprehensive, and single-source-of-truth, rather than creating disjointed or contradictory bullet points.
  - **If identical:** Skip (deduplicate).
  - **If net-new:** Identify the exact Markdown section heading (`## ...` or `### ...`) to insert under.
- Present the proposed target file, merge target / section heading, and the exact merged or new rule text to the user and wait for confirmation.

## 6. Atomic Locked Apply / Merge (Upon Confirmation)
**DO NOT use standard file-overwrite tools**, as they rely on stale in-memory file snapshots and can clobber concurrent writes from parallel sessions.
Instead, run the bundled atomic merge helper (`scripts/merge_rule.py` inside this skill directory), which acquires a **per-repository lock** (`<git-common-dir>/jae-learn.lock` or a repo-hashed temp lock outside git), performs exact-line or exact-heading matching, and writes atomically via `os.replace()`:

```bash
python3 <skill_dir>/scripts/merge_rule.py \
  "<TARGET_FILE_PATH>" \
  "<EXACT_HEADING_OR_EXISTING_RULE_LINE>" \
  "<MERGED_OR_NEW_RULE_TEXT>"
```

- Pass `""` as the second argument to append cleanly to the end of `<TARGET_FILE_PATH>`.
- `<skill_dir>` is the directory containing this `SKILL.md` (for example `.agents/skills/jae-learn-session` or `skills/jae-learn-session`).
