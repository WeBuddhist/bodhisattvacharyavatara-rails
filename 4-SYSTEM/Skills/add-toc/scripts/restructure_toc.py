#!/usr/bin/env python3
"""
restructure_toc.py — Post-process a lekphi-format TOC to fix sa-bcad nesting.

Improvements over the flat 2-level output from add_toc.py Format D:
  1. Compresses long sa-bcad overview entries to a clean section title
  2. Inserts synthetic intermediate depth-2 headings when the overview
     describes two levels of hierarchy
  3. Promotes leaf entries to depth 3 accordingly
  4. Removes meaningless stub entries (bare ལ་, ནི།, etc.)
  5. Re-numbers all ^toc-X-Y-Z block IDs

Usage:  python restructure_toc.py <toc_file.md> [output_file.md]
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tibetan helpers
# ---------------------------------------------------------------------------

_ORDINAL_PAT = re.compile(
    r"^(?:དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ|དྲུག་པ|བདུན་པ|བརྒྱད་པ|དགུ་པ|བཅུ་པ)"
    r"[་།\s]*",
    re.UNICODE,
)
_BRACKET_PAT = re.compile(r"^[༡༢༣༤༥༦༧༨༩༠]༽\s*|^[ཀ-ཬ]༽\s*", re.UNICODE)


def strip_ordinal(text):
    t = _ORDINAL_PAT.sub("", text.strip())
    t = _BRACKET_PAT.sub("", t)
    return t.strip()


def ensure_shad(text):
    """Append shad if the text doesn't end with one."""
    t = text.strip().rstrip("་")
    if not t:
        return text
    return t + ("།" if not t.endswith("།") else "")


# ---------------------------------------------------------------------------
# Enumeration markers
# ---------------------------------------------------------------------------

# Matches count words followed by ལས།/སྟེ།/། (loose — catches "དང་གསུམ།" etc.)
_ENUM_RE = re.compile(
    r"(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་)"
    r"(?:ལས།|སྟེ།|དང་བཅས།|ལས་།|།)",
    re.UNICODE,
)

# Strict "X ལ་N་ལས/སྟེ།" — X has N parts
_LAL_ENUM_RE = re.compile(
    r"ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)",
    re.UNICODE,
)


# ---------------------------------------------------------------------------
# Title extraction from long overview entries
# ---------------------------------------------------------------------------

def extract_section_title(text):
    """
    Extract the outermost (depth-1) section title from a long sa-bcad overview.

    Strategy:
      1. Find first enumeration marker in the text.
         Everything before it is: "INTRO  ITEM1  དང་།  ITEM2  [count_word]"
         Split by "དང་།" — the second-to-last part before the split is ITEM1.
         Strip any leading preamble of the form "X ལ། " (structural particle).
      2. If no "དང་།" split available, look for "TITLE ལ།" at start — TITLE
         is the noun phrase before the "ལ།" structural particle.
      3. Fallback: text before the first natural shad ".།".
    """
    raw = text.strip()

    # --- Attempt 1: Split-by-དང་། before the first enumeration marker -----
    m = _ENUM_RE.search(raw)
    if m:
        before_enum = raw[:m.start()].strip()
        # Split on "དང་།" (conjunction + shad = list separator)
        # Note: we require "།" after "དང་" to avoid splitting inside words
        parts = re.split(r"དང་།", before_enum)
        if len(parts) >= 2:
            # Second-to-last part holds ITEM1
            candidate = parts[-2].strip()
            # Strip leading structural preamble "X ལ།  " where ལ། is a particle
            # IMPORTANT: only strip if "ལ།" is preceded by a meaningful phrase
            candidate = re.sub(r"^.+?(?<=[^ལ])ལ།\s*", "", candidate).strip()
            # Also strip lone "ལ།" at start if leftover
            candidate = re.sub(r"^ལ།\s*", "", candidate).strip()
            candidate = strip_ordinal(candidate).rstrip("་")
            if len(candidate) >= 4:
                return ensure_shad(candidate)
        else:
            # Only one part — look for "TITLE ལ།" in that part
            candidate = parts[0].strip()
            m2 = re.search(r"^([^།]+?)(?<=[^ལ])ལ།", candidate, re.UNICODE)
            if m2:
                candidate = strip_ordinal(m2.group(1).strip().rstrip("་"))
                if len(candidate) >= 4:
                    return ensure_shad(candidate)

    # --- Attempt 2: "TITLE ལ།" at the very beginning ----------------------
    # Matches: noun phrase (no internal shads) + ལ། structural particle
    m2 = re.search(r"^([^།]{4,}?)(?<![ལ])ལ།", raw, re.UNICODE)
    if m2:
        candidate = strip_ordinal(m2.group(1).strip().rstrip("་"))
        if len(candidate) >= 4:
            return ensure_shad(candidate)

    # --- Attempt 3: first "དང་པོ་TITLE ལ་N་སྟེ།" -------------------------
    m3 = re.search(
        r"དང་པོ་([^།]{4,}?)ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)",
        raw, re.UNICODE
    )
    if m3:
        candidate = strip_ordinal(m3.group(1).strip().rstrip("་"))
        if len(candidate) >= 4:
            return ensure_shad(candidate)

    # --- Fallback: text before first shad ----------------------------------
    parts_shad = raw.split("།")
    candidate = strip_ordinal(parts_shad[0].strip().rstrip("་"))
    if len(candidate) >= 4:
        return ensure_shad(candidate)

    return ensure_shad(raw[:60].rstrip("་།").strip())


