#!/usr/bin/env python3
"""Build fact-check packets for one translation track.

  python3 prep.py --variant academic [--attempt 1] [--only ID ...] [--per-batch 20] [--max-comm 1500]

Each packet segment: id, Tibetan, Sanskrit, aligned commentary passages (trimmed,
de-duplicated within the batch), the locked termbase renderings, and the current
translation. Writes factcheck/<variant>-a<attempt>/batches/batch-NN.json.
"""
import argparse
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
KF = HERE.parent
VAULT = KF.parents[1]
sys.path.insert(0, str(KF / "context"))
from segment_context import build_context  # noqa: E402

spec = importlib.util.spec_from_file_location("tr", KF / "translate/gm_variant_translate.py")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variant", required=True)
    p.add_argument("--lang", default="en")
    p.add_argument("--attempt", type=int, default=1)
    p.add_argument("--only", nargs="*")
    p.add_argument("--per-batch", type=int, default=20)
    p.add_argument("--max-comm", type=int, default=1500)
    a = p.parse_args()
    tr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tr)
    tr.LANG = a.lang
    rows = tr.latest(tr.work_file(a.lang, a.variant))
    segs = json.loads((tr.TERM_RUN / "segments.json").read_text(encoding="utf-8"))
    ctx = build_context(tr.ROOT)
    terms = tr.locked_terms(a.variant)
    ids = a.only or [s["id"] for s in segs if not s["heading"] and s["id"] in rows]
    segmap = {s["id"]: s for s in segs}
    base = None
    if a.variant == "children":  # checked against the approved academic version, not the commentaries
        base = tr.latest(tr.work_file(a.lang, "academic"))
    en_ref = tr.latest(tr.work_file("en", "academic")) if a.lang != "en" and a.variant != "children" else {}
    out = HERE / (f"{a.variant}-a{a.attempt}" if a.lang == "en" else f"{a.lang}-{a.variant}-a{a.attempt}")
    (out / "batches").mkdir(parents=True, exist_ok=True)
    for f in (out / "batches").glob("*.json"):
        f.unlink()
    n = 0
    for b in range(0, len(ids), a.per_batch):
        batch, seen = [], set()
        for i in ids[b:b + a.per_batch]:
            if base is not None:
                batch.append({"id": i, "tibetan": segmap[i]["bo"], "academic_translation": base[i]["translation"],
                              "locked_terms": [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])],
                              "translation": rows[i]["translation"]})
                continue
            c = ctx.get(i, {})
            comms = {}
            for cid, ps in (c.get("commentaries") or {}).items():
                for q in ps:
                    if (cid, q["id"]) in seen:
                        comms.setdefault(cid, []).append({"id": q["id"], "text": "(same passage as above)"})
                        continue
                    seen.add((cid, q["id"]))
                    t = q["text"]
                    comms.setdefault(cid, []).append({"id": q["id"], "text": t if len(t) <= a.max_comm else t[:a.max_comm] + " …"})
            batch.append({"id": i, "tibetan": segmap[i]["bo"],
                          "sanskrit": " ".join(x["text"] for x in c.get("sa", [])) or None,
                          "commentaries": comms, "locked_terms": [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])],
                          **({"english_academic": en_ref[i]["translation"]} if i in en_ref else {}),
                          "translation": rows[i]["translation"]})
        n += 1
        (out / "batches" / f"batch-{n:02d}.json").write_text(json.dumps(batch, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"segments={len(ids)} batches={n} -> {out}")


if __name__ == "__main__":
    main()
