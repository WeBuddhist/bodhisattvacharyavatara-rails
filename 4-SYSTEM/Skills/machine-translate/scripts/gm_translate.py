#!/usr/bin/env python3
"""gm_translate.py — block-aligned zero-shot translation of a Tibetan source via Google Gemini.

Sibling of the DharmaMitra skill's dm_translate.py, and deliberately the same
shape: it imports that script's source parser, context builder and renderer,
keeps the same per-text append-only ledger and the same track layout, so
stamp_metadata.py, translation_payloads.py and upload_translations.py work on
its output unchanged. What differs is the transport and the alignment guarantee:

  * Gemini is asked for STRUCTURED output — a JSON object with one entry per
    block id, each entry an array of lines — under a response schema. The
    response is therefore split by block AND by line without marker lines or
    guesswork.
  * Every block's line count is checked against its source before it is
    recorded. A block that comes back with the wrong number of lines is re-run
    on its own with the required count stated, up to --parity-attempts times;
    only an exact match is accepted silently. A block that never matches is
    recorded with line_parity=false and REPORTED, never quietly dropped or
    silently padded.

The source is ALWAYS the Tibetan note in 1-SOURCES/. An existing machine
translation (e.g. the DharmaMitra English track) may be threaded in as
*reference* with --reference-track; that is recorded in every ledger record and
in the frontmatter, but it is never the source and `translation_of` never
changes. A true pivot (translating FROM the English) is a different track with
a different `translation_of` and is not what this script does.

Needs GEMINI_API_KEY in the environment (exported from ~/.zshrc). Stdlib only.

Usage:
  gm_translate.py --source 1-SOURCES/Text/<file>.md --lang hindi
  gm_translate.py --source ... --lang nepali --limit 6              # smoke test
  gm_translate.py --source ... --lang mongolian --only 3,4 --force  # redo blocks
  gm_translate.py --source ... --lang vietnamese --render-only      # from ledger
  gm_translate.py --source ... --list                               # parse only
  gm_translate.py --source ... --lang hindi --dry-run               # print requests
"""

import argparse
import datetime as _dt
import importlib.util
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DM_PATH = HERE / "dm_translate.py"
_spec = importlib.util.spec_from_file_location("dm_translate", DM_PATH)
dm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dm)

API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MODEL = "gemini-3.1-pro-preview"
DEFAULT_TRACK_ROOT = "3-TRANSFORMATIONS/Translations/Gemini"
KEY_ENV = "GEMINI_API_KEY"

RATE_LIMIT_BACKOFF = [10, 20, 40, 60, 120, 180]
# A 429 whose body talks about a per-day quota cannot be waited out in seconds.
DAILY_LIMIT_RE = re.compile(r"per[\s_]*day|PerDay|daily", re.I)

LANG_TAGS = dict(dm.LANG_TAGS)

