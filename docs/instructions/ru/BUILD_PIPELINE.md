# Build Pipeline

[English version](../BUILD_PIPELINE.md)

Эта инструкция нужна maintainer-части проекта. Конечному пользователю MCP
package эти шаги не нужны.

## Зависимости

```bash
python3 -m pip install -r requirements.txt
python3 -m pip install -e ".[postgres,release]"
```

Для CHM extraction нужен `extract_chmLib` из `chmlib`.

## Полный pipeline

Положить CHM files:

```text
01_parsing_API/2024/api/
```

Извлечь CHM:

```bash
./01_parsing_API/scripts/unpack_chm_recursive.sh 01_parsing_API/2024/api 01_parsing_API/2024/extracted
```

Собрать только HTML:

```bash
python3 01_parsing_API/scripts/collect_html.py 01_parsing_API/2024/extracted -o 01_parsing_API/2024/API_HTML --clean
```

Конвертировать HTML в Markdown:

```bash
python3 01_parsing_API/scripts/convert_sw_api_docs.py 01_parsing_API/2024/API_HTML -o 01_parsing_API/2024/markdown
```

Построить LLM index:

```bash
python3 01_parsing_API/scripts/build_llm_index.py 01_parsing_API/2024/markdown -o 01_parsing_API/2024/llm_index
```

Загрузить PostgreSQL:

```bash
swapi-load-postgres \
  --database-url postgresql:///solidworks_api \
  --version 2024 \
  --root .
```

## Проверка

```bash
python3 -m compileall 02_mcp_server/swapi_mcp 01_parsing_API/scripts
rg 'IModelDoc2\\.Save' 01_parsing_API/2024/llm_index/symbols.tsv
```
