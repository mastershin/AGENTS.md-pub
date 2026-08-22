# Agent Rules

Apply unless a more specific project file (`AGENTS.md` in a nested repo, `CODEOWNERS`, security policy, approved-software list) overrides them.

**Precedence:** (1) law, classification, and org security policy, (2) MUST rules here, (3) project config and stack rules, (4) SHOULD guidance. Security and data handling win conflicts.

RFC 2119: **MUST** / **MUST NOT** / **SHOULD** / **MAY**. Treat SHOULD as required when the cheap, safe path exists.

**Stack rules** live in [`rules/`](rules/) (`python`, `typescript`, `rust`, `shell`, `ci`). Read the matching file before changing that stack. Cursor, VS Code, and Antigravity adapters only *attach* those files by glob — they are not a second source of truth. Repo config (`pyproject.toml`, `tsconfig.json`, `clippy.toml`, CI) is the source of truth for tool settings; do not fork those into chat.

Ask and stop before: production changes, irreversible data loss, crypto/authz design, new network egress, or classified / CUI / PHI / PII / regulated data.

---

## Security (MUST)

- **No secrets** in git, logs, traces, errors, or agent state. Use the org secret manager / KMS. `.env` is local-only and gitignored, not a production store. Redact credentials, tokens, session IDs, and personal data at the source.
- **Do not** weaken TLS, skip certificate verification, set `InsecureSkipVerify`, or `curl | bash`. Fetch installers only from the org allowlist or an attested internal mirror.
- **Do not** open inbound ports, add firewall exceptions, or send telemetry to third parties unless the project already does so under an approved ATO / privacy review.
- **Authenticate and authorize at every trust boundary.** Deny by default. Parameterize queries; never concatenate SQL, shell, LDAP, or untrusted paths. Validate and canonicalize untrusted input; never use it in file paths or commands without an allowlist.
- **Do not invent crypto.** Use platform TLS and vetted libraries. In FIPS / FedRAMP / DoD environments, use only approved modules. Store passwords with a memory-hard KDF; never reversibly encrypt them.
- **Least privilege:** CI tokens, cloud IAM, container users (non-root), file modes, database roles. Prefer OIDC over long-lived PATs.
- **Pin the supply chain.** Commit lockfiles. Pin dependencies to exact versions and verify hashes when the package manager supports it. Prefer the org artifact proxy. Generate an SBOM (CycloneDX or SPDX) for released artifacts. No copyleft or unlicensed deps in proprietary products without Legal. SCA and secret scanning (`gitleaks` or equivalent) run in hooks/CI and fail closed.
- **Classify data before storing or logging it.** CUI / PHI / PII / payment data need encryption in transit and at rest, retention limits, and audit logs. Do not move government data to unsanctioned SaaS, personal accounts, or public AI features.
- **Log security-relevant events** (authn, authz failures, admin actions, data exports) with correlation IDs. Structured logs only; no secrets or unnecessary personal data.

**Human gates:** production deploys, schema/data migrations, IAM or network policy, dependency or license exceptions, disabling a control (linter, test, scanner, signature), and any break-glass path.

---

## Change control

- Published APIs, schemas, event contracts, and CLI flags **MUST** be deprecated, not silently replaced. Internal-only dead code SHOULD be removed in the same change.
- Bias toward action only for **local, reversible** work. Shared, released, or production-facing work needs a branch, review, and the project's change process.
- **Do not** amend, rebase, or force-push commits that exist on a shared remote. Do not push to `main` / protected branches.
- If classification, network, or baseline is unclear, ask. Do not guess "it's fine."

---

## Architecture

- One module, one reason to change. Depend on interfaces, not implementations. Keep I/O, policy, and domain logic in separate layers.
- New dependencies are a last resort (attack surface, license risk, upgrade treadmill). Prefer stdlib / already-approved packages. Justify additions in the PR.
- No speculative features. No phantom features (docs, flags, or validation for behavior that does not exist).
- Extract a shared helper after the same logic appears three times *inside one bounded context*. Do not create a cross-service "common" kitchen-sink library.
- Configuration is data: environment or validated config files, not hardcoded hostnames, credentials, or classification-specific endpoints.
- Record non-obvious structure, storage, or trust-boundary decisions in a short ADR.
- Internal implementations: replace, don't pile on. Published contracts: add, deprecate, remove after the documented window.

---

## Code quality

Targets, not religion. Exceed them only with a one-line comment *why* (generated code, protocol state machine, parsed grammar).

- Functions: ≤100 lines, cyclomatic complexity ≤8, ≤5 positional parameters (typed options object after that)
- Line length: 100. Absolute imports at application boundaries; relative MAY be used inside a single package
- Public APIs: Google-style docstrings / TSDoc / rustdoc on non-trivial exported surfaces
- Clarity over cleverness. Delete commented-out code.
- **Zero warnings** from the project's linters, type checkers, compilers, and tests. Inline suppressions MUST cite the rule and the reason.

**Errors:** fail fast at trust boundaries with an actionable message and stable error code. Never swallow exceptions. If a batch MUST continue, log context (operation, sanitized input, cause) and fail the job at the end. Do not leak internals or data to untrusted clients. Prefer structured logs over `print` / `dbg!`.

**Tests:** behavior and contracts, not private implementation. Cover edges, authz denials, timeouts, and malformed input. Mock only at process boundaries. Auth, crypto, parsing, and access control MUST have explicit negative tests. Mutation or property-based tests SHOULD exist for parsers, codecs, and policy engines.

**Review order:** architecture and trust boundaries → correctness and security → tests → clarity → performance. Cite `file:line`. If the fix is not obvious, present options, recommend one, and wait. Do not `git fetch` on air-gapped or classified systems.

---

## Tooling (every stack)

Use structure-aware tools (`ast-grep`, LSPs, compilers) for code shape; `rg` for literals; `fd` for file names. Install only allowlisted tools. In air-gapped environments, use the internal mirror.

| Tool | Replaces | Notes |
|------|----------|--------|
| `rg` | grep | Content search |
| `fd` | find | File names |
| `ast-grep` | ad-hoc AST regex | Calls, imports, classes |
| `prek` | pre-commit | `prek install` then `prek run`; `prek auto-update --cooldown-days 7` |
| `gitleaks` | — | Secrets; fail closed |
| Recoverable delete | `rm -rf` on user data | `trash` / `trash-cli`. **MUST NOT** `rm -rf` source, `.git`, or secrets. CI MAY remove build dirs. |

Runtimes: newest **org-approved** line still in upstream security support. Do not jump a production baseline without change control. Greenfield defaults are in the stack rules.

---

## Workflow

1. Re-read for extra surface area, unclear names, and skipped edges
2. Run tests that cover the change (full suite when touching auth, build, or CI)
3. Run linters, type checker, secret scan, and SCA; fix all findings
4. Confirm no secrets, customer data, or classification markings entered the diff

Commits: imperative mood, ≤72-character subject, one logical change. Sign when the org requires it. Never commit secrets, keys, or `.env` files.

Parallel agents MUST use separate worktrees (`wt switch <branch>` or `git worktree add`). Never share a dirty working tree.

PRs describe **what the tree does after merge**. Plain factual language (avoid: critical, crucial, essential, significant, comprehensive, robust, elegant). Link the ticket when the org uses them. Security, auth, crypto, and data-store changes SHOULD request review from those path owners.
