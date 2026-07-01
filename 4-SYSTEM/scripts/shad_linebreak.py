#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reflow Tibetan text by the shad (།), with Botok Unicode normalization.

Pipeline (applied to the body, never to a leading YAML frontmatter block):

  1. Unwrap wikilinks: ``[[target|display]]`` -> ``display`` (``[[|x]]`` -> ``x``,
     ``[[x]]`` -> ``x``). Brackets and target are stripped; the inner display
     text is kept and reflowed like ordinary text.
  2. Remove blockquote / ``>`` markers.
  3. Botok Unicode normalization (vendored ``normalize_unicode`` from
     OpenPecha/Botok ``botok/utils``): canonical decomposition, syllable
     reordering, rago fixes, deprecated-codepoint replacement.
  4. Collapse whitespace runs. A run containing a literal space/tab collapses
     to a single space, same as a blank-line run (2+ line breaks, a paragraph
     break) -- both are treated as an intentional separator. A run that is
     just a single hard line break (mid-paragraph text wrapping) collapses to
     *nothing*, since source files are often wrapped at a fixed width with no
     space at the wrap point (e.g. ``...འགྲེལ\nལས...`` -> ``...འགྲེལལས...``,
     ``...བྱ་\nབ...`` -> ``...བྱ་བ...``); treating it as a space would wrongly
     inject a space into the middle of a word/phrase.
  5. Insert a line break after every shad group (one or more ``།`` optionally
     separated by spaces: ``། `` / ``།།`` / ``། །`` / ``།། །།`` ...).
     Multi-shad groups are normalized to space-separated shads (``། །``).

Exceptions to the line break in step 5:

  * The opening header ``༄༅། །`` (any run of yig-mgo marks ༄ ༅ ༆ ༇ followed
    by a shad group) is kept and stays ATTACHED to the text that follows it.
  * A shad immediately followed by CLOSING emphasis (``*`` / ``**``, detected by
    parity so an *opening* run still breaks) stays attached, the span is closed,
    and the line break is placed AFTER the emphasis.
  * A shad immediately followed by a closing Tibetan/CJK bracket stays attached
    and keeps flowing; the next real shad supplies the break (e.g. ``།༽ནི།``).

Output:
  * ``status: 1-segmented`` is set in the YAML frontmatter (a minimal block is
    created if the source has none).
  * Results are written to ``<name>_segmented<ext>`` (originals untouched).

A leading YAML frontmatter block (``--- ... ---``) is otherwise preserved.

Usage:
    python shad_linebreak.py input.md                 # -> input_segmented.md
    python shad_linebreak.py input.md output.md       # explicit output path
    cat input.md | python shad_linebreak.py           # stdin -> stdout
    python shad_linebreak.py path/to/folder           # recurse -> *_segmented.md
    python shad_linebreak.py path/to/folder --ext .md .txt
    python shad_linebreak.py input.md --form nfc      # default form: nfd
