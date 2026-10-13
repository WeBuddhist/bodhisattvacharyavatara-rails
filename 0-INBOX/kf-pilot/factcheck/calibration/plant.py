#!/usr/bin/env python3
"""Checker reliability test (calibration): plant one known error in 18 of 24 academic segments.

  python3 plant.py [en zh hi]   -> calibration{,-zh,-hi}/{sample-raw,batch-cal,key}.json + prompt.md

Design as for the Diamond Sutra and the Ratnaguṇa: 24 segments, spread over the ten chapters, whose CURRENT
academic text (latest row per id in 3-TRANSFORMATIONS/Translations/<lang>-academic/work/*.jsonl) passed the
fact-check with no issue at all, in all three languages (en academic-a1..a3, zh zh-academic-a1/a2,
hi hi-academic-a1..a3; a verdict counts only if the check saw that exact text). 18 get one planted error
(9 negations, 2 numbers, 2 locked-term swaps, 2 wrong words, 1 name, 1 omission, 1 addition), 6 are clean
controls; the same kind at the same id in every language. Packets are built as factcheck/prep.py builds them
(one batch of 24, so commentary passages are de-duplicated within the batch); zh/hi carry the current, unplanted
English academic text as `english_academic`, as in the real zh/hi checks.
Score a finished run with:  python3 score.py <calibration-dir>
"""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FC = HERE.parent
KF = FC.parent
sys.path.insert(0, str(KF / "context"))
from segment_context import build_context  # noqa: E402

_spec = importlib.util.spec_from_file_location("tr", KF / "translate" / "gm_variant_translate.py")
tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tr)

RUNS = {"en": ["academic-a1", "academic-a2", "academic-a3"], "zh": ["zh-academic-a1", "zh-academic-a2"],
        "hi": ["hi-academic-a1", "hi-academic-a2", "hi-academic-a3"]}
OUT = {"en": HERE, "zh": FC / "calibration-zh", "hi": FC / "calibration-hi"}
LANG_NAMES = {"zh": "Chinese (Traditional characters)", "hi": "Hindi (Devanagari)"}
MAX_COMM = 1500
SEV = {"negation": "critical"}  # every other kind: major

