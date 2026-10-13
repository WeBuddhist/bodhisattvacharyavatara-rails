#!/usr/bin/env python3
"""Termbase-locked, commentary-grounded translation of the root text with Gemini.

  zsh -ic 'python3 gm_variant_translate.py --variant academic'            # all segments, resumable
  zsh -ic 'python3 gm_variant_translate.py --variant academic --only 7-28 7-29 --force'
  python3 gm_variant_translate.py --variant academic --render-only

Per batch of segments Gemini receives: the track's requirements.md, the locked
termbase entries for exactly the terms in those segments (sense chosen per
occurrence), and for each segment the Tibetan, the aligned Sanskrit, the aligned
commentary passages and the two machine drafts. Output is checked for ids and
for termbase compliance; a segment that misses a locked term is retried once
with the miss named. Every call goes to the usage ledger; every segment to
<track>/work/<stem>-en.jsonl (append-only; the last record per id wins).
"""
import argparse
import datetime as _dt
import importlib.util
import json
import os
import pathlib
import re
import sys
import threading
import time
import types
import uuid
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
KF = HERE.parent
VAULT = KF.parents[1]
sys.path.insert(0, str(KF / "context"))
from segment_context import build_context, COMMENTARIES, SA_FILE  # noqa: E402


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gm = load("gm_translate", VAULT / "4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py")
ledger = load("usage_ledger", VAULT / "4-SYSTEM/scripts/usage-ledger/usage_ledger.py")

TERM_RUN = KF / "term-extract/bodhicaryavatara-en"
ROOT = "bo-བློ་ལྡན་ཤེས་རབ།"
LANGS = {
    "en": {"name": "English", "label": "English", "tag": "en"},
    "zh": {"name": "Chinese", "label": "modern written Chinese in Traditional characters", "tag": "zh"},
    "hi": {"name": "Hindi", "label": "modern standard Hindi in Devanagari", "tag": "hi"},
}
LANG = "en"  # set from --lang in main()


def termbase_path(lang):
    return KF / f"termbase/bodhicaryavatara-{lang}/termbase.json"


def track_dir(lang, variant):
    return VAULT / f"3-TRANSFORMATIONS/Translations/{lang}-{variant}"


def work_file(lang, variant):
    return track_dir(lang, variant) / "work" / f"{ROOT}-{lang}.jsonl"


def zero_shot_lines(lang):
    """Gemini zero-shot root translation in `lang`, by block id (machine baseline)."""
    p = VAULT / f"3-TRANSFORMATIONS/Translations/Gemini/{lang}/work/{ROOT}-{lang}.jsonl"
    out = {}
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            t = r.get("translation")
            if t:
                out[r["block_id"]] = " ".join(t) if isinstance(t, list) else t
    return out


def kumarajiva_lines():
    """Diamond Sutra only. The Bodhicaryāvatāra has no Annotations dir, and its human Chinese
    translations stay out of the pipeline (independent reference for the report): returns {}."""
    f = VAULT / "1-SOURCES/Annotations/lzh-bodhicaryavatara.annotations.json"
    if not f.exists():
        return {}
    a = json.loads(f.read_text(encoding="utf-8"))
    out = {}
    for b in a["blocks"].values():
        for t in b.get("targets") or []:
            out[t] = (out.get(t, "") + " " + b.get("text", "")).strip()
    return out
LOCK = threading.Lock()

FORMAT = """
Output rules:
- Return JSON: {"blocks": [{"id": "<segment id>", "translation": "<translation>"}]} with exactly the ids you were sent, in order.
- Translate each segment completely and only that segment; the Sanskrit, commentary and drafts are aids, not text to translate.
- For every term listed under a segment's "locked terms", use that exact rendering (inflect for number or grammar only).
- No notes, brackets or explanations inside the translation."""

SCHEMA = {"type": "object", "properties": {"blocks": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "translation": {"type": "string"}},
    "required": ["id", "translation"]}}}, "required": ["blocks"]}

STOP = {"of", "the", "a", "an", "and", "or", "to", "in", "on", "at", "by", "with", "for", "his", "her", "its"}


