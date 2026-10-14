#!/usr/bin/env python3
"""Before/after quality of each translation track: first fact-check vs the final text.

  python3 improvement.py [--text-syllables 10680] [--json out.json]

BEFORE = the first full fact-check of the track (run "a1").
AFTER  = for each segment, the verdict of the latest check that saw the segment's CURRENT text
         (matched on the exact translation string in the check's batch file, so reverts and
         term-retries are handled). A current text that no check has seen is reported as unchecked
         and keeps its latest verdict.

Measures, each BEFORE (text the first check saw) vs AFTER (current text):
  1. fact-check: failing segments, issues by severity, issues per 100 segments, MQM-style penalty
     (minor = 1, major = 5, critical = 10 points) per 1,000 Tibetan syllables, error-free segments;
  2. locked-term compliance (the translator's automatic glossary check);
  3. chrF (character 6-grams, beta 2) against a human reference, where one is aligned by segment:
     Bodhicaryāvatāra: en vs Padmakara, Wallace, Choephel; zh vs 如石, 蔣揚仁欽, 隆蓮 (classical verse,
     Traditional; 索達吉 is Simplified and left out). None was shown to the translator. One score per
     reference plus their mean;
  4. blind pairwise judgement of the changed segments: see pairwise_judge.py (reads --pairs).
"""
import argparse
import glob
import importlib.util
import json
import pathlib
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parents[2]
TRACKS = HERE.parents[2] / "3-TRANSFORMATIONS" / "Translations"
WEIGHT = {"minor": 1, "major": 5, "critical": 10}
sys.argv_saved, sys.argv = sys.argv, sys.argv[:1]  # the translate module parses nothing at import, but be safe
_spec = importlib.util.spec_from_file_location("tr", HERE.parent / "translate" / "gm_variant_translate.py")
tr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tr)
sys.argv = sys.argv_saved
# track -> run-dir prefix ("academic-a1", "zh-academic-a2", ...)
PREFIX = {"en-academic": "academic", "en-children": "children"}


def runs(track):
    pre = PREFIX.get(track, track)
    return sorted(p for p in HERE.glob(f"{pre}-a*") if p.is_dir() and (p / "batches").exists())


def run_rows(run):
    """[(id, translation checked, verdict dict)] for one check run."""
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


def current(track):
    rows = {}
    for f in glob.glob(str(TRACKS / track / "work" / "*.jsonl")):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            rows[r["id"]] = r["translation"]
    return rows


def score(verdicts):
    iss = [i for v in verdicts for i in v["issues"]]
    return {"segments": len(verdicts),
            "fail": sum(v["verdict"] == "fail" for v in verdicts),
            "error_free": sum(not v["issues"] for v in verdicts),
            "critical": sum(i["severity"] == "critical" for i in iss),
            "major": sum(i["severity"] == "major" for i in iss),
            "minor": sum(i["severity"] == "minor" for i in iss),
            "penalty": sum(WEIGHT[i["severity"]] for i in iss)}


def compliance(track, texts):
    lang, variant = track.split("-")
    tr.LANG = lang
    terms = tr.locked_terms(variant, lang)
    req = sum(len(terms.get(i, [])) for i in texts)
    used = sum(tr.complies(t["rendering"], texts[i], lang) for i in texts for t in terms.get(i, []))
    return {"required": req, "used": used, "pct": round(100 * used / req, 2) if req else None}


def chrf(hyps, refs, n=6, beta=2.0):
    """Corpus chrF (sacrebleu-style: per-order precision/recall averaged, then F-beta), 0-100."""
    match, hyp_tot, ref_tot = [0] * n, [0] * n, [0] * n
    for h, r in zip(hyps, refs):
        h, r = "".join(h.split()), "".join(r.split())
        for k in range(1, n + 1):
            hc = Counter(h[j:j + k] for j in range(len(h) - k + 1))
            rc = Counter(r[j:j + k] for j in range(len(r) - k + 1))
            match[k - 1] += sum((hc & rc).values())
            hyp_tot[k - 1] += sum(hc.values())
            ref_tot[k - 1] += sum(rc.values())
    orders = [k for k in range(n) if hyp_tot[k] and ref_tot[k]]
    if not orders:
        return None
    prec = sum(match[k] / hyp_tot[k] for k in orders) / len(orders)
    rec = sum(match[k] / ref_tot[k] for k in orders) / len(orders)
    if not prec + rec:
        return 0.0
    return round(100 * (1 + beta ** 2) * prec * rec / (beta ** 2 * prec + rec), 2)


HUMAN = {  # Bodhicaryāvatāra: block-aligned human translations in 1-SOURCES/Translations (never shown to the pipeline)
    "en": {"Padmakara 2006": "en-Padmakara_2006", "Wallace": "en-Wallace", "Choephel": "en-David_Karma_Choephel"},
    "zh": {"如石": "zh-如石法師", "蔣揚仁欽": "zh-蔣揚仁欽譯師", "隆蓮": "zh-隆蓮法師"},
}


