#!/usr/bin/env python3
"""
restructure_toc.py — Post-process a lekphi-format TOC to fix sa-bcad nesting.

Long sa-bcad overview entries encode the full section hierarchy inline.
This script:
  1. Compresses long overview entries to their section title
  2. Inserts synthetic intermediate headings (depth 2) implied by the overview
  3. Promotes following tagged entries to depth 3 when the overview has 2 levels
  4. Removes meaningless stub entries (bare ལ་, ནི།, etc.)
  5. Re-numbers all ^toc-X-Y-Z block IDs

Usage:  python restructure_toc.py <toc_file.md> [--output <out_file.md>]
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tibetan text helpers
# ---------------------------------------------------------------------------

_ORDINAL_PAT = re.compile(
    r"^(?:དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|"
    r"བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ)[་།\s]*",
    re.UNICODE,
)
_BRACKET_MARKERS = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]༽\s*|^[ཀ-ཬ]༽\s*", re.UNICODE)

def strip_ordinal(text):
    t = _ORDINAL_PAT.sub("", text.strip())
    t = _BRACKET_MARKERS.sub("", t)
    return t.strip()


# ---------------------------------------------------------------------------
# Title extraction from long overview entries
# ---------------------------------------------------------------------------

# Enumeration markers that signal the end of a section title and start of a list
_ENUM_MARKERS = re.compile(
    r"(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་)"
    r"(?:ལས།|སྟེ།|དང་བཅས།|ལས་།)",
    re.UNICODE,
)
_INTRO_PREAMBLE = re.compile(
    r"^(?:འདི་ཉིད་|གཞུང་འདི་|མདོ་[^།]{,20}།\s*)?",
    re.UNICODE,
)

def extract_section_title(raw_text):
    """
    Extract a clean section title from a long sa-bcad overview entry.

    The overview text typically reads (translated):
      "In explaining X, there are TWO parts: A and B.
       The FIRST, A, has THREE parts: a, b, c.
       The first, a, has ..."

    The CURRENT FOCUS is whatever the overview is expanding last —
    found by the last "དང་པོ་TITLE ལ་N་སྟེ/ལས།" pattern.
    Falls back to the first item in "A དང་། B གཉིས་ལས།".
    """
    text = raw_text.strip()

    # Pattern 1 — last "དང་པོ་TITLE ལ་N་སྟེ།/ལས།"
    # This identifies the innermost level currently being expanded.
    p1 = re.compile(
        r"དང་པོ་([^།]{4,}?)ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)"
        r"(?:ལས།|སྟེ།)",
        re.UNICODE,
    )
    hits = list(p1.finditer(text))
    if hits:
        candidate = hits[-1].group(1).strip().rstrip("་")
        candidate = strip_ordinal(candidate)
        if len(candidate) >= 4:
            return candidate + ("།" if not candidate.endswith("།") else "")

    # Pattern 2 — "PREAMBLE TITLE དང་། OTHER གཉིས་ལས།"
    # The TITLE is the first of the two items enumerated.
    p2 = re.compile(
        r"ལ།\s+([^།]{4,}?)དང་།[^།]{4,}གཉིས་ལས།",
        re.UNICODE,
    )
    m = p2.search(text)
    if m:
        candidate = strip_ordinal(m.group(1).strip().rstrip("་"))
        if len(candidate) >= 4:
            return candidate + ("།" if not candidate.endswith("།") else "")

    # Pattern 3 — "TITLE ལ། SUB1 དང་།…" (the bit before the first ལ། + list)
    # Split at the first enumeration marker
    parts = _ENUM_MARKERS.split(text, maxsplit=1)
    candidate = parts[0].strip()
    # Trim trailing "ལ་" or "ལ།"
    candidate = re.sub(r"\s*ལ།?\s*$", "", candidate).strip()
    # Strip any leading preamble like "འདི་ཉིད་འཆད་པར་བྱེད་པ་ལ།"
    candidate = _INTRO_PREAMBLE.sub("", candidate).strip()
    # Drop leading "ལ།" left-overs
    candidate = re.sub(r"^ལ།\s*", "", candidate).strip()
    candidate = strip_ordinal(candidate)
    if len(candidate) >= 4:
        return candidate + ("།" if not candidate.endswith("།") else "")

    # Ultimate fallback — first 50 chars
    return text[:50].rstrip("་") + "།"


def count_overview_levels(text):
    """
    Count enumeration levels in a long overview entry.
    Returns 1 (single level — depth-2 children) or 2+ (depth-3 children needed).
    """
    # Each "ལ་N་སྟེ།/ལས།" chain = one additional nesting level
    level_markers = re.findall(
        r"ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)",
        text,
        re.UNICODE,
    )
    # "X གཉིས་ལས།" without preceding ལ་ also counts
    top_level = re.findall(r"(?<!ལ་)གཉིས་ལས།|(?<!ལ་)གསུམ་ལས།|(?<!ལ་)བཞི་ལས།", text, re.UNICODE)
    return len(level_markers) + (1 if top_level else 0)


def extract_intermediate_headings(text):
    """
    Extract the depth-2 (intermediate) headings implied by a 2-level overview.

    For an overview that says "A ལ་གསུམ་སྟེ། X། Y། Z།  དང་པོ་X ལ་གཉིས་སྟེ། ...",
    returns ["X", "Y", "Z"] — the items enumerated at the FIRST level of detail.
    """
    # Find the first "ལ་N་སྟེ།" block and split what follows on ། as items
    m = re.search(
        r"ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)\s*(.+?)(?:།།|།\s*།|དང་པོ་)",
        text,
        re.DOTALL | re.UNICODE,
    )
    if not m:
        return []
    items_text = m.group(1)
    raw_items = [x.strip() for x in items_text.split("།") if x.strip()]
    # Clean and filter short/meaningless items
    result = []
    for item in raw_items:
        item = strip_ordinal(item).rstrip("་").strip()
        if len(item) >= 5:
            result.append(item + ("།" if not item.endswith("།") else ""))
    return result


# ---------------------------------------------------------------------------
# TOC entry dataclass
# ---------------------------------------------------------------------------

class TocEntry:
    def __init__(self, depth, text, synthetic=False):
        self.depth = depth
        self.text = text
        self.synthetic = synthetic   # True if inferred from an overview, not a tagged entry
        self.toc_id = ""             # Filled in by renumber()

    def __repr__(self):
        flag = "*" if self.synthetic else " "
        return f"[{flag}d{self.depth}] {self.text[:60]}"


# ---------------------------------------------------------------------------
# Stub detection
# ---------------------------------------------------------------------------

_STUB_PAT = re.compile(
    r"^(?:ལ་?|ནི།|ལ།|དང་།|ཞེ་ན།|ལོ།|།།?)\s*$",
    re.UNICODE,
)

def is_stub(text):
    return bool(_STUB_PAT.match(text.strip()))


# ---------------------------------------------------------------------------
# Parse the existing TOC lines
# ---------------------------------------------------------------------------

def parse_toc_entries(toc_lines):
    """Read depth + text from existing * list lines."""
    entries = []
    for line in toc_lines:
        m = re.match(r"^( *)\* (.+?) \^toc-([\d\-]+)\s*$", line)
        if not m:
            continue
        indent = len(m.group(1))
        depth = indent // 3 + 1
        text = m.group(2).strip()
        entries.append(TocEntry(depth, text))
    return entries


# ---------------------------------------------------------------------------
# Restructure
# ---------------------------------------------------------------------------

LONG_THRESHOLD = 60  # chars — entries longer than this are overview entries

def restructure(entries):
    """
    Expand long overview entries, insert synthetic intermediate headings,
    promote leaf entries to depth 3 where needed, remove stubs.
    """
    result = []
    i = 0
    while i < len(entries):
        e = entries[i]
        text = e.text.strip()

        # 1. Remove stub entries
        if is_stub(text):
            i += 1
            continue

        # 2. Long depth-1 overview entry → compress + possibly add synthetics
        if e.depth == 1 and len(text) >= LONG_THRESHOLD:
            title = extract_section_title(text)
            levels = count_overview_levels(text)
            intermediates = extract_intermediate_headings(text) if levels >= 2 else []

            # Emit the compressed section heading
            result.append(TocEntry(1, title))

            if intermediates and levels >= 2:
                # Emit the FIRST intermediate heading (current focus)
                result.append(TocEntry(2, intermediates[0], synthetic=True))
                # The NEXT entries (depth 2 in current structure) become depth 3
                # They belong to this intermediate heading until we hit the next
                # depth-1 entry or another long overview
                i += 1
                collected = 0
                n_items = _count_leaf_items(text)
                while i < len(entries):
                    nxt = entries[i]
                    if nxt.depth == 1:
                        break  # Next section
                    if is_stub(nxt.text):
                        i += 1
                        continue
                    result.append(TocEntry(3, nxt.text))
                    i += 1
                    collected += 1
                    if collected >= n_items:
                        break
                # Emit remaining intermediate headings as depth-2 synthetic nodes
                for ih in intermediates[1:]:
                    result.append(TocEntry(2, ih, synthetic=True))
            else:
                i += 1
            continue

        # 3. Long depth-2 overview entry — compress to depth-2 heading
        if e.depth == 2 and len(text) >= LONG_THRESHOLD:
            title = extract_section_title(text)
            result.append(TocEntry(2, title))
            i += 1
            continue

        # 4. Normal entry — keep as-is, just clean up
        if not is_stub(text):
            result.append(TocEntry(e.depth, text))
        i += 1

    return result


def _count_leaf_items(overview_text):
    """Count the number of items at the deepest enumerated level."""
    # Find the last "ལ་N་སྟེ།" and extract N
    m = re.search(
        r"ལ་(གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་)(?:ལས།|སྟེ།)(?!.*ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་)(?:ལས།|སྟེ།))",
        overview_text,
        re.DOTALL | re.UNICODE,
    )
    if m:
        word = m.group(1).rstrip("་")
        return {"གཉིས": 2, "གསུམ": 3, "བཞི": 4, "ལྔ": 5, "དྲུག": 6, "བདུན": 7, "བརྒྱད": 8}.get(word, 3)
    return 3


# ---------------------------------------------------------------------------
# Renumber ^toc IDs
# ---------------------------------------------------------------------------

def renumber(entries):
    counters = {}
    for e in entries:
        d = e.depth
        # Reset deeper levels
        for k in list(counters.keys()):
            if k > d:
                del counters[k]
        counters[d] = counters.get(d, 0) + 1
        parts = [str(counters.get(i, 1)) for i in range(1, d + 1)]
        e.toc_id = "-".join(parts)


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render_toc(entries):
    lines = []
    for e in entries:
        indent = "   " * (e.depth - 1)
        lines.append(f"{indent}* {e.text} ^toc-{e.toc_id}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(toc_path, output_path=None):
    src = Path(toc_path).resolve()
    if not src.exists():
        print(f"ERROR: File not found: {src}", file=sys.stderr)
        return False

    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find the TOC block boundaries
    toc_heading_re = re.compile(r"^##\s*(དཀར་ཆག|Table of Contents)", re.IGNORECASE)
    toc_start = None
    toc_end = None
    for i, line in enumerate(lines):
        if toc_heading_re.match(line) and toc_start is None:
            toc_start = i
        elif toc_start is not None and line.startswith("---"):
            toc_end = i
            break

    if toc_start is None or toc_end is None:
        print("ERROR: Could not locate TOC block in file.", file=sys.stderr)
        return False

    toc_lines = lines[toc_start + 1 : toc_end]

    # Parse existing entries
    raw_entries = parse_toc_entries(toc_lines)
    print(f"Parsed {len(raw_entries)} TOC entries")

    # Restructure
    restructured = restructure(raw_entries)
    print(f"Restructured to {len(restructured)} entries")

    # Depth distribution
    from collections import Counter
    depth_dist = Counter(e.depth for e in restructured)
    print(f"Depth distribution: {dict(sorted(depth_dist.items()))}")
    synthetic_count = sum(1 for e in restructured if e.synthetic)
    print(f"Synthetic (inferred) headings: {synthetic_count}")

    # Renumber
    renumber(restructured)

    # Render new TOC
    new_toc = (
        "## དཀར་ཆག / Table of Contents\n\n"
        + render_toc(restructured)
        + "\n\n---"
    )

    # Replace TOC block in document
    new_lines = lines[:toc_start] + new_toc.splitlines() + lines[toc_end + 1:]
    new_text = "\n".join(new_lines)

    out = Path(output_path) if output_path else src.parent / f"restructured-{src.name}"
    out.write_text(new_text, encoding="utf-8")
    print(f"Output: {out}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python restructure_toc.py <toc_file.md> [output_file.md]")
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    sys.exit(0 if process_file(inp, out) else 1)
