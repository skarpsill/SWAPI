"""Automation CLI for the release manager package."""

from __future__ import annotations

import argparse
from pathlib import Path

from .paths import resolve_paths, resolve_under
from .postgres_tools import export_dump
from .publisher import publish_github_release
from .release_builder import build_server_package
from .runner import run_command


def log(message: str) -> None:
    print(message, flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build-package", help="Build the Windows MCP server release package.")
    build.add_argument("--version", default="0.1.0")
    build.add_argument("--api-version", default="2024")
    build.add_argument("--database-dump", type=Path, default=None)
    build.add_argument("--output-dir", type=Path, default=Path("02_mcp_server/dist"))

    export = sub.add_parser("export-dump", help="Export a PostgreSQL custom-format dump.")
    export.add_argument("--database", default="solidworks_api")
    export.add_argument("--user", default="postgres")
    export.add_argument("--host", default="localhost")
    export.add_argument("--port", type=int, default=5432)
    export.add_argument("--api-version", default="2024")
    export.add_argument("--output-dir", type=Path, default=Path("01_parsing_API/release-assets"))

    publish = sub.add_parser("publish-release", help="Publish a GitHub Release through gh.")
    publish.add_argument("--tag", required=True)
    publish.add_argument("--title", default="")
    publish.add_argument("--package-path", type=Path, required=True)
    publish.add_argument("--draft", action="store_true")

    gui = sub.add_parser("build-gui-exe", help="Build the Tkinter release manager executable.")
    gui.add_argument("--output-dir", type=Path, default=Path("02_mcp_server/dist/release-manager"))
    gui.add_argument("--work-dir", type=Path, default=Path("02_mcp_server/dist/pyinstaller-work"))

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = resolve_paths()

    if args.command == "build-package":
        build_server_package(
            paths=paths,
            version=args.version,
            api_version=args.api_version,
            database_dump=args.database_dump.resolve() if args.database_dump else None,
            output_dir=resolve_under(paths.repo_root, args.output_dir),
            log=log,
        )
    elif args.command == "export-dump":
        export_dump(
            output_dir=resolve_under(paths.repo_root, args.output_dir),
            api_version=args.api_version,
            database=args.database,
            user=args.user,
            host=args.host,
            port=args.port,
            log=log,
        )
    elif args.command == "publish-release":
        publish_github_release(
            repo_root=paths.repo_root,
            tag=args.tag,
            title=args.title,
            package_path=args.package_path.resolve(),
            draft=args.draft,
            log=log,
        )
    elif args.command == "build-gui-exe":
        run_command(
            [
                paths.python_exe,
                "-m",
                "PyInstaller",
                "--clean",
                "--noconfirm",
                "--onefile",
                "--windowed",
                "--name",
                "swapi-release-manager",
                "--distpath",
                resolve_under(paths.repo_root, args.output_dir),
                "--workpath",
                resolve_under(paths.repo_root, args.work_dir),
                paths.pyinstaller_packaging / "swapi_release_manager.py",
            ],
            paths.repo_root,
            log,
        )


if __name__ == "__main__":
    main()

