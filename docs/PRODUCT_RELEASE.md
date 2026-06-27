# Product Release Plan

The public product should be an installable MCP server package. The private
build pipeline can remain separate.

## Private Build Pipeline

Keep these steps private or in a separate tooling repository:

```text
.chm -> html -> markdown -> llm_index -> PostgreSQL -> compressed dump
```

The public user does not need CHM extraction, Markdown conversion, or index
generation.

## Public Release Package

GitHub Release asset:

```text
solidworks-api-mcp-<version>-windows-x64.zip
  swapi-mcp-server.exe
  solidworks_api_2024.dump
  install.ps1
  restore-db.ps1
  README.md
```

MVP runtime:

- Python server packaged as a Windows `.exe` with PyInstaller.
- PostgreSQL remains the local database backend.
- The release includes a ready PostgreSQL custom-format dump.
- The install script restores the database and can optionally write Codex or
  VS Code MCP configuration.

## Maintainer Flow

1. Build or update the local PostgreSQL database.
2. Export the release dump with the GUI, or with the automation CLI:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli export-dump --api-version 2024
```

3. Build the Windows package with the GUI, or with the automation CLI:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli build-package `
  --version 0.1.0-alpha.1 `
  --api-version 2024 `
  --database-dump .\01_parsing_API\release-assets\solidworks_api_2024.dump
```

4. Create a GitHub Release from a tag such as `v0.1.0-alpha.1`.
5. Upload `02_mcp_server/dist/solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip`.

With GitHub CLI installed:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli publish-release `
  --tag v0.1.0-alpha.1 `
  --package-path .\02_mcp_server\dist\solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip `
  --draft
```

The GitHub Actions workflow can build the executable package, but it does not
produce the proprietary/derived database dump by itself. Use the private build
pipeline or a maintainer machine to create the full release asset with the dump.

## Future Direction

A C# implementation is still attractive for deeper Windows integration, but it
does not need to block the MVP release. The current Python MCP server can be
validated as a product first, then replaced internally by a C# executable later
while keeping the same MCP tool contract.
