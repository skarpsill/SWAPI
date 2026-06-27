# SOLIDWORKS API MCP Server for Windows

This package contains everything needed to install the SOLIDWORKS API MCP server:

| File | Description |
|---|---|
| `swapi-setup.exe` | End-user installer wizard — **run this** |
| `swapi-mcp-server.exe` | MCP server executable (installed by the wizard) |
| `solidworks_api_2024.dump` | PostgreSQL database dump |
| `postgresql-18*.exe` | PostgreSQL installer (bundled when present) |

## Install

Double-click **`swapi-setup.exe`** and follow the wizard:

1. **Welcome** — click **Далее** (Next)
2. **Password** — set a PostgreSQL administrator password (minimum 4 characters, entered twice)
3. **Progress** — the wizard runs automatically:
   - Installs PostgreSQL 18 if not already present
   - Restores the SOLIDWORKS API database
   - Copies `swapi-mcp-server.exe` to `%LOCALAPPDATA%\Programs\SolidWorksApiMcp\`
   - Configures MCP servers for **VS Code** and **VS Codium**
4. Click **Завершить** (Finish) when done

## Manual Server Launch

```cmd
set SWAPI_DATABASE_URL=postgresql://postgres@localhost:5432/solidworks_api
set SWAPI_DEFAULT_VERSION=2024
swapi-mcp-server.exe
```

## Manual MCP Config

### VS Code / VS Codium — `mcp.json`

```json
{
  "mcpServers": {
    "solidworks-api": {
      "command": "C:\\Users\\you\\AppData\\Local\\Programs\\SolidWorksApiMcp\\swapi-mcp-server.exe",
      "env": {
        "SWAPI_DATABASE_URL": "postgresql://postgres@localhost:5432/solidworks_api",
        "SWAPI_DEFAULT_VERSION": "2024"
      }
    }
  }
}
```
