#!/usr/bin/env python3
"""Score a planted-error checker run against its key.

  python3 score.py <calibration-dir>   -> <dir>/result.json + per-segment table

caught  = a planted segment the checker failed (critical/major);
located = caught AND a blocking issue's span overlaps the planted text (or the plant is an omission);
false alarm = an unplanted control segment the checker failed.
"""
import json
import pathlib
import sys

d = pathlib.Path(sys.argv[1])
key = json.loads((d / "key.json").read_text(encoding="utf-8"))
out = {s["id"]: s for s in json.loads((d / "agent-out.json").read_text(encoding="utf-8"))["segments"]}


def overlaps(span, new):
    span, new = span.strip(" ，。、'\"「」"), new.strip(" ，。、'\"「」")
    if not new:
        return True
    return any(new[k:k + 2] in span for k in range(max(1, len(new) - 1)))


rows, caught, located, sev_ok, fa = [], 0, 0, 0, 0
for i, k in key.items():
    s = out[i]
    blocking = [x for x in s["issues"] if x["severity"] in ("critical", "major")]
    if k["planted"]:
        c = s["verdict"] == "fail"
        loc = c and (any(x["type"] == "omission" for x in blocking) if k["kind"] == "omission"
                     else any(overlaps(x["span"], k["new"]) for x in blocking))
        top = max((x["severity"] for x in s["issues"]), key=["minor", "major", "critical"].index, default="—")
        caught += c
        located += loc
        sev_ok += top == k["severity"]
        rows.append(f"| {i} | {k['kind']} | {k['severity']} | {top} | {'yes' if c else 'MISSED'} | {'yes' if loc else '—'} |")
    else:
        fa += s["verdict"] == "fail"
        rows.append(f"| {i} | control | — | {s['verdict']} | {'FALSE ALARM' if s['verdict'] == 'fail' else 'ok'} | |")
n = sum(k["planted"] for k in key.values())
res = {"planted": n, "caught": caught, "located": located, "missed": n - caught, "severity_matches": sev_ok,
       "controls": len(key) - n, "false_alarms": fa, "recall": round(caught / n, 3)}
(d / "result.json").write_text(json.dumps(res), encoding="utf-8")
print("| Segment | Planted kind | Planted severity | Checker's top severity | Caught | Points at plant |\n|---|---|---|---|---|---|")
print("\n".join(rows))
print(json.dumps(res))
