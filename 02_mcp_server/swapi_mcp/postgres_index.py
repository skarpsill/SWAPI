"""PostgreSQL-backed SOLIDWORKS API knowledge index."""

from __future__ import annotations

from .config import Settings, load_settings


class PostgresIndex:
    """Reader with the same public surface as LocalIndex."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or load_settings()
        if not self.settings.database_url:
            raise ValueError("DATABASE_URL or SWAPI_DATABASE_URL is required")
        try:
            import psycopg
            from psycopg.rows import dict_row
        except ImportError as exc:
            raise RuntimeError("Install PostgreSQL support with: python -m pip install 'psycopg[binary]>=3.1'") from exc
        self._psycopg = psycopg
        self._dict_row = dict_row

    def _connect(self):
        return self._psycopg.connect(self.settings.database_url, row_factory=self._dict_row)

    def _version_id(self, cur) -> int | None:
        cur.execute("SELECT id FROM api_versions WHERE version = %s", (self.settings.default_version,))
        row = cur.fetchone()
        return int(row["id"]) if row else None

    def status(self) -> dict:
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                return {
                    "backend": "postgres",
                    "ready": False,
                    "version": self.settings.default_version,
                    "error": "version not loaded",
                }
            cur.execute("SELECT count(*) AS n FROM documents WHERE version_id = %s", (vid,))
            documents = cur.fetchone()["n"]
            cur.execute("SELECT count(*) AS n FROM symbols WHERE version_id = %s", (vid,))
            symbols = cur.fetchone()["n"]
            cur.execute("SELECT count(*) AS n FROM edges WHERE version_id = %s", (vid,))
            edges = cur.fetchone()["n"]
            cur.execute("SELECT DISTINCT module FROM symbols WHERE version_id = %s ORDER BY module", (vid,))
            modules = [row["module"] for row in cur.fetchall()]
        return {
            "backend": "postgres",
            "ready": True,
            "version": self.settings.default_version,
            "document_count": documents,
            "symbol_count": symbols,
            "edge_count": edges,
            "module_count": len(modules),
            "modules": modules,
        }

    def search_symbols(
        self,
        query: str,
        *,
        module: str = "",
        kind: str = "",
        language: str = "",
        limit: int = 20,
    ) -> dict:
        needle = query.replace("::", ".").strip()
        where = ["version_id = %s"]
        filter_params: list[object] = []
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                return {"query": query, "count": 0, "hits": []}
            filter_params.append(vid)
            if module:
                where.append("module = %s")
                filter_params.append(module)
            if kind:
                where.append("kind = %s")
                filter_params.append(kind)
            if language.casefold() in {"vba", "vb6"}:
                where.append("(module LIKE %s OR title ILIKE %s)")
                filter_params.extend(["%vb6", "%vba%"])
            elif language.casefold() in {"csharp", "c#"}:
                where.append("(module NOT LIKE %s OR title ILIKE %s OR title ILIKE %s)")
                filter_params.extend(["%vb6", "%c#%", "%csharp%"])
            params = [needle, needle, needle, needle, needle] + filter_params + [needle, needle, needle, self._limit(limit, 100)]
            cur.execute(
                f"""
                SELECT id, symbol, kind, module, interface, member, path, title, project,
                    CASE
                        WHEN lower(symbol) = lower(%s) THEN 100
                        WHEN lower(member) = lower(%s) THEN 95
                        WHEN lower(symbol) LIKE lower(%s || '.%%') THEN 85
                        WHEN symbol ILIKE '%%' || %s || '%%' THEN 65
                        WHEN title ILIKE '%%' || %s || '%%' THEN 45
                        ELSE 10
                    END AS score
                FROM symbols
                WHERE {" AND ".join(where)}
                  AND (
                    symbol ILIKE '%%' || %s || '%%'
                    OR title ILIKE '%%' || %s || '%%'
                    OR path ILIKE '%%' || %s || '%%'
                  )
                ORDER BY score DESC, lower(symbol), path
                LIMIT %s
                """,
                params,
            )
            rows = cur.fetchall()
        return {"query": query, "count": len(rows), "hits": rows}

    def lookup_symbol(self, symbol_or_id: str, *, limit: int = 10) -> dict:
        query = symbol_or_id.replace("::", ".").strip()
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                return {"query": symbol_or_id, "exact": [], "candidates": []}
            cur.execute(
                """
                SELECT id, symbol, kind, module, interface, member, path, title, project
                FROM symbols
                WHERE version_id = %s
                  AND (lower(id) = lower(%s) OR lower(symbol) = lower(%s) OR lower(path) = lower(%s))
                ORDER BY lower(symbol), path
                """,
                (vid, query, query, query),
            )
            exact = cur.fetchall()
            cur.execute(
                """
                SELECT id, symbol, kind, module, interface, member, path, title, project
                FROM symbols
                WHERE version_id = %s
                  AND (symbol ILIKE '%%' || %s || '%%' OR path ILIKE '%%' || %s || '%%')
                ORDER BY lower(symbol), path
                LIMIT %s
                """,
                (vid, query, query, self._limit(limit, 50)),
            )
            candidates = cur.fetchall()
        return {"query": symbol_or_id, "exact": exact, "candidates": candidates}

    def interface_members(self, interface: str, *, module: str = "") -> dict:
        wanted = interface.casefold().lstrip("i")
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                return {"interface": interface, "count": 0, "matches": []}
            params: list[object] = [vid, wanted]
            module_sql = ""
            if module:
                module_sql = "AND module = %s"
                params.append(module)
            cur.execute(
                f"""
                SELECT id, interface, module, path, title, members
                FROM interface_members
                WHERE version_id = %s AND trim(leading 'i' from lower(interface)) = lower(%s)
                {module_sql}
                ORDER BY module, interface
                """,
                params,
            )
            rows = cur.fetchall()
        return {"interface": interface, "count": len(rows), "matches": rows}

    def get_document(self, path_or_id: str, *, max_chars: int = 30000) -> dict:
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                raise FileNotFoundError(f"version not loaded: {self.settings.default_version}")
            cur.execute(
                """
                SELECT path, markdown
                FROM documents
                WHERE version_id = %s
                  AND (id = %s OR path = %s OR symbol = %s)
                LIMIT 1
                """,
                (vid, path_or_id, path_or_id, path_or_id),
            )
            row = cur.fetchone()
        if not row:
            raise FileNotFoundError(f"document not found: {path_or_id}")
        text = row["markdown"] or ""
        cap = max(1000, min(int(max_chars), 200000))
        return {
            "path": row["path"],
            "text": text[:cap],
            "truncated": len(text) > cap,
            "total_chars": len(text),
        }

    def neighbors(
        self,
        symbol_or_id: str,
        *,
        edge_type: str = "",
        direction: str = "both",
        limit: int = 50,
    ) -> dict:
        ids = self._ids_for(symbol_or_id)
        if not ids:
            return {"query": symbol_or_id, "ids": [], "edges": []}
        where = ["version_id = %s"]
        with self._connect() as conn, conn.cursor() as cur:
            vid = self._version_id(cur)
            if vid is None:
                return {"query": symbol_or_id, "ids": [], "edges": []}
            params: list[object] = [vid]
            if edge_type:
                where.append("type = %s")
                params.append(edge_type)
            id_list = sorted(ids)
            if direction == "out":
                where.append("source = ANY(%s)")
                params.append(id_list)
            elif direction == "in":
                where.append("target = ANY(%s)")
                params.append(id_list)
            else:
                where.append("(source = ANY(%s) OR target = ANY(%s))")
                params.extend([id_list, id_list])
            params.append(self._limit(limit, 200))
            cur.execute(
                f"""
                SELECT module, source, target, type, label
                FROM edges
                WHERE {" AND ".join(where)}
                ORDER BY type, label, source, target
                LIMIT %s
                """,
                params,
            )
            rows = cur.fetchall()
        return {"query": symbol_or_id, "ids": sorted(ids), "edges": rows}

    def find_examples(self, query: str, *, language: str = "", limit: int = 20) -> dict:
        result = self.search_symbols(query, kind="example", language=language, limit=limit)
        result["language"] = language
        return result

    def _ids_for(self, symbol_or_id: str) -> set[str]:
        found = self.lookup_symbol(symbol_or_id, limit=20)
        ids = {row["id"] for row in found["exact"]}
        if "/" in symbol_or_id and not ids:
            ids.add(symbol_or_id)
        return ids

    @staticmethod
    def _limit(value: int, cap: int) -> int:
        return max(1, min(int(value), cap))
