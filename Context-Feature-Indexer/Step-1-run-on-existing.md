Use your brainstorming and planning skills. Do NOT modify any application code yet.

**Objective:**
Agents are spending too many turns grepping and opening files across this repository to figure out how to add, edit, or remove features. I want to build a deterministic **Feature & Dependency Index (`docs/FEATURE_MAP.md`)** and wire it into `AGENTS.md` so future tasks locate the exact files in 1 hop.

**Step 1: Detect Stack & Structural Constraints**
Analyze the repository and classify the architecture:
- Identify the language/framework (e.g., PHP/Zen Cart/WordPress, Vue/TypeScript, Python/FastAPI, etc.).
- Identify **Framework-Locked Paths** (directories where files CANNOT be moved without breaking framework routing, template overrides, or autoloaders) vs. **Flexible Paths**.

**Step 2: Trace & Group into Vertical Feature Slices**
Instead of listing files by folder type (controllers, views, helpers, hooks), group the codebase into logical **Business/Functional Features**. For each feature, map its exact vertical footprint across the stack:
- **Entry Points:** (Routes, URL pages, CLI commands, cron jobs, or webhook handlers)
- **UI / Templates / Views:** (`.vue`, `.tsx`, `.php` template overrides, CSS/JS assets)
- **Business Logic & State:** (Services, controllers, composables/hooks, PHP classes/functions, Python modules)
- **Data & Persistence:** (Database tables, SQL queries, ORM models, Redis keys, config constants)
- **Tests & Verification:** (Exact test files and the command to run them in isolation)
- **Blast Radius (Shared Dependencies):** Files touched by this feature that are ALSO used by other features (critical to know before editing or deleting).

**Step 3: Create `docs/FEATURE_MAP.md` & Update `AGENTS.md`**
1. Generate `docs/FEATURE_MAP.md` containing the complete vertical feature map above, plus a **"How to Add / Remove a Feature"** checklist tailored to this specific framework.
2. Update root `AGENTS.md` with an `## Architectural Navigation Protocol` that forces all agents (and Superpowers skills) to:
   - **ALWAYS read `docs/FEATURE_MAP.md` first** before running `grep`, `glob`, or `find`.
   - Open only the files listed under the target feature slice.
   - Update `docs/FEATURE_MAP.md` in the same commit whenever a file is added, moved, or deleted.

Start by scanning the repo and presenting the detected stack constraints and the proposed list of Feature Slices for my approval.
