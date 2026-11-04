# /learn Protocol: Failure Autopsy & Rule Distillation

When the user runs `/learn` or says "learn from this":

## 1. Trace the Correction
Inspect the recent turns in the conversation to identify:
- What the agent initially assumed, broke, or generated sub-optimally.
- How the user corrected the approach or what verification check failed.
- The root architectural or environment cause.

## 2. Distill a Deterministic Rule
Formulate a concise rule (1–2 sentences maximum) using this structure:
> **When [specific context or trigger], DO NOT [anti-pattern]. Instead, ALWAYS [required action] because [technical reason].**

## 3. Route to Canonical Policy
- **Language/Stack rule:** Target `rules/<stack>.md` (`python`, `typescript`, `rust`, `shell`, `ci`).
- **Feature/Path boundary:** Target `docs/FEATURE_MAP.md` (or `FEATURE_MAP.md`).
- **Repo-wide policy:** Target `AGENTS.md`.
- Never write rules directly into IDE adapter folders (`.cursor/`, `.github/`, `.agents/`); keep policy in the canonical source.

## 4. Confirm & Apply
Present the exact 1–2 line diff to the user and apply it upon confirmation.
