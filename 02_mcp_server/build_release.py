#!/usr/bin/env python3
"""Build a numbered Windows release package.

Usage (from repo root):
    python 02_mcp_server/build_release.py

Reads .build_number, increments it (01 -> 02 -> ... -> 99),
exports the DB dump, builds the EXE package and ZIP archive.

Output: 02_mcp_server/dist/solidworks-api-mcp-0.1.XX-windows-x64.zip
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # 02_mcp_server/
ROOT = HERE.parent                              # repo root
sys.path.insert(0, str(HERE))

from swapi_release_manager.paths import resolve_paths
from swapi_release_manager.postgres_tools import export_dump
from swapi_release_manager.release_builder import build_server_package

VERSION_PREFIX = "0.1"
BUILD_NUMBER_FILE = HERE / ".build_number"
OUTPUT_DIR = HERE / "dist"
API_VERSION = "2024"
DB_DATABASE = "solidworks_api"
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432


def log(msg: str) -> None:
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)


def _read_build_number() -> int:
    if BUILD_NUMBER_FILE.exists():
        try:
            return int(BUILD_NUMBER_FILE.read_text(encoding="utf-8").strip())
        except ValueError:
            pass
    return 0


def _write_build_number(n: int) -> None:
    BUILD_NUMBER_FILE.write_text(str(n), encoding="utf-8")


def main() -> None:
    current = _read_build_number()
    next_num = current + 1
    if next_num > 99:
        sys.exit("Build number exceeded 99. Reset 02_mcp_server/.build_number manually.")

    version = f"{VERSION_PREFIX}.{next_num:02d}"
    log(f"=== Building release {version} ===\n")

    paths = resolve_paths(ROOT)

    log("── Exporting database dump ──────────────────────────────")
    dump_path = export_dump(
        output_dir=ROOT / "01_parsing_API" / "release-assets",
        api_version=API_VERSION,
        database=DB_DATABASE,
        user=DB_USER,
        host=DB_HOST,
        port=DB_PORT,
        log=log,
    )

    log(f"\n── Building package {version} ───────────────────────────")
    zip_path = build_server_package(
        paths=paths,
        version=version,
        api_version=API_VERSION,
        database_dump=dump_path,
        postgresql_installer=paths.postgresql_installer,
        output_dir=OUTPUT_DIR,
        log=log,
    )

    _write_build_number(next_num)
    log(f"\n=== Done: {zip_path} ===")


if __name__ == "__main__":
    main()
