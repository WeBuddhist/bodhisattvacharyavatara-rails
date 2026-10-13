#!/usr/bin/env python3
"""Build term packets for the termbase step.

  python3 prep.py <term-run-dir> <out-dir> [--per-batch 47]

Reads the reviewed registry and occurrences of a term-extract run, the segment
table, and the Sanskrit alignment (context/segment_context.py). Writes
<out>/terms.json (all packets), <out>/batches/batch-NN.json and
<out>/overview.md (one line per term, for the style-sheet agent).
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "context"))
from segment_context import build_context  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("term_run")
    p.add_argument("out")
    p.add_argument("--per-batch", type=int, default=47)
    p.add_argument("--examples", type=int, default=3)
    a = p.parse_args()
    run, out = pathlib.Path(a.term_run), pathlib.Path(a.out)
    reg = json.loads((run / "registry-reviewed.json").read_text(encoding="utf-8"))
    occ = json.loads((run / "occurrences-reviewed.json").read_text(encoding="utf-8"))
    segs = {s["id"]: s for s in json.loads((run / "segments.json").read_text(encoding="utf-8"))}
    ctx = build_context()
    packets = []
    for i, r in enumerate(reg, 1):
        mine = [o for o in occ if o["bo"] == r["bo"]]
        # Prefer examples that show different renderings, then spread over the text.
        picked, seen = [], set()
        for o in mine:
            key = ((o["dm"] or "").lower(), (o["gm"] or "").lower())
            if key not in seen:
                seen.add(key)
                picked.append(o)
        for o in mine[:: max(1, len(mine) // a.examples)]:
            if o not in picked:
                picked.append(o)
        ex = []
        for o in picked[: a.examples]:
            s = segs[o["id"]]
            ex.append({"id": o["id"], "bo": s["bo"], "dm": s["dm"], "gm": s["gm"],
                       "sa": " ".join(x["text"] for x in ctx.get(o["id"], {}).get("sa", []))})
        packets.append({"term_id": f"T{i:03d}", "bo": r["bo"], "count": r["count"],
                        "occurrences": r["occurrences"], "dm": r["dm"], "gm": r["gm"], "examples": ex})
    (out / "batches").mkdir(parents=True, exist_ok=True)
    (out / "terms.json").write_text(json.dumps(packets, ensure_ascii=False, indent=1), encoding="utf-8")
    # Interleave so every batch gets a mix of frequent and rare terms.
    n = -(-len(packets) // a.per_batch)
    for b in range(n):
        batch = packets[b::n]
        (out / "batches" / f"batch-{b + 1:02d}.json").write_text(json.dumps(batch, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = ["| id | Tibetan | count | DharmaMitra | Gemini |", "|---|---|---|---|---|"]
    for t in packets:
        f = lambda d: "; ".join(f"{k} ({v})" for k, v in list(d.items())[:4])  # noqa: E731
        lines.append(f"| {t['term_id']} | {t['bo']} | {t['count']} | {f(t['dm'])} | {f(t['gm'])} |")
    (out / "overview.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"terms={len(packets)} batches={n} sizes={[len(packets[b::n]) for b in range(n)]}")


if __name__ == "__main__":
    main()
