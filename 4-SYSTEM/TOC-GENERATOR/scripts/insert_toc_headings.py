#!/usr/bin/env python3
"""
insert_toc_headings.py -- Phase-2 deterministic renderer + verifier for the
`toc-generator` skill.

The skill works in two phases:

  Phase 1 (model)  -- read the commentary and identify every Sachad (sa bcad /
                       structural topic-announcement) in the text, classify
                       each as a main topic (depth 1) or a sub-topic (depth 2),
                       and emit a compact *annotation* (JSON): an ordered list
                       of sections, each with a depth, a short heading title,
                       and an exact, verbatim, line-unique `body_start_context`
                       marking where that topic's own text begins. No block
                       IDs, no heading syntax, no rewriting of prose.

  Phase 2 (this)   -- take the ORIGINAL file + the annotation and do
                       everything mechanical: assign `toc-N` / `toc-N-M` block
                       IDs from depth, insert a heading line (## or ###)
                       immediately before each topic's body line, and then
                       PROVE that no existing prose was altered before writing
                       -- to a NEW file. The source file is never modified.

Because IDs are assigned by code and headings are inserted by anchored exact
match, transcription drift or accidental prose edits are caught by a diff
check and the run fails loudly instead of silently corrupting the text.

Usage
-----
  Render TOC headings into a new file:
      python3 insert_toc_headings.py render \
          --input   commentary.md \
          --annot   commentary.annotation.json \
          --output  commentary.toc.md

  (If --output is omitted, it is derived as <input-stem>.toc.md next to the
   input, auto-suffixed -v2/-v3/... if that file already exists.)

  Verify an already-generated output against its untouched source:
      python3 insert_toc_headings.py verify \
          --input  commentary.md \
          --output commentary.toc.md

Annotation format
------------------
{
  "source_file": "commentary.md",
  "sections": [
    {"depth": 1, "heading_title": "...", "body_start_context": "<verbatim line or unique substring>"},
    {"depth": 2, "heading_title": "...", "body_start_context": "<verbatim line or unique substring>"}
  ]
}

See example-annotation.json in this folder for a worked example.

Exit status is non-zero on any error (ambiguous/missing anchor, bad depth,
attempt to overwrite the input, input already tagged, or a prose-integrity
violation) so callers can fail loudly.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field


class TocError(Exception):
    """Any condition that should abort with a clear message."""


# A heading line this script is allowed to have inserted: "## ... ^toc-N" or
# "### ... ^toc-N-M"
_HEADING_RE = re.compile(r"^(##|###)\s.*\s\^toc-\d+(?:-\d+)?\s*$")


def heading_prefix(depth: int) -> str:
    if depth == 1:
        return "##"
    if depth == 2:
        return "###"
    raise TocError(
        f"toc-generator only supports depth 1 (main topic) or depth 2 "
        f"(sub-topic); got depth {depth}. Collapse deeper Sachad nesting "
        f"into its nearest depth-2 ancestor instead of adding a depth 3+ node."
    )


def assign_block_ids(depths: list[int]) -> list[str]:
    """
    depth 1 -> '1', '2', '3', ...
    depth 2 under main topic N -> 'N-1', 'N-2', ...
    A depth-2 section may not appear before any depth-1 section.
    """
    c1 = 0
    c2 = 0
    ids: list[str] = []
    for i, d in enumerate(depths):
        if d not in (1, 2):
            raise TocError(f"section {i}: depth must be 1 or 2, got {d}")
        if d == 1:
            c1 += 1
            c2 = 0
            ids.append(str(c1))
        else:  # d == 2
            if c1 == 0:
                raise TocError(
                    f"section {i}: a sub-topic (depth 2) appears before any "
                    f"main topic (depth 1)"
                )
            c2 += 1
            ids.append(f"{c1}-{c2}")
    return ids


def find_unique_line(lines: list[str], context: str, what: str) -> int:
    hits = [i for i, ln in enumerate(lines) if context in ln]
    if not hits:
        raise TocError(f"{what}: context not found in source:\n    {context!r}")
    if len(hits) > 1:
        raise TocError(
            f"{what}: context is ambiguous (matches {len(hits)} lines: "
            f"{[h + 1 for h in hits]}). Lengthen body_start_context so it is "
            f"unique:\n    {context!r}"
        )
    return hits[0]


@dataclass
class LineEdits:
    headings: list[str] = field(default_factory=list)


def render(source: str, annot: dict) -> tuple[str, dict]:
    if any(_HEADING_RE.match(ln) for ln in source.splitlines()):
        raise TocError(
            "input already contains toc-generator heading markers "
            "(a line matching '## ... ^toc-N' or '### ... ^toc-N-M'). "
            "Pass the ORIGINAL, untouched source file as --input, not a "
            "previously generated *.toc.md output."
        )

    sections = annot.get("sections")
    if not isinstance(sections, list) or not sections:
        raise TocError("annotation has no non-empty 'sections' list")

    depths = [int(s["depth"]) for s in sections]
    block_ids = assign_block_ids(depths)

    lines = source.splitlines()
    edits: dict[int, LineEdits] = {}

    def edits_for(idx: int) -> LineEdits:
        return edits.setdefault(idx, LineEdits())

    n1 = n2 = 0
    for sec, block_id, depth in zip(sections, block_ids, depths):
        title = (sec.get("heading_title") or "").strip()
        if not title:
            raise TocError(f"section ^toc-{block_id} missing heading_title")
        body_ctx = sec.get("body_start_context") or ""
        if not body_ctx:
            raise TocError(f"section ^toc-{block_id} missing body_start_context")

        idx = find_unique_line(lines, body_ctx, f"section ^toc-{block_id}")
        heading_line = f"{heading_prefix(depth)} {title} ^toc-{block_id}"
        edits_for(idx).headings.append(heading_line)
        if depth == 1:
            n1 += 1
        else:
            n2 += 1

    out_lines: list[str] = []
    for i, line in enumerate(lines):
        le = edits.get(i)
        if le and le.headings:
            if out_lines and out_lines[-1].strip() != "":
                out_lines.append("")
            for h in le.headings:
                out_lines.append(h)
            out_lines.append("")
        out_lines.append(line)

    tagged = "\n".join(out_lines)
    if source.endswith("\n"):
        tagged += "\n"

    verify_prose_unchanged(source, tagged)

    report = {
        "sections": len(sections),
        "main_topics": n1,
        "sub_topics": n2,
        "max_depth": max(depths),
    }
    return tagged, report


def prose_signature(text: str, drop_headings: bool) -> list[str]:
    sig = []
    for ln in text.splitlines():
        if drop_headings and _HEADING_RE.match(ln):
            continue
        if ln.strip() == "":
            continue
        sig.append(ln)
    return sig


def verify_prose_unchanged(source: str, tagged: str) -> None:
    before = prose_signature(source, drop_headings=False)
    after = prose_signature(tagged, drop_headings=True)
    if before == after:
        return
    for i, (a, b) in enumerate(zip(before, after)):
        if a != b:
            raise TocError(
                "PROSE INTEGRITY VIOLATION at prose line "
                f"{i + 1}:\n  source: {a!r}\n  output: {b!r}"
            )
    raise TocError(
        "PROSE INTEGRITY VIOLATION: line count differs "
        f"(source {len(before)} prose lines, output {len(after)})."
    )


def derive_output_path(input_path: str) -> str:
    stem, _ext = os.path.splitext(input_path)
    if stem.endswith(".toc"):
        stem = stem[: -len(".toc")]
    candidate = f"{stem}.toc.md"
    if not os.path.exists(candidate):
        return candidate
    v = 2
    while os.path.exists(f"{stem}.toc-v{v}.md"):
        v += 1
    return f"{stem}.toc-v{v}.md"


def cmd_render(args: argparse.Namespace) -> int:
    in_path = os.path.abspath(args.input)
    out_path = (
        os.path.abspath(args.output) if args.output else derive_output_path(args.input)
    )

    if os.path.abspath(out_path) == in_path:
        raise TocError("refusing to write output to the same path as --input")

    with open(args.input, encoding="utf-8") as f:
        source = f.read()
    with open(args.annot, encoding="utf-8") as f:
        annot = json.load(f)

    tagged, report = render(source, annot)

    if os.path.exists(out_path) and not args.force:
        raise TocError(
            f"output already exists: {out_path} (pass --force to overwrite, "
            f"or omit --output to auto-version)"
        )

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tagged)

    print("toc-generator render OK")
    print(f"  input (untouched):  {args.input}")
    print(f"  output:              {out_path}")
    print(f"  sections:            {report['sections']}")
    print(f"  main topics (##):    {report['main_topics']}")
    print(f"  sub topics (###):    {report['sub_topics']}")
    print("  prose integrity:     VERIFIED (no existing prose altered)")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    with open(args.input, encoding="utf-8") as f:
        source = f.read()
    with open(args.output, encoding="utf-8") as f:
        tagged = f.read()
    verify_prose_unchanged(source, tagged)
    print("prose integrity: VERIFIED -- output alters no existing prose.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("render", help="insert TOC headings into a new file")
    pr.add_argument("--input", required=True)
    pr.add_argument("--annot", required=True)
    pr.add_argument("--output", default=None)
    pr.add_argument("--force", action="store_true")
    pr.set_defaults(func=cmd_render)

    pv = sub.add_parser("verify", help="verify an output file vs its source")
    pv.add_argument("--input", required=True)
    pv.add_argument("--output", required=True)
    pv.set_defaults(func=cmd_verify)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except TocError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
