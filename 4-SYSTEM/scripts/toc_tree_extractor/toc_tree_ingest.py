#!/usr/bin/env python3
"""
toc_tree_ingest.py — Ingest a TOC tree into a Tibetan commentary file.

Run after extract_toc_tree.py has produced a toc-tree-<id>.md file.
This script uses Gemini to locate where each TOC node begins in the commentary,
builds an annotation JSON, then renders the final tagged commentary inline
(no external tag_inline_toc.py subprocess).

Pipeline
--------
  extract_toc_tree.py  →  toc-tree-<id>.md
        ↓
  toc_tree_ingest.py   →  annotation JSON  →  render()  →  tagged commentary
        ↓
  0-INBOX/inline_toc_commentary/toc-<commentary-filename>.md

--------------------------------------------------------------------------------
Setup
--------------------------------------------------------------------------------
    pip install google-genai
    set GEMINI_API_KEY=...        (Windows)   /   export GEMINI_API_KEY=...  (Unix)

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    python 4-SYSTEM/scripts/toc_tree_extractor/toc_tree_ingest.py \\
        --tree   0-INBOX/toc-tree-<id>.md \\
        --input  0-INBOX/<commentary-file>.md

    # Override output path:
    python ... --out 0-INBOX/inline_toc_commentary/toc-myfile.md

    # Skip the Gemini step and only re-run the renderer on existing annotation:
    python ... --annot 0-INBOX/temp/<id>.annotation.json --no-locate

    # Skip the renderer step (just produce the annotation JSON):
    python ... --no-render

    Run with --help for the full option list.
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path


def _load_dotenv():
    """Load a .env file into os.environ.

    Search order:
      1. Current working directory
      2. The vault root (nearest ancestor containing 4-SYSTEM/)
      3. The directory containing this script
    Stops at the first .env found. No external dependencies — pure stdlib.
    """
    candidates = [Path.cwd()]
    # walk up from cwd looking for vault root
    for p in Path.cwd().parents:
        if (p / "4-SYSTEM").is_dir():
            candidates.append(p)
            break
    candidates.append(Path(__file__).parent)

    for base in candidates:
        env_file = base / ".env"
        if env_file.exists():
            with open(env_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
            return  # stop after first .env found


_load_dotenv()

# ------------------------------------------------------------------------------
# Defaults
# ------------------------------------------------------------------------------
DEFAULT_MODEL = "gemini-flash-latest"
DEFAULT_FALLBACK_MODEL = "gemini-3-flash-preview"
DEFAULT_CHUNK_SIZE = 200   # commentary lines per Gemini chunk
DEFAULT_OVERLAP = 20      # overlap between chunks (so section openings aren't split)
MAX_RETRIES = 8
RETRY_BACKOFF_SECONDS = 8
MAX_BACKOFF_SECONDS = 120

TEMP_SUBDIR = "0-INBOX/temp"
OUT_SUBDIR = "0-INBOX/inline_toc_commentary"

# ------------------------------------------------------------------------------
# TOC tree parsing
# ------------------------------------------------------------------------------
# Matches:   "   * 2.3.1 གསུམ་པ་མཚན་དོན་"
_TOC_LINE_RE = re.compile(
    r"^(?P<indent>\s*)\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+(?P<title>.+?)\s*$"
)

# Tibetan ordinals used to strip the leading ordinal from a heading_title
_TIB_ORDINALS = [
    "བཅུ་གསུམ་པ་", "བཅུ་གཉིས་པ་", "བཅུ་གཅིག་པ་",
    "དང་པོ་", "གཉིས་པ་", "གསུམ་པ་", "བཞི་པ་", "ལྔ་པ་",
    "དྲུག་པ་", "བདུན་པ་", "བརྒྱད་པ་", "དགུ་པ་", "བཅུ་པ་",
]

# Trailing particles to strip for heading_title (the short name for the heading line)
_TRAILING_PARTICLES = re.compile(
    r"[་\s]*(ནི|ལ|འོ|པོ|པ|སྟེ|ཏེ|དང|གོ|ངོ|ནོ|བོ|མོ)$"
)


def strip_leading_ordinal(text: str) -> str:
    """Return the title without the leading Tibetan ordinal (for heading_title)."""
    t = text.strip()
    for ord_word in _TIB_ORDINALS:
        if t.startswith(ord_word):
            return t[len(ord_word):].lstrip("་ ")
    return t


def make_heading_title(title: str) -> str:
    """
    Produce a short section name for the heading line.
    Keep the ordinal if present (per CLAUDE.md §5b: heading shows ordinal + topic).
    Just strip trailing particles and ⟨gap⟩ markers.
    """
    t = title.strip()
    # remove ⟨gap⟩ markers
    t = re.sub(r"\s*⟨gap⟩", "", t)
    # strip trailing grammatical particles
    t = _TRAILING_PARTICLES.sub("", t).strip("་ ")
    # strip trailing shad
    t = t.rstrip("།")
    return t.strip()


def parse_toc_tree(tree_text: str) -> list[dict]:
    """
    Parse a decimal-numbered TOC tree into an ordered flat list of nodes:
      [{"decimal": "1.2.3", "depth": 3, "title": "<full title>", "heading_title": "<short>"}, ...]
    """
    nodes = []
    for line in tree_text.splitlines():
        m = _TOC_LINE_RE.match(line)
        if not m:
            continue
        dec = m.group("dec")
        title = m.group("title").strip()
        depth = len(dec.split("."))
        nodes.append({
            "decimal": dec,
            "depth": depth,
            "title": title,
            "heading_title": make_heading_title(title),
        })
    return nodes


# ------------------------------------------------------------------------------
# Gemini client helpers  (same pattern as extract_toc_tree.py)
# ------------------------------------------------------------------------------
_client = None


def get_client():
    global _client
    if _client is not None:
        return _client
    try:
        from google import genai  # type: ignore
    except ImportError:
        sys.exit("Error: google-genai not installed. Run: pip install google-genai")
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Error: set GEMINI_API_KEY environment variable.")
    _client = genai.Client(api_key=api_key)
    return _client


def _is_overloaded(err) -> bool:
    s = str(err).upper()
    return any(t in s for t in ("503", "UNAVAILABLE", "OVERLOADED", "HIGH DEMAND",
                                "429", "RESOURCE_EXHAUSTED"))


def _generate(client, model, system_prompt, user_content, fallback_model="", label=""):
    from google.genai import types  # type: ignore
    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)
    last_err = None
    for mi, mdl in enumerate(models_to_try):
        if mi > 0:
            print(f"    -> '{model}' overloaded; falling back to '{mdl}'", file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(
                    model=mdl, contents=user_content, config=config)
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)), MAX_BACKOFF_SECONDS)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded" if _is_overloaded(e) else "error"
                    print(f"    ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini failed after retries: {last_err}")


# ------------------------------------------------------------------------------
# Prompts for locating section boundaries
# ------------------------------------------------------------------------------
LOCATE_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist commentaries and ས་བཅད (sa bcad) structural outlines.

You are given:
  1. A CHUNK of a Tibetan commentary (with 1-based line numbers).
  2. A list of PENDING TOC NODES — sections from the commentary's structural outline
     that have not yet been located.

Your task: for each pending node whose section body BEGINS inside this chunk,
output a JSON record. If a node's body does not begin in this chunk, skip it.

For each located node output EXACTLY this JSON object (no extra keys):

{
  "decimal": "<node decimal e.g. 1.2.3>",
  "body_start_context": "<verbatim substring — 30–60 characters — unique to the line
                          where the section body paragraph begins in the chunk>",
  "restatement": "<verbatim ordinal+title phrase at the start of that body line
                  that can be wrapped in a self-referential wikilink — e.g.
                  'གཉིས་པ་བཤད་པ་' — or null if no restatement phrase is present>",
  "parent_announced_context": "<verbatim 30–60-char substring unique to the line
                               in the PARENT section where this child node is
                               ANNOUNCED/ENUMERATED — i.e. where the parent lists
                               its sub-topics including this one — or null if not
                               visible in this chunk>",
  "parent_announced_term": "<the verbatim announced term within that enumeration
                            line for this child (the minimal structural term only,
                            without ordinal or particles) — or null>"
}

IMPORTANT RULES:
- body_start_context must be a VERBATIM substring from the chunk, long enough to be
  unique in the file. Copy it exactly, character for character. Never paraphrase.
- restatement must appear on the SAME line as body_start_context. Copy exactly.
  Use null if there is no in-text restatement of the section title on that line.
- parent_announced_context/term: these mark where THIS child is NAMED inside its
  parent's enumeration sentence (the sa bcad announcement). Only fill these when
  the parent announcement is visible in the current chunk. Copy verbatim.
- parent_announced_term should be the SHORT announced term, not the full ordinal phrase.
  E.g. for a node titled 'གཉིས་པ་བཤད་པ་', the term in the parent announcement is
  typically 'བཤད་པ་' (or the wording used in the parent's list).
- A section BODY begins at the first commentary prose paragraph after the structural
  announcement/title phrase. The heading will be inserted BEFORE this line.
- If NO pending nodes begin in this chunk, output exactly: []
- Output only a JSON array of objects (no markdown fences, no commentary).
"""

