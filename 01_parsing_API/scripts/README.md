# Scripts

Pipeline order:

```bash
./01_parsing_API/scripts/unpack_chm_recursive.sh 01_parsing_API/2024/api 01_parsing_API/2024/extracted
python3 01_parsing_API/scripts/collect_html.py 01_parsing_API/2024/extracted -o 01_parsing_API/2024/API_HTML --clean
python3 01_parsing_API/scripts/convert_sw_api_docs.py 01_parsing_API/2024/API_HTML -o 01_parsing_API/2024/markdown
python3 01_parsing_API/scripts/build_llm_index.py 01_parsing_API/2024/markdown -o 01_parsing_API/2024/llm_index
```

## `unpack_chm_recursive.sh`

Recursively extracts `.chm` files.

Default input/output:

```bash
./01_parsing_API/scripts/unpack_chm_recursive.sh api extracted
```

The script runs multiple passes because extracted CHM files can contain nested CHM files.

Requires `extract_chmLib`.

## `collect_html.py`

Copies only `.htm` and `.html` files from the extracted tree.

```bash
python3 01_parsing_API/scripts/collect_html.py extracted -o API_HTML --clean
```

## `convert_sw_api_docs.py`

Converts SOLIDWORKS API HTML pages into LLM-friendly Markdown.

```bash
python3 01_parsing_API/scripts/convert_sw_api_docs.py API_HTML -o markdown
```

Useful smoke test:

```bash
python3 01_parsing_API/scripts/convert_sw_api_docs.py API_HTML -o /tmp/sw_md --limit 20
```

## `build_llm_index.py`

Builds compact lookup and graph indexes over the Markdown corpus.

```bash
python3 01_parsing_API/scripts/build_llm_index.py markdown -o llm_index
```
