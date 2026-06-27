# Instruction Hub

This folder contains the project documentation for the SOLIDWORKS API Knowledge
Base and its MCP server.

[Русская версия](ru/README.md)

## Guides

- [Project overview](PROJECT_OVERVIEW.md) - what the project contains, how the
  parts fit together, and which artifacts are public.
- [Build pipeline](BUILD_PIPELINE.md) - how maintainers rebuild the corpus from
  SOLIDWORKS API CHM files.
- [Using the knowledge base](USING_KNOWLEDGE_BASE.md) - how Codex, agents, and
  humans should navigate the generated Markdown and LLM indexes.
- [Windows release](WINDOWS_RELEASE.md) - how to build, install, configure, and
  publish the Windows MCP package.
- [Repository publishing](REPOSITORY_PUBLISHING.md) - what should live in Git
  and what should remain private or be published as release assets.

## Related Reference

- [MCP server reference](../MCP_SERVER.md)
- [Product release plan](../PRODUCT_RELEASE.md)
- [Script reference](../../scripts/README.md)
- [Agent instructions](../../AGENTS.md)

## Recommended Reading Order

1. Read [Project overview](PROJECT_OVERVIEW.md) to understand the architecture.
2. Read [Using the knowledge base](USING_KNOWLEDGE_BASE.md) if you want Codex or
   another agent to answer SOLIDWORKS API questions from this repository.
3. Read [Build pipeline](BUILD_PIPELINE.md) only if you maintain or regenerate
   the documentation corpus.
4. Read [Windows release](WINDOWS_RELEASE.md) when preparing an installable MCP
   package.
