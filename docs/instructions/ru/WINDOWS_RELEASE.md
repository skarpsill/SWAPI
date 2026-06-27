# Windows Release

Это руководство описывает installable Windows MCP package.

[English version](../WINDOWS_RELEASE.md)

## Содержимое package

Release asset - это zip file:

```text
solidworks-api-mcp-<version>-windows-x64.zip
  swapi-mcp-server.exe
  solidworks_api_2024.dump
  install.ps1
  restore-db.ps1
  README.md
```

Package рассчитан на пользователей, которым не нужны Python и private CHM
conversion pipeline.

## Собрать package

Экспортировать PostgreSQL dump:

```powershell
.\packaging\windows\export-postgres-dump.ps1 -ApiVersion 2024
```

Собрать Windows package:

```powershell
.\packaging\windows\build-release.ps1 `
  -Version 0.1.0-alpha.1 `
  -ApiVersion 2024 `
  -DatabaseDump .\release-assets\solidworks_api_2024.dump
```

Output path:

```text
dist/solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip
```

## Установить из zip

Установите PostgreSQL локально, распакуйте package, откройте PowerShell в
папке package и выполните:

```powershell
.\install.ps1
```

Если database уже restored:

```powershell
.\install.ps1 -SkipDatabaseRestore
```

Чтобы также записать Codex MCP config:

```powershell
.\install.ps1 -ConfigureCodex
```

Чтобы также записать VS Code-style MCP JSON config:

```powershell
.\install.ps1 -ConfigureVsCode
```

## Manual runtime command

```powershell
$env:SWAPI_DATABASE_URL = "postgresql://postgres@localhost:5432/solidworks_api"
$env:SWAPI_DEFAULT_VERSION = "2024"
.\swapi-mcp-server.exe
```

## Опубликовать GitHub Release

Рекомендуемый первый tag:

```text
v0.1.0-alpha.1
```

Если GitHub CLI installed:

```powershell
.\packaging\windows\publish-github-release.ps1 `
  -Tag v0.1.0-alpha.1 `
  -PackagePath .\dist\solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip `
  -Draft
```

GitHub Actions workflow может собрать executable package, но сам не создает
proprietary или derived database dump. Используйте maintainer machine или
private pipeline, чтобы создать полный release asset с dump.
