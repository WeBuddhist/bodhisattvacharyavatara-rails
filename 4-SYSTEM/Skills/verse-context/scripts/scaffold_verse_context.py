#!/usr/bin/env python3
"""
scaffold_verse_context.py — produce a structurally complete `2-RAILS/Verses/<verse-id>.md`
scaffold for one verse, leaving the LLM-heavy sections (Synthesis, Consensus,
Divergences, Disambiguated Restatement) as TODO placeholders for a later fill step.

Heuristic for locating commentary blocks
----------------------------------------
The commentary source files in this vault explicitly embed a transclusion of
each root-text block immediately before the commentary that discusses it:

    ![[1-SOURCES/Text/pi-dhammasangani.md#^1-0a-2]]

    Sukhāya vedanāyātiādīsu ... ^1-519
    ... ^1-520
    ... ^1-521

    ![[1-SOURCES/Text/pi-dhammasangani.md#^1-0a-3]]
    ...

So the scaffold finds the transclusion marker for the target verse and collects
every `^<block-id>` it sees before the next transclusion marker. If a
commentary contains no transclusion marker for the target verse, the
commentary subsection is emitted with an explanatory TODO so the LLM-fill step
can decide whether to drop the commentary from `commentaries:` or to search by
content.

Usage
-----
    python scaffold_verse_context.py 1-0a-2
    python scaffold_verse_context.py 1-0a-2 --root C:/path/to/abhidhamma-rails
    python scaffold_verse_context.py 1-0a-2 --dry-run        # print to stdout
    python scaffold_verse_context.py 1-0a-2 --overwrite      # overwrite an existing file
    python scaffold_verse_context.py 1-0a-2 --validate       # check existing scaffold

Inputs are configured via the constants block at the top of the file (root
text, commentary list). The script is text-agnostic in structure but is
currently configured for the Dhammasaṅgaṇī (kusalattika onwards).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------------------
# Configuration (text-specific defaults — override via CLI flags if needed)
# ---------------------------------------------------------------------------

DEFAULT_ROOT_TEXT = "1-SOURCES/Text/pi-dhammasangani.md"
DEFAULT_LANGUAGE = "pi"
DEFAULT_COMMENTARIES = [
    "dhammasangani-atthakatha",
    "dhammasangani-mulatiika",
    "dhammasangani-anutiika",
]
COMMENTARY_FILE_FOR_ID = {
    "dhammasangani-atthakatha": "1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md",
    "dhammasangani-mulatiika": "1-SOURCES/Commentaries/pi-dhammasangani-mulatiika.md",
    "dhammasangani-anutiika": "1-SOURCES/Commentaries/pi-dhammasangani-anutiika.md",
}
OUTPUT_DIR = "2-RAILS/Verses"

# Regex for an Obsidian block ID anchored at end of a line: `^chap-verse` or `^N-NNN`.
BLOCK_ID_RE = re.compile(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)")
# Regex for a transclusion line targeting the root text block we care about.
TRANSCLUSION_TEMPLATE = r"!\[\[[^\]]*?#\^{verse_id}\s*\]\]"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class CommentaryMatch:
    commentary_id: str
    source_file: str
    block_ids: list[str] = field(default_factory=list)
    found_transclusion: bool = False


@dataclass
class ScaffoldResult:
    verse_id: str
    source_pointer: str
    commentary_matches: list[CommentaryMatch]
    output_path: Path
    text: str


# ---------------------------------------------------------------------------
# Core extraction logic
# ---------------------------------------------------------------------------

def _read_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as fh:
        return fh.read()


def _verse_exists_in_source(source_text: str, verse_id: str) -> bool:
    """The root text should contain `^<verse_id>` somewhere."""
    return bool(re.search(rf"\^{re.escape(verse_id)}\b", source_text))


def _extract_commentary_blocks(commentary_text: str, verse_id: str) -> CommentaryMatch | None:
    """Scan the commentary for the transclusion marker pointing at verse_id and
    collect every `^block-id` between that marker and the next root-text
    transclusion marker (or end of file).

    Returns None for the caller-provided field defaults; the caller wraps the
    returned block list into a CommentaryMatch.
    """
    # Find every transclusion line in the commentary along with its char offset.
    transclusion_iter = list(
        re.finditer(r"!\[\[[^\]]*?#\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*\]\]", commentary_text)
    )
    target_idx = next(
        (i for i, m in enumerate(transclusion_iter) if m.group(1) == verse_id),
        None,
    )
    if target_idx is None:
        return CommentaryMatch(
            commentary_id="",  # filled in by caller
            source_file="",  # filled in by caller
            block_ids=[],
            found_transclusion=False,
        )

    start = transclusion_iter[target_idx].end()
    if target_idx + 1 < len(transclusion_iter):
        end = transclusion_iter[target_idx + 1].start()
    else:
        end = len(commentary_text)

    window = commentary_text[start:end]
    # Collect block IDs in document order, de-duplicated. We skip any block ID
    # that matches the verse_id itself (defensive — shouldn't happen because
    # the verse_id is a transclusion target, not a block ID inside the
    # commentary file).
    seen: set[str] = set()
    ordered: list[str] = []
    for m in BLOCK_ID_RE.finditer(window):
        bid = m.group(1)
        if bid == verse_id or bid in seen:
            continue
        seen.add(bid)
        ordered.append(bid)
    return CommentaryMatch(
        commentary_id="",
        source_file="",
        block_ids=ordered,
        found_transclusion=True,
    )


def gather_matches(
    root: Path,
    verse_id: str,
    commentary_ids: Iterable[str],
) -> tuple[str, list[CommentaryMatch]]:
    """Returns (source_pointer, list_of_commentary_matches)."""
    source_path = root / DEFAULT_ROOT_TEXT
    source_text = _read_file(source_path)
    if not _verse_exists_in_source(source_text, verse_id):
        raise SystemExit(
            f"verse_id ^{verse_id} not found in root text {source_path}"
        )

    matches: list[CommentaryMatch] = []
    for cid in commentary_ids:
        rel = COMMENTARY_FILE_FOR_ID.get(cid)
        if rel is None:
            print(f"warning: no source-file mapping for commentary {cid!r}; skipping",
                  file=sys.stderr)
            continue
        commentary_path = root / rel
        if not commentary_path.exists():
            print(f"warning: commentary file missing on disk: {commentary_path}; skipping",
                  file=sys.stderr)
            continue
        commentary_text = _read_file(commentary_path)
        m = _extract_commentary_blocks(commentary_text, verse_id)
        # mypy is happy because _extract_commentary_blocks always returns a
        # CommentaryMatch in this code path.
        assert m is not None
        m.commentary_id = cid
        m.source_file = rel
        matches.append(m)

    return DEFAULT_ROOT_TEXT, matches


# ---------------------------------------------------------------------------
# Scaffold rendering
# ---------------------------------------------------------------------------

FRONTMATTER_TEMPLATE = """---
verse_id: {verse_id}
root_text: {source_pointer}
root_block: ^{verse_id}
language: {language}
commentaries: [{commentary_list}]
build_status: scaffold
status: draft
---
"""

VERSE_BLOCK_TEMPLATE = """
## Verse

