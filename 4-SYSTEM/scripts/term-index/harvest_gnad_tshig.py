#!/usr/bin/env python3
"""
harvest_gnad_tshig.py
=====================

Harvests every ``#### གནད་ཚིག`` (key term) block out of the verse rails in
``2-RAILS/Verses/`` and emits a raw, source-side term index.

Why this exists
---------------
The translation pipeline's central defect was that the termbase was built *from
the English translation* — so it could only ever describe the inconsistency it
was meant to prevent, and any term the zero-shot pass rendered badly everywhere
could never be corrected (1 285 terms ended up with no termbase entry at all).

The fix is to build the term inventory from the **Tibetan source and its
commentaries, before translating**. That inventory already exists in this vault:
each verse rail carries a ``## གནད་ཚིག`` section whose blocks each hold

    a Tibetan term  +  a commentary definition (འགྲེལ་བཤད་)  +  a citation (ཁུངས།)

That is precisely a source-side, commentary-grounded, cited term list. This
script harvests it. It is deliberately a **parser, not a prompt**: no model, no
recall, no judgement. Every record it emits is traceable to a line in a rail
file and, through that, to a block ID in ``1-SOURCES/``.

What it does NOT do
-------------------
It does not group senses, normalise lemmas, or choose renderings. Those are
later phases and (for sense grouping) the one step that legitimately needs a
model — but a model *classifying supplied glosses*, never *recalling terms*.
The output of this script is the input to that step.

Pipeline position
-----------------
    [THIS SCRIPT]  →  bo-term-index.raw.yaml
                   →  (B2) mechanical lemma normalisation
                   →  (B3) LLM sense grouping  →  bo-term-index.yaml
                   →  (C)  attested renderings per language pair
                   →  (D)  per-track termbase, one rendering per sense

Usage
-----
    python3 4-SYSTEM/scripts/term-index/harvest_gnad_tshig.py

    # explicit paths / formats
    python3 harvest_gnad_tshig.py \
        --rails-dir 2-RAILS/Verses \
        --out       2-RAILS/Term-Index/bo-term-index.raw.yaml \
        --report    2-RAILS/Term-Index/coverage.md \
        --format    yaml

    # validate only; exit 1 if any anomaly is found (use in CI / pre-commit)
    python3 harvest_gnad_tshig.py --check

Notes
-----
* Dependency-free (standard library only). YAML is written by a small internal
  emitter that double-quotes every scalar, so Tibetan, ``#``, ``:`` and ``⚑``
  are all safe.
* All text is normalised to **NFC** on read. Tibetan is routinely stored in
  mixed normalisation forms; without this, ``བྱང་ཆུབ་`` from one file will not
  compare equal to ``བྱང་ཆུབ་`` from another and the whole index silently
  fragments.
* Accepts rails named either ``<verse-id>.md`` or ``<verse-id>-summary.md`` so
  it keeps working across the planned rename.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

# Heading markers, matched after NFC normalisation and rstrip().
SEC_KEYTERMS = "## གནད་ཚིག"          # opens the key-terms section
BLK_TERM = "#### གནད་ཚིག"            # opens one key-term block
BLK_GLOSS = "#### འགྲེལ་བཤད་"        # commentary definition
BLK_SOURCE = "#### ཁུངས།"            # citation

# Commentary catalog code -> registered_id (4-SYSTEM/Docs/vault-annex.md §3).
#
# Derived empirically from the rails themselves: for each "### <id> — ..."
# section, the catalog codes cited inside that section were counted, and the
# modal pairing taken. Confidence from the 154 existing rails is shown.
# Edit this table rather than the parsing code if a mapping is wrong.
COMMENTARY_IDS = {
    "BCAC19_KKP":   "kunpal",                # 89%
    "BCAC19_KS":    "khenpo-zhengah",        # 93%
    "BCAC19_MKS":   "minyak-kunzang-sonam",  # 85%
    "BCAC14_GDR":   "gyaltsab",              # 88%
    "BCAC14_NTS":   "ngulchu-thogmed",       # 89%
    "BCAC14_SMPLG": "sabzang",               # 90%
    "BCAC20_NKW":   "khenpo-kunga",          # 87%
    "BCAC20_TG":    "tenzin-gyatso",         # 100%
    # Unresolved — cited in the rails but never inside their own attributed
    # section, so no mapping could be derived mechanically. Left unmapped on
    # purpose: a guess here would silently mis-attribute a citation, which is
    # exactly the failure this vault's citation chain exists to prevent.
    # "BCAC13_KTB": "?",
    # "BCACXX_WR":  "?",
}

# Trailing Tibetan punctuation stripped when building the grouping key.
# NOT stripped from `surface`, which stays verbatim as written in the rail.
TRAILING_PUNCT = "\u0F0B\u0F0D\u0F0E\u0F14 \t"   # tsheg, shad, double shad, comma

# Matches a markdown link target of the form  path/to/file.md#^1-10
RE_BLOCKREF = re.compile(r"\(([^()\[\]]*?\.md)#(\^[0-9]+-[0-9]+)\)")
# Fallback: a citation that names the commentary file but no block ID. These are
# harvested (losing them would be worse) but flagged: without a block ID the
# claim is not verse-level traceable, which is what the citation chain requires.
RE_FILEREF = re.compile(r"\(([^()\[\]]*?\.md)\)")
RE_CATALOG = re.compile(r"(BCAC[0-9A-Z]+_[A-Z0-9]+)_")
RE_BOLD = re.compile(r"\*\*(.+?)\*\*")
RE_VERSE_FROM_NAME = re.compile(r"^(\d+-\d+)(?:-summary)?$")


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def nfc(text: str) -> str:
    """Normalise to NFC. See module docstring for why this is not optional."""
    return unicodedata.normalize("NFC", text)


def group_key(surface: str) -> str:
    """Grouping key for a surface form: NFC, trailing tsheg/shad stripped.

    ``རྒྱལ་བའི་སྐུ།`` and ``རྒྱལ་བའི་སྐུ་`` are the same term written with
    different terminal punctuation. Without this they would occupy two rows in
    the index and, downstream, receive two different renderings.
    """
    return nfc(surface).strip().rstrip(TRAILING_PUNCT)


def yaml_scalar(value) -> str:
    """Emit a YAML scalar. Strings are always double-quoted and escaped."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    s = str(value).replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", "\\n").replace("\r", "")
    return f'"{s}"'


