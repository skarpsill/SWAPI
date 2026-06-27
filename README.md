# SOLIDWORKS API Knowledge Base for Codex

Language: English | [Russian](README.ru.md)

This repository contains a local SOLIDWORKS API knowledge base for Codex and
other LLM agents. It includes a generated SOLIDWORKS API 2024 Markdown corpus,
compact lookup indexes, a documentation-only MCP server, and release tooling for
a Windows MCP package backed by PostgreSQL.

The project is designed to help agents write VBA macros and C# add-ins without
loading tens of thousands of API documentation files into the model context.

## Start Here

- [Instruction hub](docs/instructions/README.md) - full project documentation
  and task-oriented guides.
- [Russian instruction hub](docs/instructions/ru/README.md) - Russian copy of
  the same instruction set.
- [Project overview](docs/instructions/PROJECT_OVERVIEW.md) - architecture,
  repository layout, data flow, and included artifacts.
- [Build pipeline](docs/instructions/BUILD_PIPELINE.md) - CHM extraction,
  Markdown conversion, LLM index generation, and PostgreSQL loading.
- [Using the knowledge base](docs/instructions/USING_KNOWLEDGE_BASE.md) - how
  to query indexes manually and how agents should navigate the corpus.
- [Windows release guide](docs/instructions/WINDOWS_RELEASE.md) - package,
  install, and publish the Windows MCP server release.
- [MCP server details](docs/MCP_SERVER.md) - server modes, environment
  variables, tools, and config examples.

## What Is Included

- `versions/2024/markdown/` - generated Markdown API documentation.
- `versions/2024/llm_index/` - compact lookup and relationship indexes.
- `swapi_mcp/` - MCP server, local index backend, PostgreSQL backend, and SQL
  schema.
- `scripts/` - private/maintainer pipeline scripts for rebuilding the corpus.
- `packaging/windows/` - Windows release packaging and install scripts.
- `AGENTS.md` - local instructions for Codex when this repository is used as a
  workspace knowledge base.

Original `.chm` files and intermediate extracted HTML are not published. The
project code is MIT licensed. Generated Markdown may contain material derived
from official SOLIDWORKS API documentation; see [NOTICE.md](NOTICE.md).

## Quick Use

Open this repository as a workspace, or add it as a second folder next to your
SOLIDWORKS VBA/C# project. Ask Codex to follow `AGENTS.md` before writing code.

For detailed commands and workflows, use the
[instruction hub](docs/instructions/README.md).
