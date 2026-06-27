"""Build Windows release packages."""

from __future__ import annotations

from pathlib import Path
import shutil
import zipfile

from .paths import ProjectPaths
from .runner import LogFn, run_command


def build_server_package(
    *,
    paths: ProjectPaths,
    version: str,
    api_version: str,
    database_dump: Path | None,
    output_dir: Path,
    log: LogFn,
) -> Path:
    if database_dump and not database_dump.exists():
        raise FileNotFoundError(f"Database dump not found: {database_dump}")

    run_command([paths.python_exe, "-m", "pip", "install", "-e", f"{paths.repo_root}[postgres,release]"], paths.repo_root, log)

    build_root = output_dir
    package_name = f"solidworks-api-mcp-{version}-windows-x64"
    package_dir = build_root / package_name
    work_dir = build_root / "pyinstaller-work"
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    run_command(
        [
            paths.python_exe,
            "-m",
            "PyInstaller",
            "--clean",
            "--noconfirm",
            "--onefile",
            "--name",
            "swapi-mcp-server",
            "--paths",
            paths.product_root,
            "--distpath",
            package_dir,
            "--workpath",
            work_dir,
            paths.pyinstaller_packaging / "swapi_mcp_server.py",
        ],
        paths.repo_root,
        log,
    )

    for name in ("install.ps1", "restore-db.ps1", "README.md"):
        shutil.copy2(paths.windows_packaging / name, package_dir / name)

    if database_dump:
        shutil.copy2(database_dump, package_dir / f"solidworks_api_{api_version}.dump")

    zip_path = build_root / f"{package_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(package_dir))
    log(f"Release package: {zip_path}")
    return zip_path
