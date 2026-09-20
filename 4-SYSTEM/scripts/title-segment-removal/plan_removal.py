#!/usr/bin/env python3
"""Turn a `before` snapshot into a removal plan, and SIMULATE it end to end.

The plan: for each edition, every `type: title` segment, ordered by span start
DESCENDING. Bottom-up means each op's coordinates are the ones already in the
snapshot -- no cumulative-shift arithmetic, and every op can be checked against
the snapshot on its own.

WHY DESCENDING IS SOUND (backend `_adjust_span_for_delete`, vendored in
spanmath.py):

    if del_end <= start:   return (start - del_len, end - del_len)   # after  -> shifts
    if del_start >= end:   return (start, end)                       # before -> UNTOUCHED

Title spans are pairwise disjoint, so when title *k* is deleted every title
still queued (all strictly before it) hits branch 2 and keeps its original
coordinates. Ascending order would need every later offset recomputed after
every call, against a server that cannot be safely re-read mid-sequence if a
write's response is lost.

This script does not merely assert that. It replays the whole op sequence
against the snapshot using the backend's own arithmetic and writes a PREDICTED
after-state: final content and its sha256, every surviving segment's span,
every surviving TOC section's span, and the exact set of entities the server
should DETACH DELETE. `compare.py` then holds the real after-snapshot against
that prediction. Agreement is the proof; any disagreement is a finding.

Usage:
    plan_removal.py --snapshot before
    plan_removal.py --snapshot before --only <edition_id>
    plan_removal.py --snapshot before --first 2     # only the LAST 2 titles
                                                    # of each edition (the two
                                                    # deleted first)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

import spanmath

HERE = os.path.dirname(os.path.abspath(__file__))
SNAPDIR = os.environ.get("TSR_SNAPSHOTS", os.path.join(HERE, "snapshots"))


def toc_section_spans(rec):
    """Flatten the TOC into {section_id: (start, end)} plus a depth/title map."""
    spans, meta = {}, {}

    def walk(sections, depth, parent):
        for sec in sections or []:
            sp = sec.get("span") or {}
            sid = sec.get("id")
            if sid and sp.get("start") is not None:
                spans[sid] = (sp["start"], sp["end"])
                meta[sid] = {"depth": depth, "parent": parent,
                             "title": next(iter((sec.get("title") or {}).values()), None)}
            walk(sec.get("subsections"), depth + 1, sid)

    for tocdoc in (rec.get("toc") or []):
        if isinstance(tocdoc, dict):
            walk(tocdoc.get("sections"), 0, None)
    return spans, meta


def structural_checks(rec):
    """Invariants the whole method rests on. Any failure blocks the edition."""
    problems = []
    content, segs = rec["content"], rec["segments"]

    prev = 0
    for s in segs:
        if s["start"] != prev:
            problems.append(f"segment {s['reference']}: expected start {prev}, got {s['start']}")
        if s["end"] < s["start"]:
            problems.append(f"segment {s['reference']}: inverted span")
        prev = s["end"]
    if prev != len(content):
        problems.append(f"segments end at {prev} but content is {len(content)} chars")

    titles = [s for s in segs if s["type"] == "title"]
    for a, b in zip(titles, titles[1:]):
        if a["end"] > b["start"]:
            problems.append(f"titles {a['reference']} / {b['reference']} overlap")
    if not titles:
        problems.append("no title segments")
    return problems


def simulate(rec, ops):
    """Replay ops (descending) with the backend's arithmetic. Returns prediction."""
    content = rec["content"]
    seg_spans = {s["id"]: (s["start"], s["end"]) for s in rec["segments"]}
    seg_meta = {s["id"]: {"reference": s["reference"], "type": s["type"]} for s in rec["segments"]}
    toc_spans, toc_meta = toc_section_spans(rec)

    removed_segments, removed_toc = [], []
    for op in ops:
        s, e = op["start"], op["end"]
        if content[s:e] != op["text"]:
            raise AssertionError(f"op text mismatch at [{s},{e}) in {rec['edition_id']}")
        content = content[:s] + content[e:]
        seg_spans, gone = spanmath.apply_delete(seg_spans, s, e)
        removed_segments.extend(gone)
        toc_spans, gone_toc = spanmath.apply_delete(toc_spans, s, e)
        removed_toc.extend(gone_toc)

    surviving = sorted(seg_spans.items(), key=lambda kv: kv[1][0])
    pred = {
        "content_len": len(content),
        "content_sha256": hashlib.sha256(content.encode()).hexdigest(),
        "segment_count": len(seg_spans),
        "segments": [{"id": sid, "reference": seg_meta[sid]["reference"],
                      "type": seg_meta[sid]["type"], "start": sp[0], "end": sp[1]}
                     for sid, sp in surviving],
        "removed_segment_ids": sorted(removed_segments),
        "toc_sections": {sid: list(sp) for sid, sp in sorted(toc_spans.items())},
        "removed_toc_section_ids": sorted(removed_toc),
    }

    # the predicted content must still be tiled exactly by the surviving spans
    prev = 0
    tiling = []
    for _, (a, b) in surviving:
        if a != prev:
            tiling.append(f"predicted gap/overlap at {prev} vs {a}")
        prev = b
    if prev != len(content):
        tiling.append(f"predicted segments end at {prev}, content is {len(content)}")
    pred["tiling_problems"] = tiling

    # which alignment pairs should disappear: those naming a removed segment
    gone_set = set(removed_segments)
    pair_losses = {}
    for key, plist in (rec.get("pairs") or {}).items():
        if not isinstance(plist, list):
            continue
        lost = []
        for p in plist:
            ids = {v for k, v in p.items() if isinstance(v, str)}
            if ids & gone_set:
                lost.append(p)
        pair_losses[key] = {"before": len(plist), "expected_lost": len(lost),
                            "expected_after": len(plist) - len(lost)}
    pred["pair_expectations"] = pair_losses
    return pred


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", default="before")
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--first", type=int,
                    help="keep only the last N titles per edition (deleted first)")
    ap.add_argument("--out")
    args = ap.parse_args(argv)

    ok, msg = spanmath.verify_vendored_copy()
    print(("UNVERIFIED " if ok is None else "OK " if ok else "DRIFT ") + msg)
    if ok is False:
        print("refusing to plan against drifted span arithmetic")
        return 2

    snapdir = os.path.join(SNAPDIR, args.snapshot)
    index = json.load(open(os.path.join(snapdir, "_index.json")))
    editions = [e for e in index["editions"] if not args.only or e in args.only]

    plan = {"snapshot": args.snapshot, "base": index["base"],
            "first_n": args.first, "editions": {}}
    total_ops = total_problems = 0

    for eid in editions:
        path = os.path.join(snapdir, f"{eid}.json")
        if not os.path.exists(path):
            print(f"!! {eid}: no snapshot file"); total_problems += 1; continue
        rec = json.load(open(path))
        problems = structural_checks(rec)
        content = rec["content"]
        titles = [s for s in rec["segments"] if s["type"] == "title"]
        ops = [{"segment_id": t["id"], "reference": t["reference"],
                "start": t["start"], "end": t["end"],
                "length": t["end"] - t["start"],
                "text": content[t["start"]:t["end"]]}
               for t in sorted(titles, key=lambda s: s["start"], reverse=True)]
        if args.first:
            ops = ops[: args.first]

        pred = None
        if not problems:
            try:
                pred = simulate(rec, ops)
                problems.extend(pred.pop("tiling_problems"))
                if pred["removed_toc_section_ids"]:
                    problems.append(
                        "TOC sections would be DETACH DELETEd: "
                        + ",".join(pred["removed_toc_section_ids"]))
                unexpected = set(pred["removed_segment_ids"]) - {o["segment_id"] for o in ops}
                if unexpected:
                    problems.append(f"segments removed beyond the targeted titles: {sorted(unexpected)}")
                missing = {o["segment_id"] for o in ops} - set(pred["removed_segment_ids"])
                if missing:
                    problems.append(f"targeted titles NOT removed by simulation: {sorted(missing)}")
            except AssertionError as e:
                problems.append(str(e))

        lang = (rec.get("text") or {}).get("language")
        plan["editions"][eid] = {
            "language": lang,
            "title": next(iter(((rec.get("text") or {}).get("title") or {}).values()), None),
            "before": {"content_len": rec["content_len"],
                       "content_sha256": rec["content_sha256"],
                       "segment_count": rec["segment_count"]},
            "ops": ops,
            "predicted": pred,
            "problems": problems,
        }
        total_ops += len(ops)
        total_problems += len(problems)
        flag = "OK " if not problems else "!! "
        extra = ""
        if pred:
            extra = (f"  -> {pred['content_len']} chars, {pred['segment_count']} segs, "
                     f"{len(pred['toc_sections'])} toc-sections kept")
        print(f"{flag}{eid}  {lang or '?':<3} {len(ops):>3} ops{extra}")
        for p in problems:
            print(f"     - {p}")

    out = os.path.abspath(args.out or os.path.join(snapdir, os.pardir,
                          f"plan-{args.snapshot}{'-first%d' % args.first if args.first else ''}.json"))
    with open(out, "w") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=1)
    print(f"\n{total_ops} delete ops across {len(plan['editions'])} editions; {total_problems} problems")
    print(f"wrote {out}")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
