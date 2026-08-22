# Python

Repo config is the source of truth (`[tool.ruff]`, `[tool.ty.rules]` in `pyproject.toml`). Add those files if missing, then use them.

- **Runtime:** org-approved 3.12–3.14 still in upstream security support. Greenfield default: 3.14 via `uv venv`. Do not jump a production baseline without change control.
- **Tools:** `uv` (deps/lock), `ruff` (lint/format), `ty` (types), `pytest` (tests)
- **Supply chain:** commit `uv.lock`; exact pins (`==`); hashes (`uv lock` / `--require-hashes`); `pip-audit` in CI. Prefer the org index over PyPI.
- **Layout:** tests in `tests/` mirroring the package. Build with `uv_build` (pure Python) or `hatchling` (native extensions).
- **Do not** add `pip install` of unpinned packages, `setup.py` without a lock, or runtime `pip` in production images.
