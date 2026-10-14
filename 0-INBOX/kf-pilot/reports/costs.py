#!/usr/bin/env python3
"""Cost of every model call for this text, by report line and language (USD at list prices).

  python3 reports/costs.py [--json out.json]      (from the kf-pilot dir)

Reads usage-ledger.jsonl and 4-SYSTEM/scripts/usage-ledger/prices.json (via usage_ledger.row_cost).
Rows without a language that belong to one (blind-eval batches "en-01", …) take it from the batch name.
"""
import argparse
import importlib.util
import json
import pathlib
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
KF = HERE.parent
spec = importlib.util.spec_from_file_location("ul", KF.parents[1] / "4-SYSTEM/scripts/usage-ledger/usage_ledger.py")
ul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ul)
PRICES = json.loads((KF.parents[1] / "4-SYSTEM/scripts/usage-ledger/prices.json").read_text(encoding="utf-8"))

LANG = {"en": "en", "english": "en", "zh": "zh", "modern chinese": "zh", "chinese": "zh", "hi": "hi", "hindi": "hi"}


def line(r):
    s, v = r["step"], r.get("variant")
    if s == "term-extract":
        return "Term extraction (shared)"
    if s == "term-review":
        return "Term review (shared)"
    if s == "termbase":
        return "Glossary (style sheet + agents)"
    if s == "termbase-review":
        return "Glossary review"
    if s == "translate-academic":
        return "Academic translation, incl. retries and fixes"
    if s == "translate-children":
        return "Children's version, incl. retries and fixes"
    if s == "factcheck":
        return f"{'Academic' if v == 'academic' else 'Children'}'s fact-check, incl. re-checks".replace("Academic's", "Academic")
    if s == "calibration":
        return "Measurement: checker reliability test"
    if s == "improvement-judge":
        return "Measurement: blind before/after judge"
    if s == "blind-eval":
        return "Measurement: blind comparison with zero-shot and human"
    if s in ("factcheck-academic", "factcheck-children"):
        return "Academic fact-check, incl. re-checks" if s.endswith("academic") else "Children's fact-check, incl. re-checks"
    if s in ("zero-shot", "zero-shot-root"):
        return "Zero-shot root translation (baseline)"
    if s == "commentary-translation":
        return "Commentary translations, 3 commentaries (baseline, earlier)"
    if s == "setup":
        return "Setup (track contracts)"
    return s


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json")
    a = p.parse_args()
    table = defaultdict(lambda: defaultdict(float))
    unpriced = []
    for raw in (KF / "usage-ledger.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(raw)
        if r.get("text") != "bodhicaryavatara":
            continue
        lang = LANG.get((r.get("lang") or "").lower())
        if not lang and r["step"] == "blind-eval" and r.get("batch"):
            lang = LANG.get(r["batch"].split("-")[0])
        if not lang and r["step"] == "commentary-translation":
            lang = LANG.get(r.get("batch", "").rsplit("-", 1)[-1])
        models = [m for m in (r.get("model") or "").split(",") if m in PRICES["models"]]
        c = ul.row_cost(dict(r, model=models[0]), PRICES) if models else None
        if c is None:
            unpriced.append(r.get("model"))
            continue
        table[line(r)][lang or "en"] += c
    order = ["Term extraction (shared)", "Term review (shared)", "Glossary (style sheet + agents)", "Glossary review",
             "Academic translation, incl. retries and fixes", "Academic fact-check, incl. re-checks",
             "Children's version, incl. retries and fixes", "Children's fact-check, incl. re-checks",
             "Setup (track contracts)", "Measurement: checker reliability test", "Measurement: blind before/after judge",
             "Measurement: blind comparison with zero-shot and human", "Zero-shot root translation (baseline)",
             "Commentary translations, 3 commentaries (baseline, earlier)"]
    print("| Step | en | zh | hi |\n|---|---|---|---|")
    for k in order + [k for k in table if k not in order]:
        if k in table:
            print(f"| {k} | " + " | ".join(f"{table[k].get(l, 0):.2f}" for l in ("en", "zh", "hi")) + " |")
    if unpriced:
        print(f"unpriced rows: {len(unpriced)} {sorted(set(map(str, unpriced)))}")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps({k: dict(v) for k, v in table.items()}, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
