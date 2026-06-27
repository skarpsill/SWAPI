"""Repository path resolution for release tooling."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass(frozen=True)
class ProjectPaths:
    repo_root: Path
    product_root: Path
    parsing_root: Path
    packaging_root: Path
    windows_packaging: Path
    pyinstaller_packaging: Path
    python_exe: Path


def _source_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def repo_root() -> Path:
    if getattr(sys, "frozen", False):
        start = Path(sys.executable).resolve().parent
        for candidate in (start, *start.parents):
            if (candidate / "01_parsing_API").is_dir() and (candidate / "02_mcp_server").is_dir():
                return candidate
        return start
    return _source_repo_root()


def resolve_paths(root: Path | None = None) -> ProjectPaths:
    repo = (root or repo_root()).resolve()
    product = repo / "02_mcp_server"
    packaging = product / "packaging"
    venv_python = repo / ".venv" / "Scripts" / "python.exe"
    return ProjectPaths(
        repo_root=repo,
        product_root=product,
        parsing_root=repo / "01_parsing_API",
        packaging_root=packaging,
        windows_packaging=packaging / "windows",
        pyinstaller_packaging=packaging / "pyinstaller",
        python_exe=venv_python if venv_python.exists() else Path(sys.executable),
    )


def resolve_under(base: Path, path: str | Path) -> Path:
    candidate = Path(path).expanduser()
    if not candidate.is_absolute():
        candidate = base / candidate
    return candidate.resolve()
