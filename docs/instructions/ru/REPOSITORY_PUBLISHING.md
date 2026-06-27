# Публикация репозитория

[English version](../REPOSITORY_PUBLISHING.md)

## Обычно коммитим

- `README.md`
- `README.ru.md`
- `AGENTS.md`
- `docs/`
- `01_parsing_API/scripts/`
- `01_parsing_API/<year>/markdown/`, если corpus публикуется
- `01_parsing_API/<year>/llm_index/`, если index публикуется
- `02_mcp_server/swapi_mcp/`
- `02_mcp_server/packaging/`
- `pyproject.toml`
- `requirements.txt`
- `LICENSE`
- `NOTICE.md`

## Обычно не коммитим

- `.venv/`
- `__pycache__/`
- `*.egg-info/`
- `*.spec`
- `02_mcp_server/dist/`
- `01_parsing_API/release-assets/`
- `01_parsing_API/<year>/api/`
- `01_parsing_API/<year>/extracted/`
- `01_parsing_API/<year>/API_HTML/`

Публичный продукт должен скрывать CHM parsing и generation pipeline от конечного
пользователя. В release достаточно exe, PostgreSQL dump, install scripts и
README.
