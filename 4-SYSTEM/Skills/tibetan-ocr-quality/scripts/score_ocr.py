#!/usr/bin/env python3
"""Score Tibetan OCR output quality using KenLM perplexity.

Usage:
    python score_ocr.py <input_file> [--model <arpa_path>]

Requires:
    pip install kenlm

Normalization logic inlined from Botok (OpenPecha/Botok) — no botok dependency.
Sources:
  - botok/utils/corpus_normalization.py
  - botok/utils/unicode_normalization.py
  - botok/utils/standard_tibetan.py
License: Apache-2.0 (https://github.com/OpenPecha/Botok/blob/master/LICENSE)
"""

import argparse
import math
import re
import sys
import unicodedata
from enum import Enum
from pathlib import Path


# ============================================================================
# Inlined from botok/utils/unicode_normalization.py
# ============================================================================

class _Cats(Enum):
    Other = 0
    Base = 1
    Subscript = 2
    BottomVowel = 3
    BottomMark = 4
    TopVowel = 5
    TopMark = 6
    RightMark = 7


_CATEGORIES = (
    [_Cats.Other]
    + [_Cats.Base]
    + [_Cats.Other] * 22
    + [_Cats.BottomVowel] * 2
    + [_Cats.Other] * 6
    + [_Cats.Base] * 20
    + [_Cats.Other]
    + [_Cats.BottomMark]
    + [_Cats.Other]
    + [_Cats.BottomMark]
    + [_Cats.Other]
    + [_Cats.Subscript]
    + [_Cats.Other] * 4
    + [_Cats.RightMark]
    + [_Cats.Other]
    + [_Cats.Base] * 45
    + [_Cats.Other] * 4
    + [_Cats.BottomVowel]
    + [_Cats.TopVowel]
    + [_Cats.TopVowel]
    + [_Cats.BottomVowel] * 2
    + [_Cats.TopVowel] * 8
    + [_Cats.TopMark]
    + [_Cats.RightMark]
    + [_Cats.TopVowel] * 2
    + [_Cats.TopMark] * 2
    + [_Cats.BottomMark]
    + [_Cats.Other]
    + [_Cats.TopMark] * 2
    + [_Cats.Base] * 2
    + [_Cats.Base]
    + [_Cats.Other]
    + [_Cats.Base]
    + [_Cats.Subscript] * 48
)


def _charcat(c):
    o = ord(c)
    if 0x0F00 <= o <= 0x0FBC:
        return _CATEGORIES[o - 0x0F00]
    return _Cats.Other


def _unicode_reorder(txt):
    charcats = [_charcat(c) for c in txt]
    i = 0
    res = []
    while i < len(charcats):
        c = charcats[i]
        if c != _Cats.Base:
            res.append(txt[i])
            i += 1
            continue
        j = i + 1
        while j < len(charcats) and charcats[j].value > _Cats.Base.value:
            j += 1
        newindices = sorted(range(i, j), key=lambda e: (charcats[e].value, e))
        res.append("".join(txt[n] for n in newindices))
        i = j
    return "".join(res)


def _is_vowel(char):
    return bool(re.search(r"[ཱ-྄]", char))


def _is_suffix(char):
    return bool(re.search(r"[ྐ-ྼ]", char))


def _normalize_invalid_start_string(s):
    if len(s) < 2:
        return s
    if _is_vowel(s[0]) and not _is_vowel(s[1]) and not _is_suffix(s[1]):
        return s[1] + s[0] + (s[2:] if len(s) > 2 else "")
    if _is_suffix(s[0]):
        return s[1:]
    return s


