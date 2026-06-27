# SolidWorks API Knowledge Base

This workspace contains converted SOLIDWORKS API documentation for fast local
use by Codex.

## Project Zones

- `01_parsing_API/` contains the private/maintainer pipeline and generated API
  corpus.
- `02_mcp_server/` contains the MCP server source and release packaging.
- `docs/PROJECT_MAP.md` explains the file and module relationships.

## Documentation Layout

- `01_parsing_API/<year>/API_HTML/` contains extracted HTML sources.
- `01_parsing_API/<year>/markdown/` contains converted Markdown documentation,
  one logical API topic per file.
- `01_parsing_API/<year>/llm_index/` contains compact lookup and graph indexes.
- The currently included corpus is `01_parsing_API/2024/`.
- `01_parsing_API/scripts/` contains corpus rebuild and PostgreSQL loading
  scripts.
- `02_mcp_server/swapi_mcp/` contains the MCP server implementation.

## How To Use This Context

When answering SOLIDWORKS API, VBA macro, or C# add-in questions:

1. Do not scan all Markdown files.
2. Start with `01_parsing_API/2024/llm_index/symbols.tsv` for exact or substring
   API symbol lookup unless another version is requested.
3. Use `01_parsing_API/2024/llm_index/interface_members.jsonl` when the user asks
   about an interface, object, class, or available members.
4. Use `01_parsing_API/2024/llm_index/edges/` only after identifying a small
   candidate set and needing See Also / related topics.
5. Open full files from `01_parsing_API/2024/markdown/` only after narrowing the
   candidates.
6. Prefer the API flavor that matches the task:
   - VBA macros: `*apivb6` modules and VBA syntax blocks.
   - C# add-ins: .NET modules such as `sldworksapi`, `cworksapi`,
     `swdocmgrapi`, and C# syntax blocks.

## Fast Commands

Find a symbol:

```bash
rg 'IModelDoc2\\.Save' 01_parsing_API/2024/llm_index/symbols.tsv
```

Find members of an interface:

```bash
rg '"interface": "IModelDoc2"' 01_parsing_API/2024/llm_index/interface_members.jsonl
```

Open a full document after lookup:

```bash
sed -n '1,220p' 01_parsing_API/2024/markdown/sldworksapi/<file>.md
```

Regenerate Markdown:

```bash
python3 01_parsing_API/scripts/convert_sw_api_docs.py 01_parsing_API/2024/API_HTML -o 01_parsing_API/2024/markdown
```

Regenerate the LLM index:

```bash
python3 01_parsing_API/scripts/build_llm_index.py 01_parsing_API/2024/markdown -o 01_parsing_API/2024/llm_index
```

## Answering Style

For API answers, cite the exact Markdown path used. Include VBA or C# snippets
only after checking the corresponding syntax section when possible.
