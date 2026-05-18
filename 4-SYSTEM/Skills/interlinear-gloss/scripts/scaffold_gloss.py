#!/usr/bin/env python3
"""Scaffold an interlinear gloss file for one (root-text, translation) pair.

Reads two markdown files that share an Obsidian block-ID scheme and writes a
gloss file under ``2-RAILS/Bilingual-Glossaries/Raw/`` with one ``gloss`` code
block per paired block. ``\\gla`` is populated from the source tokens and
``\\ex`` verbatim from the translation; ``\\glb`` is scaffolded with ``--``
placeholders at the right column count for the LLM pass to fill in.

If the output file already exists, existing ``\\glb`` lines are preserved when
their token count still matches the refreshed ``\\gla``.

Usage:

    python3 scaffold_gloss.py <root-text>.md <translation>.md <output>.md

    python3 scaffold_gloss.py --validate <gloss-file>.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$")
HEADING_RE = re.compile(r"^#{1,6}\s")
FM_FIELD_RE = lambda name: re.compile(rf"^{name}:\s*(.+?)\s*$", re.MULTILINE)

# Tokens we strip from the end of a source token before placing it on gla.
TRAILING_PUNCT = ".,;:!?"
# Tokens we strip from the beginning.
LEADING_PUNCT = "([{"


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end():]
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields, body


def parse_blocks(path):
    """Return {block_id: paragraph_text} for ``path``. Skip headings and frontmatter."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    blocks = {}
    order = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph or HEADING_RE.match(paragraph):
            continue
        match = BLOCK_ID_RE.search(paragraph)
        if not match:
            continue
        block_id = match.group(1)
        body = paragraph[: match.start()].rstrip()
        if block_id not in blocks:
            order.append(block_id)
        blocks[block_id] = body
    return blocks, order


def tokenise_source(text):
    """Split source text into gloss tokens, stripping editorial markup.

    Strips square-bracketed variant readings (``[...]``), parenthesised
    editorial content including alphabet labels like ``(Ka)`` / ``(Kha)``,
    leading verse numbers like ``4.``, and outer punctuation from each
    token. Internal hyphens (Pali compounds) are preserved.
    """
    # 1. Drop ``[...]`` variant readings and ``(...)`` editorial inserts.
    cleaned = re.sub(r"\[[^\]]*\]", "", text)
    cleaned = re.sub(r"\([^)]*\)", "", cleaned)
    # 2. Drop leading verse number like ``4.`` or ``1.``.
    cleaned = re.sub(r"^\s*\d+\.\s*", "", cleaned)
    tokens = []
    for raw in cleaned.split():
        token = raw.strip(TRAILING_PUNCT + LEADING_PUNCT + "—–\"\'")
        if not token:
            continue
        if re.fullmatch(r"\d+", token):
            continue
        tokens.append(token)
    return tokens


def normalise_free_translation(text):
    """Collapse internal whitespace and newlines; preserve sentence punctuation."""
    return re.sub(r"\s+", " ", text).strip()


def parse_existing_gloss(text):
    """Return {block_id: {'gla': str, 'glb': str, 'ex': str}}.

    Used when refreshing an existing gloss file to preserve filled glb lines.
    """
    out = {}
    # Split on '## ^<id>' headings.
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    # parts[0] is preamble; then alternating block_id / section.
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        gla = _find_gloss_line(section, "gla")
        glb = _find_gloss_line(section, "glb")
        ex = _find_gloss_line(section, "ex")
        out[block_id] = {"gla": gla, "glb": glb, "ex": ex}
    return out


def _find_gloss_line(section, marker):
    match = re.search(rf"^\\{marker}\s+(.*)$", section, flags=re.MULTILINE)
    if not match:
        # Fallback for old format without backslash
        match = re.search(rf"^{marker}\s+(.*)$", section, flags=re.MULTILINE)
    if not match:
        return ""
    return match.group(1).rstrip()


def column_align(tokens, widths):
    """Format ``tokens`` with at-least the column widths in ``widths``."""
    out = []
    for token, width in zip(tokens, widths):
        out.append(token.ljust(width))
    return " ".join(out).rstrip()


def compute_column_widths(rows):
    """Take a list of token-list rows; return max width per column."""
    widths = []
    for row in rows:
        for i, token in enumerate(row):
            if i >= len(widths):
                widths.append(len(token))
            else:
                widths[i] = max(widths[i], len(token))
    return widths


def build_gloss_block(gla_tokens, free_translation, existing):
    """Render one ```gloss``` block with column-aligned gla/glb."""
    n = len(gla_tokens)
    glb_tokens = ["--"] * n
    if existing:
        prior_gla = existing.get("gla", "").split()
        if len(prior_gla) == n:
            prior_glb = existing.get("glb", "").split()
            if len(prior_glb) == n:
                glb_tokens = prior_glb
    widths = compute_column_widths([gla_tokens, glb_tokens])
    gla_line = column_align(gla_tokens, widths)
    glb_line = column_align(glb_tokens, widths)
    lines = ["```gloss"]
    lines.append(f"\\gla    {gla_line}")
    lines.append(f"\\glb    {glb_line}")
    lines.append(f"\\ex     {free_translation}")
    lines.append("```")
    return "\n".join(lines)


