"""GitHub release publishing through gh CLI."""

from __future__ import annotations

from pathlib import Path
import shutil

from .runner import LogFn, run_command


def publish_github_release(
    *,
    repo_root: Path,
    tag: str,
    title: str,
    package_path: Path,
    draft: bool,
    log: LogFn,
) -> None:
    if not tag:
        raise ValueError("Tag is required.")
    if not package_path.exists():
        raise FileNotFoundError(f"Release package not found: {package_path}")
    gh = shutil.which("gh")
    if not gh:
        raise FileNotFoundError("GitHub CLI 'gh' was not found. Install it or create the release in GitHub UI.")
    release_title = title or f"SOLIDWORKS API MCP Server {tag}"
    args: list[str | Path] = [
        gh,
        "release",
        "create",
        tag,
        package_path,
        "--title",
        release_title,
        "--notes-file",
        repo_root / "docs" / "PRODUCT_RELEASE.md",
    ]
    if draft:
        args.append("--draft")
    run_command(args, repo_root, log)

