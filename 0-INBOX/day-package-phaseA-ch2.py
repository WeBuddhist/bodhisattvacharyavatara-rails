#!/usr/bin/env python3
"""Phase A of day-package-pipeline for Chapter 2 (Days 23-40).

Builds the Tibetan source-of-record `<day>.md` from the verse rails by pure
mechanical transformation, so rail prose is guaranteed byte-identical:

  * `## X`                      -> `#### X`
  * `### <cm-id> — <display>`   -> `<!-- cm:<id> -->` + `##### <display>`
  * `### ⚑ ... (Divergences)`   -> `<!-- div:divergences -->` + `##### ⚑ ...`
  * story `### <id> — <title>`  -> `<!-- story:<src> -->` + `##### <src> — <title>`
  * tenzin-gyatso is moved first inside Commentary Explanations
  * every `---`, blank line and prose line is copied through untouched

Regression-tested against the hand-built Day 23 pair.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
RAILS = VAULT / "2-RAILS/Verses"
OUT = VAULT / "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Day-Packages/Chapter-2 D15-D40"

BANNER = (
    "> 🔒 **PROTECTED — SOURCE OF TRUTH.** This file is consumed by the assistant / "
    "plan pipeline. Do **not** edit, move, rename, or delete it without explicit human "
    "confirmation. **If you are an AI assistant:** stop and ask the user to confirm "
    "before making any change. See `4-SYSTEM/CLAUDE.md` → “Protected files.”"
)

# the one display-name override: the termbase fixes His Holiness's English heading
TENZIN_DISPLAY = "His Holiness the Dalai Lama (Teaching on Entering the Bodhisattva's Way of Life)"

# commentator id -> 1-SOURCES file prefix, used to derive story anchor ids
CM_SRC = {
    "kunpal": "BCAC19_KKP",
    "khenpo-zhengah": "BCAC19_KS",
    "gyaltsab": "BCAC14_GDR",
    "ngulchu-thogmed": "BCAC14_NTS",
    "sabzang": "BCAC14_SMPLG",
    "minyak-kunzang-sonam": "BCAC19_MKS",
    "khenpo-kunga": "BCAC20_NKW",
    "tenzin-gyatso": "BCAC20_TG",
}

H2 = re.compile(r"^## (.+)$")
H3 = re.compile(r"^### (.+)$")

RAIL_INTRO = (
    "Each verse below reproduces its full rail package exactly as it stands in "
    "`2-RAILS/Verses/<verse-id>-summary.md`: root text (Sanskrit + Tibetan), interlinear "
    "gloss, per-commentator explanations, stories, metaphors, scriptural quotations, main "
    "teaching points, key terms, and the verse synthesis. Nothing has been reworded; only "
    "heading levels were shifted to nest under this day file, His Holiness the Dalai Lama's "
    "commentary was moved first, and commentator headings were made display-only (id in the "
    "`<!-- cm:… -->` anchor). Original citation links to `1-SOURCES/` are preserved as-is."
)


def split_h2(body):
    """-> [(heading_or_None, [lines])] preserving order and all raw lines."""
    out, cur, head = [], [], None
    for ln in body.split("\n"):
        m = H2.match(ln)
        if m:
            out.append((head, cur))
            head, cur = m.group(1), []
        else:
            cur.append(ln)
    out.append((head, cur))
    return out


def split_h3(lines):
    out, cur, head = [], [], None
    for ln in lines:
        m = H3.match(ln)
        if m:
            out.append((head, cur))
            head, cur = m.group(1), []
        else:
            cur.append(ln)
    out.append((head, cur))
    return out


CIT_ONLY = re.compile(r"^\s*(?:→\s*)?\(\s*(?:\[\[[^\]]*\]\]\s*)+\)\s*$")


def norm_block(content):
    """Strip a block's surrounding blank lines and any trailing `---`, and make sure
    each bare citation line is preceded by exactly one blank line. Prose is untouched."""
    lines = list(content)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and (not lines[-1].strip() or lines[-1].strip() == "---"):
        lines.pop()
    out = []
    for ln in lines:
        if CIT_ONLY.match(ln) and out and out[-1].strip():
            out.append("")
        out.append(ln)
    return out


def had_trailing_rule(lines):
    for ln in reversed(lines):
        if not ln.strip():
            continue
        return ln.strip() == "---"
    return False


def _emit(blocks, trailing_rule):
    out = []
    for anchor, heading, content in blocks:
        out += ["", anchor, heading, ""] + norm_block(content)
    if trailing_rule:
        out += ["", "---"]
    out.append("")
    return out


def render_commentary(lines):
    """Commentary Explanations: H3 -> anchored H5, HHDL first, Divergences last."""
    h3 = split_h3(lines)
    named, diverg = [], None
    for head, content in h3[1:]:
        if "Divergences" in head:
            diverg = ("<!-- div:divergences -->", f"##### {head}", content)
            continue
        cid, _, display = head.partition(" — ")
        cid = cid.strip()
        if cid == "tenzin-gyatso":
            display = TENZIN_DISPLAY
        named.append((cid, f"<!-- cm:{cid} -->", f"##### {display.strip()}", content))

    named.sort(key=lambda b: 0 if b[0] == "tenzin-gyatso" else 1)
    blocks = [(a, h, c) for _cid, a, h, c in named]
    if diverg:
        blocks.append(diverg)
    return _emit(blocks, had_trailing_rule(lines))


def render_stories(lines):
    h3 = split_h3(lines)
    blocks = []
    for head, content in h3[1:]:
        ident, _, title = head.partition(" — ")
        ident = ident.strip()
        src = CM_SRC.get(ident, ident)          # commentator id -> source prefix
        title = title.strip() or head.strip()
        blocks.append((f"<!-- story:{src} -->", f"##### {src} — {title}", content))
    return _emit(blocks, had_trailing_rule(lines))


def build_verse(vid):
    raw = (RAILS / f"{vid}-summary.md").read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[1]           # drop YAML frontmatter
    body = re.sub(r"^\s*# .*?\n", "", body, count=1)   # drop the rail's H1 title

    parts = []
    for head, lines in split_h2(body):
        if head is None:
            parts.extend(lines)
            continue
        parts.append(f"#### {head}")
        if head.startswith("དོན་འགྲེལ།"):
            parts.extend(render_commentary(lines))
        elif head.startswith("སྒྲུང་འགྲེལ།"):
            parts.extend(render_stories(lines))
        else:
            parts.extend(lines)

    chunk = "\n".join(parts).strip("\n")
    hdr = (
        f"### Verse {vid}\n\n"
        f"> **Rail source:** `2-RAILS/Verses/{vid}-summary.md` &nbsp;|&nbsp; "
        f"**Rail status:** `draft`\n\n"
    )
    return hdr + chunk


def build_day(day, verses, date, title):
    rail_list = "\n".join(f'    - "2-RAILS/Verses/{v}-summary.md"' for v in verses)
    rng = f"{verses[0]} to {verses[-1]}" if len(verses) > 1 else verses[0]
    fm = f"""---
