#!/usr/bin/env python3
"""
ingest_inline_toc.py — Deterministic (no AI) Tibetan commentary tagger.

Reads a toc-tree-*.md (built by extract_toc_tree.py) and a plain commentary
.md, then produces a fully tagged commentary by:

  1. Parsing the TOC tree → ordered sections (depth, decimal, title).
  2. Searching each section's title string directly in the commentary text
     to locate its body-start line — no AI, pure string matching.
  3. Detecting parent announcement lines (where a section enumerates its
     children) and wrapping the child terms as forward wikilinks.
  4. Inserting ## heading lines and [[#^block-id|term]] wikilinks.
  5. Verifying prose integrity — no existing text is altered.
  6. Writing the tagged commentary.

Output format matches:
  0-INBOX/inline_toc_commentary/toc-bo-*.md

Usage
-----
  python 4-SYSTEM/scripts/toc_tree_extractor/ingest_inline_toc.py \\
      <commentary.md> <toc-tree.md>

  # Explicit output path:
  python ... --out 0-INBOX/inline_toc_commentary/toc-bo-mytext.md

  # Show every match/miss without writing:
  python ... --dry-run

Run with --help for all options.
"""

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Tibetan helpers
# ---------------------------------------------------------------------------
_TSHEG  = "་"   # U+0F0B inter-syllable dot
_SHAD   = "།"   # U+0F0D shad (sentence terminator)

_TIB_ORDINALS = [
    # longest first so the prefix test is greedy
    "བཅུ་གསུམ་པ", "བཅུ་གཉིས་པ", "བཅུ་གཅིག་པ", "བཅུ་པ",
    "དགུ་པ", "བརྒྱད་པ", "བདུན་པ", "དྲུག་པ", "ལྔ་པ",
    "བཞི་པ", "གསུམ་པ", "གཉིས་པ", "དང་པོ",
]

_YAML_BLOCK_RE  = re.compile(r"^---\n.*?^---\n", re.DOTALL | re.MULTILINE)
_TOC_ENTRY_RE   = re.compile(r"^\s*\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+(?P<text>.+)$")
_WIKILINK_RE    = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]")
_HEADING_TAG_RE = re.compile(r"^#{2,6}\s.*\s\^[0-9]+(?:-[0-9]+)*-0\s*$")


def strip_ordinal(title: str) -> str:
    """Remove the leading Tibetan ordinal (དང་པོ་ / གཉིས་པ་ / …) from a title."""
    t = title.strip()
    for ordinal in _TIB_ORDINALS:
        if t.startswith(ordinal):
            rest = t[len(ordinal):].lstrip(_TSHEG + " ")
            return rest if rest else t
    return t


def to_heading_title(title: str) -> str:
    """
    Strip ordinal, normalise trailing punctuation to a single shad །.
    E.g. "གཉིས་པ་འགྲུབ་ཚུལ་" → "འགྲུབ་ཚུལ།"
    """
    topic = strip_ordinal(title).rstrip(_TSHEG + _SHAD + " ")
    return topic + _SHAD


# ---------------------------------------------------------------------------
# TOC-tree parsing
# ---------------------------------------------------------------------------

def parse_toc_tree(tree_text: str) -> list[dict]:
    """Return [{depth, decimal, title}, …] in document order."""
    body = _YAML_BLOCK_RE.sub("", tree_text, count=1).lstrip("\n")
    sections = []
    for line in body.splitlines():
        m = _TOC_ENTRY_RE.match(line)
        if not m:
            continue
        dec   = m.group("dec")
        depth = len(dec.split("."))
        # Strip any trailing ^toc-… block IDs the tree may carry
        title = re.sub(r"\s*\^toc-[\d-]+$", "", m.group("text")).strip()
        sections.append({"depth": depth, "decimal": dec, "title": title})
    return sections


# ---------------------------------------------------------------------------
# Block-ID assignment  (depth-driven, same convention as tag_inline_toc.py)
# ---------------------------------------------------------------------------

class TagError(Exception):
    pass


