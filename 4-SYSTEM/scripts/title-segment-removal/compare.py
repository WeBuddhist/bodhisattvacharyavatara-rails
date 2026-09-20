#!/usr/bin/env python3
"""Hold the real after-snapshot against the plan's prediction, and report.

This is the part that makes the run reviewable. The plan does not just say
"delete these"; it says exactly what the edition should look like afterwards --
content sha256, every surviving segment's id/reference/type/span, every TOC
section's span, and every alignment pair count. This script checks all of it,
and separately diffs before vs after so nothing outside the prediction moved.

What it reports per edition:

  content      length delta, and whether the after-content equals the
               predicted content byte for byte (sha256)
  segments     which segments vanished (must be exactly the targeted titles),
               and whether every survivor kept its node id, reference, type and
               landed on its predicted span
  toc          which TOC sections survived and whether their spans match the
               prediction -- a TOC section is DETACH DELETEd if a delete range
               fully covers it, so this is where silent TOC damage would appear
  alignments   link list unchanged, and every pair list compared entry by entry
               against the before-snapshot
  titles       how many `type: title` segments remain

Exit code 0 only when every edition matches on every count.

Usage:
    compare.py --before before --after after --plan plan-before.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SNAPDIR = os.environ.get("TSR_SNAPSHOTS", os.path.join(HERE, "snapshots"))


def load(label, eid):
    p = os.path.join(SNAPDIR, label, f"{eid}.json")
    return json.load(open(p)) if os.path.exists(p) else None


def toc_spans(rec):
    out = {}

    def walk(sections):
        for sec in sections or []:
            sp = sec.get("span") or {}
            if sec.get("id") and sp.get("start") is not None:
                out[sec["id"]] = (sp["start"], sp["end"])
            walk(sec.get("subsections"))

    for tocdoc in (rec.get("toc") or []):
        if isinstance(tocdoc, dict):
            walk(tocdoc.get("sections"))
    return out


def pair_key(p):
    s, t = p.get("source_segment") or {}, p.get("target_segment") or {}
    return (s.get("id"), t.get("id"))


def compare_edition(eid, before, after, pred, ops):
    """Returns (findings, summary). findings non-empty == something is wrong."""
    f, s = [], {}
    targeted = {o["segment_id"] for o in ops}

    # --- content ---
    s["content"] = f"{before['content_len']} -> {after['content_len']}"
    s["content_delta"] = after["content_len"] - before["content_len"]
    if pred:
        if after["content_sha256"] != pred["content_sha256"]:
            f.append(f"content sha256 mismatch: predicted {pred['content_sha256'][:16]}, "
                     f"got {after['content_sha256'][:16]}")
        if after["content_len"] != pred["content_len"]:
            f.append(f"content length: predicted {pred['content_len']}, got {after['content_len']}")
    for o in ops:
        if o["text"] and o["text"] in after["content"]:
            f.append(f"removed title text still present in content: {o['text']!r}")

    # --- segments ---
    b = {x["id"]: x for x in before["segments"]}
    a = {x["id"]: x for x in after["segments"]}
    vanished, appeared = set(b) - set(a), set(a) - set(b)
    s["segments"] = f"{len(b)} -> {len(a)}"
    s["vanished"] = len(vanished)
    if vanished != targeted:
        extra, missing = vanished - targeted, targeted - vanished
        if extra:
            f.append(f"segments vanished that were NOT targeted: "
                     + ", ".join(f"{b[x]['reference']}({b[x]['type']})" for x in sorted(extra)))
        if missing:
            f.append(f"targeted segments still present: "
                     + ", ".join(f"{b[x]['reference']}" for x in sorted(missing)))
    if appeared:
        f.append(f"{len(appeared)} new segment ids appeared (segmentation was re-created, not edited)")
    for sid, seg in a.items():
        if sid in b:
            if seg["reference"] != b[sid]["reference"]:
                f.append(f"segment {sid}: reference {b[sid]['reference']} -> {seg['reference']}")
            if seg["type"] != b[sid]["type"]:
                f.append(f"segment {b[sid]['reference']}: type {b[sid]['type']} -> {seg['type']}")
    if pred:
        pmap = {x["id"]: (x["start"], x["end"]) for x in pred["segments"]}
        off = [x for x in a if x in pmap and (a[x]["start"], a[x]["end"]) != pmap[x]]
        if off:
            ex = ", ".join(f"{a[x]['reference']}: predicted {pmap[x]}, got ({a[x]['start']},{a[x]['end']})"
                           for x in off[:5])
            f.append(f"{len(off)} segment spans differ from prediction -- {ex}")
    prev, gaps = 0, 0
    for seg in a.values():
        if seg["start"] != prev:
            gaps += 1
        prev = seg["end"]
    if gaps:
        f.append(f"{gaps} gaps/overlaps in the after segmentation")
    if prev != after["content_len"]:
        f.append(f"after segments end at {prev}, content is {after['content_len']}")

    s["titles_left"] = sum(1 for x in a.values() if x["type"] == "title")

    # --- toc ---
    tb, ta = toc_spans(before), toc_spans(after)
    s["toc_sections"] = f"{len(tb)} -> {len(ta)}"
    lost = set(tb) - set(ta)
    if lost:
        f.append(f"TOC sections DELETED: {sorted(lost)}")
    if pred:
        ptoc = {k: tuple(v) for k, v in (pred.get("toc_sections") or {}).items()}
        off = [k for k in ta if k in ptoc and ta[k] != ptoc[k]]
        if off:
            ex = ", ".join(f"{k}: predicted {ptoc[k]}, got {ta[k]}" for k in off[:5])
            f.append(f"{len(off)} TOC section spans differ from prediction -- {ex}")

    # --- alignments ---
    lb = {(x["aligned_edition_id"], x["target_edition_id"]) for x in before["alignments"]}
    la = {(x["aligned_edition_id"], x["target_edition_id"]) for x in after["alignments"]}
    s["alignment_links"] = f"{len(lb)} -> {len(la)}"
    if lb != la:
        f.append(f"alignment links changed: lost {sorted(lb - la)}, gained {sorted(la - lb)}")
    s["pairs"] = {}
    for k, pb in (before.get("pairs") or {}).items():
        pa = (after.get("pairs") or {}).get(k)
        if not isinstance(pb, list) or not isinstance(pa, list):
            f.append(f"pair list {k} could not be compared")
            continue
        kb, ka = [pair_key(p) for p in pb], [pair_key(p) for p in pa]
        s["pairs"][k] = f"{len(pb)} -> {len(pa)}"
        if kb != ka:
            lostp, gained = set(kb) - set(ka), set(ka) - set(kb)
            f.append(f"pair list {k} changed: {len(pb)} -> {len(pa)} "
                     f"(lost {len(lostp)}, gained {len(gained)})")
    return f, s


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", default="before")
    ap.add_argument("--after", default="after")
    ap.add_argument("--plan", required=True)
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--report", help="write a markdown report here")
    args = ap.parse_args(argv)

    plan = json.load(open(args.plan))
    editions = [e for e in plan["editions"] if not args.only or e in args.only]

    lines, bad = [], 0
    for eid in editions:
        entry = plan["editions"][eid]
        before, after = load(args.before, eid), load(args.after, eid)
        if not before or not after:
            print(f"!! {eid}: missing snapshot"); bad += 1; continue
        findings, summary = compare_edition(eid, before, after, entry.get("predicted"), entry["ops"])
        ok = not findings
        bad += 0 if ok else 1
        head = f"{'OK ' if ok else '!! '}{eid}  [{entry.get('language')}]  {len(entry['ops'])} ops"
        print(head)
        print(f"     content {summary['content']} ({summary['content_delta']:+d})  "
              f"segments {summary['segments']} (-{summary['vanished']})  "
              f"titles left {summary['titles_left']}  "
              f"toc {summary['toc_sections']}  links {summary['alignment_links']}")
        for k, v in summary["pairs"].items():
            print(f"       pairs {k}  {v}")
        for x in findings:
            print(f"     - {x}")
        lines.append((head, summary, findings))

    print(f"\n{len(editions) - bad}/{len(editions)} editions match prediction exactly")

    if args.report:
        with open(args.report, "w") as fh:
            fh.write("# Title-segment removal — before/after comparison\n\n")
            fh.write(f"Plan: `{os.path.basename(args.plan)}`  ")
            fh.write(f"Snapshots: `{args.before}` → `{args.after}`\n\n")
            fh.write(f"**{len(editions) - bad}/{len(editions)} editions match the prediction exactly.**\n\n")
            fh.write("| edition | lang | ops | content | segments | titles left | TOC | links |\n")
            fh.write("|---|---|---|---|---|---|---|---|\n")
            for head, s, _ in lines:
                eid = head[3:].split()[0]
                lang = head.split("[")[1].split("]")[0]
                ops = head.split("]")[1].strip().split()[0]
                fh.write(f"| `{eid}` | {lang} | {ops} | {s['content']} ({s['content_delta']:+d}) | "
                         f"{s['segments']} | {s['titles_left']} | {s['toc_sections']} | "
                         f"{s['alignment_links']} |\n")
            fh.write("\n## Alignment pair lists\n\n| pair list | before → after |\n|---|---|\n")
            written = set()
            for _, s, _ in lines:
                for k, v in s["pairs"].items():
                    if k not in written:
                        fh.write(f"| `{k}` | {v} |\n"); written.add(k)
            allf = [(h, x) for h, _, fs in lines for x in fs]
            fh.write("\n## Findings\n\n")
            fh.write("None — every edition matched.\n" if not allf else
                     "".join(f"- **{h[3:].split()[0]}** — {x}\n" for h, x in allf))
        print(f"report: {args.report}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
