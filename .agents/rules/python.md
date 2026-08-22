---
trigger: glob
description: Python runtime, uv/ruff/ty/pytest, and supply chain
globs:
  - "**/*.py"
  - "**/*.pyi"
  - "**/pyproject.toml"
  - "**/uv.lock"
  - "**/requirements*.txt"
  - "**/conftest.py"
---

@../../rules/python.md
