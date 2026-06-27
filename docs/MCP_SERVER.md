# SOLIDWORKS API MCP Server

This MCP server is documentation-only. It helps an IDE agent write SOLIDWORKS
VBA macros and C# add-ins by searching the local API knowledge base. It does
not connect to SOLIDWORKS and does not execute code.

## Modes

### Local index mode

Uses the generated files in `01_parsing_API/<year>/llm_index/` and
`01_parsing_API/<year>/markdown/` directly. This is the default and requires no
database.

```bash
python -m pip install -e .
python -m swapi_mcp.server
```

Optional environment variables:

```text
SWAPI_ROOT=/path/to/SWAPI
SWAPI_LLM_INDEX_DIR=/path/to/llm_index
SWAPI_MARKDOWN_DIR=/path/to/markdown
SWAPI_DEFAULT_VERSION=2024
```

### PostgreSQL mode

Load the generated knowledge base into PostgreSQL, then set `DATABASE_URL` for
the MCP server.

```bash
python -m pip install -e '.[postgres]'
createdb solidworks_api
swapi-load-postgres \
  --database-url postgresql:///solidworks_api \
  --version 2024 \
  --root .
DATABASE_URL=postgresql:///solidworks_api python -m swapi_mcp.server
```

The loader imports:

- `documents.jsonl` plus full Markdown text
- `symbols.jsonl`
- `interface_members.jsonl`
- `edges/*.jsonl`

## VSCode / Codex MCP Config

Local index mode:

```json
{
  "mcpServers": {
    "solidworks-api": {
      "command": "python",
      "args": ["-m", "swapi_mcp.server"],
      "env": {
  "SWAPI_ROOT": "C:/path/to/SWAPI",
  "SWAPI_DEFAULT_VERSION": "2024"
      }
    }
  }
}
```

PostgreSQL mode:

```json
{
  "mcpServers": {
    "solidworks-api": {
      "command": "python",
      "args": ["-m", "swapi_mcp.server"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/solidworks_api",
        "SWAPI_DEFAULT_VERSION": "2024"
      }
    }
  }
}
```

## Tools

- `swapi_status`
- `swapi_search_symbols`
- `swapi_lookup_symbol`
- `swapi_lookup_method`
- `swapi_lookup_enum`
- `swapi_interface_members`
- `swapi_get_doc`
- `swapi_neighbors`
- `swapi_find_examples`

## Recommended Agent Flow

1. Search for the symbol with `swapi_search_symbols`.
2. For an interface/object, inspect `swapi_interface_members`.
3. Read only the narrowed document with `swapi_get_doc`.
4. Use `swapi_neighbors` for related topics and See Also links.
5. Prefer `language="vba"` for macros and `language="csharp"` for add-ins.

## Windows / WSL Development Model

The intended workflow is:

1. Install PostgreSQL and VSCode/Codex on Windows.
2. Install WSL for CHM extraction and index generation.
3. Put the SOLIDWORKS API `.chm` files for the target version in `01_parsing_API/<year>/api/`.
4. Run the existing pipeline in WSL to produce `01_parsing_API/<year>/markdown/` and `01_parsing_API/<year>/llm_index/`.
5. Optionally load the generated corpus into PostgreSQL.
6. Register the MCP server in VSCode/Codex and use it from any macro/add-in
   project without copying the generated docs into that project.