def to_yaml(records: list[dict], meta: dict) -> str:
    """Minimal, dependency-free YAML emitter for this specific shape."""
    out: list[str] = ["---"]
    for k, v in meta.items():
        out.append(f"{k}: {yaml_scalar(v)}")
    out.append("---")
    out.append("terms:")
    for r in records:
        out.append(f"  - id: {yaml_scalar(r['id'])}")
        for field in ("verse", "chapter", "surface", "key", "note",
                      "flagged", "gloss_bo", "rail"):
            out.append(f"    {field}: {yaml_scalar(r[field])}")
        if r["sources"]:
            out.append("    sources:")
            for s in r["sources"]:
                out.append(f"      - commentary: {yaml_scalar(s['commentary'])}")
                out.append(f"        code: {yaml_scalar(s['code'])}")
                out.append(f"        file: {yaml_scalar(s['file'])}")
                out.append(f"        block: {yaml_scalar(s['block'])}")
        else:
            out.append("    sources: []")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

def split_blocks(lines: list[str]) -> list[list[str]]:
    """Return the key-term blocks inside the ``## གནད་ཚིག`` section."""
    start = None
    for i, line in enumerate(lines):
        if line.rstrip().startswith(SEC_KEYTERMS):
            start = i + 1
            break
    if start is None:
        return []

    end = len(lines)
    for i in range(start, len(lines)):
        s = lines[i].rstrip()
        # A new level-2 heading closes the section. Level-4 headings are ours.
        if s.startswith("## ") and not s.startswith("#### "):
            end = i
            break

    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in lines[start:end]:
        if line.rstrip().startswith(BLK_TERM):
            if current is not None:
                blocks.append(current)
            current = []
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def parse_sources(text: str) -> tuple[list[dict], list[str]]:
    """Extract (commentary, code, file, block) tuples from a citation blob."""
    sources, problems = [], []
    found = [(p, b) for p, b in RE_BLOCKREF.findall(text)]
    if not found:
        # No block-level citation. Fall back to file-level, and flag it.
        for p in RE_FILEREF.findall(text):
            found.append((p, None))
        if found:
            problems.append("citation has no block ID (file-level only)")

    for path, block in found:
        path = path.strip()
        m = RE_CATALOG.search(Path(path).name)
        code = m.group(1) if m else None
        cid = COMMENTARY_IDS.get(code)
        if code and cid is None:
            problems.append(f"unmapped commentary code {code}")
        sources.append({
            "commentary": cid or "UNMAPPED",
            "code": code or "UNKNOWN",
            "file": path,
            "block": block,
        })
    # De-duplicate while preserving order.
    seen, unique = set(), []
    for s in sources:
        sig = (s["file"], s["block"])
        if sig not in seen:
            seen.add(sig)
            unique.append(s)
    return unique, problems


