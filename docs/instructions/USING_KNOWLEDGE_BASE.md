# Using The Knowledge Base

This guide explains how humans and agents should navigate the generated
SOLIDWORKS API documentation.

## Agent Rule

Do not scan all Markdown files. Start with compact indexes, then open the full
topic only after narrowing the target.

Recommended flow:

1. Search `01_parsing_API/2024/llm_index/symbols.tsv` for an exact or substring API
   symbol match.
2. Use `01_parsing_API/2024/llm_index/interface_members.jsonl` when the question is
   about an interface, object, class, or available members.
3. Use `01_parsing_API/2024/llm_index/edges/` only after a small candidate set has
   been identified.
4. Open files from `01_parsing_API/2024/markdown/` only after lookup.
5. Prefer the API flavor that matches the task:
   - VBA macros: `*apivb6` modules and VBA syntax blocks.
   - C# add-ins: .NET modules such as `sldworksapi`, `cworksapi`,
     `swdocmgrapi`, and C# syntax blocks.

## Manual Lookup Commands

Find a symbol:

```bash
rg 'IModelDoc2\\.Save' 01_parsing_API/2024/llm_index/symbols.tsv
```

Find members of an interface:

```bash
rg '"interface": "IModelDoc2"' 01_parsing_API/2024/llm_index/interface_members.jsonl
```

Open a narrowed document:

```bash
sed -n '1,220p' 01_parsing_API/2024/markdown/sldworksapi/<file>.md
```

## Index Files

- `manifest.json` - corpus summary.
- `symbols.tsv` - cheapest symbol lookup.
- `documents.tsv` - fast document lookup.
- `symbols.jsonl` - structured symbol lookup.
- `documents.jsonl` - compact card for each Markdown file.
- `nodes.jsonl` - graph nodes.
- `edges/` - sharded `has_member`, `member_of`, and `links_to` graph edges.
- `edges_manifest.json` - edge shard counts and type summaries.
- `interface_members.jsonl` - interface/object to methods and properties.
- `modules.json` - API module statistics.

## Using With Codex

Open this repository as a workspace, or add it as a second folder in a
multi-root workspace next to your SOLIDWORKS macro or add-in project.

Codex should be able to see:

```text
AGENTS.md
01_parsing_API/2024/llm_index/
01_parsing_API/2024/markdown/
```

Example prompt for a VBA macro:

```text
Use the SOLIDWORKS API knowledge base in this workspace.
Follow AGENTS.md.
I am writing a VBA macro. Find the correct API docs before writing code.
```

Example prompt for a C# add-in:

```text
Follow AGENTS.md.
I am writing a C# SOLIDWORKS add-in.
Prefer .NET API docs and C# syntax blocks.
```

## Using The MCP Server

The MCP server exposes the same lookup flow through tools such as
`swapi_search_symbols`, `swapi_interface_members`, `swapi_get_doc`, and
`swapi_neighbors`.

See [MCP server reference](../MCP_SERVER.md) for config examples and the full
tool list.
