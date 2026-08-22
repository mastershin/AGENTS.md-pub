# Shell

Every script MUST start with:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

- Quote variables. Prefer arrays over word-splitting. Never `eval` untrusted input.
- `shellcheck` and `shfmt -d` MUST pass.
- Use `mktemp` and traps for cleanup. Do not parse `ls`. Do not `cd` without checking.
- **MUST NOT** `curl | bash`, disable `pipefail`, or run world-writable scripts.
- Prefer `rg` / `fd` over `grep` / `find` when those tools are available.
