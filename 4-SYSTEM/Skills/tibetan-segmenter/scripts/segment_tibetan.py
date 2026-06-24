#!/usr/bin/env python3
"""Segment a Tibetan text file into one-sentence-per-line format.

Pipeline:
  1. Remove all newlines (merge into continuous text)
  2. Normalize spaces (Tibetan-specific rules, inlined from Botok)
  3. Sentence-segment at shad boundaries (all types), skipping shad inside yig mgo

Zero third-party dependencies — stdlib only.
"""

import argparse
import re
import unicodedata
from pathlib import Path


# ---------------------------------------------------------------------------
# Step 1: Remove newlines
# ---------------------------------------------------------------------------

_LINEBREAKS_RE = re.compile(r"\r\n?|| | ")
_LETTER = r"ཀ-ྼ"
_LETTER_BEFORE_NL_RE = re.compile(rf"([{_LETTER}])\n")


def remove_newlines(text: str) -> str:
    """Merge a multi-line Tibetan string into one continuous line.

    Inserts a tsheg where a Tibetan letter ends a line without one,
    preserving syllable boundaries.
    """
    text = _LINEBREAKS_RE.sub("\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"་{2,}(?=\n)", "་", text)
    text = re.sub(r"(?<=\n)་{2,}", "་", text)
    text = _LETTER_BEFORE_NL_RE.sub(r"\1་", text)
    text = text.replace("\n", "")
    return text


# ---------------------------------------------------------------------------
# Step 2: Normalize spaces
# Inlined from: https://github.com/OpenPecha/Botok/blob/master/botok/utils/corpus_normalization.py#L30
# ---------------------------------------------------------------------------

_ZERO_WIDTH_STRIP = dict.fromkeys(map(ord, [
    "​",  # ZERO WIDTH SPACE
    "⁠",  # WORD JOINER
    "﻿",  # BOM
    "᠎",  # MONGOLIAN VOWEL SEPARATOR
    "͏",  # COMBINING GRAPHEME JOINER
]))

_SPACE_TO_ASCII = {ord(ch): " " for ch in [
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ",
    " ", " ", "　",
    "\t", "\x0b", "\x0c",
]}


def normalize_spaces(text: str) -> str:
    """Normalize spaces in Tibetan text (Botok-compatible, zero dependencies).

    1. Map Unicode line endings to LF, exotic spaces to ASCII space.
    2. Strip zero-width/invisible characters.
    3. Collapse multiple spaces to one.
    4. Tibetan-specific: remove space after tsheg before initial letter/shad,
       remove space between final letter and tsheg.
    """
    if not text:
        return ""

    s = _LINEBREAKS_RE.sub("\n", text)
    s = s.translate(_ZERO_WIDTH_STRIP)
    s = s.translate(_SPACE_TO_ASCII)
    s = re.sub(r"\n{2,}", "\n", s)
    s = re.sub(r"[ ]+\n", "\n", s)
    s = re.sub(r"\n[ ]+", "\n", s)
    s = re.sub(r" {2,}", " ", s)

    # Remove space after tsheg (U+0F0B, U+0F0C, U+0FD2) before initial letter or shad
    s = re.sub(r"([་༌࿒]) +([ཀ-ཬ།-༑])", r"\1\2", s)
    # Remove space between final letter and tsheg
    s = re.sub(r"([ཀ-ྼ]) +([་༌࿒])", r"\1\2", s)

    return s


# ---------------------------------------------------------------------------
# Step 3: Sentence segmentation
#
# Walks character-by-character to:
#   - Skip shad inside yig mgo sequences (༄༅། །, ༁, ༂, ༃, etc.)
#   - Split on all shad types: ། ༎ ༏ ༐ ༑ ༒ ༔
# ---------------------------------------------------------------------------

# Yig mgo characters (opening marks) — U+0F01-U+0F0A, U+0FD0-U+0FD8 (incl. svasti signs)
_YIG_MGO_CHARS = set(
    "༁༂༃༄༅༆༇"
    "༈༉༊"
    "࿐࿑࿓࿔࿕࿖࿗࿘"
)

# All shad (sentence-ending punctuation) types
_SHAD_CHARS = set(
    "།"  # ། SHAD
    "༎"  # ༎ NYIS SHAD
    "༏"  # ༏ TSHEG SHAD
    "༐"  # ༐ NYIS TSHEG SHAD
    "༑"  # ༑ RIN CHEN SPUNGS SHAD
    "༒"  # ༒ RGYA GRAM SHAD
    "༔"  # ༔ GTER TSHEG
)

# Characters that can trail a yig mgo (shad, tsheg, space) — consumed but not a boundary
_YIG_MGO_TRAIL = _SHAD_CHARS | {"་", "༌", " "}


def segment_sentences(text: str) -> list[str]:
    """Split Tibetan text into sentences at shad boundaries.

    Yig mgo sequences and their trailing shad/tsheg are kept intact —
    only shad in running text triggers a segment break.
    """
    sentences = []
    current: list[str] = []
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        # --- Yig mgo: consume the whole mark + trailing punct as non-boundary ---
        if ch in _YIG_MGO_CHARS:
            while i < n and text[i] in _YIG_MGO_CHARS:
                current.append(text[i])
                i += 1
            while i < n and text[i] in _YIG_MGO_TRAIL:
                current.append(text[i])
                i += 1
            continue

        # --- Sentence-ending shad: consume full punct run, then break ---
        if ch in _SHAD_CHARS:
            current.append(ch)
            i += 1
            # Consume any additional shad / spaces (handles ། ། double-shad etc.)
            while i < n and text[i] in _SHAD_CHARS | {" "}:
                current.append(text[i])
                i += 1
            sentence = "".join(current).strip()
            if sentence:
                sentences.append(sentence)
            current = []
            continue

        # --- Regular character ---
        current.append(ch)
        i += 1

    # Flush remainder
    if current:
        sentence = "".join(current).strip()
        if sentence:
            sentences.append(sentence)

    return sentences


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_file(input_path: str, output_path: str | None = None) -> str:
    """Run the full pipeline on a file and return the output path."""
    inp = Path(input_path)
    out = Path(output_path) if output_path else inp.with_name(f"{inp.stem}_segmented{inp.suffix}")

    text = inp.read_text(encoding="utf-8")
    text = unicodedata.normalize("NFC", text)

    # 1. Remove newlines
    text = remove_newlines(text)

    # 2. Normalize spaces
    text = normalize_spaces(text)

    # 3. Sentence segmentation
    sentences = segment_sentences(text)

    out.write_text("\n".join(sentences) + "\n", encoding="utf-8")
    return str(out)


def main():
    parser = argparse.ArgumentParser(
        description="Segment a Tibetan text file into one-sentence-per-line format."
    )
    parser.add_argument("input", help="Path to the input Tibetan text file")
    parser.add_argument("-o", "--output", default=None, help="Output file path")
    args = parser.parse_args()

    out_path = process_file(args.input, args.output)
    print(f"Segmented output written to: {out_path}")


if __name__ == "__main__":
    main()
