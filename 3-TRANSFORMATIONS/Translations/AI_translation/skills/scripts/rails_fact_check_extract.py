#!/usr/bin/env python3
"""
rails_fact_check_extract.py
============================

Extracts paired verse data for fact-checking an AI_translation output
against `2-RAILS/Verses/<chapter>-<verse>-summary.md` rail files, instead
of a raw `1-SOURCES/` commentary (the vault's `commentary-fact-check`
skill uses the latter; this script is the RAILS/Verses counterpart
requested for the AI_translation workspace's step 5).

For each verse in the requested chapter(s), pulls from the rail file:
  - `status` (frontmatter) — rail files here are all `status: draft`;
    surfaced so the auditor knows this is not yet domain-specialist-approved.
  - `key_terms` — the གནད་ཚིག (Key terms) block list: one entry per
    term with its commentary-derived gloss and source citation. This is
    the closest rail equivalent to commentary-fact-check's "anchors" —
    the mandatory term-by-term checklist.
  - `synthesis` — the བསྡུས་དོན (AI-Overview synthesis) section: intro
    paragraph + bullet points, already commentary-grounded and concise.

And from the translation file:
  - `translation` — the full multi-line English text for that verse,
    reassembled from the source's per-segment block format (N lines of
    verse followed by ` ^chapter-verse` on the last line, one blank line
    between segments — see AI_translation/skills/requirements.md §4).

Coverage gaps (a verse present in one file but not the other) are
reported, never silently dropped.

Usage:
    python3 rails_fact_check_extract.py \\
        --rails-dir 2-RAILS/Verses \\
        --translation AI_translation/english/bca-english-plain.md \\
        --chapters 1,2,3,4 \\
        --json /tmp/pairs.json

Output JSON shape:
    {
      "1-1": {
        "translation": "I bow respectfully ... ^1-1 stripped",
        "key_terms": [{"term": "...", "gloss": "...", "source": "..."}],
        "synthesis": "...",
        "rail_file": "2-RAILS/Verses/1-1-summary.md",
        "rail_status": "draft"
      },
      ...
    }
"""
import argparse
import json
import re
from pathlib import Path

VERSE_ID_RE = re.compile(r"^\d+-\d+$")


# ---------------------------------------------------------------------------
# Translation file parsing (multi-line verse blocks)
# ---------------------------------------------------------------------------

ID_LINE_RE = re.compile(r"^(.*?)\s*\^(\d+-\d+)\s*$")


def parse_translation(content):
    """Parse a merged translation file into {verse_id: full_text}.

    Blocks are separated by blank lines. Within a block, the ID marker
    (` ^chapter-verse`) may sit on the *first* line or the *last* line —
    this file mixes both conventions (chapters 1-3 put it at the end of
    the block; chapter 4 puts it on the first line), so every line in the
    block is checked rather than assuming a fixed position. Chapter/section
    headings (`^N-0`) are excluded. Blocks whose lines carry two different
    verse IDs are flagged and skipped rather than silently merged.
    """
    blocks = re.split(r"\r?\n\s*\r?\n", content)
    verses = {}
    ambiguous = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        vid = None
        cleaned_lines = []
        conflict = False
        for l in lines:
            m = ID_LINE_RE.match(l.strip())
            if m and m.group(2).split("-")[1] != "0":
                found_vid = m.group(2)
                if vid is not None and vid != found_vid:
                    conflict = True
                vid = found_vid
                text = re.sub(r"^#+\s*", "", m.group(1)).strip()
                if text:
                    cleaned_lines.append(text)
            else:
                cleaned_lines.append(re.sub(r"^#+\s*", "", l))
        if vid is None:
            continue
        if conflict:
            ambiguous.append(vid)
            continue
        verses[vid] = "\n".join(cleaned_lines).strip()
    if ambiguous:
        print(f"WARNING: block(s) with conflicting verse IDs, skipped: {ambiguous}")
    return verses


# ---------------------------------------------------------------------------
# Rail summary file parsing
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
KEY_TERMS_SECTION_RE = re.compile(
    r"##\s*གནད་ཚིག.*?\n(.*?)(?=\n##\s|\Z)", re.DOTALL
)
KEY_TERM_ENTRY_RE = re.compile(
    r"####\s*གནད་ཚིག\s*\n(.+?)\n"
    r"####\s*འགྲེལ་བཤད[^\n]*\n(.+?)\n"
    r"####\s*ཁུངས[^\n]*\n(.+?)(?=\n####\s*གནད་ཚིག|\Z)",
    re.DOTALL,
)


