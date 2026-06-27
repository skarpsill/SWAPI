# Использование базы знаний

[English version](../USING_KNOWLEDGE_BASE.md)

Главное правило: не сканировать все Markdown files. Сначала найти нужный символ
в компактном индексе, потом открыть только конкретный документ.

## Рекомендуемый flow

1. Искать символ в `01_parsing_API/2024/llm_index/symbols.tsv`.
2. Для interface/object/class смотреть
   `01_parsing_API/2024/llm_index/interface_members.jsonl`.
3. Related topics смотреть через `01_parsing_API/2024/llm_index/edges/`.
4. Полный документ открывать из `01_parsing_API/2024/markdown/`.
5. Для VBA предпочитать `*apivb6`, для C# - .NET modules вроде
   `sldworksapi`, `cworksapi`, `swdocmgrapi`.

## Быстрые команды

```bash
rg 'IModelDoc2\\.Save' 01_parsing_API/2024/llm_index/symbols.tsv
rg '"interface": "IModelDoc2"' 01_parsing_API/2024/llm_index/interface_members.jsonl
sed -n '1,220p' 01_parsing_API/2024/markdown/sldworksapi/<file>.md
```

## Через MCP server

MCP server даёт тот же flow через tools:

- `swapi_search_symbols`
- `swapi_interface_members`
- `swapi_get_doc`
- `swapi_neighbors`
- `swapi_find_examples`

Подробности: [MCP server reference](../../MCP_SERVER.md).