def assign_block_ids(depths: list[int]) -> list[str]:
    """
    depth 1 → '1-0', '2-0', …
    depth 2 under section 1 → '1-1-0', '1-2-0', …
    Depth gaps (e.g. 10→12) are filled with 1-counters so the TOC tree
    never has to be perfectly contiguous.
    """
    counters: list[int] = []
    ids: list[str] = []
    for i, d in enumerate(depths):
        if d < 1:
            raise TagError(f"section {i}: depth must be ≥ 1, got {d}")
        if d > len(counters):
            # Fill any skipped levels with counter=1
            while len(counters) < d:
                counters.append(1)
        else:
            counters = counters[:d]
            counters[d - 1] += 1
        ids.append("-".join(str(c) for c in counters) + "-0")
    return ids


def heading_level(depth: int) -> str:
    """depth 1 → '##', depth 2 → '###', … capped at '######'."""
    return "#" * min(depth + 1, 6)


# ---------------------------------------------------------------------------
# Commentary line search
# ---------------------------------------------------------------------------

def _is_prose_line(line: str) -> bool:
    """Exclude blockquote lines and blank lines from body-start candidates."""
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith(">") and not stripped.startswith("#")


def find_body_line(lines: list[str], title: str,
                   claimed: set[int], label: str,
                   verbose: bool = False) -> int | None:
    """
    Return the index of the first unclaimed prose line containing `title`.

    Search strategy (in order):
      1. Exact title string (e.g. "གཉིས་པ་འགྲུབ་ཚུལ་")
      2. Title with trailing tsheg stripped
      3. Topic only (ordinal stripped)
      4. Topic with trailing tsheg stripped

    Returns None if no match found; warns on multiple matches.
    """
    candidates = []
    for variant in _search_variants(title):
        hits = [i for i, ln in enumerate(lines)
                if (variant in ln or variant in _nfc(ln) or variant in _nfd(ln))
                and _is_prose_line(ln) and i not in claimed]
        if hits:
            candidates = hits
            if verbose:
                print(f"    [{label}] matched {repr(variant)[:60]} → lines {[h+1 for h in hits]}")
            break

    if not candidates:
        return None
    if len(candidates) > 1 and verbose:
        print(f"  WARNING [{label}]: {len(candidates)} matches for title, "
              f"using first (line {candidates[0]+1})")
    return candidates[0]


def _nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)

def _nfd(s: str) -> str:
    return unicodedata.normalize("NFD", s)

def _tibetan_only(s: str) -> str:
    """Strip non-Tibetan characters (e.g. stray Thai/Latin) from a string."""
    return "".join(c for c in s if "ༀ" <= c <= "࿿" or c in (" ", _TSHEG, _SHAD))

def _search_variants(title: str) -> list[str]:
    """
    Ordered list of search strings to try for a section title.

    Tries (in order):
      1. Exact title / tsheg-stripped / shad-swapped
      2. Topic (ordinal stripped) + same punctuation variants
      3. Tibetan-only cleaned versions (removes stray non-Tibetan chars)
      4. NFC / NFD normalised forms of the above
      5. Keyword fallback: last 3 / 2 / 1 tsheg-separated syllables of topic
    """
    t     = title.strip()
    topic = strip_ordinal(t)
    clean = _tibetan_only(t).strip()
    clean_topic = _tibetan_only(topic).strip()

    variants: list[str] = []

    def add(s: str) -> None:
        s = s.strip()
        if s and s not in variants:
            variants.append(s)

    # Primary: title and topic with punctuation variants
    for base in [t, topic, clean, clean_topic]:
        add(base)
        add(base.rstrip(_TSHEG))
        add(base.rstrip(_SHAD))
        add(base.rstrip(_TSHEG + _SHAD))
        # Shad→tsheg swap (title ends with shad in TOC, tsheg in text)
        if base.endswith(_SHAD):
            add(base[:-1] + _TSHEG)
            add(base[:-1])

    # Unicode normalisation
    for base in [t, topic, clean, clean_topic]:
        for norm in (_nfc, _nfd):
            b = norm(base)
            add(b)
            add(b.rstrip(_TSHEG + _SHAD))

    # Keyword fallback: last N syllables of the (cleaned) topic
    syllables = [s for s in clean_topic.split(_TSHEG) if s.strip()]
    for n in [4, 3, 2]:
        if len(syllables) >= n:
            kw = _TSHEG.join(syllables[-n:])
            add(kw)
            add(_nfc(kw))
            add(kw.rstrip(_TSHEG + _SHAD))

    return variants


