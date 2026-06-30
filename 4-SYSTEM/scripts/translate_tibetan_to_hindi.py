#!/usr/bin/env python3
"""
translate_tibetan_to_hindi.py
=============================

Zero-shot translation of a classical Tibetan Buddhist Markdown file into Hindi.

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
      -> split off YAML front matter (kept verbatim, optionally translated)
      -> chunk the body into ~3000-4000 char pieces WITHOUT ever splitting a
         verse block (only break on a blank line or immediately after a line
         carrying a block identifier)
      -> translate each chunk with an LLM (Gemini via google-genai, or OpenAI)
         under a strict structure-preserving prompt
      -> reassemble + write translated_hindi.md

Audience levels
---------------
Two runtime levels are selected by the AUDIENCE_LEVEL config — module default,
overridable by the ``AUDIENCE_LEVEL`` environment variable, overridable again by
the ``--audience-level`` / ``--level`` CLI flag:

    hi-scholarly  Formal literary Hindi for advanced, Mahayana-familiar readers.
                  Sanskrit technical terms retained in Devanagari, minimal
                  glossing, four-line stanza formatting strictly preserved.
    hi-plain      Conversational "chai" Hindustani for a 13+ general public with
                  no Buddhist background. Short sentences, technical terms
                  explained inline, verses rendered as clear PROSE paragraphs.

The chunker is identical for both levels (it always respects the same structural
markers); only the generator changes — vocabulary register AND verse-vs-prose
output shape — based on the chosen level.

Usage
-----
Run from the project root (bodhisattvachartavatara-rails/).

Available Tibetan source files:
    1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md
    1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md

Sanskrit reference file:
    1-SOURCES/Text/BCAV08_SH_sk.md

    # Gemini (default), scholarly level
    export GEMINI_API_KEY=...     # or GOOGLE_API_KEY
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" --level hi-scholarly

    # Plain "chai" level (prose verses)
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" --level hi-plain

    # Level via environment variable instead of the flag
    AUDIENCE_LEVEL=hi-plain python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md"

    # Minimal (uses the module-default level)
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md"

    # Dual-source: translate the Tibetan, using the ID-aligned Sanskrit root
    # as a parallel reference for accuracy (the Sanskrit is never emitted)
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" \
        --reference "1-SOURCES/Text/BCAV08_SH_sk.md"

    # OpenAI backend
    export OPENAI_API_KEY=...
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" \
        --backend openai --model gpt-4o

    # Dry run (no API calls, just chunk breakdown)
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" --dry-run

    # Common options
    python 4-SYSTEM/scripts/translate_tibetan_to_hindi.py \
        "1-SOURCES/Translations/bo-WeBuddhist-Adaptation.md" \
        --output translated_hindi.md \
        --model gemini-2.5-flash \
        --min-chars 3000 --max-chars 4000 \
        --delay 4.0 \
        --translate-frontmatter title \
        --dry-run

Dependencies
------------
    pip install google-genai      # for --backend gemini  (default)
    pip install openai            # for --backend openai

Both backends are optional at import time; only the one you select is required.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from dataclasses import dataclass

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

FRONT_MATTER_DELIM = "---"


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

# ---------------------------------------------------------------------------
# Audience levels
# ---------------------------------------------------------------------------
#
# The script supports two runtime levels selected by the AUDIENCE_LEVEL config
# (module default below; overridable by the AUDIENCE_LEVEL env var and the
# --audience-level / --level CLI flag, in increasing order of precedence).
#
# The *chunker* is identical for both levels — it always respects the same
# structural markers (front matter, headings, ![[...]] links, ^id identifiers,
# blank lines) so the source is sliced the same way regardless of audience.
# Only the *generator* changes: each level swaps both the vocabulary register
# AND the structural output shape (verse lines vs. prose paragraph).

# Default level if nothing else is specified.
AUDIENCE_LEVEL = "hi-scholarly"


@dataclass(frozen=True)
class AudienceProfile:
    key: str
    label: str
    demographic: str
    prior_knowledge: str
    reading_level: str
    constraints: str
    system_instruction: str
    # Level-specific rule governing how a 4-line stanza is rendered.
    verse_rendering_rule: str


# Shared structural rules that BOTH levels must obey verbatim. The only thing
# that differs between levels is rule 3 (verse rendering), injected per-profile.
_STRUCTURAL_RULES = """\
ABSOLUTE STRUCTURAL RULES — follow them exactly, for every audience level:
1. Output ONLY the translated Markdown. Do not add explanations, notes, code \
fences, headings of your own, or commentary of any kind.
2. Preserve every structural element EXACTLY as-is, in the same relative \
position, unchanged:
   - Markdown heading markers (#, ##, ###, ####). Translate the heading TEXT \
into Hindi but keep the marker and any trailing block identifier intact.
   - Resource / transclusion links written as ![[...]] — reproduce them \
character-for-character. NEVER translate, alter, move, or drop them, and keep \
them on their own line.
   - Verse / block identifiers such as ^1-1, ^6-33, ^I-3, ^0 — reproduce them \
EXACTLY and keep each one attached to the END of the last line of the block it \
belongs to.
   - Blank lines — keep the same blank-line layout between blocks.
4. Do NOT merge, split, reorder, renumber, add, or remove blocks. Translate the \
human-readable Tibetan text only; leave link paths, identifiers, and Markdown \
syntax untouched."""


AUDIENCE_PROFILES: dict[str, AudienceProfile] = {
    "hi-scholarly": AudienceProfile(
        key="hi-scholarly",
        label="Scholarly / practitioner Hindi",
        demographic=(
            "18+, Mahayana-familiar Buddhists (India, Nepal, global Hindi "
            "speakers), monastics, scholars, and serious practitioners."
        ),
        prior_knowledge=(
            "Medium-to-advanced. Comfortable with terms like बोधिचित्त, शून्यता, "
            "संसार."
        ),
        reading_level="Graduate / classical Hindi prose register.",
        constraints=(
            "Formal literary Hindi; Sanskrit technical terms retained in "
            "Devanagari; four-line stanza formatting strictly preserved; "
            "minimal to no glossing."
        ),
        system_instruction=(
            "You are an expert translator of classical Tibetan Buddhist "
            "literature into formal, literary Hindi (Devanagari) for an "
            "advanced, Mahayana-familiar readership of monastics, scholars, and "
            "serious practitioners. You retain established Sanskrit/Buddhist "
            "technical terms (e.g. बोधिचित्त, शून्यता, संसार) in Devanagari "
            "rather than paraphrasing them, and you render verse as verse in an "
            "elevated, poetic classical register."
        ),
        verse_rendering_rule=(
            "3. VERSE RENDERING (hi-scholarly): Each Tibetan verse is a 4-line "
            "stanza. Render it as exactly 4 Hindi lines — one Hindi line per "
            "source line — preserving the line breaks and the poetic verse "
            "shape. Use formal, literary classical Hindi. Retain Buddhist "
            "Sanskrit technical terms in Devanagari (बोधिचित्त, शून्यता, संसार, "
            "etc.) without inline explanation; do NOT gloss or simplify them. "
            "Keep the trailing ^id on the LAST (4th) line, exactly where it was."
        ),
    ),
    "hi-plain": AudienceProfile(
        key="hi-plain",
        label="Plain / general-public Hindi",
        demographic=(
            "13+, secular or generally religious general public unfamiliar with "
            "Buddhist philosophy."
        ),
        prior_knowledge=(
            "Minimal; concepts like शून्यता or बोधिचित्त are completely new."
        ),
        reading_level="Class 8–10 level.",
        constraints=(
            "Conversational 'chai' Hindustani register; short sentences "
            "(~15–20 words max); technical terms explained inline; verses "
            "rendered as clear prose paragraphs instead of verse lines."
        ),
        system_instruction=(
            "You are a warm, plain-spoken translator who turns classical "
            "Tibetan Buddhist verse into simple, everyday conversational Hindi "
            "('chai' Hindustani register) for ordinary readers (age 13+) with "
            "NO background in Buddhist philosophy. You use short, clear "
            "sentences, and whenever an unavoidable technical idea appears you "
            "explain it inline in plain words so a newcomer immediately "
            "understands. You render verse as flowing prose, not as poetic "
            "lines."
        ),
        verse_rendering_rule=(
            "3. VERSE RENDERING (hi-plain): Each Tibetan verse is a 4-line "
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
    ),
}


def get_profile(level: str) -> AudienceProfile:
    if level not in AUDIENCE_PROFILES:
        raise TranslationError(
            f"Unknown AUDIENCE_LEVEL '{level}'. "
            f"Choose one of: {', '.join(AUDIENCE_PROFILES)}."
        )
    return AUDIENCE_PROFILES[level]


def resolve_level(cli_value: str | None) -> str:
    """Resolve the active audience level. Precedence: CLI > env > module default."""
    return cli_value or os.environ.get("AUDIENCE_LEVEL") or AUDIENCE_LEVEL


def build_system_instruction(level: str) -> str:
    return get_profile(level).system_instruction


CHUNK_PROMPT_TEMPLATE = """\
You are translating into HINDI (Devanagari script) for this audience level: \
{level} — {label}.
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


def build_prompt(chunk: str, level: str,
                 reference_map: dict[str, str] | None = None) -> str:
    profile = get_profile(level)
    return CHUNK_PROMPT_TEMPLATE.format(
        level=profile.key,
        label=profile.label,
        demographic=profile.demographic,
        prior_knowledge=profile.prior_knowledge,
        reading_level=profile.reading_level,
        constraints=profile.constraints,
        structural_rules=_STRUCTURAL_RULES,
        verse_rendering_rule=profile.verse_rendering_rule,
        reference_section=build_reference_section(chunk, reference_map),
        chunk=chunk,
    )


# ---------------------------------------------------------------------------
# LLM backends
# ---------------------------------------------------------------------------

class TranslationError(RuntimeError):
    pass


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
                           system_instruction: str) -> str:
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
                "Translate the following short text into Hindi (Devanagari). "
                "Return ONLY the translation, no quotes, no notes:\n\n" + value
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
# Driver
# ---------------------------------------------------------------------------

