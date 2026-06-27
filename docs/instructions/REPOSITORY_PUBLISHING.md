# Repository Publishing

This guide separates public repository contents from private or release-only
artifacts.

## Commit To Git

Usually commit:

- `README.md`
- `README.ru.md`, if maintained
- `AGENTS.md`
- `LICENSE`
- `NOTICE.md`
- `docs/`
- `scripts/`
- `swapi_mcp/`
- `packaging/`
- `requirements.txt`
- `pyproject.toml`
- `versions/<year>/markdown/`, if publishing an example generated corpus
- `versions/<year>/llm_index/`, if publishing a ready-to-use index for that
  corpus

## Keep Private Or Release Separately

Do not normally commit:

- `versions/<year>/api/`
- `versions/<year>/extracted/`
- `versions/<year>/API_HTML/`
- local PostgreSQL data directories
- PyInstaller build directories
- release zips and database dumps

The public product should hide CHM parsing and index generation from end users.
For the installable MVP, publish only the MCP executable, PostgreSQL dump,
install scripts, and release README.

## Legal Notice

Project source code is MIT licensed. Generated Markdown may contain material
derived from official SOLIDWORKS API documentation. Keep [NOTICE.md](../../NOTICE.md)
visible in the repository and release materials.
