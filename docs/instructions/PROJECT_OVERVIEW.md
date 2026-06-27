# Project Overview

This project turns SOLIDWORKS API documentation into a local knowledge base that
Codex and other LLM agents can navigate cheaply and predictably.

The repository has two related purposes:

- provide a ready-to-use SOLIDWORKS API 2024 Markdown corpus and lookup index;
- provide a documentation-only MCP server that exposes the corpus through search
  and lookup tools.

## Main Data Flow

```text
SOLIDWORKS API .chm
  -> extracted HTML
  -> cleaned API_HTML tree
  -> Markdown topic files
  -> compact LLM indexes
  -> optional PostgreSQL database
  -> optional Windows release package
```

The public release package does not need to expose the whole private build
pipeline. End users can receive an executable MCP server, a PostgreSQL dump, and
install scripts.

## Repository Layout

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

## Versioned Corpus Layout

Each supported API year uses the same structure:

```text
versions/<year>/api/        # private input CHM files
versions/<year>/extracted/  # generated full CHM extraction
versions/<year>/API_HTML/   # generated HTML-only source tree
versions/<year>/markdown/   # generated Markdown documentation
versions/<year>/llm_index/  # generated lookup and graph indexes
```

The current included corpus is `versions/2024/`.

## Runtime Components

- `swapi_mcp/server.py` defines the MCP tool surface.
- `swapi_mcp/local_index.py` reads `versions/<year>/llm_index/` and
  `versions/<year>/markdown/` directly.
- `swapi_mcp/postgres_index.py` reads the same corpus after it has been loaded
  into PostgreSQL.
- `swapi_mcp/config.py` resolves default paths and environment overrides.
- `swapi_mcp/schema.sql` defines the PostgreSQL tables.

## Environment Overrides

The default version is `2024`. These environment variables can override the
default paths:

```text
SWAPI_DEFAULT_VERSION
SWAPI_VERSION_ROOT
SWAPI_LLM_INDEX_DIR
SWAPI_MARKDOWN_DIR
DATABASE_URL
SWAPI_DATABASE_URL
```

If `DATABASE_URL` or `SWAPI_DATABASE_URL` is set, the MCP server uses
PostgreSQL mode. Otherwise it uses local index mode.
