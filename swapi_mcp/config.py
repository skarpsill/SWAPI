"""Configuration helpers for the SOLIDWORKS API knowledge server."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Runtime settings resolved from environment variables."""

    project_root: Path
    index_dir: Path
    markdown_dir: Path
    default_version: str
    database_url: str | None


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_settings() -> Settings:
    root = Path(os.environ.get("SWAPI_ROOT", _default_root())).expanduser().resolve()
    default_version = os.environ.get("SWAPI_DEFAULT_VERSION", "2024")
    version_root = Path(os.environ.get("SWAPI_VERSION_ROOT", root / "versions" / default_version)).expanduser()
    legacy_index_dir = root / "llm_index"
    legacy_markdown_dir = root / "markdown"
    default_index_dir = version_root / "llm_index" if (version_root / "llm_index").exists() else legacy_index_dir
    default_markdown_dir = version_root / "markdown" if (version_root / "markdown").exists() else legacy_markdown_dir
    index_dir = Path(os.environ.get("SWAPI_LLM_INDEX_DIR", default_index_dir)).expanduser().resolve()
    markdown_dir = Path(os.environ.get("SWAPI_MARKDOWN_DIR", default_markdown_dir)).expanduser().resolve()
    return Settings(
        project_root=root,
        index_dir=index_dir,
        markdown_dir=markdown_dir,
        default_version=default_version,
        database_url=os.environ.get("DATABASE_URL") or os.environ.get("SWAPI_DATABASE_URL"),
    )
