#!/usr/bin/env python3
"""Convert extracted SOLIDWORKS API HTML help into LLM-friendly Markdown."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString, Tag


SECTION_ALIASES = {
    ".net syntax": "Syntax",
    "syntax": "Syntax",
    "visual basic for applications (vba) syntax": "VBA Syntax",
    "parameters": "Parameters",
    "return value": "Return Value",
    "remarks": "Remarks",
    "example": "Examples",
    "examples": "Examples",
    "see also": "See Also",
    "availability": "Availability",
}

LANG_ALIASES = {
    "c#": "csharp",
    "visual basic": "vb",
    "visual basic (declaration)": "vb",
    "visual basic (usage)": "vb",
    "visual basic for applications (vba)": "vb",
    "vba": "vb",
    "c++/cli": "cpp",
    "vb": "vb",
}


@dataclass
class DocMeta:
    title: str
    project: str
    interface: str
    member: str
    kind: str
    source: str


def clean_text(value: str) -> str:
    value = unescape(value or "")
    value = value.replace("\ufeff", "").replace("\xa0", " ")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\n\s*", "\n", value)
    return value.strip()


def clean_code(value: str) -> str:
    value = (value or "").replace("&&nbsp;", "&nbsp;")
    value = unescape(value)
    value = value.replace("\ufeff", "").replace("\xa0", " ")
    value = re.sub(r"&(?= {2,})", "", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in value.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def code_text(node: Tag, collapse_text_newlines: bool = False) -> str:
    parts: list[str] = []

    def walk(child: Tag | NavigableString) -> None:
        if isinstance(child, NavigableString):
            text = str(child)
            if collapse_text_newlines:
                text = re.sub(r"[ \t\r\n\f\v]+", " ", text)
            parts.append(text)
            return
        if child.name == "br":
            parts.append("\n")
            return
        for grandchild in child.children:
            if isinstance(grandchild, (Tag, NavigableString)):
                walk(grandchild)

    walk(node)
    return "".join(parts)


def slug_section(text: str) -> str:
    text = clean_text(text)
    return SECTION_ALIASES.get(text.lower(), text)


def fence(code: str, lang: str = "") -> str:
    code = clean_code(code)
    ticks = "```"
    if "```" in code:
        ticks = "````"
    return f"{ticks}{lang}\n{code}\n{ticks}" if code else ""


def yaml_scalar(value: str) -> str:
    value = clean_text(value)
    if not value:
        return '""'
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_block(meta: DocMeta) -> str:
    fields = {
        "title": meta.title,
        "project": meta.project,
        "interface": meta.interface,
        "member": meta.member,
        "kind": meta.kind,
        "source": meta.source,
    }
    lines = ["---"]
    lines.extend(f"{key}: {yaml_scalar(value)}" for key, value in fields.items())
    lines.append("---")
    return "\n".join(lines)


def extract_meta(soup: BeautifulSoup, source: Path) -> DocMeta:
    page_title = soup.select_one("#pagetitle")
    html_title = soup.find("title")
    title = clean_text(page_title.get_text(" ", strip=True) if page_title else "")
    if not title and html_title:
        title = clean_text(html_title.get_text(" ", strip=True))
    if not title:
        title = source.stem

    project_node = soup.select_one("#projecttitle")
    project = clean_text(project_node.get_text(" ", strip=True) if project_node else "")

    kind = ""
    interface = ""
    member = ""

    typed_match = re.match(r"^(?P<member>.+?)\s+(?P<kind>Method|Property|Event)\s+\((?P<iface>.+?)\)$", title, re.I)
    if typed_match:
        member = clean_text(typed_match.group("member"))
        interface = clean_text(typed_match.group("iface"))
        kind = typed_match.group("kind").lower()
    else:
        for label, normalized in (
            ("Interface", "interface"),
            ("Class", "class"),
            ("Enumeration", "enum"),
            ("Delegate", "delegate"),
            ("Namespace", "namespace"),
            ("Object", "object"),
        ):
            suffix = f" {label}"
            if title.lower().endswith(suffix.lower()):
                kind = normalized
                interface = title[: -len(suffix)].strip()
                break

    if not kind:
        stem = source.stem
        if stem.endswith("_members"):
            kind = "members"
        elif stem.endswith("_methods"):
            kind = "methods"
        elif stem.endswith("_properties"):
            kind = "properties"
        elif "_Example_" in stem or "Example" in title:
            kind = "example"
        else:
            kind = "topic"

    if not interface or not member:
        parts = source.stem.split("~")
        if len(parts) >= 3:
            interface = interface or parts[-2].split(".")[-1]
            member = member or parts[-1]
        elif len(parts) == 2:
            interface = interface or parts[-1].split(".")[-1]

    return DocMeta(title=title, project=project, interface=interface, member=member, kind=kind, source=source.as_posix())


def remove_noise(soup: BeautifulSoup) -> None:
    selectors = [
        "script",
        "style",
        "xml",
        "form",
        "input",
        "map",
        "area",
        "object",
        "embed",
        "#pagetop",
        "#pagefooter",
        ".dxpopupbubble",
        ".saveHistory",
        ".copyCode",
        ".toggle",
        ".toggleAll",
        ".userDataStyle",
    ]
    for node in soup.select(",".join(selectors)):
        node.decompose()
    for img in soup.find_all("img"):
        alt = clean_text(img.get("alt", ""))
        img.replace_with(f" {alt} " if alt else "")


def language_from_heading(text: str) -> str:
    normalized = clean_text(text).lower()
    return LANG_ALIASES.get(normalized, "")


def render_syntax_table(table: Tag) -> str:
    blocks: list[str] = []
    for pre in table.find_all("pre"):
        header = ""
        row = pre.find_parent("tr")
        if row:
            previous = row.find_previous_sibling("tr")
            if previous:
                header = clean_text(previous.get_text(" ", strip=True))
        if not header:
            first_th = table.find("th")
            header = clean_text(first_th.get_text(" ", strip=True) if first_th else "")
        lang = language_from_heading(header)
        label = header if header else "Syntax"
        code = fence(code_text(pre), lang)
        if code:
            blocks.append(f"### {label}\n\n{code}")
    return "\n\n".join(blocks)


def render_table(table: Tag) -> str:
    if "syntaxtable" in table.get("class", []):
        return render_syntax_table(table)

    rows: list[list[str]] = []
    for tr in table.find_all("tr", recursive=True):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        rows.append([clean_text(cell.get_text(" ", strip=True)).replace("|", "\\|") for cell in cells])

    if not rows:
        return ""

    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    body = rows[1:]
    separator = ["---"] * width
    rendered = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    rendered.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(rendered)


def render_definition_list(dl: Tag) -> str:
    lines: list[str] = []
    current = ""
    for child in dl.children:
        if not isinstance(child, Tag):
            continue
        if child.name == "dt":
            current = clean_text(child.get_text(" ", strip=True))
        elif child.name == "dd":
            body = render_children(child).strip() or clean_text(child.get_text(" ", strip=True))
            if current:
                lines.append(f"- `{current}`: {body}")
            elif body:
                lines.append(f"- {body}")
    return "\n".join(lines)


def render_list(node: Tag, ordered: bool) -> str:
    lines: list[str] = []
    for index, li in enumerate(node.find_all("li", recursive=False), start=1):
        marker = f"{index}." if ordered else "-"
        body = render_children(li).strip().replace("\n", "\n  ")
        if body:
            lines.append(f"{marker} {body}")
    return "\n".join(lines)


def inline_text(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        return clean_text(str(node))
    if node.name == "br":
        return "\n"
    if node.name == "a":
        text = clean_text(node.get_text(" ", strip=True))
        href = clean_text(node.get("href", ""))
        if href and not href.startswith(("javascript:", "mailto:")):
            return f"[{text}]({href})" if text else href
        return text
    if node.name in {"b", "strong"}:
        text = clean_text(node.get_text(" ", strip=True))
        return f"**{text}**" if text else ""
    if node.name in {"i", "em"}:
        text = clean_text(node.get_text(" ", strip=True))
        return f"`{text}`" if text else ""
    return clean_text(node.get_text(" ", strip=True))


def render_paragraph(p: Tag) -> str:
    pieces = [inline_text(child) for child in p.children]
    text = "".join(pieces)
    text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def is_apicode(node: object) -> bool:
    return isinstance(node, Tag) and node.name == "p" and "APICODE" in node.get("class", [])


def render_apicode_block(nodes: list[Tag]) -> str:
    code_parts: list[str] = []
    for node in nodes:
        text = code_text(node, collapse_text_newlines=True)
        text = re.sub(r"\n{2,}", "\n", text)
        code_parts.append(text)
    return fence("\n".join(code_parts), "vb")


def render_heading(node: Tag) -> str:
    level = int(node.name[1]) if node.name and re.match(r"h[1-6]", node.name) else 2
    text = slug_section(node.get_text(" ", strip=True))
    if not text:
        return ""
    if "heading" in node.get("class", []):
        level = 2
    elif "dxh4" in node.get("class", []):
        level = 3
    else:
        level = min(level + 1, 6)
    return f"{'#' * level} {text}"


def render_node(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        text = clean_text(str(node))
        return text if text else ""
    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return render_heading(node)
    if node.name == "table":
        return render_table(node)
    if node.name == "pre":
        return fence(code_text(node))
    if node.name == "dl":
        return render_definition_list(node)
    if node.name in {"ul", "ol"}:
        return render_list(node, node.name == "ol")
    if node.name == "p":
        return render_paragraph(node)
    if node.name == "br":
        return "\n"
    if node.name in {"div", "section", "tbody", "tr", "td", "span"}:
        return render_children(node)
    if node.name == "a":
        return inline_text(node)
    return render_children(node)


def render_children(parent: Tag) -> str:
    chunks: list[str] = []
    children = list(parent.children)
    index = 0
    while index < len(children):
        child = children[index]
        if is_apicode(child):
            group: list[Tag] = []
            while index < len(children) and (is_apicode(children[index]) or clean_text(str(children[index])) == ""):
                if is_apicode(children[index]):
                    group.append(children[index])  # type: ignore[arg-type]
                index += 1
            if group:
                chunks.append(render_apicode_block(group))
            continue

        rendered = render_node(child).strip() if isinstance(child, (Tag, NavigableString)) else ""
        if rendered:
            chunks.append(rendered)
        index += 1
    return "\n\n".join(chunks)


def normalize_markdown(markdown: str) -> str:
    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def remove_duplicate_body_headings(body: Tag, title: str) -> None:
    direct_headings = [child for child in body.children if isinstance(child, Tag) and child.name == "h1"]
    for index, heading in enumerate(direct_headings[:3]):
        text = clean_text(heading.get_text(" ", strip=True))
        compact_text = re.sub(r"\s+", " ", text)
        if compact_text == title or (index == 0 and compact_text.lower().endswith(" help")):
            heading.decompose()


def convert_file(source: Path, input_root: Path) -> str:
    raw = source.read_bytes()
    soup = BeautifulSoup(raw, "lxml")
    meta = extract_meta(soup, source.relative_to(input_root))
    remove_noise(soup)

    body = soup.select_one("#mainbody") or soup.body or soup
    remove_duplicate_body_headings(body, meta.title)
    body_md = render_children(body)
    title_md = f"# {meta.title}"
    if body_md.lstrip().startswith("# "):
        content = body_md
    else:
        content = f"{title_md}\n\n{body_md}" if body_md else title_md
    return normalize_markdown(f"{yaml_block(meta)}\n\n{content}")


def html_files(root: Path, output_root: Path) -> Iterable[Path]:
    suffixes = {".htm", ".html"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        try:
            path.relative_to(output_root)
            continue
        except ValueError:
            yield path


def output_path_for(source: Path, input_root: Path, output_root: Path) -> Path:
    relative = source.relative_to(input_root)
    return output_root / relative.with_suffix(".md")


def default_input_dir() -> Path:
    api_html = Path("API_HTML")
    return api_html if api_html.is_dir() else Path(".")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        default=default_input_dir(),
        type=Path,
        help="Directory with extracted HTML files. Defaults to API_HTML if it exists, otherwise current directory.",
    )
    parser.add_argument("-o", "--output", default="markdown", type=Path, help="Directory for generated Markdown.")
    parser.add_argument("--limit", type=int, default=0, help="Convert only the first N files, useful for smoke tests.")
    args = parser.parse_args()

    input_root = args.input.resolve()
    output_root = args.output.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    converted = 0
    failed: list[tuple[Path, str]] = []
    for source in html_files(input_root, output_root):
        if args.limit and converted >= args.limit:
            break
        target = output_path_for(source, input_root, output_root)
        try:
            markdown = convert_file(source, input_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
            converted += 1
        except Exception as exc:  # Keep batch conversion useful even with one malformed topic.
            failed.append((source.relative_to(input_root), str(exc)))

    print(f"converted: {converted}")
    if failed:
        print(f"failed: {len(failed)}")
        for path, error in failed[:20]:
            print(f"- {path}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
