# Build Pipeline

This guide is for maintainers who rebuild the generated SOLIDWORKS API corpus.
End users of the Windows MCP package should not need these steps.

## Dependencies

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
python3 -m pip install -e ".[postgres,release]"
```

To extract CHM files, install `extract_chmLib` from `chmlib`.

Debian or Ubuntu:

```bash
sudo apt install libchm-bin
```

Fedora:

```bash
sudo dnf install chmlib
```

Arch Linux:

```bash
sudo pacman -S chmlib
```

Check the extractor:

```bash
which extract_chmLib
extract_chmLib 2>&1 | head
```

## 1. Add CHM Files

Put the SOLIDWORKS API CHM files for the target year into the versioned input
folder:

```text
versions/2024/api/
```

Example:

```text
versions/2024/api/sldworksapi.chm
versions/2024/api/sldworksapivb6.chm
versions/2024/api/swconst.chm
versions/2024/api/cworksapi.chm
```

## 2. Extract CHM Recursively

```bash
./scripts/unpack_chm_recursive.sh versions/2024/api versions/2024/extracted
```

The script performs multiple passes because SOLIDWORKS API CHM files can contain
nested CHM files.

## 3. Collect HTML Only

```bash
python3 scripts/collect_html.py versions/2024/extracted -o versions/2024/API_HTML --clean
```

This keeps only `.htm` and `.html` files while preserving the source directory
layout.

## 4. Convert HTML to Markdown

```bash
python3 scripts/convert_sw_api_docs.py versions/2024/API_HTML -o versions/2024/markdown
```

The converter is specialized for the SOLIDWORKS/Innovasys help format. It
removes service navigation, preserves headings and tables, converts syntax
blocks to fenced code blocks, adds YAML metadata, and keeps related links.

## 5. Build the LLM Index

```bash
python3 scripts/build_llm_index.py versions/2024/markdown -o versions/2024/llm_index
```

The index is a navigation layer, not a full RAG database. It lets an agent find
symbols first, inspect interfaces and relationships second, and open full
Markdown files only after narrowing the candidate set.

## 6. Load PostgreSQL

Create a database and load the generated files:

```bash
createdb solidworks_api
swapi-load-postgres \
  --database-url postgresql:///solidworks_api \
  --version 2024 \
  --root .
```

The loader imports documents, symbols, interface members, and graph edges from
`versions/<year>/llm_index/` plus full Markdown text from
`versions/<year>/markdown/`.

## Validation

```bash
python3 -m compileall swapi_mcp scripts
rg 'IModelDoc2\\.Save' versions/2024/llm_index/symbols.tsv
rg '"interface": "IModelDoc2"' versions/2024/llm_index/interface_members.jsonl
```
