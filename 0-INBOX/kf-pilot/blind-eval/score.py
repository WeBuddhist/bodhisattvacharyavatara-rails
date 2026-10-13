#!/usr/bin/env python3
"""Unblind and score the MQM annotations.

  python3 score.py [--json results.json]

Penalty per candidate segment: minor 1, major 5, critical 10 (same weights as the improvement metric).
Per language, system and annotator (claude / gemini): mean penalty per segment, blocking errors (major + critical)
per 100 segments, error-free segments, accuracy errors. Head-to-head: share of segments where the governed version
has a lower / equal / higher penalty than each other system. Annotator agreement: for every pair of candidates in a
segment, do Claude and Gemini order them the same way (ties excluded from the denominator only when both tie)?
"""
import argparse
import itertools
import json
import pathlib
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
W = {"minor": 1, "major": 5, "critical": 10}
LANGS = ["en", "zh", "hi"]
NAMES = {"governed": "Governed academic", "zeroshot-gemini": "Zero-shot Gemini",
         "zeroshot-dharmamitra": "Zero-shot DharmaMitra",
         "human-padmakara": "Human: Padmakara 2006", "human-rushi": "Human: 如石 (classical verse)"}


def load(annotator, lang):
    out = {}
    for f in sorted((HERE / annotator).glob(f"{lang}-*.json")):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            out[s["id"]] = s["candidates"]
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--json")
    a = p.parse_args()
    key = json.loads((HERE / "key.json").read_text(encoding="utf-8"))
    res = {}
    for lang in LANGS:
        ann = {who: load(who, lang) for who in ("claude", "gemini")}
        ids = [k.split(":", 1)[1] for k in key if k.startswith(lang + ":")]
        per = defaultdict(lambda: defaultdict(dict))  # who -> system -> id -> errors
        for who, d in ann.items():
            for i in ids:
                if i not in d:
                    continue
                for L, sysname in key[f"{lang}:{i}"].items():
                    per[who][sysname][i] = d[i][L]
        systems = list(key[f"{lang}:{ids[0]}"].values())
        stats = {}
        for who in ann:
            for s in systems:
                errs = per[who][s]
                if not errs:
                    continue
                n = len(errs)
                pen = [sum(W[e["severity"]] for e in es) for es in errs.values()]
                flat = [e for es in errs.values() for e in es]
                stats.setdefault(s, {})[who] = {
                    "segments": n, "mean_penalty": round(sum(pen) / n, 2),
                    "blocking_per_100": round(100 * sum(e["severity"] != "minor" for e in flat) / n, 1),
                    "critical": sum(e["severity"] == "critical" for e in flat),
                    "major": sum(e["severity"] == "major" for e in flat),
                    "minor": sum(e["severity"] == "minor" for e in flat),
                    "accuracy_errors": sum(e["category"].startswith("accuracy") for e in flat),
                    "error_free_pct": round(100 * sum(not es for es in errs.values()) / n, 1)}
        h2h = {}
        for who in ann:
            g = per[who]["governed"]
            for s in systems:
                if s == "governed" or not per[who][s]:
                    continue
                common = [i for i in g if i in per[who][s]]
                pg = {i: sum(W[e["severity"]] for e in g[i]) for i in common}
                ps = {i: sum(W[e["severity"]] for e in per[who][s][i]) for i in common}
                h2h.setdefault(s, {})[who] = {"segments": len(common),
                                              "governed_better": sum(pg[i] < ps[i] for i in common),
                                              "equal": sum(pg[i] == ps[i] for i in common),
                                              "governed_worse": sum(pg[i] > ps[i] for i in common)}
        agree = tot = 0
        for i in ids:
            if i not in ann["claude"] or i not in ann["gemini"]:
                continue
            for x, y in itertools.combinations(systems, 2):
                c = (sum(W[e["severity"]] for e in per["claude"][x][i]) - sum(W[e["severity"]] for e in per["claude"][y][i]))
                m = (sum(W[e["severity"]] for e in per["gemini"][x][i]) - sum(W[e["severity"]] for e in per["gemini"][y][i]))
                if c == 0 and m == 0:
                    continue
                tot += 1
                agree += (c > 0) == (m > 0) and (c < 0) == (m < 0)
        res[lang] = {"stats": stats, "head_to_head": h2h,
                     "annotator_pair_agreement": {"agree": agree, "of": tot,
                                                  "pct": round(100 * agree / tot, 1) if tot else None}}
        print(f"\n### {lang}  (annotators order candidate pairs the same way in {agree}/{tot} cases)")
        print("| System | Annotator | Mean penalty per segment | Major+critical per 100 seg | Critical / major / minor | Error-free segments |")
        print("|---|---|---|---|---|---|")
        for s in systems:
            for who, v in stats.get(s, {}).items():
                print(f"| {NAMES[s]} | {who} | {v['mean_penalty']} | {v['blocking_per_100']} | "
                      f"{v['critical']} / {v['major']} / {v['minor']} | {v['error_free_pct']}% |")
        for s, d in h2h.items():
            for who, v in d.items():
                print(f"  governed vs {s} ({who}): better {v['governed_better']}, equal {v['equal']}, "
                      f"worse {v['governed_worse']} of {v['segments']}")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