# One seed style per commissioned language. It is written to <track>/style.md
# on first run and read back VERBATIM from there afterwards, so the file, not
# this dict, is what governs a track once it exists. Edit the file.
LANG_STYLES = {
    "hi": (
        "Translate this Tibetan liturgical text into Hindi, line by line: render each "
        "Tibetan line as exactly one Hindi line, in the same order, keeping the same "
        "number of lines as the source. Write in Devanagari. Use the established "
        "Hindi/Sanskrit Buddhist vocabulary (बुद्ध, धर्म, संघ, बोधिचित्त, त्रिकाय, गुरु, शरण, "
        "पुण्य, परिणामना) rather than coining new terms or borrowing Hindu-devotional or "
        "Christian idiom; where Hindi Buddhist usage has a settled term, prefer it. "
        "Devotional but clear register, suitable for recitation, in natural Hindi word "
        "order rather than a calque of the Tibetan. Keep mantra syllables and dhāraṇīs "
        "as Devanagari transliteration of the Sanskrit (e.g. ॐ मणि पद्मे हूँ), never "
        "translated. Render buddhas, bodhisattvas and deities by their Sanskrit names in "
        "Devanagari (अवलोकितेश्वर, तारा, पद्मसम्भव, मञ्जुश्री); transliterate Tibetan personal "
        "names and place names. Do not add commentary, notes, or explanation."
    ),
    "ne": (
        "Translate this Tibetan liturgical text into Nepali, line by line: render each "
        "Tibetan line as exactly one Nepali line, in the same order, keeping the same "
        "number of lines as the source. Write standard Nepali in Devanagari (Nepali, not "
        "Hindi: Nepali verb forms, postpositions and honorifics). Use the Buddhist "
        "vocabulary current among Nepali-speaking Buddhists — Sanskrit-derived terms "
        "(बुद्ध, धर्म, संघ, बोधिचित्त, गुरु, शरण, पुण्य, परिणामना) and the forms familiar in "
        "Nepal's Tibetan Buddhist communities (गुरु रिन्पोछे, लामा). Devotional but clear "
        "register, suitable for recitation, in natural Nepali word order. Keep mantra "
        "syllables and dhāraṇīs as Devanagari transliteration of the Sanskrit (ॐ मणि पद्मे "
        "हूँ), never translated. Render buddhas, bodhisattvas and deities by their "
        "Sanskrit names in Devanagari (अवलोकितेश्वर, तारा, पद्मसम्भव, मञ्जुश्री); transliterate "
        "Tibetan personal names and place names. Do not add commentary, notes, or "
        "explanation."
    ),
    "mn": (
        "Translate this Tibetan liturgical text into Mongolian, line by line: render each "
        "Tibetan line as exactly one Mongolian line, in the same order, keeping the same "
        "number of lines as the source. Write modern Mongolian in Cyrillic script (Khalkha "
        "standard as used in Mongolia). Mongolian Buddhism has a centuries-old liturgical "
        "vocabulary derived from Tibetan — use it: бурхан, ном, хутагт, лам, ядам, дагина, "
        "сахиус, лагшин, бодь сэтгэл, буян, зориулга, аврал; and the established Mongolian "
        "names of deities (Жанрайсиг, Дарь эх, Манзушир, Очирваань, Ловон Бадамжунай). "
        "Devotional register suited to recitation, in natural Mongolian word order. Keep "
        "mantras and dhāraṇīs in Cyrillic transliteration as Mongolian practitioners "
        "recite them (Ум мани бадмэ хум), never translated. Transliterate other Tibetan "
        "personal names and place names. Do not add commentary, notes, or explanation."
    ),
    "vi": (
        "Translate this Tibetan liturgical text into Vietnamese, line by line: render each "
        "Tibetan line as exactly one Vietnamese line, in the same order, keeping the same "
        "number of lines as the source. Write Vietnamese with full diacritics. Use the "
        "Sino-Vietnamese Buddhist vocabulary standard in Vietnamese Buddhist literature "
        "(Phật, Pháp, Tăng, Bồ-đề tâm, Tam thân, Đạo sư, quy y, công đức, hồi hướng, chúng "
        "sinh) and the established Vietnamese names of buddhas and bodhisattvas (Quán Thế "
        "Âm, Văn Thù, Liên Hoa Sanh, Tara); transliterate other Tibetan names. Devotional, "
        "clear, recitable register, phrased the way Vietnamese Vajrayana communities phrase "
        "their prayers. Keep mantras and dhāraṇīs in romanized Sanskrit as Vietnamese "
        "Vajrayana practitioners write them (Om Mani Padme Hum, Om Ah Hum Vajra Guru Padma "
        "Siddhi Hum), never translated. Do not add commentary, notes, or explanation."
    ),
}

GENERIC_STYLE = (
    "Translate this Tibetan liturgical text into {language}, line by line: render each "
    "Tibetan line as exactly one line of {language}, in the same order, keeping the "
    "same number of lines as the source. Use the established Buddhist vocabulary of "
    "{language} where one exists. Devotional but clear register, suitable for "
    "recitation. Keep mantra syllables and dhāraṇīs in transliteration rather than "
    "translating them; render buddhas, bodhisattvas and deities by their conventional "
    "names in {language} where established, otherwise transliterate. Do not add "
    "commentary, notes, or explanation."
)

# Transport contract, appended to the style instruction as the system prompt.
# It is NOT style: it is what makes the response splittable by block and line.
FORMAT_RULES = """

OUTPUT CONTRACT (strict; this is transport, not style):
- You receive a JSON object {"blocks": [{"id": ..., "lines": [...]}]}: the source lines of one or more consecutive blocks of the same text.
- Return a JSON object of exactly the same shape: {"blocks": [{"id": ..., "lines": [...]}]}, with the SAME ids in the SAME order, and nothing else.
- For every block, output EXACTLY as many lines as that source block has. Line k of your output translates line k of the source and nothing else. Never merge, split, reorder, drop or add lines, and never leave a line empty.
- A line is translation only: no line numbers, no source text, no notes, no markdown, no bracketed glosses unless the style instruction asks for them.
- Never copy Tibetan punctuation or ornaments into the output (no ༈, ༄༅, །, ༔, ༎): a line that opens with an ornament in the source opens with its first word in the target.
- Headings are not sent to you; translate only what is sent."""

PARITY_CLAUSE = (
    "\n\nThis single block has exactly {n} source line(s). Your \"lines\" array for it "
    "must contain exactly {n} string(s), one per source line, in order."
)

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "blocks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "lines": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["id", "lines"],
            },
        }
    },
    "required": ["blocks"],
}

# Wrathful-deity praises, exorcisms and smoke offerings trip generic content
# filters. This is canonical liturgy; do not let a classifier drop blocks.
SAFETY_OFF = [
    {"category": c, "threshold": "BLOCK_NONE"}
    for c in ("HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH",
              "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT")
]

