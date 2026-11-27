#!/usr/bin/env python3
"""Atomically merge, insert, or append a distilled rule into a policy file."""

from __future__ import annotations

import contextlib
import hashlib
import os
import pathlib
import subprocess
import sys
import tempfile
from typing import Iterator

try:
    import fcntl
except ImportError:  # pragma: no cover - non-POSIX fallback
    fcntl = None  # type: ignore[assignment]


def resolve_lock_path(target_dir: pathlib.Path) -> pathlib.Path:
    """Resolve a per-repository lockfile path inside git common dir or temp."""
    search_dir = target_dir if target_dir.exists() else pathlib.Path.cwd()
    result = subprocess.run(
        ["git", "-C", str(search_dir), "rev-parse", "--path-format=absolute", "--git-common-dir"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip():
        git_common = pathlib.Path(result.stdout.strip())
        if git_common.is_dir():
            return git_common / "jae-learn.lock"

    repo_hash = hashlib.sha256(str(target_dir.resolve()).encode("utf-8")).hexdigest()[:12]
    return pathlib.Path(tempfile.gettempdir()) / f"jae-learn-{repo_hash}.lock"


@contextlib.contextmanager
def repo_lock(lock_path: pathlib.Path) -> Iterator[None]:
    """Acquire an exclusive advisory lock for the target repository."""
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock_file:
        if fcntl is not None:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            if fcntl is not None:
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def atomic_write(target_path: pathlib.Path, content: str) -> None:
    """Write content atomically via sibling temp file, fsync, and os.replace."""
    target_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{target_path.name}.",
        suffix=".tmp",
        dir=str(target_path.parent),
    )
    tmp_path = pathlib.Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, target_path)
    except BaseException:
        tmp_path.unlink(missing_ok=True)
        raise


def apply_rule(content: str, target: str, new_rule: str) -> tuple[str, str]:
    """Return (updated_content, status_message) without partial-substring replacements."""
    normalized_block = f"\n{new_rule}\n"
    if normalized_block in f"\n{content}\n":
        return content, "SKIP: Rule already present"

    lines = content.splitlines(keepends=True)

    if target and not target.startswith("#"):
        for idx, line in enumerate(lines):
            if line.strip() == target:
                ending = "\n" if line.endswith("\n") or idx < len(lines) - 1 else "\n"
                lines[idx] = f"{new_rule}{ending}"
                return "".join(lines), "OK: Atomically merged into existing rule"

    if target and target.startswith("#"):
        for idx, line in enumerate(lines):
            if line.strip() == target:
                insertion = f"\n{new_rule}\n"
                updated_lines = lines[: idx + 1] + [insertion] + lines[idx + 1 :]
                return "".join(updated_lines), "OK: Atomically inserted rule under section"

    sep = "\n" if content and not content.endswith("\n") else ""
    return f"{content}{sep}{new_rule}\n", "OK: Atomically appended rule"


def main(argv: list[str]) -> int:
    """CLI entrypoint: merge_rule.py <target_file> <target_or_heading> <rule_text>."""
    if len(argv) != 4:
        print(
            "Usage: merge_rule.py <target_file> <section_header_or_existing_rule> <new_rule>",
            file=sys.stderr,
        )
        return 2

    target_path = pathlib.Path(argv[1])
    target_selector = argv[2].strip()
    new_rule = argv[3].strip()

    if not new_rule:
        print("Error: new_rule must not be empty.", file=sys.stderr)
        return 2

    lock_path = resolve_lock_path(target_path.parent)
    with repo_lock(lock_path):
        content = target_path.read_text(encoding="utf-8") if target_path.exists() else ""
        updated, status = apply_rule(content, target_selector, new_rule)
        if not status.startswith("SKIP:"):
            atomic_write(target_path, updated)
        print(f"{status} in {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
