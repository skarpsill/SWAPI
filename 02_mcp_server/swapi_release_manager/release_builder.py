"""Build Windows release packages."""

from __future__ import annotations

from pathlib import Path
import shutil
import zipfile

from .paths import ProjectPaths
from .runner import LogFn, run_command


def _pyinstaller_build(
    *,
    paths: ProjectPaths,
    name: str,
    entry_point: Path,
    package_dir: Path,
    work_dir: Path,
    log: LogFn,
) -> None:
    cmd = [
        paths.python_exe,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        "--onefile",
        "--name",
        name,
        "--paths",
        str(paths.product_root),
        "--specpath",
        str(work_dir),
        "--distpath",
        str(package_dir),
        "--workpath",
        str(work_dir),
        str(entry_point),
    ]
    run_command(cmd, paths.product_root, log)


def build_server_package(
    *,
    paths: ProjectPaths,
    version: str,
    api_version: str,
    database_dump: Path | None,
    postgresql_installer: Path | None,
    output_dir: Path,
    log: LogFn,
) -> Path:
    if database_dump and not database_dump.exists():
        raise FileNotFoundError(f"Database dump not found: {database_dump}")
    if postgresql_installer and not postgresql_installer.exists():
        raise FileNotFoundError(f"PostgreSQL installer not found: {postgresql_installer}")

    run_command(
        [paths.python_exe, "-m", "pip", "install", "-e", f"{paths.product_root}[postgres,release]"],
        paths.product_root,
        log,
    )

    build_root = output_dir
    package_name = f"solidworks-api-mcp-{version}-windows-x64"
    package_dir = build_root / package_name
    work_dir = build_root / "pyinstaller-work"
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    log("Building swapi-mcp-server.exe...")
    _pyinstaller_build(
        paths=paths,
        name="swapi-mcp-server",
        entry_point=paths.pyinstaller_packaging / "swapi_mcp_server.py",
        package_dir=package_dir,
        work_dir=work_dir,
        log=log,
    )

    log("Building swapi-setup.exe...")
    _pyinstaller_build(
        paths=paths,
        name="swapi-setup",
        entry_point=paths.pyinstaller_packaging / "swapi_setup.py",
        package_dir=package_dir,
        work_dir=work_dir,
        log=log,
    )

    for item in ("README.md",):
        shutil.copy2(paths.windows_packaging / item, package_dir / item)

    if database_dump:
        shutil.copy2(database_dump, package_dir / f"solidworks_api_{api_version}.dump")

    if postgresql_installer:
        shutil.copy2(postgresql_installer, package_dir / postgresql_installer.name)
        log(f"Bundled PostgreSQL installer: {postgresql_installer.name}")

    zip_path = build_root / f"{package_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(package_dir))
    log(f"Release package: {zip_path}")
    return zip_path
