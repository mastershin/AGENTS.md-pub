# Node / TypeScript

Repo `tsconfig.json` and oxlint config are the source of truth. Add them if missing, then use them.

- **Runtime:** org-approved Active or Maintenance LTS. Greenfield default: Node 24 Active LTS. Node 22 Maintenance LTS is acceptable until EOL. ESM only (`"type": "module"`).
- **Tools:** `oxlint`, `oxfmt`, `vitest`, `tsc`. Enable oxlint plugins `typescript`, `import`, `unicorn`.
- **`tsconfig` MUST include:** `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noPropertyAccessFromIndexSignature`, `verbatimModuleSyntax`, `isolatedModules`
- **Supply chain:** `pnpm` with frozen lockfile, exact versions (no `^` / `~`), `ignore-scripts`, `pnpm audit --audit-level=moderate`. 24h publish delay for new packages when the registry allows. Prefer the org npm proxy.
- **Tests:** colocate `*.test.ts`.
- **Do not** enable `postinstall` scripts, check in `node_modules`, or use `any` to silence the type checker.
