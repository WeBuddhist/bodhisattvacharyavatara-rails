#!/usr/bin/env python3
"""Snapshot every piece of live state a content PATCH could disturb.

Take one before the patch run and one after, then `compare.py` them. What is
captured, per edition:

  * the edition record and its text record
  * the full `content` string (stored verbatim, plus sha256 and length)
  * every segment: node id, reference, type, line spans
  * the edition's alignment links
  * every alignment PAIR LIST the edition takes part in, in both directions

The pair lists are the point of the exercise. Deleting a segment DETACH-deletes
it in Neo4j, which takes its `ALIGNED_TO` relationships with it — so a pair list
is where collateral damage would show up first.

Usage:
    snapshot.py before --seed 3rCvwAoWrzKGlIQdtLjCu
    snapshot.py after                       # reuses the edition set from `before`
    snapshot.py before --seed <id> --no-crawl   # seed editions only
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import sys
import time

import api

HERE = os.path.dirname(os.path.abspath(__file__))
SNAPDIR = os.environ.get("TSR_SNAPSHOTS", os.path.join(HERE, "snapshots"))


def discover(seeds, crawl=True):
    """Seed editions plus, if crawling, everything aligned to or from them."""
    seen, queue = set(), list(seeds)
    while queue:
        eid = queue.pop(0)
        if eid in seen:
            continue
        seen.add(eid)
        if not crawl:
            continue
        for link in api.alignments(eid):
            for side in ("aligned_edition_id", "target_edition_id"):
                other = link.get(side)
                if other and other not in seen:
                    queue.append(other)
    return sorted(seen)


def capture(eid):
    rec = {"edition_id": eid}
    ed = api.edition(eid)
    rec["edition"] = ed
    try:
        rec["text"] = api.text(ed.get("text_id")) if ed.get("text_id") else None
    except api.ApiError as e:
        rec["text"] = {"error": str(e)}
    body = api.content(eid)
    rec["content"] = body
    rec["content_sha256"] = hashlib.sha256(body.encode()).hexdigest()
    rec["content_len"] = len(body)
    segs = api.segments(eid)
    rec["segments"] = [
        {"id": s["id"], "reference": s["reference"], "type": s["type"],
         "lines": s["lines"],
         "start": s["lines"][0]["start"] if s["lines"] else None,
         "end": s["lines"][-1]["end"] if s["lines"] else None}
        for s in segs
    ]
    rec["segment_count"] = len(segs)
    links = api.alignments(eid)
    rec["alignments"] = links
    rec["pairs"] = {}
    for link in links:
        src, tgt = link["aligned_edition_id"], link["target_edition_id"]
        key = f"{src}->{tgt}"
        if key in rec["pairs"]:
            continue
        try:
            rec["pairs"][key] = api.pairs(src, tgt)
        except api.ApiError as e:
            rec["pairs"][key] = {"error": str(e)}
    try:
        rec["toc"] = api.toc(eid)
    except api.ApiError as e:
        rec["toc"] = {"error": str(e)}
    return rec


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("label", help="snapshot name, e.g. before / after-2")
    ap.add_argument("--seed", action="append", default=[],
                    help="edition id to start from (repeatable)")
    ap.add_argument("--from-label", help="reuse the edition set of an earlier snapshot")
    ap.add_argument("--no-crawl", action="store_true",
                    help="do not follow alignment links out from the seeds")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args(argv)

    outdir = os.path.join(SNAPDIR, args.label)
    os.makedirs(outdir, exist_ok=True)

    if args.from_label or (not args.seed and os.path.exists(os.path.join(SNAPDIR, "before", "_index.json"))):
        src = args.from_label or "before"
        idx = json.load(open(os.path.join(SNAPDIR, src, "_index.json")))
        editions = idx["editions"]
        print(f"reusing {len(editions)} editions from snapshot '{src}'")
    else:
        editions = discover(args.seed, crawl=not args.no_crawl)
        print(f"discovered {len(editions)} editions from {len(args.seed)} seed(s)")

    index = {"label": args.label, "taken": time.strftime("%Y-%m-%dT%H:%M:%S"),
             "base": api.BASE, "editions": editions, "summary": {}}

    def work(eid):
        try:
            return eid, capture(eid), None
        except Exception as e:  # noqa: BLE001
            return eid, None, repr(e)[:300]

    with cf.ThreadPoolExecutor(args.workers) as ex:
        for eid, rec, err in ex.map(work, editions):
            if err:
                print(f"  !! {eid}: {err}")
                index["summary"][eid] = {"error": err}
                continue
            with open(os.path.join(outdir, f"{eid}.json"), "w") as fh:
                json.dump(rec, fh, ensure_ascii=False, indent=1)
            titles = [s for s in rec["segments"] if s["type"] == "title"]
            index["summary"][eid] = {
                "title_bo": ((rec.get("text") or {}).get("title") or {}).get("bo"),
                "language": (rec.get("text") or {}).get("language"),
                "chars": rec["content_len"],
                "sha256": rec["content_sha256"][:12],
                "segments": rec["segment_count"],
                "title_segments": len(titles),
                "alignment_links": len(rec["alignments"]),
                "pair_lists": {k: (len(v) if isinstance(v, list) else "ERROR")
                               for k, v in rec["pairs"].items()},
            }
            print(f"  {eid}  {rec['content_len']:>8} chars  "
                  f"{rec['segment_count']:>5} segs  {len(titles):>4} titles  "
                  f"{len(rec['alignments'])} links")

    with open(os.path.join(outdir, "_index.json"), "w") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
    print(f"\nwrote {outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