ABOUT_TEMPLATE = """---
title: "{tag} — Gemini zero-shot ({lang})"
track_type: machine-baseline
target_language: {lang}
lang_tag: {tag}
source_language: tibetan
generator: {model}
endpoint: {endpoint}
rails_used: none
termbase: none
status: draft
seeded: {today}
---

# Gemini/{tag} — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of Google Gemini (model `{model}`, recorded per
block in the ledger as `model_version`), produced by
`4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py`, which sends a small
batch of adjacent block IDs per call and asks for a JSON object holding one
array of lines per block. Nothing in it passed through `2-RAILS/`: no
verse-context package, no consolidated bilingual glossary, no per-track
`termbase.md`, no human review. It therefore does **not** satisfy the
Translation-track contract in
[`../../About Transformations.md`](../../About%20Transformations.md) §3, and it is
not eligible to be marked `status: complete` or to be cited by any other
transformation.

**Source.** Every block is translated from the Tibetan in `1-SOURCES/Text/`,
which is the closest thing to the original that exists. `translation_of` and the
segment alignment therefore point at the Tibetan text. If a run was given an
existing machine translation as *reference* (`--reference-track`), that fact is
recorded in the frontmatter (`reference_translation`) and on every ledger
record (`reference_used`); the reference was context, not source.

## What it is for

- A first display translation for the app in a language no track covers yet.
- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The style instruction, sent **verbatim** as the system prompt on every call (followed by the fixed output contract). Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | A work-NEUTRAL, track-wide preamble prepended to every call. The per-text `Work: …` line is derived from each source's own metadata and appended after it. |
| `work/<text>-{tag}.jsonl` | Append-only ledger, one per source text: one record per block, holding source, translation, the exact context sent, model version, token usage, line-parity result and timings. The audit trail and the resume point. |
| `<text>-{tag}.md` | The rendered translation, block-ID aligned to the source. |

## Line parity

The whole point of a block-ID-aligned track is that block `^N` here renders
block `^N` of the Tibetan, line for line. The script checks every block's line
count against its source before recording it; a block that comes back wrong is
re-run alone with the required count stated, and only an exact match is
accepted silently. Anything still divergent is recorded with
`line_parity: false` and listed in the run report for human attention.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py \\
  --source "1-SOURCES/Text/<text>.md" --lang {lang}
python3 4-SYSTEM/Skills/machine-translate/scripts/gm_translate.py \\
  --source "1-SOURCES/Text/<text>.md" --lang {lang} --headings     # section headings
```

The renderer carries the researched title, backend ids and import provenance
over from the file it overwrites (see `PRESERVE_FM_KEYS` in `dm_translate.py`),
so no separate stamping pass is needed in this vault.
"""


class DailyQuotaExceeded(RuntimeError):
    """The key's daily quota is spent. Retrying today cannot help."""


class ApiStop(RuntimeError):
    """A hard transport failure after all retries. Stop the run; ledger is intact."""


class BadResponse(RuntimeError):
    """The model answered, but not in a form that can be trusted to be split."""


# ---------------------------------------------------------------- helpers


def strip_tags(s):
    """Drop the `[person:…] [bdrc:…] [role:…]` tags stamped on `author:`."""
    return re.sub(r"\s*\[(?:person|bdrc|role):[^\]]*\]", "", s or "").strip()


def make_batches(todo, args):
    """Group blocks into calls: closed on count, heading change, chars or lines."""
    batches, cur, chars, nlines = [], [], 0, 0
    for b in todo:
        c, l = len(b["text"]), len(b["lines"])
        if cur and (
            len(cur) >= args.batch
            or b["heading"] != cur[-1]["heading"]
            or chars + c > args.batch_max_chars
            or nlines + l > args.batch_max_lines
        ):
            batches.append(cur)
            cur, chars, nlines = [], 0, 0
        cur.append(b)
        chars += c
        nlines += l
    if cur:
        batches.append(cur)
    return batches


def load_reference(track_dir, stem):
    """block_id -> translation from a sibling track's ledger for this text."""
    track = pathlib.Path(track_dir)
    tag = track.name
    led = track / "work" / f"{stem}-{tag}.jsonl"
    if not led.exists():
        return tag, {}
    latest = {}
    for line in led.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            latest[r["block_id"]] = r["translation"]
    return tag, latest


def blocks_json(batch):
    return json.dumps(
        {"blocks": [{"id": u["id"], "lines": u["lines"]} for u in batch]},
        ensure_ascii=False, indent=1)


