#!/usr/bin/env python3
"""Build term packets for a non-English termbase, pivoting on the approved English termbase.

  python3 prep_lang.py --lang zh [--per-batch 47] [--examples 3]

Each packet: term_id, Tibetan, Sanskrit, the English academic/children renderings per
sense (with the occurrence ids of each sense), and up to N example segments with the
Tibetan plus, where available, Kumārajīva's aligned classical Chinese (zh only) and the
Gemini zero-shot line in the target language. Writes termbase/bodhicaryavatara-<lang>/.
"""
import argparse
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parents[2]
EN = HERE / "bodhicaryavatara-en"
TERM_RUN = HERE.parent / "term-extract/bodhicaryavatara-en"


def zero_shot(lang):
    p = VAULT / f"3-TRANSFORMATIONS/Translations/Gemini/{lang}/work/bo-བློ་ལྡན་ཤེས་རབ།-{lang}.jsonl"
    out = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("translation"):
                t = r["translation"]
                out[r["block_id"]] = " ".join(t) if isinstance(t, list) else t
    return out


def kumarajiva():
    """Diamond Sutra only; the Bodhicaryāvatāra's human Chinese versions stay out of the pipeline."""
    f = VAULT / "1-SOURCES/Annotations/lzh-bodhicaryavatara.annotations.json"
    if not f.exists():
        return {}
    a = json.loads(f.read_text(encoding="utf-8"))
    out = {}
    for b in a["blocks"].values():
        for t in b.get("targets") or []:
            out[t] = (out.get(t, "") + " " + b.get("text", "")).strip()
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lang", required=True)
    p.add_argument("--per-batch", type=int, default=47)
    p.add_argument("--examples", type=int, default=3)
    a = p.parse_args()
    tb = json.loads((EN / "termbase.json").read_text(encoding="utf-8"))
    src = {t["term_id"]: t for t in json.loads((EN / "terms.json").read_text(encoding="utf-8"))}
    segs = {s["id"]: s for s in json.loads((TERM_RUN / "segments.json").read_text(encoding="utf-8"))}
    zs = zero_shot(a.lang)
    kj = kumarajiva() if a.lang == "zh" else {}
    packets = []
    for e in tb:
        senses = [{"sense": s["sense"], "occurrences": s["occurrences"], "en_academic": s["academic"],
                   "en_children": s["children"]} for s in e["senses"]]
        ex = []
        for x in src[e["term_id"]]["examples"][: a.examples]:
            item = {"id": x["id"], "bo": segs[x["id"]]["bo"]}
            if x["id"] in kj:
                item["kumarajiva"] = kj[x["id"]]
            if x["id"] in zs:
                item["gemini_zero_shot"] = zs[x["id"]]
            ex.append(item)
        packets.append({"term_id": e["term_id"], "bo": e["bo"], "sanskrit": e.get("sanskrit"), "count": e["count"],
                        "occurrences": e["occurrences"], "senses": senses, "examples": ex})
    out = HERE / f"bodhicaryavatara-{a.lang}"
    for d in ("batches", "agents", "rendered"):
        (out / d).mkdir(parents=True, exist_ok=True)
    (out / "terms.json").write_text(json.dumps(packets, ensure_ascii=False, indent=1), encoding="utf-8")
    n = -(-len(packets) // a.per_batch)
    for b in range(n):
        (out / "batches" / f"batch-{b + 1:02d}.json").write_text(
            json.dumps(packets[b::n], ensure_ascii=False, indent=1), encoding="utf-8")
    ov = ["| id | Tibetan | Sanskrit | count | English academic / children's (per sense) |", "|---|---|---|---|---|"]
    for t in packets:
        ov.append(f"| {t['term_id']} | {t['bo']} | {t['sanskrit'] or ''} | {t['count']} | " +
                  "; ".join(f"{s['sense']}: {s['en_academic']} / {s['en_children']}" for s in t["senses"]) + " |")
    (out / "overview.md").write_text("\n".join(ov) + "\n", encoding="utf-8")
    print(f"lang={a.lang} terms={len(packets)} batches={n} zero-shot lines={len(zs)} kumarajiva segments={len(kj)}")


if __name__ == "__main__":
    main()
