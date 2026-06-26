"""Load generated llm_index and Markdown files into PostgreSQL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


def iter_jsonl(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def batched(rows: Iterable[tuple], size: int = 1000) -> Iterable[list[tuple]]:
    batch: list[tuple] = []
    for row in rows:
        batch.append(row)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch


def read_markdown(markdown_root: Path, relative_path: str) -> str:
    path = (markdown_root / relative_path).resolve()
    root = markdown_root.resolve()
    if path != root and root not in path.parents:
        raise ValueError(f"path escapes markdown root: {relative_path}")
    return path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""


def load_schema(conn) -> None:
    schema_path = Path(__file__).resolve().parents[1] / "swapi_mcp" / "schema.sql"
    with conn.cursor() as cur:
        cur.execute(schema_path.read_text(encoding="utf-8"))
    conn.commit()


def version_id(conn, version: str, markdown_root: Path, index_root: Path) -> int:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO api_versions (version, markdown_root, index_root)
            VALUES (%s, %s, %s)
            ON CONFLICT (version) DO UPDATE
            SET markdown_root = EXCLUDED.markdown_root,
                index_root = EXCLUDED.index_root
            RETURNING id
            """,
            (version, str(markdown_root), str(index_root)),
        )
        return int(cur.fetchone()[0])


def clear_version(conn, vid: int) -> None:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM edges WHERE version_id = %s", (vid,))
        cur.execute("DELETE FROM interface_members WHERE version_id = %s", (vid,))
        cur.execute("DELETE FROM symbols WHERE version_id = %s", (vid,))
        cur.execute("DELETE FROM documents WHERE version_id = %s", (vid,))
    conn.commit()


def execute_batches(conn, sql: str, rows: Iterable[tuple], batch_size: int, label: str) -> int:
    total = 0
    with conn.cursor() as cur:
        for batch in batched(rows, batch_size):
            cur.executemany(sql, batch)
            total += len(batch)
            conn.commit()
            print(f"{label}: loaded {total}")
    return total


def load_documents(conn, vid: int, index_root: Path, markdown_root: Path, batch_size: int) -> int:
    def rows():
        for item in iter_jsonl(index_root / "documents.jsonl"):
            yield (
                vid,
                item.get("id", ""),
                item.get("path", ""),
                item.get("module", ""),
                item.get("kind", ""),
                item.get("title", ""),
                item.get("symbol", ""),
                item.get("interface", ""),
                item.get("member", ""),
                item.get("project", ""),
                json.dumps(item.get("headings", []), ensure_ascii=False),
                json.dumps(item.get("signatures", {}), ensure_ascii=False),
                item.get("token_estimate"),
                item.get("words"),
                item.get("link_count"),
                read_markdown(markdown_root, str(item.get("path", ""))),
            )

    sql = """
        INSERT INTO documents (
            version_id, id, path, module, kind, title, symbol, interface, member,
            project, headings, signatures, token_estimate, words, link_count, markdown
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s, %s, %s, %s
        )
    """
    return execute_batches(conn, sql, rows(), batch_size, "documents")


def load_symbols(conn, vid: int, index_root: Path, batch_size: int) -> int:
    def rows():
        for item in iter_jsonl(index_root / "symbols.jsonl"):
            yield (
                vid,
                item.get("id", ""),
                item.get("symbol", ""),
                item.get("kind", ""),
                item.get("module", ""),
                item.get("path", ""),
                item.get("title", ""),
                item.get("interface", ""),
                item.get("member", ""),
                item.get("project", ""),
            )

    sql = """
        INSERT INTO symbols (
            version_id, id, symbol, kind, module, path, title, interface, member, project
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    return execute_batches(conn, sql, rows(), batch_size, "symbols")


def load_interface_members(conn, vid: int, index_root: Path, batch_size: int) -> int:
    def rows():
        for item in iter_jsonl(index_root / "interface_members.jsonl"):
            yield (
                vid,
                item.get("id", ""),
                item.get("interface", ""),
                item.get("module", ""),
                item.get("path", ""),
                item.get("title", ""),
                json.dumps(item.get("members", []), ensure_ascii=False),
            )

    sql = """
        INSERT INTO interface_members (
            version_id, id, interface, module, path, title, members
        ) VALUES (%s, %s, %s, %s, %s, %s, %s::jsonb)
    """
    return execute_batches(conn, sql, rows(), batch_size, "interface_members")


def load_edges(conn, vid: int, index_root: Path, batch_size: int) -> int:
    def rows():
        for shard in sorted((index_root / "edges").glob("*.jsonl")):
            module = shard.stem
            for item in iter_jsonl(shard):
                yield (
                    vid,
                    module,
                    item.get("source", ""),
                    item.get("target", ""),
                    item.get("type", ""),
                    item.get("label", ""),
                )

    sql = """
        INSERT INTO edges (version_id, module, source, target, type, label)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    return execute_batches(conn, sql, rows(), batch_size, "edges")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database-url", required=True, help="PostgreSQL connection URL.")
    parser.add_argument("--version", default="2024", help="SOLIDWORKS API version label.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root containing markdown/ and llm_index/.")
    parser.add_argument("--index", type=Path, default=None, help="Override llm_index directory.")
    parser.add_argument("--markdown", type=Path, default=None, help="Override markdown directory.")
    parser.add_argument("--batch-size", type=int, default=1000)
    parser.add_argument("--schema-only", action="store_true", help="Only create/update schema.")
    parser.add_argument("--append", action="store_true", help="Do not clear existing rows for this version first.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        import psycopg
    except ImportError as exc:
        raise SystemExit("Install PostgreSQL support with: python -m pip install 'psycopg[binary]>=3.1'") from exc

    root = args.root.resolve()
    index_root = (args.index or root / "llm_index").resolve()
    markdown_root = (args.markdown or root / "markdown").resolve()

    with psycopg.connect(args.database_url) as conn:
        load_schema(conn)
        if args.schema_only:
            print("schema ready")
            return
        vid = version_id(conn, args.version, markdown_root, index_root)
        if not args.append:
            clear_version(conn, vid)
        print(f"loading version {args.version} from {index_root}")
        counts = {
            "documents": load_documents(conn, vid, index_root, markdown_root, args.batch_size),
            "symbols": load_symbols(conn, vid, index_root, args.batch_size),
            "interface_members": load_interface_members(conn, vid, index_root, args.batch_size),
            "edges": load_edges(conn, vid, index_root, args.batch_size),
        }
        print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
