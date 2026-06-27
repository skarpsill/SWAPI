# Карта проекта и связей файлов

Репозиторий разделён на две главные зоны с номерами. Это намеренное разделение:
pipeline подготовки API-документации не смешивается с конечным MCP product.

## Верхний уровень

```text
.
|-- 01_parsing_API/        # maintainer pipeline и generated API corpus
|-- 02_mcp_server/         # MCP server product, packaging, installer
|-- docs/                  # проектная документация
|-- .github/workflows/     # CI/release workflows
|-- AGENTS.md              # правила для Codex в этом workspace
|-- pyproject.toml         # Python package metadata и console entry points
|-- requirements.txt       # базовые Python dependencies
|-- README.md
|-- README.ru.md
|-- LICENSE
`-- NOTICE.md
```

## 01_parsing_API

Эта зона отвечает за подготовку данных.

```text
01_parsing_API/
|-- 2022/
|-- 2023/
|-- 2024/
|   |-- api/        # private CHM input, не публикуется
|   |-- extracted/  # generated full CHM extraction, не публикуется
|   |-- API_HTML/   # generated HTML-only tree, не публикуется
|   |-- markdown/   # generated Markdown corpus
|   `-- llm_index/  # generated lookup and graph indexes
|-- 2025/
|-- 2026/
|-- release-assets/ # local PostgreSQL dumps for release assembly
`-- scripts/
    |-- unpack_chm_recursive.sh
    |-- collect_html.py
    |-- convert_sw_api_docs.py
    |-- build_llm_index.py
    `-- load_postgres.py
```

Связи:

- `unpack_chm_recursive.sh` читает `01_parsing_API/<year>/api/` и пишет
  `01_parsing_API/<year>/extracted/`.
- `collect_html.py` читает `extracted/` и пишет `API_HTML/`.
- `convert_sw_api_docs.py` читает `API_HTML/` и пишет `markdown/`.
- `build_llm_index.py` читает `markdown/` и пишет `llm_index/`.
- `load_postgres.py` читает `markdown/` + `llm_index/`, берёт schema из
  `02_mcp_server/swapi_mcp/schema.sql` и загружает PostgreSQL.

## 02_mcp_server

Эта зона отвечает за конечный продукт.

```text
02_mcp_server/
|-- swapi_mcp/
|   |-- server.py          # MCP tools and main entry point
|   |-- config.py          # path/env resolution
|   |-- local_index.py     # local Markdown/llm_index backend
|   |-- postgres_index.py  # PostgreSQL backend
|   |-- schema.sql         # PostgreSQL schema
|   |-- __main__.py
|   `-- __init__.py
`-- packaging/
    |-- pyinstaller/
    |   `-- swapi_mcp_server.py
    `-- windows/
        |-- build-release.ps1
        |-- export-postgres-dump.ps1
        |-- install.ps1
        |-- publish-github-release.ps1
        |-- restore-db.ps1
        `-- README.md
```

Связи:

- `pyproject.toml` maps package `swapi_mcp` to `02_mcp_server/swapi_mcp`.
- Console command `swapi-mcp` calls `swapi_mcp.server:main`.
- `server.py` chooses local or PostgreSQL backend through `config.py`.
- Local mode reads `01_parsing_API/<year>/llm_index/` and
  `01_parsing_API/<year>/markdown/`.
- PostgreSQL mode uses `DATABASE_URL` or `SWAPI_DATABASE_URL`.
- `build-release.ps1` installs the root package, builds
  `swapi-mcp-server.exe`, and writes release output to `02_mcp_server/dist/`.
- `install.ps1` installs the exe, restores the bundled dump, and can write
  Codex/VS Code MCP config.

## Python package links

`pyproject.toml` is still at repository root because it describes both runtime
and maintainer commands:

```text
swapi-mcp           -> 02_mcp_server/swapi_mcp/server.py
swapi-load-postgres -> 01_parsing_API/scripts/load_postgres.py
```

`swapi_mcp/schema.sql` is included as package data so `load_postgres.py` can
load the database schema even after editable/installable packaging.

## Generated and removable artifacts

These are local/generated and should not be committed:

- `.venv/`
- `__pycache__/`
- `*.egg-info/`
- `*.spec`
- `02_mcp_server/dist/`
- `01_parsing_API/release-assets/`
- `01_parsing_API/<year>/api/`
- `01_parsing_API/<year>/extracted/`
- `01_parsing_API/<year>/API_HTML/`

The generated `markdown/` and `llm_index/` folders are intentionally published
for `2024` as the ready-to-use example corpus.
