# SOLIDWORKS API MCP Server for Windows

This package contains a Windows executable MCP server and a PostgreSQL database
dump with the generated SOLIDWORKS API knowledge base.

## Install

1. Install PostgreSQL locally.
2. Run PowerShell in this package directory.
3. Run:

```powershell
.\install.ps1
```

The installer copies `swapi-mcp-server.exe`, restores the bundled database dump,
and prints an MCP configuration snippet.

If the database is already restored:

```powershell
.\install.ps1 -SkipDatabaseRestore
```

To also update Codex MCP configuration:

```powershell
.\install.ps1 -ConfigureCodex
```

By default this writes to:

```text
%USERPROFILE%\.codex\config.toml
```

To also update a VS Code-style MCP JSON file:

```powershell
.\install.ps1 -ConfigureVsCode
```

By default this writes to:

```text
%APPDATA%\Code\User\mcp.json
```

## Manual Server Command

```powershell
$env:SWAPI_DATABASE_URL = "postgresql://postgres@localhost:5432/solidworks_api"
$env:SWAPI_DEFAULT_VERSION = "2024"
.\swapi-mcp-server.exe
```

## Manual Codex Config

```toml
[mcp_servers.solidworks-api]
command = 'C:\Users\you\AppData\Local\Programs\SolidWorksApiMcp\swapi-mcp-server.exe'
env = { SWAPI_DATABASE_URL = 'postgresql://postgres@localhost:5432/solidworks_api', SWAPI_DEFAULT_VERSION = '2024' }
```
