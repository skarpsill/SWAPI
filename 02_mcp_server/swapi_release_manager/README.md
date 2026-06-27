# SWAPI Release Manager

Python/Tkinter GUI for Windows release maintenance.

## Source Layout

| Module | Purpose |
|---|---|
| `app.py` | Tkinter GUI (Export / Build / Install / Publish tabs) |
| `setup_wizard.py` | End-user installation wizard (bundled as `swapi-setup.exe`) |
| `release_builder.py` | Builds `swapi-mcp-server.exe`, `swapi-setup.exe`, and the release ZIP |
| `installer.py` | Local install flow used by the GUI "Install Locally" tab |
| `postgres_tools.py` | PostgreSQL discovery, silent install, dump export, restore |
| `mcp_config.py` | MCP config writers for VS Code and VS Codium |
| `publisher.py` | GitHub Release publishing via `gh` CLI |
| `paths.py` | Repository path resolution |
| `runner.py` | Subprocess helpers with log streaming |
| `cli.py` | Automation CLI (build-package, export-dump, publish-release, build-gui-exe) |

## GUI

```
python -m swapi_release_manager
```

Or launch the compiled executable:

```
swapi-release-manager.exe
```

## Automation CLI

From the repository root:

```bash
# Export a PostgreSQL dump
python -m swapi_release_manager.cli export-dump

# Build the release package (swapi-setup.exe + swapi-mcp-server.exe + dump + zip)
python -m swapi_release_manager.cli build-package \
  --version 0.1.0 \
  --api-version 2024 \
  --postgresql-installer 02_mcp_server/packaging/windows/postgresql-18.4-2-windows-x64.exe

# Publish a GitHub Release
python -m swapi_release_manager.cli publish-release \
  --tag v0.1.0 \
  --package-path 02_mcp_server/dist/solidworks-api-mcp-0.1.0-windows-x64.zip \
  --draft

# Build the release manager GUI executable
python -m swapi_release_manager.cli build-gui-exe
```

## Release Package Contents

After `build-package` the ZIP contains:

```
solidworks-api-mcp-<version>-windows-x64/
├── swapi-setup.exe                     ← end-user installer wizard
├── swapi-mcp-server.exe                ← MCP server
├── solidworks_api_<version>.dump       ← database
├── postgresql-18*.exe                  ← bundled PostgreSQL installer (if provided)
└── README.md
```
