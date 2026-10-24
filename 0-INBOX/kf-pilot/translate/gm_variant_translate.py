#!/usr/bin/env python3
"""Termbase-locked, commentary-grounded translation of the root text with Gemini.

  zsh -ic 'python3 gm_variant_translate.py --variant academic'            # all segments, resumable
  zsh -ic 'python3 gm_variant_translate.py --variant academic --only 7-28 7-29 --force'
  python3 gm_variant_translate.py --variant academic --render-only
  zsh -ic 'python3 gm_variant_translate.py --variant easy --lang es --model kimi-k3'   # from es-academic
  zsh -ic 'python3 gm_variant_translate.py --variant wbw --lang en'                     # en defines the word split
  zsh -ic 'python3 gm_variant_translate.py --variant academic --lang es --model gpt-6-sol --only 1-1 1-2 --out-track bakeoff-es-gpt'

Variants: academic (from the sources), children and easy (retold from the same language's academic
track), wbw (word-by-word gloss table from the Tibetan + the academic track; the en-wbw track fixes the
Tibetan word split that every other language reuses). Models: gemini-* (Gemini API with a response
schema), gpt-* / kimi-* (multilang/lib/llm.py, JSON mode). Kimi refuses Tibetan script, so it runs
only children/easy, with the Tibetan left out of the prompt.

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
import unicodedata
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
llm = load("llm", VAULT.parent / "multilang/lib/llm.py")

TERM_RUN = KF / "term-extract/bodhicaryavatara-en"
ROOT = "bo-བློ་ལྡན་ཤེས་རབ།"
LANGS = {
    "en": {"name": "English", "label": "English", "tag": "en"},
    "zh": {"name": "Chinese", "label": "modern written Chinese in Traditional characters", "tag": "zh"},
    "hi": {"name": "Hindi", "label": "modern standard Hindi in Devanagari", "tag": "hi"},
    "es": {"name": "Spanish", "label": "neutral international Spanish", "tag": "es"},
    "pt": {"name": "Portuguese", "label": "Brazilian Portuguese", "tag": "pt"},
    "fr": {"name": "French", "label": "modern standard French", "tag": "fr"},
    "it": {"name": "Italian", "label": "modern standard Italian", "tag": "it"},
    "id": {"name": "Indonesian", "label": "standard Indonesian (Bahasa Indonesia)", "tag": "id"},
    "sw": {"name": "Swahili", "label": "standard Swahili (Kiswahili sanifu)", "tag": "sw"},
    "ja": {"name": "Japanese", "label": "modern written Japanese (kanji and kana)", "tag": "ja"},
    "ko": {"name": "Korean", "label": "modern standard Korean in Hangul", "tag": "ko"},
    "vi": {"name": "Vietnamese", "label": "modern standard Vietnamese (Latin script with full diacritics)", "tag": "vi"},
    "th": {"name": "Thai", "label": "modern standard Thai in Thai script", "tag": "th"},
    "ne": {"name": "Nepali", "label": "modern standard Nepali in Devanagari", "tag": "ne"},
    "mr": {"name": "Marathi", "label": "modern standard Marathi in Devanagari", "tag": "mr"},
    "si": {"name": "Sinhala", "label": "modern written Sinhala in Sinhala script", "tag": "si"},
    "mn": {"name": "Mongolian", "label": "modern Khalkha Mongolian in Cyrillic script", "tag": "mn"},
}
LANG = "en"  # set from --lang in main()
VARIANTS = ["academic", "children", "easy", "wbw"]
SENSE_KEY = {"academic": "academic", "children": "children", "easy": "academic", "wbw": "academic"}  # termbase sense field
# Shown after the title in the frontmatter and the H1 (user rule: every title says the text is AI-made).
AI_LABEL = {
    "en": {"academic": "AI translation (academic)", "children": "AI translation (children's)",
           "easy": "AI translation (easy-to-read)", "wbw": "AI translation (word-by-word)"},
    "zh": {"academic": "AI 翻譯（學術版）", "children": "AI 翻譯（兒童版）",
           "easy": "AI 翻譯（易讀版）", "wbw": "AI 翻譯（逐詞對照版）"},
    "hi": {"academic": "एआई अनुवाद (शैक्षणिक संस्करण)", "children": "एआई अनुवाद (बाल संस्करण)",
           "easy": "एआई अनुवाद (सरल संस्करण)", "wbw": "एआई अनुवाद (शब्दशः)"},
    "es": {"academic": "Traducción con IA (académica)", "children": "Traducción con IA (infantil)",
           "easy": "Traducción con IA (lectura fácil)", "wbw": "Traducción con IA (palabra por palabra)"},
    "pt": {"academic": "Tradução por IA (acadêmica)", "children": "Tradução por IA (infantil)",
           "easy": "Tradução por IA (leitura fácil)", "wbw": "Tradução por IA (palavra por palavra)"},
    "fr": {"academic": "Traduction par IA (version académique)", "children": "Traduction par IA (version jeunesse)",
           "easy": "Traduction par IA (version facile à lire)", "wbw": "Traduction par IA (mot à mot)"},
    "it": {"academic": "Traduzione con IA (versione accademica)", "children": "Traduzione con IA (versione per ragazzi)",
           "easy": "Traduzione con IA (versione di facile lettura)", "wbw": "Traduzione con IA (parola per parola)"},
    "id": {"academic": "Terjemahan AI (akademik)", "children": "Terjemahan AI (anak-anak)",
           "easy": "Terjemahan AI (mudah dibaca)", "wbw": "Terjemahan AI (kata demi kata)"},
    "sw": {"academic": "Tafsiri ya AI (toleo la kitaaluma)", "children": "Tafsiri ya AI (toleo la watoto)",
           "easy": "Tafsiri ya AI (toleo rahisi kusoma)", "wbw": "Tafsiri ya AI (neno kwa neno)"},
    "ja": {"academic": "AI翻訳（学術版）", "children": "AI翻訳（子ども版）",
           "easy": "AI翻訳（わかりやすい版）", "wbw": "AI翻訳（逐語対訳）"},
    "ko": {"academic": "AI 번역 (학술판)", "children": "AI 번역 (어린이판)",
           "easy": "AI 번역 (쉬운 글판)", "wbw": "AI 번역 (단어별 대역)"},
    "vi": {"academic": "Bản dịch AI (học thuật)", "children": "Bản dịch AI (thiếu nhi)",
           "easy": "Bản dịch AI (dễ đọc)", "wbw": "Bản dịch AI (từng từ)"},
    "th": {"academic": "คำแปลโดย AI (ฉบับวิชาการ)", "children": "คำแปลโดย AI (ฉบับสำหรับเด็ก)",
           "easy": "คำแปลโดย AI (ฉบับอ่านง่าย)", "wbw": "คำแปลโดย AI (ฉบับคำต่อคำ)"},
    "ne": {"academic": "एआई अनुवाद (प्राज्ञिक संस्करण)", "children": "एआई अनुवाद (बाल संस्करण)",
           "easy": "एआई अनुवाद (सरल संस्करण)", "wbw": "एआई अनुवाद (शब्दशः)"},
    "mr": {"academic": "एआय अनुवाद (शैक्षणिक आवृत्ती)", "children": "एआय अनुवाद (बाल आवृत्ती)",
           "easy": "एआय अनुवाद (सोपी आवृत्ती)", "wbw": "एआय अनुवाद (शब्दशः)"},
    "si": {"academic": "AI පරිවර්තනය (ශාස්ත්‍රීය සංස්කරණය)", "children": "AI පරිවර්තනය (ළමා සංස්කරණය)",
           "easy": "AI පරිවර්තනය (පහසු කියවීමේ සංස්කරණය)", "wbw": "AI පරිවර්තනය (වචනයෙන් වචනය)"},
    "mn": {"academic": "Хиймэл оюуны орчуулга (эрдэм шинжилгээний хувилбар)",
           "children": "Хиймэл оюуны орчуулга (хүүхдийн хувилбар)",
           "easy": "Хиймэл оюуны орчуулга (уншихад хялбар хувилбар)",
           "wbw": "Хиймэл оюуны орчуулга (үгчилсэн хувилбар)"},
}


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

FORMAT_WBW = """
Output rules:
- Return JSON: {"blocks": [{"id": "<segment id>", "words": [{"bo": "<Tibetan word or particle group>", "gloss": "<gloss>"}]}]} with exactly the ids you were sent, in order.
- The `bo` values, read in order, must reproduce the segment's whole Tibetan text: every syllable once, in order, nothing skipped, repeated or changed (tsheg and shad may be left out).
- If a segment carries `bo_words`, use exactly those strings as the `bo` values, in that order, and write only the glosses.
- Each `gloss` is the meaning of that word in this verse (as `academic_translation` reads it), in a few words of the target language.
- For a word that is a locked term, the gloss is the locked rendering.
- No notes, brackets or explanations inside a gloss."""

SCHEMA_WBW = {"type": "object", "properties": {"blocks": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "words": {"type": "array", "items": {
        "type": "object", "properties": {"bo": {"type": "string"}, "gloss": {"type": "string"}},
        "required": ["bo", "gloss"]}}},
    "required": ["id", "words"]}}}, "required": ["blocks"]}

STOP = {"of", "the", "a", "an", "and", "or", "to", "in", "on", "at", "by", "with", "for", "his", "her", "its"}


def words(s):
    return [w.strip("'-") for w in re.findall(r"[a-zāīūṛṝḷṃṁṅñṇṭḍśṣḥ'-]+", s.lower().replace("’", "'")) if w.strip("'-")]


# Devanagari languages (hi logic): helper verbs / postpositions skipped, and the infinitive ending stripped.
DEVA_SKIP = {"ne": {"गर्नु", "हुनु", "को", "का", "की", "मा", "ले", "लाई", "बाट", "र", "वा", "तथा"},
             "mr": {"करणे", "होणे", "चा", "ची", "चे", "च्या", "ला", "ना", "त", "ने", "आणि", "किंवा", "व"}}
DEVA_INF = {"hi": "ना", "ne": "नु", "mr": "णे"}
# Word-based languages: function words that a locked rendering may carry but need not repeat.
STOP_U = {
    "es": {"de", "del", "la", "el", "los", "las", "lo", "y", "e", "o", "u", "en", "a", "al", "un", "una",
           "por", "para", "con", "su", "sus", "se", "que"},
    "pt": {"de", "do", "da", "dos", "das", "o", "a", "os", "as", "e", "ou", "em", "no", "na", "nos", "nas",
           "um", "uma", "por", "para", "com", "seu", "sua", "seus", "suas", "se", "que"},
    "fr": {"de", "du", "des", "la", "le", "les", "l", "d", "et", "ou", "en", "à", "au", "aux", "un", "une",
           "par", "pour", "avec", "sa", "son", "ses", "se", "que", "qui"},
    "it": {"di", "del", "della", "dello", "dei", "degli", "delle", "il", "lo", "la", "i", "gli", "le", "l",
           "e", "ed", "o", "in", "nel", "nella", "a", "al", "alla", "un", "una", "uno", "per", "con",
           "suo", "sua", "se", "che"},
    "id": {"dan", "atau", "yang", "di", "ke", "dari", "para", "sang", "untuk", "dengan"},
    "sw": {"na", "ya", "wa", "za", "la", "cha", "vya", "kwa", "katika", "au"},
    "mn": {"ба", "болон", "буюу", "нь", "юм", "ийн"},
    "vi": {"của", "và", "hoặc", "các", "những", "là", "sự"},
    "ko": {"의", "와", "과", "및", "또는", "그리고"},
    "si": {"සහ", "හෝ", "හා", "ගේ", "ට", "ද"},
}


def uwords(s, lang):
    """Lower-cased NFC words of any script (Sinhala by code block: its vowel signs are not letters)."""
    s = unicodedata.normalize("NFC", s).lower()
    return re.findall(r"[඀-෿‍]+" if lang == "si" else r"[^\W\d_]+", s)


def complies(rendering, text, lang=None):
    """Loose check that the locked rendering is used.
    en: every content word occurs (prefix match allows plural/inflection);
    zh: the rendering occurs as a substring (punctuation ignored); ja, th the same (NFKC, any punctuation);
    hi: every word of two or more letters occurs, allowing a changed final vowel sign (inflection); ne, mr the same;
    es, pt, fr, it, mn: every content word occurs as a word prefix once its ending is trimmed (as en);
    id, sw, ko, si: every content word's stem occurs inside some word (affixes, particles, case endings);
    vi: every content syllable occurs as a word (no inflection)."""
    lang = lang or LANG
    if lang in ("ja", "th"):
        strip = lambda x: re.sub(r"[^\w฀-๿]", "", unicodedata.normalize("NFKC", x))  # noqa: E731
        return strip(rendering) in strip(text)
    if lang in STOP_U:
        tw = uwords(text, lang)
        for w in uwords(rendering, lang):
            if w in STOP_U[lang] or len(w) < (1 if lang in ("ko", "vi") else 2 if lang == "si" else 3):
                continue
            if lang == "vi":
                stem = w
            elif lang == "ko":  # verbs: 집착하다 -> 집착 (집착하지, 집착을)
                stem = w[:-2] if w.endswith("하다") and len(w) > 2 else w[:-1] if w.endswith("다") and len(w) > 1 else w
            elif lang == "si":  # trailing vowel signs, virama, anusvara/visarga (case endings attach after them)
                stripped = re.sub(r"[ංඃ්-ෟෲෳ‍]+$", "", w)
                stem = stripped if len(stripped) >= 2 else w
            else:
                stem = w[:-2] if len(w) > 6 else w[:-1] if len(w) > 4 else w
            if lang == "vi":
                ok = stem in tw
            elif lang in ("es", "pt", "fr", "it", "mn"):
                ok = any(t.startswith(stem) for t in tw)
            else:
                ok = any(stem in t for t in tw)
            if not ok:
                return False
        return True
    if lang == "zh":
        strip = lambda x: re.sub(r"[\s，。、；：「」『』《》（）·・—…！？,.;:()\"'-]", "", x)  # noqa: E731
        return strip(rendering) in strip(text)
    if lang in DEVA_INF:
        # Sanskrit-style compounds carry a term inside a longer word (सम्यक्सम्बुद्ध, परिनिर्वाण,
        # आत्म-ग्राह), so a stem may occur anywhere in a word; helper verbs and postpositions are skipped.
        skip = DEVA_SKIP[lang] if lang in DEVA_SKIP else {"करना", "होना", "का", "की", "के", "में", "से", "को", "और", "या"}
        tw = re.findall(r"[\u0900-\u097F]+", text)
        for w in re.findall(r"[\u0900-\u097F]+", rendering):
            if len(w) < 2 or w in skip:
                continue
            if w.endswith("\u094d"):  # final virama: आत्मन् -> आत्म
                stem = w[:-2]
            else:
                # strip the inflectional ending: infinitive -ना (देना -> दे/देता), then trailing vowel signs,
                # nasals and plural vowels (चीज़ें -> चीज़/चीज़ों, नदी -> नद/नदियों, पूर्णताएँ -> पूर्णत/पूर्णताओं)
                stem = w[:-2] if w.endswith(DEVA_INF[lang]) and len(w) > 3 else w
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
        out.setdefault(o["id"], []).append({"bo": o["bo"], "rendering": sense[SENSE_KEY[variant]], "sense": sense["sense"]})
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


def payload(batch, segs, ctx, terms, max_comm, base=None, refs=None, no_tibetan=False, bo_words=None):
    """Per-segment prompt items. With `base` (another track's rows), the item carries that
    translation as the source of meaning instead of Sanskrit, commentaries and machine drafts.
    `no_tibetan` drops every Tibetan field (Kimi); `bo_words` adds the en-wbw word split (wbw)."""
    out, seen = [], set()
    if base is not None:
        items = [{"id": i, "heading": segs[i]["heading"], "tibetan": segs[i]["bo"],
                  "academic_translation": base[i]["translation"],
                  "locked_terms": [{"tibetan": t["bo"], "use": t["rendering"]} for t in terms.get(i, [])]}
                 for i in batch]
        for it in items:
            if no_tibetan:
                del it["tibetan"]
                it["locked_terms"] = [{"use": t["use"]} for t in it["locked_terms"]]
            if bo_words and it["id"] in bo_words:
                it["bo_words"] = bo_words[it["id"]]
        return items
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


def no_bo(s):
    """Remove Tibetan script (Kimi's content filter rejects any prompt that contains it)."""
    return re.sub(r"[ༀ-࿿]+", "", s)


def bo_norm(s):
    """Tibetan letters only: no spaces, tsheg, shad or other marks (to compare a word split with its segment)."""
    return re.sub(r"[\sༀ-༔༺-༽]", "", s)


def gloss_text(translation):
    """The glosses of a wbw row (its translation is a JSON list of {bo, gloss}), for the locked-term check."""
    return " ".join(w["gloss"] for w in json.loads(translation))


def wbw_problem(i, words, segs, ref):
    """None if the word list is a valid split of segment i (and matches the en-wbw split `ref`), else the problem.
    A split that differs from `ref` only in tsheg/spacing is set to `ref` in place."""
    if not words or any(not w["bo"] or not w["gloss"] for w in words):
        return "every entry needs a non-empty `bo` and `gloss`"
    if ref is not None:
        if len(words) == len(ref) and all(bo_norm(w["bo"]) == bo_norm(r) for w, r in zip(words, ref)):
            for w, r in zip(words, ref):
                w["bo"] = r
            return None
        return f"the `bo` values must be exactly the {len(ref)} strings of `bo_words`, in order"
    if bo_norm("".join(w["bo"] for w in words)) != bo_norm(segs[i]["bo"]):
        return "the `bo` values, read in order, do not reproduce the whole Tibetan segment (a syllable is missing, repeated or changed)"
    return None


def user_text(body_items, a, variant, feedback=None):
    """The user message translate_batch() sends: this variant's instructions, then the payload JSON."""
    label = LANGS[LANG]["label"]
    if variant == "wbw":
        user = (f"Make a word-by-word gloss of these segments of the Tibetan Bodhicaryāvatāra in {label}. Split each "
                f"segment's `tibetan` into its words, in order, and gloss each word as `academic_translation` (the checked "
                f"{LANGS[LANG]['name']} academic translation) reads it."
                + (" Segments with `bo_words` already have their word split (it is shared by every language): keep it exactly."
                   if any("bo_words" in it for it in body_items) else "") + " Return JSON only.\n\n")
    elif variant == "easy":
        user = (f"Retell these segments of the Bodhicaryāvatāra in {label} as an easy-to-read version for adult general "
                f"readers. Take the meaning from `academic_translation` (checked against the Tibetan); write plain, clear "
                f"wording, and use every locked term exactly as given, so the terms match the academic version. Return JSON only.\n\n")
    elif a.base_rows is not None:
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
    return user


def translate_batch(batch, a, key, system, segs, ctx, terms, work, variant, attempt=1, feedback=None):
    body_items = payload(batch, segs, ctx, terms, a.max_comm, a.base_rows, a.refs, a.no_tibetan, a.wbw_ref)
    user = user_text(body_items, a, variant, feedback)
    call_id = uuid.uuid4().hex[:12]
    t0 = time.time()
    if a.model.startswith("gemini"):
        body = {"systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "user", "parts": [{"text": user}]}],
                "generationConfig": {"responseMimeType": "application/json",
                                     "responseSchema": SCHEMA_WBW if variant == "wbw" else SCHEMA},
                "safetySettings": gm.SAFETY_OFF}
        args = types.SimpleNamespace(model=a.model, retries=6, timeout=900)
        text, info = gm.call_api(body, args, key)
        u = info["usage"]
        model_version, engine = info["model_version"], "gemini-api"
        tokens = {"input": u["prompt_tokens"], "output": u["output_tokens"], "thinking": u["thinking_tokens"]}
    else:  # gpt-* / kimi-*: OpenAI-style chat, JSON mode; the output rules in `system` give the JSON shape
        if a.no_tibetan:
            system, user = no_bo(system), no_bo(user)
        r = llm.chat(a.model, system, user, json_mode=True, timeout=900)
        text, model_version, engine, tokens = r["text"], r["model"], llm.engine_of(a.model), r["tokens"]
    ledger.log_call(step=f"translate-{variant}", text="bodhicaryavatara", lang=LANG, variant=variant,
                    engine=engine, model=model_version, batch=call_id, segments=len(batch),
                    attempt=attempt, tokens=tokens,
                    seconds=round(time.time() - t0, 1), note=f"{batch[0]}..{batch[-1]}")
    blocks = json.loads(text).get("blocks", [])
    if variant == "wbw":
        data = {b["id"]: [{"bo": str(w.get("bo", "")).strip(), "gloss": str(w.get("gloss", "")).strip()}
                          for w in b.get("words") or []] for b in blocks}
    else:
        data = {b["id"]: b["translation"].strip() for b in blocks}
    missing_ids = [i for i in batch if not data.get(i)]
    if missing_ids:
        raise gm.BadResponse(f"ids missing from answer: {missing_ids}")
    misses = {}
    with LOCK, work.open("a", encoding="utf-8") as fh:
        for i in batch:
            if variant == "wbw":  # a bad word split is not saved; it is retried (or left for a rerun)
                problem = wbw_problem(i, data[i], segs, (a.wbw_ref or {}).get(i))
                if problem:
                    misses[i] = [{"bo": "", "rendering": "", "problem": problem}]
                    continue
                data[i] = json.dumps(data[i], ensure_ascii=False)
            req = terms.get(i, [])
            plain = gloss_text(data[i]) if variant == "wbw" else data[i]
            miss = [t for t in req if not complies(t["rendering"], plain)]
            if miss:
                misses[i] = miss
            fh.write(json.dumps({"id": i, "translation": data[i], "variant": variant, "call_id": call_id,
                                 "attempt": attempt, "model": model_version,
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
        problems = any("problem" in t for m in misses.values() for t in m)
        fb = ("PREVIOUS ATTEMPT had these problems — fix them this time:\n" if problems else
              "PREVIOUS ATTEMPT missed locked terms — use them this time:\n") + "\n".join(
            f"{i}: " + "; ".join(t.get("problem") or (f"use {t['rendering']}" if a.no_tibetan else f"{t['bo']} → {t['rendering']}")
                                 for t in m) for i, m in misses.items())
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
    plain = {i: gloss_text(r["translation"]) if variant == "wbw" else r["translation"] for i, r in rows.items()}
    missed_ids = [i for i in order if i in rows
                  and any(not complies(t["rendering"], plain[i]) for t in terms.get(i, []))]
    missed = len(missed_ids)
    (track / "work").mkdir(parents=True, exist_ok=True)
    (track / "work" / "termbase-compliance.json").write_text(json.dumps(
        {i: [t["rendering"] for t in terms.get(i, []) if not complies(t["rendering"], plain[i])]
         for i in missed_ids}, ensure_ascii=False, indent=1), encoding="utf-8")
    # wbw: title and headings read as the academic track has them; the table carries the glosses
    heads = {i: r["translation"] for i, r in latest(work_file(LANG, "academic")).items()} if variant == "wbw" else plain
    title = heads.get("0", "Bodhicaryāvatāra")
    ai = AI_LABEL[LANG][variant]
    # date of the newest row, so a re-render does not change it (falls back to today)
    gen_date = max((r.get("ts", "") for r in rows.values()), default="")[:10] or _dt.date.today().isoformat()
    L = LANGS[LANG]
    if variant == "academic":
        packages = (f"context_packages: [termbase.md, aligned Sanskrit ({SA_FILE}), "
                    f"aligned commentaries: {', '.join(COMMENTARIES)}]")
    else:  # children, easy, wbw: built from the same language's academic track
        packages = f"context_packages: [termbase.md, ../{LANG}-academic/{ROOT}-{LANG}.md (meaning source)"
        packages += (f", ../en-wbw/{ROOT}-en.md (Tibetan word split)]" if variant == "wbw" and LANG != "en" else "]")
    fm = ["---", f"title: {title} — {ai}", "ai_generated: true", f"track: {track.name}", f"language: {L['name']}",
          f"lang_tag: {LANG}",
          "file_type: translation", "track_type: governed-draft", f"root_text: 1-SOURCES/Translations/{ROOT}.md",
          "source_language: tibetan", f"target_language: {L['name'].lower()}", f"generator: {model}", packages,
          f"blocks_translated: {done}", f"blocks_total: {len(order)}", f"segments_missing_locked_terms: {missed}",
          f"generation_date: {gen_date}", "status: draft", "---", ""]
    body = []
    for i in order:
        r = rows.get(i)
        if not r:
            continue
        if variant == "wbw":
            cell = lambda x: x.replace("|", "\\|").replace("\n", " ")  # noqa: E731
            table = ["| Tibetan | " + L["name"] + " |", "|---|---|"] + [
                f"| {cell(w['bo'])} | {cell(w['gloss'])} |" for w in json.loads(r["translation"])]
            head = heads.get(i, plain[i])
            if i == "0":
                body += [f"# {head} — {ai} ^0", ""] + table + [""]
            elif segs[i]["heading"]:
                body += [f"## {head} ^{i}", ""] + table + [""]
            else:
                body += [f"![[{ROOT}#^{i}]]", ""] + table + ["", f"^{i}", ""]
        elif i == "0":
            body += [f"# {r['translation']} — {ai} ^0", ""]
        elif segs[i]["heading"]:
            body += [f"## {r['translation']} ^{i}", ""]
        else:
            body += [f"![[{ROOT}#^{i}]]", "", f"{r['translation']} ^{i}", ""]
    (track / f"{stem}-{LANG}.md").write_text("\n".join(fm + body), encoding="utf-8")
    print(f"rendered {done}/{len(order)} blocks; segments still missing a locked term: {missed}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variant", required=True, choices=VARIANTS)
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
    p.add_argument("--from-track", help="build from another track's translation (e.g. academic) instead of the sources"
                                        " (easy and wbw: academic by default)")
    p.add_argument("--out-track", help="write work jsonl + render to Translations/NAME/ instead of <lang>-<variant>/"
                                       " (requirements still come from <lang>-<variant>/; e.g. a model bake-off)")
    a = p.parse_args()

    global LANG
    LANG = a.lang
    if a.variant in ("easy", "wbw") and not a.from_track:
        a.from_track = "academic"
    if not termbase_path(LANG).exists():
        sys.exit(f"no {LANG} termbase yet ({termbase_path(LANG)}): build it before translating")
    track = VAULT / f"3-TRANSFORMATIONS/Translations/{a.out_track}" if a.out_track else track_dir(LANG, a.variant)
    work = track / "work" / f"{ROOT}-{LANG}.jsonl"
    segs = {s["id"]: s for s in json.loads((TERM_RUN / "segments.json").read_text(encoding="utf-8"))}
    if a.render_only:
        return render(track, ROOT, segs, latest(work), a.variant, a.model)
    a.no_tibetan = a.model.startswith("kimi")
    if a.no_tibetan and (a.variant not in ("children", "easy") or a.from_track != "academic"):
        sys.exit(f"{a.model} rejects any prompt with Tibetan script: use it only for --variant children/easy "
                 f"with --from-track academic (the Tibetan is then left out of the prompt)")
    key_env = {"gemini-api": gm.KEY_ENV, "openai-api": "OPENAI_API_KEY",
               "moonshot-api": "MOONSHOT_API_KEY"}[llm.engine_of(a.model)]
    key = os.environ.get(key_env, "")
    if not key:
        sys.exit(f"{key_env} is not set (run via: zsh -ic 'python3 ...')")
    work.parent.mkdir(parents=True, exist_ok=True)
    system = (track_dir(LANG, a.variant) / "requirements.md").read_text(encoding="utf-8") + (
        FORMAT_WBW if a.variant == "wbw" else FORMAT)
    ctx = build_context(ROOT)
    terms = locked_terms(a.variant)
    done = latest(work)
    a.base_rows = None
    if a.from_track:
        a.base_rows = latest(work_file(LANG, a.from_track))
    a.wbw_ref = None  # wbw: the English run fixes the Tibetan word split; other languages reuse it
    if a.variant == "wbw" and LANG != "en":
        a.wbw_ref = {i: [w["bo"] for w in json.loads(r["translation"])]
                     for i, r in latest(work_file("en", "wbw")).items()} or None
        if a.wbw_ref is None:
            print("note: no en-wbw track yet, so this run makes its own Tibetan word split")
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
    if a.base_rows is not None and any(i not in a.base_rows for i in todo):
        lack = [i for i in todo if i not in a.base_rows]
        print(f"skipping {len(lack)} segments with no {LANG}-{a.from_track} translation yet: {lack[:10]}")
        todo = [i for i in todo if i in a.base_rows]
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
