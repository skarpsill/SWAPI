# SOLIDWORKS API Versions

This directory stores generated API corpora by SOLIDWORKS release year.

```text
01_parsing_API/
  2022/
    api/        # source CHM files, local only
    extracted/  # full CHM extraction, generated
    API_HTML/   # collected HTML files, generated
    markdown/   # converted Markdown docs
    llm_index/  # generated lookup and graph indexes
  2023/
  2024/         # currently included corpus
  2025/
  2026/
```

The default MCP and PostgreSQL loader version is `2024`. Set
`SWAPI_DEFAULT_VERSION` or pass `--version` to work with another release.
