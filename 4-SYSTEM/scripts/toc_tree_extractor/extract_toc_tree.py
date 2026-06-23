#!/usr/bin/env python3
"""
extract_toc_tree.py — ས་བཅད (sa bcad) structural-outline candidate extraction
using Google Gemini Flash.

This is a runnable version of the `toc-candidate-extraction` skill
(4-SYSTEM/Skills/toc-candidate-extraction). It does the whole pipeline end to end:

    1. Chunk the input file into overlapping line windows.
    2. Send each chunk to Gemini with the sa-bcad extraction prompt.
    3. Save one result file per chunk under
       0-INBOX/temp/TOC-<commentary-id>/candidates/ (resumable). A second pass copies the
       raw enumeration blocks to 0-INBOX/temp/TOC-<commentary-id>/enumerations/.
    4. Combine all chunk results into 0-INBOX/toc-candidates-<commentary-id>.md.
    5. Send the merged candidates back to Gemini and build a full nested,
       decimal-numbered TOC tree (no ^toc block IDs) saved to
       0-INBOX/toc-tree-<commentary-id>.md, then QC it.  (skip tree with --no-tree)

The extraction step prioritises RECALL: it is better to extract too many
candidates than to miss one.

--------------------------------------------------------------------------------
Setup
--------------------------------------------------------------------------------
    pip install google-genai
    set GEMINI_API_KEY=...        (Windows)   /   export GEMINI_API_KEY=...  (mac/Linux)

--------------------------------------------------------------------------------
Usage
--------------------------------------------------------------------------------
    python 4-SYSTEM/scripts/extract_toc_tree.py <input_file> [options]

    # commentary-id is inferred from the filename if not given:
    python 4-SYSTEM/scripts/extract_toc_tree.py 1-SOURCES/Commentaries/bo-kunpal.md

    # explicit id, custom chunking:
    python 4-SYSTEM/scripts/extract_toc_tree.py input.md \
        --commentary-id kunpal --chunk-size 150 --overlap 25

    # re-run: existing chunk result files are skipped automatically, so an
    # interrupted run resumes from the first missing chunk. Use --force to redo all.

Run with --help for the full option list.
"""

import argparse
import os
import random
import re
import sys
import time
from datetime import date
from pathlib import Path

# ------------------------------------------------------------------------------
# Defaults
# ------------------------------------------------------------------------------
DEFAULT_MODEL = "gemini-flash-latest"
# Used automatically when the primary model keeps returning 503/overloaded after all
# retries. Set to "" (or pass --fallback-model "") to disable fallback.
DEFAULT_FALLBACK_MODEL = "gemini-3-flash-preview"
DEFAULT_CHUNK_SIZE = 150
DEFAULT_OVERLAP = 25
MAX_RETRIES = 8
RETRY_BACKOFF_SECONDS = 8       # base; backoff grows exponentially per attempt
MAX_BACKOFF_SECONDS = 120       # cap on a single wait

# Where outputs go, relative to the vault root (the dir that contains 4-SYSTEM/).
# Both per-chunk staging folders live together under one TOC-<name> folder in temp:
#   0-INBOX/temp/TOC-<commentary-id>/candidates/   and   .../enumerations/
TEMP_BASE_SUBDIR = "0-INBOX/temp"     # the TOC-<name> folder is created under here
CANDIDATES_DIRNAME = "candidates"     # per-chunk section-candidate staging
ENUM_DIRNAME = "enumerations"         # per-chunk raw enumeration blocks (one file/chunk)
FINAL_SUBDIR = "0-INBOX"


# ------------------------------------------------------------------------------
# The extraction prompt — lifted from the toc-candidate-extraction SKILL.md
# ------------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist texts specialising in ས་བཅད (sa bcad) — \
the structural outlining system used in Tibetan commentarial literature.

Your task is to extract the ས་བཅད SECTION TITLES from the input text chunk — the
genuine structural divisions of the text, NOT every number, list, or ordinal you see.

Balance recall and precision. Extract a candidate only when it truly marks a structural
section: a division being announced, a header opening a section, or a closing count that
defines a structural division. Capture every real section, but when you are not confident
that something is a structural section rather than incidental text, LEAVE IT OUT. A clean
list of real sections is worth more than an exhaustive list full of false positives.

THREE SECTION TYPES — extract all three independently:

Type A — Announcement
A passage where the author declares a division: a topic is split into N named parts.
  e.g. དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།

Type B — Node header
A short label opening a section, signalling "now treating part N."
  e.g. གཉིས་པ་འགྱུར་ཕྱག་ནི།

Type C — Closing count
A number word appearing after a list, summarising how many items were just given.
  e.g. ཞེས་རྣམ་པ་གསུམ་མོ། / གནས་བརྒྱད་དོ། / ཚུལ་བཞི་པོ་དེ་དག

RECOGNITION — meaning first, markers second.
Do not pattern-match on surface markers alone. For each passage ask: is this text
dividing a topic into named parts, labelling a sub-section, or counting items just
listed? If yes — regardless of exact wording — extract it.

Common signals — any one is enough:
- Topic announced then split into named sub-parts
- Ordinal labels: དང་པོ། / གཉིས་པ། / གསུམ་པ། (even scattered across paragraphs)
- Division words: སྟེ། / ལ། / དབྱེ་ན། following a topic heading
- Number word near a list of named items
- Verse listing items that prose then unpacks
- ལ་སོགས་པ། closing a partial list with a nearby number
- རྣམ་པ་ / གནས་ / ཚུལ་ / ཞེས་བྱ་བ་ within 30 words of a number

