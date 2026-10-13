#!/usr/bin/env python3
"""Blind pairwise judgement of fixed segments: Gemini compares the text before the fact-check fix with
the text after it, in random order, without being told which is which.

  zsh -ic 'python3 pairwise_judge.py <pairs.json> --out <judged.json> [--per-call 8] [--workers 4]'

<pairs.json> comes from `improvement.py --pairs`. Context per segment is taken from the track's first
fact-check batch (Tibetan, Sanskrit, commentaries, reference translation, locked terms). Every pair is judged
twice, with A/B swapped (pass 1: random, pass 2: flipped), to cancel position bias. Combined result: win (both
passes prefer the fixed text), loss (both prefer the original), tie (both tie, or the passes disagree).
Resumes: (pair, pass) already in <judged.json> are skipped.

Keep-best rule for minor fixes (user decision 2026-10-07): a fix made for minor issues only is kept when the judge
prefers it or ties; when both passes prefer the original, `--revert-losses` appends a `call_id: revert` row that
restores the original (the text the first check saw and passed). Fixes of major errors are never reverted here.
"""
import argparse
import datetime as _dt
import importlib.util
import json
import os
import pathlib
import random
import sys
import threading
import time
import types
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gm = load("gm_translate", VAULT / "4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py")
ledger = load("usage_ledger", VAULT / "4-SYSTEM/scripts/usage-ledger/usage_ledger.py")
imp = load("improvement", HERE / "improvement.py")

LANG_NAMES = {"en": "English", "zh": "Chinese (Traditional characters)", "hi": "Hindi"}
SYSTEM = """You compare two {lang_name} translations, A and B, of the same segment of the Tibetan Bodhicaryāvatāra (Śāntideva). {register}

For each segment you get the Tibetan source and aids to settle its meaning: {aids}. Decide which translation is better:
1. Fidelity first: does it say what the Tibetan says — no meaning changed, nothing dropped or added, negations, numbers, comparisons and referents right, locked glossary terms used for the right sense?
2. Then {second}.
Answer "A" or "B" when one is better on these criteria, "tie" when they are equally good or the differences do not matter. Do not prefer a version for being longer, more literal, or closer to the reference wording as such. Give a reason of at most 25 words naming the decisive difference."""
REGISTER = {
    "academic": ("The translations are academic study translations: faithful and precise.",
                 "the Sanskrit, passages from three Tibetan commentaries, an approved English academic translation (for zh/hi), and the locked glossary renderings",
                 "precision and clarity of the wording"),
    "children": ("The translations are a children's version (ages 8–12) made from an approved academic translation: simpler wording is intended, not an error.",
                 "the approved academic translation in the same language (the meaning to keep) and the locked children's glossary renderings",
                 "how easily a child of 8–12 can follow it"),
}
SCHEMA = {"type": "object", "properties": {"judgements": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "better": {"type": "string", "enum": ["A", "B", "tie"]},
                                     "reason": {"type": "string"}},
    "required": ["id", "better", "reason"]}}}, "required": ["judgements"]}
LOCK = threading.Lock()


def contexts(track):
    """{id: context dict} from the track's first fact-check batch (without the translation)."""
    out = {}
    for f in sorted((imp.runs(track)[0] / "batches").glob("*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")):
            out[s["id"]] = {k: v for k, v in s.items() if k not in ("translation", "id")}
    return out


