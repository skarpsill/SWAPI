# Project Overview

This project is split into two numbered areas:

- `01_parsing_API/` - maintainer tooling and generated SOLIDWORKS API corpus.
- `02_mcp_server/` - installable MCP server product and release packaging.

The split keeps CHM parsing and corpus generation separate from the product that
end users install.

## Main Data Flow

```text
SOLIDWORKS API .chm
  -> extracted HTML
  -> API_HTML
  -> Markdown topic files
  -> compact LLM indexes
  -> optional PostgreSQL database
  -> optional Windows release package
```

## Main Links

- `01_parsing_API/scripts/` builds `01_parsing_API/<year>/markdown/` and
  `01_parsing_API/<year>/llm_index/`.
- `02_mcp_server/swapi_mcp/` serves the generated corpus through MCP tools.
- `pyproject.toml` maps Python packages to their new subdirectories.
- `02_mcp_server/packaging/windows/` builds and installs the Windows release.

See [Project map](../PROJECT_MAP.md) for the detailed folder and file
dependency map.
