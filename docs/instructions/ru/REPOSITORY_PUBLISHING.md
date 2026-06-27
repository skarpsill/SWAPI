# Публикация репозитория

Это руководство разделяет содержимое public repository и private или
release-only artifacts.

[English version](../REPOSITORY_PUBLISHING.md)

## Коммитить в Git

Обычно стоит коммитить:

- `README.md`
- `README.ru.md`, если поддерживается
- `AGENTS.md`
- `LICENSE`
- `NOTICE.md`
- `docs/`
- `scripts/`
- `swapi_mcp/`
- `packaging/`
- `requirements.txt`
- `pyproject.toml`
- `versions/<year>/markdown/`, если публикуется example generated corpus
- `versions/<year>/llm_index/`, если публикуется ready-to-use index для этого
  corpus

## Держать приватно или публиковать отдельно

Обычно не стоит коммитить:

- `versions/<year>/api/`
- `versions/<year>/extracted/`
- `versions/<year>/API_HTML/`
- local PostgreSQL data directories
- PyInstaller build directories
- release zips и database dumps

Публичный продукт должен скрывать CHM parsing и index generation от конечных
пользователей. Для installable MVP публикуйте только MCP executable, PostgreSQL
dump, install scripts и release README.

## Legal notice

Project source code распространяется по MIT license. Generated Markdown может
содержать материалы, производные от официальной документации SOLIDWORKS API.
Оставляйте [NOTICE.md](../../../NOTICE.md) видимым в repository и release
materials.
