#!/usr/bin/env python3
"""Execute a removal plan: one `delete` PATCH per title segment, bottom-up.

    PATCH /v2/editions/{id}/content  {"type": "delete", "start": S, "end": E}

Ordering is descending by start, so every op uses the coordinates already in
the plan -- nothing is recomputed against a moving target. See plan_removal.py
for why that is sound.

FOUR SAFETY RULES, each earned:

 1. WRITES ARE NEVER RETRIED. A content PATCH is not idempotent. A delete whose
    response was lost in transit has still been applied server-side, and
    re-sending it eats the NEXT E-S characters. That cost a manual repair on
    the liturgy corpus (2026-09-19, edition kIBLisYhjyIOw2NUno2Ul). On any write
    failure this script stops that edition and leaves it for the operator.

 2. EVERY OP IS RE-CHECKED AGAINST LIVE STATE FIRST. Immediately before each
    PATCH the target segment is re-fetched and must still be `type: title` with
    exactly the planned span and text. That makes the run idempotent and
    resumable: a killed run is restarted with the same command, and an op that
    has already been applied fails its precheck and is skipped, not repeated.

 3. ONE EDITION AT A TIME, SEQUENTIALLY WITHIN THE EDITION. Ops within an
    edition are order-dependent; editions are independent of each other, but
    concurrency buys little here and makes a partial failure much harder to
    read. Editions run in sequence too.

 4. --dry-run IS THE DEFAULT POSTURE. Nothing is written without --execute.

Usage:
    remove_titles.py --plan plan-before.json --dry-run
    remove_titles.py --plan plan-before.json --execute --only <edition_id>
    remove_titles.py --plan plan-before.json --execute            # whole plan

Credentials: WEBUDDHIST_API_KEY (and WEBUDDHIST_APP) must be in the
environment; PATCH is key-gated. Ledger: written after every single call.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import api

HERE = os.path.dirname(os.path.abspath(__file__))


def precheck(eid, op):
    """Re-read the live segment. Returns (ok, reason, live_segment_or_None)."""
    try:
        segs = api.paged(f"/v2/editions/{eid}/segmentation/segments")
    except api.ApiError as e:
        return False, f"segment fetch failed: {e}", None
    live = next((s for s in segs if s["id"] == op["segment_id"]), None)
    if live is None:
        return False, "segment no longer exists (already removed?)", None
    if live["type"] != "title":
        return False, f"segment type is {live['type']}, not title", live
    start = live["lines"][0]["start"]
    end = live["lines"][-1]["end"]
    if (start, end) != (op["start"], op["end"]):
        return False, f"span moved: live [{start},{end}) vs planned [{op['start']},{op['end']})", live
    try:
        text = api.segment_content(op["segment_id"])
    except api.ApiError as e:
        return False, f"segment content fetch failed: {e}", live
    if text != op["text"]:
        return False, f"text differs: live {text!r} vs planned {op['text']!r}", live
    return True, "", live


def run_edition(eid, entry, execute, ledger, ledger_path):
    ops = entry["ops"]
    print(f"\n=== {eid}  [{entry.get('language')}]  {len(ops)} ops "
          f"({entry['before']['content_len']} chars, {entry['before']['segment_count']} segs)")
    results = []
    for i, op in enumerate(ops, 1):
        tag = f"  {i:>3}/{len(ops)}  {op['reference']:<6} [{op['start']},{op['end']})"
        ok, reason, live = precheck(eid, op)
        rec = {"edition_id": eid, "reference": op["reference"],
               "segment_id": op["segment_id"], "start": op["start"], "end": op["end"],
               "text": op["text"], "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
        if not ok:
            rec["status"] = "precheck-failed"
            rec["reason"] = reason
            print(f"{tag}  SKIP  {reason}")
            results.append(rec)
            ledger["ops"].append(rec)
            _save(ledger, ledger_path)
            continue
        if not execute:
            rec["status"] = "would-delete"
            print(f"{tag}  would delete {op['text']!r}")
            results.append(rec)
            continue
        try:
            status = api.delete_span(eid, op["start"], op["end"])
            rec["status"] = "deleted"
            rec["http"] = status
            print(f"{tag}  HTTP {status}  deleted {op['text']!r}")
        except Exception as e:  # noqa: BLE001
            rec["status"] = "write-failed"
            rec["reason"] = repr(e)[:300]
            print(f"{tag}  WRITE FAILED  {rec['reason']}")
            print(f"     !! stopping this edition. DO NOT re-run blindly: re-read live state first.")
            results.append(rec)
            ledger["ops"].append(rec)
            _save(ledger, ledger_path)
            break
        results.append(rec)
        ledger["ops"].append(rec)
        _save(ledger, ledger_path)
    return results


def _save(ledger, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(ledger, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--execute", action="store_true", help="actually write")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--ledger", default=os.path.join(HERE, "removal-ledger.json"))
    args = ap.parse_args(argv)

    if args.execute and args.dry_run:
        print("--execute and --dry-run are mutually exclusive"); return 2
    if args.execute and not os.environ.get("WEBUDDHIST_API_KEY"):
        print("WEBUDDHIST_API_KEY is not set; PATCH is key-gated. Refusing to run.")
        return 2

    plan = json.load(open(args.plan))
    editions = {k: v for k, v in plan["editions"].items() if not args.only or k in args.only}
    total = sum(len(v["ops"]) for v in editions.values())
    mode = "EXECUTE" if args.execute else "DRY RUN"
    print(f"{mode}: {total} delete ops across {len(editions)} edition(s) on {api.BASE}")
    if args.execute:
        print("writes are NOT retried; a failure stops that edition.")

    ledger = {"plan": os.path.abspath(args.plan), "base": api.BASE,
              "started": time.strftime("%Y-%m-%dT%H:%M:%S"), "mode": mode, "ops": []}
    if args.execute and os.path.exists(args.ledger):
        ledger = json.load(open(args.ledger))
        ledger.setdefault("ops", [])
        ledger["resumed"] = time.strftime("%Y-%m-%dT%H:%M:%S")

    counts = {}
    for eid, entry in editions.items():
        for rec in run_edition(eid, entry, args.execute, ledger, args.ledger):
            counts[rec["status"]] = counts.get(rec["status"], 0) + 1
    if args.execute:
        ledger["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        _save(ledger, args.ledger)
        print(f"\nledger: {args.ledger}")
    print("result:", json.dumps(counts, ensure_ascii=False))
    bad = {k for k in counts if k not in ("deleted", "would-delete")}
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
