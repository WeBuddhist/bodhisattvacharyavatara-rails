#!/usr/bin/env python3
"""Blind MQM comparison: governed academic vs zero-shot vs human, on a fixed sample of Bodhicaryāvatāra verses.

  python3 build.py [--n 40] [--per-agent 20] [--seed 7]

Picks n verses (ids `<chapter>-<verse>`; no headings, no I-/a-/b- blocks) spread evenly over the text (one at
random from each of n equal slices, seeded), the same ids in every language. Per language the candidates are:
  en: governed academic, DharmaMitra zero-shot, Gemini zero-shot, human: Padmakara 2006
  zh: governed academic, Gemini zero-shot, human: 如石 (classical Chinese verse)
  hi: governed academic, Gemini zero-shot
Each verse's candidates are shuffled to letters A, B, C, D (seeded). Annotators see the Tibetan (with the
neighbouring verses), the Sanskrit and the commentaries (Kunpal, Shenga, Gyaltsab) — no glossary and no English
reference, which would favour the governed version. Writes sample-<lang>-NN.json (what annotators see), key.json
(letter -> system, never shown), prompts/<lang>-NN.md (Claude annotator prompts).

Human alignment: Padmakara and 如石 number their verses by the Sanskrit-based edition (ch. 3 has 34, ch. 7 76,
ch. 8 187 verses), not by this Tibetan root. Padmakara's file carries a transclusion of the Tibetan verse above each
block, so a Tibetan id is mapped to Padmakara's own block id through it; 如石 has no transclusions but uses the same
numbering as Padmakara (checked at ch. 3, 7 and 8), so it is mapped through the same table. Padmakara/如石 3-3 is the
second half of Tibetan 3-2 and is appended to it; their 7-62, 8-51 and 8-186 have no Tibetan counterpart.
"""
import argparse
import importlib.util
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
KF = HERE.parent
VAULT = KF.parents[1]
sys.path.insert(0, str(KF / "context"))
from segment_context import blocks, build_context  # noqa: E402

_spec = importlib.util.spec_from_file_location("tr", KF / "translate" / "gm_variant_translate.py")
tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tr)

LANG_NAMES = {"en": "English", "zh": "Chinese", "hi": "Hindi"}
SPLIT = {"3-3": "3-2"}  # human block (own numbering) -> Tibetan verse it completes


def human_lines(stem):
    """{Tibetan verse id: human translation}, mapped through Padmakara's transclusions (see the module doc)."""
    _, above = blocks("1-SOURCES/Translations/en-Padmakara_2006.md", with_trans=True)
    own_to_tib = {k: v[0] for k, v in above.items() if len(v) == 1}
    text = blocks(f"1-SOURCES/Translations/{stem}.md")
    out = {}
    for own, t in text.items():
        tib = own_to_tib.get(own) or SPLIT.get(own)
        if tib and t.strip():
            out[tib] = (out.get(tib, "") + " " + t).strip()
    return out


def dharmamitra_lines():
    """DharmaMitra en zero-shot (3-TRANSFORMATIONS/Translations/Dharmamitra/en), latest row per block id."""
    p = VAULT / f"3-TRANSFORMATIONS/Translations/Dharmamitra/en/work/{tr.ROOT}-en.jsonl"
    out = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        t = r.get("translation")
        if t:
            out[r["block_id"]] = " ".join(t) if isinstance(t, list) else t
    return out


def candidates(lang):
    gov = {i: r["translation"] for i, r in tr.latest(tr.work_file(lang, "academic")).items()}
    gm = tr.zero_shot_lines(lang)
    if lang == "en":
        return {"governed": gov, "zeroshot-dharmamitra": dharmamitra_lines(), "zeroshot-gemini": gm,
                "human-padmakara": human_lines("en-Padmakara_2006")}
    if lang == "zh":
        return {"governed": gov, "zeroshot-gemini": gm, "human-rushi": human_lines("zh-如石法師")}
    return {"governed": gov, "zeroshot-gemini": gm}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=40)
    p.add_argument("--per-agent", type=int, default=20)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--max-comm", type=int, default=1500)
    a = p.parse_args()
    segs = json.loads((tr.TERM_RUN / "segments.json").read_text(encoding="utf-8"))
    segmap = {s["id"]: s for s in segs}
    cands = {lang: candidates(lang) for lang in ("en", "zh", "hi")}
    verses = [s["id"] for s in segs if not s["heading"] and re.fullmatch(r"\d+-\d+", s["id"])]
    eligible = [i for i in verses if all((t.get(i) or "").strip() for c in cands.values() for t in c.values())]
    for lang, c in cands.items():
        for name, t in c.items():
            miss = [i for i in verses if not (t.get(i) or "").strip()]
            if miss:
                print(f"  {lang} {name}: no text for {len(miss)} verses {miss[:10]}")
    rng = random.Random(a.seed)
    k = len(eligible) / a.n
    ids = [eligible[int(j * k) + rng.randrange(max(1, int(k)))] for j in range(a.n)]
    ctx = build_context(tr.ROOT)
    key = {}
    order_ids = [x["id"] for x in segs]
    (HERE / "prompts").mkdir(exist_ok=True)
    for lang, systems in cands.items():
        items = []
        for i in ids:
            c = ctx.get(i, {})
            comms = {cid: [q["text"] if len(q["text"]) <= a.max_comm else q["text"][:a.max_comm] + " …" for q in ps]
                     for cid, ps in (c.get("commentaries") or {}).items()}
            order = list(systems)
            random.Random(f"{a.seed}:{lang}:{i}").shuffle(order)
            letters = dict(zip("ABCD", order))
            key[f"{lang}:{i}"] = letters
            pos = order_ids.index(i)
            items.append({"id": i, "tibetan": segmap[i]["bo"],
                          "tibetan_previous_segment": segs[pos - 1]["bo"] if pos else None,
                          "tibetan_next_segment": segs[pos + 1]["bo"] if pos + 1 < len(segs) else None,
                          "sanskrit": " ".join(x["text"] for x in c.get("sa", [])) or None,
                          "commentaries": comms,
                          "candidates": {L: systems[s][i] for L, s in letters.items()}})
        for b in range(0, len(items), a.per_agent):
            n = b // a.per_agent + 1
            path = HERE / f"sample-{lang}-{n:02d}.json"
            path.write_text(json.dumps(items[b:b + a.per_agent], ensure_ascii=False, indent=1), encoding="utf-8")
            rubric = (HERE / "rubric-mqm.md").read_text(encoding="utf-8").format(
                lang_name=LANG_NAMES[lang], n_cand=len(systems), letters=", ".join("ABCD"[:len(systems)]))
            prompt = (HERE / "prompt-mqm.md").read_text(encoding="utf-8").format(
                rubric=rubric.strip(), input_path=path, out_path=HERE / "claude" / f"{lang}-{n:02d}.json",
                check_script=HERE / "check.py")
            (HERE / "prompts" / f"{lang}-{n:02d}.md").write_text(prompt, encoding="utf-8")
    (HERE / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "claude").mkdir(exist_ok=True)
    (HERE / "gemini").mkdir(exist_ok=True)
    print(f"verses={len(verses)} eligible={len(eligible)} sample={len(ids)}: {ids}")


if __name__ == "__main__":
    main()
