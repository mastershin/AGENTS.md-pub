# ROLE & CONTEXT
You are an expert Frontend Architect specializing in Vue.js, design systems, and component modularity. We are working in a stack with a Vue.js frontend and a Python backend.

# TASK
Refactor the Vue.js frontend to completely eliminate hardcoded design values. Abstract all visual styling into a centralized, scalable Design Token system using standard CSS custom properties. The goal is to create a single source of truth for our design language that can be easily updated and shared across multiple projects.

# SPECIFIC DIRECTIVES

## 1. Audit & Extract
- Scan all `.vue` components, stylesheets, and inline styles.
- Identify every hardcoded color (hex, rgb, hsl), typography value (font-sizes, weights), spacing value (margins, paddings), and shadow/border radius.

## 2. Build the Token System
- Create a centralized token repository (`src/design-tokens/` using native CSS variables, or integrated with the project's utility CSS config).
- Implement a two-tier token architecture:
  - **Primitive Tokens:** Base values (e.g., `--primitive-color-blue-600: #2563EB;`)
  - **Semantic Tokens:** Meaningful usage intent (e.g., `--color-primary-action: var(--primitive-color-blue-600);`)

## 3. Refactor Vue Components
- Replace all hardcoded values in `<style>` blocks or utility classes with references to the new semantic design tokens.
- Ensure absolutely NO hardcoded colors remain in any `.vue` file.

## 4. Enable Cross-Project Sharing
- Structure the token configuration so it is completely isolated from business logic and the Python backend.
- Organize the files so they can be easily extracted into a shared Git submodule, npm package, or monorepo workspace for use in other projects.

## 5. Documentation
- Generate a `DESIGN_TOKENS.md` file explaining the architecture, how to apply the tokens in new Vue components, and how to update the core theme to ensure visual consistency across projects.