def _normalize_unicode(s, form="nfd"):
    s = s.replace("ཱི", "ཱི")
    s = s.replace("ཱུ", "ཱུ")
    s = s.replace("ཷ", "ྲཱྀ")
    s = s.replace("ཹ", "ླཱྀ")
    s = s.replace("ཱྀ", "ཱྀ")
    if form == "nfd":
        s = s.replace("གྷ", "གྷ")
        s = s.replace("཈", "ཇྷ")
        s = s.replace("ཌྷ", "ཌྷ")
        s = s.replace("དྷ", "དྷ")
        s = s.replace("བྷ", "བྷ")
        s = s.replace("ཛྷ", "ཛྷ")
        s = s.replace("ཀྵ", "ཀྵ")
        s = s.replace("ྲྀ", "ྲྀ")
        s = s.replace("ླྀ", "ླྀ")
        s = s.replace("ྒྷ", "ྒྷ")
        s = s.replace("྘", "ྗྷ")
        s = s.replace("ྜྷ", "ྜྷ")
        s = s.replace("ྡྷ", "ྡྷ")
        s = s.replace("ྦྷ", "ྦྷ")
        s = s.replace("ྫྷ", "ྫྷ")
        s = s.replace("ྐྵ", "ྐྵ")
    else:
        s = s.replace("གྷ", "གྷ")
        s = s.replace("ཌྷ", "ཌྷ")
        s = s.replace("དྷ", "དྷ")
        s = s.replace("བྷ", "བྷ")
        s = s.replace("ཛྷ", "ཛྷ")
        s = s.replace("ཀྵ", "ཀྵ")
        s = s.replace("ྲྀ", "ྲྀ")
        s = s.replace("ླྀ", "ླྀ")
        s = s.replace("ྒྷ", "ྒྷ")
        s = s.replace("ྜྷ", "ྜྷ")
        s = s.replace("ྡྷ", "ྡྷ")
        s = s.replace("ྦྷ", "ྦྷ")
        s = s.replace("ྫྷ", "ྫྷ")
        s = s.replace("ྐྵ", "ྐྵ")
    s = s.replace("ༀ", "ཨོཾ")
    s = s.replace("ཅ༹", "ཙ")
    s = s.replace("ཆ༹", "ཚ")
    s = s.replace("ཇ༹", "ཛ")
    s = _unicode_reorder(s)
    s = re.sub(
        "ཪ(?![ྐ-ྗྚ-ྫྷྮྯྴ-ྼ])",
        "ར", s,
    )
    s = _normalize_invalid_start_string(s)
    return s


# ============================================================================
# Inlined from botok/utils/standard_tibetan.py
# ============================================================================