def parse_block(body: list[str]) -> tuple[dict, list[str]]:
    """Parse one key-term block into a record plus a list of anomalies."""
    problems: list[str] = []
    term_lines, gloss_lines, source_lines = [], [], []
    mode = "term"

    for line in body:
        s = line.rstrip()
        if s.startswith(BLK_GLOSS):
            mode = "gloss"
            continue
        if s.startswith(BLK_SOURCE):
            mode = "source"
            continue
        if s.strip() in ("---", "***"):
            continue
        {"term": term_lines, "gloss": gloss_lines, "source": source_lines}[mode].append(s)

    term_raw = " ".join(x.strip() for x in term_lines if x.strip()).strip()
    bold = RE_BOLD.findall(term_raw)
    if bold:
        surface = bold[0].strip()
        note = RE_BOLD.sub("", term_raw).strip()
    else:
        surface = term_raw
        note = ""
        if term_raw:
            problems.append("term not in **bold**")

    flagged = "⚑" in term_raw or "⚑" in " ".join(gloss_lines)
    note = note.replace("⚑", "").strip(" ()/—-")

    gloss = " ".join(x.strip() for x in gloss_lines if x.strip()).strip()
    src_blob = "\n".join(source_lines)
    sources, src_problems = parse_sources(src_blob)
    problems += src_problems

    if not surface:
        problems.append("empty term")
    if not gloss:
        problems.append("missing commentary definition (འགྲེལ་བཤད་)")
    if not sources:
        problems.append("missing or unparseable citation (ཁུངས།)")

    return {
        "surface": surface,
        "key": group_key(surface),
        "note": note,
        "flagged": flagged,
        "gloss_bo": gloss,
        "sources": sources,
    }, problems


def read_frontmatter_verse(lines: list[str]) -> str | None:
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:40]:
        if line.strip() == "---":
            break
        m = re.match(r'^verse_id:\s*"?([0-9]+-[0-9]+)"?\s*$', line.strip())
        if m:
            return m.group(1)
    return None