def build_request(batch, ctx, reference, args, parity_n=None):
    """One generateContent body. Returns (body, context_text_sent)."""
    rules = FORMAT_RULES
    if getattr(args, "headings", False):
        rules = rules.replace("\n- Headings are not sent to you; translate only what is sent.", "")
    system = args.style.strip() + rules
    if parity_n is not None:
        system += PARITY_CLAUSE.format(n=parity_n)

    parts = [ctx.strip()] if ctx.strip() else []
    if reference:
        ref_tag, ref_map = reference
        hits = [(u["id"], ref_map[u["id"]]) for u in batch if u["id"] in ref_map]
        if hits:
            parts.append(
                f"Reference rendering of the SAME blocks in `{ref_tag}` (a machine "
                f"baseline; use it only to disambiguate meaning and keep terminology "
                f"consistent — translate from the Tibetan, and keep the Tibetan line "
                f"structure):\n\n"
                + "\n\n".join(f"[{i}]\n{t}" for i, t in hits)
            )
    context_text = "\n\n".join(parts)
    user = (
        (context_text + "\n\n" if context_text else "")
        + f"Translate the following block(s) from Tibetan into {args.lang}. "
          f"Return JSON only.\n\n" + blocks_json(batch)
    )
    gen = {"responseMimeType": "application/json", "responseSchema": RESPONSE_SCHEMA}
    if args.temperature is not None:
        gen["temperature"] = args.temperature
    if args.thinking:
        gen["thinkingConfig"] = {"thinkingLevel": args.thinking}
    body = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": gen,
        "safetySettings": SAFETY_OFF,
    }
    return body, context_text


# ---------------------------------------------------------------- api