_ONSET_SET = frozenset({
    "ཀ", "ཀྱ", "ཀྲ", "ཀླ", "དཀ", "དཀྱ", "དཀྲ", "བཀ", "བཀྱ", "བཀྲ", "བཀླ",
    "རྐ", "རྐྱ", "ལྐ", "སྐ", "སྐྱ", "སྐྲ", "བརྐ", "བརྐྱ", "བསྐ", "བསྐྱ", "བསྐྲ",
    "ཁ", "ཁྱ", "ཁྲ", "མཁ", "མཁྱ", "མཁྲ", "འཁ", "འཁྱ", "འཁྲ",
    "ག", "གྱ", "གྲ", "གླ", "དག", "དགྱ", "དགྲ", "བག", "བགྱ", "བགྲ",
    "མག", "མགྱ", "མགྲ", "འག", "འགྱ", "འགྲ", "རྒ", "རྒྱ", "ལྒ",
    "སྒ", "སྒྱ", "སྒྲ", "བརྒ", "བརྒྱ", "བསྒ", "བསྒྱ", "བསྒྲ",
    "ང", "དང", "མང", "རྔ", "ལྔ", "སྔ", "བརྔ", "བསྔ",
    "ཅ", "གཅ", "བཅ", "ལྕ", "ཆ", "མཆ", "འཆ",
    "ཇ", "མཇ", "འཇ", "རྗ", "ལྗ", "བརྗ",
    "ཉ", "གཉ", "མཉ", "རྙ", "སྙ", "བརྙ", "བསྙ",
    "ཏ", "གཏ", "བཏ", "རྟ", "ལྟ", "སྟ", "བརྟ", "བལྟ", "བསྟ",
    "ཐ", "མཐ", "འཐ",
    "ད", "དྲ", "གད", "བད", "མད", "འད", "འདྲ", "རྡ", "ལྡ", "སྡ", "བརྡ", "བལྡ", "བསྡ",
    "ན", "གན", "མན", "རྣ", "སྣ", "བརྣ", "བསྣ",
    "པ", "པྱ", "པྲ", "དཔ", "དཔྱ", "དཔྲ", "ལྤ", "སྤ", "སྤྱ", "སྤྲ",
    "ཕ", "ཕྱ", "ཕྲ", "འཕ", "འཕྱ", "འཕྲ",
    "བ", "བྱ", "བྲ", "བླ", "དབ", "དབྱ", "དབྲ", "འབ", "འབྱ", "འབྲ",
    "རྦ", "ལྦ", "སྦ", "སྦྱ", "སྦྲ",
    "མ", "མྱ", "དམ", "དམྱ", "རྨ", "རྨྱ", "སྨ", "སྨྱ",
    "ཙ", "གཙ", "བཙ", "རྩ", "སྩ", "བརྩ", "བསྩ",
    "ཚ", "མཚ", "འཚ", "ཛ", "མཛ", "འཛ", "རྫ", "བརྫ",
    "ཝ", "ཞ", "གཞ", "བཞ", "ཟ", "ཟླ", "གཟ", "བཟ", "བཟླ",
    "འ", "ཡ", "གཡ", "ར", "རླ", "བརླ", "ལ",
    "ཤ", "གཤ", "བཤ", "ས", "སྲ", "སླ", "གས", "བས", "བསྲ", "བསླ",
    "ཧ", "ཧྲ", "ལྷ", "ཨ",
    "བགླ", "མྲ", "སྨྲ", "ཏྲ", "ཐྲ", "སྣྲ",
    "ཀྭ", "བཀྭ", "ཁྭ", "གྭ", "གྲྭ", "བཅྭ", "ཉྭ",
    "ཏྭ", "ཐྭ", "དྭ", "དྲྭ", "ཕྱྭ", "མྭ",
    "ཙྭ", "རྩྭ", "ཚྭ", "ཛྭ", "ཞྭ", "ཟྭ",
    "རྭ", "ལྭ", "ལྷྭ", "ཤྭ", "སྟྭ", "སྭ", "བསྭ", "ཧྭ",
})

_VOWEL_CODA_SET = frozenset({
    "", "འ", "ག", "གས", "ང", "ངས", "ད", "ན", "བ", "བས", "མ", "མས", "ལ",
    "འི", "འིའོ", "འོ", "འང", "འམ", "ར", "ས",
    "ི", "ིག", "ིགས", "ིང", "ིངས", "ིད", "ིན", "ིབ", "ིབས", "ིམ", "ིམས", "ིལ",
    "ིའི", "ིའིའོ", "ིའོ", "ིའང", "ིའམ", "ིར", "ིས",
    "ུ", "ུག", "ུགས", "ུང", "ུངས", "ུད", "ུན", "ུབ", "ུབས", "ུམ", "ུམས", "ུལ",
    "ུའི", "ུའིའོ", "ུའོ", "ུའང", "ུའམ", "ུར", "ུས",
    "ེ", "ེག", "ེགས", "ེང", "ེངས", "ེད", "ེན", "ེབ", "ེབས", "ེམ", "ེམས", "ེལ",
    "ེའི", "ེའིའོ", "ེའོ", "ེའང", "ེའམ", "ེར", "ེས",
    "ོ", "ོག", "ོགས", "ོང", "ོངས", "ོད", "ོན", "ོབ", "ོབས", "ོམ", "ོམས", "ོལ",
    "ོའི", "ོའིའོ", "ོའོ", "ོའང", "ོའམ", "ོར", "ོས",
    "འུ", "འུའི", "འུའིའོ", "འུའོ", "འུའང", "འུའམ", "འུར", "འུས",
    "ིའུ", "ིའུའི", "ིའུའིའོ", "ིའུའོ", "ིའུའང", "ིའུའམ", "ིའུར", "ིའུས",
    "ུའུ", "ུའུའི", "ུའུའིའོ", "ུའུའོ", "ུའུའང", "ུའུའམ", "ུའུར", "ུའུས",
    "ེའུ", "ེའུའི", "ེའུའིའོ", "ེའུའོ", "ེའུའང", "ེའུའམ", "ེའུར", "ེའུས",
    "ོའུ", "ོའུའི", "ོའུའིའོ", "ོའུའོ", "ོའུའང", "ོའུའམ", "ོའུར", "ོའུས",
})

