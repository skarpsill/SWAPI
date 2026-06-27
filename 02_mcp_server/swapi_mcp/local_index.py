"""Read-only navigation over the generated llm_index and Markdown corpus."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .config import Settings, load_settings


@dataclass(frozen=True)
class SearchFilters:
    module: str = ""
    kind: str = ""
    language: str = ""


class LocalIndex:
    """Small, dependency-free reader for the generated JSONL/Markdown index."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or load_settings()
        self.index_dir = self.settings.index_dir
        self.markdown_dir = self.settings.markdown_dir

    def status(self) -> dict:
        manifest = self._read_json(self.index_dir / "manifest.json", default={})
        return {
            "backend": "local",
            "ready": self.index_dir.is_dir() and self.markdown_dir.is_dir(),
            "version": self.settings.default_version,
            "index_dir": str(self.index_dir),
            "markdown_dir": str(self.markdown_dir),
            "document_count": manifest.get("document_count"),
            "symbol_count": self._line_count(self.index_dir / "symbols.jsonl"),
            "edge_count": manifest.get("edge_count"),
            "module_count": manifest.get("module_count"),
            "modules": manifest.get("modules", []),
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
        terms = [part for part in query.casefold().replace("::", ".").split() if part]
        needle = query.casefold().replace("::", ".").strip()
        rows = []
        for row in self._iter_jsonl(self.index_dir / "symbols.jsonl"):
            if not self._matches_filters(row, SearchFilters(module, kind, language)):
                continue
            score = self._symbol_score(row, needle, terms)
            if score:
                item = self._symbol_card(row)
                item["score"] = score
                rows.append(item)
        rows.sort(key=lambda item: (-item["score"], item["symbol"].casefold(), item["path"]))
        return {"query": query, "count": len(rows), "hits": rows[: self._limit(limit, 100)]}

    def lookup_symbol(self, symbol_or_id: str, *, limit: int = 10) -> dict:
        query = symbol_or_id.casefold().replace("::", ".").strip()
        exact = []
        fuzzy = []
        for row in self._iter_jsonl(self.index_dir / "symbols.jsonl"):
            values = {
                str(row.get("id", "")).casefold(),
                str(row.get("symbol", "")).casefold().replace("::", "."),
                str(row.get("path", "")).casefold(),
            }
            card = self._symbol_card(row)
            if query in values:
                exact.append(card)
            elif query and any(query in value for value in values):
                fuzzy.append(card)
        fuzzy.sort(key=lambda item: (item["symbol"].casefold(), item["path"]))
        return {"query": symbol_or_id, "exact": exact, "candidates": fuzzy[: self._limit(limit, 50)]}

    def interface_members(self, interface: str, *, module: str = "") -> dict:
        wanted = interface.casefold().lstrip("i")
        matches = []
        for row in self._iter_jsonl(self.index_dir / "interface_members.jsonl"):
            name = str(row.get("interface", ""))
            if name.casefold().lstrip("i") != wanted:
                continue
            if module and str(row.get("module", "")).casefold() != module.casefold():
                continue
            matches.append(row)
        return {"interface": interface, "count": len(matches), "matches": matches}

    def get_document(self, path_or_id: str, *, max_chars: int = 30000) -> dict:
        rel = self._resolve_document_path(path_or_id)
        full = (self.markdown_dir / rel).resolve()
        root = self.markdown_dir.resolve()
        if full != root and root not in full.parents:
            raise ValueError("document path escapes markdown root")
        if not full.is_file():
            raise FileNotFoundError(f"document not found: {path_or_id}")
        text = full.read_text(encoding="utf-8", errors="replace")
        cap = max(1000, min(int(max_chars), 200000))
        return {
            "path": rel,
            "absolute_path": str(full),
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
        module_names = sorted({item.split("/", 1)[0] for item in ids if "/" in item})
        edges = []
        for module in module_names:
            for edge in self._iter_jsonl(self.index_dir / "edges" / f"{module}.jsonl"):
                if edge_type and str(edge.get("type", "")).casefold() != edge_type.casefold():
                    continue
                source_hit = edge.get("source") in ids
                target_hit = edge.get("target") in ids
                if direction == "out" and not source_hit:
                    continue
                if direction == "in" and not target_hit:
                    continue
                if direction == "both" and not (source_hit or target_hit):
                    continue
                edges.append(edge)
                if len(edges) >= self._limit(limit, 200):
                    break
        return {"query": symbol_or_id, "ids": sorted(ids), "edges": edges}

    def find_examples(self, query: str, *, language: str = "", limit: int = 20) -> dict:
        result = self.search_symbols(query, kind="example", language=language, limit=limit)
        result["language"] = language
        return result

    def _resolve_document_path(self, path_or_id: str) -> str:
        candidate = path_or_id.strip().lstrip("/")
        if candidate.endswith(".md"):
            return candidate
        for row in self._iter_jsonl(self.index_dir / "documents.jsonl"):
            if candidate in {str(row.get("id", "")), str(row.get("path", "")), str(row.get("symbol", ""))}:
                return str(row.get("path", ""))
        lookup = self.lookup_symbol(candidate, limit=1)
        if lookup["exact"]:
            return lookup["exact"][0]["path"]
        raise FileNotFoundError(f"cannot resolve document: {path_or_id}")

    def _ids_for(self, symbol_or_id: str) -> set[str]:
        query = symbol_or_id.casefold().replace("::", ".").strip()
        ids = set()
        for row in self._iter_jsonl(self.index_dir / "symbols.jsonl"):
            row_id = str(row.get("id", ""))
            symbol = str(row.get("symbol", "")).casefold().replace("::", ".")
            path = str(row.get("path", "")).casefold()
            if query in {row_id.casefold(), symbol, path}:
                ids.add(row_id)
        if "/" in symbol_or_id and not ids:
            ids.add(symbol_or_id.strip())
        return ids

    @staticmethod
    def _symbol_card(row: dict) -> dict:
        return {
            "id": row.get("id", ""),
            "symbol": row.get("symbol", ""),
            "kind": row.get("kind", ""),
            "module": row.get("module", ""),
            "interface": row.get("interface", ""),
            "member": row.get("member", ""),
            "path": row.get("path", ""),
            "title": row.get("title", ""),
            "project": row.get("project", ""),
        }

    @staticmethod
    def _symbol_score(row: dict, needle: str, terms: list[str]) -> int:
        symbol = str(row.get("symbol", "")).casefold().replace("::", ".")
        title = str(row.get("title", "")).casefold()
        path = str(row.get("path", "")).casefold()
        interface = str(row.get("interface", "")).casefold()
        member = str(row.get("member", "")).casefold()
        haystacks = [symbol, title, path, interface, member]
        if needle:
            if symbol == needle or member == needle:
                return 100
            if symbol.endswith("." + needle):
                return 90
            if symbol.startswith(needle):
                return 80
            if needle in symbol:
                return 65
            if needle in title:
                return 45
            if needle in path:
                return 30
        if terms and all(any(term in value for value in haystacks) for term in terms):
            return 20 + sum(1 for term in terms for value in haystacks if term in value)
        return 0

    @staticmethod
    def _matches_filters(row: dict, filters: SearchFilters) -> bool:
        if filters.module and str(row.get("module", "")).casefold() != filters.module.casefold():
            return False
        if filters.kind and str(row.get("kind", "")).casefold() != filters.kind.casefold():
            return False
        if filters.language:
            module = str(row.get("module", "")).casefold()
            title = str(row.get("title", "")).casefold()
            lang = filters.language.casefold()
            if lang in {"vba", "vb6"}:
                return module.endswith("vb6") or "vba" in title
            if lang in {"csharp", "c#"}:
                return not module.endswith("vb6") or "c#" in title or "csharp" in title
        return True

    @staticmethod
    def _iter_jsonl(path: Path) -> Iterable[dict]:
        if not path.is_file():
            return
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue

    @staticmethod
    def _read_json(path: Path, default):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return default

    @staticmethod
    def _line_count(path: Path) -> int | None:
        if not path.is_file():
            return None
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return sum(1 for _ in handle)

    @staticmethod
    def _limit(value: int, cap: int) -> int:
        return max(1, min(int(value), cap))
