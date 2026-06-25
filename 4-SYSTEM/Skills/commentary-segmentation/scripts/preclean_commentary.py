#!/usr/bin/env python3
"""Stage-0 pre-clean for Tibetan commentary segmentation.

Removes editorial scaffolding from a Tibetan commentary, producing continuous
prose suitable for Stage-1 (segment_commentary.py) boundary detection.

Passes (all run before the no-loss snapshot, in order):
  1. git conflict markers  -- 7+ consecutive <, =, or > at line start
  2. blockquote prefixes   -- leading > chars (1-6); text content kept
  3. bare heading lines    -- lines that are only # chars; dropped entirely
  4. # characters          -- all # removed; heading text becomes prose
  5. Latin letters         -- a-z, A-Z removed (OCR artefacts)
  6. ASCII digit runs      -- 0-9 removed (incl. fused noise like "lo16")
  7. Obsidian block IDs    -- ^N-N patterns
  8. standalone numbers    -- whitespace-bounded digits (ASCII + Tibetan)
  9. line reflow           -- consecutive content lines joined into prose runs

Frontmatter (--- block) is preserved verbatim and excluded from no-loss check.

Usage:
    python3 preclean_commentary.py INPUT.md OUTPUT.md [--report R.tsv] [--dry-run]
"""
from __future__ import annotations
import argparse, re, sys, unicodedata
from pathlib import Path

TSHEG     = "་"   # Tibetan mark intersyllabic tsheg
SHAD      = "།"   # Tibetan mark shad
NYIS_SHAD = "༎"   # Tibetan mark nyis shad
HONOR     = "༄༅"  # Tibetan honorific mark (text/section opener)

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BLOCK_ID_RE    = re.compile(r"\s*\^[A-Za-z0-9_-]+")
HEADING_RE     = re.compile(r"^\s*#{1,6}\s*(.*)$")
SUSPECT_HEADING_TEXT_RE = re.compile(r"^[0-9༠-༩]+[.)]?$")
BARE_NUM_RE    = re.compile(r"(?<!\S)[0-9༠-༩]+(?:\.[0-9༠-༩]+)*[.)]?(?!\S)")

GIT_MARKER_RE  = re.compile(r"^(?:<{7,}|={7,}|>{7,}).*$", re.MULTILINE)
BLOCKQUOTE_RE  = re.compile(r"^>{1,6} ?",               re.MULTILINE)
BARE_HEADING_RE= re.compile(r"^#{1,6}\s*$",             re.MULTILINE)
HASH_RE        = re.compile(r"#+")
LATIN_RE       = re.compile(r"[a-zA-Z]+")
ASCII_DIGIT_RE = re.compile(r"[0-9]+")
REPLACEMENT_RE = re.compile("\ufffd+")

SEP = "\n\n"


def count_syllables(text):
    return text.count(TSHEG) + (1 if text.strip() else 0)

def squeeze(s):
    return re.sub(r"\s+", "", s)

def strip_frontmatter(text):
    return FRONTMATTER_RE.sub("", text, count=1)

def strip_numbers(body):
    matches = list(BARE_NUM_RE.finditer(body))
    out, last = [], 0
    for m in matches:
        out.append(body[last:m.start()])
        last = m.end()
    out.append(body[last:])
    return "".join(out), len(matches), []


