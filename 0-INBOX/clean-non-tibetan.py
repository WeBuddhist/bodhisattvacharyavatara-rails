#!/usr/bin/env python3
"""
clean-non-tibetan.py

Removes all non-Tibetan script from a commentary file:
  - page-number lines (e.g. "-486-")
  - garbled OCR running-header lines (legacy-font Wylie, e.g. "hGÝ-q-ÁïÅ-...")
  - any stray non-Tibetan characters (Latin letters, brackets < > [ ], etc.)

Rule: keep only characters in the Tibetan Unicode block (U+0F00–U+0FFF)
plus spaces/tabs. Any line that has NO Tibetan character left after
filtering is dropped entirely (this catches page numbers and OCR headers).
Blank lines are preserved; runs of 2+ blank lines are collapsed to one.

The ORIGINAL file is never modified. Output is written to a new file
with a ".cleaned.md" suffix next to the source, so you can review and
diff before replacing.

Usage:
    python clean-non-tibetan.py "<path-to-file.md>"

If no path is given, it defaults to the rgyal-ba-rin-po-che commentary.
"""

import sys
import os
import re

DEFAULT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "1-SOURCES", "Commentaries", "bo-རྒྱལ་བ་རིན་པོ་ཆེ།.md",
)


def is_tibetan(ch: str) -> bool:
    return "ༀ" <= ch <= "࿿"


def keep(ch: str) -> bool:
    # keep Tibetan block characters and plain horizontal whitespace
    return is_tibetan(ch) or ch in " \t"


def clean(src: str) -> tuple[str, dict]:
    out_lines = []
    stats = {"lines_dropped": 0, "lines_kept": 0, "chars_removed": 0}

    for line in src.split("\n"):
        # filter to Tibetan + whitespace only
        filtered = "".join(c for c in line if keep(c))
        stats["chars_removed"] += len(line) - len(filtered)

        # collapse runs of spaces, trim trailing whitespace
        filtered = re.sub(r"[ \t]{2,}", " ", filtered).rstrip()

        if line.strip() and not any(is_tibetan(c) for c in filtered):
            # the original line had content but nothing Tibetan survived
            # -> it was a page number or an OCR header -> drop it
            stats["lines_dropped"] += 1
            continue

        out_lines.append(filtered)
        if filtered.strip():
            stats["lines_kept"] += 1

    text = "\n".join(out_lines)
    # collapse 3+ newlines (i.e. 2+ blank lines) down to a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n", stats


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        sys.exit(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        src = f.read()

    cleaned, stats = clean(src)

    base, ext = os.path.splitext(path)
    out_path = base + ".cleaned" + ext
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("Done.")
    print(f"  source : {path}")
    print(f"  output : {out_path}")
    print(f"  lines dropped (page numbers + OCR headers): {stats['lines_dropped']}")
    print(f"  non-Tibetan characters removed            : {stats['chars_removed']}")
    print(f"  content lines kept                        : {stats['lines_kept']}")
    print("\nReview the .cleaned.md file, and if it looks right, replace the original.")


if __name__ == "__main__":
    main()
