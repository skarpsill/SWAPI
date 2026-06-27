"""PostgreSQL tool discovery and database operations."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import time

from .runner import LogFn, capture_command, run_command


POSTGRES_VERSIONS = ("18", "17", "16", "15")
POSTGRES_MAJOR = "18"


def _sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _sql_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def find_postgres_tool(name: str) -> Path:
    found = shutil.which(name)
    if found:
        return Path(found)
    for version in POSTGRES_VERSIONS:
        candidate = Path("C:/Program Files/PostgreSQL") / version / "bin" / f"{name}.exe"
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"{name} was not found. Install PostgreSQL or add its bin directory to PATH.")


def is_postgres_installed() -> bool:
    """Return True if PostgreSQL 18 binaries are available."""
    if shutil.which("pg_restore"):
        return True
    return (Path("C:/Program Files/PostgreSQL") / POSTGRES_MAJOR / "bin" / "pg_restore.exe").exists()


def install_postgres_silent(installer_path: Path, password: str, log: LogFn) -> None:
    """Run EnterpriseDB PostgreSQL installer in unattended mode."""
    run_command(
        [
            installer_path,
            "--mode", "unattended",
            "--superpassword", password,
            "--servicename", f"postgresql-x64-{POSTGRES_MAJOR}",
            "--enable-components", "server,commandlinetools",
            "--disable-components", "pgAdmin,stackbuilder",
        ],
        cwd=installer_path.parent,
        log=log,
    )


def wait_for_postgres_service(timeout: int, log: LogFn) -> None:
    """Poll Windows SCM until the PostgreSQL service reports RUNNING."""
    service_name = f"postgresql-x64-{POSTGRES_MAJOR}"
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        result = subprocess.run(
            ["sc", "query", service_name],
            capture_output=True,
            text=True,
        )
        if "RUNNING" in result.stdout:
            return
        log("  Ожидание запуска службы...")
        time.sleep(3)
    raise TimeoutError(f"Служба {service_name} не запустилась за {timeout} секунд.")


def export_dump(
    *,
    output_dir: Path,
    api_version: str,
    database: str,
    user: str,
    host: str,
    port: int,
    log: LogFn,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    dump_path = output_dir / f"solidworks_api_{api_version}.dump"
    pg_dump = find_postgres_tool("pg_dump")
    run_command(
        [
            pg_dump,
            "--host",
            host,
            "--port",
            str(port),
            "--username",
            user,
            "--format",
            "custom",
            "--compress",
            "9",
            "--no-owner",
            "--no-privileges",
            "--file",
            dump_path,
            database,
        ],
        cwd=output_dir,
        log=log,
    )
    log(f"PostgreSQL dump: {dump_path}")
    return dump_path


def restore_dump(
    *,
    dump_path: Path,
    database: str,
    user: str,
    host: str,
    port: int,
    drop_existing: bool,
    log: LogFn,
    password: str | None = None,
) -> None:
    if not dump_path.exists():
        raise FileNotFoundError(f"Database dump not found: {dump_path}")

    psql = find_postgres_tool("psql")
    pg_restore = find_postgres_tool("pg_restore")
    pg_env = {"PGPASSWORD": password} if password else None

    if drop_existing:
        run_command(
            [psql, "--host", host, "--port", str(port), "--username", user, "--dbname", "postgres", "--command", f"DROP DATABASE IF EXISTS {database}"],
            cwd=dump_path.parent,
            log=log,
            extra_env=pg_env,
        )

    existing_database = capture_command(
        [
            psql,
            "--host",
            host,
            "--port",
            str(port),
            "--username",
            user,
            "--dbname",
            "postgres",
            "--tuples-only",
            "--no-align",
            "--command",
            f"SELECT 1 FROM pg_database WHERE datname = {_sql_literal(database)}",
        ],
        cwd=dump_path.parent,
        log=log,
        extra_env=pg_env,
    )
    if existing_database.strip() != "1":
        run_command(
            [psql, "--host", host, "--port", str(port), "--username", user, "--dbname", "postgres", "--command", f"CREATE DATABASE {_sql_identifier(database)}"],
            cwd=dump_path.parent,
            log=log,
            extra_env=pg_env,
        )
    run_command(
        [
            pg_restore,
            "--host",
            host,
            "--port",
            str(port),
            "--username",
            user,
            "--dbname",
            database,
            "--clean",
            "--if-exists",
            "--no-owner",
            "--no-privileges",
            dump_path,
        ],
        cwd=dump_path.parent,
        log=log,
        extra_env=pg_env,
    )
