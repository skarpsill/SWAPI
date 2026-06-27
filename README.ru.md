# SOLIDWORKS API Knowledge Base for Codex

Язык: [English](README.md) | Русский

Этот репозиторий содержит локальную базу знаний SOLIDWORKS API для Codex и
других LLM-агентов. Внутри есть сгенерированный Markdown-корпус SOLIDWORKS API
2024, компактные индексы для поиска, documentation-only MCP server и tooling для
Windows-релиза с PostgreSQL.

Проект помогает агенту писать VBA-макросы и C# add-in приложения, не загружая в
контекст десятки тысяч файлов API-документации.

## С чего начать

- [Папка инструкций](docs/instructions/README.md) - полная документация проекта
  и практические руководства.
- [Папка инструкций на русском](docs/instructions/ru/README.md) - русская копия
  набора инструкций.
- [Обзор проекта](docs/instructions/PROJECT_OVERVIEW.md) - архитектура,
  структура репозитория, поток данных и артефакты.
- [Build pipeline](docs/instructions/BUILD_PIPELINE.md) - извлечение CHM,
  конвертация в Markdown, генерация LLM index и загрузка в PostgreSQL.
- [Использование базы знаний](docs/instructions/USING_KNOWLEDGE_BASE.md) -
  ручной поиск по индексам и рекомендуемый flow для агентов.
- [Windows release](docs/instructions/WINDOWS_RELEASE.md) - сборка, установка,
  настройка и публикация Windows MCP package.
- [MCP server](docs/MCP_SERVER.md) - режимы сервера, переменные окружения,
  tools и примеры конфигурации.

## Что внутри

- `versions/2024/markdown/` - сгенерированная Markdown-документация API.
- `versions/2024/llm_index/` - компактные lookup и relationship индексы.
- `swapi_mcp/` - MCP server, local index backend, PostgreSQL backend и SQL
  schema.
- `scripts/` - maintainer pipeline scripts для пересборки корпуса.
- `packaging/windows/` - Windows release packaging и install scripts.
- `AGENTS.md` - локальные инструкции для Codex при использовании репозитория как
  workspace knowledge base.

Оригинальные `.chm` файлы и промежуточный HTML не публикуются. Код проекта
распространяется по MIT License. Сгенерированный Markdown может содержать
материалы, производные от официальной документации SOLIDWORKS API; см.
[NOTICE.md](NOTICE.md).

## Быстрое использование

Откройте этот репозиторий как workspace или добавьте его второй папкой рядом с
вашим SOLIDWORKS VBA/C# проектом. Попросите Codex следовать `AGENTS.md` перед
написанием кода.

Подробные команды и сценарии находятся в
[папке инструкций](docs/instructions/README.md).
