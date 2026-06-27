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

Экспорт dump:

```powershell
.\02_mcp_server\packaging\windows\export-postgres-dump.ps1 -ApiVersion 2024
```

Сборка package:

```powershell
.\02_mcp_server\packaging\windows\build-release.ps1 `
  -Version 0.1.0-alpha.1 `
  -ApiVersion 2024 `
  -DatabaseDump .\01_parsing_API\release-assets\solidworks_api_2024.dump
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
