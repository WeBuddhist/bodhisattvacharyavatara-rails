#!/usr/bin/env python3
"""
translate_zeroshot.py
=====================

Zero-shot translation of a structured Buddhist Markdown file from any source
language into any target language, with audience-level control for Hindi output.

The source Markdown has a strict structure that MUST be preserved byte-for-byte
in everything that is not actual verse text:

    1. A YAML front matter block delimited by `---` ... `---` at the top.
    2. Main title with `#`, chapters with `##` (and `###`/`####` sub-sections).
    3. Each verse is a 4-line stanza, preceded by a transclusion link such as
       `![[1-SOURCES/Text/BCAV08_SH_sk.md#^1-1]]`, and the last line of the
       stanza ends with an Obsidian block identifier like `^1-1`, `^6-33`,
       `^I-3`, or `^0`.

Pipeline
--------
    read file
      -> detect or accept --source-lang / --target-lang
      -> split off YAML front matter (kept verbatim, optionally translated)
      -> chunk the body BY CHAPTER (default): one chunk per `##` heading, so
         each LLM call sees a whole chapter and keeps register/terminology
         coherent within it. A chapter whose text exceeds --max-chapter-chars
         falls back to the legacy ~3000-4000 char verse-safe window
         (chunk_body) for that chapter only -- never crossing a chapter
         boundary, and never splitting inside a verse block. Pass
         --chunk-mode char to revert to fixed-size-window chunking for the
         whole file (the old default).
      -> translate each chunk automatically via LLM API (gemini / claude / openai)
      -> checkpoint each chunk to work/<source>_<level>/ for --resume
      -> reassemble + write translated_<level>.md

Backends (automated)
--------------------
    auto      Pick first available API key: gemini → claude → openai (default).
    gemini    GEMINI_API_KEY / GOOGLE_API_KEY
    claude    ANTHROPIC_API_KEY
    openai    OPENAI_API_KEY
    manual    Export prompts only (no API); use --assemble after pasting responses.

Automated usage
---------------
    # Full automated run (uses .env API key)
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --level hi-beginner

    # Resume after interrupt (skips completed chunk checkpoints)
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --level hi-beginner --resume

Manual fallback (optional)
--------------------------
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --backend manual
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --assemble --work-dir ...

Languages
---------
Source language is auto-detected from the filename prefix (``bo-``, ``en-``,
``sk-``, ``fr-``, …) or set explicitly with ``--source-lang``.

Target language defaults to ``hi`` (Hindi) for backward compatibility and is
set with ``--target-lang``.

Audience levels (Hindi)
-----------------------
Selected by ``--audience-level`` / ``--level`` (or ``--tier`` + ``--target-lang``):

    hi-beginner   Class 8 (8th standard) reading level. Plain everyday Hindi for
                  readers with no Buddhist or Sanskrit background. Every technical
                  term glossed inline on first use; verses as short prose paragraphs.
    hi-plain      Conversational "chai" Hindustani for 13+ general public. Short
                  sentences, terms explained when unavoidable, verses as prose.
    hi-scholarly  Formal literary Hindi for advanced Mahayana-familiar readers.
                  Sanskrit terms retained in Devanagari, 4-line stanzas preserved.

For non-Hindi targets, pass ``--tier scholarly|plain|beginner``; the script
builds a matching generic profile for the requested language.

Usage
-----
Run from the project root (bodhisattvachartavatara-rails/).

    # Automated (default) — translates all chunks via API
    python 4-SYSTEM/scripts/translate_zeroshot.py \\
        "1-SOURCES/Translations/en-Wallace.md" \\
        --level hi-beginner

    # Resume interrupted run
    python 4-SYSTEM/scripts/translate_zeroshot.py \\
        "1-SOURCES/Translations/en-Wallace.md" \\
        --level hi-beginner --resume

    # Explicit backend
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --backend claude

    # Manual export only (no API)
    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE --backend manual

    # Dry run
    python 4-SYSTEM/scripts/translate_zeroshot.py \\
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" --dry-run

Dependencies
------------
    pip install google-genai      # for --backend gemini
    pip install anthropic         # for --backend claude
    pip install openai            # for --backend openai
    pip install python-dotenv     # optional; auto-loads project .env

API backends are optional at import time; only the selected one is required.
Manual mode needs no packages beyond the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WORK_ROOT = os.path.join(SCRIPT_DIR, "translate_zeroshot", "work")


def _load_dotenv() -> None:
    """Load project .env (python-dotenv if available, else minimal parser)."""
    roots = (os.getcwd(), os.path.join(SCRIPT_DIR, "..", ".."))
    env_path: str | None = None
    for candidate in roots:
        path = os.path.join(os.path.abspath(candidate), ".env")
        if os.path.isfile(path):
            env_path = path
            break
    if not env_path:
        return

    try:
        from dotenv import load_dotenv
        load_dotenv(env_path)
        return
    except ImportError:
        pass

    # Fallback when python-dotenv is not installed.
    with open(env_path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip().strip("'\"")
            if key and key not in os.environ:
                os.environ[key] = value


_load_dotenv()


class TranslationError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# Structural patterns
# ---------------------------------------------------------------------------

# Block identifier at end of a line. The task spec gives `\^\d+-[a-zA-Z0-9]+`,
# but real vault files also use non-numeric chapter slots (`^I-3`) and bare
# heading IDs (`^0`). We broaden to cover all of them while still matching the
# canonical `^chapter-verse` form. The identifier must sit at end-of-line.
BLOCK_ID_RE = re.compile(r"\^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\s*$")

# Strict form the task explicitly mentions, kept available for callers/tests.
STRICT_BLOCK_ID_RE = re.compile(r"\^\d+-[a-zA-Z0-9]+")

# Transclusion / resource link line, e.g. ![[1-SOURCES/Text/...#^1-1]]
RESOURCE_LINK_RE = re.compile(r"^!\[\[.*\]\]\s*$")

# Markdown heading line (# .. ######)
HEADING_RE = re.compile(r"^#{1,6}\s")

# Chapter-level heading. Per the vault convention (CLAUDE.md Sec 5a), `##`
# marks chapter level (`## N. Title ^N-0`); `###`/`####` are sub-sections that
# stay inside their parent chapter's chunk.
CHAPTER_HEADING_RE = re.compile(r"^##\s")

FRONT_MATTER_DELIM = "---"

# ISO-style language codes used in vault filenames (bo-, en-, sk-, …).
LANG_CODE_RE = re.compile(r"^([a-z]{2,3})-", re.IGNORECASE)


@dataclass(frozen=True)
class LanguageSpec:
    code: str
    name: str
    script: str
    literary: str


LANGUAGES: dict[str, LanguageSpec] = {
    "bo": LanguageSpec(
        "bo", "Tibetan", "Tibetan script (Uchen)",
        "classical Tibetan Buddhist literature",
    ),
    "en": LanguageSpec(
        "en", "English", "Latin script",
        "English Buddhist literature",
    ),
    "sk": LanguageSpec(
        "sk", "Sanskrit", "Devanagari (or as in source)",
        "classical Sanskrit Buddhist literature",
    ),
    "hi": LanguageSpec(
        "hi", "Hindi", "Devanagari",
        "Hindi Buddhist literature",
    ),
    "fr": LanguageSpec("fr", "French", "Latin script", "French Buddhist literature"),
    "de": LanguageSpec("de", "German", "Latin script", "German Buddhist literature"),
    "es": LanguageSpec("es", "Spanish", "Latin script", "Spanish Buddhist literature"),
    "zh": LanguageSpec("zh", "Chinese", "Chinese characters", "Chinese Buddhist literature"),
    "ja": LanguageSpec("ja", "Japanese", "Japanese script", "Japanese Buddhist literature"),
}


def detect_lang_from_path(path: str) -> str | None:
    """Infer a language code from a vault filename prefix (e.g. ``bo-…``)."""
    m = LANG_CODE_RE.match(os.path.basename(path))
    return m.group(1).lower() if m else None


def resolve_language(code: str | None, path: str, role: str,
                     default: str | None = None) -> LanguageSpec:
    """Resolve a language code, falling back to filename detection."""
    resolved = (code or detect_lang_from_path(path) or default or "").lower()
    if not resolved:
        raise TranslationError(
            f"Cannot determine {role} language. Pass --{role}-lang or use a "
            f"filename prefixed with a known code ({', '.join(LANGUAGES)})."
        )
    if resolved not in LANGUAGES:
        # Accept unknown codes with a generic spec so any target works.
        return LanguageSpec(
            resolved,
            resolved.upper(),
            f"{resolved.upper()} script",
            f"{resolved.upper()} Buddhist literature",
        )
    return LANGUAGES[resolved]


# ---------------------------------------------------------------------------
# Front matter handling
# ---------------------------------------------------------------------------

@dataclass
class Document:
    front_matter: str  # full block INCLUDING the surrounding --- lines, or ""
    body: str          # everything after the front matter


def split_front_matter(text: str) -> Document:
    """Isolate a leading YAML front matter block.

    Returns the front matter *including* its delimiter lines so it can be
    written back untouched, plus the remaining body.
    """
    # Normalise newlines for processing; we keep '\n' internally.
    lines = text.split("\n")

    # Front matter must start on the very first line.
    if not lines or lines[0].strip() != FRONT_MATTER_DELIM:
        return Document(front_matter="", body=text)

    # Find the closing delimiter.
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONT_MATTER_DELIM:
            fm = "\n".join(lines[: i + 1])
            body = "\n".join(lines[i + 1 :])
            # Drop a single leading blank line from the body for tidiness.
            if body.startswith("\n"):
                body = body[1:]
            return Document(front_matter=fm, body=body)

    # No closing delimiter found -> treat whole thing as body (be safe).
    return Document(front_matter="", body=text)


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def _is_breakable_after(line: str) -> bool:
    """A chunk boundary is allowed immediately AFTER this line if the line
    carries a block identifier (i.e. it closes a verse/block)."""
    return bool(BLOCK_ID_RE.search(line.rstrip()))


def chunk_body(body: str, min_chars: int = 3000, max_chars: int = 4000) -> list[str]:
    """Slice the body into chunks of roughly ``min_chars``..``max_chars``.

    Hard guarantee: a verse block is NEVER split. A break is only ever placed
    - on an empty line, or
    - immediately after a line that ends with a block identifier,
    AND never while we are *inside* an open verse block.

    A verse block opens at its transclusion link (``![[...]]``) and closes at
    the line carrying its block identifier (``^1-1``). The blank line that sits
    between the link and the stanza is *inside* the block, so we must not cut
    there — otherwise the link gets stranded at the end of one chunk while its
    stanza moves to the next. We therefore track an ``in_block`` state and only
    treat a boundary as safe when no block is currently open.

    Strategy: walk the text line by line, accumulating into the current chunk.
    We remember the most recent *safe* boundary. Once the accumulated size
    reaches ``min_chars`` we cut at the next safe boundary. If a unit would push
    us past ``max_chars`` we still cut at the last safe boundary rather than
    mid-verse.
    """
    if not body.strip():
        return []

    lines = body.split("\n")
    chunks: list[str] = []

    cur: list[str] = []          # lines in the current chunk
    cur_len = 0                  # char length of current chunk
    safe_cut = 0                 # index in `cur` where we may safely cut (exclusive)
    safe_len = 0                 # char length up to safe_cut
    in_block = False             # True while between a ![[link]] and its ^id

    def length_of(seg: list[str]) -> int:
        if not seg:
            return 0
        return sum(len(l) for l in seg) + (len(seg) - 1)  # +newlines

    def flush(upto: int, length: int) -> None:
        """Emit cur[:upto] as a chunk, retain the remainder as the new cur."""
        nonlocal cur, cur_len, safe_cut, safe_len
        if upto <= 0:
            return
        chunks.append("\n".join(cur[:upto]))
        cur = cur[upto:]
        cur_len = length_of(cur)
        safe_cut = 0
        safe_len = 0

    for line in lines:
        cur.append(line)
        # +1 for the newline that joins it to the previous line (except first).
        cur_len += len(line) + (1 if len(cur) > 1 else 0)

        is_blank = line.strip() == ""
        closes_block = _is_breakable_after(line)
        opens_block = bool(RESOURCE_LINK_RE.match(line))

        # Open a verse block on a transclusion link.
        if opens_block:
            in_block = True

        # A boundary is safe only when we are NOT inside an open block and the
        # line either closes a block (carries an id) or is blank.
        boundary_here = (closes_block or is_blank) and not (in_block and not closes_block)

        # Close the block once its id line is seen.
        if closes_block:
            in_block = False

        if boundary_here:
            candidate_cut = len(cur)
            candidate_len = cur_len

            if cur_len >= min_chars:
                flush(candidate_cut, candidate_len)
                continue

            safe_cut = candidate_cut
            safe_len = candidate_len

        # If we've blown past max_chars, cut at the last known safe boundary.
        if cur_len > max_chars and safe_cut > 0:
            flush(safe_cut, safe_len)

    # Emit whatever remains.
    if cur and any(l.strip() for l in cur):
        chunks.append("\n".join(cur))

    return chunks


def chunk_by_chapter(body: str, *, chapter_max_chars: int = 12000,
                     fallback_min_chars: int = 3000,
                     fallback_max_chars: int = 4000) -> list[str]:
    """Slice the body into one chunk per chapter (level-2 ``##`` heading).

    Chapter boundaries are the primary and only intentional cut points: per
    the vault convention, ``##`` marks chapter level (``## N. Title ^N-0``),
    while ``###``/``####`` sub-sections stay inside their parent chapter's
    chunk. Any preamble before the first ``##`` heading (the document's ``#``
    title line, an opening prostration, etc.) is folded into chapter 1's
    chunk instead of being sent as its own tiny fragment.

    Why per-chapter and not per-verse or fixed-size: sending a whole chapter
    in one call lets the model keep register and terminology coherent across
    the chapter's own arc, and it maps naturally onto how a human translator
    (and every other skill in this vault, e.g. ``bo-hi-translate``) already
    works "chapter by chapter, identify locked terms, then translate".

    Chapters vary hugely in length -- Chapter 6 (Patience) alone runs to
    roughly 130 verses -- so a chapter whose text exceeds ``chapter_max_chars``
    is NOT sent as one unbounded chunk (risking silently truncated LLM
    output); it falls back to the verse-safe boundary splitting in
    ``chunk_body()`` for that chapter only. A sub-split from that fallback
    never crosses into a neighboring chapter.

    If the body has no ``##`` headings at all (e.g. a non-chaptered fragment),
    this falls back to plain ``chunk_body()`` over the whole thing.
    """
    if not body.strip():
        return []

    lines = body.split("\n")
    heading_idxs = [i for i, l in enumerate(lines) if CHAPTER_HEADING_RE.match(l)]

    if not heading_idxs:
        return chunk_body(body, fallback_min_chars, fallback_max_chars)

    # Fold any preamble (everything before the first ## heading) into
    # chapter 1's span rather than emitting it as a separate chunk.
    starts = [0] + heading_idxs[1:]
    ends = heading_idxs[1:] + [len(lines)]

    chunks: list[str] = []
    for start, end in zip(starts, ends):
        text = "\n".join(lines[start:end]).strip("\n")
        if not text.strip():
            continue
        if len(text) > chapter_max_chars:
            chunks.extend(chunk_body(text, fallback_min_chars, fallback_max_chars))
        else:
            chunks.append(text)
    return chunks


def chunk_label(chunk: str) -> str:
    """First heading line in a chunk, for human-readable dry-run reports."""
    for line in chunk.split("\n"):
        if HEADING_RE.match(line):
            return line.strip()
    return ""


# ---------------------------------------------------------------------------
# Parallel reference source (e.g. Sanskrit root text)
# ---------------------------------------------------------------------------

def parse_blocks(text: str) -> dict[str, str]:
    """Map every block identifier in a Markdown source to its text.

    Used for a *parallel reference* file (e.g. the Sanskrit root) whose block
    IDs are aligned with the file being translated. Each ``^id`` is mapped to
    the content of the block it closes (the ``^id`` marker itself is stripped).
    Blocks are delimited by blank lines or by the id-bearing line.
    """
    doc = split_front_matter(text)
    blocks: dict[str, str] = {}
    acc: list[str] = []
    for raw in doc.body.split("\n"):
        line = raw.rstrip()
        if line.strip() == "":
            acc = []
            continue
        m = BLOCK_ID_RE.search(line)
        if m:
            content = line[: m.start()].rstrip()
            if content:
                acc.append(content)
            block_id = m.group(0).strip()  # e.g. "^4-36"
            blocks[block_id] = "\n".join(a for a in acc if a)
            acc = []
        else:
            acc.append(line)
    return blocks


def chunk_block_ids(chunk: str) -> list[str]:
    """Ordered list of the block IDs that *close* blocks in this chunk.

    These are the end-of-line ``^id`` markers (verse/heading closers), not the
    ids embedded inside ![[...]] transclusion links. They identify which
    reference verses to surface for the chunk.
    """
    ids: list[str] = []
    for line in chunk.split("\n"):
        if RESOURCE_LINK_RE.match(line):
            continue
        m = BLOCK_ID_RE.search(line.rstrip())
        if m:
            ids.append(m.group(0).strip())
    return ids


def build_reference_section(chunk: str, reference_map: dict[str, str] | None) -> str:
    """Build the parallel-reference block for a chunk, or '' if none applies."""
    if not reference_map:
        return ""
    entries: list[str] = []
    for block_id in chunk_block_ids(chunk):
        ref = reference_map.get(block_id)
        if ref:
            entries.append(f"{block_id}:\n{ref}")
    if not entries:
        return ""
    body = "\n\n".join(entries)
    return (
        "PARALLEL REFERENCE ORIGINAL (reference ONLY — do NOT output it). Each "
        "entry below is the original-language verse for the matching ^id in the "
        "text to translate. Use it to disambiguate and verify the meaning of the "
        "corresponding verse, but still translate FROM the text between BEGIN "
        "and END and preserve that text's structure exactly:\n\n"
        f"{body}\n\n"
    )


# ---------------------------------------------------------------------------
# Prompting
# ---------------------------------------------------------------------------

# Default level if nothing else is specified.
AUDIENCE_LEVEL = "hi-scholarly"
AUDIENCE_TIERS = ("beginner", "plain", "scholarly")


@dataclass(frozen=True)
class AudienceProfile:
    key: str
    label: str
    demographic: str
    prior_knowledge: str
    reading_level: str
    constraints: str
    system_instruction: str
    verse_rendering_rule: str
    verse_as_stanzas: bool = True


def build_structural_rules(target: LanguageSpec, source: LanguageSpec) -> str:
    return f"""\
