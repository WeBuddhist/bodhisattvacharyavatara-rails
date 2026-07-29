#!/usr/bin/env python3
"""Build per-batch context bundles for rails-to-verse-translation (Step 3).

For each verse in range, emits: Tibetan root, Sanskrit, the human-translation
witnesses, the rail's synthesis, its key-term table, and its divergence block.

Run from the vault root.

    python3 extract_rails_context.py --range 2-25-2-50 --batch-size 6 --out /tmp/work

Reports any verse whose rail is missing a section, and any witness whose verse
numbering is offset (see SKILL.md Rule 3).
"""
import argparse
import json
import os
import re
import sys

ROOT_BO = "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
ROOT_SK = "1-SOURCES/Text/BCAV08_SH_sk.md"
WITNESSES = [
    ("pad", "Padmakara", "1-SOURCES/Translations/en-Padmakara_2006.md"),
    ("wal", "Wallace", "1-SOURCES/Translations/en-Wallace.md"),
    ("cho", "Choephel", "1-SOURCES/Translations/en-David_Karma_Choephel.md"),
]
RAIL = "2-RAILS/Verses/{vid}-summary.md"

SECTIONS = {
    "synthesis": r"## བསྡུས་དོན།.*?(?=\n---|\Z)",
    "key_terms": r"## གནད་ཚིག.*?(?=\n---|\n## |\Z)",
    "divergences": r"### ⚑ འགྲེལ་ཚུལ་མི་མཐུན་པ།.*?(?=\n---|\n## |\Z)",
    "teaching_points": r"## གཙོ་གནད།.*?(?=\n---|\n## |\Z)",
}


def parse_blocks(path):
    """Map block ID -> block text for a file using ^chapter-verse IDs."""
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    blocks, buf = {}, []
    for line in text.split("\n"):
        m = re.search(r"\^(\S+)\s*$", line)
        buf.append(re.sub(r"\^\S+\s*$", "", line))
        if m:
            blocks[m.group(1)] = "\n".join(x for x in buf if x.strip())
            buf = []
    return blocks


def strip_transclusions(s):
    return re.sub(r"!\[\[.*?\]\]\n?", "", s).strip()


def parse_range(spec):
    m = re.match(r"^(\d+)-(\d+)-(?:\1-)?(\d+)$", spec) or re.match(
        r"^(\d+)-(\d+)\s*(?:to|\.\.)\s*(?:\1-)?(\d+)$", spec
    )
    if not m:
        sys.exit(f"could not parse --range {spec!r}; use e.g. 2-25-2-50")
    ch, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if b < a:
        sys.exit(f"range end {b} precedes start {a}")
    return ch, a, b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--range", required=True, help="e.g. 2-25-2-50")
    ap.add_argument("--batch-size", type=int, default=6)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    ch, first, last = parse_range(args.range)
    vids = [f"{ch}-{n}" for n in range(first, last + 1)]
    os.makedirs(args.out, exist_ok=True)

    src = {"bo": parse_blocks(ROOT_BO), "sk": parse_blocks(ROOT_SK)}
    for key, _label, path in WITNESSES:
        src[key] = parse_blocks(path)

    problems = []
    for key, label, path in [("bo", "Tibetan root", ROOT_BO), ("sk", "Sanskrit", ROOT_SK)] + [
        (k, l, p) for k, l, p in WITNESSES
    ]:
        if src.get(key) is None:
            problems.append(f"MISSING FILE  {label}: {path}")
            continue
        absent = [v for v in vids if v not in src[key]]
        if absent:
            problems.append(
                f"OFFSET/GAP    {label}: missing {', '.join(absent)} "
                f"-- verify alignment before using as a witness (SKILL.md Rule 3)"
            )

    rails, rail_problems = {}, []
    for vid in vids:
        path = RAIL.format(vid=vid)
        if not os.path.exists(path):
            rail_problems.append(f"MISSING RAIL  {path}")
            rails[vid] = {}
            continue
        text = open(path, encoding="utf-8").read()
        got = {}
        for name, pat in SECTIONS.items():
            m = re.search(pat, text, re.S)
            got[name] = m.group(0) if m else ""
        st = re.search(r"^status:\s*(\S+)", text, re.M)
        got["status"] = st.group(1) if st else "unknown"
        if not got["synthesis"]:
            rail_problems.append(f"NO SYNTHESIS  {path}")
        if not got["key_terms"]:
            rail_problems.append(
                f"NO KEY TERMS  {path} -- fall back to གཙོ་གནད། teaching points"
            )
        if got["status"] != "complete":
            rail_problems.append(f"STATUS={got['status']:<9} {path}")
        rails[vid] = got

    batches = [vids[i : i + args.batch_size] for i in range(0, len(vids), args.batch_size)]
    for bi, batch in enumerate(batches, 1):
        out = [f"# CONTEXT BUNDLE — batch {bi}: verses {batch[0]} to {batch[-1]}\n"]
        for vid in batch:
            out.append("\n" + "=" * 70)
            out.append(f"## VERSE {vid}")
            out.append("=" * 70 + "\n")
            out.append("### Tibetan root\n" + strip_transclusions(src["bo"].get(vid, "—") if src["bo"] else "—"))
            out.append("\n### Sanskrit\n" + strip_transclusions(src["sk"].get(vid, "—") if src["sk"] else "—"))
            for key, label, _ in WITNESSES:
                if not src.get(key):
                    continue
                t = strip_transclusions(src[key].get(vid, ""))
                if t:
                    out.append(f"\n### EN witness — {label}\n{t}")
            r = rails.get(vid, {})
            if r.get("synthesis"):
                out.append("\n### RAIL — synthesis\n" + r["synthesis"])
            if r.get("key_terms"):
                out.append("\n### RAIL — key terms\n" + r["key_terms"])
            elif r.get("teaching_points"):
                out.append(
                    "\n### RAIL — teaching points (no key-term table in this rail)\n"
                    + r["teaching_points"]
                )
            if r.get("divergences"):
                out.append("\n### RAIL — DIVERGENCES\n" + r["divergences"])
        path = os.path.join(args.out, f"batch{bi}.md")
        open(path, "w", encoding="utf-8").write("\n".join(out))
        print(f"wrote {path}  ({len(batch)} verses)")

    # aggregate key terms for Step 4
    rows = []
    for vid in vids:
        for line in rails.get(vid, {}).get("key_terms", "").split("\n"):
            m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", line)
            if m:
                rows.append({"verse": vid, "lemma": m.group(1).strip(), "gloss": m.group(2).strip()})
    tb = os.path.join(args.out, "key_terms.json")
    json.dump(rows, open(tb, "w"), ensure_ascii=False, indent=1)

    lemmas = {}
    for r in rows:
        lemmas.setdefault(r["lemma"], []).append(r)
    multi = {k: v for k, v in lemmas.items() if len({x["gloss"] for x in v}) > 1}

    print(f"\nverses            : {len(vids)} ({vids[0]}..{vids[-1]})")
    print(f"batches           : {len(batches)}")
    print(f"key-term rows     : {len(rows)} across {len(lemmas)} unique lemmas -> {tb}")
    print(f"lemmas w/ conflicting glosses (⚑ candidates): {len(multi)}")
    for k in list(multi)[:15]:
        print(f"    {k}  ({len(multi[k])} readings)")

    if problems or rail_problems:
        print("\n--- ATTENTION ---")
        for p in problems + rail_problems:
            print("  " + p)
    else:
        print("\nno source problems detected")


if __name__ == "__main__":
    main()
