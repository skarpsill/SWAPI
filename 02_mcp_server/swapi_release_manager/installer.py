"""Install a built MCP package locally."""

from __future__ import annotations

from pathlib import Path
import shutil

from .mcp_config import write_codex_config, write_vscode_config
from .postgres_tools import restore_dump
from .runner import LogFn


def install_local_package(
    *,
    package_dir: Path,
    install_dir: Path,
    database: str,
    database_user: str,
    database_host: str,
    database_port: int,
    api_version: str,
    skip_database_restore: bool,
    configure_codex: bool,
    codex_config_path: Path,
    configure_vscode: bool,
    vscode_config_path: Path,
    log: LogFn,
) -> Path:
    exe = package_dir / "swapi-mcp-server.exe"
    if not exe.exists():
        raise FileNotFoundError(f"Package exe not found: {exe}")
    install_dir.mkdir(parents=True, exist_ok=True)
    for name in ("swapi-mcp-server.exe", "README.md"):
        source = package_dir / name
        if source.exists():
            shutil.copy2(source, install_dir / name)

    if not skip_database_restore:
        dumps = sorted(package_dir.glob("solidworks_api_*.dump"))
        if not dumps:
            raise FileNotFoundError("No solidworks_api_<version>.dump found in package directory.")
        restore_dump(
            dump_path=dumps[0],
            database=database,
            user=database_user,
            host=database_host,
            port=database_port,
            drop_existing=False,
            log=log,
        )

    installed_exe = install_dir / "swapi-mcp-server.exe"
    database_url = f"postgresql://{database_user}@{database_host}:{database_port}/{database}"
    env = {"SWAPI_DATABASE_URL": database_url, "SWAPI_DEFAULT_VERSION": api_version}
    if configure_codex:
        write_codex_config(codex_config_path, installed_exe, env)
        log(f"Updated Codex MCP config: {codex_config_path}")
    if configure_vscode:
        write_vscode_config(vscode_config_path, installed_exe, env)
        log(f"Updated VS Code MCP config: {vscode_config_path}")
    log(f"Installed MCP server: {installed_exe}")
    return installed_exe

