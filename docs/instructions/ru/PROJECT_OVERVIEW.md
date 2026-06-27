# Обзор проекта

[English version](../PROJECT_OVERVIEW.md)

Проект разделён на две главные зоны:

- `01_parsing_API/` - подготовка и хранение корпуса SOLIDWORKS API.
- `02_mcp_server/` - конечный MCP server и Windows release packaging.

## Поток данных

```text
CHM files
  -> extracted HTML
  -> API_HTML
  -> markdown
  -> llm_index
  -> PostgreSQL dump
  -> Windows MCP package
```

## Основные связи

- `01_parsing_API/scripts/` строит `01_parsing_API/<year>/markdown/` и
  `01_parsing_API/<year>/llm_index/`.
- `02_mcp_server/swapi_mcp/` читает готовый corpus напрямую или через
  PostgreSQL.
- `pyproject.toml` связывает оба мира: runtime command `swapi-mcp` указывает на
  MCP server, а maintainer command `swapi-load-postgres` указывает на loader.
- `02_mcp_server/packaging/windows/` собирает installable Windows zip.

Подробная схема находится в [карте проекта](../../PROJECT_MAP.md).