# Controls (no plant): one seeded random zero-issue segment from chapters 1, 3, 5, 6, 9, 10.
CONTROLS = ["1-31", "3-18", "5-57", "6-121", "9-7", "10-55"]
# id -> kind, then (old, new) per language. `old` must occur exactly once in that segment's translation.
PLANTS = {
    "1-8": ("negation", {"en": ("Should never forsake bodhicitta", "Should forsake bodhicitta"),
                         "zh": ("恆時皆不應捨棄菩提心", "恆時皆應捨棄菩提心"),
                         "hi": ("बोधिचित्त का कभी त्याग न करें", "बोधिचित्त का त्याग करें")}),
    "2-5": ("mistranslation", {"en": ("swans", "peacocks"),  # ངང་པ swan (Kunpal: ངང་པ་དང་བཞད)
                               "zh": ("天鵝", "孔雀"),
                               "hi": ("हंसों", "मोरों")}),
    "2-41": ("negation", {"en": ("I have not relied upon even that", "I have relied upon that"),
                          "zh": ("然我亦未曾依止彼", "然我亦曾依止彼"),
                          "hi": ("तो मैंने उसका भी आश्रय नहीं लिया", "तो मैंने उसका भी आश्रय लिया")}),
    "3-5": ("negation", {"en": ("Do not leave these wandering beings in blindness",
                                "Leave these wandering beings in blindness"),
                         "zh": ("莫將這些眾生置於盲目之中", "將這些眾生置於盲目之中"),
                         "hi": ("अंधा न छोड़कर", "अंधा छोड़कर")}),
    "4-19": ("number", {"en": ("a hundred ten-million eons", "a hundred thousand eons"),  # བསྐལ་པ་བྱེ་བ་བརྒྱ
                        "zh": ("百俱胝劫", "十萬劫"),
                        "hi": ("सौ करोड़ कल्पों", "एक लाख कल्पों")}),
    "4-28": ("omission", {"en": (", craving", ""),  # སྲེད (Skt tṛṣṇā) dropped
                          "zh": ("、渴愛", ""),
                          "hi": (", तृष्णा", "")}),
    "5-83": ("negation", {"en": ("One should not forsake the greater", "One should forsake the greater"),
                          "zh": ("不應為小而捨大", "應為小而捨大"),
                          "hi": ("बड़े का त्याग न करे", "बड़े का त्याग करे")}),
    "5-96": ("terminology", {"en": ("introspection", "vigilance"),  # ཤེས་བཞིན locked
                             "zh": ("正知", "警覺"),
                             "hi": ("सम्प्रजन्य", "सतर्कता")}),
    "6-1": ("number", {"en": ("a thousand eons", "ten eons"),  # བསྐལ་པ་སྟོང (Gyaltsab: བརྒྱ་དང་སྟོང)
                       "zh": ("千劫", "十劫"),
                       "hi": ("सहस्र कल्पों", "दस कल्पों")}),
    "6-128": ("negation", {"en": ("do not harm him in return", "harm him in return"),
                           "zh": ("雖有能力亦不予報復", "雖有能力亦予報復"),
                           "hi": ("हानि नहीं पहुँचाते हैं", "हानि पहुँचाते हैं")}),
    "7-14": ("mistranslation", {"en": ("boat of a human body", "boat of a divine body"),  # མི་ཡི་གྲུ
                                "zh": ("依靠人身", "依靠天身"),
                                "hi": ("मनुष्य की नौका", "देव की नौका")}),
    "7-21": ("negation", {"en": ("Yet I will not attain awakening", "Yet I will attain awakening"),
                          "zh": ("卻不會獲得菩提", "卻會獲得菩提"),
                          "hi": ("बोधि प्राप्त नहीं कर पाऊँगा", "बोधि प्राप्त कर पाऊँगा")}),
    "8-4": ("terminology", {"en": ("special insight", "superior insight"),  # ལྷག་མཐོང locked
                            "zh": ("勝觀", "觀照"),
                            "hi": ("विपश्यना", "अन्तर्दृष्टि")}),
    "8-32": ("negation", {"en": ("Since others do not take a share", "Since others take a share"),
                          "zh": ("他人既不分擔苦", "他人既分擔苦"),
                          "hi": ("यदि दुःख का भाग अन्य नहीं लेते", "यदि दुःख का भाग अन्य लेते")}),
    "8-84": ("addition", {"en": ("Within peaceful forests", "Within peaceful forests and mountain caves"),
                          "zh": ("之寂靜森林中", "之寂靜森林與山洞中"),
                          "hi": ("शान्त वनों के भीतर", "शान्त वनों और पर्वत-गुफाओं के भीतर")}),
    "9-2": ("negation", {"en": ("Ultimate truth is not the domain", "Ultimate truth is the domain"),
                         "zh": ("勝義諦不是智的行境", "勝義諦是智的行境"),
                         "hi": ("परमार्थ बुद्धि का विषय नहीं है", "परमार्थ बुद्धि का विषय है")}),
    "9-17": ("negation", {"en": ("the mind does not see the mind", "the mind sees the mind"),
                          "zh": ("以心不能見於心", "以心能見於心"),
                          "hi": ("चित्त से चित्त नहीं देखा जाता", "चित्त से चित्त देखा जाता है")}),
    "10-51": ("name", {"en": ("Mañjuśrī", "Avalokiteśvara"),  # འཇམ་དབྱངས
                       "zh": ("文殊師利", "觀世音"),
                       "hi": ("मञ्जुश्री", "अवलोकितेश्वर")}),
}


