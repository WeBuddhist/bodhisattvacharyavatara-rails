#!/usr/bin/env python3
"""Check every uploaded edition's source markdown still reproduces its live content.

A regenerated TOC is only valid if the spans it computes refer to the content
the backend actually holds. So before any TOC is deleted and re-uploaded, run
each source through the parser and compare the resulting `content` against the
live edition, byte for byte.

A mismatch means the markdown has drifted since upload. The TOC generated from
it would carry spans measured against a *different* string — silently pointing
at the wrong text. Those editions must be reconciled (re-upload the content, or
recover the source that was uploaded) before their TOC is touched.

Usage (from the vault root, with a post-sweep snapshot on disk):
    TSR_SNAPSHOTS=/path/to/snapshots \\
      python3 4-SYSTEM/scripts/title-segment-removal/preflight_toc.py --snapshot sweep-after
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
SNAPDIR = Path(os.environ.get("TSR_SNAPSHOTS", Path(__file__).parent / "snapshots"))

ROOT_PARSER = VAULT / "4-SYSTEM/scripts/parser-root-text/parser.py"
COMM_PARSER = VAULT / "4-SYSTEM/scripts/parser-commentary/parser_commentary.py"
ROOT_LINT = VAULT / "4-SYSTEM/scripts/linter-root-text/output"
COMM_LINT = VAULT / "4-SYSTEM/scripts/linter-commentary/output"

# edition_id -> (source markdown, which parser)
EDITIONS = {
    "3rCvwAoWrzKGlIQdtLjCu": ("1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md", "root"),
    "oPhp5eN2PkvMoiq9pReuu": ("1-SOURCES/Text/BCAV08_SH_sk.md", "root"),
    "ru8JW2ztLc2dNEEibTXra": ("1-SOURCES/Translations/en-Wallace.md", "root"),
    "KR8O5cLLsJ6pJ7w63PDvG": ("1-SOURCES/Translations/en-David_Karma_Choephel.md", "root"),
    "UeXaNlPycKnnUpTnyXnas": ("1-SOURCES/Translations/zh-蔣揚仁欽譯師.md", "root"),
    "2AWdQyWXlLjIqMqLosTXV": ("3-TRANSFORMATIONS/Translations/AI_translation/english/bca-english-plain.md", "root"),
    "gz0jVjcJJ7IHFQiSRp9to": ("3-TRANSFORMATIONS/Translations/AI_translation/hindi/bca-hindi-plain.md", "root"),
    "YJRbRrAWPXC8TDr8doccI": ("3-TRANSFORMATIONS/Translations/AI_translation/marathi/bca-marathi-scholars.md", "root"),
    "AVGM32fuCApuhpmw7oa5q": ("3-TRANSFORMATIONS/Translations/AI_translation/marathi/bca-marathi-children.md", "root"),
    "nzztsifbIVhBlBHm2QWsT": ("1-SOURCES/Commentaries/Transcluded/BCAC14_NTS_bo_segmented.md", "commentary"),
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def build_content(mod, src, kind):
    """Content + segments, without going through build_edition().

    build_edition() resolves a translation's `root_text:` frontmatter only to
    pick a default segment type, and its fallback walks `rglob` up the parent
    directories — which from a vault under $HOME can reach the whole home
    directory and take minutes. None of that affects the content string, which
    is all this check compares, so it is skipped.
    """
    fm, body = mod._read_source(src)
    blocks = mod._extract_blocks(body)
    doc_default = "paragraph" if kind == "commentary" else "verse"
    content, segs, headings = mod._build_content_and_segmentation(blocks, doc_default)
    if kind == "commentary":
        content, segs, headings = mod._strip_verse_ids(content, segs, headings)
    return content, segs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", default="sweep-after")
    ap.add_argument("--only", action="append", default=[])
    args = ap.parse_args(argv)

    root = load("_pf_root", ROOT_PARSER)
    comm = load("_pf_comm", COMM_PARSER)
    tmp = Path(os.environ.get("TMPDIR", "/tmp")) / "preflight-toc-out"
    root.OUTPUT_DIR = tmp
    comm.OUTPUT_DIR = tmp

    print(f"{'edition':<24}{'lang/source':<46}{'live':>9}{'parsed':>9}  match")
    bad = []
    for eid, (rel, kind) in EDITIONS.items():
        if args.only and eid not in args.only:
            continue
        snap = SNAPDIR / args.snapshot / f"{eid}.json"
        if not snap.exists():
            print(f"{eid:<24}{rel[:44]:<46}{'':>9}{'':>9}  NO SNAPSHOT")
            bad.append((eid, "no snapshot"))
            continue
        live = json.load(open(snap))
        src = VAULT / rel
        mod = root if kind == "root" else comm
        lintdir = ROOT_LINT if kind == "root" else COMM_LINT
        lint = lintdir / f"{src.stem}.lint.json"
        if not lint.exists():
            print(f"{eid:<24}{rel[:44]:<46}{'':>9}{'':>9}  NO LINT FILE")
            bad.append((eid, "no lint file"))
            continue
        try:
            parsed, segs = build_content(mod, src, kind)
        except Exception as e:  # noqa: BLE001
            print(f"{eid:<24}{rel[:44]:<46}{'':>9}{'':>9}  PARSE ERROR {e!r}"[:200])
            bad.append((eid, f"parse error: {e!r}"))
            continue
        ok = hashlib.sha256(parsed.encode()).hexdigest() == live["content_sha256"]
        titles = sum(1 for s in segs if s["type"] == "title")
        note = "yes" if ok else f"NO ({len(parsed) - live['content_len']:+d} chars)"
        if titles:
            note += f"  !! {titles} title segments still emitted"
        print(f"{eid:<24}{Path(rel).name[:44]:<46}{live['content_len']:>9}{len(parsed):>9}  {note}")
        if not ok or titles:
            bad.append((eid, note))

    print(f"\n{len(EDITIONS) - len(bad)}/{len(EDITIONS)} editions reproduce their live content exactly")
    if bad:
        print("\nNOT safe to regenerate a TOC for:")
        for eid, why in bad:
            print(f"  {eid}  {why}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
