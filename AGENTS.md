# SolidWorks API Knowledge Base

This workspace contains converted SOLIDWORKS API documentation for fast local use by Codex.

## Documentation Layout

- `versions/<year>/API_HTML/` contains the original extracted HTML sources.
- `versions/<year>/markdown/` contains converted Markdown documentation, one logical API topic per file.
- `versions/<year>/llm_index/` contains compact lookup and graph indexes for low-token navigation.
- The currently included corpus is `versions/2024/`.
- `scripts/unpack_chm_recursive.sh` recursively extracts CHM files from `versions/<year>/api/` to `versions/<year>/extracted/`.
- `scripts/collect_html.py` copies only HTML files from `versions/<year>/extracted/` to `versions/<year>/API_HTML/`.
- `scripts/convert_sw_api_docs.py` regenerates `versions/<year>/markdown/` from `versions/<year>/API_HTML/`.
- `scripts/build_llm_index.py` regenerates `versions/<year>/llm_index/` from `versions/<year>/markdown/`.

## How To Use This Context

When answering SOLIDWORKS API, VBA macro, or C# add-in questions:

1. Do not scan all Markdown files.
2. Start with `versions/2024/llm_index/symbols.tsv` for exact or substring API symbol lookup unless another version is requested.
3. Use `versions/2024/llm_index/interface_members.jsonl` when the user asks about an interface, object, class, or available members.
4. Use `versions/2024/llm_index/edges/` only after identifying a small candidate set and needing See Also / related topics.
5. Open full files from `versions/2024/markdown/` only after narrowing the candidates.
6. Prefer the API flavor that matches the task:
   - VBA macros: `*apivb6` modules and VBA syntax blocks.
   - C# add-ins: .NET modules such as `sldworksapi`, `cworksapi`, `swdocmgrapi`, and C# syntax blocks.

## Fast Commands

Find a symbol:

```bash
rg 'IModelDoc2\\.Save' versions/2024/llm_index/symbols.tsv
```

Find members of an interface:

```bash
rg '"interface": "IModelDoc2"' versions/2024/llm_index/interface_members.jsonl
```

Open a full document after lookup:

```bash
sed -n '1,220p' versions/2024/markdown/sldworksapi/<file>.md
```

Regenerate Markdown:

```bash
python3 scripts/convert_sw_api_docs.py versions/2024/API_HTML -o versions/2024/markdown
```

Regenerate the LLM index:

```bash
python3 scripts/build_llm_index.py versions/2024/markdown -o versions/2024/llm_index
```

## Answering Style

For API answers, cite the exact Markdown path used. Include VBA or C# snippets only after checking the corresponding syntax section when possible.