def run_rows(run):
    """[(id, translation the check saw, verdict)] for one fact-check run (as in improvement.py)."""
    text = {}
    for f in sorted((run / "batches").glob("*.json")):
        for s in json.loads(f.read_text(encoding="utf-8")):
            text[s["id"]] = s["translation"]
    out = []
    for f in sorted((run / "agents").glob("*.json")):
        for v in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            if v["id"] in text:
                out.append((v["id"], text[v["id"]], v))
    return out


def current(lang):
    return {i: r["translation"] for i, r in tr.latest(tr.work_file(lang, "academic")).items()}


def verdict_of_current(lang, cur):
    seen = {}
    for r in RUNS[lang]:
        for i, t, v in run_rows(FC / r):
            seen[(i, t)] = v
    return {i: seen.get((i, t)) for i, t in cur.items()}


def main(langs):
    segs = json.loads((tr.TERM_RUN / "segments.json").read_text(encoding="utf-8"))
    order = [s["id"] for s in segs]
    segmap = {s["id"]: s for s in segs}
    ids = sorted(list(PLANTS) + CONTROLS, key=order.index)
    assert len(ids) == 24 and len(PLANTS) == 18
    ctx = build_context(tr.ROOT)
    en_cur = current("en")
    for lang in langs:
        tr.LANG = lang
        cur = current(lang)
        ver = verdict_of_current(lang, cur)
        terms = tr.locked_terms("academic", lang)
        for i in ids:
            v = ver[i]
            assert v and v["verdict"] == "pass" and not v["issues"], (lang, i, "current text not passed cleanly")
        raw, seen = [], set()
        for i in ids:
            c = ctx.get(i, {})
            comms = {}
            for cid, ps in (c.get("commentaries") or {}).items():
                for q in ps:
                    if (cid, q["id"]) in seen:
                        comms.setdefault(cid, []).append({"id": q["id"], "text": "(same passage as above)"})
                        continue
                    seen.add((cid, q["id"]))
                    t = q["text"]
                    comms.setdefault(cid, []).append({"id": q["id"], "text": t if len(t) <= MAX_COMM else t[:MAX_COMM] + " …"})
            raw.append({"id": i, "tibetan": segmap[i]["bo"],
                        "sanskrit": " ".join(x["text"] for x in c.get("sa", [])) or None,
                        "commentaries": comms,
                        "locked_terms": [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])],
                        **({"english_academic": en_cur[i]} if lang != "en" else {}),
                        "translation": cur[i]})
        out = OUT[lang]
        out.mkdir(exist_ok=True)
        (out / "sample-raw.json").write_text(json.dumps(raw, ensure_ascii=False, indent=1), encoding="utf-8")
        key, cal = {}, []
        for s in raw:
            s = dict(s)
            if s["id"] in PLANTS:
                kind, per = PLANTS[s["id"]]
                old, new = per[lang]
                assert s["translation"].count(old) == 1, (lang, s["id"], old, s["translation"].count(old))
                s["translation"] = s["translation"].replace(old, new)
                key[s["id"]] = {"planted": True, "kind": kind, "severity": SEV.get(kind, "major"), "old": old, "new": new}
            else:
                key[s["id"]] = {"planted": False}
            cal.append(s)
        (out / "batch-cal.json").write_text(json.dumps(cal, ensure_ascii=False, indent=1), encoding="utf-8")
        (out / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
        tpl = (FC / "prompts" / ("factcheck-agent.md" if lang == "en" else "factcheck-agent-lang.md")).read_text(encoding="utf-8")
        (out / "prompt.md").write_text(tpl.format(
            batch_path=out / "batch-cal.json", out_path=out / "agent-out.json", batch_name="calibration",
            check_script=FC / "check.py", lang_name=LANG_NAMES.get(lang, "English")), encoding="utf-8")
        print(f"{lang}: {sum(v['planted'] for v in key.values())} planted, "
              f"{sum(not v['planted'] for v in key.values())} controls -> {out}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["en", "zh", "hi"])