def words(s):
    return [w.strip("'-") for w in re.findall(r"[a-zāīūṛṝḷṃṁṅñṇṭḍśṣḥ'-]+", s.lower().replace("’", "'")) if w.strip("'-")]


def complies(rendering, text, lang=None):
    """Loose check that the locked rendering is used.
    en: every content word occurs (prefix match allows plural/inflection);
    zh: the rendering occurs as a substring (punctuation ignored);
    hi: every word of two or more letters occurs, allowing a changed final vowel sign (inflection)."""
    lang = lang or LANG
    if lang == "zh":
        strip = lambda x: re.sub(r"[\s，。、；：「」『』《》（）·・—…！？,.;:()\"'-]", "", x)  # noqa: E731
        return strip(rendering) in strip(text)
    if lang == "hi":
        # Sanskrit-style compounds carry a term inside a longer word (सम्यक्सम्बुद्ध, परिनिर्वाण,
        # आत्म-ग्राह), so a stem may occur anywhere in a word; helper verbs and postpositions are skipped.
        skip = {"करना", "होना", "का", "की", "के", "में", "से", "को", "और", "या"}
        tw = re.findall(r"[\u0900-\u097F]+", text)
        for w in re.findall(r"[\u0900-\u097F]+", rendering):
            if len(w) < 2 or w in skip:
                continue
            if w.endswith("\u094d"):  # final virama: आत्मन् -> आत्म
                stem = w[:-2]
            else:
                # strip the inflectional ending: infinitive -ना (देना -> दे/देता), then trailing vowel signs,
                # nasals and plural vowels (चीज़ें -> चीज़/चीज़ों, नदी -> नद/नदियों, पूर्णताएँ -> पूर्णत/पूर्णताओं)
                stem = w[:-2] if w.endswith("ना") and len(w) > 3 else w
                stripped = re.sub(r"[\u093E-\u094C\u0901-\u0903\u0907-\u0914]+$", "", stem)
                stem = stripped if len(stripped) >= 2 else stem
            if not any(stem in t for t in tw):
                return False
        return True
    tw = words(text)
    tw += [part for w in tw if "-" in w for part in w.split("-")]  # non-phenomena -> phenomena
    tw += [w[:-3] + "man" for w in tw if w.endswith("men")]  # laymen -> layman
    for w in words(rendering):
        if w in STOP or len(w) < 3:
            continue
        stem = w[:-2] if len(w) > 6 else w[:-1] if len(w) > 4 else w  # phenomenon/phenomena, mark/marks
        if not any(t.startswith(stem) for t in tw):
            return False
    return True


def locked_terms(variant, lang=None):
    """{segment id: [{bo, rendering, sense}]} from the term occurrences and the language's termbase."""
    tb = {e["bo"]: e for e in json.loads(termbase_path(lang or LANG).read_text(encoding="utf-8"))}
    occ = json.loads((TERM_RUN / "occurrences-reviewed.json").read_text(encoding="utf-8"))
    ov = termbase_path(lang or LANG).parent / "overrides.json"
    skip = {(x["id"], x["bo"]) for x in (json.loads(ov.read_text(encoding="utf-8")).get("exclude_occurrences", [])
                                        if ov.exists() else [])}
    out = {}
    for o in occ:
        if (o["id"], o["bo"]) in skip:  # editor/fact-check: this occurrence is not the glossary sense
            continue
        e = tb.get(o["bo"])
        if not e:
            continue
        sense = next((s for s in e["senses"] if s["occurrences"] == "all" or o["id"] in s["occurrences"]),
                     e["senses"][0])
        out.setdefault(o["id"], []).append({"bo": o["bo"], "rendering": sense[variant], "sense": sense["sense"]})
    # A term nested in a longer locked term of the same segment (e.g. སེམས་ཅན་དམྱལ་བ inside
    # སེམས་ཅན་དམྱལ་བའི་སྲུང་མ) is not locked when every appearance of it is inside the longer one:
    # locking both forces two renderings onto one phrase (BCA 5-4).
    segs = {s["id"]: s["bo"] for s in json.loads((TERM_RUN / "segments.json").read_text(encoding="utf-8"))}
    for sid, ts in out.items():
        text = segs.get(sid, "")
        out[sid] = [t for t in ts if not any(t["bo"] != u["bo"] and t["bo"] in u["bo"]
                                             and text.count(t["bo"]) <= text.count(u["bo"]) for u in ts)]
    return out