_MAX_ONSET_LEN = max(len(s) for s in _ONSET_SET if s)
_MAX_VCODA_LEN = max(len(s) for s in _VOWEL_CODA_SET if s)


def _find_longest_prefix(text, start, candidates, max_len):
    end = len(text)
    for length in range(min(max_len, end - start), 0, -1):
        if text[start: start + length] in candidates:
            return start + length
    return -1


def _is_standard_tibetan(syllable):
    if not syllable:
        return False
    onset_end = _find_longest_prefix(syllable, 0, _ONSET_SET, _MAX_ONSET_LEN)
    if onset_end == -1:
        return False
    if onset_end == len(syllable):
        return True
    coda_end = _find_longest_prefix(syllable, onset_end, _VOWEL_CODA_SET, _MAX_VCODA_LEN)
    return coda_end == len(syllable)


def _keepinstack(cp):
    return (0x0F71 <= cp <= 0x0F87) or (0x0F8D <= cp <= 0x0FBC) or cp == 0x0F39


def _split_into_stacks(syllable):
    stacks = []
    i = 0
    n = len(syllable)
    while i < n:
        j = i + 1
        while j < n and _keepinstack(ord(syllable[j])):
            j += 1
        stacks.append(syllable[i:j])
        i = j
    return stacks


# ============================================================================
# Inlined from botok/utils/corpus_normalization.py
# ============================================================================

_LINEBREAKS_RE = re.compile(r"\r\n?|| | ")

_ZERO_WIDTH_STRIP = dict.fromkeys(map(ord, [
    "​", "⁠", "﻿", "᠎", "͏",
]))

_UNICODE_SPACES = [
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ",
    " ", " ", "　", "\t", "\x0b", "\x0c",
]
_SPACE_TO_ASCII = {ord(ch): " " for ch in _UNICODE_SPACES}


def _normalize_spaces(text, collapse_internal_spaces=True, tibetan_specific=False):
    if not text:
        return ""
    s = _LINEBREAKS_RE.sub("\n", text)
    s = s.translate(_ZERO_WIDTH_STRIP)
    s = s.translate(_SPACE_TO_ASCII)
    s = re.sub(r"\n{2,}", "\n", s)
    s = re.sub(r"[ ]+\n", "\n", s)
    s = re.sub(r"\n[ ]+", "\n", s)
    if collapse_internal_spaces:
        s = re.sub(r" {2,}", " ", s)
    if tibetan_specific:
        s = re.sub(r"([་༌࿒]) +([ཀ-ཬ།-༑])", r"\1\2", s)
        s = re.sub(r"([ཀ-ྼ]) +([་༌࿒])", r"\1\2", s)
    return s


def _normalize_corpus(text, strip_control=True, collapse_internal_spaces=True):
    if not text:
        return ""
    s = unicodedata.normalize("NFC", text)
    if strip_control:
        s = "".join(ch for ch in s if ch == "\n" or (unicodedata.category(ch)[0] != "C"))
    s = _normalize_spaces(s, collapse_internal_spaces=collapse_internal_spaces)
    s = _normalize_unicode(s)
    s = s.replace("༌", "་")
    s = s.replace("༎", "།།")
    return s


# --- Compiled patterns for normalize_for_perplexity ---

_LETTER = r"ཀ-ྼ"
_VOWEL = r"ཱ-྄"
_PUNCT = r"།-༔"
_YIG_MGO_START = r"༁-༇༉༊࿐࿑࿓-࿘"

