---
name: jae-extract-design-tokens
description: Extracts hardcoded frontend design values into a zero-dependency two-tier CSS custom property token system with light/dark theme support across any web stack. Use when the user runs /jae-extract-design-tokens, /extract-design-tokens, /extract-tokens, or asks to extract design tokens.
---

# /jae-extract-design-tokens (/extract-design-tokens) Protocol

When triggered via `/jae-extract-design-tokens`, `/extract-design-tokens`, `/extract-tokens`, or "extract design tokens":

## 1. Directory Isolation & Zero-Dependency Rule
Locate the project's frontend source root (e.g., `src/`, `app/`, `frontend/src/`, `styles/`) and place all design tokens inside `<frontend_root>/design-tokens/` (default `src/design-tokens/`):
```text
<frontend_root>/design-tokens/
├── primitives.css      # Raw scales: colors, base spacing units, raw radii, shadows
├── semantic.css        # Intent aliases: surface, text, action states, layout spacing (+ dark theme overrides)
├── typography.css      # Font families, sizes, line heights, weights
├── index.css           # Single entry aggregator (@import primitives, semantic, typography)
└── DESIGN_TOKENS.md    # Developer & agent guide for applying and extending tokens
```
- **Zero-dependency rule:** Files inside `design-tokens/` MUST NOT import from React, Vue, Svelte, Angular, Astro, state stores, or application modules.
- Use native CSS custom properties (optionally generated from a pure `tokens.json` or bridged into Tailwind CSS v4 `@theme` if the repo uses Tailwind) so the token folder is portable across frameworks.

## 2. Two-Tier Token & Theming Contract
- **Primitive Tokens (`primitives.css`):** Map physical scales in `:root` (e.g., `--primitive-color-slate-900: #0f172a;`, `--primitive-space-4: 1rem;`).
- **Semantic Tokens (`semantic.css`):** Map usage intent to primitives in `:root` (e.g., `--surface-primary`, `--text-primary`, `--action-primary`, `--border-subtle`).
- **Theme Switching (If Repo Supports Dark Mode or Multi-Theme):** Override **only semantic tokens** inside `[data-theme="dark"]` (or `@media (prefers-color-scheme: dark)` / `.dark`), never duplicating component CSS.
- **Component Rule:** UI components (`.tsx`, `.jsx`, `.vue`, `.svelte`, `.astro`, `.html`, `.css`, `.scss`) MUST reference **semantic tokens only** (`var(--text-primary)`), never primitive tokens or raw color literals directly.

## 3. Audit & Refactor Workflow
1. Scan UI files across the detected frontend root for hardcoded colors (`#hex`, `rgb(`, `rgba(`, `hsl(`, `oklch(`), magic spacing values, font sizes/weights, shadows, and border radii.
2. Extract raw values into `primitives.css`, map semantic aliases (and dark-mode overrides if applicable) in `semantic.css`, and group typographic scales in `typography.css`.
3. Import `design-tokens/index.css` once at the detected application root entrypoint or global stylesheet (e.g., `src/main.tsx`, `src/main.ts`, `app/layout.tsx`, `src/app.css`, `index.html`).
4. Replace hardcoded values in component styles/stylesheets with semantic CSS variables (or Tailwind `@theme` tokens mapped to `var(--...)`).
5. **Verify Zero Leaks:** Run `rg -n "(#[0-9a-fA-F]{3,8}|rgba?\(|hsla?\()" <frontend_root> -g '!**/design-tokens/**' -g '!*.test.*'` and confirm zero unintended hardcoded color literals remain outside `design-tokens/`, then run the repo's build/typecheck/lint commands.

## 4. Documentation
Generate or update `<frontend_root>/design-tokens/DESIGN_TOKENS.md` documenting the token hierarchy, naming conventions, theme overrides, how to consume semantic variables in components, and how to extend or share the token package.
