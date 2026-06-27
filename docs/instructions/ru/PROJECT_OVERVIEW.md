# Обзор проекта

Этот проект превращает документацию SOLIDWORKS API в локальную базу знаний,
которую Codex и другие LLM-агенты могут просматривать дешево и предсказуемо.

[English version](../PROJECT_OVERVIEW.md)

У репозитория две связанные цели:

- предоставить готовый Markdown-корпус SOLIDWORKS API 2024 и lookup index;
- предоставить documentation-only MCP server, который открывает доступ к
  корпусу через search и lookup tools.

## Основной поток данных

```text
SOLIDWORKS API .chm
  -> extracted HTML
  -> cleaned API_HTML tree
  -> Markdown topic files
  -> compact LLM indexes
  -> optional PostgreSQL database
  -> optional Windows release package
```

Публичный release package не обязан раскрывать весь приватный build pipeline.
Конечные пользователи могут получить executable MCP server, PostgreSQL dump и
install scripts.

## Структура репозитория

```text
.
|-- AGENTS.md
|-- README.md
|-- docs/
|   |-- MCP_SERVER.md
|   |-- PRODUCT_RELEASE.md
|   `-- instructions/
|-- packaging/
|   |-- pyinstaller/
|   `-- windows/
|-- scripts/
|-- swapi_mcp/
`-- versions/
    |-- 2022/
    |-- 2023/
    |-- 2024/
    |-- 2025/
    `-- 2026/
```

## Версионированная структура корпуса

Каждый поддерживаемый год API использует одну и ту же структуру:

```text
versions/<year>/api/        # private input CHM files
versions/<year>/extracted/  # generated full CHM extraction
versions/<year>/API_HTML/   # generated HTML-only source tree
versions/<year>/markdown/   # generated Markdown documentation
versions/<year>/llm_index/  # generated lookup and graph indexes
```

Текущий включенный корпус находится в `versions/2024/`.

## Runtime components

- `swapi_mcp/server.py` определяет MCP tool surface.
- `swapi_mcp/local_index.py` читает `versions/<year>/llm_index/` и
  `versions/<year>/markdown/` напрямую.
- `swapi_mcp/postgres_index.py` читает тот же корпус после загрузки в
  PostgreSQL.
- `swapi_mcp/config.py` вычисляет default paths и environment overrides.
- `swapi_mcp/schema.sql` определяет PostgreSQL tables.

## Environment overrides

Версия по умолчанию: `2024`. Эти переменные окружения могут переопределить
пути:

```text
SWAPI_DEFAULT_VERSION
SWAPI_VERSION_ROOT
SWAPI_LLM_INDEX_DIR
SWAPI_MARKDOWN_DIR
DATABASE_URL
SWAPI_DATABASE_URL
```

Если задан `DATABASE_URL` или `SWAPI_DATABASE_URL`, MCP server использует
PostgreSQL mode. Иначе используется local index mode.