def find_match_text(line: str, title: str) -> str | None:
    """
    Return the exact substring of `line` that matches `title`.
    Tries each search variant against the raw line and NFC/NFD versions;
    returns the variant string only when it is actually present in the
    raw line (so apply_wraps can locate it).
    """
    for variant in _search_variants(title):
        if variant in line:
            return variant
        # If it matches a normalised form, find the raw span via char offsets
        for norm in (_nfc, _nfd):
            if variant in norm(line):
                # locate start in normalised, map back — simplest: re-search raw
                # by trying tsheg-boundary substrings around the match
                idx = norm(line).find(variant)
                if idx != -1:
                    raw_candidate = line[idx: idx + len(variant)]
                    if raw_candidate in line:
                        return raw_candidate
    return None


# ---------------------------------------------------------------------------
# Announcement-line detection
# ---------------------------------------------------------------------------

def find_announcement_line(lines: list[str],
                            child_topics: list[tuple[str, str]],
                            search_from: int,
                            search_to: int,
                            verbose: bool = False) -> int | None:
    """
    Find the line in lines[search_from:search_to] that contains the most
    child topic words.  Returns the line index, or None.

    child_topics: [(topic_string, block_id), …]
    search_from / search_to: line index range (exclusive end).
    """
    if not child_topics or search_from >= search_to:
        return None

    best_idx, best_count = None, 0
    for i in range(search_from, search_to):
        ln = lines[i]
        if not _is_prose_line(ln):
            continue
        count = sum(1 for topic, _ in child_topics if _topic_in_line(topic, ln))
        if count > best_count:
            best_count, best_idx = count, i

    if best_idx is not None and verbose:
        print(f"    announcement line {best_idx+1} ({best_count}/{len(child_topics)} topics found)")
    # Require at least 2 sibling topics to confirm it's really an enumeration
    # (except when there's only one child)
    min_required = min(2, len(child_topics))
    return best_idx if best_count >= min_required else None


def _topic_in_line(topic: str, line: str) -> bool:
    """Check whether a topic word (or normalised variants) is in a line."""
    t = topic.strip()
    return any(v and v in line
               for v in [t, t.rstrip(_TSHEG), t.rstrip(_SHAD), t.rstrip(_TSHEG + _SHAD)])


def find_topic_in_line(topic: str, line: str) -> str | None:
    """Return the matched substring of topic in line, or None."""
    t = topic.strip()
    for candidate in [t, t.rstrip(_TSHEG), t.rstrip(_SHAD), t.rstrip(_TSHEG + _SHAD)]:
        if candidate and candidate in line:
            return candidate
    return None


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

@dataclass
class LineEdits:
    headings: list[str]            = field(default_factory=list)
    wraps:    list[tuple[str,str]] = field(default_factory=list)   # (term, block_id)


def apply_wraps(line: str, wraps: list[tuple[str,str]]) -> str:
    """Wrap each (term, block_id) in line as [[#^block_id|term]]."""
    spans: list[tuple[int,int,str,str]] = []
    cursor: dict[str,int] = {}
    for term, bid in wraps:
        if not term:
            continue
        start = line.find(term, cursor.get(term, 0))
        if start == -1:
            # Unicode mismatch between TOC and commentary — skip silently
            continue
        end = start + len(term)
        cursor[term] = end
        spans.append((start, end, term, bid))
    spans.sort()
    # Remove overlapping spans (keep the first/longer one, skip the rest)
    clean: list[tuple[int,int,str,str]] = []
    for span in spans:
        s2, e2, t2, b2 = span
        if clean and s2 < clean[-1][1]:
            # overlaps with previous — skip silently
            continue
        clean.append(span)
    spans = clean
    out, prev = [], 0
    for s, e, term, bid in spans:
        out.append(line[prev:s])
        out.append(f"[[#^{bid}|{term}]]")
        prev = e
    out.append(line[prev:])
    return "".join(out)


def _unwrap_links(text: str) -> str:
    return _WIKILINK_RE.sub(lambda m: m.group(1), text)