LOCATE_USER_TEMPLATE = """\
--- PENDING TOC NODES (find which start in this chunk) ---
{nodes_text}

--- CHUNK (lines {start_line}–{end_line}) ---
{chunk_text}
"""


def format_nodes_for_prompt(nodes: list[dict]) -> str:
    lines = []
    for n in nodes:
        lines.append(f"  {n['decimal']}  {n['title']}")
    return "\n".join(lines)


def locate_sections_in_chunk(client, model, chunk_text, start_line, end_line,
                              pending_nodes, fallback_model=""):
    """Ask Gemini to locate pending TOC nodes in a chunk. Returns list of dicts."""
    if not pending_nodes:
        return []
    nodes_text = format_nodes_for_prompt(pending_nodes)
    user_content = LOCATE_USER_TEMPLATE.format(
        nodes_text=nodes_text,
        start_line=start_line,
        end_line=end_line,
        chunk_text=chunk_text,
    )
    raw = _generate(client, model, LOCATE_SYSTEM_PROMPT, user_content,
                    fallback_model=fallback_model,
                    label=f"locate lines {start_line}-{end_line}")
    # strip code fences if Gemini wraps despite instructions
    raw = re.sub(r"^```[a-zA-Z]*\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)
    raw = raw.strip()
    if not raw or raw == "[]":
        return []
    try:
        result = json.loads(raw)
        if not isinstance(result, list):
            print(f"  ! Gemini returned non-list JSON for lines {start_line}-{end_line}; "
                  f"skipping.", file=sys.stderr)
            return []
        return result
    except json.JSONDecodeError as e:
        print(f"  ! JSON parse error for lines {start_line}-{end_line}: {e}\n"
              f"    Raw: {raw[:200]}", file=sys.stderr)
        return []


# ------------------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------------------
def make_chunks(lines: list[str], chunk_size: int, overlap: int):
    """Yield (start_line_1based, end_line_1based, numbered_text) tuples."""
    total = len(lines)
    start = 0
    while start < total:
        end = min(start + chunk_size, total)
        # Build numbered text for Gemini
        numbered = "".join(
            f"{start + i + 1:5d}  {lines[start + i]}"
            for i in range(end - start)
        )
        yield (start + 1, end, numbered)
        if end >= total:
            break
        start = end - overlap


# ------------------------------------------------------------------------------
# Build annotation JSON from located sections + node metadata
# ------------------------------------------------------------------------------
def build_annotation(nodes: list[dict], located: dict) -> dict:
    """
    nodes   — ordered flat list from parse_toc_tree()
    located — {decimal: gemini_result_dict}

    Returns annotation dict ready to dump as JSON for tag_inline_toc.py.
    Only nodes that were successfully located are included.

    Depth-skip guard: tag_inline_toc.py requires depth to increase by at most 1
    at a time. When a parent node was not located but a deep child was, the depth
    would jump (e.g. 7 → 10), causing a fatal error. We drop any section whose
    inclusion would produce such a skip.
    """
    sections = []
    current_depth = 0  # depth of the last accepted section

    skipped_depth_skip = 0

    for node in nodes:
        dec = node["decimal"]
        if dec not in located:
            # Not located — update current_depth tracking: if this node is
            # shallower than current_depth it resets the "allowed next depth"
            # but we don't emit it, so current_depth stays.
            continue
        loc = located[dec]
        body_ctx = loc.get("body_start_context", "").strip()
        if not body_ctx:
            continue

        depth = node["depth"]

        # Depth-skip guard: only allow descending one level at a time.
        # A section at depth D is only valid if D <= current_depth + 1.
        # (Ascending any number of levels is always fine.)
        if depth > current_depth + 1:
            skipped_depth_skip += 1
            continue  # drop this section to avoid the depth-skip error

        section: dict = {
            "depth": depth,
            "heading_title": node["heading_title"],
            "body_start_context": body_ctx,
        }
        restatement = (loc.get("restatement") or "").strip()
        if restatement:
            section["restatement"] = restatement

        par_ctx = (loc.get("parent_announced_context") or "").strip()
        par_term = (loc.get("parent_announced_term") or "").strip()
        if par_ctx and par_term:
            section["announced_in_parent"] = {
                "context": par_ctx,
                "term": par_term,
            }
        sections.append(section)
        current_depth = depth

    if skipped_depth_skip:
        print(f"  Note: {skipped_depth_skip} section(s) dropped due to depth-skip "
              f"(parent not located). Re-run with --force to retry locating missing nodes.")

    return {"sections": sections}


# ------------------------------------------------------------------------------
# No-AI location: search for each TOC title directly in the commentary text
# ------------------------------------------------------------------------------
# Tibetan tsheg and shad chars used for normalisation
_TSHEG = "་"
_SHAD_RE = re.compile(r"[།༎༏༐༑༒༔\s]+")

# Trailing particles to strip when searching (the tree title may lack them)
_SEARCH_PARTICLES_RE = re.compile(
    r"[་\s]*(ནི|ལ|འོ|པོ|པ|སྟེ|ཏེ|དང|གོ|ངོ|ནོ|བོ|མོ|ནས|གིས|གི|ཀྱི|ཀྱིས|གིས)\s*$"
)


def _normalise(text: str) -> str:
    """Strip shad AND all whitespace (including spaces between syllables)."""
    t = _SHAD_RE.sub("", text)
    t = re.sub(r"\s+", "", t)   # also collapse any remaining spaces
    return t.strip()


def _find_verbatim(needle_norm: str, raw_line: str) -> str | None:
    """
    Find `needle_norm` (a normalised/space-stripped string) inside `raw_line`
    which may have spaces between syllables.  Returns the VERBATIM substring
    from raw_line so it can be used as a context or restatement string.
    Returns None if not found.
    """
    if not needle_norm:
        return None
    # Build a regex that allows \s* between every character of the needle
    # so "གཉིས་པ་སྒྲུབ་ཚུལ་" matches "གཉིས་པ་ སྒྲུབ་ཚུལ་"
    flexible = r"\s*".join(re.escape(ch) for ch in needle_norm)
    m = re.search(flexible, raw_line)
    return m.group(0) if m else None


def _search_variants(title: str) -> list[str]:
    """
    Return a list of search strings to try for `title`, from most to least specific.
    Each is a normalised substring we'll look for in the commentary line text.
    """
    variants = []
    base = _normalise(title)
    if base:
        variants.append(base)
    # Strip one trailing particle
    stripped = _SEARCH_PARTICLES_RE.sub("", base).strip(_TSHEG + " ")
    if stripped and stripped != base:
        variants.append(stripped)
    # Strip leading Tibetan ordinal too (search by topic name only)
    topic = _normalise(strip_leading_ordinal(title))
    if topic and topic not in variants:
        variants.append(topic)
    return variants


def locate_sections_no_ai(nodes: list[dict], lines: list[str]) -> dict:
    """
    Pure string-search location of TOC nodes in the commentary.

    For each node, search the commentary lines for its title text.
    Strategy (tries each in order, stops at first unambiguous match):
      1. Exact normalised title (ordinal + topic)
      2. Title with trailing particle stripped
      3. Topic name only (ordinal stripped)

    Returns {decimal: result_dict} in the same shape as the Gemini path,
    with `body_start_context` set to a 50-char verbatim substring of the
    matching line and `restatement` set to the matched title text.

    Ambiguous matches (title found on multiple lines) are skipped and reported.
    """
    located = {}
    ambiguous = 0
    not_found = 0

    # Pre-build a normalised index: norm_line -> [line_idx, ...]
    norm_lines = [_normalise(l) for l in lines]

    for node in nodes:
        dec = node["decimal"]
        title = node["title"]
        matched_line_idx = None
        matched_variant = None

        for variant in _search_variants(title):
            if not variant:
                continue
            hits = [i for i, nl in enumerate(norm_lines) if variant in nl]
            if len(hits) == 1:
                matched_line_idx = hits[0]
                matched_variant = variant
                break
            elif len(hits) > 1:
                # Ambiguous — try a longer variant next iteration
                continue

        if matched_line_idx is None:
            not_found += 1
            continue

        raw_line = lines[matched_line_idx].rstrip("\n")

        # body_start_context: verbatim substring from raw_line where the match begins.
        # Use _find_verbatim so spaces between syllables are ignored in the search.
        verbatim_match = _find_verbatim(matched_variant, raw_line)
        if verbatim_match:
            ctx_start = raw_line.find(verbatim_match)
            body_ctx = raw_line[ctx_start:ctx_start + 60].strip()
        else:
            body_ctx = raw_line[:60].strip()

        # restatement: verbatim form of the title as it appears in raw_line.
        # Strip trailing particles/shad from the tree title first, then find
        # the verbatim form (ignoring spaces) in the raw line.
        rest_candidate = _normalise(title.strip().rstrip("།").strip())
        rest = _find_verbatim(rest_candidate, raw_line)

        located[dec] = {
            "decimal": dec,
            "body_start_context": body_ctx,
            "restatement": rest,
            "parent_announced_context": None,
            "parent_announced_term": None,
        }

    total = len(nodes)
    found = len(located)
    print(f"  String search: {found}/{total} nodes located "
          f"({total - found} not found — will be absent from annotation)")

    # Second pass: find parent announcement lines and populate
    # parent_announced_context / parent_announced_term for each child.
    enrich_parent_announcements(nodes, located, lines)

    return located


def enrich_parent_announcements(nodes: list[dict], located: dict,
                                 lines: list[str]) -> None:
    """
    For each located node, find the line in the commentary where its parent
    ANNOUNCES it (the enumeration sentence listing the children).

    Strategy:
      1. Build decimal → line-index from body_start_context matches.
      2. For each node at depth > 1, find its parent's line index and its
         own line index, then scan lines between them.
      3. In that window, search for a line containing this child's title
         (short topic form, space-insensitive).  The first such line is the
         announcement line.
      4. Extract the verbatim term and a unique context substring.

    Mutates located[dec] in place.
    """
    # Build decimal → 0-based line index
    dec_to_line: dict[str, int] = {}
    for dec, loc in located.items():
        ctx = loc.get("body_start_context", "")
        if not ctx:
            continue
        ctx_norm = _normalise(ctx)
        for i, raw in enumerate(lines):
            if ctx_norm in _normalise(raw):
                dec_to_line[dec] = i
                break

    # Build ordered list of (decimal, line_idx) for boundary calculations
    dec_order = [n["decimal"] for n in nodes if n["decimal"] in dec_to_line]

    enriched = 0
    for node in nodes:
        dec = node["decimal"]
        if dec not in located or dec not in dec_to_line:
            continue

        parts = dec.split(".")
        if len(parts) == 1:
            continue  # top-level: no parent to announce it

        parent_dec = ".".join(parts[:-1])
        if parent_dec not in dec_to_line:
            continue

        parent_line = dec_to_line[parent_dec]
        child_line  = dec_to_line[dec]

        # Search window: from parent body start up to (but NOT including) child
        # body start — the child's own body line holds the restatement tag and
        # must not also receive a parent_announced_term (overlap error).
        window_start = parent_line
        window_end   = min(child_line, parent_line + 30)

        # Collect search terms: full title (with ordinal), topic only (without)
        full_title  = _normalise(node["title"])
        short_topic = _normalise(strip_leading_ordinal(node["title"]))

        for li in range(window_start, window_end):
            raw_line = lines[li].rstrip("\n")
            if not raw_line.strip():
                continue

            # Try full title first, then short topic
            for search_norm in [full_title, short_topic]:
                if not search_norm:
                    continue
                verbatim = _find_verbatim(search_norm, raw_line)
                if verbatim:
                    # Use this line as the announcement line.
                    # context: first 60 chars (unique enough for most lines)
                    ctx_str = raw_line[:60].strip()
                    # term: the short topic form (strip ordinal from verbatim)
                    topic_verb = _find_verbatim(short_topic, raw_line) or verbatim
                    # strip leading ordinal from verbatim if present
                    topic_only = strip_leading_ordinal(topic_verb).strip("་ ")
                    if not topic_only:
                        topic_only = topic_verb

                    located[dec]["parent_announced_context"] = ctx_str
                    located[dec]["parent_announced_term"]    = topic_only
                    enriched += 1
                    break
            else:
                continue
            break  # found for this node

    print(f"  Announcement enrichment: {enriched} children linked to parent lines")


# ------------------------------------------------------------------------------
# Phase 2 — Gemini-based TOC injection
# ------------------------------------------------------------------------------
class TagError(Exception):
    """Abort rendering with a clear message."""


_WIKILINK_RE = re.compile(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]")
_HEADING_RE = re.compile(r"^#{2,6}\s.*\s\^[0-9]+(?:-[0-9]+)*-0\s*$")


def _unwrap_links(text: str) -> str:
    return _WIKILINK_RE.sub(lambda m: m.group(1), text)


def _heading_level(depth: int, offset: int = 1) -> str:
    """depth=1, offset=1 → '##'; depth=1, offset=2 → '###'. Capped at 6 hashes."""
    return "#" * min(depth + offset, 6)


def _detect_heading_offset(source_text: str) -> int:
    """
    Scan the source for existing markdown headings and return an offset so that
    depth-1 injected headings land one level below the shallowest existing heading.

    Examples:
      source has ## (level 2) → offset=2 → depth-1 becomes ###
      source has # only       → offset=1 → depth-1 becomes ##
      source has no headings  → offset=1 → depth-1 becomes ##
    """
    min_level = None
    for line in source_text.splitlines():
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            level = len(m.group(1))
            if min_level is None or level < min_level:
                min_level = level
    if min_level is None:
        return 1   # no existing headings — start injected headings at ##
    return min_level  # depth-1 lands at min_level+1 (one step below shallowest)


def _assign_block_ids(depths: list) -> list:
    counters: list = []
    ids: list = []
    for i, d in enumerate(depths):
        if d < 1:
            raise TagError(f"section {i}: depth must be >= 1, got {d}")
        if d > len(counters) + 1:
            raise TagError(
                f"section {i}: depth {d} skips a level "
                f"(current depth {len(counters)}). Depth may only increase by 1."
            )
        if d == len(counters) + 1:
            counters.append(1)
        else:
            counters = counters[:d]
            counters[d - 1] += 1
        ids.append("-".join(str(c) for c in counters) + "-0")
    return ids


_ANY_HEADING_RE = re.compile(r'^#{1,6}\s')


def _prose_signature(text: str, drop_headings: bool) -> list:
    sig = []
    for ln in text.splitlines():
        # Drop injected block-ID headings AND remapped pre-existing headings
        if drop_headings and _ANY_HEADING_RE.match(ln):
            continue
        ln = _unwrap_links(ln)
        if ln.strip() == "":
            continue
        sig.append(ln)
    return sig


_EXISTING_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*$')
# Matches block-ID suffix like " ^1-2-3-0"
_BLOCK_ID_RE = re.compile(r'\s+\^[\w-]+-0\s*$')


def _find_existing_headings(lines: list) -> list:
    """
    Return list of (0-based line_idx, current_hashes, heading_text) for every
    markdown heading in the source that does NOT already have a block ID.
    These are pre-existing structural headings that may need remapping.
    """
    result = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        if _BLOCK_ID_RE.search(stripped):
            continue   # already a tagged heading — skip
        m = _EXISTING_HEADING_RE.match(stripped)
        if m:
            result.append((i, len(m.group(1)), m.group(2).strip()))
    return result


def _verify_prose_unchanged(source: str, tagged: str) -> None:
    """Verify tagged text differs from source only by inserted headings and remapped heading levels."""
    before = _prose_signature(source, drop_headings=False)
    after = _prose_signature(tagged, drop_headings=True)
    if before == after:
        return
    for i, (a, b) in enumerate(zip(before, after)):
        if a != b:
            raise TagError(
                f"PROSE INTEGRITY VIOLATION at prose line {i + 1}:\n"
                f"  source: {a!r}\n  output: {b!r}"
            )
    raise TagError(
        f"PROSE INTEGRITY VIOLATION: line count differs "
        f"(source {len(before)} prose lines, output {len(after)})."
    )


INJECT_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist commentaries and ས་བཅད structural outlines.

You are given:
  1. A Tibetan commentary with 1-based line numbers.
  2. NEW_HEADINGS — an ordered list of section headings to INSERT, each with:
       - heading: the exact heading line to insert (e.g. "### གཉིས་པ་བཤད་པ་ ^1-2-0")
       - context: a verbatim substring on (or very near) the line BEFORE which
                  the heading should be placed
  3. EXISTING_HEADINGS — pre-existing heading lines already in the source, each with:
       - line_no: 1-based line number in the source
       - current_heading: the heading as it currently appears
       - toc_nodes: the TOC tree nodes (decimal + title + depth) for reference
     Your job for each existing heading: find the TOC node it belongs to and
     return the CORRECT heading level (number of # characters) it should have,
     based on its structural depth in the TOC tree.

OUTPUT — a single JSON object (no markdown fences):
{
  "insertions": [
    {"heading": "<exact heading string>", "insert_before_line": <int or null>},
    ...
  ],
  "remaps": [
    {"line_no": <int>, "correct_hashes": <int 1-6>},
    ...
  ]
}

RULES for insertions:
- Same order as NEW_HEADINGS input.
- When context matches multiple lines, use document structure to pick the right one.
- Use null if genuinely cannot locate.

RULES for remaps:
- Return one entry per EXISTING_HEADING.
- correct_hashes is 1–6 (number of # chars the heading should have).
- Base the depth on the TOC node the heading corresponds to, plus the heading_offset
  already applied to new headings (so depth-1 TOC node → heading_offset+1 hashes).
- If a heading cannot be matched to any TOC node, return the same number of hashes
  it already has (no change).
"""

INJECT_USER_TEMPLATE = """\
heading_offset: {heading_offset}

--- NEW_HEADINGS (insert these, in document order) ---
{headings_json}

--- EXISTING_HEADINGS (remap these to correct levels) ---
{existing_json}

--- TOC_NODES (full tree for depth reference) ---
{toc_nodes_json}

--- COMMENTARY ---
{numbered_text}
"""


def gemini_inject_toc(client, model: str, source_text: str, annotation: dict,
                      nodes: list, fallback_model: str = "") -> tuple:
    """
    Ask Gemini to:
      1. Locate insertion points for each annotation section heading.
      2. Remap pre-existing source headings to their correct structural depth.
    Returns (tagged_text, n_inserted, n_remapped).
    """
    sections = annotation.get("sections", [])
    if not sections:
        raise TagError("annotation has no 'sections' list")

    depths = [int(s["depth"]) for s in sections]
    block_ids = _assign_block_ids(depths)

    heading_offset = _detect_heading_offset(source_text)
    print(f"  Auto heading offset: {heading_offset} "
          f"(depth-1 → {'#' * min(1 + heading_offset, 6)})", flush=True)

    lines = source_text.splitlines()

    # --- Part 1: new headings to insert ---
    heading_specs = []
    for sec, block_id in zip(sections, block_ids):
        heading_line = f"{_heading_level(sec['depth'], heading_offset)} {sec['heading_title']} ^{block_id}"
        heading_specs.append({
            "heading": heading_line,
            "context": sec.get("body_start_context", ""),
        })

    # --- Part 2: pre-existing headings to remap ---
    existing = _find_existing_headings(lines)
    existing_specs = [
        {
            "line_no": idx + 1,
            "current_heading": f"{'#' * lvl} {text}",
        }
        for idx, lvl, text in existing
    ]

    # Compact TOC node list for Gemini reference
    toc_nodes_compact = [
        {"decimal": n["decimal"], "depth": n["depth"], "title": n["title"]}
        for n in nodes
    ]

    numbered_text = "".join(f"{i + 1:5d}  {lines[i]}\n" for i in range(len(lines)))

    user_content = INJECT_USER_TEMPLATE.format(
        heading_offset=heading_offset,
        headings_json=json.dumps(heading_specs, ensure_ascii=False, indent=2),
        existing_json=json.dumps(existing_specs, ensure_ascii=False, indent=2),
        toc_nodes_json=json.dumps(toc_nodes_compact, ensure_ascii=False, indent=2),
        numbered_text=numbered_text,
    )

    print(f"  Asking Gemini to insert {len(heading_specs)} headings "
          f"and remap {len(existing_specs)} existing headings ...", flush=True)
    raw = _generate(client, model, INJECT_SYSTEM_PROMPT, user_content,
                    fallback_model=fallback_model, label="inject TOC")

    raw = re.sub(r"^```[a-zA-Z]*\n?", "", raw.strip())
    raw = re.sub(r"\n?```$", "", raw).strip()

    try:
        result_obj = json.loads(raw)
    except json.JSONDecodeError as e:
        raise TagError(f"Gemini returned invalid JSON for injection: {e}\n  Raw: {raw[:300]}")

    insertions = result_obj.get("insertions", [])
    remaps = result_obj.get("remaps", [])

    if len(insertions) != len(heading_specs):
        raise TagError(
            f"Gemini returned {len(insertions)} insertions for {len(heading_specs)} headings"
        )

    # --- Build insert_map: 0-based idx → [heading lines] ---
    insert_map: dict = {}
    skipped = 0
    for spec, res in zip(heading_specs, insertions):
        line_no = res.get("insert_before_line")
        if line_no is None:
            print(f"  ! Could not locate: {spec['heading'][:70]}", file=sys.stderr)
            skipped += 1
            continue
        idx = int(line_no) - 1
        if idx < 0 or idx >= len(lines):
            print(f"  ! Out-of-range line {line_no}: {spec['heading'][:70]}", file=sys.stderr)
            skipped += 1
            continue
        insert_map.setdefault(idx, []).append(spec["heading"])

    if skipped:
        print(f"  Warning: {skipped} heading(s) could not be located and were skipped.")

    # --- Build remap_map: 0-based idx → correct_hashes ---
    remap_map: dict = {}
    n_remapped = 0
    for res in remaps:
        line_no = res.get("line_no")
        correct_hashes = res.get("correct_hashes")
        if line_no is None or correct_hashes is None:
            continue
        idx = int(line_no) - 1
        if idx < 0 or idx >= len(lines):
            continue
        # Only apply if heading level actually changes
        m = _EXISTING_HEADING_RE.match(lines[idx].rstrip())
        if m and len(m.group(1)) != correct_hashes:
            remap_map[idx] = correct_hashes
            n_remapped += 1

    # --- Build output ---
    out_lines: list = []
    for i, line in enumerate(lines):
        # Apply heading remap first (replace existing heading level)
        if i in remap_map:
            m = _EXISTING_HEADING_RE.match(line.rstrip())
            if m:
                new_hashes = min(max(remap_map[i], 1), 6)
                line = "#" * new_hashes + " " + m.group(2) + ("\n" if line.endswith("\n") else "")

        # Insert new headings before this line
        headings = insert_map.get(i)
        if headings:
            if out_lines and out_lines[-1].strip() != "":
                out_lines.append("")
            for h in headings:
                out_lines.append(h)
            out_lines.append("")

        out_lines.append(line.rstrip("\n"))

    tagged = "\n".join(out_lines)
    if source_text.endswith("\n"):
        tagged += "\n"

    _verify_prose_unchanged(source_text, tagged)

    n_inserted = sum(len(v) for v in insert_map.values())
    return tagged, n_inserted, n_remapped


# ------------------------------------------------------------------------------
# Vault-root detection (same as extract_toc_tree.py)
# ------------------------------------------------------------------------------
def find_vault_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "4-SYSTEM").is_dir():
            return parent
    return start.parent if start.is_file() else start


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Ingest a TOC tree into a Tibetan commentary using Gemini.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--tree", required=True,
                        help="Path to the toc-tree-<id>.md file from extract_toc_tree.py")
    parser.add_argument("--input", required=True,
                        help="Path to the source commentary .md file")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL,
                        help=f"Fallback model on 503/overloaded (default: {DEFAULT_FALLBACK_MODEL})")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE,
                        help=f"Commentary lines per Gemini chunk (default: {DEFAULT_CHUNK_SIZE})")
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP,
                        help=f"Overlap lines between chunks (default: {DEFAULT_OVERLAP})")
    parser.add_argument("--vault-root", default=None,
                        help="Vault root (dir containing 4-SYSTEM/). Default: auto-detect.")
    parser.add_argument("--annot", default=None,
                        help="Path for annotation JSON (default: <temp>/<input-stem>.annotation.json)")
    parser.add_argument("--out", default=None,
                        help="Output path for the final tagged commentary "
                             "(default: <vault>/0-INBOX/inline_toc_commentary/toc-<input-filename>)")
    parser.add_argument("--no-ai", action="store_true",
                        help="Locate sections by direct string search instead of Gemini "
                             "(fast, no API calls, no API key needed)")
    parser.add_argument("--no-locate", action="store_true",
                        help="Skip location pass entirely; use existing --annot file")
    parser.add_argument("--no-render", action="store_true",
                        help="Stop after writing annotation; skip Gemini render")
    parser.add_argument("--force", action="store_true",
                        help="Re-run location even if annotation exists")
    parser.add_argument("--dry-run", action="store_true",
                        help="Parse and plan but make no API calls and write no files")
    args = parser.parse_args()

    tree_path = Path(args.tree).expanduser().resolve()
    input_path = Path(args.input).expanduser().resolve()

    if not tree_path.exists():
        sys.exit(f"Error: tree file not found: {tree_path}")
    if not input_path.exists():
        sys.exit(f"Error: commentary file not found: {input_path}")

    vault_root = Path(args.vault_root).resolve() if args.vault_root \
        else find_vault_root(input_path)

    temp_dir = vault_root / TEMP_SUBDIR
    temp_dir.mkdir(parents=True, exist_ok=True)

    annot_path = Path(args.annot).resolve() if args.annot \
        else temp_dir / f"{input_path.stem}.annotation.json"

    out_dir = vault_root / OUT_SUBDIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out).resolve() if args.out \
        else out_dir / f"toc-{input_path.name}"

    tree_text = tree_path.read_text(encoding="utf-8")
    nodes = parse_toc_tree(tree_text)
    if not nodes:
        sys.exit("Error: no TOC nodes found in tree file.")

    lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)

    print(f"Tree:         {tree_path}")
    print(f"Commentary:   {input_path} ({len(lines)} lines)")
    print(f"TOC nodes:    {len(nodes)}")
    if not args.no_ai:
        print(f"Model:        {args.model}")
    print(f"Annotation:   {annot_path}")
    print(f"Output:       {out_path}")
    print()

    if args.dry_run:
        print("Dry run — no API calls or file writes.")
        for n in nodes[:5]:
            print(f"  {n['decimal']:12s}  depth={n['depth']}  {n['title'][:60]}")
        return

    located: dict = {}

    if args.no_locate:
        if not annot_path.exists():
            sys.exit(f"Error: --no-locate given but annotation not found: {annot_path}")
        existing = json.loads(annot_path.read_text(encoding="utf-8"))
        print(f"Loading existing annotation ({len(existing.get('sections', []))} sections)")

    elif args.no_ai:
        print("Phase 1 — locating section boundaries by string search (no AI):")
        located = locate_sections_no_ai(nodes, lines)
        annotation = build_annotation(nodes, located)
        annotation["source_file"] = str(input_path)
        annot_path.write_text(json.dumps(annotation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n✓ Annotation written: {annot_path}")
        print(f"  {len(annotation['sections'])} sections annotated out of {len(nodes)} TOC nodes")

    else:
        decimal_set = {n["decimal"] for n in nodes}
        pending = list(nodes)
        print("Phase 1 — locating section boundaries via Gemini:")
        chunks = list(make_chunks(lines, args.chunk_size, args.overlap))
        print(f"  {len(chunks)} chunks (size={args.chunk_size}, overlap={args.overlap})\n")
        client = get_client()

        for chunk_idx, (start_line, end_line, chunk_text) in enumerate(chunks):
            still_pending = [n for n in pending if n["decimal"] not in located]
            if not still_pending:
                print(f"  All {len(nodes)} nodes located — stopping early.")
                break
            print(f"  chunk {chunk_idx+1}/{len(chunks)} (lines {start_line}\u2013{end_line}) | {len(still_pending)} pending  \u2192 Gemini ...", flush=True)
            results = locate_sections_in_chunk(client, args.model, chunk_text, start_line, end_line, still_pending, fallback_model=args.fallback_model)
            found_in_chunk = 0
            for r in results:
                dec = r.get("decimal", "").strip()
                if dec in decimal_set and dec not in located:
                    located[dec] = r
                    found_in_chunk += 1
            print(f"    \u2192 {found_in_chunk} section(s) located ({len(located)}/{len(nodes)} total)")

        not_found = [n["decimal"] for n in nodes if n["decimal"] not in located]
        if not_found:
            print(f"\n  Warning: {len(not_found)} node(s) not located:")
            for dec in not_found[:10]:
                node = next(n for n in nodes if n["decimal"] == dec)
                print(f"    {dec}  {node['title'][:60]}")
            if len(not_found) > 10:
                print(f"    ... and {len(not_found) - 10} more")

        annotation = build_annotation(nodes, located)
        annotation["source_file"] = str(input_path)
        annot_path.write_text(json.dumps(annotation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n\u2713 Annotation written: {annot_path}")
        print(f"  {len(annotation['sections'])} sections annotated out of {len(nodes)} TOC nodes")

    if args.no_render:
        print("\nStopping before render (--no-render).")
        return

    print(f"\nPhase 2 \u2014 injecting TOC via Gemini ...")
    source_text = input_path.read_text(encoding="utf-8")
    annotation = json.loads(annot_path.read_text(encoding="utf-8"))
    client = get_client()
    try:
        tagged, n_inserted, n_remapped = gemini_inject_toc(
            client, args.model, source_text, annotation, nodes,
            fallback_model=args.fallback_model,
        )
    except TagError as e:
        print(f"\nERROR: {e}", file=sys.stderr)
        sys.exit(1)

    out_path.write_text(tagged, encoding="utf-8")

    print(f"\n\u2713 Done.")
    print(f"  Annotation:          {annot_path}")
    print(f"  Output:              {out_path}")
    print(f"  Headings inserted:   {n_inserted}")
    print(f"  Headings remapped:   {n_remapped}")
    print(f"  Prose integrity:     VERIFIED")


if __name__ == "__main__":
    main()
