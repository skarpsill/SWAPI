# Windows Release

[English version](../WINDOWS_RELEASE.md)

Windows release - это конечный installable package из зоны `02_mcp_server/`.

## Содержимое zip

```text
solidworks-api-mcp-<version>-windows-x64.zip
  swapi-mcp-server.exe
  solidworks_api_2024.dump
  install.ps1
  restore-db.ps1
  README.md
```

## Сборка

Предпочтительный maintainer flow - Python GUI:

```powershell
.\02_mcp_server\dist\release-manager\swapi-release-manager.exe
```

GUI умеет экспортировать PostgreSQL dump, собирать release zip, устанавливать
package локально и публиковать draft GitHub Release.

Сборка GUI exe из repository root:

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

Экспорт dump:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli export-dump --api-version 2024
```

Сборка package:

```powershell
.\.venv\Scripts\python.exe -m swapi_release_manager.cli build-package `
  --version 0.1.0-alpha.1 `
  --api-version 2024 `
  --database-dump .\01_parsing_API\release-assets\solidworks_api_2024.dump
```

Результат:

```text
02_mcp_server/dist/solidworks-api-mcp-0.1.0-alpha.1-windows-x64.zip
```

## Установка

```powershell
.\install.ps1
.\install.ps1 -ConfigureCodex
.\install.ps1 -ConfigureVsCode
```

## GitHub Release

Рекомендуемый первый tag:

```text
v0.1.0-alpha.1
```