_MULTI_TSHEG_RE = re.compile(r"་{2,}")
_GA_SHA_KA_NL_RE = re.compile(rf"([གཤཀ][{_VOWEL}]?)\n")
_LETTER_BEFORE_NL_RE = re.compile(rf"([{_LETTER}])\n")
_YIG_MGO_RE = re.compile(rf"[{_YIG_MGO_START}]+[{_PUNCT}]*")
_DIGIT_RUN_RE = re.compile(r"[0-9༠-༳][0-9༠-༳, ]*")
_NON_TIBETAN_RE = re.compile(r"[^ༀ-࿿ D]")
_PUNCT_OR_SPACE_RE = re.compile(rf"[{_PUNCT} ]+")
_MULTI_SPACE_RE = re.compile(r" {2,}")
_TSHEG_OR_SPACE_RE = re.compile(r"(་| )")
_BRACKET_RE = re.compile(r"([༼༽])")
_AFFIX_RE = re.compile(rf"^([{_LETTER}]+)(འིས|འི|འོ|འམ|འང|འས|འད|འར)$")


def _split_syllable_affixes(syllable):
    if syllable.endswith("འུར") and len(syllable) > 3:
        return _split_syllable_affixes(syllable[:-1]) + " ར"
    m = _AFFIX_RE.match(syllable)
    if not m:
        return syllable
    stem, affix = m.group(1), m.group(2)
    return _split_syllable_affixes(stem) + " " + affix


def _apply_affix_splits(text):
    parts = _TSHEG_OR_SPACE_RE.split(text)
    for i in range(0, len(parts), 2):
        if any(0x0F40 <= ord(c) <= 0x0FBC for c in parts[i]):
            parts[i] = _split_syllable_affixes(parts[i])
    return "".join(parts)


def _process_sskt(text, space_sskt, fold_sskt):
    parts = _TSHEG_OR_SPACE_RE.split(text)
    out = []
    in_sskt_run = False

    def flush_sskt():
        nonlocal in_sskt_run
        if in_sskt_run:
            out.append(" S")
            in_sskt_run = False

    n = len(parts)
    for i in range(0, n, 2):
        content = parts[i]
        delim = parts[i + 1] if i + 1 < n else ""
        if not content:
            if delim == " " and fold_sskt:
                flush_sskt()
            if delim:
                out.append(delim)
            continue
        has_tibetan = any(0x0F40 <= ord(c) <= 0x0FBC for c in content)
        if not has_tibetan:
            if fold_sskt:
                flush_sskt()
            out.append(content)
            if delim:
                out.append(delim)
            continue
        std = _is_standard_tibetan(content)
        if std:
            if fold_sskt and in_sskt_run:
                flush_sskt()
                out.append(" ")
            out.append(content)
            if delim:
                out.append(delim)
        else:
            if fold_sskt:
                in_sskt_run = True
                if delim == " ":
                    flush_sskt()
                    out.append(delim)
            elif space_sskt:
                stacks = _split_into_stacks(content)
                out.append(" ".join(stacks))
                if delim:
                    out.append(delim)
            else:
                out.append(content)
                if delim:
                    out.append(delim)
    if fold_sskt:
        flush_sskt()
    return _MULTI_SPACE_RE.sub(" ", "".join(out))