CAPTURE THESE (genuine sections):
- དང་པོ་ / གཉིས་པ་ / གསུམ་པ་ labels that open a structural section
- Announcements that divide a topic into named structural sub-parts
- Closing counts that define a structural division
- Nested sections — extract both inner and outer separately
- Sections in the overlap zone — extract once only

DO NOT EXTRACT (common false positives — these are NOT sections):
- Numbers that are part of the doctrinal content itself (enumerations of qualities,
  attributes, dimensions, or quantities being explained — not the text's own outline)
- Numerals inside quotations, citations, folio/page references, dates, or mantra counts
- Ordinal-looking words used in ordinary prose rather than as section labels
- Counts summarising a list mentioned only in passing, with no structural role
- A section already extracted earlier in this same chunk (do not repeat it)
When unsure, omit it. Precision matters: do not pad the output with doubtful candidates.

OUTPUT FORMAT — for each section output EXACTLY this block, nothing more:

CONTEXT: [10 Tibetan words before + 10 Tibetan words after the section]
SECTION_TITLE: [the section ordinal marker TOGETHER WITH the section's topic name, but
WITHOUT any trailing division clause or grammatical particle. Strip the "divided into N"
phrase (e.g. ལ་གཉིས་ཏེ། , ལ་གསུམ་ལས། , ལ་བཞི། ) and trailing markers such as ནི། and the
closing shad །. Keep the ordinal; keep the topic words; drop only the trailing
particle / division phrase. Examples:
    དང་པོ་ལ་གཉིས་ཏེ།      ->  དང་པོ་
    གཉིས་པ་འགྱུར་ཕྱག་ནི།   ->  གཉིས་པ་འགྱུར་ཕྱག་
    གསུམ་པ་མཚན་དོན་ནི།     ->  གསུམ་པ་མཚན་དོན་]
ITEMS:
1. [first named item, in Tibetan]
2. [second named item, in Tibetan]

No commentary. No analysis. No linking. List each named item on its own line under
ITEMS:, numbered 1., 2., 3., ... If items cannot be determined, write "ITEMS:" on its
own line followed by a single line "[implicit]". Separate section blocks with a single
blank line. If the chunk contains NO sections at all, output exactly: NO CANDIDATES
"""

USER_PROMPT_TEMPLATE = """\
Extract the ས་བཅད section titles from the following text chunk. Output only the section \
blocks in the required format. Omit doubtful candidates that are not genuine sections.

--- BEGIN CHUNK ---
{chunk_text}
--- END CHUNK ---
"""


# ------------------------------------------------------------------------------
# The enumeration prompt — SECOND, independent pass. Copies out the author's own
# division announcements VERBATIM, with no interpretation (no PARENT/COUNT/ITEMS).
# ------------------------------------------------------------------------------
ENUM_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist ས་བཅད (sa bcad) structural outlines.

Your task is to COPY OUT, VERBATIM, the passages of the chunk that ANNOUNCE structural
divisions — the sentences where the author divides a topic into a stated number of named
parts (e.g. "...ལེའུ་བཅུ་ཡོད་པ་ལས།", "...ལ་གཉིས་ཏེ། X དང་། Y'འོ། །", "...ལ་གསུམ་ལས།").
These announcement passages are the text's OWN enumeration of its structure.

RULES:
- Copy the Tibetan EXACTLY as it appears in the source. Do NOT paraphrase, translate,
  summarise, renumber, reorder, or add any interpretation, labels, or commentary.
- Group CONSECUTIVE announcement sentences — a cascade of nested divisions with no
  intervening explanatory prose — into ONE block, preserving their order and line breaks.
- Start a NEW block whenever a run of announcements is separated from the next run by
  intervening commentary / explanatory text.
- Include ONLY the announcement sentences themselves, not the surrounding commentary.

OUTPUT EXACTLY in this shape, and nothing else:

Enumeration Block 1:
<verbatim Tibetan announcement line(s) of the first block>
Enumeration Block 2:
<verbatim Tibetan announcement line(s) of the second block>

The label "Enumeration Block N:" is the ONLY text you add; everything under it is copied
verbatim. If the chunk contains NO division announcements at all, output exactly:
NO ENUMERATIONS
"""

ENUM_USER_PROMPT_TEMPLATE = """\
Copy out, verbatim, every ས་བཅད division-announcement passage from the following text \
chunk, grouped and labelled as required. Output only the enumeration blocks.

--- BEGIN CHUNK ---
{chunk_text}
--- END CHUNK ---
"""


# ------------------------------------------------------------------------------
# The tree-building prompt — converts the merged candidates into a nested,
# decimal-numbered TOC tree (matches the `add-toc` skill conventions).
# ------------------------------------------------------------------------------
TREE_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist ས་བཅད (sa bcad) structural outlines.

You are given TWO inputs from a single commentary, in document order.

INPUT 1 — CANDIDATES: extracted section headers. Each block looks like:

    CONTEXT: <surrounding Tibetan>
    SECTION_TITLE: <ordinal + topic name, trailing particle/division phrase stripped,
                    e.g. གཉིས་པ་འགྱུར་ཕྱག་>
    ITEMS:
    1. <first named sub-part>
    2. <second named sub-part>
    (ITEMS may be a single line "[implicit]" when sub-parts are not stated)

INPUT 2 — ENUMERATIONS: the author's division announcements, copied VERBATIM from the
source (no interpretation). They are grouped into blocks like:

    Enumeration Block 1:
    <verbatim Tibetan: "...ལེའུ་བཅུ་ཡོད་པ་ལས།  དང་པོ་ལ་གསུམ་ལས། X དང་། Y དང་། Z ...">
    Enumeration Block 2:
    <verbatim Tibetan announcement passage>

Read each block to recover, for every announcement: the parent being divided, the
declared count, and the named parts. The ENUMERATIONS are the author's own skeleton of
the text and are MORE AUTHORITATIVE than individual candidates. Use them two ways:

A. ELIMINATE FALSE POSITIVES — a CANDIDATE section that matches no part named in any
   enumeration, and is not itself the parent of a declared division, is suspect. Drop it
   from the tree unless its ordinal sequence clearly makes it a real sibling. Do not let
   stray numbers or incidental ordinals become nodes.

B. FILL GAPS — but ONLY for STRUCTURAL divisions. Every part of a genuine sa-bcad
   division MUST appear as a child node of its parent; if such a part has no matching
   candidate section, insert it (using the part's title text). The number of children
   under a structural parent must match the count its announcement declared. Do NOT add
   any marker to inserted nodes — they look like every other entry.

   NOT EVERY ENUMERATION IS PART OF THE INLINE TOC. The enumerations file also contains
   DOCTRINAL / CONTENT lists — items enumerated as subject matter being explained, not as
   structural divisions of the text. These must NOT be added to the tree. A list is part
   of the inline TOC (and may seed nodes) ONLY when its parts are subsequently OPENED as
   their own sections — i.e. each part later recurs as an ordinal-led node header
   (དང་པོ་... ནི། / གཉིས་པ་... ལ་... etc.) that the commentary then treats in turn.
   Signs a list is CONTENT, not structure — do NOT make it into nodes:
     - the items are never re-opened later as their own ordinal-led sections
     - it enumerates doctrinal categories, qualities, examples, or stages as the topic
       being discussed (e.g. a list of qualities, perfections, signs) rather than dividing
       the text
     - it sits inside the explanation of a single leaf section without subdividing it
   When in doubt, require corroboration: add a missing node only if the part's absence
   breaks an otherwise-confirmed structural division (some siblings DO appear as real
   headers). Do not expand a content list into a branch of the tree.

MATCHING — names are often WORDED DIFFERENTLY where a part is first declared (in the
enumeration) and where its section actually opens (the node header). Match by MEANING and
shared core content words, NOT by exact string equality. Treat two names as the SAME
section when one is clearly a fuller, shorter, or lightly reworded form of the other:
   - inserted / dropped qualifiers or adverbs (ཅུང་ཟད་ "briefly", མདོ་ཙམ་, རྒྱས་པར་, ...)
   - synonymous verbs or near-synonyms (བསྒྱུར་བ་ ~ བཤད་པ་), added/removed ནི། པ་ པོ་ འོ།
   - abbreviation vs. full phrase, or a different but equivalent ordinal/particle
   Example — these are the SAME section, do NOT treat as a gap or duplicate:
     enumeration part:  ...མཚན་དོན་བཤད་པའོ། །
     node header:       གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་ལ་གཉིས་ཏེ།
   Use the node header's ORDINAL together with the fuzzy name to align it to the right
   part: a node opening with གཉིས་པ་ is the 2nd declared part of its parent even if its
   wording differs (above, གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ aligns to the parent's 2nd part
   མཚན་དོན་བཤད་པ). When a part and a node match this way, use them as ONE node (prefer the
   node header's wording for the display text) and do NOT create a duplicate sibling.
   Insert a part as a new node only when NO candidate plausibly corresponds to it.
   Likewise, do not split one real section into two because its name varies.

   ALWAYS KEEP THE NODE-TITLE ORDINAL: every node's display text must begin with the
   Tibetan ordinal (དང་པོ་ , གཉིས་པ་ , གསུམ་པ་ ...) exactly as it appears in the node
   header — even when the enumeration's wording of that part has NO ordinal. If the node
   header carries an ordinal, include it; never drop it just because the enumeration
   listed the part without one. But never FABRICATE an ordinal: if NEITHER the node header
   NOR the enumeration part has a Tibetan number, the display text has none (the decimal
   numbering still applies).

Your task: reconstruct the FULL hierarchical table of contents (dkar-chag) as a
single nested tree, reconciled against the enumerations, and emit it with hierarchical
decimal numbering.

HOW TO INFER HIERARCHY (read the Tibetan, do not guess from candidate order alone):

1. Ordinal prefixes mark sibling rank within one parent's enumeration:
   དང་པོ་=1, གཉིས་པ་=2, གསུམ་པ་=3, བཞི་པ་=4, ལྔ་པ་=5, དྲུག་པ་=6, བདུན་པ་=7, ...
   Bracket/parenthetical markers (༡༽, ༢༽, ཀ༽, ཁ༽) follow the same logic.
   A series restarts when a new parent is introduced.

2. An "announcement" candidate that introduces sub-items (ends in a count such as
   གཉིས་ཏེ། / གསུམ་སྟེ། / བཞི་ལས། / ...ལ།) is a PARENT. Its named ITEMS become its
   direct children, one level deeper. Each child that is itself later announced and
   subdivided becomes a parent in turn — match a child to the announcement that
   re-states and divides it.

3. When a peer ordinal reappears (e.g. གཉིས་པ་ after a run of children), return to
   the depth of the matching དང་པོ་ that opened that sibling series.

4. A short candidate that merely names one element of an enumeration (no trailing
   count phrase) is a leaf at its depth.

CLEAN each display string:
   - KEEP the leading Tibetan ordinal prefix (དང་པོ་ , གཉིས་པ་ , གསུམ་པ་ , ...) at the
     START of the display text when the node header or the enumeration part HAS one — it
     must agree with the decimal's last segment and is used for quality-checking, so do NOT
     strip it. But do NOT INVENT an ordinal: if neither the node header nor the enumeration
     part carries a Tibetan ordinal, leave the text without one (the decimal still numbers it).
   - strip leading bullets, bracket markers (༡༽ ཀ༽ ...), and Tibetan decimal labels
   - strip trailing block IDs (^...) and wiki-link wrappers ([[#^id|text]] -> text)
   - KEEP ONLY THE TITLE. Strip everything after the topic name: the division clause that
     announces sub-parts (ལ་གཉིས་ཏེ། / ལ་གསུམ་ལས། / ལ་བཞི། / ...སྟེ། / ...ལས།) and trailing
     grammatical particles / connectives (ནི། / ནི / ལ། / འོ། / པོ། / སྟེ། / དང་). Examples:
       གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་ལ་གཉིས་ཏེ།  ->  གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་
       དང་པོ་བྱང་ཆུབ་སེམས་བསྐྱེད་ཀྱི་རྟེན་ནི།        ->  དང་པོ་བྱང་ཆུབ་སེམས་བསྐྱེད་ཀྱི་རྟེན་
   - strip any trailing shad (།, །།, ལོ།) — do NOT add a ། at the end of entries
   - keep the full descriptive topic phrase otherwise — do not over-truncate the title

OUTPUT — emit ONLY the TOC block, exactly in this shape and nothing else:

## དཀར་ཆག / Table of Contents

* 1. <clean text>
   * 1.1 <clean text>
      * 1.1.1 <clean text>
   * 1.2 <clean text>
* 2. <clean text>

---

FORMAT RULES (follow exactly):
   - indent = 3 spaces × (depth − 1); depth-1 items have no indent
   - decimal = 1. for depth-1, 1.1 for depth-2, 1.1.1 for depth-3, etc.
   - do NOT emit ^toc block IDs — the decimal numbering alone identifies each entry
   - when an entry's text carries a Tibetan ordinal it MUST equal the decimal's last
     segment (གསུམ་པ་ -> ...3 ; གཉིས་པ་ -> ...2); never let them disagree. Do not add a
     Tibetan ordinal that is absent from both the node header and the enumeration.
   - one entry per line, no blank lines between entries
   - counters reset for deeper levels whenever you move up to a shallower level
   - cover the whole document; do not drop branches. Output Tibetan, no English,
     no commentary, no code fences.
   - each entry is the TITLE ONLY (ordinal + topic name); no trailing particle, no ། , no
     ⟨gap⟩ or any other marker on any entry.
"""

TREE_USER_PROMPT_TEMPLATE = """\
Build the full nested decimal-numbered table of contents for commentary \
"{commentary_id}" from the candidates below, reconciled against the enumerations \
(use them to drop false-positive candidates and to fill/flag gaps). Output only the \
TOC block.

--- BEGIN CANDIDATES ---
{candidates_text}
--- END CANDIDATES ---

--- BEGIN ENUMERATIONS ---
{enumerations_text}
--- END ENUMERATIONS ---
"""


# ------------------------------------------------------------------------------
# The QC-repair prompt — fixes numbering/structure issues found by the deterministic
# checker, guided by the explicit issue list.
# ------------------------------------------------------------------------------
QC_SYSTEM_PROMPT = """\
You are an expert in classical Tibetan Buddhist ས་བཅད (sa bcad) TOC trees. You are given a
decimal-numbered TOC tree, a list of QC ISSUES found by an automated checker, the author's
VERBATIM ENUMERATION BLOCKS (the sa-bcad division announcements), and the SECTION
CANDIDATES (the section headers extracted from the text). Produce a CORRECTED tree.

The QC pass FOCUSES ON THREE THINGS — do these and little else:

1. NUMBERING vs TIBETAN ORDINALS — make the decimal numbering agree with the Tibetan
   ordinal at the start of each node's text (དང་པོ་=1, གཉིས་པ་=2, གསུམ་པ་=3, བཞི་པ་=4,
   ལྔ་པ་=5, དྲུག་པ་=6, བདུན་པ་=7, བརྒྱད་པ་=8, དགུ་པ་=9, བཅུ་པ་=10, ...). The Tibetan
   ordinal is AUTHORITATIVE for a node's position: when the decimal's last segment differs
   from the ordinal, fix the DECIMAL (not the ordinal), then renumber the siblings around it
   and cascade the corrected numbers into all descendants.

2. NO GAPS — every parent's children must run 1, 2, 3 … with NO missing number and NO
   duplicate, and the count must match the number of parts its enumeration declared. If a
   declared child is missing from the tree, FIRST look for it among the SECTION CANDIDATES
   (it may be present under a slightly different wording that was not matched — match by
   meaning, see below) and insert that real node; only if no candidate corresponds, insert
   the enumerated part as a normal node (NO marker). If any entry still carries a "⟨gap⟩"
   marker from a previous run, REMOVE the marker — the final tree must contain no ⟨gap⟩ tags.

3. RECONCILE BOTH SOURCES — fix every issue by checking the tree against BOTH the
   enumerations (what the author declared: parents, counts, ordered parts) AND the section
   candidates (what was actually found in the text). Match names by MEANING and shared core
   words, not exact strings (inserted/dropped qualifiers like ཅུང་ཟད་, near-synonym verbs,
   added/removed ནི། པ་ འོ།). Do not duplicate a node that already exists under a varied name.

ALSO tidy: indentation must be 3 spaces × (depth − 1); remove duplicate decimals; repair
malformed lines. Each entry must be the TITLE ONLY — strip any trailing division clause
(ལ་གཉིས་ཏེ། ...) or particle (ནི། ལ། འོ། ...) and any trailing ། from every entry. Do NOT
add ^toc block IDs.

DO NOT: reorder or reword the topic of existing real nodes; change Tibetan text; turn
doctrinal/content lists into nodes; or INVENT a Tibetan ordinal where neither the node nor
the enumeration has one.

OUTPUT ONLY the corrected tree block, in the exact same shape as the input (starting with
"## དཀར་ཆག / Table of Contents"), no commentary, no code fences.
"""

QC_USER_PROMPT_TEMPLATE = """\
Correct the following TOC tree for commentary "{commentary_id}", fixing every listed issue
by checking the tree against BOTH the enumeration blocks and the section candidates. Output
only the corrected tree.

--- BEGIN ISSUES ---
{issues_text}
--- END ISSUES ---

--- BEGIN ENUMERATIONS ---
{enumerations_text}
--- END ENUMERATIONS ---

--- BEGIN SECTION CANDIDATES ---
{candidates_text}
--- END SECTION CANDIDATES ---

--- BEGIN TREE ---
{tree_text}
--- END TREE ---
"""


# ------------------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------------------
def make_chunks(lines, chunk_size, overlap):
    """Return a list of (index, start_line, end_line, text) tuples (1-based line numbers)."""
    total = len(lines)
    chunks = []
    start = 0
    idx = 0
    while start < total:
        end = min(start + chunk_size, total)
        text = "".join(lines[start:end])
        chunks.append((idx, start + 1, end, text))
        idx += 1
        if end >= total:
            break
        start = end - overlap
    return chunks


# ------------------------------------------------------------------------------
# Gemini call
# ------------------------------------------------------------------------------
def get_client():
    try:
        from google import genai  # type: ignore
    except ImportError:
        sys.exit(
            "Error: google-genai is not installed.\n"
            "  Install it with:  pip install google-genai"
        )

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit(
            "Error: no API key found.\n"
            "  Set the GEMINI_API_KEY environment variable to your Gemini API key."
        )
    return genai.Client(api_key=api_key)


def _is_overloaded(err) -> bool:
    """True if the error looks like a transient capacity problem worth a fallback model."""
    s = str(err).upper()
    return any(tok in s for tok in (
        "503", "UNAVAILABLE", "OVERLOADED", "HIGH DEMAND",
        "429", "RESOURCE_EXHAUSTED",
    ))


def _generate(client, model, system_prompt, contents, fallback_model="", label="chunk"):
    """Call Gemini with exponential backoff + jitter, plus an optional fallback model.

    On a persistent 503/overloaded condition the primary model's retries are exhausted
    and we switch to `fallback_model` (if given). Non-capacity errors are not retried
    against the fallback.
    """
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
            print(f"    -> '{model}' still overloaded; falling back to '{mdl}'",
                  file=sys.stderr)
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = client.models.generate_content(
                    model=mdl, contents=contents, config=config,
                )
                return (resp.text or "").strip()
            except Exception as e:  # noqa: BLE001 - surface any API/transport error
                last_err = e
                if attempt < MAX_RETRIES:
                    base = min(RETRY_BACKOFF_SECONDS * (2 ** (attempt - 1)),
                               MAX_BACKOFF_SECONDS)
                    wait = base + random.uniform(0, base * 0.25)
                    kind = "overloaded (503/429)" if _is_overloaded(e) else "error"
                    print(f"    ! {label} attempt {attempt}/{MAX_RETRIES} {kind}: {e}; "
                          f"retrying in {wait:.0f}s...", file=sys.stderr)
                    time.sleep(wait)
        # Retries exhausted for this model. Only try the fallback if it was a
        # capacity problem; a genuine error would just fail again.
        if not _is_overloaded(last_err):
            break
    raise RuntimeError(f"Gemini call failed after retries on "
                       f"{models_to_try}: {last_err}")


def extract_from_chunk(client, model, chunk_text, fallback_model=""):
    """Pass 1 — section candidates. Returns the model's text (CONTEXT/SECTION_TITLE/ITEMS)."""
    contents = USER_PROMPT_TEMPLATE.format(chunk_text=chunk_text)
    return _generate(client, model, SYSTEM_PROMPT, contents,
                     fallback_model=fallback_model, label="chunk")


def extract_enumerations_from_chunk(client, model, chunk_text, fallback_model=""):
    """Pass 2 — raw enumeration blocks, copied verbatim (no interpretation)."""
    contents = ENUM_USER_PROMPT_TEMPLATE.format(chunk_text=chunk_text)
    return _generate(client, model, ENUM_SYSTEM_PROMPT, contents,
                     fallback_model=fallback_model, label="enum")


def build_toc_tree(client, model, commentary_id, candidates_text,
                   enumerations_text="", fallback_model=""):
    """Single Gemini call: turn candidates + enumerations into a nested TOC tree."""
    contents = TREE_USER_PROMPT_TEMPLATE.format(
        commentary_id=commentary_id,
        candidates_text=candidates_text,
        enumerations_text=enumerations_text or "(none extracted)",
    )
    text = _generate(client, model, TREE_SYSTEM_PROMPT, contents,
                     fallback_model=fallback_model, label="tree")
    # defensively strip any stray code fences
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n?```$", "", text)
    return text.strip()


def repair_tree(client, model, commentary_id, tree_text, issues_text,
                enumerations_text="", candidates_text="", fallback_model=""):
    """QC-repair pass: fix flagged issues using BOTH enumerations and section candidates."""
    contents = QC_USER_PROMPT_TEMPLATE.format(
        commentary_id=commentary_id,
        issues_text=issues_text or "(none)",
        enumerations_text=enumerations_text or "(none extracted)",
        candidates_text=candidates_text or "(none extracted)",
        tree_text=tree_text,
    )
    text = _generate(client, model, QC_SYSTEM_PROMPT, contents,
                     fallback_model=fallback_model, label="qc")
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
    text = re.sub(r"\n?```$", "", text)
    return text.strip()


# ------------------------------------------------------------------------------
# Deterministic TOC-tree QC checker (no API calls)
# ------------------------------------------------------------------------------
# Tibetan ordinals -> integer, longest forms first so e.g. བཅུ་གཅིག་པ matches before བཅུ་པ.
_TIB_ORDINALS = [
    ("བཅུ་གསུམ་པ", 13), ("བཅུ་གཉིས་པ", 12), ("བཅུ་གཅིག་པ", 11),
    ("དང་པོ", 1), ("གཉིས་པ", 2), ("གསུམ་པ", 3), ("བཞི་པ", 4), ("ལྔ་པ", 5),
    ("དྲུག་པ", 6), ("བདུན་པ", 7), ("བརྒྱད་པ", 8), ("དགུ་པ", 9), ("བཅུ་པ", 10),
]
_TREE_LINE_RE = re.compile(
    r"^(?P<indent>\s*)\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+"
    r"(?P<text>.*?)(?:\s*\^toc-[\d-]+)?\s*$"
)


def _leading_tibetan_ordinal(text: str):
    """Return the integer value of the leading Tibetan ordinal, or None."""
    t = text.lstrip(" *#\t")
    for word, num in _TIB_ORDINALS:
        if t.startswith(word):
            return num
    return None


def qc_check_tree(tree_text: str):
    """Return a list of human-readable QC issue strings for a TOC tree (deterministic)."""
    issues = []
    seen = {}
    parsed = []  # (lineno, segs_tuple)
    for lineno, raw in enumerate(tree_text.splitlines(), 1):
        if not re.match(r"^\s*\*\s", raw):
            continue  # not a tree entry (header, ---, blank, etc.)
        m = _TREE_LINE_RE.match(raw)
        if not m:
            issues.append(f"L{lineno}: unparseable tree line: {raw.strip()}")
            continue
        dec = m.group("dec")
        text = m.group("text").strip()
        indent = len(m.group("indent").replace("\t", "   "))
        segs = dec.split(".")
        depth = len(segs)
        last = int(segs[-1])

        if indent != 3 * (depth - 1):
            issues.append(f"L{lineno}: indent {indent} spaces != expected "
                          f"{3 * (depth - 1)} for depth {depth} ({dec})")
        ordn = _leading_tibetan_ordinal(text)
        if ordn is not None and ordn != last:
            issues.append(f"L{lineno}: Tibetan ordinal = {ordn} but decimal last "
                          f"segment = {last}  ->  {dec} {text[:40]}")
        if dec in seen:
            issues.append(f"L{lineno}: duplicate decimal {dec} (also at L{seen[dec]})")
        else:
            seen[dec] = lineno
        parsed.append((lineno, tuple(int(s) for s in segs)))

    # sibling-sequence check: each parent's children must be 1..n with no gaps/dups
    children = {}
    for lineno, segs in parsed:
        children.setdefault(segs[:-1], []).append(segs[-1])
    for parent, nums in children.items():
        expected = list(range(1, len(nums) + 1))
        if sorted(nums) != expected:
            pid = ".".join(map(str, parent)) or "(root)"
            issues.append(f"children of {pid}: numbered {sorted(nums)}, "
                          f"expected {expected}")
    return issues


# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
def find_vault_root(start: Path) -> Path:
    """Walk upward looking for the vault root (the dir containing 4-SYSTEM/)."""
    for parent in [start, *start.parents]:
        if (parent / "4-SYSTEM").is_dir():
            return parent
    # Fallback: save outputs alongside the input file (e.g. inside SANDBOX),
    # so the 0-INBOX/ subfolders land next to the source.
    return start.parent if start.is_file() else start


def infer_commentary_id(input_path: Path) -> str:
    stem = input_path.stem
    # strip a leading language tag like "bo-", "en-", "zh-"
    stem = re.sub(r"^(bo|en|zh|sk|pi|hi|ne|mn|ru)-", "", stem)
    # strip trailing helpers like "-toc", ".segmented"
    stem = re.sub(r"[-.](toc|segmented|raw)$", "", stem)
    return stem


def count_candidates(text: str) -> int:
    return len(re.findall(r"^\s*SECTION_TITLE:", text, flags=re.MULTILINE))


def count_enum_blocks(text: str) -> int:
    return len(re.findall(r"^\s*Enumeration Block\s+\d+:", text, flags=re.MULTILINE))


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Extract ས་བཅད (sa bcad) TOC candidates from Tibetan commentary "
                    "using Gemini Flash.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("input_file", help="Path to the input .md/.txt file")
    parser.add_argument("--commentary-id", default=None,
                        help="Short id for output paths (default: inferred from filename)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Gemini model (default: {DEFAULT_MODEL})")
    parser.add_argument("--fallback-model", default=DEFAULT_FALLBACK_MODEL,
                        help="Model to switch to when the primary keeps returning "
                             f"503/overloaded (default: {DEFAULT_FALLBACK_MODEL}). "
                             "Pass an empty string to disable fallback.")
    parser.add_argument("--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE,
                        help=f"Lines per chunk (default: {DEFAULT_CHUNK_SIZE})")
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP,
                        help=f"Overlap lines between chunks (default: {DEFAULT_OVERLAP})")
    parser.add_argument("--vault-root", default=None,
                        help="Vault root (dir containing 4-SYSTEM/). Default: auto-detect.")
    parser.add_argument("--temp-dir", default=None,
                        help="Override per-chunk section-candidate staging dir "
                             "(default: <root>/0-INBOX/temp/TOC-<commentary-id>/candidates/)")
    parser.add_argument("--out", default=None,
                        help="Override combined candidates file "
                             "(default: <root>/0-INBOX/toc-candidates-<commentary-id>.md)")
    parser.add_argument("--enum-dir", default=None,
                        help="Override the per-chunk enumerations folder "
                             "(default: <root>/0-INBOX/temp/TOC-<commentary-id>/enumerations/). "
                             "One file per chunk, raw verbatim enumeration blocks.")
    parser.add_argument("--tree-out", default=None,
                        help="Override TOC-tree output file "
                             "(default: <root>/0-INBOX/toc-tree-<commentary-id>.md)")
    parser.add_argument("--no-enum", action="store_true",
                        help="Skip the enumeration extraction pass (pass 2)")
    parser.add_argument("--no-tree", action="store_true",
                        help="Stop after merging candidates; skip the TOC-tree step")
    parser.add_argument("--qc-out", default=None,
                        help="Override the TOC-tree QC report file "
                             "(default: <root>/0-INBOX/toc-tree-qc-<commentary-id>.md)")
    parser.add_argument("--no-qc", action="store_true",
                        help="Skip the QC pass on the TOC tree")
    parser.add_argument("--no-qc-fix", action="store_true",
                        help="Run QC detection + report but do NOT LLM-repair the tree")
    parser.add_argument("--force", action="store_true",
                        help="Re-process all chunks even if result files already exist")
    parser.add_argument("--dry-run", action="store_true",
                        help="Chunk and set up paths but do NOT call Gemini")
    args = parser.parse_args()

    input_path = Path(args.input_file).expanduser().resolve()
    if not input_path.exists():
        sys.exit(f"Error: file not found: {input_path}")

    commentary_id = args.commentary_id or infer_commentary_id(input_path)
    vault_root = Path(args.vault_root).resolve() if args.vault_root else find_vault_root(input_path)

    toc_folder = vault_root / TEMP_BASE_SUBDIR / f"TOC-{commentary_id}"
    temp_dir = Path(args.temp_dir).resolve() if args.temp_dir \
        else toc_folder / CANDIDATES_DIRNAME
    out_file = Path(args.out).resolve() if args.out \
        else vault_root / FINAL_SUBDIR / f"toc-candidates-{commentary_id}.md"
    enum_dir = Path(args.enum_dir).resolve() if args.enum_dir \
        else toc_folder / ENUM_DIRNAME
    tree_file = Path(args.tree_out).resolve() if args.tree_out \
        else vault_root / FINAL_SUBDIR / f"toc-tree-{commentary_id}.md"
    qc_file = Path(args.qc_out).resolve() if args.qc_out \
        else vault_root / FINAL_SUBDIR / f"toc-tree-qc-{commentary_id}.md"

    temp_dir.mkdir(parents=True, exist_ok=True)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    if not args.no_enum:
        enum_dir.mkdir(parents=True, exist_ok=True)

    lines = input_path.read_text(encoding="utf-8").splitlines(keepends=True)
    chunks = make_chunks(lines, args.chunk_size, args.overlap)

    print(f"Input:        {input_path}")
    print(f"Commentary:   {commentary_id}")
    print(f"Lines:        {len(lines)}  ->  {len(chunks)} chunks "
          f"(size={args.chunk_size}, overlap={args.overlap})")
    print(f"Model:        {args.model}")
    print(f"Staging dir:  {temp_dir}")
    print(f"Candidates:   {out_file}")
    if not args.no_enum:
        print(f"Enum folder:  {enum_dir}  (one file per chunk)")
    if not args.no_tree:
        print(f"TOC tree:     {tree_file}")
    print()

    if args.dry_run:
        print("Dry run — no API calls made. Chunk plan:")
        for idx, start, end, _ in chunks:
            print(f"  chunk_{idx:03d}: lines {start}–{end}")
        return

    client = get_client()

    # ---- Step 3: PASS 1 — section candidates (resumable) ----
    print("Pass 1 — section candidates:")
    for idx, start, end, text in chunks:
        chunk_out = temp_dir / f"chunk_{idx:03d}.md"
        if chunk_out.exists() and not args.force:
            print(f"  chunk_{idx:03d} (lines {start}–{end})  [skip — exists]")
            continue

        print(f"  chunk_{idx:03d} (lines {start}–{end})  → Gemini ...", flush=True)
        result = extract_from_chunk(client, args.model, text,
                                    fallback_model=args.fallback_model)

        header = f"<!-- chunk {idx:03d} | lines {start}–{end} | source: {commentary_id} -->\n\n"
        if not result or result.strip().upper() == "NO CANDIDATES":
            body = "<!-- no candidates -->\n"
        else:
            body = result.rstrip() + "\n"
        chunk_out.write_text(header + body, encoding="utf-8")

    # ---- Step 3b: PASS 2 — raw enumeration blocks, one file per chunk (resumable) ----
    if not args.no_enum:
        print("\nPass 2 — raw enumeration blocks:")
        for idx, start, end, text in chunks:
            enum_out = enum_dir / f"chunk_{idx:03d}.md"
            if enum_out.exists() and not args.force:
                print(f"  chunk_{idx:03d} (lines {start}–{end})  [skip — exists]")
                continue

            print(f"  chunk_{idx:03d} (lines {start}–{end})  → Gemini ...", flush=True)
            enum_result = extract_enumerations_from_chunk(
                client, args.model, text, fallback_model=args.fallback_model)

            if not enum_result or enum_result.strip().upper() == "NO ENUMERATIONS":
                enum_out.write_text("NO ENUMERATIONS\n", encoding="utf-8")
            else:
                enum_out.write_text(enum_result.rstrip() + "\n", encoding="utf-8")

    # ---- Step 4a: combine section candidates into one file ----
    combined_parts = []
    total_candidates = 0
    for idx, start, end, _ in chunks:
        chunk_out = temp_dir / f"chunk_{idx:03d}.md"
        if not chunk_out.exists():
            print(f"  ! missing {chunk_out.name}; skipping in combine", file=sys.stderr)
            continue
        content = chunk_out.read_text(encoding="utf-8")
        total_candidates += count_candidates(content)
        combined_parts.append(content.rstrip() + "\n")

    frontmatter = (
        "---\n"
        f"source: {commentary_id}\n"
        "skill: toc-candidate-extraction\n"
        "stage: candidates\n"
        f"date: {date.today().isoformat()}\n"
        f"model: {args.model}\n"
        f"total_candidates: {total_candidates}\n"
        "---\n\n"
    )
    candidates_doc = frontmatter + "\n".join(combined_parts)
    out_file.write_text(candidates_doc, encoding="utf-8")

    # ---- Step 4b: assemble enumeration text (per-chunk files) for the tree step ----
    enumerations_text = ""
    total_enum_blocks = enum_file_count = 0
    if not args.no_enum:
        enum_chunks = []
        for idx, start, end, _ in chunks:
            enum_out = enum_dir / f"chunk_{idx:03d}.md"
            if not enum_out.exists():
                continue
            c = enum_out.read_text(encoding="utf-8").strip()
            enum_file_count += 1
            if not c or c.upper().startswith("NO ENUMERATIONS"):
                continue
            total_enum_blocks += count_enum_blocks(c)
            enum_chunks.append(f"<!-- chunk {idx:03d} | lines {start}–{end} -->\n{c}")
        enumerations_text = "\n\n".join(enum_chunks)

    print()
    print(f"✓ Pass 1: {total_candidates} section candidates merged → {out_file}")
    if not args.no_enum:
        print(f"✓ Pass 2: {total_enum_blocks} enumeration blocks across "
              f"{enum_file_count} chunk files → {enum_dir}")

    # ---- Step 5: build the nested decimal TOC tree ----
    if args.no_tree:
        return

    print()
    print("Building TOC tree from candidates + enumerations → Gemini ...", flush=True)
    tree_body = build_toc_tree(client, args.model, commentary_id, candidates_doc,
                               enumerations_text=enumerations_text,
                               fallback_model=args.fallback_model)

    tree_frontmatter = (
        "---\n"
        f"source: {commentary_id}\n"
        "skill: toc-candidate-extraction\n"
        "stage: toc-tree\n"
        f"date: {date.today().isoformat()}\n"
        f"model: {args.model}\n"
        "---\n\n"
    )
    tree_file.write_text(tree_frontmatter + tree_body.rstrip() + "\n", encoding="utf-8")

    # ---- Step 6: QC the tree (deterministic check, optional LLM repair) ----
    if not args.no_qc:
        print()
        print("QC — checking the TOC tree ...", flush=True)
        issues_before = qc_check_tree(tree_body)
        print(f"  {len(issues_before)} issue(s) found.")

        repaired = False
        issues_after = issues_before
        if issues_before and not args.no_qc_fix:
            print("  Repairing tree → Gemini ...", flush=True)
            issues_text = "\n".join(f"- {x}" for x in issues_before)
            fixed = repair_tree(client, args.model, commentary_id, tree_body,
                                issues_text, enumerations_text=enumerations_text,
                                candidates_text=candidates_doc,
                                fallback_model=args.fallback_model)
            if fixed:
                issues_after = qc_check_tree(fixed)
                tree_body = fixed
                tree_file.write_text(tree_frontmatter + tree_body.rstrip() + "\n",
                                     encoding="utf-8")
                repaired = True
                print(f"  After repair: {len(issues_after)} issue(s) remain.")

        def _issue_list(items):
            return "\n".join(f"- {x}" for x in items) if items else "- (none)"

        qc_doc = (
            "---\n"
            f"source: {commentary_id}\n"
            "skill: toc-candidate-extraction\n"
            "stage: toc-tree-qc\n"
            f"date: {date.today().isoformat()}\n"
            f"model: {args.model}\n"
            f"repaired: {str(repaired).lower()}\n"
            f"issues_before: {len(issues_before)}\n"
            f"issues_after: {len(issues_after)}\n"
            "---\n\n"
            "# TOC tree QC report\n\n"
            f"## Issues found{' (before repair)' if repaired else ''}\n\n"
            f"{_issue_list(issues_before)}\n"
        )
        if repaired:
            qc_doc += ("\n## Issues remaining after repair\n\n"
                       f"{_issue_list(issues_after)}\n")
        qc_file.write_text(qc_doc, encoding="utf-8")

    print()
    print("✓ Done.")
    print(f"  Candidates:   {out_file}")
    if not args.no_enum:
        print(f"  Enum folder:  {enum_dir}")
    print(f"  TOC tree:     {tree_file}")
    if not args.no_qc:
        print(f"  QC report:    {qc_file}")


if __name__ == "__main__":
    main()
