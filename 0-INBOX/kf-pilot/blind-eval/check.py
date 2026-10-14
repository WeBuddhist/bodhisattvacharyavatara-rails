#!/usr/bin/env python3
"""Validate an MQM annotation file against its sample: python3 check.py <sample.json> <annotation.json>"""
import json
import sys

CATS = {"accuracy/mistranslation", "accuracy/omission", "accuracy/addition", "terminology", "fluency", "style"}
SEV = {"minor", "major", "critical"}
sample = json.load(open(sys.argv[1], encoding="utf-8"))
try:
    out = json.load(open(sys.argv[2], encoding="utf-8"))
except Exception as exc:  # noqa: BLE001
    sys.exit(f"JSON does not load: {exc}")
errs = []
got = [s.get("id") for s in out.get("segments", [])]
if got != [s["id"] for s in sample]:
    errs.append(f"segment ids/order differ from the input: {got}")
for s, o in zip(sample, out.get("segments", [])):
    if set(o.get("candidates", {})) != set(s["candidates"]):
        errs.append(f"{s['id']}: candidates must be exactly {sorted(s['candidates'])}")
    for L, es in o.get("candidates", {}).items():
        for e in es:
            if e.get("category") not in CATS:
                errs.append(f"{s['id']} {L}: category must be one of {sorted(CATS)}")
            if e.get("severity") not in SEV:
                errs.append(f"{s['id']} {L}: severity must be one of {sorted(SEV)}")
            if not (e.get("span") or "").strip() or not (e.get("explanation") or "").strip():
                errs.append(f"{s['id']} {L}: each error needs a span and an explanation")
print("OK" if not errs else "\n".join(errs))
sys.exit(1 if errs else 0)
