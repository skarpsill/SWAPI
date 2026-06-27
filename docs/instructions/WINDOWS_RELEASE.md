# Windows Release

This guide covers the installable Windows MCP package.

## Package Contents

The release asset is a zip file:

```text
solidworks-api-mcp-<version>-windows-x64.zip
  swapi-mcp-server.exe
  solidworks_api_2024.dump
  install.ps1
  restore-db.ps1
  README.md
```

The package is designed for users who do not need Python or the private CHM
conversion pipeline.

## Build The Package

Preferred maintainer flow is the Python GUI:

```powershell
.\02_mcp_server\dist\release-manager\swapi-release-manager.exe
```

The GUI can export the PostgreSQL dump, build the release zip, install a local
package, and publish a draft GitHub Release.

Build the GUI exe from repository root:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller `
  --clean `
  --noconfirm `
  --onefile `
  --windowed `
  --name swapi-release-manager `
  --distpath .\02_mcp_server\dist\release-manager `
  --workpath .\02_mcp_server\dist\pyinstaller-work `
  .\02_mcp_server\packaging\pyinstaller\swapi_release_manager.py
```

Automation CLI flow:

Export a PostgreSQL dump:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli export-dump --api-version 2024
```

Build the Windows package:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli build-package `
  --version 0.1.0-alpha.1 `
  --api-version 2024 `
  --database-dump .\01_parsing_API\release-assets\solidworks_api_2024.dump
```

The output path is:

```text
02_mcp_server/dist/solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip
```

## Install From The Zip

Install PostgreSQL locally, unzip the package, open PowerShell in the package
directory, and run:

```powershell
.\install.ps1
```

If the database is already restored:

```powershell
.\install.ps1 -SkipDatabaseRestore
```

To also write Codex MCP config:

```powershell
.\install.ps1 -ConfigureCodex
```

To also write a VS Code-style MCP JSON config:

```powershell
.\install.ps1 -ConfigureVsCode
```

## Manual Runtime Command

```powershell
$env:SWAPI_DATABASE_URL = "postgresql://postgres@localhost:5432/solidworks_api"
$env:SWAPI_DEFAULT_VERSION = "2024"
.\swapi-mcp-server.exe
```

## Publish A GitHub Release

Recommended first tag:

```text
v0.1.0-alpha.1
```

With GitHub CLI installed:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli publish-release `
  --tag v0.1.0-alpha.1 `
  --package-path .\02_mcp_server\dist\solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip `
  --draft
```

The GitHub Actions workflow can build the executable package, but it does not
produce the proprietary or derived database dump by itself. Use a maintainer
machine or private pipeline to create the full release asset with the dump.