def normalize_for_perplexity(text, space_sskt=True, fold_sskt=False):
    """Normalize Tibetan text for perplexity calculation.

    Produces space-delimited tokens with shad (།) as sentence boundary marker.
    """
    text = _normalize_corpus(text)

    # 1) NYIS TSHEG -> TSHEG, collapse runs
    text = text.replace("࿒", "་")
    text = _MULTI_TSHEG_RE.sub("་", text)

    # 2) Remove honorific particles and TSA-PHRU
    text = text.translate({ord("༵"): None, ord("༷"): None, ord("༹"): None})

    # 3) Normalize nasalization marks
    text = text.replace("ྂ", "ཾ").replace("ྃ", "ཾ")

    # 3.5) Typographic shad for ga/sha/ka at line end
    text = _GA_SHA_KA_NL_RE.sub(r"\1།\n", text)

    # 4) Tibetan letter before newline -> insert tsheg
    text = _LETTER_BEFORE_NL_RE.sub(r"\1་\n", text)

    # 5) Drop newlines
    text = text.replace("\n", "")

    # 6) Drop yig-mgo marks
    text = _YIG_MGO_RE.sub("", text)

    # 7) Digit runs -> placeholder D
    text = _DIGIT_RUN_RE.sub("D", text)

    # 8) Strip non-Tibetan (keep D and spaces)
    text = _NON_TIBETAN_RE.sub(" ", text)

    # 9) Punctuation/space runs -> shad token
    text = _PUNCT_OR_SPACE_RE.sub(" ། ", text)

    # 9b) Isolate brackets
    text = _BRACKET_RE.sub(r" \1 ", text)

    # 9c) Split case affixes
    text = _apply_affix_splits(text)

    # 9d) Sanskrit syllable handling
    if space_sskt or fold_sskt:
        text = _process_sskt(text, space_sskt, fold_sskt)

    # 10) Tshegs -> spaces
    text = text.replace("་", " ")
    text = _MULTI_SPACE_RE.sub(" ", text)

    return text.strip()


# ============================================================================
# Scoring
# ============================================================================

def score_file(input_path, model_path):
    """Normalize the input text and compute perplexity with KenLM."""
    import kenlm

    model_p = Path(model_path)
    if not model_p.exists():
        print(
            f"ERROR: Model file not found: {model_path}\n"
            "Download from https://huggingface.co/openpecha/BoKenlm-syl-v0.4\n"
            "and place the .arpa file at the expected path.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = kenlm.Model(model_path)

    input_p = Path(input_path)
    if not input_p.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    raw_text = input_p.read_text(encoding="utf-8")
    if not raw_text.strip():
        print("ERROR: Input file is empty.", file=sys.stderr)
        sys.exit(1)

    normalized = normalize_for_perplexity(raw_text)
    if not normalized.strip():
        print(
            "ERROR: Normalization produced no tokens. "
            "The file may not contain Tibetan text.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Split into sentences on shad
    sentences = [s.strip() for s in normalized.split("།") if s.strip()]
    if not sentences:
        print("ERROR: No sentences found after normalization.", file=sys.stderr)
        sys.exit(1)

    total_log_prob = 0.0
    total_tokens = 0

    for sentence in sentences:
        log_prob = model.score(sentence)
        token_count = len(sentence.split())
        total_log_prob += log_prob
        total_tokens += token_count

    if total_tokens == 0:
        print("ERROR: Zero tokens after scoring.", file=sys.stderr)
        sys.exit(1)

    # KenLM returns log10 scores
    avg_log_prob = total_log_prob / total_tokens
    perplexity = math.pow(10, -avg_log_prob)

    print("=== Tibetan OCR Quality Report ===")
    print(f"File:       {input_path}")
    print(f"Model:      {model_path}")
    print(f"Sentences:  {len(sentences)}")
    print(f"Tokens:     {total_tokens}")
    print(f"Log-prob:   {total_log_prob:.4f}")
    print(f"Perplexity: {perplexity:.4f}")
    print("================================")


def main():
    parser = argparse.ArgumentParser(
        description="Score Tibetan OCR quality via KenLM perplexity"
    )
    parser.add_argument("input_file", help="Path to the Tibetan .txt file")
    parser.add_argument(
        "--model",
        default="4-SYSTEM/models/BoKenlm-syl-v0.4.arpa",
        help="Path to the KenLM ARPA model (default: 4-SYSTEM/models/BoKenlm-syl-v0.4.arpa)",
    )
    args = parser.parse_args()

    try:
        import kenlm  # noqa: F401
    except ImportError:
        print(
            "ERROR: kenlm not installed.\n"
            "Install with: pip install kenlm --break-system-packages",
            file=sys.stderr,
        )
        sys.exit(1)

    score_file(args.input_file, args.model)


if __name__ == "__main__":
    main()
