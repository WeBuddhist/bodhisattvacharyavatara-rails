"""
apply.py — helper script for the add-block-id skill.

Two modes
---------
audit   python apply.py audit <file.md>
            Reads the file and prints a structured report:
            - heading structure (existing IDs and gaps)
            - every block that has no ID, with chapter context and content
            - verse count per chapter vs. Sanskrit expected
            - other issues (null bytes, multiple blanks, spacing)
            Used by the LLM to identify zones before making changes.

apply   python apply.py apply <file.md>
            Applies all mechanical changes the script can do without LLM judgment:
            - null bytes removed
            - whitespace-only lines collapsed to blank, 3+ blanks → 1
            - trailing spaces stripped
            - ^0 added to # book title
            - ^I-0 added to ## 0. Introduction
            - ^N-0 added to ## N. chapter headings
            - ^0-N legacy IDs fixed to ^I-N
            - colophon lines detected by pattern or position tagged ^N-a
            - verse lines with ordinal prefix "N. text" tagged ^C-N and prefix stripped
            - bare ordinal "N." lines tagged ^C-N
            - ^a ^b … added to book back-matter blocks (after ^10-a)
            - blank line inserted after each single-line verse block if missing
            - multiple spaces before ^ normalised to one
            Prints audit report afterwards so LLM can see what remains.

What the script cannot do (requires LLM judgment after apply):
            - zone classification for ambiguous blocks
            - interpolated verses ^C-Vx1
            - multi-line stanzas (ID goes on last line only)
            - chapter intros ^N-I
            - colophons not detectable by pattern or position
            - structural anomalies unique to a file
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Colophon detection — pattern-based + position-based, no hardcoded text
# ---------------------------------------------------------------------------
# Script-closing characters that end a colophon line.
# Chinese: 竟 (jìng, "finished") and 终 (zhōng, "end").
# Add patterns for other scripts here as new languages are added.
_COLOPHON_CLOSING = re.compile(r'[竟终]\s*$')


def _colophon_positions(lines: list) -> set:
    """
    Pre-scan: return line indices of the last non-blank, non-heading, no-ID
    content line immediately before each ## N. chapter heading.
    These are positional colophon candidates.
    """
    positions = set()
    for i, line in enumerate(lines):
        if re.match(r'^## \d+\.', line):
            j = i - 1
            while j >= 0 and lines[j].strip() == "":
                j -= 1
            if (j >= 0
                    and not re.match(r'^#+\s', lines[j])
                    and not re.search(r'\^[\w-]+', lines[j])):
                positions.add(j)
    return positions


def _is_colophon(text: str, line_idx: int, positions: set) -> bool:
    """
    True if this line is a chapter colophon.
    Two signals — either is sufficient:
    1. Pattern: ends with a known closing character (竟, 终, …)
    2. Position: last content line before the next chapter heading
                 AND not an ordinal-prefixed verse (those have their own rule)
    """
    if _COLOPHON_CLOSING.search(text):
        return True
    if line_idx in positions and not re.match(r'^\d+\.', text.strip()):
        return True
    return False


SK_VERSE_COUNTS = {1: 36, 2: 65, 3: 33, 4: 48, 5: 109, 6: 134, 7: 75, 8: 185, 9: 167, 10: 58}

BM_LETTERS = list("abcdefghijklmnopqrstuvwxyz")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def has_id(line: str) -> bool:
    return bool(re.search(r"\^[\w-]+", line))

def is_heading(line: str) -> bool:
    return bool(re.match(r"^#+\s", line))

def is_blank(line: str) -> bool:
    return line.strip() == ""

def read_file(path: Path):
    content = path.read_bytes().replace(b"\x00", b"").decode("utf-8")
    return content.split("\n")


# ---------------------------------------------------------------------------
# AUDIT
# ---------------------------------------------------------------------------

def cmd_audit(path: Path):
    lines = read_file(path)
    in_yaml = True
    current_ch = 0
    issues = []
    blocks_no_id = []
    block = []
    block_start = 0
    null_bytes = b"\x00" in path.read_bytes()

    if null_bytes:
        issues.append("NULL BYTES present — will be stripped by apply")

    # Count multiple-blank sequences
    multi_blank = 0
    prev_blank = False
    for l in lines:
        if is_blank(l):
            if prev_blank:
                multi_blank += 1
            prev_blank = True
        else:
            prev_blank = False
    if multi_blank:
        issues.append(f"Multiple consecutive blank lines: {multi_blank} sequences")

    # Spacing before ^
    bad_spacing = sum(1 for l in lines if re.search(r" {2,}\^", l))
    if bad_spacing:
        issues.append(f"Lines with 2+ spaces before ^: {bad_spacing}")

    print(f"=== AUDIT: {path.name} ({len(lines)} lines) ===\n")

    # Heading structure
    print("--- Heading structure ---")
    for i, l in enumerate(lines, 1):
        if re.match(r"^#+\s", l):
            tag = re.search(r"\^([\w-]+)", l)
            flag = ""
            if re.match(r"^# ", l) and not tag:
                flag = "  ← missing ^0"
            elif re.match(r"^## 0\.", l) and not tag:
                flag = "  ← missing ^I-0"
            elif re.match(r"^## \d+\.", l):
                m = re.match(r"^## (\d+)\.", l)
                n = int(m.group(1)) if m else 0
                if not re.search(rf"\^{n}-0\b", l):
                    flag = f"  ← missing ^{n}-0"
            print(f"  L{i}: {l.rstrip()}{flag}")
    print()

    # Pre-scan colophon positions for audit classification
    col_positions = _colophon_positions(lines)

    # Blocks without IDs
    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_yaml:
            if i > 0 and stripped == "---":
                in_yaml = False
            continue
        m_ch = re.match(r"^## (\d+)\.", line)
        if m_ch:
            current_ch = int(m_ch.group(1))
        if is_blank(line):
            if block:
                last = block[-1]
                if not has_id(last) and not is_heading(last):
                    blocks_no_id.append((block_start + 1, current_ch, list(block), block_start + len(block) - 1))
                block = []
        else:
            if not block:
                block_start = i
            block.append(line.rstrip())
    if block:
        last = block[-1]
        if not has_id(last) and not is_heading(last):
            blocks_no_id.append((block_start + 1, current_ch, list(block), block_start + len(block) - 1))

    print(f"--- Blocks without IDs: {len(blocks_no_id)} ---")
    for start, ch, blk, last_idx in blocks_no_id:
        text = blk[-1]
        auto = ""
        if _is_colophon(text, last_idx, col_positions):
            auto = f"  [auto → ^{ch}-a (colophon)]"
        elif re.match(r"^\d+\.\s+\S", text):
            m = re.match(r"^(\d+)\.", text)
            auto = f"  [auto → ^{ch}-{m.group(1)}]" if m else ""
        elif re.match(r"^\d+\.\s*$", text):
            m = re.match(r"^(\d+)\.", text)
            auto = f"  [auto → ^{ch}-{m.group(1)} (empty)]" if m else ""
        else:
            auto = "  [needs LLM judgment]"
        print(f"  L{start} Ch{ch}: {text[:80]}{auto}")
    print()

    # Verse counts
    print("--- Verse counts ---")
    max_v: dict = {}
    for l in lines:
        m = re.search(r"\^(\d+)-(\d+)\b", l)
        if m:
            c, v = int(m.group(1)), int(m.group(2))
            max_v[c] = max(max_v.get(c, 0), v)
    for c in range(0, 11):
        if c in max_v:
            got = max_v[c]
            exp = SK_VERSE_COUNTS.get(c, "")
            flag = "✓" if got == exp else f"  ← expected {exp}" if exp else ""
            print(f"  Ch{c}: {got}{flag}")
    print()

    # Other issues
    if issues:
        print("--- Other issues ---")
        for iss in issues:
            print(f"  {iss}")
        print()

    needs_llm = [b for b in blocks_no_id
                 if not _is_colophon(b[2][-1], b[3], col_positions)
                 and not re.match(r"^\d+\.\s*", b[2][-1])]
    if needs_llm:
        print(f">>> {len(needs_llm)} block(s) need LLM zone identification before apply.")
    else:
        print(">>> All untagged blocks can be handled automatically. Run: apply")


# ---------------------------------------------------------------------------
# APPLY
# ---------------------------------------------------------------------------

def cmd_apply(path: Path):
    lines = read_file(path)
    result = []
    in_yaml = True
    yaml_done = False

    # Pass 1: heading IDs, ^0-N → ^I-N
    for i, line in enumerate(lines):
        if in_yaml:
            if i == 0 and line.strip() == "---":
                result.append(line); continue
            if i > 0 and line.strip() == "---" and not yaml_done:
                in_yaml = False; yaml_done = True
                result.append(line); continue
            result.append(line); continue

        # Book title ^0
        if re.match(r"^# \S", line) and not has_id(line) and not re.match(r"^##", line):
            result.append(line.rstrip() + " ^0"); continue

        # Front matter heading
        if re.match(r"^## 0\.", line) and not has_id(line):
            result.append(line.rstrip() + " ^I-0"); continue

        # Chapter headings
        m_ch = re.match(r"^(## (\d+)\. .+?)(\s+\^[\w-]+)?\s*$", line)
        if m_ch:
            n = int(m_ch.group(2))
            heading = m_ch.group(1).rstrip()
            if not re.search(rf"\^{n}-0\b", line):
                result.append(f"{heading} ^{n}-0"); continue

        # Fix ^0-N → ^I-N
        if re.search(r"\^0-\d+\b", line):
            line = re.sub(r"\^0-(\d+)\b", r"^I-\1", line)

        result.append(line)

    lines = result

    # Pre-scan colophon positions on the post-pass-1 lines
    col_positions = _colophon_positions(lines)

    # Pass 2: colophon IDs, verse IDs, back matter
    result2 = []
    in_yaml2 = True
    yaml_done2 = False
    current_ch = 0
    past_10a = False
    bm_idx = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_yaml2:
            if stripped == "---" and result2:
                in_yaml2 = False; yaml_done2 = True
            result2.append(line); continue

        m_ch = re.match(r"^## (\d+)\.", line)
        if m_ch:
            current_ch = int(m_ch.group(1))
            past_10a = False

        if has_id(line) or is_heading(line) or is_blank(line):
            if re.search(r"\^10-a\b", line):
                past_10a = True
            result2.append(line); continue

        if past_10a:
            if bm_idx < len(BM_LETTERS):
                result2.append(f"{stripped} ^{BM_LETTERS[bm_idx]}")
                bm_idx += 1
            else:
                result2.append(line)
            continue

        # Colophon (pattern or position)
        if current_ch > 0 and _is_colophon(stripped, i, col_positions):
            cid = f"^{current_ch}-a"
            result2.append(f"{stripped} {cid}")
            if cid == "^10-a":
                past_10a = True
            continue

        # Verse with ordinal
        m = re.match(r"^(\d+)\.\s+(.+)", stripped)
        if m and current_ch > 0:
            result2.append(f"{m.group(2).rstrip()} ^{current_ch}-{m.group(1)}"); continue

        # Bare ordinal
        m2 = re.match(r"^(\d+)\.\s*$", stripped)
        if m2 and current_ch > 0:
            result2.append(f"^{current_ch}-{m2.group(1)}"); continue

        result2.append(line)

    lines = result2

    # Pass 3: strip ordinal prefixes from lines that now have IDs
    lines = [
        re.sub(r"^\d+\.\s+", "", l) if has_id(l) and re.match(r"^\d+\.\s+", l) else l
        for l in lines
    ]

    # Pass 4: blank line after each single-line verse block
    result4 = []
    for i, line in enumerate(lines):
        result4.append(line)
        if re.search(r"\^\d+-\d+x?\d*\s*$", line.rstrip()):
            if i + 1 < len(lines) and not is_blank(lines[i + 1]):
                result4.append("")
    lines = result4

    # Pass 5: cleanup
    text = "\n".join(lines)
    text = re.sub(r" {2,}(\^)", r" \1", text)
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)

    path.write_text(text, encoding="utf-8")
    print(f"Applied mechanical changes to {path.name}")
    print()

    # Post-apply audit
    cmd_audit(path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python apply.py audit <file.md>   — report structure, flag issues")
        print("  python apply.py apply <file.md>   — apply mechanical changes")
        sys.exit(1)

    mode = sys.argv[1]
    p = Path(sys.argv[2])
    if not p.exists():
        print(f"File not found: {p}")
        sys.exit(1)

    if mode == "audit":
        cmd_audit(p)
    elif mode == "apply":
        cmd_apply(p)
    else:
        print(f"Unknown mode: {mode}. Use 'audit' or 'apply'.")
        sys.exit(1)
