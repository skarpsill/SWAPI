"""MCP server for SOLIDWORKS API documentation-assisted code writing.

This server is intentionally documentation-only: it never connects to
SOLIDWORKS, never executes macros, and never touches user CAD files. Its job is
to help an IDE agent find the right API symbols, signatures, examples, related
topics, and versioned documentation before writing VBA/C# code.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .config import load_settings
from .local_index import LocalIndex
from .postgres_index import PostgresIndex

mcp = FastMCP(
    "solidworks-api",
    instructions=(
        "Use this server only as a SOLIDWORKS API knowledge source for writing "
        "VBA macros, C# add-ins, and related automation code. Do not attempt to "
        "control SOLIDWORKS through this server. Start with swapi_search_symbols "
        "or swapi_lookup_method, then read the exact document with swapi_get_doc. "
        "Prefer *apivb6 modules for VBA macros and .NET modules for C# add-ins. "
        "Check remarks, parameters, examples, and related symbols before emitting code."
    ),
)

def _make_index():
    settings = load_settings()
    if settings.database_url:
        return PostgresIndex(settings)
    return LocalIndex(settings)


_index = _make_index()


@mcp.tool()
def swapi_status() -> dict:
    """Report the configured local SOLIDWORKS API knowledge corpus."""
    return _index.status()


@mcp.tool()
def swapi_search_symbols(
    query: str,
    module: str = "",
    kind: str = "",
    language: str = "",
    limit: int = 20,
) -> dict:
    """Search API symbols by name/title/path.

    Examples: query='FeatureExtrusion3', query='IModelDoc2.Save3',
    query='swOpenDocOptions_e'. Use language='vba' to prefer VB6/VBA modules or
    language='csharp' for .NET-oriented docs.
    """
    return _index.search_symbols(query, module=module, kind=kind, language=language, limit=limit)


@mcp.tool()
def swapi_lookup_symbol(symbol_or_id: str, limit: int = 10) -> dict:
    """Resolve an exact API symbol, index id, or Markdown path to candidate docs."""
    return _index.lookup_symbol(symbol_or_id, limit=limit)


@mcp.tool()
def swapi_lookup_method(interface: str, method: str, language: str = "", limit: int = 10) -> dict:
    """Find a method by interface and method name, e.g. IFeatureManager + FeatureExtrusion3."""
    query = f"{interface.rstrip('.')}.{method}"
    result = _index.search_symbols(query, kind="method", language=language, limit=limit)
    if not result["hits"]:
        result = _index.search_symbols(method, kind="method", language=language, limit=limit)
    result["interface"] = interface
    result["method"] = method
    return result


@mcp.tool()
def swapi_lookup_enum(enum_name: str, limit: int = 10) -> dict:
    """Find an enum topic, e.g. swOpenDocOptions_e."""
    return _index.search_symbols(enum_name, kind="enum", limit=limit)


@mcp.tool()
def swapi_interface_members(interface: str, module: str = "") -> dict:
    """Return the compact member list for an interface/object/class."""
    return _index.interface_members(interface, module=module)


@mcp.tool()
def swapi_get_doc(path_or_id: str, max_chars: int = 30000) -> dict:
    """Read a narrowed Markdown document by path, id, or exact symbol.

    Use this only after a symbol search or interface member lookup narrows the
    candidate set.
    """
    return _index.get_document(path_or_id, max_chars=max_chars)


@mcp.tool()
def swapi_neighbors(
    symbol_or_id: str,
    edge_type: str = "",
    direction: str = "both",
    limit: int = 50,
) -> dict:
    """Return graph edges around a symbol/id.

    edge_type can be has_member, member_of, or links_to. direction can be both,
    in, or out.
    """
    return _index.neighbors(symbol_or_id, edge_type=edge_type, direction=direction, limit=limit)


@mcp.tool()
def swapi_find_examples(query: str, language: str = "", limit: int = 20) -> dict:
    """Find example topics relevant to a task or symbol."""
    return _index.find_examples(query, language=language, limit=limit)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
