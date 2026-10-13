#!/usr/bin/env python3
"""Check a fact-check agent's output, or merge all outputs of a run.

  python3 check.py <batch.json> <agent-out.json>
  python3 check.py --merge <run-dir>      -> <run-dir>/verdicts.json + summary
"""
import json
import pathlib
import sys

TYPES = {"mistranslation", "omission", "addition", "terminology", "doctrinal", "ambiguity", "fluency", "form"}
SEV = {"critical", "major", "minor"}


def problems(batch, out):
    ids = [s["id"] for s in batch]
    got = [s.get("id") for s in out.get("segments", [])]
    errs = [] if got == ids else [f"segment ids/order differ: missing={sorted(set(ids) - set(got))} extra={sorted(set(got) - set(ids))}"]
    for s in out.get("segments", []):
        iss = s.get("issues", [])
        if s.get("verdict") not in ("pass", "fail"):
            errs.append(f"{s.get('id')}: verdict must be pass or fail")
        blocking = [i for i in iss if i.get("severity") in ("critical", "major")]
        if (s.get("verdict") == "fail") != bool(blocking):
            errs.append(f"{s.get('id')}: verdict must be fail exactly when there is a critical or major issue")
        for i in iss:
            if i.get("type") not in TYPES:
                errs.append(f"{s.get('id')}: issue type must be one of {sorted(TYPES)}")
            if i.get("severity") not in SEV:
                errs.append(f"{s.get('id')}: severity must be one of {sorted(SEV)}")
            for k in ("span", "evidence", "fix"):
                if not (i.get(k) or "").strip():
                    errs.append(f"{s.get('id')}: issue needs a non-empty {k}")
    return errs


if sys.argv[1] == "--merge":
    run = pathlib.Path(sys.argv[2])
    segs = []
    for f in sorted((run / "agents").glob("batch-*.json")):
        segs += json.loads(f.read_text(encoding="utf-8"))["segments"]
    (run / "verdicts.json").write_text(json.dumps(segs, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    sev = Counter(i["severity"] for s in segs for i in s["issues"])
    typ = Counter(i["type"] for s in segs for i in s["issues"] if i["severity"] != "minor")
    print(json.dumps({"segments": len(segs), "pass": sum(s["verdict"] == "pass" for s in segs),
                      "fail": sum(s["verdict"] == "fail" for s in segs), "issues_by_severity": sev,
                      "blocking_issues_by_type": typ}))
    sys.exit(0)
batch = json.load(open(sys.argv[1], encoding="utf-8"))
try:
    out = json.load(open(sys.argv[2], encoding="utf-8"))
except Exception as exc:  # noqa: BLE001
    sys.exit(f"JSON does not load: {exc}")
errs = problems(batch, out)
print("OK" if not errs else "\n".join(errs))
sys.exit(1 if errs else 0)
