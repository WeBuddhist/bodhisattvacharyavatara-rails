#!/usr/bin/env python3
"""Cross-model review: Gemini checks the term list Claude extracted, batch by batch.

  python3 gemini_review.py <run-dir> [--model gemini-3.1-pro-preview] [--workers 4]

Needs GEMINI_API_KEY (run through `zsh -ic` so ~/.zshrc is read).
For each <run-dir>/batches/batch-NN.json it sends the segments, Claude's terms
for them (from occurrences.json) and the statistical recall flags, and asks
Gemini to drop non-terms, fix badly cut Tibetan spans and add missed terms.
Raw answers go to <run-dir>/review/batch-NN.json, the merged decisions to
<run-dir>/review.json, and every call is logged in the usage ledger.
Apply the result with:  verify.py consolidate <run-dir> --review <run-dir>/review.json
"""
import argparse
import importlib.util
import json
import os
import pathlib
import sys
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

DEFINITION = (HERE / "prompts/extract-agent.md").read_text(encoding="utf-8").split(
    "## What counts as a glossary term", 1)[1].split("## For each term", 1)[0].strip()

SYSTEM = f"""You are reviewing a glossary-term list that another model extracted from a Tibetan Buddhist root text. Each segment gives the Tibetan (`bo`), two English machine translations (`dm`, `gm`), the extracted `terms` (numbered `n`, each with its Tibetan span and the English each translation used), and `flags`: English words that a statistical keyword extractor ranked highly in this segment but that no listed term covers.

The definition of a glossary term the list must follow:

{DEFINITION}

Tibetan spans must be literal substrings of `bo`, covering the term's own syllables, without case particles and without a trailing tsheg or shad where possible.

For each segment report only changes:
- `drop`: terms (by `n`) that are not glossary terms under the definition, with a short reason.
- `fix_span`: terms (by `n`) whose Tibetan span is wrong (includes particles or neighbouring words, or cuts the term); give the corrected literal substring of `bo`.
- `add`: glossary terms in `bo` that no listed term covers (check the `flags` — most are ordinary words, some point to a missed term). Give the literal Tibetan substring, and the English each translation used as a literal substring of `dm` / `gm` (null if absent), with a short reason.
Leave a list empty when nothing needs changing. Be consistent: the same Tibetan term gets the same decision in every segment."""

SCHEMA = {
    "type": "object",
    "properties": {"segments": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "drop": {"type": "array", "items": {"type": "object", "properties": {
                "n": {"type": "integer"}, "reason": {"type": "string"}}, "required": ["n", "reason"]}},
            "fix_span": {"type": "array", "items": {"type": "object", "properties": {
                "n": {"type": "integer"}, "bo_fixed": {"type": "string"}}, "required": ["n", "bo_fixed"]}},
            "add": {"type": "array", "items": {"type": "object", "properties": {
                "bo": {"type": "string"}, "dm": {"type": "string", "nullable": True},
                "gm": {"type": "string", "nullable": True}, "reason": {"type": "string"}},
                "required": ["bo", "reason"]}},
        },
        "required": ["id", "drop", "fix_span", "add"]}}},
    "required": ["segments"],
}


def review_batch(bfile, occ_by_seg, flags, args, key, text_slug, lang):
    batch = json.loads(bfile.read_text(encoding="utf-8"))
    payload, index = [], {}
    for s in batch:
        terms = []
        for n, o in enumerate(occ_by_seg.get(s["id"], []), 1):
            terms.append({"n": n, "bo": o["bo"], "dm": o["dm"], "gm": o["gm"]})
            index[(s["id"], n)] = o
        payload.append({"id": s["id"], "bo": s["bo"], "dm": s["dm"], "gm": s["gm"],
                        "terms": terms, "flags": flags.get(s["id"], {})})
    body = {
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        "contents": [{"role": "user", "parts": [{"text":
            "Review these segments. Return JSON only.\n\n" + json.dumps(payload, ensure_ascii=False)}]}],
        "generationConfig": {"responseMimeType": "application/json", "responseSchema": SCHEMA},
        "safetySettings": gm.SAFETY_OFF,
    }
    t0 = time.time()
    text, info = gm.call_api(body, args, key)
    u = info["usage"]
    ledger.log_call(step="term-review", text=text_slug, lang=lang, engine="gemini-api",
                    model=info["model_version"], batch=bfile.stem, segments=len(batch),
                    tokens={"input": u["prompt_tokens"], "output": u["output_tokens"],
                            "thinking": u["thinking_tokens"]},
                    seconds=round(time.time() - t0, 1), note="Gemini review of Claude term list")
    data = json.loads(text)
    out = {"drop": [], "fix_span": [], "add": []}
    for s in data.get("segments", []):
        sid = s["id"]
        for d in s.get("drop", []):
            o = index.get((sid, d["n"]))
            if o:
                out["drop"].append({"id": sid, "bo": o["bo"], "reason": d["reason"]})
        for f in s.get("fix_span", []):
            o = index.get((sid, f["n"]))
            if o:
                out["fix_span"].append({"id": sid, "bo": o["bo"], "bo_fixed": f["bo_fixed"]})
        for m in s.get("add", []):
            out["add"].append({"id": sid, "bo": m["bo"], "dm": m.get("dm"), "gm": m.get("gm"),
                               "reason": m["reason"]})
    return bfile.stem, data, out, u


def main():
    p = argparse.ArgumentParser()
    p.add_argument("run_dir")
    p.add_argument("--model", default=gm.DEFAULT_MODEL)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--text", default="bodhicaryavatara")
    p.add_argument("--lang", default="en")
    p.add_argument("--only", nargs="*", help="batch stems to (re)run")
    a = p.parse_args()
    key = os.environ.get(gm.KEY_ENV, "")
    if not key:
        sys.exit("GEMINI_API_KEY is not set (run via: zsh -ic 'python3 ...')")
    args = types.SimpleNamespace(model=a.model, retries=6, timeout=900)
    run = pathlib.Path(a.run_dir)
    occ = json.loads((run / "occurrences.json").read_text(encoding="utf-8"))
    occ_by_seg = {}
    for o in occ:
        occ_by_seg.setdefault(o["id"], []).append(o)
    flags_path = run / "recall-flags.json"
    flags = json.loads(flags_path.read_text(encoding="utf-8")) if flags_path.exists() else {}
    (run / "review").mkdir(exist_ok=True)
    todo = sorted((run / "batches").glob("batch-*.json"))
    if a.only:
        todo = [b for b in todo if b.stem in a.only]
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = [ex.submit(review_batch, b, occ_by_seg, flags, args, key, a.text, a.lang) for b in todo]
        for f in futs:
            stem, raw, out, u = f.result()
            (run / "review" / f"{stem}.json").write_text(
                json.dumps({"raw": raw, "decisions": out}, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"{stem}: drop={len(out['drop'])} fix={len(out['fix_span'])} add={len(out['add'])} "
                  f"tokens in/out/think={u['prompt_tokens']}/{u['output_tokens']}/{u['thinking_tokens']}")
    merged = {"drop": [], "fix_span": [], "add": []}
    for f in sorted((run / "review").glob("batch-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))["decisions"]
        for k in merged:
            merged[k] += d[k]
    (run / "review.json").write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
    print({k: len(v) for k, v in merged.items()})


if __name__ == "__main__":
    main()
