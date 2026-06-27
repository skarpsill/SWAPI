# Build Pipeline

Это руководство для maintainers, которые пересобирают сгенерированный корпус
SOLIDWORKS API. Конечным пользователям Windows MCP package эти шаги не нужны.

[English version](../BUILD_PIPELINE.md)

## Зависимости

Установите Python dependencies:

```bash
python3 -m pip install -r requirements.txt
python3 -m pip install -e ".[postgres,release]"
```

Для извлечения CHM установите `extract_chmLib` из `chmlib`.

Debian или Ubuntu:

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

Проверка extractor:

```bash
which extract_chmLib
extract_chmLib 2>&1 | head
```

## 1. Добавить CHM files

Положите SOLIDWORKS API CHM files для нужного года в versioned input folder:

```text
versions/2024/api/
```

Пример:

```text
versions/2024/api/sldworksapi.chm
versions/2024/api/sldworksapivb6.chm
versions/2024/api/swconst.chm
versions/2024/api/cworksapi.chm
```

## 2. Рекурсивно извлечь CHM

```bash
./scripts/unpack_chm_recursive.sh versions/2024/api versions/2024/extracted
```

Скрипт выполняет несколько проходов, потому что SOLIDWORKS API CHM files могут
содержать вложенные CHM files.

## 3. Собрать только HTML

```bash
python3 scripts/collect_html.py versions/2024/extracted -o versions/2024/API_HTML --clean
```

Этот шаг оставляет только `.htm` и `.html` files, сохраняя исходную структуру
каталогов.

## 4. Конвертировать HTML в Markdown

```bash
python3 scripts/convert_sw_api_docs.py versions/2024/API_HTML -o versions/2024/markdown
```

Конвертер специализирован под формат SOLIDWORKS/Innovasys help. Он удаляет
служебную навигацию, сохраняет headings и tables, превращает syntax blocks в
fenced code blocks, добавляет YAML metadata и сохраняет related links.

## 5. Построить LLM index

```bash
python3 scripts/build_llm_index.py versions/2024/markdown -o versions/2024/llm_index
```

Индекс является navigation layer, а не полноценной RAG database. Он позволяет
агенту сначала найти symbols, затем изучить interfaces и relationships, и только
после сужения кандидатов открыть full Markdown files.

## 6. Загрузить PostgreSQL

Создайте database и загрузите generated files:

```bash
createdb solidworks_api
swapi-load-postgres \
  --database-url postgresql:///solidworks_api \
  --version 2024 \
  --root .
```

Loader импортирует documents, symbols, interface members и graph edges из
`versions/<year>/llm_index/`, а также full Markdown text из
`versions/<year>/markdown/`.

## Проверка

```bash
python3 -m compileall swapi_mcp scripts
rg 'IModelDoc2\\.Save' versions/2024/llm_index/symbols.tsv
rg '"interface": "IModelDoc2"' versions/2024/llm_index/interface_members.jsonl
```
