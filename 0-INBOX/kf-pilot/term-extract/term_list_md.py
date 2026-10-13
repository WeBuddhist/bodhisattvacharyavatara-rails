#!/usr/bin/env python3
"""Render a run's reviewed registry as a readable Markdown term list.

  python3 term_list_md.py <run-dir>   -> <run-dir>/term-list.md
"""
import json
import pathlib
import sys

run = pathlib.Path(sys.argv[1])
reg = json.loads((run / "registry-reviewed.json").read_text(encoding="utf-8"))
occ = json.loads((run / "occurrences-reviewed.json").read_text(encoding="utf-8"))
review = json.loads((run / "review.json").read_text(encoding="utf-8"))


def rend(d):
    return "; ".join(f"{k} ({v})" if v > 1 else k for k, v in d.items()) or "—"


def base(t):
    """Compare renderings ignoring case, diacritics on a/i/u and a plural -s."""
    t = t.lower().replace("ā", "a").replace("ī", "i").replace("ū", "u").strip()
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in t.split())


def kind(r):
    dm = {base(k) for k in r["dm"]}
    gm = {base(k) for k in r["gm"]}
    if len(dm) == 1 and dm == gm:
        return "same"
    if dm & gm:
        return "partly"
    return "differ"


added = {o["bo"] for o in occ if o["origin"] == "gemini-review"}
rows = [(r, kind(r)) for r in reg]
n_same = sum(k == "same" for _, k in rows)
n_segs = len(json.loads((run / "segments.json").read_text(encoding="utf-8")))
n_batches = len(list((run / "batches").glob("batch-*.json")))
lines = [
    "# Bodhicaryāvatāra — glossary terms from the two English machine translations", "",
    f"{len(reg)} Tibetan terms, {len(occ)} occurrences in {n_segs} segments. Extracted by Claude Sonnet "
    f"({n_batches} parallel agents) from the Tibetan + DharmaMitra + Gemini English; reviewed by Gemini 3.1 Pro "
    f"(dropped {len(review['drop'])}, fixed {len(review['fix_span'])} spans, added {len(review['add'])} occurrences).", "",
    f"- **same**: both translations always use one rendering (ignoring case, plural and long-vowel marks) — {n_same} terms",
    f"- **partly**: they share a rendering but at least one also varies — {sum(k == 'partly' for _, k in rows)} terms",
    f"- **differ**: no rendering in common — {sum(k == 'differ' for _, k in rows)} terms",
    "- ✚ = term first added by the Gemini review", "",
    "Counts in brackets are occurrences. Renderings are verbatim from each translation.", "",
]
for title, keep in (("Terms to decide (the two translations differ or vary)", ("differ", "partly")),
                    ("Terms where both translations agree", ("same",))):
    lines += [f"## {title}", "", "| # | Tibetan | Occ. | DharmaMitra | Gemini | |", "|---|---|---|---|---|---|"]
    i = 0
    for r, k in rows:
        if k in keep:
            i += 1
            mark = "✚" if r["bo"] in added and r["count"] == sum(1 for o in occ if o["bo"] == r["bo"] and o["origin"] == "gemini-review") else ""
            lines.append(f"| {i} | {r['bo']} {mark} | {r['count']} | {rend(r['dm'])} | {rend(r['gm'])} | {k} |")
    lines.append("")
(run / "term-list.md").write_text("\n".join(lines), encoding="utf-8")
print(f"terms={len(reg)} same={n_same} to-decide={len(reg) - n_same}")
