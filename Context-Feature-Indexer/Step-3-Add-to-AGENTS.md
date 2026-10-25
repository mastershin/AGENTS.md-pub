## Universal Feature Indexing & Low-Context Protocol

1. **Map Before Search:**
   - Check if `docs/FEATURE_MAP.md` (or `FEATURE_INDEX.md`) exists.
   - If it exists, you MUST read it before running `grep`, `ripgrep`, `find`, or broad `glob` searches during `brainstorming` or `writing-plans`.
   - If it does NOT exist on an existing project with >20 files, offer to generate `docs/FEATURE_MAP.md` first.

2. **Vertical Slice Isolation:**
   - When adding or editing a feature, keep logic colocated in a single feature/domain module (`features/<name>/` or `domains/<name>/`).
   - In legacy or convention-locked frameworks (Zen Cart, WordPress, Pages Router) where entry files must live in specific framework directories, keep those framework files as thin 1–5 line adapters that delegate to a single self-contained feature class/module.

3. **Self-Maintaining Index:**
   - Any task that adds, renames, or removes a file or feature is INCOMPLETE until `docs/FEATURE_MAP.md` is updated to reflect the change.
