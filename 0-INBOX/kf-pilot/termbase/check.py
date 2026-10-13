#!/usr/bin/env python3
"""Check a termbase agent's output against its batch.

  python3 check.py <batch.json> <agent-out.json>

Every term_id present once; each term has >= 1 sense; academic, children and
reason non-empty; basis valid; a sense's `occurrences` is "all" or a list of the
term's own occurrence ids; with several senses, every occurrence is assigned to
exactly one sense. Prints OK or the problems.
"""
import json
import sys

BASIS = {"dm", "gm", "both", "new", "style-sheet", "kumarajiva", "zero-shot", "english-pivot"}
batch = {t["term_id"]: t for t in json.load(open(sys.argv[1], encoding="utf-8"))}
try:
    out = json.load(open(sys.argv[2], encoding="utf-8"))
except Exception as exc:  # noqa: BLE001
    sys.exit(f"JSON does not load: {exc}")
errs = []
got = [t.get("term_id") for t in out.get("terms", [])]
if sorted(got) != sorted(batch):
    errs.append(f"term ids differ: missing={sorted(set(batch) - set(got))} extra={sorted(set(got) - set(batch))} dup={[x for x in got if got.count(x) > 1][:5]}")
for t in out.get("terms", []):
    src = batch.get(t.get("term_id"))
    if not src:
        continue
    if t.get("bo") != src["bo"]:
        errs.append(f"{t['term_id']}: bo changed")
    senses = t.get("senses") or []
    if src.get("senses") and [x["sense"] for x in senses] != [x["sense"] for x in src["senses"]]:
        errs.append(f"{t['term_id']}: keep exactly the input senses, same labels and order")
    if not senses:
        errs.append(f"{t['term_id']}: no senses")
    assigned = []
    for s in senses:
        for k in ("sense", "academic", "children", "reason"):
            if not (s.get(k) or "").strip():
                errs.append(f"{t['term_id']}: empty {k}")
        if s.get("basis") not in BASIS:
            errs.append(f"{t['term_id']}: basis must be one of {sorted(BASIS)}")
        occ = s.get("occurrences")
        if occ == "all":
            assigned += src["occurrences"]
        elif isinstance(occ, list):
            bad = [o for o in occ if o not in src["occurrences"]]
            if bad:
                errs.append(f"{t['term_id']}: occurrences not of this term: {bad[:5]}")
            assigned += occ
        else:
            errs.append(f"{t['term_id']}: occurrences must be 'all' or a list")
    if len(senses) > 1 and sorted(assigned) != sorted(src["occurrences"]):
        errs.append(f"{t['term_id']}: with several senses every occurrence must be assigned exactly once")
print("OK" if not errs else "\n".join(errs))
sys.exit(1 if errs else 0)
