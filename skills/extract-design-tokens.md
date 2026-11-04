# /extract-design-tokens Protocol

When triggered via `/extract-design-tokens`, `/extract-tokens`, or "extract design tokens":

## 1. Directory Isolation & Zero-Dependency Rule
Place all design tokens strictly within `src/design-tokens/`:
```text
src/design-tokens/
├── primitives.css      # Raw scales: colors, base spacing units, raw radii, shadows
├── semantic.css        # Intent aliases: surface, text, action states, layout spacing
├── typography.css      # Font families, sizes, line heights, weights
├── index.css           # Single entry aggregator (@import primitives, semantic, typography)
└── DESIGN_TOKENS.md    # Developer & agent guide for applying and extending tokens
```
- **Zero-dependency rule:** Files inside `src/design-tokens/` MUST NOT import from Vue, Vue Router, Pinia/stores, or any application-specific modules.
- Use native CSS custom properties (and optionally a pure `tokens.json` source) so that moving `src/design-tokens/` into a standalone package or shared submodule requires zero code changes inside the token files.

## 2. Two-Tier Token Contract
- **Primitive Tokens:** Map physical scales (e.g., `--primitive-color-slate-900: #0f172a;`, `--primitive-space-4: 1rem;`).
- **Semantic Tokens:** Map usage intent to primitives (e.g., `--text-primary: var(--primitive-color-slate-900);`, `--action-primary: var(--primitive-color-indigo-600);`).
- **Component Rule:** UI components (`.vue`, `.tsx`, stylesheets) MUST reference **semantic tokens only**, never primitive tokens directly.

## 3. Audit & Refactor Workflow
1. Scan all `.vue` single-file components, stylesheets, and inline styles for hardcoded colors (hex, rgb, hsl), magic spacing values, font sizes/weights, shadows, and border radii.
2. Extract raw values into `primitives.css`, map semantic aliases in `semantic.css`, and group typographic scales in `typography.css`.
3. Import `src/design-tokens/index.css` once at the application root (`src/main.ts`).
4. Replace all hardcoded values in `<style>` blocks and utility classes with semantic CSS variables.
5. Verify that zero hardcoded color literals remain in any `.vue` file.

## 4. Documentation
Generate or update `src/design-tokens/DESIGN_TOKENS.md` documenting the token hierarchy, naming conventions, how to consume semantic variables in components, and how to theme or share the token package across projects.