def extract_active_heading(text):
    """
    Depth-2 active heading = last 'དང་པོ་TITLE ལ་N་སྟེ།' match.
    This is the sub-section currently being expanded in the overview.
    """
    hits = list(re.finditer(
        r"དང་པོ་([^།]{4,}?)ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)",
        text, re.UNICODE
    ))
    if hits:
        candidate = strip_ordinal(hits[-1].group(1).strip().rstrip("་"))
        if len(candidate) >= 4:
            return ensure_shad(candidate)
    return None


def extract_intermediate_headings(text):
    """
    The depth-2 sibling headings from the first 'ལ་N་སྟེ/ལས།' block.
    These are the items enumerated at the first level of detail.
    """
    # Find first "ལ་N་སྟེ།/ལས།" and take the items listed after it
    m = re.search(
        r"ལ་(?:གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་)(?:ལས།|སྟེ།)\s*(.+?)(?:།།|།\s*།|དང་པོ་)",
        text, re.DOTALL | re.UNICODE
    )
    if not m:
        return []
    raw_items = [x.strip() for x in m.group(1).split("།") if x.strip()]
    result = []
    for item in raw_items:
        item = strip_ordinal(item).rstrip("་").strip()
        if len(item) >= 5:
            result.append(ensure_shad(item))
    return result


def count_overview_levels(text):
    """Count nesting levels described by the overview (1 = single, 2+ = nested)."""
    lal = len(_LAL_ENUM_RE.findall(text))
    top = len(re.findall(r"(?<![་ལ])(?:གཉིས་ལས།|གསུམ་ལས།|བཞི་ལས།|ལྔ་ལས།)", text, re.UNICODE))
    return lal + (1 if top else 0)


def _count_leaf_items(text):
    """Number from the LAST enumeration marker in the overview."""
    hits = list(re.finditer(
        r"(གཉིས་|གསུམ་|བཞི་|ལྔ་|དྲུག་|བདུན་|བརྒྱད་)(?:ལས།|སྟེ།|།)",
        text, re.UNICODE
    ))
    if not hits:
        return 3
    return {
        "གཉིས": 2, "གསུམ": 3, "བཞི": 4,
        "ལྔ": 5, "དྲུག": 6, "བདུན": 7, "བརྒྱད": 8
    }.get(hits[-1].group(1).rstrip("་"), 3)


# ---------------------------------------------------------------------------
# Stub detection
# ---------------------------------------------------------------------------

_STUB_PAT = re.compile(
    r"^(?:ལ་?|ནི།|ལ།|དང་།|ཞེ་ན།|ལོ།|།།?|ངོ་བོ་ནི་?|་+)\s*$",
    re.UNICODE,
)


def is_stub(text):
    t = text.strip()
    return not t or bool(_STUB_PAT.match(t)) or (len(t) <= 5 and t.endswith("།") and len(t.replace("།", "").replace("་", "")) <= 2)


# ---------------------------------------------------------------------------
# TOC entry
# ---------------------------------------------------------------------------

class TocEntry:
    def __init__(self, depth, text, synthetic=False):
        self.depth = depth
        self.text = text
        self.synthetic = synthetic
        self.toc_id = ""


# ---------------------------------------------------------------------------
# Parse existing TOC entries from * list
# ---------------------------------------------------------------------------

