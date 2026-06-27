# SWAPI Release Manager

Python/Tkinter GUI for Windows release maintenance.

## Features

- Export PostgreSQL custom-format dumps.
- Build `swapi-mcp-server.exe` and the Windows release zip.
- Install a built package locally.
- Write Codex and VS Code MCP config entries.
- Publish a draft GitHub Release through `gh`.

## Source Layout

- `app.py` - Tkinter UI.
- `release_builder.py` - PyInstaller server package build.
- `postgres_tools.py` - PostgreSQL tool discovery, dump export, restore.
- `installer.py` - local install flow.
- `mcp_config.py` - Codex and VS Code config writers.
- `publisher.py` - GitHub Release publishing through `gh`.
- `paths.py` - repository path resolution.
- `runner.py` - subprocess logging helpers.

## Build Exe

From repository root:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli build-gui-exe
```

## Automation CLI

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli export-dump
.\.venv\Scripts\python.exe -m swapi_release_manager.cli build-package --version 0.1.0-alpha.1 --api-version 2024
.\.venv\Scripts\python.exe -m swapi_release_manager.cli publish-release --tag v0.1.0-alpha.1 --package-path .\02_mcp_server\dist\solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip --draft
```