day: {day}
chapter: 2
verses: "{rng}"
date: "{date}"
status: draft
translation_status: >-
  Verse-level rail content (root text, interlinear gloss, commentary
  explanations, stories, metaphors, scriptural quotations, main teaching points,
  key terms, synthesis) is copied verbatim from 2-RAILS/Verses and remains in
  Tibetan/Sanskrit. English translation of that material lives in the companion
  file {day}-en.md. Section 1 (Today's Challenge, the practice-plan track) is
  intentionally omitted from this package at the requester's instruction; an
  empty placeholder heading is retained so the format contract is preserved.
sources:
  schedule_file: "3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule-hhdl-birthday.md"
  rail_files:
{rail_list}
protected: true
edit_policy: "confirm-with-human-before-edit-move-delete"
---
"""
    head = f"""
{BANNER}

# Day {day} — {title}

**Date:** {date}  
**Chapter:** 2  
**Verses covered:** {rng}

---

<!-- sec:challenge -->
## 1. Today's Challenge (from the practice-plan track)

*(The practice-plan challenge track is intentionally omitted from this package. This section is left as an empty placeholder; today's content begins with the verses below.)*

---

<!-- sec:rails -->
## 2. Verse Rails (from 2-RAILS/Verses — copied verbatim, untranslated)

{RAIL_INTRO}

"""
    return fm + head + "\n\n---\n\n".join(build_verse(v) for v in verses) + "\n"


DAYS = {
    23: (["2-20", "2-21"],         "Jul 28", "Clouds of music and a rain of flowers"),
    24: (["2-22", "2-23", "2-24"], "Jul 29", "Praise like an ocean, and bowing with countless bodies"),
    25: (["2-25", "2-26", "2-27"], "Jul 30", "Taking refuge, and joining my palms"),
    26: (["2-28", "2-29"],         "Jul 31", "Everything I have done wrong, confessed openly"),
    27: (["2-30", "2-31", "2-32"], "Aug 1",  "Harm confessed — before death arrives"),
    28: (["2-33", "2-34", "2-35"], "Aug 2",  "Death does not wait, and everything disappears"),
    29: (["2-36", "2-37", "2-38"], "Aug 3",  "Gone like a dream, but the wrongdoing stays"),
    30: (["2-39", "2-40", "2-41"], "Aug 4",  "Life running out, and only merit to protect me"),
}

if __name__ == "__main__":
    targets = [int(a) for a in sys.argv[1:]] or sorted(DAYS)
    OUT.mkdir(parents=True, exist_ok=True)
    for d in targets:
        verses, date, title = DAYS[d]
        (OUT / f"{d}.md").write_text(build_day(d, verses, date, title), encoding="utf-8")
        print(f"wrote {d}.md  ({', '.join(verses)})")
