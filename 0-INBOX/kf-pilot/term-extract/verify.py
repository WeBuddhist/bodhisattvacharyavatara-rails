#!/usr/bin/env python3
"""Literal-occurrence check and consolidation for extracted terms.

  python3 verify.py check <batch.json> <agent-out.json>
      Every input segment present in order; every bo/dm/gm value is a literal
      substring of its segment field. Prints OK or the list of problems.

  python3 verify.py consolidate <run-dir> [--review <review.json>]
      Reads <run-dir>/segments.json and <run-dir>/agents/batch-*.json (plus an
      optional Gemini review), writes <run-dir>/occurrences.json and
      <run-dir>/registry.json, and prints stats.
"""
import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict


def norm_bo(s):
    s = (s or "").replace("​", "").replace(" ", " ").strip()
    return s.rstrip("་། ").strip()


def bo_in(term, seg):
    return bool(norm_bo(term)) and norm_bo(term) in seg["bo"].replace("​", "")


def en_in(term, text):
    return term is None or (term.strip() != "" and term.lower() in (text or "").lower())


def status(dm, gm):
    if dm and gm:
        return "agree" if dm.lower() == gm.lower() else "disagree"
    return "dm-only" if dm else "gm-only" if gm else "none"


def problems(batch, out):
    segs = {s["id"]: s for s in batch}
    got = [s["id"] for s in out.get("segments", [])]
    errs = []
    if got != [s["id"] for s in batch]:
        errs.append(f"segment ids/order differ from input: missing={sorted(set(segs) - set(got))} "
                    f"extra={sorted(set(got) - set(segs))}")
    for s in out.get("segments", []):
        seg = segs.get(s["id"])
        if not seg:
            continue
        for t in s.get("terms", []):
            if not bo_in(t.get("bo"), seg):
                errs.append(f'{s["id"]}: bo not in segment: {t.get("bo")!r}')
            for k in ("dm", "gm"):
                if not en_in(t.get(k), seg.get(k)):
                    errs.append(f'{s["id"]}: {k} not in its translation: {t.get(k)!r}')
            if not t.get("dm") and not t.get("gm"):
                errs.append(f'{s["id"]}: both dm and gm are null for {t.get("bo")!r}')
    return errs


def cmd_check(a):
    batch = json.loads(pathlib.Path(a.batch).read_text(encoding="utf-8"))
    try:
        out = json.loads(pathlib.Path(a.out).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"JSON does not load: {exc}")
        return 1
    errs = problems(batch, out)
    print("OK" if not errs else "\n".join(errs))
    return 1 if errs else 0


def cmd_consolidate(a):
    run = pathlib.Path(a.run_dir)
    segs = {s["id"]: s for s in json.loads((run / "segments.json").read_text(encoding="utf-8"))}
    occ = []
    for f in sorted((run / "agents").glob("batch-*.json")):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            seen = set()
            for t in s["terms"]:
                bo = norm_bo(t["bo"])
                if bo in seen:
                    continue
                seen.add(bo)
                occ.append({"id": s["id"], "bo": bo, "dm": t.get("dm"), "gm": t.get("gm"), "origin": "claude"})
    review = {}
    if a.review:
        review = json.loads(pathlib.Path(a.review).read_text(encoding="utf-8"))
        drops = {(d["id"], norm_bo(d["bo"])) for d in review.get("drop", [])}
        fixes = {(f["id"], norm_bo(f["bo"])): norm_bo(f["bo_fixed"]) for f in review.get("fix_span", [])}
        kept = []
        for o in occ:
            k = (o["id"], o["bo"])
            if k in drops:
                continue
            if k in fixes and bo_in(fixes[k], segs[o["id"]]):
                o = dict(o, bo=fixes[k], span_fixed_by="gemini")
            kept.append(o)
        have = {(o["id"], o["bo"]) for o in kept}
        for m in review.get("add", []):
            k = (m["id"], norm_bo(m["bo"]))
            if k not in have:
                kept.append({"id": m["id"], "bo": k[1], "dm": m.get("dm"), "gm": m.get("gm"), "origin": "gemini-review"})
        occ = kept
    for o in occ:
        seg = segs[o["id"]]
        o["bo_ok"] = bo_in(o["bo"], seg)
        o["dm_ok"] = en_in(o["dm"], seg.get("dm"))
        o["gm_ok"] = en_in(o["gm"], seg.get("gm"))
        o["status"] = status(o["dm"], o["gm"])
    bad = [o for o in occ if not (o["bo_ok"] and o["dm_ok"] and o["gm_ok"])]
    good = [o for o in occ if o["bo_ok"] and o["dm_ok"] and o["gm_ok"]]
    order = {sid: i for i, sid in enumerate(segs)}
    good.sort(key=lambda o: order[o["id"]])

    reg = defaultdict(lambda: {"occurrences": [], "dm": Counter(), "gm": Counter(), "status": Counter()})
    for o in good:
        r = reg[o["bo"]]
        r["occurrences"].append(o["id"])
        if o["dm"]:
            r["dm"][o["dm"]] += 1
        if o["gm"]:
            r["gm"][o["gm"]] += 1
        r["status"][o["status"]] += 1
    registry = [{"bo": bo, "count": len(r["occurrences"]), "occurrences": r["occurrences"],
                 "dm": dict(r["dm"].most_common()), "gm": dict(r["gm"].most_common()),
                 "status": dict(r["status"])} for bo, r in reg.items()]
    registry.sort(key=lambda r: -r["count"])
    suffix = "-reviewed" if a.review else ""
    (run / f"occurrences{suffix}.json").write_text(json.dumps(good, ensure_ascii=False, indent=1), encoding="utf-8")
    (run / f"registry{suffix}.json").write_text(json.dumps(registry, ensure_ascii=False, indent=1), encoding="utf-8")
    if bad:
        (run / f"rejected{suffix}.json").write_text(json.dumps(bad, ensure_ascii=False, indent=1), encoding="utf-8")
    st = Counter(o["status"] for o in good)
    origin = Counter(o["origin"] for o in good)
    print(json.dumps({"occurrences": len(good), "rejected_literal_check": len(bad),
                      "unique_terms": len(registry), "status": st, "origin": origin,
                      "review": {k: len(v) for k, v in review.items() if isinstance(v, list)}},
                     ensure_ascii=False))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("batch")
    c.add_argument("out")
    c.set_defaults(func=cmd_check)
    k = sub.add_parser("consolidate")
    k.add_argument("run_dir")
    k.add_argument("--review")
    k.set_defaults(func=cmd_consolidate)
    a = p.parse_args()
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