def judge(track, group, ctx, args, key, out_path, done, pass_no):
    lang, variant = track.split("-")
    reg, aids, second = REGISTER[variant]
    items = []
    for p in group:
        first = random.Random(f"{track}:{p['id']}").choice("AB")  # fixed per pair, reproducible
        p["after_is"] = first if pass_no == 1 else ("B" if first == "A" else "A")
        a, b = (p["after"], p["before"]) if p["after_is"] == "A" else (p["before"], p["after"])
        items.append({"id": p["id"], **ctx[p["id"]], "A": a, "B": b})
    body = {"systemInstruction": {"parts": [{"text": SYSTEM.format(lang_name=LANG_NAMES[lang], register=reg,
                                                                   aids=aids, second=second)}]},
            "contents": [{"role": "user", "parts": [{"text": json.dumps(items, ensure_ascii=False)
                                                     + "\n\nJudge every segment. Return JSON only."}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": SCHEMA},
            "safetySettings": gm.SAFETY_OFF}
    t0 = time.time()
    text, info = gm.call_api(body, types.SimpleNamespace(model=args.model, retries=6, timeout=900), key)
    u = info["usage"]
    ledger.log_call(step="improvement-judge", text="bodhicaryavatara", lang=lang, variant=variant, engine="gemini-api",
                    model=info["model_version"], batch=f"p{pass_no} {group[0]['id']}..{group[-1]['id']}", segments=len(group),
                    tokens={"input": u["prompt_tokens"], "output": u["output_tokens"], "thinking": u["thinking_tokens"]},
                    seconds=round(time.time() - t0, 1), note="blind pairwise: before vs after fact-check fix")
    got = {j["id"]: j for j in json.loads(text)["judgements"]}
    with LOCK:
        for p in group:
            j = got.get(p["id"])
            if not j:
                continue
            res = "tie" if j["better"] == "tie" else ("win" if j["better"] == p["after_is"] else "loss")
            done[(track, p["id"], pass_no)] = {"track": track, "id": p["id"], "pass": pass_no, "result": res,
                                               "after_was": p["after_is"],
                                      "reason": j["reason"], "before_verdict": p["before_verdict"],
                                      "after_verdict": p["after_verdict"]}
        out_path.write_text(json.dumps(list(done.values()), ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  pass {pass_no} {track} {group[0]['id']}..{group[-1]['id']} ok", flush=True)


def combine(rows):
    """One result per pair from its two passes (pairs with a missing pass are left out)."""
    by = {}
    for r in rows:
        by.setdefault((r["track"], r["id"]), {})[r.get("pass", 1)] = r
    out = []
    for (t, i), ps in by.items():
        if 1 in ps and 2 in ps:
            a, b = ps[1]["result"], ps[2]["result"]
            out.append({"track": t, "id": i, "result": a if a == b else "tie", "consistent": a == b,
                        "passes": [a, b], "reasons": [ps[1]["reason"], ps[2]["reason"]]})
    return out


def summary(rows):
    rows = combine(rows)
    flips = sum(not r["consistent"] for r in rows)
    print(f"pairs={len(rows)}; passes disagreed on {flips} (counted as tie)")
    print("| Track | Pairs | Fixed version better | Tie | Original better |\n|---|---|---|---|---|")
    tracks = sorted({r["track"] for r in rows}, key=lambda t: (t.split("-")[1], ["en", "zh", "hi"].index(t.split("-")[0])))
    for t in tracks + ["all"]:
        rs = [r for r in rows if t == "all" or r["track"] == t]
        n = len(rs)
        c = {k: sum(r["result"] == k for r in rs) for k in ("win", "tie", "loss")}
        print(f"| {t} | {n} | {c['win']} ({100 * c['win'] / n:.0f}%) | {c['tie']} ({100 * c['tie'] / n:.0f}%) | "
              f"{c['loss']} ({100 * c['loss'] / n:.0f}%) |")


def revert_losses(rows, pairs_path):
    """Append a revert row for every minor-only fix whose combined result is a loss. Idempotent."""
    pairs = {(p["track"], p["id"]): p for p in json.loads(pathlib.Path(pairs_path).read_text(encoding="utf-8"))}
    n = 0
    for r in combine(rows):
        p = pairs.get((r["track"], r["id"]))
        if r["result"] != "loss" or not p or p["before_verdict"] != "pass":
            continue
        work = next((imp.TRACKS / r["track"] / "work").glob("*.jsonl"))
        lines = work.read_text(encoding="utf-8").splitlines()
        rows_ = [json.loads(x) for x in lines]
        cur = [x for x in rows_ if x["id"] == r["id"]][-1]
        if cur["translation"] == p["before"]:
            continue  # already restored
        src = [x for x in rows_ if x["id"] == r["id"] and x["translation"] == p["before"]][-1]
        new = dict(src, attempt=9, call_id="revert", ts=_dt.datetime.now().isoformat(timespec="seconds"),
                   note="keep-best (minor fix): blind pairwise judge preferred the original in both A/B orders — "
                        + r["reasons"][0][:200])
        with open(work, "a", encoding="utf-8") as f:
            f.write(json.dumps(new, ensure_ascii=False) + "\n")
        n += 1
        print(f"  reverted {r['track']} {r['id']}")
    print(f"reverted {n} minor-only fixes the judge rated worse")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("pairs")
    p.add_argument("--out", required=True)
    p.add_argument("--model", default=gm.DEFAULT_MODEL)
    p.add_argument("--per-call", type=int, default=8)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--summary-only", action="store_true")
    p.add_argument("--revert-losses", action="store_true",
                   help="after judging, restore the original for minor-only fixes both passes rated worse")
    p.add_argument("--limit", type=int, help="judge at most N calls (trial runs)")
    a = p.parse_args()
    out_path = pathlib.Path(a.out)
    done = {}
    if out_path.exists():
        done = {(r["track"], r["id"], r.get("pass", 1)): r for r in json.loads(out_path.read_text(encoding="utf-8"))}
    if not a.summary_only:
        key = os.environ.get(gm.KEY_ENV, "")
        if not key:
            sys.exit("GEMINI_API_KEY is not set (run via: zsh -ic 'python3 ...')")
        allp = json.loads(pathlib.Path(a.pairs).read_text(encoding="utf-8"))
        jobs, pairs = [], 0
        for pass_no in (1, 2):
            todo = [dict(x) for x in allp if (x["track"], x["id"], pass_no) not in done]
            pairs += len(todo)
            for track in dict.fromkeys(x["track"] for x in todo):
                ctx = contexts(track)
                tp = [x for x in todo if x["track"] == track]
                jobs += [(track, tp[k:k + a.per_call], ctx, pass_no) for k in range(0, len(tp), a.per_call)]
        jobs = jobs[:a.limit] if a.limit else jobs
        print(f"judgements to make={pairs} calls={len(jobs)}", flush=True)
        with ThreadPoolExecutor(a.workers) as ex:
            for f in [ex.submit(judge, t, g, c, a, key, out_path, done, n) for t, g, c, n in jobs]:
                f.result()
    summary(list(done.values()))
    if a.revert_losses:
        revert_losses(list(done.values()), a.pairs)


if __name__ == "__main__":
    main()