ABSOLUTE STRUCTURAL RULES — follow them exactly, for every audience level:
1. Output ONLY the translated Markdown. Do not add explanations, notes, code \
fences, headings of your own, or commentary of any kind.
2. Preserve every structural element EXACTLY as-is, in the same relative \
position, unchanged:
   - Markdown heading markers (#, ##, ###, ####). Translate the heading TEXT \
into {target.name} ({target.script}) but keep the marker and any trailing block \
identifier intact.
   - Resource / transclusion links written as ![[...]] — reproduce them \
character-for-character. NEVER translate, alter, move, or drop them, and keep \
them on their own line.
   - Verse / block identifiers such as ^1-1, ^6-33, ^I-3, ^0 — reproduce them \
EXACTLY and keep each one attached to the END of the last line of the block it \
belongs to.
   - Blank lines — keep the same blank-line layout between blocks.
4. Do NOT merge, split, reorder, renumber, add, or remove blocks. Translate the \
human-readable {source.name} text only; leave link paths, identifiers, and \
Markdown syntax untouched."""


# Hindi audience profiles (keys: hi-beginner, hi-plain, hi-scholarly).
# system_instruction and verse_rendering_rule use {source_literary},
# {target_name}, {target_script} placeholders filled at resolve time.
_AUDIENCE_TEMPLATES: dict[str, dict] = {
    "hi-beginner": {
        "label": "Beginner Hindi (Class 8 / 8th standard)",
        "demographic": (
            "15+, Hindi-speaking general public encountering Buddhist teachings "
            "for the first time. No monastic or scholarly background; blank slate "
            "for both Buddhist and Sanskrit vocabulary."
        ),
        "prior_knowledge": (
            "None. Every Sanskrit or Buddhist technical term is new and must be "
            "glossed in plain Hindi on first use."
        ),
        "reading_level": "Class 8 (8th standard) Hindi reading level.",
        "constraints": (
            "Plain everyday Hindi; very short sentences (~12–15 words); short "
            "paragraphs suited to mobile reading; every technical term glossed "
            "inline on first use in simple words; no footnotes, diacritics, or "
            "Roman-script Sanskrit; verses as clear prose paragraphs."
        ),
        "verse_as_stanzas": False,
        "system_instruction": (
            "You are a patient, plain-spoken translator who turns {source_literary} "
            "into simple everyday Hindi (Devanagari) for a Class 8 (8th standard) "
            "reader with NO background in Buddhist philosophy or Sanskrit. Use "
            "the simplest Hindi a 13–14-year-old can follow. Every Sanskrit or "
            "Buddhist term must be glossed inline in plain words on first use "
            "(e.g. 'बोधिचित्त — सबके भले की इच्छा'). Keep sentences short. "
            "Render verse as flowing prose, not poetic lines."
        ),
        "verse_rendering_rule": (
            "3. VERSE RENDERING (hi-beginner): Each source verse is a 4-line "
            "stanza, but DO NOT keep the 4-line shape. Render the whole stanza "
            "as ONE short PROSE paragraph (a single line, no internal line breaks) "
            "in plain everyday Hindi at Class 8 (8th standard) reading level. "
            "Use very short sentences of about 12–15 words. Assume the reader "
            "knows nothing about Buddhism: gloss EVERY technical or Sanskrit term "
            "inline on first use in the simplest possible Hindi. No footnotes or "
            "diacritics. Put the trailing ^id at the very END of that single prose "
            "paragraph line, exactly preserving the identifier."
        ),
    },
    "hi-plain": {
        "label": "Plain / general-public Hindi",
        "demographic": (
            "13+, secular or generally religious general public unfamiliar with "
            "Buddhist philosophy."
        ),
        "prior_knowledge": (
            "Minimal; concepts like शून्यता or बोधिचित्त are completely new."
        ),
        "reading_level": "Class 8–10 level.",
        "constraints": (
            "Conversational 'chai' Hindustani register; short sentences "
            "(~15–20 words max); technical terms explained inline; verses "
            "rendered as clear prose paragraphs instead of verse lines."
        ),
        "verse_as_stanzas": False,
        "system_instruction": (
            "You are a warm, plain-spoken translator who turns {source_literary} "
            "into simple, everyday conversational Hindi ('chai' Hindustani register) "
            "for ordinary readers (age 13+) with NO background in Buddhist "
            "philosophy. You use short, clear sentences, and whenever an "
            "unavoidable technical idea appears you explain it inline in plain "
            "words so a newcomer immediately understands. You render verse as "
            "flowing prose, not as poetic lines."
        ),
        "verse_rendering_rule": (
            "3. VERSE RENDERING (hi-plain): Each source verse is a 4-line "
            "stanza, but DO NOT keep the 4-line shape. Render the whole stanza "
            "as ONE clear PROSE paragraph (a single line, no internal line "
            "breaks) in conversational 'chai' Hindustani. Use short sentences "
            "of about 15–20 words at most. Assume the reader has never met any "
            "Buddhist concept: when a term like शून्यता or बोधिचित्त is "
            "unavoidable, explain it inline in plain words (e.g. 'शून्यता "
            "यानी हर चीज़ का कोई ठोस, स्थायी रूप नहीं होता'). Target a Class "
            "8–10 reading level. Put the trailing ^id at the very END of that "
            "single prose paragraph line, exactly preserving the identifier."
        ),
    },
    "hi-scholarly": {
        "label": "Scholarly / practitioner Hindi",
        "demographic": (
            "18+, Mahayana-familiar Buddhists (India, Nepal, global Hindi "
            "speakers), monastics, scholars, and serious practitioners."
        ),
        "prior_knowledge": (
            "Medium-to-advanced. Comfortable with terms like बोधिचित्त, शून्यता, "
            "संसार."
        ),
        "reading_level": "Graduate / classical Hindi prose register.",
        "constraints": (
            "Formal literary Hindi; Sanskrit technical terms retained in "
            "Devanagari; four-line stanza formatting strictly preserved; "
            "minimal to no glossing."
        ),
        "verse_as_stanzas": True,
        "system_instruction": (
            "You are an expert translator of {source_literary} into formal, "
            "literary Hindi (Devanagari) for an advanced, Mahayana-familiar "
            "readership of monastics, scholars, and serious practitioners. You "
            "retain established Sanskrit/Buddhist technical terms (e.g. बोधिचित्त, "
            "शून्यता, संसार) in Devanagari rather than paraphrasing them, and you "
            "render verse as verse in an elevated, poetic classical register."
        ),
        "verse_rendering_rule": (
            "3. VERSE RENDERING (hi-scholarly): Each source verse is a 4-line "
            "stanza. Render it as exactly 4 Hindi lines — one Hindi line per "
            "source line — preserving the line breaks and the poetic verse "
            "shape. Use formal, literary classical Hindi. Retain Buddhist "
            "Sanskrit technical terms in Devanagari (बोधिचित्त, शून्यता, संसार, "
            "etc.) without inline explanation; do NOT gloss or simplify them. "
            "Keep the trailing ^id on the LAST (4th) line, exactly where it was."
        ),
    },
}


def _fmt_lang(template: str, source: LanguageSpec, target: LanguageSpec) -> str:
    return template.format(
        source_literary=source.literary,
        source_name=source.name,
        target_name=target.name,
        target_script=target.script,
    )


def _profile_from_template(key: str, tmpl: dict,
                           source: LanguageSpec,
                           target: LanguageSpec) -> AudienceProfile:
    return AudienceProfile(
        key=key,
        label=tmpl["label"],
        demographic=tmpl["demographic"],
        prior_knowledge=tmpl["prior_knowledge"],
        reading_level=tmpl["reading_level"],
        constraints=tmpl["constraints"],
        system_instruction=_fmt_lang(tmpl["system_instruction"], source, target),
        verse_rendering_rule=_fmt_lang(tmpl["verse_rendering_rule"], source, target),
        verse_as_stanzas=tmpl["verse_as_stanzas"],
    )


def build_generic_profile(tier: str, source: LanguageSpec,
                          target: LanguageSpec) -> AudienceProfile:
    """Fallback profile for non-Hindi targets (or unknown hi-* extensions)."""
    key = f"{target.code}-{tier}"
    if tier == "beginner":
        return AudienceProfile(
            key=key,
            label=f"Beginner {target.name}",
            demographic=f"General public, age 13+, no Buddhist background ({target.name}).",
            prior_knowledge="None; all technical terms explained inline on first use.",
            reading_level="Class 8 (8th standard) reading level.",
            constraints=(
                f"Plain everyday {target.name}; short sentences; verses as prose "
                "paragraphs; inline glosses for technical terms."
            ),
            system_instruction=_fmt_lang(
                "You are a patient translator who turns {source_literary} into "
                "plain, accessible {target_name} ({target_script}) for a Class 8 "
                "(8th standard) reader with no Buddhist background. Use short "
                "sentences and gloss every technical term inline on first use. "
                "Render verse as flowing prose.",
                source, target,
            ),
            verse_rendering_rule=(
                f"3. VERSE RENDERING ({key}): Render each 4-line stanza as ONE "
                f"short prose paragraph in plain {target.name} at Class 8 reading "
                "level. Gloss technical terms inline. Put the trailing ^id at the "
                "END of the prose line."
            ),
            verse_as_stanzas=False,
        )
    if tier == "plain":
        return AudienceProfile(
            key=key,
            label=f"Plain / general-public {target.name}",
            demographic=f"13+, general public unfamiliar with Buddhism ({target.name}).",
            prior_knowledge="Minimal Buddhist background.",
            reading_level="Class 8–10 reading level.",
            constraints=(
                f"Conversational {target.name}; short sentences; verses as prose; "
                "technical terms explained when unavoidable."
            ),
            system_instruction=_fmt_lang(
                "You are a warm, accessible translator who turns {source_literary} "
                "into clear, conversational {target_name} ({target_script}) for "
                "ordinary readers (13+) with no Buddhist background. Explain "
                "technical ideas inline in plain words. Render verse as prose.",
                source, target,
            ),
            verse_rendering_rule=(
                f"3. VERSE RENDERING ({key}): Render each 4-line stanza as ONE "
                f"prose paragraph in conversational {target.name}. Short sentences "
                "(15–20 words). Explain unavoidable technical terms inline. Put "
                "the trailing ^id at the END of the prose line."
            ),
            verse_as_stanzas=False,
        )
    # scholarly (default tier)
    return AudienceProfile(
        key=key,
        label=f"Scholarly / practitioner {target.name}",
        demographic=f"18+, Mahayana-familiar readers, scholars, practitioners ({target.name}).",
        prior_knowledge="Medium-to-advanced Buddhist background.",
        reading_level="Advanced literary register.",
        constraints=(
            f"Formal literary {target.name}; technical terms retained; "
            "four-line stanza formatting preserved; minimal glossing."
        ),
        system_instruction=_fmt_lang(
            "You are an expert translator of {source_literary} into formal, "
            "literary {target_name} ({target_script}) for an advanced, "
            "Mahayana-familiar readership. Retain established Buddhist technical "
            "terms rather than paraphrasing them. Render verse as verse in an "
            "elevated register.",
            source, target,
        ),
        verse_rendering_rule=(
            f"3. VERSE RENDERING ({key}): Render each 4-line stanza as exactly "
            f"4 {target.name} lines — one per source line — preserving line breaks "
            "and poetic shape. Retain technical terms without glossing. Keep the "
            "trailing ^id on the LAST (4th) line."
        ),
        verse_as_stanzas=True,
    )


def get_profile(level: str, source: LanguageSpec,
                target: LanguageSpec) -> AudienceProfile:
    if level in _AUDIENCE_TEMPLATES:
        return _profile_from_template(level, _AUDIENCE_TEMPLATES[level],
                                      source, target)
    # Accept tier shorthand: "beginner", "plain", "scholarly" -> {target}-tier
    if level in AUDIENCE_TIERS:
        return build_generic_profile(level, source, target)
    # Accept prefixed keys for non-Hindi targets: fr-plain, de-scholarly, …
    if "-" in level:
        prefix, _, tier = level.partition("-")
        if tier in AUDIENCE_TIERS and prefix == target.code:
            return build_generic_profile(tier, source, target)
    raise TranslationError(
        f"Unknown audience level '{level}'. "
        f"Hindi levels: {', '.join(_AUDIENCE_TEMPLATES)}; "
        f"or use --tier in {{{', '.join(AUDIENCE_TIERS)}}} with --target-lang."
    )


def resolve_level(cli_level: str | None, cli_tier: str | None,
                  target: LanguageSpec) -> str:
    """Resolve audience level. Precedence: --level > AUDIENCE_LEVEL env > tier."""
    if cli_level:
        return cli_level
    env_level = os.environ.get("AUDIENCE_LEVEL")
    if env_level:
        return env_level
    tier = cli_tier or os.environ.get("AUDIENCE_TIER") or "scholarly"
    if target.code == "hi":
        return f"hi-{tier}"
    return f"{target.code}-{tier}"


CHUNK_PROMPT_TEMPLATE = """\
You are translating from {source_name} into {target_name} ({target_script}) \
for this audience level: {level} — {label}.
  • Readers: {demographic}
  • Prior knowledge: {prior_knowledge}
  • Reading level: {reading_level}
  • Style constraints: {constraints}

{structural_rules}

{verse_rendering_rule}

{reference_section}Here is the text to translate:

----- BEGIN -----
{chunk}
----- END -----

Return ONLY the translated Markdown for the section between BEGIN and END, with \
identical structure (same headings, ![[...]] links, ^identifiers, and blank-line \
layout) and the verse content rendered for the {level} audience exactly as the \
VERSE RENDERING rule above requires."""


def build_prompt(chunk: str, level: str, source: LanguageSpec,
                 target: LanguageSpec,
                 reference_map: dict[str, str] | None = None) -> str:
    profile = get_profile(level, source, target)
    return CHUNK_PROMPT_TEMPLATE.format(
        source_name=source.name,
        target_name=target.name,
        target_script=target.script,
        level=profile.key,
        label=profile.label,
        demographic=profile.demographic,
        prior_knowledge=profile.prior_knowledge,
        reading_level=profile.reading_level,
        constraints=profile.constraints,
        structural_rules=build_structural_rules(target, source),
        verse_rendering_rule=profile.verse_rendering_rule,
        reference_section=build_reference_section(chunk, reference_map),
        chunk=chunk,
    )


# ---------------------------------------------------------------------------
# LLM backends
# ---------------------------------------------------------------------------

DEFAULT_MODELS: dict[str, str] = {
    "gemini": "gemini-2.5-flash",
    "claude": "claude-sonnet-4-6",
    "openai": "gpt-4o",
}

BACKEND_KEY_ORDER: list[tuple[str, list[str]]] = [
    ("gemini", ["GEMINI_API_KEY", "GOOGLE_API_KEY"]),
    ("claude", ["ANTHROPIC_API_KEY"]),
    ("openai", ["OPENAI_API_KEY"]),
]


def detect_available_backend() -> str | None:
    """Return the first backend whose API key is set in the environment."""
    for name, env_vars in BACKEND_KEY_ORDER:
        if any(os.environ.get(v) for v in env_vars):
            return name
    return None


def resolve_backend_and_model(cli_backend: str,
                              cli_model: str | None) -> tuple[str, str, bool]:
    """Return (backend_name, model, use_manual_export)."""
    if cli_backend == "manual":
        return "manual", "", True
    if cli_backend == "auto":
        detected = detect_available_backend()
        if detected is None:
            raise TranslationError(
                "No API key found for automated translation. Add one of "
                "GEMINI_API_KEY, ANTHROPIC_API_KEY, or OPENAI_API_KEY to "
                "your .env file, or pass --backend manual to export prompts."
            )
        model = cli_model or DEFAULT_MODELS[detected]
        return detected, model, False
    model = cli_model or DEFAULT_MODELS.get(cli_backend, cli_backend)
    return cli_backend, model, False


class GeminiBackend:
    def __init__(self, model: str):
        try:
            from google import genai
            from google.genai import types
        except ImportError as e:  # pragma: no cover
            raise TranslationError(
                "google-genai is not installed. Run: pip install google-genai"
            ) from e

        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise TranslationError(
                "Set GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment."
            )
        self._types = types
        self._client = genai.Client(api_key=api_key)
        self._model = model

    def translate(self, prompt: str, system_instruction: str) -> str:
        cfg = self._types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3,
        )
        resp = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=cfg,
        )
        text = getattr(resp, "text", None)
        if not text:
            raise TranslationError("Empty response from Gemini.")
        return text.strip()


class AnthropicBackend:
    def __init__(self, model: str):
        try:
            import anthropic
        except ImportError as e:  # pragma: no cover
            raise TranslationError(
                "anthropic is not installed. Run: pip install anthropic"
            ) from e

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise TranslationError("Set ANTHROPIC_API_KEY in the environment.")
        self._client = anthropic.Anthropic(api_key=api_key)
        self._model = model

    def translate(self, prompt: str, system_instruction: str) -> str:
        resp = self._client.messages.create(
            model=self._model,
            max_tokens=8192,
            temperature=0.3,
            system=system_instruction,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text if resp.content else None
        if not text:
            raise TranslationError("Empty response from Anthropic.")
        return text.strip()


class OpenAIBackend:
    def __init__(self, model: str):
        try:
            from openai import OpenAI
        except ImportError as e:  # pragma: no cover
            raise TranslationError(
                "openai is not installed. Run: pip install openai"
            ) from e

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise TranslationError("Set OPENAI_API_KEY in the environment.")
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def translate(self, prompt: str, system_instruction: str) -> str:
        resp = self._client.chat.completions.create(
            model=self._model,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt},
            ],
        )
        text = resp.choices[0].message.content
        if not text:
            raise TranslationError("Empty response from OpenAI.")
        return text.strip()


def make_backend(name: str, model: str):
    if name == "gemini":
        return GeminiBackend(model)
    if name == "claude":
        return AnthropicBackend(model)
    if name == "openai":
        return OpenAIBackend(model)
    raise TranslationError(f"Unknown backend: {name}")


def _strip_code_fences(text: str) -> str:
    """Defensive: some models wrap output in ```markdown fences despite the
    instruction. Strip a single outer fence if present."""
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.split("\n")
        # drop first fence line
        lines = lines[1:]
        # drop trailing fence line if present
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        return "\n".join(lines).strip()
    return text


def translate_with_retry(backend, prompt: str, system_instruction: str,
                         retries: int = 3, backoff: float = 5.0) -> str:
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            return _strip_code_fences(
                backend.translate(prompt, system_instruction)
            )
        except Exception as e:  # noqa: BLE001 - we want to retry on anything
            last_err = e
            wait = backoff * attempt
            print(f"  ! attempt {attempt}/{retries} failed: {e}; "
                  f"retrying in {wait:.0f}s", file=sys.stderr)
            time.sleep(wait)
    raise TranslationError(f"All {retries} attempts failed: {last_err}")


# ---------------------------------------------------------------------------
# Front-matter selective translation
# ---------------------------------------------------------------------------

def translate_front_matter(fm: str, fields: list[str], backend,
                           system_instruction: str,
                           target: LanguageSpec) -> str:
    """Translate only the values of the named YAML keys; leave the rest as-is.

    This is a light, line-oriented pass — it does not attempt to parse nested
    YAML. It only touches top-level `key: value` lines whose key is requested.
    """
    if not fm or not fields:
        return fm

    out_lines = []
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.+)$", line)
        if m and m.group(1) in fields:
            key, value = m.group(1), m.group(2)
            prompt = (
                f"Translate the following short text into {target.name} "
                f"({target.script}). Return ONLY the translation, no quotes, "
                f"no notes:\n\n{value}"
            )
            try:
                translated = translate_with_retry(
                    backend, prompt, system_instruction
                ).strip()
                line = f"{key}: {translated}"
            except TranslationError as e:
                print(f"  ! front-matter field '{key}' not translated: {e}",
                      file=sys.stderr)
        out_lines.append(line)
    return "\n".join(out_lines)


# ---------------------------------------------------------------------------
# Verification helper
# ---------------------------------------------------------------------------

def extract_anchors(text: str) -> list[str]:
    """Return all block identifiers and resource links, in order, for a
    structural-integrity comparison between source and translation."""
    anchors: list[str] = []
    for line in text.split("\n"):
        for m in re.finditer(r"!\[\[[^\]]*\]\]", line):
            anchors.append(m.group(0))
        bm = BLOCK_ID_RE.search(line.rstrip())
        if bm:
            anchors.append(bm.group(0).strip())
    return anchors


# ---------------------------------------------------------------------------
# Manual export / assemble (no API key)
# ---------------------------------------------------------------------------

_MANUAL_README = """\
# Manual translation workflow

This folder was exported by `translate_zeroshot.py`. Translate each chunk in
any chat UI, then assemble the final file.

## Files

- `system_instruction.txt` — paste as system/context at the start of each session
- `chunks/NNN_prompt.md` — user prompt for chunk NNN
- `chunks/NNN_response.md` — paste the model's translated Markdown here

## Claude.ai

1. Open a new chat.
2. Paste the contents of `system_instruction.txt` as your first message (or use
   Claude's system prompt field if available).
3. For each chunk, paste the contents of `chunks/NNN_prompt.md`.
4. Copy the model reply (Markdown only) into `chunks/NNN_response.md`.
5. When all chunks are filled, run assemble (see below).

## Google Gemini

1. Start a new Gemini chat.
2. Paste `system_instruction.txt`, then a blank line, then `chunks/NNN_prompt.md`
   as one message (or use Gems/custom instructions for the system text).
3. Save the reply to `chunks/NNN_response.md`.
4. Repeat for each chunk.

## Cursor chat

1. Open this repo in Cursor.
2. Reference `@chunks/NNN_prompt.md` in the chat (or paste its contents).
3. Include `system_instruction.txt` in the same message or as project context.
4. Save the assistant reply to `chunks/NNN_response.md`.
5. Repeat for each chunk.

## Assemble

From the project root:

    python 4-SYSTEM/scripts/translate_zeroshot.py SOURCE \\
        --assemble --work-dir PATH/TO/THIS/FOLDER \\
        -o translated_OUTPUT.md

Re-run assemble any time after filling more response files.
"""


def default_work_dir(source_path: str, level: str) -> str:
    stem = Path(source_path).stem
    safe = re.sub(r"[^\w\-.]+", "_", f"{stem}_{level}")
    return os.path.join(DEFAULT_WORK_ROOT, safe)


def write_manifest(work_dir: str, manifest: dict) -> None:
    os.makedirs(work_dir, exist_ok=True)
    with open(os.path.join(work_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")


def load_manifest(work_dir: str) -> dict:
    path = os.path.join(work_dir, "manifest.json")
    if not os.path.isfile(path):
        raise TranslationError(f"No manifest.json in {work_dir}. Run without --resume.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_chunk_response(work_dir: str, index: int, text: str) -> None:
    """Save translated chunk as a checkpoint (1-based index)."""
    tag = f"{index:03d}"
    chunks_dir = os.path.join(work_dir, "chunks")
    os.makedirs(chunks_dir, exist_ok=True)
    path = os.path.join(chunks_dir, f"{tag}_response.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def load_chunk_responses(work_dir: str, chunk_count: int) -> list[str | None]:
    """Return saved responses per chunk (None = not yet translated)."""
    results: list[str | None] = []
    for i in range(1, chunk_count + 1):
        path = os.path.join(work_dir, "chunks", f"{i:03d}_response.md")
        if _response_is_filled(path):
            results.append(_read_response_file(path))
        else:
            results.append(None)
    return results


def init_automated_workdir(
    work_dir: str,
    *,
    source_path: str,
    source: LanguageSpec,
    target: LanguageSpec,
    level: str,
    output: str,
    system_instruction: str,
    chunks: list[str],
    front_matter: str,
    reference_path: str | None,
    backend_name: str,
    model: str,
    chunk_mode: str = "chapter",
) -> None:
    """Write manifest and system instruction for an automated (checkpointed) run."""
    os.makedirs(os.path.join(work_dir, "chunks"), exist_ok=True)
    manifest = {
        "source": os.path.abspath(source_path),
        "source_lang": source.code,
        "target_lang": target.code,
        "level": level,
        "output": output,
        "chunk_count": len(chunks),
        "chunk_mode": chunk_mode,
        "front_matter": front_matter,
        "reference": os.path.abspath(reference_path) if reference_path else None,
        "source_chunk_ids": [chunk_block_ids(c) for c in chunks],
        "backend": backend_name,
        "model": model,
        "mode": "automated",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    write_manifest(work_dir, manifest)
    with open(os.path.join(work_dir, "system_instruction.txt"), "w",
              encoding="utf-8") as f:
        f.write(system_instruction.rstrip() + "\n")


def export_manual_workdir(
    work_dir: str,
    *,
    source_path: str,
    source: LanguageSpec,
    target: LanguageSpec,
    level: str,
    output: str,
    system_instruction: str,
    chunks: list[str],
    front_matter: str,
    reference_path: str | None,
    reference_map: dict[str, str] | None,
    translate_frontmatter: list[str] | None,
    chunk_mode: str = "chapter",
) -> None:
    """Write manifest, system prompt, per-chunk prompts, and response templates."""
    os.makedirs(os.path.join(work_dir, "chunks"), exist_ok=True)

    manifest = {
        "source": os.path.abspath(source_path),
        "source_lang": source.code,
        "target_lang": target.code,
        "level": level,
        "output": output,
        "chunk_count": len(chunks),
        "chunk_mode": chunk_mode,
        "front_matter": front_matter,
        "reference": os.path.abspath(reference_path) if reference_path else None,
        "translate_frontmatter": translate_frontmatter,
        "source_chunk_ids": [chunk_block_ids(c) for c in chunks],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    with open(os.path.join(work_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    with open(os.path.join(work_dir, "system_instruction.txt"), "w",
              encoding="utf-8") as f:
        f.write(system_instruction)
        if not system_instruction.endswith("\n"):
            f.write("\n")

    with open(os.path.join(work_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(_MANUAL_README)

    for i, chunk in enumerate(chunks, 1):
        tag = f"{i:03d}"
        prompt = build_prompt(chunk, level, source, target, reference_map)
        prompt_path = os.path.join(work_dir, "chunks", f"{tag}_prompt.md")
        resp_path = os.path.join(work_dir, "chunks", f"{tag}_response.md")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        if not os.path.isfile(resp_path):
            with open(resp_path, "w", encoding="utf-8") as f:
                f.write(
                    f"<!-- Paste translated Markdown for chunk {i} here. "
                    f"Delete this comment. -->\n"
                )
        print(f"  Exported chunk {i}/{len(chunks)} -> chunks/{tag}_prompt.md")


def _read_response_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # Drop HTML comment placeholders
    lines = [
        ln for ln in text.splitlines()
        if not ln.strip().startswith("<!--")
    ]
    return _strip_code_fences("\n".join(lines).strip())


def _response_is_filled(path: str) -> bool:
    if not os.path.isfile(path):
        return False
    text = _read_response_file(path)
    return bool(text) and "<!-- Paste translated" not in text


def run_assemble(args: argparse.Namespace) -> int:
    work_dir = args.work_dir
    if not work_dir:
        raise TranslationError("--assemble requires --work-dir.")
    manifest_path = os.path.join(work_dir, "manifest.json")
    if not os.path.isfile(manifest_path):
        raise TranslationError(f"No manifest.json in {work_dir}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    chunk_count = manifest["chunk_count"]
    output = args.output or manifest.get("output", "translated.md")
    front_matter = manifest.get("front_matter", "")
    source_chunk_ids: list[list[str]] = manifest.get("source_chunk_ids", [])

    all_chunks: list[str] = []
    missing: list[int] = []

    for i in range(1, chunk_count + 1):
        tag = f"{i:03d}"
        resp_path = os.path.join(work_dir, "chunks", f"{tag}_response.md")
        if not _response_is_filled(resp_path):
            missing.append(i)
            continue
        translated = _read_response_file(resp_path)
        if source_chunk_ids and i - 1 < len(source_chunk_ids):
            out_ids = chunk_block_ids(translated)
            src_ids = source_chunk_ids[i - 1]
            if src_ids != out_ids:
                print(f"  ! WARNING chunk {i}: block-id mismatch\n"
                      f"      expected: {src_ids}\n"
                      f"      got      : {out_ids}", file=sys.stderr)
        all_chunks.append(translated)
        print(f"  Assembled chunk {i}/{chunk_count}")

    if missing:
        raise TranslationError(
            f"{len(missing)} chunk(s) still empty: {missing}. "
            "Fill chunks/NNN_response.md and re-run --assemble."
        )

    body_out = "\n\n".join(all_chunks)
    parts = []
    if front_matter:
        parts.append(front_matter)
    parts.append(body_out)
    result = "\n\n".join(parts).rstrip() + "\n"

    with open(output, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nDone. Wrote {output} ({len(result)} chars) "
          f"from {chunk_count} chunks.")
    return 0


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def run(args: argparse.Namespace) -> int:
    source = resolve_language(args.source_lang, args.source, "source")
    target = resolve_language(args.target_lang, args.source, "target",
                              default="hi")
    level = resolve_level(args.audience_level, args.tier, target)
    profile = get_profile(level, source, target)
    system_instruction = profile.system_instruction

    # Default output name reflects target language and level.
    output = args.output or f"translated_{level}.md"

    with open(args.source, "r", encoding="utf-8") as f:
        text = f.read()

    doc = split_front_matter(text)
    if args.chunk_mode == "chapter":
        chunks = chunk_by_chapter(
            doc.body,
            chapter_max_chars=args.max_chapter_chars,
            fallback_min_chars=args.min_chars,
            fallback_max_chars=args.max_chars,
        )
    else:
        chunks = chunk_body(doc.body, args.min_chars, args.max_chars)

    # Optional parallel reference (e.g. the Sanskrit root text). It is parsed
    # into an id->verse map and surfaced to the model per chunk; it is never
    # translated or emitted, and it does NOT affect chunking.
    reference_map: dict[str, str] | None = None
    if args.reference:
        with open(args.reference, "r", encoding="utf-8") as f:
            reference_map = parse_blocks(f.read())
        # Report how well the reference aligns with the text being translated.
        src_ids = {bid for c in chunks for bid in chunk_block_ids(c)}
        matched = sorted(src_ids & set(reference_map))
        missing = sorted(src_ids - set(reference_map))

    verse_shape = "4-line stanzas" if profile.verse_as_stanzas else "prose paragraphs"
    print(f"Source: {args.source}  ({source.name})")
    print(f"Target: {target.name} ({target.script})")
    print(f"AUDIENCE_LEVEL: {level}  ({profile.label})")
    print(f"  readers        : {profile.demographic}")
    print(f"  reading level  : {profile.reading_level}")
    print(f"  verse output   : {verse_shape}")
    if args.reference:
        print(f"Reference: {args.reference}")
        print(f"  reference blocks parsed : {len(reference_map)}")
        print(f"  ids matched / unmatched : {len(matched)} / {len(missing)}")
        if missing:
            preview = ", ".join(missing[:10]) + ("..." if len(missing) > 10 else "")
            print(f"  unmatched ids (no ref)  : {preview}")
    print(f"Output: {output}")
    print(f"Front matter: {'yes' if doc.front_matter else 'no'}")
    print(f"Chunk mode: {args.chunk_mode}"
          + (f"  (max {args.max_chapter_chars} chars/chapter before fallback split)"
             if args.chunk_mode == "chapter" else ""))
    print(f"Body length: {len(doc.body)} chars -> {len(chunks)} chunk(s)")
    for i, c in enumerate(chunks, 1):
        label = chunk_label(c)
        label_part = f"  [{label}]" if label else ""
        print(f"  chunk {i:>3}: {len(c):>5} chars, "
              f"{len(extract_anchors(c))} anchor(s){label_part}")

    if args.dry_run:
        print("\n[dry-run] No API calls made.")
        return 0

    backend_name, model, use_manual = resolve_backend_and_model(
        args.backend, args.model
    )
    work_dir = args.work_dir or default_work_dir(args.source, level)

    if use_manual:
        print("Manual mode: exporting prompts (no API calls).")
        print(f"Work dir: {work_dir}")
        export_manual_workdir(
            work_dir,
            source_path=args.source,
            source=source,
            target=target,
            level=level,
            output=output,
            system_instruction=system_instruction,
            chunks=chunks,
            front_matter=doc.front_matter,
            reference_path=args.reference,
            reference_map=reference_map,
            translate_frontmatter=args.translate_frontmatter,
            chunk_mode=args.chunk_mode,
        )
        print(f"\nPaste responses into {work_dir}/chunks/")
        print("  (e.g. 001_response.md, 002_response.md, … — not a literal 'NNN' name)")
        print("Then assemble:")
        print(f"  python 4-SYSTEM/scripts/translate_zeroshot.py {args.source!r} "
              f"--assemble --work-dir {work_dir!r} -o {output!r}")
        return 0

    print(f"Backend: {backend_name}  model: {model}")
    backend = make_backend(backend_name, model)

    if args.resume:
        manifest = load_manifest(work_dir)
        if manifest.get("chunk_count") != len(chunks):
            raise TranslationError(
                f"Chunk count mismatch: manifest has {manifest['chunk_count']}, "
                f"source produces {len(chunks)}. Delete {work_dir} or run "
                "without --resume."
            )
        prior_mode = manifest.get("chunk_mode", "char")  # older manifests predate this field
        if prior_mode != args.chunk_mode:
            raise TranslationError(
                f"Chunk mode mismatch: checkpoint was created with "
                f"--chunk-mode {prior_mode}, but this run passed "
                f"--chunk-mode {args.chunk_mode}. Match the original mode, "
                f"or delete {work_dir} to start over."
            )
        saved = load_chunk_responses(work_dir, len(chunks))
        done = sum(1 for s in saved if s is not None)
        print(f"Resume: {done}/{len(chunks)} chunk(s) already checkpointed in "
              f"{work_dir}")
    else:
        saved = [None] * len(chunks)
        init_automated_workdir(
            work_dir,
            source_path=args.source,
            source=source,
            target=target,
            level=level,
            output=output,
            system_instruction=system_instruction,
            chunks=chunks,
            front_matter=doc.front_matter,
            reference_path=args.reference,
            backend_name=backend_name,
            model=model,
            chunk_mode=args.chunk_mode,
        )
        print(f"Checkpoints: {work_dir}/chunks/001_response.md, 002_response.md, …")

    # Selectively translate front matter if requested.
    front_matter = doc.front_matter
    if args.translate_frontmatter:
        print("Translating selected front-matter fields: "
              f"{', '.join(args.translate_frontmatter)}")
        front_matter = translate_front_matter(
            doc.front_matter, args.translate_frontmatter, backend,
            system_instruction, target
        )

    translated_chunks: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        if saved[i - 1] is not None:
            print(f"Skipping chunk {i}/{len(chunks)} (checkpoint exists)")
            translated_chunks.append(saved[i - 1])
            continue

        print(f"Translating chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        prompt = build_prompt(chunk, level, source, target, reference_map)
        translated = translate_with_retry(
            backend, prompt, system_instruction,
            retries=args.retries, backoff=args.backoff
        )

        src_ids = chunk_block_ids(chunk)
        out_ids = chunk_block_ids(translated)
        if src_ids != out_ids:
            print(f"  ! WARNING chunk {i}: block-id mismatch\n"
                  f"      source : {src_ids}\n"
                  f"      output : {out_ids}", file=sys.stderr)

        write_chunk_response(work_dir, i, translated)
        translated_chunks.append(translated)

        if i < len(chunks) and args.delay > 0:
            time.sleep(args.delay)

    # Reassemble: front matter, blank line, then chunks joined by blank lines.
    body_out = "\n\n".join(translated_chunks)
    parts = []
    if front_matter:
        parts.append(front_matter)
    parts.append(body_out)
    result = "\n\n".join(parts).rstrip() + "\n"

    with open(output, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nDone. Wrote {output} ({len(result)} chars) for level '{level}'.")
    print(f"Checkpoints saved in {work_dir}")
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    hi_levels = ", ".join(_AUDIENCE_TEMPLATES)
    p = argparse.ArgumentParser(
        description="Zero-shot Buddhist Markdown translator with chapter-wise, "
                    "verse-safe chunking and structure preservation. Any "
                    "source language to any target language."
    )
    p.add_argument("source", help="Path to the source Markdown file.")
    p.add_argument("--source-lang", "--from", dest="source_lang", default=None,
                   metavar="CODE",
                   help="Source language code (bo, en, sk, …). Auto-detected "
                        "from filename prefix if omitted.")
    p.add_argument("--target-lang", "--to", dest="target_lang", default="hi",
                   metavar="CODE",
                   help="Target language code (default: hi).")
    p.add_argument("-l", "--audience-level", "--level", dest="audience_level",
                   default=None,
                   help="Full audience level key (e.g. hi-beginner, hi-plain, "
                        f"hi-scholarly, fr-plain). Hindi levels: {hi_levels}. "
                        "Overrides AUDIENCE_LEVEL env var.")
    p.add_argument("--tier", choices=list(AUDIENCE_TIERS), default=None,
                   help="Audience tier shorthand when --level is omitted: "
                        "beginner (Class 8), plain, or scholarly. Combined "
                        "with --target-lang (e.g. hi + beginner -> hi-beginner).")
    p.add_argument("-o", "--output", default=None,
                   help="Output Markdown path. Default: translated_<level>.md.")
    p.add_argument("--reference", "--sanskrit", dest="reference", default=None,
                   metavar="PATH",
                   help="Optional second source (e.g. the Sanskrit root text) "
                        "used as an ID-aligned PARALLEL REFERENCE to improve "
                        "translation accuracy. It is NOT translated or emitted; "
                        "for each chunk, only the reference verses whose ^id "
                        "matches the text being translated are shown to the "
                        "model. Does not affect chunking.")
    p.add_argument("--backend",
                   choices=["auto", "gemini", "claude", "openai", "manual"],
                   default="auto",
                   help="LLM backend (default: auto). auto picks gemini→claude→"
                        "openai from env keys. manual exports prompts only.")
    p.add_argument("--model", default=None,
                   help="Model name. Default per backend: "
                        f"{', '.join(f'{k}={v}' for k, v in DEFAULT_MODELS.items())}.")
    p.add_argument("--work-dir", dest="work_dir", default=None,
                   metavar="PATH",
                   help="Checkpoint folder for automated runs and manual mode. "
                        "Default: translate_zeroshot/work/<source>_<level>/")
    p.add_argument("--resume", action="store_true",
                   help="Resume automated translation: skip chunks that already "
                        "have checkpoints in --work-dir.")
    p.add_argument("--assemble", action="store_true",
                   help="Assemble translated output from saved chunk responses "
                        "in --work-dir (no API calls).")
    p.add_argument("--chunk-mode", choices=["chapter", "char"], default="chapter",
                   dest="chunk_mode",
                   help="Chunking strategy (default: chapter). 'chapter' sends "
                        "one LLM call per ## chapter heading, so a whole "
                        "chapter's register/terminology stays coherent in one "
                        "call; a chapter bigger than --max-chapter-chars still "
                        "falls back to verse-safe --min-chars/--max-chars "
                        "splitting for that chapter only. 'char' uses the "
                        "legacy fixed-size window over the whole file, "
                        "ignoring chapter boundaries.")
    p.add_argument("--max-chapter-chars", type=int, default=12000,
                   dest="max_chapter_chars",
                   help="In --chunk-mode chapter: a chapter larger than this "
                        "many characters is sub-split via --min-chars/"
                        "--max-chars instead of sent as one chunk, to avoid "
                        "truncated LLM output on long chapters (default: "
                        "12000).")
    p.add_argument("--min-chars", type=int, default=3000, dest="min_chars",
                   help="Minimum chunk size in characters (default: 3000). "
                        "Used directly in --chunk-mode char, and as the "
                        "fallback split size for oversized chapters in "
                        "--chunk-mode chapter.")
    p.add_argument("--max-chars", type=int, default=4000, dest="max_chars",
                   help="Maximum chunk size in characters (default: 4000). "
                        "Used directly in --chunk-mode char, and as the "
                        "fallback split size for oversized chapters in "
                        "--chunk-mode chapter.")
    p.add_argument("--delay", type=float, default=4.0,
                   help="Seconds to wait between chunk API calls (default: 4).")
    p.add_argument("--retries", type=int, default=3,
                   help="Retries per chunk on API error (default: 3).")
    p.add_argument("--backoff", type=float, default=5.0,
                   help="Base backoff seconds, multiplied by attempt (default: 5).")
    p.add_argument("--translate-frontmatter", nargs="*", default=None,
                   metavar="KEY",
                   help="YAML keys whose values should also be translated "
                        "(e.g. title). Omit to keep front matter verbatim.")
    p.add_argument("--dry-run", action="store_true",
                   help="Chunk and report only; make no API calls.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    if args.min_chars > args.max_chars:
        print("error: --min-chars must be <= --max-chars", file=sys.stderr)
        return 2
    try:
        if args.assemble:
            return run_assemble(args)
        return run(args)
    except (TranslationError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