def scaffold(source_path, target_path, output_path):
    source_fm, _ = parse_frontmatter(source_path.read_text(encoding="utf-8"))
    target_fm, _ = parse_frontmatter(target_path.read_text(encoding="utf-8"))
    source_blocks, order = parse_blocks(source_path)
    target_blocks, _ = parse_blocks(target_path)

    source_lang = source_fm.get("lang_tag", source_fm.get("language", "src"))
    target_lang_tag = target_fm.get("lang_tag", target_fm.get("language", "tgt"))
    target_language = target_fm.get("language", target_lang_tag)
    translator = target_fm.get("translator", "")

    existing = {}
    if output_path.exists():
        try:
            existing = parse_existing_gloss(output_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print(f"warning: could not re-parse existing {output_path}: {exc}", file=sys.stderr)

    blocks_rendered = 0
    skipped_target_missing = 0
    skipped_source_missing = 0
    reset_lines = []

    out_lines = []
    out_lines.append("---")
    out_lines.append(f"source_file: 1-SOURCES/Text/{source_path.name}")
    out_lines.append(f"source_language: {source_lang}")
    out_lines.append(f"target_file: 1-SOURCES/Translations/{target_path.name}")
    out_lines.append(f"target_language: {target_language}")
    out_lines.append(f"target_lang_tag: {target_lang_tag}")
    if translator:
        out_lines.append(f"translator: {translator}")
    out_lines.append("total_verses: __PLACEHOLDER__")
    out_lines.append(f"generated: {dt.date.today().isoformat()}")
    out_lines.append("status: draft")
    out_lines.append("---")
    out_lines.append("")
    title = f"Interlinear gloss — {source_lang} → {target_lang_tag}"
    out_lines.append(f"# {title}")
    out_lines.append("")

    for block_id in order:
        source_text = source_blocks.get(block_id, "")
        target_text = target_blocks.get(block_id, "")
        if not source_text:
            skipped_source_missing += 1
            continue
        if not target_text.strip() or target_text.strip() == "-":
            skipped_target_missing += 1
            continue
        gla_tokens = tokenise_source(source_text)
        if not gla_tokens:
            continue
        # Check whether we are resetting glb due to a token-count change.
        prior = existing.get(block_id)
        if prior:
            prior_gla = prior.get("gla", "").split()
            if prior_gla and len(prior_gla) != len(gla_tokens):
                reset_lines.append(block_id)
        free_t = normalise_free_translation(target_text)
        block = build_gloss_block(gla_tokens, free_t, prior)
        out_lines.append(f"## ^{block_id}")
        out_lines.append("")
        out_lines.append(block)
        out_lines.append("")
        blocks_rendered += 1

    # Patch the total_verses placeholder.
    rendered = "\n".join(out_lines).replace("__PLACEHOLDER__", str(blocks_rendered))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    return {
        "blocks_rendered": blocks_rendered,
        "skipped_target_missing": skipped_target_missing,
        "skipped_source_missing": skipped_source_missing,
        "reset_lines": reset_lines,
    }


def validate(gloss_path):
    text = gloss_path.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    errors = []
    checked = 0
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        gla = _find_gloss_line(section, "gla").split()
        glb = _find_gloss_line(section, "glb").split()
        if not gla:
            errors.append(f"{block_id}: missing or empty gla")
            continue
        checked += 1
        if len(glb) != len(gla):
            errors.append(f"{block_id}: glb has {len(glb)} tokens, gla has {len(gla)}")
    return checked, errors


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", metavar="FILE", help="Validate an existing gloss file")
    parser.add_argument("source", nargs="?", type=Path, help="Root-text markdown file")
    parser.add_argument("target", nargs="?", type=Path, help="Translation markdown file")
    parser.add_argument("output", nargs="?", type=Path, help="Output gloss file")
    args = parser.parse_args(argv[1:])

    if args.validate:
        checked, errors = validate(Path(args.validate))
        if errors:
            for err in errors:
                print(f"  {err}", file=sys.stderr)
            print(f"FAIL — {len(errors)} mismatches across {checked} blocks", file=sys.stderr)
            return 1
        print(f"OK — {checked} blocks all have matching token counts")
        return 0

    if not (args.source and args.target and args.output):
        parser.print_help(sys.stderr)
        return 2

    stats = scaffold(args.source, args.target, args.output)
    print(
        f"Wrote {args.output}: blocks={stats['blocks_rendered']} "
        f"skipped_target_missing={stats['skipped_target_missing']} "
        f"skipped_source