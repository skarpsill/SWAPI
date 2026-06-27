# SOLIDWORKS API Knowledge Base for Codex

Язык: [English](README.md) | Русский

Репозиторий разделён на две главные зоны:

- `01_parsing_API/` - maintainer tooling и сгенерированный корпус SOLIDWORKS API.
- `02_mcp_server/` - конечный MCP server product и release packaging.

Проект помогает Codex и другим LLM-агентам отвечать на вопросы по SOLIDWORKS API
и писать VBA-макросы или C# add-ins без сканирования десятков тысяч Markdown
файлов.

## С чего начать

- [Карта проекта](docs/PROJECT_MAP.md) - подробная карта папок, файлов и связей.
- [Папка инструкций](docs/instructions/README.md) - полный английский набор
  инструкций.
- [Папка инструкций на русском](docs/instructions/ru/README.md) - русская копия
  инструкций.
- [MCP server reference](docs/MCP_SERVER.md) - режимы сервера, tools и config.
- [Product release plan](docs/PRODUCT_RELEASE.md) - flow Windows package.

## Что внутри

- `01_parsing_API/2024/markdown/` - сгенерированная Markdown-документация API.
- `01_parsing_API/2024/llm_index/` - компактные lookup и relationship индексы.
- `01_parsing_API/scripts/` - maintainer pipeline scripts для пересборки
  корпуса.
- `02_mcp_server/swapi_mcp/` - MCP server package и PostgreSQL schema.
- `02_mcp_server/packaging/windows/` - Windows release и install scripts.
- `AGENTS.md` - локальные инструкции для Codex при использовании репозитория как
  workspace knowledge base.

Оригинальные `.chm` files и промежуточный extracted HTML не публикуются. Код
проекта распространяется по MIT license. Generated Markdown может содержать
материалы, производные от официальной документации SOLIDWORKS API; см.
[NOTICE.md](NOTICE.md).

## Быстрое использование

Откройте этот репозиторий как workspace или добавьте его второй папкой рядом с
вашим SOLIDWORKS VBA/C# project. Попросите Codex следовать `AGENTS.md` перед
написанием кода.

Подробные workflows лежат в [docs/instructions](docs/instructions/README.md).