def run(args: argparse.Namespace) -> int:
    # Resolve the active audience level (CLI > env AUDIENCE_LEVEL > default).
    level = resolve_level(args.audience_level)
    profile = get_profile(level)
    system_instruction = profile.system_instruction

    # Default output name reflects the level unless one was given explicitly.
    output = args.output or f"translated_{level}.md"

    with open(args.source, "r", encoding="utf-8") as f:
        text = f.read()

    doc = split_front_matter(text)
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

    print(f"Source: {args.source}")
    print(f"AUDIENCE_LEVEL: {level}  ({profile.label})")
    print(f"  readers        : {profile.demographic}")
    print(f"  reading level  : {profile.reading_level}")
    print(f"  verse output   : "
          f"{'4-line stanzas' if level == 'hi-scholarly' else 'prose paragraphs'}")
    if args.reference:
        print(f"Reference: {args.reference}")
        print(f"  reference blocks parsed : {len(reference_map)}")
        print(f"  ids matched / unmatched : {len(matched)} / {len(missing)}")
        if missing:
            preview = ", ".join(missing[:10]) + ("..." if len(missing) > 10 else "")
            print(f"  unmatched ids (no ref)  : {preview}")
    print(f"Output: {output}")
    print(f"Front matter: {'yes' if doc.front_matter else 'no'}")
    print(f"Body length: {len(doc.body)} chars -> {len(chunks)} chunk(s)")
    for i, c in enumerate(chunks, 1):
        print(f"  chunk {i:>3}: {len(c):>5} chars, "
              f"{len(extract_anchors(c))} anchor(s)")

    if args.dry_run:
        print("\n[dry-run] No API calls made.")
        return 0

    backend = make_backend(args.backend, args.model)

    # Selectively translate front matter if requested.
    front_matter = doc.front_matter
    if args.translate_frontmatter:
        print("Translating selected front-matter fields: "
              f"{', '.join(args.translate_frontmatter)}")
        front_matter = translate_front_matter(
            doc.front_matter, args.translate_frontmatter, backend,
            system_instruction
        )

    translated_chunks: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Translating chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
        prompt = build_prompt(chunk, level, reference_map)
        translated = translate_with_retry(
            backend, prompt, system_instruction,
            retries=args.retries, backoff=args.backoff
        )

        # Structural sanity check: the verse/block identifiers must survive.
        # Transclusion links (![[...]]) are intentionally NOT required to be
        # preserved, so their presence/absence is ignored here — only a change
        # to the ^id identifiers (a real alignment problem) is reported.
        src_ids = chunk_block_ids(chunk)
        out_ids = chunk_block_ids(translated)
        if src_ids != out_ids:
            print(f"  ! WARNING chunk {i}: block-id mismatch\n"
                  f"      source : {src_ids}\n"
                  f"      output : {out_ids}", file=sys.stderr)

        translated_chunks.append(translated)

        # Rate-limit between calls (skip after the last one).
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
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Zero-shot Tibetan Buddhist Markdown -> Hindi translator "
                    "with verse-safe chunking and structure preservation."
    )
    p.add_argument("source", help="Path to the source Markdown file.")
    p.add_argument("-l", "--audience-level", "--level", dest="audience_level",
                   choices=list(AUDIENCE_PROFILES), default=None,
                   help="Audience level. Overrides the AUDIENCE_LEVEL env var "
                        f"and the module default ('{AUDIENCE_LEVEL}'). "
                        "'hi-scholarly' = formal literary Hindi, Sanskrit terms "
                        "retained, 4-line stanzas; 'hi-plain' = conversational "
                        "'chai' Hindi, terms explained inline, verses as prose.")
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
    p.add_argument("--backend", choices=["gemini", "openai"], default="gemini",
                   help="LLM backend (default: gemini).")
    p.add_argument("--model", default="gemini-2.5-flash",
                   help="Model name (default: gemini-2.5-flash). "
                        "For OpenAI try e.g. gpt-4o.")
    p.add_argument("--min-chars", type=int, default=3000, dest="min_chars",
                   help="Minimum chunk size in characters (default: 3000).")
    p.add_argument("--max-chars", type=int, default=4000, dest="max_chars",
                   help="Maximum chunk size in characters (default: 4000).")
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
        return run(args)
    except (TranslationError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
