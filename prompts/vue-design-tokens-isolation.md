# ROLE & CONTEXT
You are an expert Frontend Architect specializing in Vue.js, design systems, and modular CSS architecture. We are running a Vue.js frontend with a Python backend.

# GOAL
Extract all hardcoded design values (colors, spacing, typography, radii, shadows) into a centralized, zero-dependency Design Token architecture located inside the project, strictly prepared for future extraction into an independent repository or shared npm package.

# DIRECTIVES & ARCHITECTURE

## 1. Directory Isolation
- Place all design tokens strictly within: `src/design-tokens/`
- **Zero-dependency rule:** Files in `src/design-tokens/` must NEVER import anything from Vue, Vue Router, Pinia/stores, or any app-specific components/utilities.
- Use standard CSS custom properties (and optionally a pure `tokens.json` source) so that no framework-specific bundler plugins are required.

## 2. File Structure to Establish
Create the following layout:
```text
src/design-tokens/
├── primitives.css      # Raw scales: colors, base spacing units, raw radii
├── semantic.css        # Intent aliases: surface, text, action states, card padding
├── typography.css      # Font sizes, line heights, weights
├── index.css           # Single entry aggregator (@import primitives, semantic, typography)
└── DESIGN_TOKENS.md    # Guide for developers/agents on how to use and update tokens
```

## 3. Two-Tier Token Contract
- **Primitives** map to physical values (e.g., `--primitive-color-slate-900: #0f172a;`).
- **Semantics** map to primitives (e.g., `--text-primary: var(--primitive-color-slate-900);`, `--action-primary: var(--primitive-color-indigo-600);`).
- Vue components must reference **SEMANTIC** tokens only, never primitive tokens directly.

## 4. Refactor & Hook Up
- Import `src/design-tokens/index.css` once at the application root (`src/main.ts`).
- Audit all `.vue` single-file components and stylesheets.
- Replace all hardcoded hex/rgb/hsl values, magic spacing values, and hardcoded border radii with the corresponding semantic CSS variables.
- Ensure zero hardcoded colors remain in any `.vue` file.

## 5. Verification
- Confirm that moving the `src/design-tokens/` folder out of the repository in the future will require zero code changes inside the token files themselves.