def parse_toc_entries(lines):
    entries = []
    for line in lines:
        m = re.match(r"^( *)\* (.+?) \^toc-([\d\-]+)\s*$", line)
        if not m:
            continue
        indent = len(m.group(1))
        depth = indent // 3 + 1
        entries.append(TocEntry(depth, m.group(2).strip()))
    return entries


# ---------------------------------------------------------------------------
# Main restructure pass
# ---------------------------------------------------------------------------

LONG_THRESHOLD = 60


def restructure(entries):
    result = []
    i = 0
    while i < len(entries):
        e = entries[i]
        text = e.text.strip()

        # Drop stubs
        if is_stub(text):
            i += 1
            continue

        # Long depth-1 overview entry — compress + optional 3-level expansion
        if e.depth == 1 and len(text) >= LONG_THRESHOLD:
            outer = extract_section_title(text)
            levels = count_overview_levels(text)
            active = extract_active_heading(text) if levels >= 2 else None
            intermediates = extract_intermediate_headings(text) if (levels >= 2 and active) else []

            result.append(TocEntry(1, outer))

            if active:
                result.append(TocEntry(2, active, synthetic=True))
                # Consume next N leaf entries → depth 3
                i += 1
                n = _count_leaf_items(text)
                collected = 0
                while i < len(entries) and collected < n:
                    nxt = entries[i]
                    if nxt.depth == 1:
                        break
                    if is_stub(nxt.text):
                        i += 1
                        continue
                    result.append(TocEntry(3, nxt.text))
                    i += 1
                    collected += 1
                # Emit remaining intermediate headings (siblings of active)
                for ih in intermediates:
                    if ih != active:
                        result.append(TocEntry(2, ih, synthetic=True))
            else:
                i += 1
            continue

        # Long depth-2 entry — compress
        if e.depth == 2 and len(text) >= LONG_THRESHOLD:
            result.append(TocEntry(2, extract_section_title(text)))
            i += 1
            continue

        # Normal entry
        if not is_stub(text):
            result.append(TocEntry(e.depth, text))
        i += 1

    return result


# ---------------------------------------------------------------------------
# Renumber IDs
# ---------------------------------------------------------------------------

def renumber(entries):
    counters = {}
    for e in entries:
        d = e.depth
        for k in list(counters.keys()):
            if k > d:
                del counters[k]
        counters[d] = counters.get(d, 0) + 1
        e.toc_id = "-".join(str(counters.get(j, 1)) for j in range(1, d + 1))


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render_toc(entries):
    return "\n".join(
        "   " * (e.depth - 1) + "* " + e.text + " ^toc-" + e.toc_id
        for e in entries
    )


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

_TOC_HDR = re.compile(r"^##\s*(དཀར་ཆག|Table of Contents)", re.IGNORECASE)


def process_file(src_path, out_path=None):
    src = Path(src_path).resolve()
    if not src.exists():
        print(f"ERROR: {src}", file=sys.stderr); return False

    lines = src.read_text("utf-8").splitlines()
    toc_start = toc_end = None
    for i, line in enumerate(lines):
        if _TOC_HDR.match(line) and toc_start is None:
            toc_start = i
        elif toc_start is not None and line.startswith("---"):
            toc_end = i; break

    if toc_start is None or toc_end is None:
        print("ERROR: TOC block not found", file=sys.stderr); return False

    raw = parse_toc_entries(lines[toc_start + 1 : toc_end])
    print(f"Parsed {len(raw)} entries")
    restructured = restructure(raw)
    print(f"Restructured → {len(restructured)} entries")
    from collections import Counter
    dc = Counter(e.depth for e in restructured)
    print(f"Depths: {dict(sorted(dc.items()))}")
    print(f"Synthetic headings: {sum(1 for e in restructured if e.synthetic)}")
    renumber(restructured)

    new_toc_block = "## དཀར་ཆག / Table of Contents\n\n" + render_toc(restructured) + "\n\n---"
    new_lines = lines[:toc_start] + new_toc_block.splitlines() + lines[toc_end + 1:]
    out = Path(out_path) if out_path else src.parent / f"restructured-{src.name}"
    out.write_text("\n".join(new_lines), "utf-8")
    print(f"Output → {out}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python restructure_toc.py <toc_file.md> [output_file.md]")
        sys.exit(1)
    sys.exit(0 if process_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None) else 1)
