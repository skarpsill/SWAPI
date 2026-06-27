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

Export a PostgreSQL dump:

```powershell
.\02_mcp_server\packaging\windows\export-postgres-dump.ps1 -ApiVersion 2024
```

Build the Windows package:

```powershell
.\02_mcp_server\packaging\windows\build-release.ps1 `
  -Version 0.1.0-alpha.1 `
  -ApiVersion 2024 `
  -DatabaseDump .\01_parsing_API\release-assets\solidworks_api_2024.dump
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
.\02_mcp_server\packaging\windows\publish-github-release.ps1 `
  -Tag v0.1.0-alpha.1 `
  -PackagePath .\dist\solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip `
  -Draft
```

The GitHub Actions workflow can build the executable package, but it does not
produce the proprietary or derived database dump by itself. Use a maintainer
machine or private pipeline to create the full release asset with the dump.