# Alignment of the human translations to the Tibetan verse ids (fixed 2026-10-08; before, each file was read by
# its OWN block ids, which follow other editions' numbering and were 1-2 verses off in ch. 2, 3, 7, 8, 9, 10).
# - Padmakara, Choephel: through the Tibetan verse each block transcludes (checked against the content:
#   99% agreement with a similarity alignment); blocks without a transclusion are verses the Tibetan root lacks
#   (7-62, 8-51, 8-186 ...) and are dropped, except own 3-3, the second half of Tibetan 3-2, which is joined to it.
# - 如石 (no transclusions) and 蔣揚仁欽 (transclusions wrong at 8-48..8-51 and 9-44..9-51): same numbering as
#   Padmakara (99% agreement by content) -> Padmakara's table, except that both keep the Sanskrit order of
#   9-44..9-51 (CH9_ZH below; Padmakara reorders these to the Tibetan).
# - Wallace, 隆蓮: their transclusions just repeat their own numbers, which are wrong after the first divergence,
#   so they are mapped by the offset rules below (from a content alignment, change points checked by hand).
# Several own blocks mapped to one Tibetan verse are joined in file order.
SPLIT_HALF = {"3-3": "3-2"}
TRANSCLUDED = {"en-Padmakara_2006", "en-David_Karma_Choephel"}
PADMAKARA_NUMBERED = {"zh-如石法師", "zh-蔣揚仁欽譯師"}
CH9_ZH = {"9-44": "9-49", "9-45": "9-50", "9-46": "9-51", "9-47": "9-44", "9-48": "9-45", "9-49": "9-46",
          "9-50": "9-47", "9-51": "9-48"}


def _padmakara_table():
    from segment_context import blocks  # noqa: E402
    _, above = blocks("1-SOURCES/Translations/en-Padmakara_2006.md", with_trans=True)
    t = {k: v[0] for k, v in above.items() if len(v) == 1}
    t.update(SPLIT_HALF)
    return t


def _wallace(own, _pt):
    """Wallace (from the Sanskrit): 2-32 is a placeholder, 8-25 and 10-16 have no Tibetan counterpart;
    the Tibetan 5-5 is inside Wallace 5-4 and 10-21 inside Wallace 10-22 (left without a reference)."""
    if own in ("2-32", "8-25", "10-16"):
        return None
    ch, _, n = own.partition("-")
    if not n.isdigit():
        return own
    n = int(n)
    if (ch == "2" and n >= 33) or (ch == "8" and n >= 26) or (ch == "10" and 17 <= n <= 21):
        return f"{ch}-{n - 1}"
    return own


def _longlian(own, pt):
    """隆蓮: ch. 2 lacks 2-32 (own 2-33.. = Tibetan 2-32..); ch. 7 and 8 number like Padmakara; ch. 9 divides
    9-13..9-21 by half verses (own 9-14..9-19 ~ Tibetan 9-15..9-20, own 9-20 joins 9-20) and own 9-22.. = 9-21..;
    its I-1 is the homage, Tibetan I-3."""
    if own == "I-1":
        return "I-3"
    ch, _, n = own.partition("-")
    if not n.isdigit():
        return own
    if ch in ("7", "8"):
        return pt.get(own)
    n = int(n)
    if ch == "2" and n >= 33:
        return f"2-{n - 1}"
    if ch == "9" and 14 <= n <= 19:
        return f"9-{n + 1}"
    if ch == "9" and n >= 22:
        return f"9-{n - 1}"
    return own


RULES = {"en-Wallace": _wallace, "zh-隆蓮法師": _longlian}


def aligned_reference(stem):
    """{Tibetan segment id: human translation} for one file in 1-SOURCES/Translations (see the notes above)."""
    from segment_context import blocks  # noqa: E402
    text, above = blocks(f"1-SOURCES/Translations/{stem}.md", with_trans=True)
    pt = _padmakara_table()
    out = {}
    for own, t in text.items():
        if not t.strip():
            continue
        if stem in TRANSCLUDED:
            v = above.get(own) or []
            tib = v[0] if len(v) == 1 else SPLIT_HALF.get(own)
        elif stem in PADMAKARA_NUMBERED:
            tib = CH9_ZH.get(own) or pt.get(own)
        else:
            tib = RULES[stem](own, pt)
        if tib:
            out[tib] = (out.get(tib, "") + " " + t).strip()
    return out


def references(track):
    """[(name, {segment id: human reference})] for each independent segment-aligned human translation."""
    lang, variant = track.split("-", 1)
    if variant != "academic":
        return []
    return [(name, aligned_reference(stem)) for name, stem in HUMAN.get(lang, {}).items()]


