"""PostgreSQL tool discovery and database operations."""

from __future__ import annotations

from pathlib import Path
import shutil

from .runner import LogFn, capture_command, run_command


POSTGRES_VERSIONS = ("18", "17", "16", "15")


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
) -> None:
    if not dump_path.exists():
        raise FileNotFoundError(f"Database dump not found: {dump_path}")

    psql = find_postgres_tool("psql")
    pg_restore = find_postgres_tool("pg_restore")

    if drop_existing:
        run_command(
            [psql, "--host", host, "--port", str(port), "--username", user, "--dbname", "postgres", "--command", f"DROP DATABASE IF EXISTS {database}"],
            cwd=dump_path.parent,
            log=log,
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
    )
    if existing_database.strip() != "1":
        run_command(
            [psql, "--host", host, "--port", str(port), "--username", user, "--dbname", "postgres", "--command", f"CREATE DATABASE {_sql_identifier(database)}"],
            cwd=dump_path.parent,
            log=log,
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
    )