def make_batches(ids, segs, size, budget):
    batches, cur, chars = [], [], 0
    for i in ids:
        n = len(segs[i]["bo"])
        if cur and (len(cur) >= size or chars + n > budget):
            batches.append(cur)
            cur, chars = [], 0
        cur.append(i)
        chars += n
    if cur:
        batches.append(cur)
    return batches


def payload(batch, segs, ctx, terms, max_comm, base=None, refs=None):
    """Per-segment prompt items. With `base` (another track's rows), the item carries that
    translation as the source of meaning instead of Sanskrit, commentaries and machine drafts."""
    out, seen = [], set()
    if base is not None:
        return [{"id": i, "heading": segs[i]["heading"], "tibetan": segs[i]["bo"],
                 "academic_translation": base[i]["translation"],
                 "locked_terms": [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])]}
                for i in batch]
    for i in batch:
        s, c = segs[i], ctx.get(i, {})
        comms = {}
        for cid, passages in (c.get("commentaries") or {}).items():
            for p in passages:
                key = (cid, p["id"])
                if key in seen:
                    comms.setdefault(cid, []).append(f"(passage {p['id']}, given above)")
                    continue
                seen.add(key)
                txt = p["text"]
                comms.setdefault(cid, []).append(txt if len(txt) <= max_comm else txt[:max_comm] + " …")
        item = {"id": i, "heading": s["heading"], "tibetan": s["bo"],
                "sanskrit": " ".join(x["text"] for x in c.get("sa", [])) or None,
                "commentaries": comms or None}
        if refs is None:  # English: the two English machine baselines
            item["machine_drafts"] = {"dharmamitra": s["dm"], "gemini": s["gm"]}
        else:  # other languages: approved English academic + target-language aids
            for k, table in refs.items():
                if i in table:
                    item[k] = table[i]
        item["locked_terms"] = [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])]
        out.append(item)
    return out


def translate_batch(batch, a, key, system, segs, ctx, terms, work, variant, attempt=1, feedback=None):
    body_items = payload(batch, segs, ctx, terms, a.max_comm, a.base_rows, a.refs)
    label = LANGS[LANG]["label"]
    if a.base_rows is not None:
        user = (f"Retell these segments of the Bodhicaryāvatāra in {label} for the {variant} register. Take the meaning "
                f"from `academic_translation` (checked against the Tibetan); write new, simple wording. Return JSON only.\n\n")
    else:
        user = f"Translate these segments of the Tibetan Bodhicaryāvatāra into {label} ({variant} register). Return JSON only.\n\n"
        if a.refs:
            user += ("Each segment also carries `english_academic` (the approved, fact-checked English academic "
                     "translation — use it to confirm the meaning, not as the text to translate)"
                     + (", `kumarajiva` (Kumārajīva's classical Chinese, for established terminology only)" if a.refs.get("kumarajiva") else "")
                     + " and `zero_shot` (an unreviewed machine draft in the target language). Translate from the Tibetan.\n\n")
    if feedback:
        user += feedback + "\n\n"
    user += json.dumps(body_items, ensure_ascii=False)
    body = {"systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {"responseMimeType": "application/json", "responseSchema": SCHEMA},
            "safetySettings": gm.SAFETY_OFF}
    args = types.SimpleNamespace(model=a.model, retries=6, timeout=900)
    call_id = uuid.uuid4().hex[:12]
    t0 = time.time()
    text, info = gm.call_api(body, args, key)
    u = info["usage"]
    ledger.log_call(step=f"translate-{variant}", text="bodhicaryavatara", lang=LANG, variant=variant,
                    engine="gemini-api", model=info["model_version"], batch=call_id, segments=len(batch),
                    attempt=attempt, tokens={"input": u["prompt_tokens"], "output": u["output_tokens"],
                                             "thinking": u["thinking_tokens"]},
                    seconds=round(time.time() - t0, 1), note=f"{batch[0]}..{batch[-1]}")
    data = {b["id"]: b["translation"].strip() for b in json.loads(text).get("blocks", [])}
    missing_ids = [i for i in batch if not data.get(i)]
    if missing_ids:
        raise gm.BadResponse(f"ids missing from answer: {missing_ids}")
    misses = {}
    with LOCK, work.open("a", encoding="utf-8") as fh:
        for i in batch:
            req = terms.get(i, [])
            miss = [t for t in req if not complies(t["rendering"], data[i])]
            if miss:
                misses[i] = miss
            fh.write(json.dumps({"id": i, "translation": data[i], "variant": variant, "call_id": call_id,
                                 "attempt": attempt, "model": info["model_version"],
                                 "terms_required": len(req), "terms_missed": [t["rendering"] for t in miss],
                                 "batch": batch, "ts": _dt.datetime.now().isoformat(timespec="seconds")},
                                ensure_ascii=False) + "\n")
    return misses