def track_report(track, syl):
    rs = runs(track)
    first_rows = run_rows(rs[0])
    first = {i: v for i, _, v in first_rows}
    first_text = {i: t for i, t, _ in first_rows}
    seen = {}  # (id, text) -> verdict, later runs override earlier ones
    latest = {}
    for run in rs:
        for i, t, v in run_rows(run):
            seen[(i, t)] = v
            latest[i] = v
    cur = current(track)
    after, unchecked = {}, []
    for i in first:
        v = seen.get((i, cur.get(i)))
        if v is None:
            unchecked.append(i)
            v = latest[i]
        after[i] = v
    b, a = score(list(first.values())), score(list(after.values()))
    for s in (b, a):
        s["penalty_per_1k_syl"] = round(s["penalty"] * 1000 / syl, 2)
        s["error_free_pct"] = round(100 * s["error_free"] / s["segments"], 1)
    for s_, v in ((b, first), (a, after)):
        s_["issues_per_100_seg"] = round(100 * (s_["critical"] + s_["major"] + s_["minor"]) / s_["segments"], 1)
        s_["blocking_per_100_seg"] = round(100 * (s_["critical"] + s_["major"]) / s_["segments"], 2)
    after_text = {i: cur.get(i, first_text[i]) for i in first}
    changed = [i for i in first if after_text[i] != first_text[i]]
    b["terms"], a["terms"] = compliance(track, first_text), compliance(track, after_text)
    per_ref = []
    for ref_name, refs in references(track):
        ref_ids = [i for i in first if refs.get(i)]
        if not ref_ids:
            continue
        ch = [i for i in changed if refs.get(i)]
        per_ref.append({"reference": ref_name, "segments": len(ref_ids),
                        "whole_before": chrf([first_text[i] for i in ref_ids], [refs[i] for i in ref_ids]),
                        "whole_after": chrf([after_text[i] for i in ref_ids], [refs[i] for i in ref_ids]),
                        "changed_segments": len(ch),
                        "changed_before": chrf([first_text[i] for i in ch], [refs[i] for i in ch]) if ch else None,
                        "changed_after": chrf([after_text[i] for i in ch], [refs[i] for i in ch]) if ch else None})
    chrf_rep = None
    if per_ref:
        mean = lambda k: (round(sum(r[k] for r in per_ref) / len(per_ref), 2)  # noqa: E731
                          if all(r[k] is not None for r in per_ref) else None)
        chrf_rep = {"reference": " / ".join(r["reference"] for r in per_ref) + (" (mean)" if len(per_ref) > 1 else ""),
                    "segments": per_ref[0]["segments"], "changed_segments": per_ref[0]["changed_segments"],
                    **{k: mean(k) for k in ("whole_before", "whole_after", "changed_before", "changed_after")},
                    "per_reference": per_ref}
    return {"track": track, "runs": [r.name for r in rs], "before": b, "after": a,
            "segments_regenerated": len(changed), "chrf": chrf_rep,
            "unchecked_current_text": unchecked,
            "pairs": [{"track": track, "id": i, "before": first_text[i], "after": after_text[i],
                       "before_verdict": first[i]["verdict"], "after_verdict": after[i]["verdict"]} for i in changed]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text-syllables", type=int, default=26724)  # Bodhicaryāvatāra Tibetan root, all blocks
    p.add_argument("--json")
    p.add_argument("--pairs", help="write the changed segments' before/after texts (input of pairwise_judge.py)")
    a = p.parse_args()
    out = []
    for track in ["en-academic", "zh-academic", "hi-academic", "en-children", "zh-children", "hi-children"]:
        if runs(track):
            out.append(track_report(track, a.text_syllables))
    print("| Track | Regenerated | Failing segments | Critical / major | Minor | Penalty per 1k syl | Error-free segments |")
    print("|---|---|---|---|---|---|---|")
    for r in out:
        b, f = r["before"], r["after"]
        print(f"| {r['track']} | {r['segments_regenerated']} | {b['fail']} → {f['fail']} | "
              f"{b['critical']}/{b['major']} → {f['critical']}/{f['major']} | {b['minor']} → {f['minor']} | "
              f"{b['penalty_per_1k_syl']} → {f['penalty_per_1k_syl']} | {b['error_free_pct']}% → {f['error_free_pct']}% |")
    print("\n| Track | Issues per 100 segments | Glossary compliance | chrF vs reference, whole text | chrF, changed segments |")
    print("|---|---|---|---|---|")
    for r in out:
        b, f, c = r["before"], r["after"], r["chrf"]
        cs = (f"{c['whole_before']} → {c['whole_after']}", f"{c['changed_before']} → {c['changed_after']} ({c['changed_segments']} seg)") if c else ("—", "—")
        print(f"| {r['track']} | {b['issues_per_100_seg']} → {f['issues_per_100_seg']} | "
              f"{b['terms']['pct']}% → {f['terms']['pct']}% | {cs[0]} | {cs[1]} |")
    for r in out:
        if r["unchecked_current_text"]:
            print(f"\n{r['track']}: current text never re-checked for {r['unchecked_current_text']} (latest verdict used)")
    if a.pairs:
        pathlib.Path(a.pairs).write_text(json.dumps([x for r in out for x in r["pairs"]], ensure_ascii=False, indent=1),
                                         encoding="utf-8")
    if a.json:
        slim = [{k: v for k, v in r.items() if k != "pairs"} for r in out]
        pathlib.Path(a.json).write_text(json.dumps(slim, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