def clean_term(raw):
    """Strip surrounding markdown bold markers from a term line without
    dropping alias text in parentheses (e.g. '**word** (alias1 / alias2)')."""
    t = raw.strip()
    t = re.sub(r"\*\*", "", t)
    return re.sub(r"\s+", " ", t).strip()
SYNTHESIS_SECTION_RE = re.compile(
    r"##\s*བསྡུས་དོན.*?\n(.*?)\Z", re.DOTALL
)


def parse_rail_file(path):
    content = path.read_text(encoding="utf-8")

    status = None
    fm = FRONTMATTER_RE.match(content)
    if fm:
        sm = re.search(r"^status:\s*(\S+)", fm.group(1), re.MULTILINE)
        if sm:
            status = sm.group(1)

    key_terms = []
    kt_section = KEY_TERMS_SECTION_RE.search(content)
    if kt_section:
        for m in KEY_TERM_ENTRY_RE.finditer(kt_section.group(1)):
            term, gloss, source = m.groups()
            key_terms.append(
                {
                    "term": clean_term(term),
                    "gloss": re.sub(r"\s+", " ", gloss.strip()),
                    "source": re.sub(r"\s+", " ", source.strip()),
                }
            )

    synthesis = None
    syn_section = SYNTHESIS_SECTION_RE.search(content)
    if syn_section:
        synthesis = syn_section.group(1).strip()

    return {"status": status, "key_terms": key_terms, "synthesis": synthesis}


# ---------------------------------------------------------------------------
# Pairing
# ---------------------------------------------------------------------------

def build_pairs(rails_dir, translation_verses, chapters):
    rails_dir = Path(rails_dir)
    pairs = {}
    rail_only, translation_only = [], []

    rail_ids = set()
    for f in rails_dir.glob("*-summary.md"):
        m = re.match(r"^(\d+)-(\d+)-summary\.md$", f.name)
        if not m:
            continue
        vid = f"{m.group(1)}-{m.group(2)}"
        if chapters and m.group(1) not in chapters:
            continue
        rail_ids.add(vid)

    translation_ids = {
        vid for vid in translation_verses if not chapters or vid.split("-")[0] in chapters
    }

    for vid in sorted(rail_ids | translation_ids, key=lambda v: [int(x) for x in v.split("-")]):
        in_rail = vid in rail_ids
        in_trans = vid in translation_ids
        if in_rail and not in_trans:
            rail_only.append(vid)
            continue
        if in_trans and not in_rail:
            translation_only.append(vid)
            continue

        rail_path = rails_dir / f"{vid}-summary.md"
        parsed = parse_rail_file(rail_path)
        pairs[vid] = {
            "translation": translation_verses[vid],
            "key_terms": parsed["key_terms"],
            "synthesis": parsed["synthesis"],
            "rail_file": str(rail_path).replace("\\", "/"),
            "rail_status": parsed["status"],
        }

    return pairs, rail_only, translation_only


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rails-dir", default="2-RAILS/Verses", help="Directory of <chapter>-<verse>-summary.md rail files")
    ap.add_argument("--translation", required=True, help="Path to the merged translation .md file")
    ap.add_argument("--chapters", default=None, help="Comma-separated chapter numbers to include (default: all)")
    ap.add_argument("--json", default=None, help="Write the paired {verse_id: {...}} JSON to this path")
    args = ap.parse_args()

    chapters = set(args.chapters.split(",")) if args.chapters else None

    translation_content = Path(args.translation).read_text(encoding="utf-8")
    translation_verses = parse_translation(translation_content)

    pairs, rail_only, translation_only = build_pairs(args.rails_dir, translation_verses, chapters)

    print(f"Paired {len(pairs)} verses.")
    if rail_only:
        print(f"WARNING: {len(rail_only)} verse(s) have a rail summary but no translation match: {rail_only}")
    if translation_only:
        print(f"WARNING: {len(translation_only)} verse(s) have a translation but no rail summary: {translation_only}")
    no_key_terms = [vid for vid, d in pairs.items() if not d["key_terms"]]
    if no_key_terms:
        print(f"NOTE: {len(no_key_terms)} paired verse(s) have an empty Key Terms section (nothing to anchor a term-check on): {no_key_terms}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(pairs, f, ensure_ascii=False, indent=2)
        print(f"Wrote {len(pairs)} pairs to {args.json}")


if __name__ == "__main__":
    main()