def harvest(rails_dir: Path) -> tuple[list[dict], list[dict], dict]:
    records: list[dict] = []
    anomalies: list[dict] = []
    files_with_section = 0
    rail_files = sorted(
        p for p in rails_dir.glob("*.md")
        if RE_VERSE_FROM_NAME.match(p.stem)
    )

    for path in rail_files:
        verse = RE_VERSE_FROM_NAME.match(path.stem).group(1)
        try:
            raw = nfc(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError as exc:
            anomalies.append({"rail": str(path), "verse": verse, "term": "",
                              "problem": f"unreadable: {exc}"})
            continue
        lines = raw.splitlines()

        fm_verse = read_frontmatter_verse(lines)
        if fm_verse and fm_verse != verse:
            anomalies.append({
                "rail": str(path), "verse": verse, "term": "",
                "problem": f"frontmatter verse_id '{fm_verse}' != filename '{verse}'",
            })

        blocks = split_blocks(lines)
        if not blocks:
            anomalies.append({"rail": str(path), "verse": verse, "term": "",
                              "problem": "no ## གནད་ཚིག section or no blocks in it"})
            continue
        files_with_section += 1

        for n, body in enumerate(blocks, start=1):
            rec, problems = parse_block(body)
            rec["id"] = f"{verse}.{n:02d}"
            rec["verse"] = verse
            rec["chapter"] = int(verse.split("-")[0])
            rec["rail"] = str(path).replace("\\", "/")
            records.append(rec)
            for p in problems:
                anomalies.append({"rail": str(path), "verse": verse,
                                  "term": rec["surface"][:40], "problem": p})

    stats = {
        "rail_files_scanned": len(rail_files),
        "rail_files_with_key_terms": files_with_section,
        "term_blocks": len(records),
        "distinct_keys": len({r["key"] for r in records}),
        "anomalies": len(anomalies),
    }
    return records, anomalies, stats


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def build_report(records, anomalies, stats, rails_dir) -> str:
    by_chapter = Counter(r["chapter"] for r in records)
    verses_seen = {r["verse"] for r in records}
    key_counts = Counter(r["key"] for r in records)
    verses_per_key = defaultdict(set)
    for r in records:
        verses_per_key[r["key"]].add(r["verse"])
    commentary_counts = Counter(
        s["commentary"] for r in records for s in r["sources"]
    )

    out = [
        "---",
        "title: Term-index harvest — coverage report",
        f"source: {rails_dir}",
        "generated_by: 4-SYSTEM/scripts/term-index/harvest_gnad_tshig.py",
        "status: draft",
        "---",
        "",
        "# Coverage",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Rail files scanned | {stats['rail_files_scanned']} |",
        f"| Rail files with a `## གནད་ཚིག` section | {stats['rail_files_with_key_terms']} |",
        f"| Verses represented | {len(verses_seen)} |",
        f"| **Key-term blocks harvested** | **{stats['term_blocks']}** |",
        f"| Distinct surface keys | {stats['distinct_keys']} |",
        f"| Anomalies | {stats['anomalies']} |",
        "",
        "## Per chapter",
        "",
        "| Chapter | Terms | Verses |",
        "|---:|---:|---:|",
    ]
    for ch in sorted(by_chapter):
        nv = len({r["verse"] for r in records if r["chapter"] == ch})
        out.append(f"| {ch} | {by_chapter[ch]} | {nv} |")

    out += ["", "## Citations by commentary", "",
            "| Commentary | Citations |", "|---|---:|"]
    for cid, n in commentary_counts.most_common():
        out.append(f"| `{cid}` | {n} |")

    out += ["", "## Most frequent terms (candidate high-priority senses)", "",
            "These are the terms a wrong rendering damages most often. "
            "Work the sense-grouping pass (B3) from the top of this list down.",
            "", "| Term | Blocks | Verses |", "|---|---:|---:|"]
    for key, n in key_counts.most_common(40):
        out.append(f"| {key} | {n} | {len(verses_per_key[key])} |")

    singles = sum(1 for k, n in key_counts.items() if n == 1)
    out += ["", "## Distribution", "",
            f"- Terms appearing in only one block: **{singles}** "
            f"({100*singles/max(len(key_counts),1):.0f}% of distinct keys)",
            f"- Terms appearing in 5+ blocks: "
            f"**{sum(1 for _, n in key_counts.items() if n >= 5)}**",
            ""]

    if anomalies:
        out += ["## Anomalies", "",
                "Every row is a block that could not be fully parsed, or a rail "
                "that is missing something. Fix these in the rail files — this "
                "script deliberately does not guess.",
                "", "| Rail | Verse | Term | Problem |", "|---|---|---|---|"]
        for a in anomalies[:200]:
            rail = Path(a["rail"]).name
            out.append(f"| `{rail}` | {a['verse']} | {a['term']} | {a['problem']} |")
        if len(anomalies) > 200:
            out.append(f"| … | | | {len(anomalies)-200} more |")
    else:
        out += ["## Anomalies", "", "None. Every block parsed cleanly.", ""]

    out += ["", "---", "",
            "## Next step (B2 — mechanical, no model)", "",
            "Group the `key` values into lemmas: strip case particles "
            "(`ཀྱི་ གྱི་ གི་ འི་ ཀྱིས་ གྱིས་ གིས་ ལ་ ནས་ ལས་ དུ་ ཏུ་ སུ་ ར་`), "
            "collect the stripped forms as `variants:`, and only then hand each "
            "lemma's collected `gloss_bo` strings to a model for sense grouping "
            "(B3). The model classifies supplied glosses; it never recalls terms.",
            ""]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[3])
    ap.add_argument("--rails-dir", default="2-RAILS/Verses")
    ap.add_argument("--out", default="2-RAILS/Term-Index/bo-term-index.raw.yaml")
    ap.add_argument("--report", default="2-RAILS/Term-Index/coverage.md")
    ap.add_argument("--format", choices=("yaml", "json"), default="yaml")
    ap.add_argument("--check", action="store_true",
                    help="validate only; write nothing; exit 1 on any anomaly")
    args = ap.parse_args()

    rails_dir = Path(args.rails_dir)
    if not rails_dir.is_dir():
        print(f"ERROR: rails dir not found: {rails_dir}", file=sys.stderr)
        return 2

    records, anomalies, stats = harvest(rails_dir)

    print(f"  rails scanned          : {stats['rail_files_scanned']}")
    print(f"  rails with key terms   : {stats['rail_files_with_key_terms']}")
    print(f"  key-term blocks        : {stats['term_blocks']}")
    print(f"  distinct surface keys  : {stats['distinct_keys']}")
    print(f"  anomalies              : {stats['anomalies']}")

    if args.check:
        for a in anomalies[:30]:
            print(f"    ! {Path(a['rail']).name} [{a['verse']}] "
                  f"{a['term']}: {a['problem']}")
        if len(anomalies) > 30:
            print(f"    ! … {len(anomalies)-30} more")
        return 1 if anomalies else 0

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "source_dir": str(rails_dir).replace("\\", "/"),
        "generated_by": "4-SYSTEM/scripts/term-index/harvest_gnad_tshig.py",
        "language": "bo",
        "status": "raw",
        "note": "Mechanical harvest. No sense grouping, no lemma normalisation, "
                "no renderings. Input to phase B2/B3.",
        **{k: v for k, v in stats.items()},
    }
    if args.format == "json":
        out_path.write_text(
            json.dumps({"meta": meta, "terms": records},
                       ensure_ascii=False, indent=2),
            encoding="utf-8", newline="\n")
    else:
        out_path.write_text(to_yaml(records, meta), encoding="utf-8", newline="\n")
    print(f"  → {out_path}")

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(build_report(records, anomalies, stats, rails_dir),
                           encoding="utf-8", newline="\n")
    print(f"  → {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
