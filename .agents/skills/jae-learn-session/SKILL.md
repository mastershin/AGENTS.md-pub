---
name: jae-learn-session
description: Distills an edge case, user correction, or bug resolution into a concise, permanent rule in AGENTS.md or rules/.
---

# /jae-learn-session (/learn-session, /learn) Protocol: Session Distillation & Concurrent Rule Merging

When the user runs `/jae-learn-session`, `/learn-session`, `/learn`, or says "learn from this":

## 1. Synthesize Session Takeaways
Briefly summarize (3–5 bullets max) what was accomplished, debugged, or decided in the session:
- **Root Causes / Gotchas:** What broke, what the agent initially misjudged, or what environment quirk surfaced.
- **Architectural Decisions:** Key patterns, boundaries, or tool configurations locked in during this session.

## 2. Just-In-Time (JIT) Target Read (NEVER Overwrite)
**CRITICAL FOR PARALLEL SESSIONS:** Multiple parallel sessions may operate on the same project simultaneously. Never overwrite existing policy files (`AGENTS.md`, `docs/FEATURE_MAP.md`, or `rules/*.md`).
- Immediately before evaluating candidate rules, **re-read the target policy files directly from disk** to capture any rules appended or updated by parallel agent sessions while this session was running.

## 3. Run the Discoverability & Noise Gate
Evaluate every candidate takeaway against three strict filters using the freshly read policy files. **Drop any item that fails even one filter:**
1. **Static Discoverability Filter:** Can a fresh coding agent discover this in under 10 seconds on a new session by reading `pyproject.toml`, `package.json`, `compose.yaml`, `Makefile`, type definitions, or existing directory structure? *(If yes -> DROP).*
2. **Redundancy & Parallel-Session Filter:** Is this already covered in the freshly re-read `AGENTS.md`, `docs/FEATURE_MAP.md`, or `rules/<stack>.md` (including rules just added by another parallel session), or is it standard framework knowledge? *(If yes -> DROP).*
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
Map each surviving rule to its canonical target file (`rules/<stack>.md`, `docs/FEATURE_MAP.md`, or `AGENTS.md`—never inside `.cursor/`, `.github/`, or `.agents/`).
- **Inspect Target File for Existing Related Rules:**
  - Check if the target file already contains an existing rule or guideline covering the same tool, command, library, or pattern.
  - **If a related rule exists:** **Merge and synthesize.** Combine the new learning with the existing rule so the documentation remains unified, comprehensive, and single-source-of-truth, rather than creating disjointed or contradictory bullet points.
  - **If identical:** Skip (deduplicate).
  - **If net-new:** Identify the relevant section header to insert under.
- Present the proposed target file, merge target / section header, and the exact merged or new rule text to the user and wait for confirmation.

## 6. Atomic Locked Apply / Merge (Upon Confirmation)
**DO NOT use standard file-overwrite tools**, as they rely on stale in-memory file snapshots and will clobber concurrent writes from parallel sessions.
Instead, apply the confirmed rule by running this self-contained atomic lock script via your terminal/bash tool (works on both macOS and Linux). It safely handles merging with existing rules, inserting under section headers, or appending:

```bash
python3 - "TARGET_FILE_PATH" "TARGET_SECTION_HEADER_OR_EXISTING_RULE" "MERGED_OR_NEW_RULE_TEXT" << 'EOF'
import fcntl, pathlib, sys

target_path = pathlib.Path(sys.argv[1])
target_section_or_existing = sys.argv[2].strip()
new_or_merged_rule = sys.argv[3].strip()

lock_path = pathlib.Path("/tmp/repo_learn_session_skill.lock")
lock_path.touch(exist_ok=True)

with lock_path.open("r+") as lock_file:
    # Acquire exclusive OS-level lock (blocks if another parallel session is writing)
    fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
    try:
        content = target_path.read_text(encoding="utf-8") if target_path.exists() else ""

        # Deduplication check against concurrent session writes
        if new_or_merged_rule in content:
            print(f"SKIP: Rule already present in {target_path}")
            sys.exit(0)

        # 1. Merge into existing rule line if specified and found (not a section header)
        if target_section_or_existing and target_section_or_existing in content and not target_section_or_existing.startswith("#"):
            updated = content.replace(target_section_or_existing, new_or_merged_rule, 1)
            print(f"OK: Atomically merged into existing rule in {target_path}")
        # 2. Insert under target section header if specified and found
        elif target_section_or_existing and target_section_or_existing in content and target_section_or_existing.startswith("#"):
            idx = content.index(target_section_or_existing) + len(target_section_or_existing)
            next_line = content.find("\n", idx)
            insert_pos = next_line + 1 if next_line != -1 else len(content)
            updated = content[:insert_pos] + f"\n{new_or_merged_rule}\n" + content[insert_pos:]
            print(f"OK: Atomically inserted rule under section in {target_path}")
        # 3. Otherwise append cleanly
        else:
            sep = "\n" if content and not content.endswith("\n") else ""
            updated = f"{content}{sep}{new_or_merged_rule}\n"
            print(f"OK: Atomically appended rule to {target_path}")

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(updated, encoding="utf-8")
    finally:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
EOF
```
