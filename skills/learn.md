# /learn Protocol: Session Distillation & Concurrent Rule Extraction

When the user runs `/learn` or says "learn from this":

## 1. Synthesize Session Takeaways
Briefly summarize (3–5 bullets max) what was accomplished, debugged, or decided in the session:
- **Root Causes / Gotchas:** What broke, what the agent initially misjudged, or what environment quirk surfaced.
- **Architectural Decisions:** Key patterns, boundaries, or tool configurations locked in during this session.

## 2. Just-In-Time (JIT) Target Sync
**CRITICAL FOR PARALLEL SESSIONS:** Never rely on earlier in-context snapshots of `AGENTS.md`, `docs/FEATURE_MAP.md`, or `rules/*.md`.
- Immediately before evaluating candidate rules, **re-read the target policy files directly from disk** to capture any rules appended by parallel agent sessions while this session was running.

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

## 5. Route & Preview Diff
Map each surviving rule to its canonical source (`rules/<stack>.md`, `docs/FEATURE_MAP.md`, or `AGENTS.md`—never inside `.cursor/`, `.github/`, or `.agents/`).
- Present the proposed target file, section header (optional), and exact rule text to the user and wait for confirmation.

## 6. Atomic Locked Apply (Upon Confirmation)
**DO NOT use standard file-overwrite or IDE edit tools**, as they rely on stale in-memory file snapshots and will clobber concurrent writes from parallel sessions.
Instead, apply the confirmed rule by running this self-contained atomic lock script via your terminal/bash tool (works on both macOS and Linux):

```bash
python3 - "TARGET_FILE_PATH" "## TARGET_SECTION_HEADER" "EXACT_RULE_BULLET" << 'EOF'
import fcntl, pathlib, sys

target_path = pathlib.Path(sys.argv[1])
section_header = sys.argv[2].strip()
new_rule = sys.argv[3].strip()

lock_path = pathlib.Path("/tmp/repo_learn_skill.lock")
lock_path.touch(exist_ok=True)

with lock_path.open("r+") as lock_file:
    # Acquire exclusive OS-level lock (blocks if another parallel session is writing)
    fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
    try:
        content = target_path.read_text(encoding="utf-8") if target_path.exists() else ""

        # Deduplication check against concurrent session writes
        if new_rule in content:
            print(f"SKIP: Rule already present in {target_path}")
            sys.exit(0)

        # Insert under target section header if specified and found; otherwise append to EOF
        if section_header and section_header in content:
            idx = content.index(section_header) + len(section_header)
            next_Line = content.find("\n", idx)
            insert_pos = next_Line + 1 if next_Line != -1 else len(content)
            updated = content[:insert_pos] + f"\n{new_rule}\n" + content[insert_pos:]
        else:
            sep = "\n" if content and not content.endswith("\n") else ""
            updated = f"{content}{sep}{new_rule}\n"

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(updated, encoding="utf-8")
        print(f"OK: Atomically appended rule to {target_path}")
    finally:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
EOF