def call_api(body, args, key):
    """POST once with retries. Returns (text, info). Raises ApiStop / DailyQuotaExceeded."""
    url = f"{API_BASE}/{args.model}:generateContent"
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    last = None
    for attempt in range(1, args.retries + 1):
        req = urllib.request.Request(
            url, data=data, method="POST",
            headers={"Content-Type": "application/json", "x-goog-api-key": key},
        )
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=args.timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            elapsed = time.time() - t0
            cands = payload.get("candidates") or []
            if not cands:
                reason = (payload.get("promptFeedback") or {}).get("blockReason", "no candidates")
                raise BadResponse(f"prompt blocked: {reason}")
            c = cands[0]
            finish = c.get("finishReason", "")
            text = "".join(p.get("text", "") for p in (c.get("content") or {}).get("parts", [])
                           if "text" in p)
            um = payload.get("usageMetadata") or {}
            info = {
                "model_version": payload.get("modelVersion", args.model),
                "finish_reason": finish,
                "usage": {
                    "prompt_tokens": um.get("promptTokenCount"),
                    "output_tokens": um.get("candidatesTokenCount"),
                    "thinking_tokens": um.get("thoughtsTokenCount"),
                },
                "elapsed_s": round(elapsed, 2),
            }
            if finish not in ("STOP", "") or not text.strip():
                raise BadResponse(f"finishReason={finish or '?'}, {len(text)} chars")
            return text, info
        except BadResponse:
            raise
        except urllib.error.HTTPError as exc:
            last = exc
            try:
                detail = exc.read().decode("utf-8", "replace")[:600]
            except Exception:  # noqa: BLE001
                detail = ""
            if exc.code == 429:
                if DAILY_LIMIT_RE.search(detail) and "minute" not in detail.lower():
                    raise DailyQuotaExceeded(
                        f"daily quota spent ({detail.strip()[:200]}). Resume tomorrow; "
                        f"finished blocks are already saved.") from exc
                wait = int(exc.headers.get("Retry-After") or 0) or RATE_LIMIT_BACKOFF[
                    min(attempt - 1, len(RATE_LIMIT_BACKOFF) - 1)]
                print(f"    ! 429 rate-limited; waiting {wait}s (attempt {attempt}/{args.retries})",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            if exc.code in (400, 401, 403, 404):
                raise ApiStop(f"HTTP {exc.code} from {url}: {detail}") from exc
            wait = 2 ** attempt
            print(f"    ! HTTP {exc.code} (attempt {attempt}/{args.retries}); retrying in {wait}s",
                  file=sys.stderr)
            time.sleep(wait)
        except Exception as exc:  # noqa: BLE001 — network/parse failures, then back off
            last = exc
            if attempt < args.retries:
                wait = 2 ** attempt
                print(f"    ! attempt {attempt}/{args.retries} failed ({exc}); retrying in {wait}s",
                      file=sys.stderr)
                time.sleep(wait)
    raise ApiStop(f"generateContent failed after {args.retries} attempts: {last}")


def parse_response(text, batch):
    """-> {id: [lines]} or None. Strict: ids must match the batch exactly, in order."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    blocks = data.get("blocks") if isinstance(data, dict) else None
    if not isinstance(blocks, list):
        return None
    if [str(b.get("id")) for b in blocks] != [u["id"] for u in batch]:
        return None
    out = {}
    for b in blocks:
        lines = b.get("lines")
        if not isinstance(lines, list):
            return None
        clean = [str(l).strip() for l in lines if str(l).strip()]
        if not clean:
            return None
        out[str(b["id"])] = clean
    return out


# ---------------------------------------------------------------- main


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True, help="block-ID'd Tibetan note under 1-SOURCES/")
    p.add_argument("--lang", default=None, help="target language LABEL (hindi, nepali, …)")
    p.add_argument("--lang-tag", default=None, help="vault lang tag (hi, ne, mn, vi, …)")
    p.add_argument("--out", default=None,
                   help=f"track folder (default {DEFAULT_TRACK_ROOT}/<lang-tag>)")
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--thinking", default=None, choices=[None, "low", "medium", "high"],
                   help="thinkingLevel; default = the model's own default")
    p.add_argument("--temperature", type=float, default=None,
                   help="omit to use the model default (recommended for Gemini 3)")
    p.add_argument("--style", default=None, help="style instruction, verbatim")
    p.add_argument("--style-file", default=None)
    p.add_argument("--context-header", default=None)
    p.add_argument("--glossary", default=None,
                   help="optional 'source<TAB>target' lines; matching entries join the context")
    p.add_argument("--reference-track", default=None,
                   help="a sibling track folder whose ledger renderings are threaded in "
                        "as REFERENCE (recorded; never the source)")
    p.add_argument("--context-blocks", type=int, default=6,
                   help="how many prior translated blocks of this text to thread back in")
    p.add_argument("--context-cap", type=int, default=9000, help="max chars of context")
    p.add_argument("--batch", type=int, default=8, help="max blocks per call")
    p.add_argument("--batch-max-chars", type=int, default=3000, help="max source chars per call")
    p.add_argument("--batch-max-lines", type=int, default=80, help="max source lines per call")
    p.add_argument("--parity-attempts", type=int, default=3,
                   help="solo re-runs allowed for a block whose line count is wrong")
    p.add_argument("--only", default=None, help="comma-separated block IDs")
    p.add_argument("--limit", type=int, default=0, help="stop after N new blocks (0 = all)")
    p.add_argument("--sleep", type=float, default=1.0, help="seconds between calls")
    p.add_argument("--timeout", type=int, default=240, help="per-call timeout")
    p.add_argument("--retries", type=int, default=6)
    p.add_argument("--layout", default="transclusion",
                   choices=["transclusion", "parallel", "translation-only"],
                   help="transclusion (default): an Obsidian ![[src#^id]] above each block")
    p.add_argument("--transclusion-target", default=None,
                   help="link target for the transclusion layout (default: the source stem)")
    p.add_argument("--headings", action="store_true",
                   help="translate the section headings (^N-0 units, level >= 2) in one call "
                        "instead of the blocks; the H1 is never translated")
    p.add_argument("--extra-fm", default=None,
                   help="JSON file of frontmatter keys to seed/override on render")
    p.add_argument("--force", action="store_true", help="re-translate blocks already in the ledger")
    p.add_argument("--render-only", action="store_true", help="re-render markdown from the ledger")
    p.add_argument("--list", action="store_true", help="print parsed units and exit")
    p.add_argument("--dry-run", action="store_true", help="print request bodies, make no calls")
    args = p.parse_args()

    src_path = pathlib.Path(args.source)
    if not src_path.exists():
        sys.exit(f"source not found: {src_path}")
    if "1-SOURCES" not in str(src_path.resolve()):
        sys.exit(f"refusing: source must be a note under 1-SOURCES/ ({src_path})")

    meta, units = dm.parse_source(src_path)
    all_blocks = [u for u in units if u["kind"] == "block" and u["id"]]
    # FORK(21-taras-rails): --headings makes the ^N-0 heading units the work
    # list. Each is a one-line "block" to the transport, so the JSON schema and
    # the line-parity check apply unchanged; records are marked kind: heading
    # and the renderer puts them into the `##` lines.
    if args.headings:
        blocks = [u for u in units if u["kind"] == "heading" and u["id"] and u.get("level", 2) >= 2]
        for u in blocks:
            u["heading"] = None
    else:
        blocks = all_blocks
    extra_fm = json.loads(pathlib.Path(args.extra_fm).read_text(encoding="utf-8")) if args.extra_fm else None

    if args.list:
        for u in units:
            kind = "H" if u["kind"] == "heading" else " "
            print(f"{kind} ^{u['id'] or '-':<6} {len(u['lines'])} line(s)  {u['lines'][0][:48]}")
        print(f"\n{len(blocks)} translatable blocks, "
              f"{sum(1 for u in units if u['kind'] == 'heading')} headings")
        return

    if not args.lang:
        sys.exit("--lang is required (a language label such as hindi, nepali, mongolian, vietnamese)")
    args.lang = args.lang.strip().lower()
    args.lang_tag = args.lang_tag or LANG_TAGS.get(args.lang) or re.sub(r"[^a-z]", "", args.lang)[:3]
    args.source_language = "tibetan"
    out_dir = pathlib.Path(args.out or f"{DEFAULT_TRACK_ROOT}/{args.lang_tag}")
    work_dir = out_dir / "work"
    work_dir.mkdir(parents=True, exist_ok=True)

    # Refuse to write into a folder that already holds a non-baseline translation.
    for f in out_dir.glob("*.md"):
        head = f.read_text(encoding="utf-8")[:2000]
        if "file_type: translation" in head and "track_type: machine-baseline" not in head:
            sys.exit(f"refusing: {out_dir} holds a non-baseline translation ({f.name})")

    if args.style_file:
        args.style = pathlib.Path(args.style_file).read_text(encoding="utf-8").strip()
    elif not args.style:
        style_md = out_dir / "style.md"
        args.style = (style_md.read_text(encoding="utf-8").strip() if style_md.exists()
                      else LANG_STYLES.get(args.lang_tag, GENERIC_STYLE.format(language=args.lang)))
    track_style = args.style          # what the rendered frontmatter reports
    if args.headings:
        # A heading is a label, not verse: the track's style.md still sets the
        # script, vocabulary and name conventions, and this clause narrows it.
        args.style = (args.style + "\n\nHEADINGS: each block sent is one SECTION HEADING of the "
                      "text, not verse. Render it as a short heading in the target language: "
                      "one line, no sentence, no commentary, no quotation marks. Keep any "
                      "leading numeral such as '1.' exactly as it is.")

    # Per-text "Work:" line, ALWAYS derived from the text being translated.
    title = meta.get("title") or src_path.stem
    title_en = meta.get("title_en") or meta.get("title_in_english") or ""
    author = strip_tags(meta.get("author")) or "unknown"
    work_line = (f"Work: {title}" + (f" ({title_en})" if title_en else "")
                 + f", author: {author}. A canonical Tibetan text; the blocks below are "
                   f"being translated in order.")
    if args.context_header:
        preamble = pathlib.Path(args.context_header).read_text(encoding="utf-8").strip()
    else:
        ch = out_dir / "context-header.md"
        preamble = (ch.read_text(encoding="utf-8").strip() if ch.exists()
                    else dm.DEFAULT_TRACK_PREAMBLE.strip())
    header = f"{preamble}\n\n{work_line}".strip() if preamble else work_line

    # A track may carry its own glossary: `source term<TAB>rendering` lines in
    # <track>/glossary.tsv. Entries whose source term occurs in the batch are
    # added to that call's context ("Terminology already fixed for this text").
    # This is how a recurring term-level error found in review is fixed without
    # rewriting the style prompt. --glossary overrides it.
    if not args.glossary and (out_dir / "glossary.tsv").exists():
        args.glossary = str(out_dir / "glossary.tsv")
    glossary = dm.load_glossary(args.glossary)
    stem = re.sub(r'[/\\:*?"<>|]', "", src_path.stem).strip() or "text"
    reference = load_reference(args.reference_track, stem) if args.reference_track else None
    ref_rel = str(args.reference_track).rstrip("/") if args.reference_track else "none"

    ledger_path = work_dir / f"{stem}-{args.lang_tag}.jsonl"
    ledger = []
    if ledger_path.exists():
        for line in ledger_path.read_text(encoding="utf-8").split("\n"):
            if line.strip():
                ledger.append(json.loads(line))

    out_md = out_dir / f"{stem}-{args.lang_tag}.md"
    src_rel = str(src_path)
    endpoint = f"{API_BASE}/{args.model}:generateContent"

    def seed():
        about = out_dir / "about.md"
        if not about.exists():
            about.write_text(ABOUT_TEMPLATE.format(
                tag=args.lang_tag, lang=args.lang, model=args.model, endpoint=endpoint,
                today=_dt.date.today().isoformat(), track=out_dir), encoding="utf-8")
            print(f"seeded {about}")
        style_md = out_dir / "style.md"
        if not style_md.exists():
            style_md.write_text(args.style.strip() + "\n", encoding="utf-8")
            print(f"seeded {style_md}")
        ch = out_dir / "context-header.md"
        if not ch.exists():
            ch.write_text(dm.DEFAULT_TRACK_PREAMBLE.strip() + "\n", encoding="utf-8")
            print(f"seeded {ch}")

    def do_render():
        by_block, by_head = dm.latest_by_id(ledger)
        ordered = [by_block[b["id"]] for b in all_blocks if b["id"] in by_block]
        ordered += [by_head[u["id"]] for u in units if u["kind"] == "heading" and u["id"] in by_head]
        versions = {r.get("model_version") for r in ordered if r.get("model_version")}
        style_now, args.style = args.style, track_style   # frontmatter reports style.md
        prov = {
            "label": "Gemini zero-shot",
            "generator": ",".join(sorted(versions)) if versions else args.model,
            "endpoint": endpoint,
            "site": "https://ai.google.dev",
            "fields": {
                "model": args.model,
                "thinking": args.thinking or "default",
                "temperature": "default" if args.temperature is None else args.temperature,
                "response_format": "json-schema blocks[].lines[]",
                "context_blocks": args.context_blocks,
                "batching": f"<={args.batch} blocks/call, <={args.batch_max_chars} src chars, "
                            f"<={args.batch_max_lines} src lines",
                "reference_translation": ref_rel,
                "glossary": args.glossary or "none",
                "line_parity_failures": sum(1 for r in ordered
                                            if r.get("line_parity") is False and not dm.is_heading_record(r)),
            },
            "warning": (
                "> [!warning] Machine baseline — not a rails-governed translation.\n"
                "> Every line below is raw Google Gemini output (model in the frontmatter), "
                "produced in small batches of adjacent blocks under a JSON line schema, with "
                "no termbase, no verse-context rails, and no human review. It is a first "
                "display translation and a drafting aid only. See `about.md` in this folder."
            ),
        }
        dm.render(out_md, units, ordered, meta, args, src_rel, prov=prov, extra_fm=extra_fm)
        args.style = style_now
        return [r for r in ordered if not dm.is_heading_record(r)]

    if not args.dry_run:
        seed()

    if args.render_only:
        ordered = do_render()
        print(f"rendered {out_md} from {len(ordered)} ledger entries")
        return

    key = os.environ.get(KEY_ENV, "")
    if not key and not args.dry_run:
        sys.exit(f"{KEY_ENV} is not set (it is exported from ~/.zshrc; run `source ~/.zshrc`)")

    done_ids = {r["block_id"] for r in ledger if dm.is_heading_record(r) == bool(args.headings)}
    wanted = [b.strip() for b in args.only.split(",")] if args.only else None
    todo = [b for b in blocks
            if (wanted is None or b["id"] in wanted)
            and (args.force or b["id"] not in done_ids)]
    if args.limit:
        todo = todo[: args.limit]

    print(f"source     : {src_path}")
    print(f"target     : {args.lang} ({args.lang_tag})   model={args.model}"
          f"   thinking={args.thinking or 'default'}" + ("   mode=headings" if args.headings else ""))
    print(f"track      : {out_dir}")
    print(f"reference  : {ref_rel}")
    print(f"glossary   : {args.glossary or 'none'}" + (f" ({len(glossary)} entries)" if glossary else ""))
    print(f"blocks     : {len(blocks)} total, {len(done_ids)} already in ledger, {len(todo)} to do")
    if not todo:
        do_render()
        print(f"nothing to translate; re-rendered {out_md}")
        print("SUMMARY " + json.dumps({"text": stem, "lang_tag": args.lang_tag, "blocks_total": len(blocks),
                                       "blocks_done": len(done_ids), "new": 0, "calls": 0,
                                       "fallbacks": 0, "parity_failures": [], "failed": [],
                                       "stopped_at": None}))
        return

    args.batch = max(1, args.batch)
    batches = make_batches(todo, args)
    print(f"batching   : {len(batches)} calls for {len(todo)} blocks "
          f"(<={args.batch} blocks, <={args.batch_max_chars} chars, "
          f"<={args.batch_max_lines} lines per call)")

    calls = 0
    fallbacks, parity_fail, failed, stopped_at = [], [], [], None
    n_new = 0

    def record(unit, lines, info, batch_ids, ctx, fell_back, parity, attempts):
        nonlocal ledger, n_new
        rec = {
            "block_id": unit["id"],
            "kind": "heading" if args.headings else "block",
            "heading": unit["heading"],
            "source": unit["text"],
            "translation": "\n".join(lines),
            "target_language": args.lang,
            "model": args.model,
            "model_version": info.get("model_version"),
            "thinking": args.thinking or "default",
            "temperature": args.temperature,
            "style_instruction": args.style,
            "context": ctx,
            "endpoint": endpoint,
            "batch_size": len(batch_ids),
            "batch_block_ids": batch_ids,
            "batch_fallback": fell_back,
            "line_parity": parity,
            "parity_attempts": attempts,
            "reference_used": reference[0] if reference else None,
            "usage": info.get("usage"),
            "elapsed_s": info.get("elapsed_s"),
            "ts": _dt.datetime.now().isoformat(timespec="seconds"),
        }
        ledger = [r for r in ledger
                  if not (r["block_id"] == unit["id"] and dm.is_heading_record(r) == bool(args.headings))] + [rec]
        with ledger_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        n_new += 1
        if not parity:
            parity_fail.append((unit["id"], len(unit["lines"]), len(lines)))

    order = {b["id"]: i for i, b in enumerate(blocks)}

    def context_for(batch):
        """Rolling context: the blocks of this text that PRECEDE the batch, in
        source order, already translated. dm.build_context keeps the last
        `window` of what it is given, so hand it the predecessors only."""
        first_pos = min(order[u["id"]] for u in batch)
        prior = [r for r in ledger
                 if dm.is_heading_record(r) == bool(args.headings)
                 and r["block_id"] in order and order[r["block_id"]] < first_pos]
        prior.sort(key=lambda r: order[r["block_id"]])
        combined = {"text": "\n".join(u["text"] for u in batch)}
        return dm.build_context(header, prior, combined, glossary,
                                args.context_blocks, args.context_cap)

    def solo(unit, first=None):
        """Translate one block alone until its line count matches. Returns
        (lines, info, ctx, parity, attempts) or None when every call failed."""
        want = len(unit["lines"])
        best, best_info, best_gap, best_ctx = first, {}, (abs(len(first) - want) if first else None), None
        attempts = 0
        for k in range(1, args.parity_attempts + 1):
            ctx = context_for([unit])
            body, ctx_text = build_request([unit], ctx, reference, args, parity_n=want)
            attempts += 1
            print(f"    ^{unit['id']} solo {k}/{args.parity_attempts} (want {want}) … ",
                  end="", flush=True)
            try:
                text, info = call_api(body, args, key)
                got = parse_response(text, [unit])
            except BadResponse as exc:
                print(f"bad response ({exc})")
                got = None
            if got is None:
                if args.sleep:
                    time.sleep(args.sleep)
                continue
            lines = got[unit["id"]]
            gap = abs(len(lines) - want)
            print(f"{info['elapsed_s']}s -> {len(lines)} line(s){'  OK' if gap == 0 else ''}")
            if best_gap is None or gap < best_gap:
                best, best_info, best_gap, best_ctx = lines, info, gap, ctx_text
            if gap == 0:
                return lines, info, ctx_text, True, attempts
            if args.sleep:
                time.sleep(args.sleep)
        if best is None:
            return None
        return best, best_info, best_ctx or "", False, attempts

    try:
        for bi, batch in enumerate(batches, 1):
            ids = [u["id"] for u in batch]
            ctx = context_for(batch)
            body, ctx_text = build_request(batch, ctx, reference, args)
            label = "^" + ",^".join(ids)
            src_chars = sum(len(u["text"]) for u in batch)
            print(f"[{bi}/{len(batches)}] {label}  ({len(batch)} blk, {src_chars} src, "
                  f"{len(ctx_text)} ctx) … ", end="", flush=True)

            if args.dry_run:
                print("(dry run)")
                print(json.dumps(body, ensure_ascii=False, indent=2))
                continue

            got, info, why = None, {}, ""
            try:
                text, info = call_api(body, args, key)
                calls += 1
                got = parse_response(text, batch)
                if got is None:
                    why = "response not splittable (ids or shape wrong)"
            except BadResponse as exc:
                calls += 1
                why = str(exc)

            if got is not None:
                first = got[batch[0]["id"]][0]
                print(f"{info['elapsed_s']}s  {first[:52]}")
                for unit in batch:
                    lines = got[unit["id"]]
                    if len(lines) == len(unit["lines"]):
                        record(unit, lines, info, ids, ctx_text, False, True, 1)
                        continue
                    print(f"    ^{unit['id']}: {len(unit['lines'])} source lines -> "
                          f"{len(lines)} returned; re-running alone")
                    res = solo(unit, first=lines)
                    calls += res[4] if res else args.parity_attempts
                    if res is None:
                        record(unit, lines, info, ids, ctx_text, False, False, 1)
                    else:
                        l2, i2, c2, ok, att = res
                        record(unit, l2, i2 or info, [unit["id"]], c2 or ctx_text,
                               False, ok, att + 1)
            else:
                # Never guess a split. Re-run the batch one block per call.
                print(f"! {why}; retrying {len(batch)} block(s) singly", flush=True)
                fallbacks.append(ids)
                for unit in batch:
                    res = solo(unit)
                    calls += res[4] if res else args.parity_attempts
                    if res is None:
                        failed.append(unit["id"])
                        print(f"    ^{unit['id']}: no usable response; left untranslated")
                        continue
                    l2, i2, c2, ok, att = res
                    record(unit, l2, i2, [unit["id"]], c2, True, ok, att)
            if args.sleep and bi < len(batches):
                time.sleep(args.sleep)
    except DailyQuotaExceeded as exc:
        stopped_at = "quota"
        print(f"\nSTOPPED: {exc}", file=sys.stderr)
    except ApiStop as exc:
        stopped_at = "api"
        print(f"\nSTOPPED: {exc}\nLedger is intact; re-run the same command to resume.",
              file=sys.stderr)
    except KeyboardInterrupt:
        stopped_at = "interrupt"
        print("\ninterrupted; ledger is intact", file=sys.stderr)

    if args.dry_run:
        return

    ordered = do_render()
    done_now = len({r["block_id"] for r in ledger if not dm.is_heading_record(r)})
    print(f"\nwrote {out_md}  ({len(ordered)}/{len(all_blocks)} blocks)")
    print(f"ledger {ledger_path}")
    print(f"calls  {calls} for {n_new} block(s) recorded this run")
    if fallbacks:
        print(f"note   {len(fallbacks)} batch(es) fell back to one-block calls: "
              + "; ".join("^" + ",^".join(f) for f in fallbacks[:5]))
    if parity_fail:
        print(f"note   {len(parity_fail)} block(s) recorded WITHOUT line parity "
              f"(id: source→output): "
              + ", ".join(f"^{i}: {w}→{g}" for i, w, g in parity_fail))
    if failed:
        print(f"note   {len(failed)} block(s) got no usable response: "
              + ", ".join("^" + i for i in failed))
    if stopped_at:
        print(f"note   run stopped early ({stopped_at}); re-run to resume")
    print("SUMMARY " + json.dumps({
        "text": stem, "lang_tag": args.lang_tag, "blocks_total": len(blocks),
        "blocks_done": done_now, "new": n_new, "calls": calls,
        "fallbacks": len(fallbacks),
        "parity_failures": [{"id": i, "source": w, "output": g} for i, w, g in parity_fail],
        "failed": failed, "stopped_at": stopped_at,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
