#!/usr/bin/env python3
"""Build the fix-request file for gm_variant_translate.py --feedback from a merged fact-check run.

  python3 make_feedback.py <run-dir>               -> <run-dir>/feedback-all.json   (every segment with an issue)
  python3 make_feedback.py <run-dir> --major-only  -> <run-dir>/feedback-major.json (only failing segments)

<run-dir> is a fact-check run after `check.py --merge` (e.g. 0-INBOX/kf-pilot/factcheck/zh-academic-a1).
Output format, as in the pilot: {id: {"translation": <text the check saw>, "issues": [...]}}.
"""
import json
import pathlib
import sys

run = pathlib.Path(sys.argv[1])
major_only = "--major-only" in sys.argv
seen = {s["id"]: s["translation"] for f in sorted((run / "batches").glob("*.json"))
        for s in json.loads(f.read_text(encoding="utf-8"))}
out = {}
for v in json.loads((run / "verdicts.json").read_text(encoding="utf-8")):
    if not v["issues"] or (major_only and v["verdict"] != "fail"):
        continue
    out[v["id"]] = {"translation": seen[v["id"]], "issues": v["issues"]}
name = "feedback-major.json" if major_only else "feedback-all.json"
(run / name).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(out)} segments -> {run / name}")
