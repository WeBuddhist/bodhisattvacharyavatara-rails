#!/usr/bin/env python3
"""Regenerate a raw bilingual glossary file from an interlinear gloss file.

Replaces the LLM-curation half of ``glossary-extract-raw`` with a deterministic
script: groups token-pairs by normalized source lemma, counts distinct blocks
per rendering, and writes the glossary with rendering tables ordered by
frequency descending (ties broken by first-attestation block order — the
rendering first attested in an earlier block wins).

Usage:

    python3 regenerate_raw_glossary.py \\
        <gloss-file>.md <bilingual-glossary>.md

Frequency definition: "Frequencies count distinct blocks, not raw token-pair
occurrences" (per SKILL.md completion-check). Two occurrences in the same
block count once for that block.

Lemma normalization:
- Strip Leipzig-style morphology suffix (everything from ``-<UPPERCASE>``
  onward). ``kusala-NOM.PL.M`` → ``kusala``; ``samādhi+indriya-ACC.SG.N`` →
  ``samādhi+indriya``.
- Lowercase to merge casing variants (``Yo`` / ``yo`` → ``yo``).
- Strip trailing ``…pe…`` from compound-with-ellipsis lemmas
  (``hoti…pe…`` → ``hoti``).

Filtering:
- Drop degenerate lemmas (starting with ``--``, single-char particles, or empty).
- Drop a small skiplist of pure function/glue words (particles, demonstratives,
  relative pronouns).
- Keep lemmas with total occurrence count ≥ 3 (the skill's keyword threshold).
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# -----------------------------------------------------------------------------
# Function-word skiplist. These are pure glue words that recur thousands of
# times but carry no domain content. Keep "katama" / "hoti" / "atthi" — those
# carry interpretive weight in question-and-answer formulas.
# -----------------------------------------------------------------------------
SKIP_LEMMAS = {
    # particles
    "na", "ca", "vā", "eva", "pi", "api", "iti", "hi", "nu", "mā",
    "pana", "kira", "atho", "evaṃ", "tu", "ti",
    # demonstratives / relative pronouns (forms that show up as lemmas)
    "ima", "ta", "aya", "ya", "eta", "tad", "etad", "ima-",
    "yo", "yā", "yaṃ", "yāni", "yassa",
    "ayaṃ", "idaṃ", "ime", "imāni", "imāsaṃ", "imaṃ",
    "tasmiṃ", "tasmi", "tassa", "tāni", "tāsaṃ", "tāsu", "taṃ", "te",
    "yassmin", "yasmiṃ", "yasmin",
    # numerals & quantifiers (low content for this task)
    # left out — kept e.g. eka, dvi may have interpretive use
    # placeholders / scaffold artifacts
    "pe", "…pe…",
}

LEMMA_MORPH_RE = re.compile(r"^([^\-]+(?:-[a-zāīūṇṅñṭḍṃḷ]+)*?)(?=-[A-Z]|$)")
TRAILING_PE_RE = re.compile(r"…pe…$")


def normalize_lemma(raw: str) -> str:
    """Strip morphology suffix, lowercase, drop trailing …pe…."""
    if not raw:
        return ""
    m = LEMMA_MORPH_RE.match(raw)
    head = m.group(1) if m else raw
    head = TRAILING_PE_RE.sub("", head)
    head = head.lower()
    return head


def looks_degenerate(lemma: str) -> bool:
    if not lemma:
        return True
    if lemma.startswith("--"):
        return True
    if lemma in SKIP_LEMMAS:
        return True
    if len(lemma) < 2:
        return True
    # Pure numeric / punctuation
    if re.fullmatch(r"[\.…\-+0-9]+", lemma):
        return True
    return False


# -----------------------------------------------------------------------------
# Block-ID sorting. Block IDs look like "1-272" or "1-0a-1". We sort them by
# the numeric and lexicographic parts so that "1-2" < "1-10" < "1-100".
# -----------------------------------------------------------------------------
def block_sort_key(bid: str):
    parts = re.split(r"[-]", bid)
    out = []
    for p in parts:
        m = re.match(r"^(\d+)([A-Za-z]*)$", p)
        if m:
            out.append((int(m.group(1)), m.group(2)))
        else:
            out.append((0, p))
    return out


# -----------------------------------------------------------------------------
# Gloss-file parsing — for sample-pairing snippet extraction.
# -----------------------------------------------------------------------------
BLOCK_HEADING_RE = re.compile(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", re.MULTILINE)
GLOSS_BLOCK_RE = re.compile(r"```gloss\s*\n(.*?)```", re.DOTALL)
LINE_RE = lambda marker: re.compile(rf"^\\{marker}\s+(.*)$", re.MULTILINE)


def parse_gloss_file(path: Path):
    text = path.read_text(encoding="utf-8")
    parts = re.split(BLOCK_HEADING_RE, text)
    for i in range(1, len(parts), 2):
        bid = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        m = GLOSS_BLOCK_RE.search(section)
        if not m:
            continue
        body = m.group(1)
        gla = _line(body, "gla")
        glb = _line(body, "glb")
        glc = _line(body, "glc")
        yield bid, gla, glb, glc


def _line(body: str, marker: str):
    m = LINE_RE(marker).search(body)
    if not m:
        return []
    return m.group(1).split()


# -----------------------------------------------------------------------------
# Core regeneration.
# -----------------------------------------------------------------------------
def regenerate(gloss_path: Path, output_path: Path, min_freq: int = 3,
               translator_label: str = "Rhys Davids") -> dict:
    """Regenerate the raw bilingual glossary file. Return stats dict."""

    # First pass — collect token-pair rows, indexed by normalized lemma.
    # For each lemma, store per-rendering: set of distinct blocks + per-block
    # sample (block_id -> source_token).
    lemma_data = defaultdict(lambda: {
        "renderings": defaultdict(lambda: {"blocks": set(), "first_block": None}),
        "samples": defaultdict(list),  # rendering -> [(block_id, source_token), ...]
    })

    total_pairs = 0
    skipped_degenerate = 0

    for bid, gla, glb, glc in parse_gloss_file(gloss_path):
        if not gla:
            continue
        for i, src in enumerate(gla):
            rendering = glc[i] if i < len(glc) else "--"
            if rendering == "--" or not rendering:
                continue
            lemma_cell = glb[i] if i < len(glb) else ""
            if not lemma_cell or lemma_cell == "--":
                lemma_cell = src
            lemma = normalize_lemma(lemma_cell)
            if looks_degenerate(lemma):
                skipped_degenerate += 1
                continue
            total_pairs += 1
            entry = lemma_data[lemma]
            r_entry = entry["renderings"][rendering]
            r_entry["blocks"].add(bid)
            if r_entry["first_block"] is None:
                r_entry["first_block"] = bid
            else:
                # Keep smaller (earlier) first_block
                if block_sort_key(bid) < block_sort_key(r_entry["first_block"]):
                    r_entry["first_block"] = bid
            entry["samples"][rendering].append((bid, src))

    # Filter to lemmas with total occurrences >= min_freq.
    keep = {}
    for lemma, data in lemma_data.items():
        total = sum(len(r["blocks"]) for r in data["renderings"].values())
        if total >= min_freq:
            keep[lemma] = data

    # Build the output.
    lines = []
    lines.append("---")
    lines.append(f"gloss_file: 2-RAILS/Bilingual-Glossaries/Raw/{gloss_path.name}")
    lines.append("source_file: 1-SOURCES/Text/pi-dhammasangani.md")
    lines.append("target_file: 1-SOURCES/Translations/en-dhammasangani-rd.md")
    lines.append("source_language: pi")
    lines.append("target_language: en")
    lines.append("language_pair: pi-en")
    lines.append("target_lang_tag: en-rd")
    lines.append("translator: C.A.F. Rhys Davids, A Buddhist Manual of Psychological Ethics (PTS, 1900)")
    lines.append(f"total_keywords: {len(keep)}")
    lines.append("status: draft")
    lines.append("ordering: renderings within each keyword are ordered by frequency descending; ties broken by first-attestation block order (rendering first attested in an earlier block wins).")
    lines.append("---")
    lines.append("")
    lines.append(f"# Raw bilingual glossary — {translator_label}")
    lines.append("")
    lines.append(f"Extracted from the interlinear gloss file ({len(keep)} keywords with occurrence ≥ {min_freq}, function words excluded).")
    lines.append("")

    # Sort headwords alphabetically (per skill's rule).
    for lemma in sorted(keep.keys(), key=lambda s: (s.lower(), s)):
        data = keep[lemma]
        lines.append(f"## {lemma}")
        lines.append("")
        lines.append("**Renderings attested in this source:**")
        lines.append("")
        lines.append("| Rendering | Frequency | First seen | Notes |")
        lines.append("|-----------|-----------|------------|-------|")
        # Order renderings by (count desc, first_block asc).
        ordered = sorted(
            data["renderings"].items(),
            key=lambda kv: (-len(kv[1]["blocks"]), block_sort_key(kv[1]["first_block"])),
        )
        for rendering, r in ordered:
            n = len(r["blocks"])
            fb = r["first_block"]
            lines.append(f"| {rendering} | {n} | ^{fb} | — |")
        lines.append("")
        lines.append("**Sample pairings:**")
        lines.append("")
        # Pick up to 3 samples: prefer one per top rendering (most frequent first).
        seen_blocks = set()
        sample_picks = []
        for rendering, _ in ordered:
            samples = data["samples"][rendering]
            # Pick earliest sample (by block_sort_key) not yet shown.
            samples_sorted = sorted(samples, key=lambda t: block_sort_key(t[0]))
            for sb, st in samples_sorted:
                if sb in seen_blocks:
                    continue
                sample_picks.append((sb, st, rendering))
                seen_blocks.add(sb)
                break
            if len(sample_picks) >= 3:
                break
        for sb, st, rendering in sample_picks:
            lines.append(f"> **^{sb}** — *{st}* → \"{rendering}\"")
            lines.append(">")
        # Drop trailing > if any
        while lines and lines[-1] == ">":
            lines.pop()
        lines.append("")
        lines.append("---")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")

    return {
        "total_pairs": total_pairs,
        "skipped_degenerate": skipped_degenerate,
        "lemmas_before_filter": len(lemma_data),
        "lemmas_kept": len(keep),
        "total_block_occurrences_in_output": sum(
            len(r["blocks"])
            for d in keep.values()
            for r in d["renderings"].values()
        ),
    }


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    gloss_path = Path(argv[1])
    out_path = Path(argv[2])
    stats = regenerate(gloss_path, out_path)
    print(f"Wrote {out_path}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