![[{source_pointer}#^{verse_id}]]
"""

COMMENTARY_HEADER = """
## Commentary passages
"""

COMMENTARY_SUBSECTION_HEADER = "\n### {commentary_id}\n"
COMMENTARY_NO_MATCH_NOTE = (
    "\n_TODO: no transclusion marker for ^{verse_id} found in this commentary._\n"
    "_If the commentary nonetheless discusses this verse, locate the relevant_\n"
    "_blocks by content and add them here; otherwise drop this commentary from_\n"
    "_the `commentaries:` frontmatter._\n"
)

TODO_BODY = """
## Synthesis (per commentator)

TODO — for each commentary listed above, write a paragraph in the original
language (Pāli) stating how this commentary reads the verse: what each word
refers to, how each compound is parsed, which sense of an ambiguous term is
active, what each pronoun's antecedent is. Cite every claim with
`(1-SOURCES/Commentaries/<commentary>.md#^<block-id>)`.

### dhammasangani-atthakatha

TODO

### dhammasangani-mulatiika

TODO

### dhammasangani-anutiika

TODO

## Consensus

TODO — one paragraph in the original language (Pāli) stating what every
commentary listed agrees on for this verse: referents, sense selections,
compound readings. Cite the underlying commentary blocks.

## Divergences ⚑

TODO — one bullet per genuine disagreement. Both readings, both flagged with
⚑, both cited. If there is no genuine divergence, write `_No genuine
divergence among the listed commentaries._` and omit the placeholder bullets.

- **<token or phrase>** — <commentary-A> reads … ⚑; <commentary-B> reads … ⚑.
  (1-SOURCES/Commentaries/<commentary-A>.md#^<block-id>)
  (1-SOURCES/Commentaries/<commentary-B>.md#^<block-id>)

## Disambiguated Restatement (original language)

TODO — rewrite the verse in the original language (Pāli) so that every
ambiguity the Synthesis resolves is explicit. Annotate every key term
morphologically (case, number, gender / verb form) and footnote the sense
selected with a citation to the commentary block that authorises it. Where
commentaries diverge, follow the Consensus reading and mark each alternative
with ⚑.
"""


def render_scaffold(
    verse_id: str,
    source_pointer: str,
    commentary_matches: list[CommentaryMatch],
    language: str = DEFAULT_LANGUAGE,
) -> str:
    commentary_list = ", ".join(m.commentary_id for m in commentary_matches)
    out: list[str] = [
        FRONTMATTER_TEMPLATE.format(
            verse_id=verse_id,
            source_pointer=source_pointer,
            language=language,
            commentary_list=commentary_list,
        ).rstrip("\n"),
        VERSE_BLOCK_TEMPLATE.format(
            source_pointer=source_pointer, verse_id=verse_id
        ).rstrip("\n"),
        COMMENTARY_HEADER.rstrip("\n"),
    ]

    for m in commentary_matches:
        out.append(COMMENTARY_SUBSECTION_HEADER.format(commentary_id=m.commentary_id).rstrip("\n"))
        if not m.found_transclusion:
            out.append(COMMENTARY_NO_MATCH_NOTE.format(verse_id=verse_id).rstrip("\n"))
            continue
        if not m.block_ids:
            out.append(
                "\n_TODO: transclusion marker found, but no block IDs followed it; "
                "verify the commentary file._\n".rstrip("\n")
            )
            continue
        for bid in m.block_ids:
            out.append(f"![[{m.source_file}#^{bid}]]")

    out.append(TODO_BODY.rstrip("\n"))
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Validation (for `--validate`)
# ---------------------------------------------------------------------------

REQUIRED_HEADINGS = [
    "## Verse",
    "## Commentary passages",
    "## Synthesis",
    "## Consensus",
    "## Divergences",
    "## Disambiguated Restatement",
]


def validate_scaffold(path: Path) -> tuple[bool, list[str]]:
    text = _read_file(path)
    errors: list[str] = []
    for h in REQUIRED_HEADINGS:
        if h not in text:
            errors.append(f"missing required heading: {h!r}")
    if "verse_id:" not in text:
        errors.append("frontmatter missing verse_id")
    if "build_status:" not in text:
        errors.append("frontmatter missing build_status")
    return (not errors), errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("verse_id", help="block ID without caret, e.g. 1-0a-2")
    
    # Determine default root relative to this script's directory
    script_dir = Path(__file__).resolve().parent
    if len(script_dir.parents) >= 4:
        default_root = script_dir.parents[3]
    else:
        default_root = Path.cwd()

    p.add_argument(
        "--root",
        default=os.environ.get("VAULT_ROOT", str(default_root)),
        help="vault root (defaults to $VAULT_ROOT or detected vault root)",
    )
    p.add_argument(
        "--language", default=DEFAULT_LANGUAGE, help="root-text language tag",
    )
    p.add_argument(
        "--commentaries",
        nargs="+",
        default=DEFAULT_COMMENTARIES,
        help="commentary IDs to include (in order)",
    )
    p.add_argument(
        "--out",
        default=None,
        help="explicit output path; default <root>/2-RAILS/Verses/<verse-id>.md",
    )
    p.add_argument("--dry-run", action="store_true", help="print to stdout, do not write")
    p.add_argument("--overwrite", action="store_true", help="overwrite an existing file")
    p.add_argument(
        "--validate",
        action="store_true",
        help="validate the existing output file rather than scaffolding",
    )
    args = p.parse_args(argv)

    root = Path(args.root).resolve()
    output_path = (
        Path(args.out)
        if args.out is not None
        else root / OUTPUT_DIR / f"{args.verse_id}.md"
    )

    if args.validate:
        ok, errs = validate_scaffold(output_path)
        if ok:
            print(f"ok: {output_path}")
            return 0
        for e in errs:
            print(f"error: {e}", file=sys.stderr)
        return 1

    source_pointer, matches = gather_matches(root, args.verse_id, args.commentaries)
    text = render_scaffold(args.verse_id, source_pointer, matches, language=args.language)

    if args.dry_run:
        print(text)
        return 0

    if output_path.exists() and not args.overwrite:
        print(
            f"refusing to overwrite existing file {output_path} "
            "(pass --overwrite to replace it)",
            file=sys.stderr,
        )
        return 2

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    summary = ", ".join(
        f"{m.commentary_id}={len(m.block_ids)}" for m in matches
    )
    print(f"wrote {output_path} ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
