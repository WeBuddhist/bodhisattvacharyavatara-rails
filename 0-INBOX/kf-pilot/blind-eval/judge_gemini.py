#!/usr/bin/env python3
"""Gemini MQM annotation of the blind sample, with the same rubric as the Claude annotators.

  zsh -ic 'python3 judge_gemini.py [--per-call 10] [--workers 4]'

Reads sample-<lang>-NN.json, writes gemini/<lang>-NN.json in the same format as claude/<lang>-NN.json.
Resumes: segments already annotated are skipped.
"""
import argparse
import importlib.util
import json
import os
import pathlib
import subprocess
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
LANG_NAMES = {"en": "English", "zh": "Chinese", "hi": "Hindi"}
CATS = ["accuracy/mistranslation", "accuracy/omission", "accuracy/addition", "terminology", "fluency", "style"]
ERR = {"type": "object", "properties": {"category": {"type": "string", "enum": CATS},
                                        "severity": {"type": "string", "enum": ["minor", "major", "critical"]},
                                        "span": {"type": "string"}, "explanation": {"type": "string"}},
       "required": ["category", "severity", "span", "explanation"]}
LOCK = threading.Lock()


def schema(letters):
    return {"type": "object", "properties": {"segments": {"type": "array", "items": {
        "type": "object", "properties": {"id": {"type": "string"}, "candidates": {
            "type": "object", "properties": {L: {"type": "array", "items": ERR} for L in letters},
            "required": list(letters)}}, "required": ["id", "candidates"]}}}, "required": ["segments"]}


def annotate(sample_path, chunk, args, key, done):
    lang = sample_path.stem.split("-")[1]
    letters = sorted(chunk[0]["candidates"])
    rubric = (HERE / "rubric-mqm.md").read_text(encoding="utf-8").format(
        lang_name=LANG_NAMES[lang], n_cand=len(letters), letters=", ".join(letters))
    body = {"systemInstruction": {"parts": [{"text": rubric}]},
            "contents": [{"role": "user", "parts": [{"text": json.dumps(chunk, ensure_ascii=False)
                                                     + "\n\nAnnotate every segment and every candidate. Return JSON only."}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": schema(letters)},
            "safetySettings": gm.SAFETY_OFF}
    t0 = time.time()
    text, info = gm.call_api(body, types.SimpleNamespace(model=args.model, retries=6, timeout=900), key)
    u = info["usage"]
    ledger.log_call(step="blind-eval", text="bodhicaryavatara", lang=lang, engine="gemini-api", model=info["model_version"],
                    batch=f"{sample_path.stem} {chunk[0]['id']}..{chunk[-1]['id']}", segments=len(chunk),
                    tokens={"input": u["prompt_tokens"], "output": u["output_tokens"], "thinking": u["thinking_tokens"]},
                    seconds=round(time.time() - t0, 1), note="blind MQM annotation (Gemini side)")
    got = {s["id"]: s for s in json.loads(text)["segments"]}
    with LOCK:
        for s in chunk:
            if s["id"] in got:
                done[sample_path.stem][s["id"]] = got[s["id"]]
    print(f"  {sample_path.stem} {chunk[0]['id']}..{chunk[-1]['id']} ok", flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default=gm.DEFAULT_MODEL)
    p.add_argument("--per-call", type=int, default=10)
    p.add_argument("--workers", type=int, default=4)
    a = p.parse_args()
    key = os.environ.get(gm.KEY_ENV, "")
    if not key:
        sys.exit("GEMINI_API_KEY is not set (run via: zsh -ic 'python3 ...')")
    samples = sorted(HERE.glob("sample-*.json"))
    done, jobs = {}, []
    for sp in samples:
        out = HERE / "gemini" / f"{sp.stem.removeprefix('sample-')}.json"
        prev = {s["id"]: s for s in json.loads(out.read_text(encoding="utf-8"))["segments"]} if out.exists() else {}
        done[sp.stem] = prev
        todo = [s for s in json.loads(sp.read_text(encoding="utf-8")) if s["id"] not in prev]
        jobs += [(sp, todo[k:k + a.per_call]) for k in range(0, len(todo), a.per_call)]
    print(f"calls={len(jobs)}", flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        for f in [ex.submit(annotate, sp, ch, a, key, done) for sp, ch in jobs]:
            f.result()
    for sp in samples:
        order = [s["id"] for s in json.loads(sp.read_text(encoding="utf-8"))]
        out = HERE / "gemini" / f"{sp.stem.removeprefix('sample-')}.json"
        out.write_text(json.dumps({"segments": [done[sp.stem][i] for i in order if i in done[sp.stem]]},
                                  ensure_ascii=False, indent=1), encoding="utf-8")
        r = subprocess.run([sys.executable, str(HERE / "check.py"), str(sp), str(out)], capture_output=True, text=True)
        print(sp.stem, r.stdout.strip()[:300])


if __name__ == "__main__":
    main()