"""
import argparse
import os
import re
import sys
from enum import Enum

# --------------------------------------------------------------------------- #
#  Botok Unicode normalization                                                #
#  Vendored from OpenPecha/Botok -> botok/utils/unicode_normalization.py      #
#  (Apache-2.0). Kept self-contained so this script has no dependency.        #
# --------------------------------------------------------------------------- #


class Cats(Enum):
    Other = 0
    Base = 1
    Subscript = 2
    BottomVowel = 3
    BottomMark = 4
    TopVowel = 5
    TopMark = 6
    RightMark = 7


CATEGORIES = (
    [Cats.Other]                 # 0F00
    + [Cats.Base]                # 0F01
    + [Cats.Other] * 22          # 0F02-0F17
    + [Cats.BottomVowel] * 2     # 0F18-0F19
    + [Cats.Other] * 6           # 0F1A-0F1F
    + [Cats.Base] * 20           # 0F20-0F33
    + [Cats.Other]               # 0F34
    + [Cats.BottomMark]          # 0F35
    + [Cats.Other]               # 0F36
    + [Cats.BottomMark]          # 0F37
    + [Cats.Other]               # 0F38
    + [Cats.Subscript]           # 0F39
    + [Cats.Other] * 4           # 0F3A-0F3D
    + [Cats.RightMark]           # 0F3E
    + [Cats.Other]               # 0F3F
    + [Cats.Base] * 45           # 0F40-0F6C
    + [Cats.Other] * 4           # 0F6D-0F70
    + [Cats.BottomVowel]         # 0F71
    + [Cats.TopVowel]            # 0F72
    + [Cats.TopVowel]            # 0F73
    + [Cats.BottomVowel] * 2     # 0F74-0F75
    + [Cats.TopVowel] * 8        # 0F76-0F7D
    + [Cats.TopMark]             # 0F7E
    + [Cats.RightMark]           # 0F7F
    + [Cats.TopVowel] * 2        # 0F80-0F81
    + [Cats.TopMark] * 2         # 0F82-0F83
    + [Cats.BottomMark]          # 0F84
    + [Cats.Other]               # 0F85
    + [Cats.TopMark] * 2         # 0F86-0F87
    + [Cats.Base] * 2            # 0F88-0F89
    + [Cats.Base]                # 0F8A
    + [Cats.Other]               # 0F8B
    + [Cats.Base]                # 0F8C
    + [Cats.Subscript] * 48      # 0F8D-0FBC
)


def charcat(c):
    """Return the category for a single-char string."""
    o = ord(c)
    if 0x0F00 <= o <= 0x0FBC:
        return CATEGORIES[o - 0x0F00]
    return Cats.Other


def unicode_reorder(txt):
    charcats = [charcat(c) for c in txt]
    i = 0
    res = []
    valid = True
    while i < len(charcats):
        c = charcats[i]
        if c != Cats.Base:
            if c.value > Cats.Base.value:
                valid = False
            res.append(txt[i])
            i += 1
            continue
        j = i + 1
        while j < len(charcats) and charcats[j].value > Cats.Base.value:
            j += 1
        newindices = sorted(range(i, j), key=lambda e: (charcats[e].value, e))
        res.append("".join(txt[m] for m in newindices))
        i = j
    return "".join(res), valid


def is_vowel(char):
    return bool(re.search(r"[ཱ-྄]", char))


def is_suffix(char):
    return bool(re.search(r"[ྐ-ྼ]", char))


def normalize_invalid_start_string(s):
    if len(s) < 2:
        return s
    if is_vowel(s[0]) and not is_vowel(s[1]) and not is_suffix(s[1]):
        return s[1] + s[0] + (s[2:] if len(s) > 2 else "")
    if is_suffix(s[0]):
        return s[1:]
    return s


def normalize_unicode(s, form="nfd"):
    # discouraged / deprecated codepoints
    s = s.replace("ཱི", "ཱི")
    s = s.replace("ཱུ", "ཱུ")
    s = s.replace("ཷ", "ྲཱྀ")
    s = s.replace("ཹ", "ླཱྀ")
    s = s.replace("ཱྀ", "ཱྀ")
    if form == "nfd":
        for a, b in (
            ("གྷ", "གྷ"), ("཈", "ཇྷ"),
            ("ཌྷ", "ཌྷ"), ("དྷ", "དྷ"),
            ("བྷ", "བྷ"), ("ཛྷ", "ཛྷ"),
            ("ཀྵ", "ཀྵ"), ("ྲྀ", "ྲྀ"),
            ("ླྀ", "ླྀ"), ("ྒྷ", "ྒྷ"),
            ("྘", "ྗྷ"), ("ྜྷ", "ྜྷ"),
            ("ྡྷ", "ྡྷ"), ("ྦྷ", "ྦྷ"),
            ("ྫྷ", "ྫྷ"), ("ྐྵ", "ྐྵ"),
        ):
            s = s.replace(a, b)
    else:  # nfc
        for a, b in (
            ("གྷ", "གྷ"), ("ཌྷ", "ཌྷ"),
            ("དྷ", "དྷ"), ("བྷ", "བྷ"),
            ("ཛྷ", "ཛྷ"), ("ཀྵ", "ཀྵ"),
            ("ྲྀ", "ྲྀ"), ("ླྀ", "ླྀ"),
            ("ྒྷ", "ྒྷ"), ("ྜྷ", "ྜྷ"),
            ("ྡྷ", "ྡྷ"), ("ྦྷ", "ྦྷ"),
            ("ྫྷ", "ྫྷ"), ("ྐྵ", "ྐྵ"),
        ):
            s = s.replace(a, b)
    s = s.replace("ༀ", "ཨོཾ")
    s, _valid = unicode_reorder(s)
    # rago: 0f6a -> 0f62 unless followed by certain subjoined letters
    s = re.sub(
        "ཪ(?![ྐ-ྗྚ-ྫྷྮྯྴ-ྼ])",
        "ར", s,
    )
    s = normalize_invalid_start_string(s)
    return s


# --------------------------------------------------------------------------- #
#  Reflow logic                                                               #
# --------------------------------------------------------------------------- #
SHAD = "།"                                  # ། primary shad (0F0D)
# Shad-family terminators that Botok classifies as NORMAL_PUNCT and that end a
# phrase/line: ། (0F0D) ༎ (0F0E nyis) ༏ (0F0F tsheg) ༐ (0F10 nyis-tsheg)
# ༑ (0F11 rin chen spungs) ༔ (0F14 gter tsheg) ༈ (0F08 sbrul). They are all
# treated like the ordinary shad for grouping and line-breaking, just as in
# Botok's chunker (where ༑ shares the NORMAL_PUNCT class with །).
SHAD_MARKS = "།༎༏༐༔༈"
HEAD = "༄༅༆༇"                # ༄ ༅ ༆ ༇  yig-mgo head marks

# Inherent closing punctuation a shad must stay attached to (no break).
# ༻ ༽ ) ] } ） 」 』 】 〕
BRACKET_CLOSERS = set("༻༽)]}）」』】〕")
EMPHASIS = set("*_")                             # handled by parity

# Ornamental shads to flatten to a plain shad (།) before reflowing. Botok does
# NOT do this (it keeps the codepoint), so it is an explicit choice here:
#   ༑ TIBETAN MARK RIN CHEN SPUNGS SHAD (0F11) -> །
ORNAMENTAL_SHAD_MAP = {"༑": "།"}

STATUS_VALUE = "1-segmented"     # written into the output frontmatter
SEGMENTED_SUFFIX = "_segmented"  # appended to the output filename

# Leading YAML frontmatter: --- then content then --- (or ...) on its own line.
FRONTMATTER = re.compile(
    r"\A(---\r?\n.*?\r?\n(?:---|\.\.\.)[ \t]*\r?\n?)", re.DOTALL
)

# Wikilink: [[ ... ]] (inner text may span lines, never contains ']').
WIKILINK = re.compile(r"\[\[([^\]]*)\]\]")


def split_frontmatter(text):
    """Return (frontmatter, body); frontmatter is '' if none present."""
    m = FRONTMATTER.match(text)
    if m:
        return m.group(1), text[m.end():]
    return "", text


def set_status(front, value):
    """Set/add `status: <value>` in the YAML frontmatter.

    If there is no frontmatter, a minimal one containing only the status is
    created. An existing `status:` line is replaced; otherwise the field is
    inserted just before the closing delimiter.
    """
    if not front:
        return f"---\nstatus: {value}\n---\n"
    lines = front.splitlines(keepends=True)
    for idx in range(1, len(lines)):
        if re.match(r"\s*status\s*:", lines[idx]):
            lines[idx] = f"status: {value}\n"
            return "".join(lines)
        if lines[idx].strip() in ("---", "..."):
            lines.insert(idx, f"status: {value}\n")
            return "".join(lines)
    return "".join(lines)


def segmented_name(path):
    """foo.md -> foo_segmented.md"""
    root, ext = os.path.splitext(path)
    return root + SEGMENTED_SUFFIX + ext


def unwrap_wikilinks(text):
    """[[target|display]] -> display ; [[x]] -> x ; [[|x]] -> x."""
    return WIKILINK.sub(lambda m: m.group(1).split("|")[-1], text)


def consume_shad_group(s, i):
    """s[i] is a shad. Return (end, raw_group) consuming `། (spaces །)*`."""
    j = i + 1
    while True:
        k = j
        while k < len(s) and s[k] == " ":
            k += 1
        if k < len(s) and s[k] in SHAD_MARKS:
            j = k + 1
        else:
            break
    return j, s[i:j]


def norm_group(group):
    """Normalize shad-group spacing.

    Preserve tight vs spaced shads instead of forcing a space between every
    shad: tight doubles/quads (`།།`, `།། །།`) keep NO space after the shad,
    while single and already-spaced shads (`།`, `། །`, `། ། ། །`) keep a single
    space. Runs of whitespace inside the group are collapsed to one space.
    """
    return re.sub(r"\s+", " ", group)


def insert_breaks(s):
    """Walk the collapsed one-line body, inserting breaks after shad groups."""
    res = []
    i, n = 0, len(s)
    emph_open = False  # parity of '*'/'_' emphasis runs

    while i < n:
        c = s[i]

        # --- yig-mgo header: keep + attach to following text, no break ----- #
        if c in HEAD:
            j = i
            while j < n and s[j] in HEAD:
                j += 1
            head = s[i:j]
            if j < n and s[j] in SHAD_MARKS:
                j, group = consume_shad_group(s, j)
                res.append(head + norm_group(group))
            else:
                res.append(head)
            i = j
            continue

        # --- shad group --------------------------------------------------- #
        if c in SHAD_MARKS:
            end, group = consume_shad_group(s, i)
            k = end
            while k < n and s[k] == " ":
                k += 1
            nx = s[k] if k < n else ""

            if nx in EMPHASIS and emph_open:
                # closing emphasis (**...།**): glue shad to the emphasis run,
                # close the span, THEN break after it.
                m = k
                while m < n and s[m] in EMPHASIS:
                    m += 1
                res.append(norm_group(group) + s[k:m] + "\n")
                emph_open = False
                i = m
            elif nx in BRACKET_CLOSERS:
                # inherent closer (།༽ནི།): glue, no break; next shad breaks.
                res.append(norm_group(group))
                i = k
            else:
                # single shad -> add a trailing space before the break;
                # multi-shad groups keep their preserved spacing as-is.
                marks = sum(ch in SHAD_MARKS for ch in group)
                tail = " \n" if marks == 1 else "\n"
                res.append(norm_group(group) + tail)
                i = end
            continue

        # --- emphasis runs: track parity, tighten delimiter spaces -------- #
        if c in EMPHASIS:
            j = i
            while j < n and s[j] == c:
                j += 1
            run = s[i:j]
            if emph_open:
                # this run CLOSES emphasis: drop any space right before it so the
                # markers sit flush against the emphasized text (** ...x **->...x**)
                while res and res[-1] == " ":
                    res.pop()
                res.append(run)
                emph_open = False
                i = j
            else:
                # this run OPENS emphasis: drop any space right after it so the
                # markers sit flush against the emphasized text (** x...->**x...).
                # This re-attaches an opener that a line break had stranded.
                res.append(run)
                emph_open = True
                i = j
                while i < n and s[i] == " ":
                    i += 1
            continue

        res.append(c)
        i += 1

    return "".join(res)


def collapse_whitespace(match):
    """Collapse one run of whitespace (see step 4 in the module docstring).

    * Contains a literal space/tab, or is a blank-line run (2+ line breaks):
      an intentional separator -> single space.
    * A lone hard line break (mid-paragraph wrap): no separator -> nothing.
    """
    run = match.group(0)
    if " " in run or "\t" in run or run.count("\n") >= 2:
        return " "
    return ""


def reflow(body, form="nfd"):
    body = unwrap_wikilinks(body)                   # 1. unwrap [[...]]
    body = re.sub(r"[ \t]*>+[ \t]?", "", body)      # 2. remove > markers
    body = normalize_unicode(body, form=form)       # 3. Botok normalization
    for _orn, _plain in ORNAMENTAL_SHAD_MAP.items():  # 3b. flatten ༑ -> །
        body = body.replace(_orn, _plain)
    body = re.sub(r"\s+", collapse_whitespace, body).strip()  # 4. collapse ws
    if not body:
        return ""
    out = insert_breaks(body)                       # 5. break after shad groups
    out = re.sub(r"\n[ \t]+", "\n", out)            # strip leading spaces per line
    out = re.sub(r"\n{2,}", "\n", out)              # collapse blank lines
    out = out.strip("\n")                            # keep single-shad trailing space
    return out + "\n"


def process_text(text, form="nfd", status=STATUS_VALUE):
    front, body = split_frontmatter(text)           # YAML frontmatter preserved
    front = set_status(front, status)               # status: 1-segmented
    return front + reflow(body, form=form)


def process_folder(folder, exts, form="nfd"):
    """Recurse folder, writing each `foo.md` to `foo_segmented.md`.

    Originals are left untouched; files already ending in `_segmented` are
    skipped so re-runs don't pile up suffixes.
    """
    exts = tuple(e.lower() for e in exts)
    count = 0
    for dirpath, _dirs, files in os.walk(folder):
        for name in sorted(files):
            root, ext = os.path.splitext(name)
            if ext.lower() not in exts or root.endswith(SEGMENTED_SUFFIX):
                continue
            path = os.path.join(dirpath, name)
            out_path = os.path.join(dirpath, root + SEGMENTED_SUFFIX + ext)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(process_text(text, form=form))
            print(os.path.relpath(out_path, folder))
            count += 1
    return count


def main():
    p = argparse.ArgumentParser(
        description="Reflow Tibetan text by the shad with Botok normalization."
    )
    p.add_argument("input", nargs="?", help="input file or folder (stdin if omitted)")
    p.add_argument("output", nargs="?", help="output file (single-file mode only)")
    p.add_argument("--ext", nargs="+", default=[".md"],
                   help="folder mode: extensions to process (default: .md)")
    p.add_argument("--form", choices=["nfd", "nfc"], default="nfd",
                   help="Botok normalization form (default: nfd)")
    args = p.parse_args()

    if args.input and os.path.isdir(args.input):
        n = process_folder(args.input, args.ext, form=args.form)
        print(f"\n{n} file(s) processed -> *{SEGMENTED_SUFFIX}.", file=sys.stderr)
        return

    # stdin -> stdout
    if not args.input:
        sys.stdout.write(process_text(sys.stdin.read(), form=args.form))
        return

    # single file -> <name>_segmented<ext> (or an explicit output path)
    with open(args.input, encoding="utf-8") as f:
        text = f.read()
    result = process_text(text, form=args.form)
    out_path = args.output or segmented_name(args.input)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(out_path, file=sys.stderr)


if __name__ == "__main__":
    main()
