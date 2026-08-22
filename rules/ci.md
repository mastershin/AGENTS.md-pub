# CI / CD

Applies to GitHub Actions, GitLab, Azure DevOps, and on-prem. Same bar: pinned tools, least-privilege tokens, no secrets in logs, scanners as merge gates.

- Pin tools and container tags to digest or full SHA. No floating `latest`.
- Least-privilege tokens. Prefer OIDC over long-lived PATs. Default GitHub `GITHUB_TOKEN` to `permissions: { contents: read }`, then grant per job.
- Secret scanning and SCA are merge gates. Failed scans MUST NOT be ignored.

### GitHub Actions

- Pin to full SHA with a version comment: `actions/checkout@<sha>  # vX.Y.Z`
- `persist-credentials: false` on checkout
- Do not checkout untrusted PR code in `pull_request_target` with writable tokens
- `zizmor` and `actionlint` MUST pass before merge
- Dependabot/Renovate: 7-day cooldown, grouped updates, lockfile-aware (`uv.lock`, `pnpm-lock.yaml`, `Cargo.lock` — not raw pip). Manual approval when policy requires it.