def fact_feedback(batch, fb):
    """Prompt text listing a fact-checker's blocking issues for the segments in this batch."""
    lines = ["A FACT-CHECK of your previous translation of these segments found these problems. "
             "Retranslate each segment from the Tibetan, fixing them (the suggested fixes are guidance, "
             "not mandatory wording); keep everything that was correct:"]
    for i in batch:
        prev = fb[i]
        lines.append(f"[{i}] previous translation: {prev['translation']}")
        for iss in prev["issues"]:
            lines.append(f"  - {iss['severity']} {iss['type']}: \"{iss['span']}\" — {iss['evidence']} Suggested: {iss['fix']}")
    return "\n".join(lines)


def run_batch(batch, *ctx_args):
    a, key, system, segs, ctx, terms, work, variant = ctx_args
    fb = fact_feedback(batch, a.feedback_data) if a.feedback_data else None
    misses = translate_batch(batch, *ctx_args, attempt=a.attempt, feedback=fb)
    if misses and a.retry_terms:
        retry = list(misses)
        fb = "PREVIOUS ATTEMPT missed locked terms — use them this time:\n" + "\n".join(
            f"{i}: " + "; ".join(f"{t['bo']} → {t['rendering']}" for t in m) for i, m in misses.items())
        misses = translate_batch(retry, a, key, system, segs, ctx, terms, work, variant,
                                 attempt=a.attempt + 1, feedback=fb)
    return batch, misses


def latest(work):
    rows = {}
    if work.exists():
        for line in work.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            rows[r["id"]] = r
    return rows


