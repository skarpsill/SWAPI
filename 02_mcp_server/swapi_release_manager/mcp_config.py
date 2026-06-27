"""Codex and VS Code MCP config writers."""

from __future__ import annotations

from pathlib import Path
import json
import os
import re


SERVER_NAME = "solidworks-api"


def toml_literal(value: str) -> str:
    if "'" not in value:
        return f"'{value}'"
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def default_codex_config() -> Path:
    return Path.home() / ".codex" / "config.toml"


def default_vscode_config() -> Path:
    return Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming")) / "Code" / "User" / "mcp.json"


def default_vscodium_config() -> Path:
    return Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming")) / "VSCodium" / "User" / "mcp.json"


def write_codex_config(config_path: Path, command: Path, env: dict[str, str]) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    env_parts = ", ".join(f"{key} = {toml_literal(env[key])}" for key in sorted(env))
    block = "\n".join(
        [
            f"[mcp_servers.{SERVER_NAME}]",
            f"command = {toml_literal(str(command))}",
            f"env = {{ {env_parts} }}",
        ]
    )
    existing = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
    pattern = re.compile(rf"(?ms)^\[mcp_servers\.{re.escape(SERVER_NAME)}\]\r?\n.*?(?=^\[|\Z)")
    if pattern.search(existing):
        updated = pattern.sub(block, existing)
    elif existing.strip():
        updated = existing.rstrip() + "\n\n" + block + "\n"
    else:
        updated = block + "\n"
    config_path.write_text(updated, encoding="utf-8")


def write_vscode_config(config_path: Path, command: Path, env: dict[str, str]) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    if config_path.exists() and config_path.read_text(encoding="utf-8").strip():
        config = json.loads(config_path.read_text(encoding="utf-8"))
    else:
        config = {}
    config.setdefault("mcpServers", {})
    config["mcpServers"][SERVER_NAME] = {"command": str(command), "env": dict(sorted(env.items()))}
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")


def write_vscodium_config(config_path: Path, command: Path, env: dict[str, str]) -> None:
    write_vscode_config(config_path, command, env)

