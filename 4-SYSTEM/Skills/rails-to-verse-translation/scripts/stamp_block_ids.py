#!/usr/bin/env python3
"""Stamp ^chapter-verse block IDs onto a verse-translation file (Step 9).

Attaches each ID to the END of the verse's final line, per CLAUDE.md §5 and the
convention in the Tibetan root. An ID separated from its verse by a blank line
becomes its own Obsidian block and silently breaks every ![[file#^id]] pointing
at it -- this script never produces that shape.

Normalises two marker irregularities found in real vault files:
  * a marker sharing a line with its first line of text  -> moved to its own line
  * an unbolded marker  (N)  -> **(N)**
Both are mechanical presentation fixes, not interpretive edits.

Run from the vault root.

    python3 stamp_block_ids.py --file <file> --numerals devanagari [--dry-run]

Exit status 0 = success, 1 = verification failed (file left unchanged).
"""
import argparse
import re
import shutil
import sys

NUMERALS = {
    "devanagari": "०१२३४५६७८९",
    "latin": "0123456789",
    "bengali": "০১২৩৪৫৬৭৮৯",
    "tibetan": "༠༡༢༣༤༥༦༧༨༩",
}
# chapter headings: any heading level, containing a numeral in the chosen system
CHAPTER_RE = r"^(#{1,6}\s+.*?[{d}]+.*?)\s*(?:\^(\d+)-0)?\s*$"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--numerals", default="devanagari", choices=sorted(NUMERALS))
    ap.add_argument("--chapter-word", default=None,
                    help="word marking a chapter heading, e.g. अध्याय. Default: infer.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    digits = NUMERALS[args.numerals]
    D = re.escape(digits)
    to_int = lambda s: int("".join(str(digits.index(c)) for c in s))

    original = open(args.file, encoding="utf-8").read()
    text = original

    # split frontmatter so we never rewrite inside it
    fm = ""
    if text.startswith("---"):
        end = text.index("\n---", 3) + len("\n---")
        fm, text = text[:end], text[end:]

    # normalise markers
    text, n_inline = re.subn(
        r"^(?:\*\*)?\([" + D + r"]+\)(?:\*\*)?[ \t]+(\S.*)$",
        lambda m: re.sub(r"[ \t]+\S.*$", "", m.group(0)).strip() + "\n" + m.group(1),
        text, flags=re.M)
    text, n_bold = re.subn(r"^\((["+D+r"]+)\)[ \t]*$", r"**(\1)**", text, flags=re.M)

    # infer the chapter-heading word if not given
    chapter_word = args.chapter_word
    if not chapter_word:
        for line in text.split("\n"):
            if re.match(r"^#{1,6}\s", line) and re.search(r"[" + D + r"]", line):
                toks = re.findall(r"[^\s#*:.,()\[\]]+", line)
                cand = [t for t in toks if not re.search(r"[" + D + r"]", t)]
                if cand:
                    chapter_word = cand[0]
                    break

    out, ch, pending = [], None, None

    def flush():
        """Append the pending ID to the last non-empty line already emitted."""
        nonlocal pending
        if pending is None:
            return
        for k in range(len(out) - 1, -1, -1):
            if out[k].strip():
                out[k] = re.sub(r"\s*\^\d+-\d+\s*$", "", out[k]).rstrip() + f" ^{pending[0]}-{pending[1]}"
                break
        pending = None

    for line in text.split("\n"):
        mh = None
        if chapter_word and re.match(r"^#{1,6}\s", line) and chapter_word in line:
            mnum = re.search(r"[" + D + r"]+", line)
            if mnum:
                mh = mnum.group(0)
        if mh:
            flush()
            ch = to_int(mh)
            base = re.sub(r"\s*\^\d+-0\s*$", "", line).rstrip()
            out.append(f"{base} ^{ch}-0")
            continue
        mv = re.match(r"^\*\*\(([" + D + r"]+)\)\*\*\s*$", line)
        if mv:
            flush()
            if ch is None:
                sys.exit("FAIL: verse marker encountered before any chapter heading; "
                         "pass --chapter-word explicitly")
            pending = (ch, to_int(mv.group(1)))
            out.append(line)
            continue
        out.append(re.sub(r"\s*\^\d+-\d+\s*$", "", line) if re.search(r"\^\d+-\d+\s*$", line) else line)
    flush()

    body = "\n".join(out)
    # exactly one blank line before every marker and heading
    body = re.sub(r"\n+(\*\*\([" + D + r"]+\)\*\*)", r"\n\n\1", body)
    body = re.sub(r"\n+(#{1,6}\s)", r"\n\n\1", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    result = (fm + "\n\n" + body.strip() + "\n") if fm else (body.strip() + "\n")

    # ---- verification, before writing ----
    ids = [(int(c), int(v)) for c, v in re.findall(r"\^(\d+)-(\d+)", result)]
    verse_ids = [x for x in ids if x[1] > 0]
    problems = []
    if re.search(r"^\^\d+-\d+\s*$", result, re.M):
        problems.append("an ID landed alone on a line (would break transclusion)")
    dupes = sorted({x for x in verse_ids if verse_ids.count(x) > 1})
    if dupes:
        problems.append(f"duplicate IDs: {dupes}")
    by_ch = {}
    for c, v in verse_ids:
        by_ch.setdefault(c, []).append(v)
    for c, vs in sorted(by_ch.items()):
        vs = sorted(vs)
        if vs != list(range(1, len(vs) + 1)):
            gaps = [n for n in range(1, max(vs) + 1) if n not in vs]
            problems.append(f"chapter {c} not contiguous from 1; missing {gaps}")
    def norm(s):
        s = re.sub(r"\^\d+-\d+", "", s)                       # added IDs
        s = re.sub(r"\*\*(\([" + D + r"]+\))\*\*", r"\1", s)  # marker bolding
        return re.sub(r"\s+", "", s)                          # whitespace/blank lines

    if norm(result) != norm(original):
        problems.append("verse text changed beyond added IDs and marker normalisation")

    print(f"numeral system      : {args.numerals}")
    print(f"chapter-heading word: {chapter_word!r}")
    print(f"markers normalised  : {n_inline} inline, {n_bold} unbolded")
    print(f"chapter IDs         : {[f'^{c}-0' for c, v in ids if v == 0]}")
    for c, vs in sorted(by_ch.items()):
        print(f"chapter {c}           : {len(vs)} verse IDs, 1..{max(vs)} contiguous={sorted(vs) == list(range(1, len(vs) + 1))}")
    print(f"IDs attached to a verse-final line: {len(verse_ids)}")

    if problems:
        print("\nFAILED -- file NOT written:")
        for p in problems:
            print("  " + p)
        return 1

    if args.dry_run:
        print("\ndry run: verification passed, nothing written")
        return 0

    shutil.copy(args.file, args.file + ".bak")
    open(args.file, "w", encoding="utf-8").write(result)
    print(f"\nwritten. backup at {args.file}.bak")
    return 0


if __name__ == "__main__":
    sys.exit(main())
