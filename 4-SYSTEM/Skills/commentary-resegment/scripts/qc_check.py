#!/usr/bin/env python3
"""
qc_check.py — deterministic QC for line-wise resegmented commentaries.

Runs after resegment_linewise.py. Scans every block of a `.reseg.md` for known
boundary-quality problems and writes a report. This checker is DETERMINISTIC and
makes no API calls and no edits — it only flags blocks for human attention. (Unlike
the windowed block-resegmentation skill, mid-line splitting is out of scope here,
so QC reports rather than repairs.)

Usage:
    python3 4-SYSTEM/Skills/block-resegmentation-linewise/scripts/qc_check.py \\
        "0-INBOX/resegmented/<id>.reseg.md"

    # tune the over-length threshold (syllables):
    python3 ... "<id>.reseg.md" --over-length 60

Checks:
    CONNECTOR_ENDING      block ends in a connector particle
                          (དང་། ཞིང་། ཅིང་། ཤིང་། ནས། ལས། སྟེ། ཏེ། དེ། པས། ལ།) —
                          sentence likely continues; block may need merging forward.
    OBJECTION_REPLY_FUSED block contains both an objection (ཅེ་ན།/ཞེ་ན།/སྙམ་ན།) and a
                          reply (འོ་ན།) — two thoughts in one block.
    OVER_LENGTH           block exceeds --over-length syllables — may hide a boundary.
    SHORT_FRAGMENT        block under 4 syllables — possible stray fragment.

Output:
    0-INBOX/resegmented/<id>.qc.md   QC report (flags + block previews)
    Exit code 0 always (report-only).
"""

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r'^---[ \t]*\r?\n.*?\r?\n---[ \t]*\r?\n', re.DOTALL)

# connector particles that signal an incomplete sentence at a block's end
CONNECTOR_END_RE = re.compile(r'(?:དང|ཞིང|ཅིང|ཤིང|ནས|ལས|སྟེ|ཏེ|དེ|པས|ཅེས|ལ)[་\s]*།[\s།]*$')

OBJECTION_RE = re.compile(r'(?:ཅེ་ན|ཞེ་ན|སྙམ་ན)།')
REPLY_RE     = re.compile(r'འོ་ན།')

SHORT_SYLLABLES = 4


def is_heading(block: str) -> bool:
    return block.lstrip().startswith('#')


def syllable_count(text: str) -> int:
    """Approximate Tibetan syllable count via tsheg (་) and shad (།) delimiters."""
    cleaned = re.sub(r'[།\s]+', '་', text)
    parts = [p for p in cleaned.split('་') if p.strip()]
    return len(parts)


def parse_blocks(path: Path):
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    m = FRONTMATTER_RE.match(text)
    body = text[m.end():] if m else text
    raw = re.split(r'\n{2,}', body)
    return [b.strip() for b in raw if b.strip()]


def last_line(block: str) -> str:
    lines = [l for l in block.split('\n') if l.strip()]
    return lines[-1] if lines else block


def check_block(block: str, over_length: int):
    flags = []
    if is_heading(block):
        return flags
    if CONNECTOR_END_RE.search(last_line(block)):
        flags.append("CONNECTOR_ENDING")
    if OBJECTION_RE.search(block) and REPLY_RE.search(block):
        flags.append("OBJECTION_REPLY_FUSED")
    syl = syllable_count(block)
    if syl > over_length:
        flags.append(f"OVER_LENGTH({syl})")
    if syl < SHORT_SYLLABLES:
        flags.append(f"SHORT_FRAGMENT({syl})")
    return flags


def main():
    ap = argparse.ArgumentParser(description="Deterministic QC for line-wise resegmentation.")
    ap.add_argument("reseg_file", help="The <id>.reseg.md to check")
    ap.add_argument("--over-length", type=int, default=60,
                    help="Syllable threshold for OVER_LENGTH (default: 60)")
    args = ap.parse_args()

    path = Path(args.reseg_file)
    if not path.exists():
        sys.exit(f"Error: file not found: {path}")

    blocks = parse_blocks(path)
    content_blocks = [b for b in blocks if not is_heading(b)]

    findings = []
    for i, b in enumerate(blocks):
        fl = check_block(b, args.over_length)
        if fl:
            findings.append((i, fl, b))

    tally: dict = {}
    for _, fl, _ in findings:
        for f in fl:
            key = f.split('(')[0]
            tally[key] = tally.get(key, 0) + 1

    def preview(t, n=90):
        t = t.replace('\n', ' ')
        return t[:n] + ('…' if len(t) > n else '')

    out = [
        f"# QC Report — {path.stem}",
        "",
        f"Total blocks   : {len(blocks)}",
        f"Content blocks : {len(content_blocks)}",
        f"Flagged blocks : {len(findings)}",
        "",
        "## flags_before",
        "",
    ]
    if tally:
        for k in sorted(tally):
            out.append(f"- {k}: {tally[k]}")
    else:
        out.append("- (none)")
    out.append("")

    if findings:
        out += ["## Flagged blocks", ""]
        for idx, fl, b in findings:
            out.append(f"**Block {idx}** — {', '.join(fl)}")
            out.append(f"  {preview(b)}")
            out.append("")

    qc_path = path.parent / (path.stem.replace(".reseg", "") + ".qc.md")
    qc_path.write_text("\n".join(out), encoding="utf-8")

    print(f"Blocks checked : {len(blocks)}")
    print(f"Flagged        : {len(findings)}")
    for k in sorted(tally):
        print(f"  {k}: {tally[k]}")
    print(f"\nReport: {qc_path}")


if __name__ == "__main__":
    main()