def render(track, stem, segs, rows, variant, model):
    order = list(segs)
    done = sum(1 for i in order if i in rows)
    terms = locked_terms(variant)
    missed_ids = [i for i in order if i in rows
                  and any(not complies(t["rendering"], rows[i]["translation"]) for t in terms.get(i, []))]
    missed = len(missed_ids)
    (track / "work" / "termbase-compliance.json").write_text(json.dumps(
        {i: [t["rendering"] for t in terms.get(i, []) if not complies(t["rendering"], rows[i]["translation"])]
         for i in missed_ids}, ensure_ascii=False, indent=1), encoding="utf-8")
    title = rows.get("0", {}).get("translation", "Bodhicaryāvatāra")
    L = LANGS[LANG]
    fm = ["---", f"title: {title}", f"track: {LANG}-{variant}", f"language: {L['name']}", f"lang_tag: {LANG}",
          "file_type: translation", "track_type: governed-draft", f"root_text: 1-SOURCES/Translations/{ROOT}.md",
          "source_language: tibetan", f"target_language: {L['name'].lower()}", f"generator: {model}",
          (f"context_packages: [termbase.md, ../{LANG}-academic/{ROOT}-{LANG}.md (meaning source)]" if variant == "children" else
          f"context_packages: [termbase.md, aligned Sanskrit ({SA_FILE}), "
          f"aligned commentaries: {', '.join(COMMENTARIES)}]"),
          f"blocks_translated: {done}", f"blocks_total: {len(order)}", f"segments_missing_locked_terms: {missed}",
          f"generation_date: {_dt.date.today().isoformat()}", "status: draft", "---", ""]
    body = []
    for i in order:
        r = rows.get(i)
        if not r:
            continue
        if i == "0":
            body += [f"# {r['translation']} ^0", ""]
        elif segs[i]["heading"]:
            body += [f"## {r['translation']} ^{i}", ""]
        else:
            body += [f"![[{ROOT}#^{i}]]", "", f"{r['translation']} ^{i}", ""]
    (track / f"{stem}-{LANG}.md").write_text("\n".join(fm + body), encoding="utf-8")
    print(f"rendered {done}/{len(order)} blocks; segments still missing a locked term: {missed}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variant", required=True, choices=["academic", "children"])
    p.add_argument("--lang", default="en", choices=sorted(LANGS))
    p.add_argument("--model", default=gm.DEFAULT_MODEL)
    p.add_argument("--batch-size", type=int, default=6)
    p.add_argument("--budget", type=int, default=1800, help="max Tibetan chars per batch")
    p.add_argument("--max-comm", type=int, default=2500, help="max chars per commentary passage")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--only", nargs="*")
    p.add_argument("--force", action="store_true")
    p.add_argument("--limit", type=int, help="translate at most N batches (trial runs)")
    p.add_argument("--no-retry-terms", dest="retry_terms", action="store_false")
    p.add_argument("--render-only", action="store_true")
    p.add_argument("--feedback", help="fact-check feedback JSON {id: {translation, issues}}; translates only those ids")
    p.add_argument("--attempt", type=int, default=1)
    p.add_argument("--from-track", help="build from another track's translation (e.g. academic) instead of the sources")
    a = p.parse_args()

    global LANG
    LANG = a.lang
    track = track_dir(LANG, a.variant)
    work = work_file(LANG, a.variant)
    segs = {s["id"]: s for s in json.loads((TERM_RUN / "segments.json").read_text(encoding="utf-8"))}
    if a.render_only:
        return render(track, ROOT, segs, latest(work), a.variant, a.model)
    key = os.environ.get(gm.KEY_ENV, "")
    if not key:
        sys.exit("GEMINI_API_KEY is not set (run via: zsh -ic 'python3 ...')")
    system = (track / "requirements.md").read_text(encoding="utf-8") + FORMAT
    ctx = build_context(ROOT)
    terms = locked_terms(a.variant)
    done = latest(work)
    a.base_rows = None
    if a.from_track:
        a.base_rows = latest(work_file(LANG, a.from_track))
    a.refs = None
    if LANG != "en" and a.base_rows is None:
        a.refs = {"english_academic": {i: r["translation"] for i, r in latest(work_file("en", "academic")).items()},
                  "zero_shot": zero_shot_lines(LANG)}
        if LANG == "zh" and kumarajiva_lines():
            a.refs["kumarajiva"] = kumarajiva_lines()
    a.feedback_data = json.loads(pathlib.Path(a.feedback).read_text(encoding="utf-8")) if a.feedback else None
    if a.feedback_data:
        todo = list(a.feedback_data)
    else:
        todo = a.only or [i for i in segs if a.force or i not in done]
    batches = make_batches(todo, segs, a.batch_size, a.budget)
    if a.limit:
        batches = batches[: a.limit]
    print(f"segments to translate={len(todo)} batches={len(batches)}")
    args = (a, key, system, segs, ctx, terms, work, a.variant)
    failed = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(run_batch, b, *args): b for b in batches}
        for f in futs:
            b = futs[f]
            try:
                _, misses = f.result()
                print(f"  {b[0]}..{b[-1]} ok" + (f"  still missing terms in {list(misses)}" if misses else ""))
            except Exception as exc:  # noqa: BLE001
                failed.append(b)
                print(f"  {b[0]}..{b[-1]} FAILED: {exc}")
    if failed:
        print(f"failed batches: {len(failed)} — rerun the same command to resume")
    render(track, ROOT, segs, latest(work), a.variant, a.model)


if __name__ == "__main__":
    main()
