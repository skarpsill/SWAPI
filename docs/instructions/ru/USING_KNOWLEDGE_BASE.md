# Использование базы знаний

Это руководство объясняет, как людям и агентам пользоваться сгенерированной
документацией SOLIDWORKS API.

[English version](../USING_KNOWLEDGE_BASE.md)

## Правило для агента

Не сканировать все Markdown files. Сначала использовать компактные индексы, и
только после сужения цели открывать полный topic.

Рекомендуемый flow:

1. Искать exact или substring API symbol match в
   `versions/2024/llm_index/symbols.tsv`.
2. Использовать `versions/2024/llm_index/interface_members.jsonl`, когда вопрос
   про interface, object, class или available members.
3. Использовать `versions/2024/llm_index/edges/` только после того, как найден
   небольшой candidate set.
4. Открывать files из `versions/2024/markdown/` только после lookup.
5. Предпочитать API flavor, подходящий задаче:
   - VBA macros: `*apivb6` modules и VBA syntax blocks.
   - C# add-ins: .NET modules вроде `sldworksapi`, `cworksapi`,
     `swdocmgrapi`, и C# syntax blocks.

## Команды ручного lookup

Найти symbol:

```bash
rg 'IModelDoc2\\.Save' versions/2024/llm_index/symbols.tsv
```

Найти members интерфейса:

```bash
rg '"interface": "IModelDoc2"' versions/2024/llm_index/interface_members.jsonl
```

Открыть narrowed document:

```bash
sed -n '1,220p' versions/2024/markdown/sldworksapi/<file>.md
```

## Index files

- `manifest.json` - corpus summary.
- `symbols.tsv` - самый дешевый symbol lookup.
- `documents.tsv` - быстрый document lookup.
- `symbols.jsonl` - structured symbol lookup.
- `documents.jsonl` - compact card для каждого Markdown file.
- `nodes.jsonl` - graph nodes.
- `edges/` - sharded `has_member`, `member_of` и `links_to` graph edges.
- `edges_manifest.json` - edge shard counts и type summaries.
- `interface_members.jsonl` - interface/object to methods and properties.
- `modules.json` - API module statistics.

## Использование с Codex

Откройте этот репозиторий как workspace или добавьте его второй папкой в
multi-root workspace рядом с вашим SOLIDWORKS macro или add-in project.

Codex должен видеть:

```text
AGENTS.md
versions/2024/llm_index/
versions/2024/markdown/
```

Пример prompt для VBA macro:

```text
Use the SOLIDWORKS API knowledge base in this workspace.
Follow AGENTS.md.
I am writing a VBA macro. Find the correct API docs before writing code.
```

Пример prompt для C# add-in:

```text
Follow AGENTS.md.
I am writing a C# SOLIDWORKS add-in.
Prefer .NET API docs and C# syntax blocks.
```

## Использование MCP server

MCP server открывает тот же lookup flow через tools вроде
`swapi_search_symbols`, `swapi_interface_members`, `swapi_get_doc` и
`swapi_neighbors`.

Смотрите [MCP server reference](../../MCP_SERVER.md) для config examples и
полного списка tools.