def _prose_signature(text: str, drop_headings: bool) -> list[str]:
    sig = []
    for ln in text.splitlines():
        if drop_headings and _HEADING_TAG_RE.match(ln):
            continue
        ln = _unwrap_links(ln)
        if ln.strip():
            sig.append(ln)
    return sig


def verify_prose_unchanged(source: str, tagged: str) -> None:
    before = _prose_signature(source, drop_headings=False)
    after  = _prose_signature(tagged,  drop_headings=True)
    if before == after:
        return
    for i, (a, b) in enumerate(zip(before, after)):
        if a != b:
            raise TagError(
                f"PROSE INTEGRITY VIOLATION at prose line {i+1}:\n"
                f"  source: {a!r}\n  output: {b!r}")
    raise TagError(
        f"PROSE INTEGRITY VIOLATION: line count differs "
        f"(source {len(before)}, output {len(after)})")


# ---------------------------------------------------------------------------
# Main tagging logic
# ---------------------------------------------------------------------------

def tag_commentary(source_text: str, toc_sections: list[dict],
                   verbose: bool = False) -> tuple[str, dict]:
    """
    Insert headings and wikilinks into source_text guided by toc_sections.
    Returns (tagged_text, report_dict).
    """
    lines     = source_text.splitlines()
    depths    = [s["depth"] for s in toc_sections]
    block_ids = assign_block_ids(depths)

    # -----------------------------------------------------------------------
    # Pass 1 — find body-start line for each section
    # -----------------------------------------------------------------------
    body_lines: list[int | None] = []   # parallel to toc_sections
    claimed:    set[int]         = set()

    for sec, bid in zip(toc_sections, block_ids):
        title = sec["title"]
        label = f"{sec['decimal']} {title[:40]}"
        idx   = find_body_line(lines, title, claimed, label, verbose)
        body_lines.append(idx)
        if idx is not None:
            claimed.add(idx)
        else:
            print(f"  MISS  {sec['decimal']:30s}  {sec['title'][:60]}")

    found_count = sum(1 for x in body_lines if x is not None)
    if verbose:
        print(f"\nFound {found_count}/{len(toc_sections)} section body lines.\n")

    # -----------------------------------------------------------------------
    # Pass 2 — collect edits
    # -----------------------------------------------------------------------
    edits: dict[int, LineEdits] = {}

    def ed(i: int) -> LineEdits:
        return edits.setdefault(i, LineEdits())

    n_headings = n_restate = n_announce = 0

    for sec, bid, body_idx in zip(toc_sections, block_ids, body_lines):
        if body_idx is None:
            continue

        # Insert heading before body line
        ht = to_heading_title(sec["title"])
        ed(body_idx).headings.append(f"{heading_level(sec['depth'])} {ht} ^{bid}")
        n_headings += 1

        # Wrap restatement (full title as it actually appears on the line)
        matched_text = find_match_text(lines[body_idx], sec["title"])
        if matched_text:
            ed(body_idx).wraps.append((matched_text, bid))
            n_restate += 1

    # -----------------------------------------------------------------------
    # Pass 3 — parent announcement wikilinks
    # -----------------------------------------------------------------------
    # Group sections by parent decimal (everything up to last ".")
    from collections import defaultdict
    by_parent: dict[str, list[int]] = defaultdict(list)
    for i, sec in enumerate(toc_sections):
        dec = sec["decimal"]
        parent = dec.rsplit(".", 1)[0] if "." in dec else ""
        by_parent[parent].append(i)

    for parent_dec, child_indices in by_parent.items():
        # Only look for announcements when parent has ≥ 2 children
        # (single children are usually not pre-announced on a separate line)
        child_body_lines = [body_lines[i] for i in child_indices
                            if body_lines[i] is not None]
        if not child_body_lines:
            continue

        first_child_line = min(child_body_lines)

        # The parent's own body line (where its scope begins)
        if parent_dec:
            parent_idx_in_toc = next(
                (i for i, s in enumerate(toc_sections)
                 if s["decimal"] == parent_dec), None)
            parent_body = (body_lines[parent_idx_in_toc]
                           if parent_idx_in_toc is not None else None)
        else:
            parent_body = None   # top-level sections have no parent body

        search_from = (parent_body + 1) if parent_body is not None else 0
        search_to   = first_child_line   # must appear BEFORE the first child

        child_topics: list[tuple[str, str]] = []
        for i in child_indices:
            if body_lines[i] is None:
                continue
            topic = strip_ordinal(toc_sections[i]["title"]).rstrip(_TSHEG)
            child_topics.append((topic, block_ids[i]))

        ann_line = find_announcement_line(
            lines, child_topics, search_from, search_to, verbose)
        if ann_line is None:
            continue

        for topic, bid in child_topics:
            matched = find_topic_in_line(topic, lines[ann_line])
            if matched:
                ed(ann_line).wraps.append((matched, bid))
                n_announce += 1

    # -----------------------------------------------------------------------
    # Pass 4 — build output
    # -----------------------------------------------------------------------
    out: list[str] = []
    for i, line in enumerate(lines):
        le = edits.get(i)
        new_line = apply_wraps(line, le.wraps) if le and le.wraps else line
        if le and le.headings:
            if out and out[-1].strip():
                out.append("")
            for h in le.headings:
                out.append(h)
            out.append("")
        out.append(new_line)

    tagged = "\n".join(out)
    if source_text.endswith("\n"):
        tagged += "\n"

    verify_prose_unchanged(source_text, tagged)

    report = {
        "sections_total":      len(toc_sections),
        "sections_found":      found_count,
        "sections_missed":     len(toc_sections) - found_count,
        "headings_inserted":   n_headings,
        "restatements_tagged": n_restate,
        "announcements_tagged":n_announce,
    }
    return tagged, report


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_vault_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "4-SYSTEM").is_dir():
            return p
    return start.parent if start.is_file() else start


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tag a Tibetan commentary with sa-bcad headings and wikilinks (no AI).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("commentary",
                        help="Source commentary .md (plain text, no headings)")
    parser.add_argument("toc_tree",
                        help="toc-tree-<id>.md produced by extract_toc_tree.py")
    parser.add_argument("--out", default=None,
                        help="Output path (default: 0-INBOX/inline_toc_commentary/toc-<id>.md)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show match results without writing output")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print per-section match details")
    parser.add_argument("--vault-root", default=None)
    args = parser.parse_args()

    commentary_path = Path(args.commentary).expanduser().resolve()
    toc_path        = Path(args.toc_tree).expanduser().resolve()

    if not commentary_path.exists():
        sys.exit(f"Error: commentary not found: {commentary_path}")
    if not toc_path.exists():
        sys.exit(f"Error: TOC tree not found: {toc_path}")

    vault_root = (Path(args.vault_root).resolve() if args.vault_root
                  else find_vault_root(commentary_path))

    # Default output path
    commentary_id = re.sub(r"^toc-tree-", "", toc_path.stem)
    if args.out:
        out_path = Path(args.out).expanduser().resolve()
    else:
        out_path = vault_root / "0-INBOX" / "inline_toc_commentary" / f"toc-{commentary_id}.md"

    print(f"TOC tree:     {toc_path}")
    print(f"Commentary:   {commentary_path}")
    if not args.dry_run:
        print(f"Output:       {out_path}")
    print()

    source_text  = commentary_path.read_text(encoding="utf-8")
    tree_text    = toc_path.read_text(encoding="utf-8")
    toc_sections = parse_toc_tree(tree_text)

    if not toc_sections:
        sys.exit("Error: no sections parsed from toc-tree file.")

    print(f"TOC sections: {len(toc_sections)}")
    print()

    try:
        tagged, report = tag_commentary(
            source_text, toc_sections, verbose=args.verbose or args.dry_run)
    except TagError as e:
        sys.exit(f"Error: {e}")

    # Report
    print(f"Sections found:       {report['sections_found']}/{report['sections_total']}")
    if report["sections_missed"]:
        print(f"Sections missed:      {report['sections_missed']}  (run with -v to see which)")
    print(f"Headings inserted:    {report['headings_inserted']}")
    print(f"Restatements tagged:  {report['restatements_tagged']}")
    print(f"Announcements tagged: {report['announcements_tagged']}")
    print(f"Prose integrity:      VERIFIED")

    if args.dry_run:
        print("\n(dry-run — no file written)")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(tagged, encoding="utf-8")
    print(f"\nWritten: {out_path}")


if __name__ == "__main__":
    main()
