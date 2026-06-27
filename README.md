# SOLIDWORKS API Knowledge Base for Codex

Language: English | [Russian](README.ru.md)

This repository is split into two main areas:

- `01_parsing_API/` - maintainer tooling and generated SOLIDWORKS API corpus.
- `02_mcp_server/` - the installable MCP server product and release packaging.

The project helps Codex and other LLM agents answer SOLIDWORKS API questions and
write VBA macros or C# add-ins without scanning tens of thousands of Markdown
files.

## Start Here

- [Project map](docs/PROJECT_MAP.md) - detailed folder and file dependency map.
- [Instruction hub](docs/instructions/README.md) - full English instruction set.
- [Russian instruction hub](docs/instructions/ru/README.md) - Russian copy of
  the instruction set.
- [MCP server reference](docs/MCP_SERVER.md) - server modes, tools, and config.
- [Product release plan](docs/PRODUCT_RELEASE.md) - Windows package flow.

## What Is Included

- `01_parsing_API/2024/markdown/` - generated Markdown API documentation.
- `01_parsing_API/2024/llm_index/` - compact lookup and relationship indexes.
- `01_parsing_API/scripts/` - maintainer pipeline scripts for rebuilding the
  corpus.
- `02_mcp_server/swapi_mcp/` - MCP server package and PostgreSQL schema.
- `02_mcp_server/packaging/windows/` - Windows release and install scripts.
- `AGENTS.md` - local instructions for Codex when this repository is used as a
  workspace knowledge base.

Original `.chm` files and intermediate extracted HTML are not published. Project
source code is MIT licensed. Generated Markdown may contain material derived
from official SOLIDWORKS API documentation; see [NOTICE.md](NOTICE.md).

## Quick Use

Open this repository as a workspace, or add it as a second folder next to your
SOLIDWORKS VBA/C# project. Ask Codex to follow `AGENTS.md` before writing code.

Detailed workflows live in [docs/instructions](docs/instructions/README.md).
