#!/usr/bin/env python3
"""Combine raw per-source glossaries into one consolidated language-pair file.

Reads every file under ``raw_dir`` whose frontmatter declares the requested
``language_pair`` and emits a consolidated glossary at ``output_path`` with
one ``##`` heading per source-language keyword and a rendering table that
sums frequencies across sources.

Usage:

    python3 combine_glossaries.py <language-pair> <raw-dir> <output-path> [--check]

The ``--check`` flag dry-runs the merge and prints counts without writing.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LANG_PAIR_RE = re.compile(r"^language_pair:\s*([^\s#]+)", re.MULTILINE)
TABLE_HEADER_RE = re.compile(
    r"^\|\s*Rendering\s*\|\s*Frequency\s*\|.*?\|\s*$",
    re.MULTILINE | re.IGNORECASE,
)
TABLE_DIVIDER_RE = re.compile(r"^\|[\s\-:|]+\|\s*$", re.MULTILINE)


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def _extract_table_rows(section):
    header = TABLE_HEADER_RE.search(section)
    if not header:
        return []
    after_header = section[header.end():]
    divider = TABLE_DIVIDER_RE.search(after_header)
    if not divider:
        return []
    table_body = after_header[divider.end():]
    rows = []
    seen_row = False
    for line in table_body.splitlines():
        stripped = line.strip()
        if not stripped:
            if seen_row:
                break
            continue
        if not stripped.startswith("|"):
            break
        seen_row = True
        match = re.match(r"\|([^|]+)\|([^|]+)\|([^|]*)\|([^|]*)\|\s*$", line)
        if not match:
            continue
        rendering = match.group(1).strip()
        freq_text = match.group(2).strip()
        try:
            freq = int(freq_text)
        except ValueError:
            continue
        rows.append((rendering, freq))
    return rows


def parse_raw_glossary(path):
    text = path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(text)
    source_label = path.stem
    keywords = {}
    parts = re.split(r"^##\s+(?!#)(.+?)\s*$", body, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        keyword = parts[i].strip()
        section = parts[i + 1] if i + 1 < len(parts) else ""
        renderings = _extract_table_rows(section)
        if renderings:
            keywords[keyword] = renderings
    return source_label, keywords


def normalise_rendering(rendering):
    return rendering.strip().lower()


def combine(language_pair, raw_dir):
    consolidated = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    display_form = {}
    raw_files = []
    for path in sorted(raw_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        lp_match = LANG_PAIR_RE.search(fm)
        if not lp_match or lp_match.group(1).strip() != language_pair:
            continue
        raw_files.append(f"2-RAILS/Glossaries/Raw/{path.name}")
        source_label, keywords = parse_raw_glossary(path)
        for keyword, renderings in keywords.items():
            for rendering, freq in renderings:
                key = normalise_rendering(rendering)
                consolidated[keyword][key][source_label] += freq
                display_form.setdefault((keyword, key), rendering)
    return consolidated, raw_files, display_form


def local_wiki_link(keyword, vault_root):
    base = re.sub(r"\s*\(.+\)\s*$", "", keyword).strip()
    candidate = vault_root / "2-RAILS" / "Local-Wiki" / f"{base}.md"
    if candidate.exists():
        return f"[[{base}]]"
    return "—"


def _sort_key_keyword(keyword):
    match = re.match(r"^(.*?)\s*\((.+)\)\s*$", keyword)
    if match:
        return (match.group(1).strip().lower(), match.group(2).strip().lower())
    return (keyword.strip().lower(), "")


def write_consolidated(output_path, language_pair, raw_files, consolidated, display_form, vault_root):
    source_lang, target_lang = language_pair.split("-", 1)
    keyword_count = len(consolidated)
    rendering_count = sum(len(rs) for rs in consolidated.values())
    lines = []
    lines.append("---")
    lines.append(f"language_pair: {language_pair}")
    lines.append(f"source_language: {source_lang}")
    lines.append(f"target_language: {target_lang}")
    lines.append("raw_sources:")
    for raw in raw_files:
        lines.append(f"  - {raw}")
    lines.append(f"total_keywords: {keyword_count}")
    lines.append(f"total_distinct_renderings: {rendering_count}")
    lines.append(f"generated: {dt.date.today().isoformat()}")
    lines.append("status: draft")
    lines.append("---")
    lines.append("")
    lines.append(f"# Consolidated glossary — {source_lang} → {target_lang}")
    lines.append("")
    for keyword in sorted(consolidated, key=_sort_key_keyword):
        lines.append(f"## {keyword}")
        lines.append("")
        lines.append("| Rendering | Sources | Total frequency | Local-Wiki |")
        lines.append("|-----------|---------|-----------------|------------|")
        rendering_items = list(consolidated[keyword].items())
        rendering_items.sort(key=lambda item: (-sum(item[1].values()), item[0]))
        wiki_cell = local_wiki_link(keyword, vault_root)
        for norm, per_source in rendering_items:
            display = display_form[(keyword, norm)]
            sources_text = ", ".join(f"{src} ({freq})" for src, freq in sorted(per_source.items()))
            total = sum(per_source.values())
            lines.append(f"| {display} | {sources_text} | {total} | {wiki_cell} |")
        lines.append("")
        lines.append("---")
        lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return keyword_count, rendering_count


def find_vault_root(start):
    current = start.resolve()
    for _ in range(8):
        if (current / "2-RAILS").is_dir() and (current / "1-SOURCES").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent
    return start.resolve()


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("language_pair")
    parser.add_argument("raw_dir", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv[1:])

    consolidated, raw_files, display_form = combine(args.language_pair, args.raw_dir)
    if not consolidated:
        print(f"No raw glossaries with language_pair={args.language_pair} found in {args.raw_dir}", file=sys.stderr)
        return 1

    if args.check:
        kw = len(consolidated)
        rd = sum(len(rs) for rs in consolidated.values())
        print(f"language_pair={args.language_pair} keywords={kw} distinct_renderings={rd} raw_files={len(raw_files)}")
        return 0

    vault_root = find_vault_root(args.raw_dir)
    kw, rd = write_consolidated(args.output_path, args.language_pair, raw_files, consolidated, display_form, vault_root)
    print(f"Wrote {args.output_path}: keywords={kw} distinct_renderings={rd} raw_files={len(raw_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
