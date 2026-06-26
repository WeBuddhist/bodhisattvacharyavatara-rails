#!/usr/bin/env python3
"""
Format a verse-paragraph translation file into stanza (one-clause-per-line) form.

Each verse paragraph ends with a marker like  ^1-1 . The verse text is broken so
that every clause (after a comma / period / semicolon / colon) sits on its own
line, with the ^x-x marker kept on the final line.

Non-verse lines (YAML frontmatter, blank lines, and # headings) are left as-is.

Usage:
    python format_stanzas.py input.md [output.md]

If no output path is given, writes <input>.stanzas.md next to the input.
"""

import re
import sys
from pathlib import Path

# A verse line ends with a marker such as  ^1-1  ^I-0  ^10-58
MARKER_RE = re.compile(r"\s*(\^[^\s]+)\s*$")
# Split AFTER sentence/clause punctuation followed by whitespace.
SPLIT_RE = re.compile(r"(?<=[,;:.!?])\s+")


def format_verse(text: str, marker: str) -> str:
    """Break one verse into clause-per-line stanza form, marker on last line."""
    parts = [p.strip() for p in SPLIT_RE.split(text.strip()) if p.strip()]
    if not parts:
        return f"{text.strip()} {marker}".strip()
    # Keep a trailing space after each non-final line (matches the sample style).
    lines = [p + " " for p in parts[:-1]]
    lines.append(f"{parts[-1]} {marker}")
    return "\n".join(lines)


def process(src: Path, dst: Path) -> None:
    lines = src.read_text(encoding="utf-8").splitlines()
    out = []
    in_frontmatter = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track YAML frontmatter delimited by --- at the top of the file.
        if stripped == "---" and (i == 0 or in_frontmatter):
            in_frontmatter = not in_frontmatter
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            continue

        # Leave blank lines and headings untouched.
        if not stripped or stripped.startswith("#"):
            out.append(line)
            continue

        m = MARKER_RE.search(line)
        if m:
            marker = m.group(1)
            text = line[: m.start()]
            out.append(format_verse(text, marker))
        else:
            out.append(line)

    dst.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {dst}")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python format_stanzas.py input.md [output.md]")
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".stanzas.md")
    process(src, dst)


if __name__ == "__main__":
    main()
