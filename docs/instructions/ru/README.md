# Центр инструкций

Эта папка содержит русскую версию документации проекта SOLIDWORKS API Knowledge
Base и его MCP server.

[English version](../README.md)

## Руководства

- [Обзор проекта](PROJECT_OVERVIEW.md) - что содержит проект, как части связаны
  между собой и какие артефакты публикуются.
- [Build pipeline](BUILD_PIPELINE.md) - как maintainers пересобирают корпус из
  SOLIDWORKS API CHM files.
- [Использование базы знаний](USING_KNOWLEDGE_BASE.md) - как Codex, агенты и
  люди должны пользоваться Markdown-корпусом и LLM index.
- [Windows release](WINDOWS_RELEASE.md) - как собрать, установить, настроить и
  опубликовать Windows MCP package.
- [Публикация репозитория](REPOSITORY_PUBLISHING.md) - что хранить в Git, а что
  оставлять приватным или публиковать как release assets.

## Связанные справочные материалы

- [MCP server reference](../../MCP_SERVER.md)
- [Product release plan](../../PRODUCT_RELEASE.md)
- [Script reference](../../../scripts/README.md)
- [Agent instructions](../../../AGENTS.md)

## Рекомендуемый порядок чтения

1. Прочитайте [Обзор проекта](PROJECT_OVERVIEW.md), чтобы понять архитектуру.
2. Прочитайте [Использование базы знаний](USING_KNOWLEDGE_BASE.md), если хотите
   использовать Codex или другого агента для ответов по SOLIDWORKS API.
3. Прочитайте [Build pipeline](BUILD_PIPELINE.md), только если вы поддерживаете
   или пересобираете корпус документации.
4. Прочитайте [Windows release](WINDOWS_RELEASE.md), когда готовите
   installable MCP package.
