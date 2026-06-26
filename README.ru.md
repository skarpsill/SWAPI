# SOLIDWORKS API Knowledge Base for Codex

Language: [English](README.md) | Русский

Проект превращает официальную документацию SOLIDWORKS API из `.chm` в локальную базу Markdown-документов и компактный индекс для Codex/LLM-агентов.

Цель: быстро писать VBA-макросы и C# add-in приложения, не загружая в контекст десятки тысяч файлов документации.

Этот публичный репозиторий содержит скрипты пайплайна, пример готового `markdown/` корпуса и готовый `llm_index/`, сгенерированные на основе SOLIDWORKS API 2024. Оригинальные `.chm` файлы и промежуточные HTML-файлы не публикуются.

Код проекта распространяется под MIT License и может использоваться в коммерческих проектах. Сгенерированный Markdown может содержать материалы, производные от официальной документации SOLIDWORKS API; см. [NOTICE.md](NOTICE.md).

## Что получается

- `API_HTML/` - HTML-файлы, извлечённые из CHM, без картинок/CSS/JS.
- `markdown/` - Markdown-документация, один файл на один логический API-объект.
- `llm_index/` - компактные индексы и граф связей для быстрого поиска.
- `AGENTS.md` - инструкция для Codex, как пользоваться индексом и не тратить контекст.

## Структура проекта

```text
.
├── api/                  # исходные .chm файлы конкретной версии SOLIDWORKS API
├── extracted/            # полная распаковка CHM, генерируется
├── API_HTML/             # только .htm/.html, генерируется
├── markdown/             # Markdown-документация, публикуется как пример SOLIDWORKS API 2024
├── llm_index/            # индекс для Codex/LLM, публикуется как пример SOLIDWORKS API 2024
├── scripts/
│   ├── unpack_chm_recursive.sh
│   ├── collect_html.py
│   ├── convert_sw_api_docs.py
│   └── build_llm_index.py
├── AGENTS.md
├── NOTICE.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Зависимости

Python:

```bash
python3 -m pip install -r requirements.txt
```

Для распаковки CHM нужен `extract_chmLib` из `chmlib`.

Debian/Ubuntu:

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

Проверка:

```bash
which extract_chmLib
extract_chmLib 2>&1 | head
```

Если пакет в вашем дистрибутиве не содержит `extract_chmLib`, установите `chmlib` из исходников или используйте любой совместимый CHM extractor, который умеет команду вида:

```bash
extract_chmLib input.chm output_directory
```

## Полный пайплайн

### 1. Положить CHM

Сложите `.chm` файлы нужной версии SOLIDWORKS API в папку:

```text
api/
```

Пример:

```text
api/sldworksapi.chm
api/sldworksapivb6.chm
api/swconst.chm
api/cworksapi.chm
```

### 2. Распаковать CHM рекурсивно

```bash
./scripts/unpack_chm_recursive.sh api extracted
```

Скрипт делает несколько проходов, потому что внутри CHM могут лежать вложенные `.chm`.

### 3. Собрать только HTML

```bash
python3 scripts/collect_html.py extracted -o API_HTML --clean
```

Этот шаг удаляет картинки, CSS, JS и оставляет только `.htm/.html`, сохраняя структуру каталогов.

### 4. Конвертировать HTML в Markdown

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown
```

Конвертер специализирован под формат SOLIDWORKS/Innovasys help:

- удаляет служебную навигацию;
- сохраняет заголовки, секции, таблицы, списки;
- превращает блоки Syntax в fenced code blocks;
- добавляет YAML-метаданные;
- сохраняет связи через Markdown-ссылки.

### 5. Построить индекс для Codex/LLM

```bash
python3 scripts/build_llm_index.py markdown -o llm_index
```

Индекс нужен не для RAG, а для дешёвой навигации:

- сначала найти символ;
- затем найти интерфейс/соседей;
- затем открыть только нужные Markdown-файлы.

## Быстрая проверка

```bash
find markdown -type f -name '*.md' | wc -l
find llm_index -maxdepth 1 -type f | sort
rg 'IModelDoc2\\.Save' llm_index/symbols.tsv
```

## Как подключать к Codex в VSCode/VSCodium

Откройте корень этого проекта как workspace или добавьте его как вторую папку в multi-root workspace рядом с вашим VBA/C# проектом.

Codex должен видеть:

- `AGENTS.md`
- `llm_index/`
- `markdown/`

Пример запроса:

```text
Use the SOLIDWORKS API knowledge base in this workspace.
Follow AGENTS.md.
I am writing a VBA macro. Find the correct API docs before writing code.
```

Для C# add-in:

```text
Follow AGENTS.md.
I am writing a C# SOLIDWORKS add-in.
Prefer .NET API docs and C# syntax blocks.
```

## Как пользоваться индексом вручную

Найти символ:

```bash
rg 'IModelDoc2\\.Save' llm_index/symbols.tsv
```

Найти члены интерфейса:

```bash
rg '"interface": "IModelDoc2"' llm_index/interface_members.jsonl
```

Открыть найденный документ:

```bash
sed -n '1,220p' markdown/sldworksapi/<file>.md
```

## Файлы индекса

- `manifest.json` - общая статистика корпуса.
- `symbols.tsv` - самый дешёвый поиск по API-символам.
- `documents.tsv` - быстрый поиск по документам.
- `symbols.jsonl` - структурный symbol lookup.
- `documents.jsonl` - компактная карточка каждого Markdown-файла.
- `nodes.jsonl` - узлы графа.
- `edges/` - разбитые по исходному модулю связи графа `has_member`, `member_of`, `links_to`.
- `edges_manifest.json` - количество связей по shard-файлам и типам.
- `interface_members.jsonl` - интерфейс/объект -> методы/свойства.
- `modules.json` - статистика по модулям API.

## Рекомендации для GitHub

Обычно в репозиторий стоит коммитить:

- `scripts/`
- `README.md`
- `AGENTS.md`
- `LICENSE`
- `NOTICE.md`
- `requirements.txt`
- `markdown/`, если вы осознанно публикуете готовый пример корпуса для конкретной версии API
- `llm_index/`, если вы осознанно публикуете готовый индекс для включённого Markdown-корпуса

А большие/воспроизводимые артефакты держать вне Git или публиковать отдельно:

- `api/`
- `extracted/`
- `API_HTML/`

Если не хотите хранить сгенерированные данные в Git-истории, публикуйте `markdown/` и `llm_index/` как release artifacts.