def process(text):
    fm = FRONTMATTER_RE.match(text)
    if fm:
        head = fm.group(0).rstrip("\n")
        body = text[fm.end():]
    else:
        head = None
        body = text

    # 1. Git conflict markers
    n_git    = len(GIT_MARKER_RE.findall(body)); body = GIT_MARKER_RE.sub("", body)
    # 2. Blockquote prefixes
    n_bq     = len(BLOCKQUOTE_RE.findall(body)); body = BLOCKQUOTE_RE.sub("", body)
    # 3. Bare heading lines (count before # strip)
    n_bare   = len(BARE_HEADING_RE.findall(body)); body = BARE_HEADING_RE.sub("", body)
    # 4. All # characters
    n_hash   = len(HASH_RE.findall(body)); body = HASH_RE.sub("", body)
    # 5. Latin letters
    n_latin  = len(LATIN_RE.findall(body)); body = LATIN_RE.sub("", body)
    # 6. ASCII digit runs (incl. fused noise)
    n_digits = len(ASCII_DIGIT_RE.findall(body)); body = ASCII_DIGIT_RE.sub("", body)
    # 6b. Unicode replacement character U+FFFD (encoding artefacts)
    n_repl   = len(REPLACEMENT_RE.findall(body)); body = REPLACEMENT_RE.sub("", body)
    # 7. Obsidian block IDs
    n_ids    = len(BLOCK_ID_RE.findall(body)); body = BLOCK_ID_RE.sub("", body)
    # 8. Standalone numbers (Tibetan digits + any remaining)
    body, n_nums, _ = strip_numbers(body)

    expected_body = body   # no-loss snapshot -- taken after all char removal

    blocks, buf = [], []
    stats = dict(git_markers=n_git, blockquotes=n_bq, bare_headings=n_bare,
                 hashes=n_hash, latin=n_latin, ascii_digits=n_digits,
                 replacement_chars=n_repl,
                 block_ids=n_ids, numbers=n_nums,
                 headings=0, suspect_headings=0)

    def flush():
        if buf:
            run = re.sub(r"\s+", " ", " ".join(s.strip() for s in buf)).strip()
            # Remove spurious spaces after tsheg (line-break artefacts)
            run = re.sub(TSHEG + r" +", TSHEG, run)
            # Remove spurious space after honorific mark (༄༅། །) before text
            run = re.sub(r"(" + HONOR + SHAD + r"\s" + SHAD + r")\s+(?=[ཀ-ྼ])",
                         r"\1", run)
            # Split at double-shad (། །) sentence boundaries not part of the
            # honorific mark: (?<!༅) ensures we don't split the prefix.
            run = re.sub(r"(?<!༅)(" + SHAD + r"\s" + SHAD + r")\s+(?=[ཀ-ྼ])",
                         lambda m: m.group(1) + "\n\n", run)
            # Split before honorific marks appearing mid-run.
            run = re.sub(r"\s+(?=" + HONOR + r")", "\n\n", run)
            for part in (p.strip() for p in run.split("\n\n")):
                if part:
                    blocks.append(("prose", part))
            buf.clear()

    for ln in body.split("\n"):
        m = HEADING_RE.match(ln)   # will not match after step 4 removes all #
        if m:
            flush()
            htext = ln.strip()
            if htext:
                if SUSPECT_HEADING_TEXT_RE.match(m.group(1).strip()):
                    blocks.append(("heading-suspect", htext))
                    stats["suspect_headings"] += 1
                else:
                    blocks.append(("heading", htext))
                stats["headings"] += 1
            continue
        if ln.strip():
            buf.append(ln)
        else:
            flush()  # blank line = paragraph separator
    flush()

    # Merge standalone honorific-mark blocks (bare "༄༅། །" with no Tibetan
    # content after it) into the following prose block -- the mark is a prefix.
    merged, i = [], 0
    while i < len(blocks):
        kind, text = blocks[i]
        if (kind == "prose"
                and text.startswith(HONOR)
                and not re.search(r"[ཀ-ྼ]", text[len(HONOR):])):
            if i + 1 < len(blocks) and blocks[i + 1][0] == "prose":
                merged.append(("prose", text + blocks[i + 1][1]))
                i += 2
                continue
        merged.append(blocks[i])
        i += 1
    blocks[:] = merged

    out = []
    if head:
        out.append(head)
    out.extend(b[1] for b in blocks)
    return SEP.join(out) + "\n", blocks, stats, expected_body


def assert_no_loss(expected_body, cleaned):
    if squeeze(expected_body) != squeeze(strip_frontmatter(cleaned)):
        sys.exit("ABORT: pre-clean altered body text. No file written.")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--report"); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv[1:])

    text = unicodedata.normalize("NFC", Path(a.input).read_text(encoding="utf-8", errors="replace"))
    cleaned, blocks, stats, expected_body = process(text)
    assert_no_loss(expected_body, cleaned)

    print("{}: removed {} git markers, {} blockquote prefixes, {} bare headings, "
          "{} hashes, {} latin letters, {} ASCII digits, {} replacement chars, "
          "{} numbers, {} block IDs; emitted {} blocks.".format(
              a.input, stats["git_markers"], stats["blockquotes"],
              stats["bare_headings"], stats["hashes"], stats["latin"],
              stats["ascii_digits"], stats["replacement_chars"],
              stats["numbers"], stats["block_ids"], len(blocks)))

    if a.report:
        with Path(a.report).open("w", encoding="utf-8") as fh:
            fh.write("index\tkind\tsyllables\tpreview\n")
            for i, (kind, txt) in enumerate(blocks, 1):
                preview = txt.strip()[:80].replace("\t", " ").replace("\n", "/")
                fh.write(f"{i}\t{kind}\t{count_syllables(txt)}\t{preview}\n")
        print("Report: " + a.report)

    if not a.dry_run:
        p = Path(a.output)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(cleaned, encoding="utf-8")
        print("Wrote " + a.output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
