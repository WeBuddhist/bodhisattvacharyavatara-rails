#!/usr/bin/env python3
"""dm_translate.py — block-by-block zero-shot translation via DharmaMitra cat-translate.

Reads a block-ID'd source file from 1-SOURCES/, sends a SMALL BATCH of adjacent
blocks per API call (DharmaMitra's own guidance is 3-5 sentences per call),
threads the previously translated blocks back in as rolling context, and writes
both an append-only JSONL ledger (audit trail, resume point) and a rendered
block-ID-aligned markdown translation.

Batched blocks are separated by [[n]] marker lines that the model is instructed
to echo; the response is split back on those markers. If the markers do not come
back exactly 1..N, the batch is automatically retried one block per call, so
block-ID alignment can never be lost to a bad split.

Never writes to 1-SOURCES/. Output goes to a machine-baseline track folder under
3-TRANSFORMATIONS/Translations/ and never replaces an existing human or
rails-generated translation.

Endpoint: POST https://dharmamitra.org/api-search/cat-translate/v1/translate
Stdlib only (urllib) — no pip install.

Authentication: if DHARMAMITRA_API_KEY is set (in the environment, or as a
KEY=VALUE line in the vault's git-ignored 4-SYSTEM/scripts/.env), it is sent as
the X-API-Key header, which lifts the public endpoint's daily quota. Without it
the call is anonymous (public quota: 400 requests per day). The key is never
printed, logged, or written to the ledger.

Usage:
  dm_translate.py --source 1-SOURCES/Text/<file>.md --lang english
  dm_translate.py --source ... --lang german --limit 3          # smoke test
  dm_translate.py --source ... --lang english --only 1-1,1-2
  dm_translate.py --source ... --lang english --batch 1         # one block per call
  dm_translate.py --source ... --lang english --workers 4       # 4 concurrent lanes (needs a key)
  dm_translate.py --source ... --lang english --render-only     # re-render from ledger
  dm_translate.py --source ... --list                           # parse check, no calls
"""

import argparse
import concurrent.futures
import datetime as _dt
import json
import os
import pathlib
import re
import sys
import threading
import time
import urllib.error
import urllib.request

RATE_LIMIT_BACKOFF = [20, 40, 60, 90, 120, 180]

# The public endpoint enforces a DAILY quota (observed: "400 per 1 day"), not just
# a per-minute one. Backing off seconds against a daily quota is useless and just
# keeps hitting a service that has already said no, so a daily 429 aborts at once.
DAILY_LIMIT_RE = re.compile(r"per\s+1?\s*day|per\s+\d+\s*days?", re.I)


class DailyQuotaExceeded(RuntimeError):
    """The daily request quota is spent. Retrying today cannot help."""

ENDPOINT = os.environ.get(
    "DHARMAMITRA_CAT_TRANSLATE_URL",
    "https://dharmamitra.org/api-search/cat-translate/v1/translate",
)

# The key that lifts the daily quota. Read from the environment first, then from
# the vault's git-ignored 4-SYSTEM/scripts/.env (cwd = vault root, or the vault
# this script is installed in). It is a credential: never print it, never pass it
# on the command line, never commit it, never copy it into another vault's files.
API_KEY_VAR = "DHARMAMITRA_API_KEY"


def load_api_key():
    """Return (key, where-it-came-from) or ("", "none")."""
    key = os.environ.get(API_KEY_VAR, "").strip()
    if key:
        return key, "environment"
    script_vault = pathlib.Path(__file__).resolve().parents[3]   # <vault>/4-SYSTEM
    for env_file in (pathlib.Path("4-SYSTEM/scripts/.env"), script_vault / "scripts" / ".env"):
        try:
            text = env_file.read_text(encoding="utf-8")
        except OSError:
            continue
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("export "):
                line = line[7:].strip()
            if line.startswith(API_KEY_VAR + "="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                if key:
                    return key, str(env_file)
    return "", "none"


API_KEY, API_KEY_SOURCE = load_api_key()

BLOCK_ID_RE = re.compile(r"[ \t]\^([A-Za-z0-9][A-Za-z0-9._-]*)[ \t]*$")

# Language label -> vault lang tag. Extend as new tracks are commissioned.
LANG_TAGS = {
    "english": "en", "german": "de", "french": "fr", "spanish": "es",
    "italian": "it", "portuguese": "pt", "russian": "ru", "hindi": "hi",
    "nepali": "ne", "sinhala": "si", "bengali": "bn", "thai": "th",
    "vietnamese": "vi", "japanese": "ja", "korean": "ko", "mongolian": "mn",
    "chinese": "zh", "modern chinese": "zh", "indonesian": "id",
}

DEFAULT_STYLE = (
    "Translate this Tibetan verse of praise line by line: render each Tibetan "
    "line as one line of the target language, in the same order, and keep the "
    "same number of lines as the source. Devotional but clear register. Keep "
    "mantra syllables and proper names in transliteration rather than "
    "translating them. Do not add commentary, notes, or explanation."
)

# FORK(liturgy-rails): work-NEUTRAL. Anything work-specific belongs in the
# per-text "Work: …" line that is appended to this at call time.
# SINGLE-TEXT VAULT: this vault serves one text, so the preamble is generic;
# the "Work:" line carries the title and author.
DEFAULT_TRACK_PREAMBLE = (
    "A canonical Tibetan Buddhist text, translated block by block from the "
    "critical edition in this vault. The blocks below are being translated in order."
)

# SINGLE-TEXT VAULT: track layout follows the Liturgy vault —
# 3-TRANSFORMATIONS/Translations/<Generator>/<tag>/<source stem>-<tag>.md —
# so the six imported tracks and any new one share one shape.
DEFAULT_TRACK_ROOT = "3-TRANSFORMATIONS/Translations/Dharmamitra"

# Full language names the vault linter accepts in `language:` (it patches the
# field itself from `lang_tag` when they disagree, so this is a courtesy).
LANG_NAMES = {
    "en": "English", "zh": "Chinese", "hi": "Hindi", "ne": "Nepali",
    "mn": "Mongolian", "vi": "Vietnamese", "de": "German", "fr": "French",
    "es": "Spanish", "it": "Italian", "pt": "Portuguese", "ru": "Russian",
    "ja": "Japanese", "ko": "Korean", "bn": "Bengali", "th": "Thai", "si": "Sinhala",
    "id": "Indonesian", "bo": "Tibetan", "sa": "Sanskrit", "pi": "Pali",
}

# SINGLE-TEXT VAULT: the renderer rebuilds the frontmatter from the ledger on
# every run. These keys are NOT the renderer's to invent — backend ids,
# researched titles, import provenance — so they are carried over from the
# file that is being overwritten (and may be seeded with --extra-fm). Order is
# the order they are written in.
PRESERVE_FM_KEYS = [
    "title", "title_original", "title_attested", "title_source", "alt_titles",
    "translator", "license", "category_id", "edition_type", "source",
    "bdrc_work_id", "text_id", "edition_id", "toc_id", "previous_edition_id",
    "translation_of_text_id", "translation_of_edition_id",
    "imported_from", "import_note",
]

# Section headings are translated on their own (--headings), one call each,
# under this instruction rather than style.md: a heading is a label, not verse.
HEADING_STYLE = (
    "This is a section heading of a Tibetan Buddhist liturgical text. Translate it "
    "into the target language as a short heading: one line only, no sentence, no "
    "commentary, no explanation, no quotation marks. Keep any leading numeral such "
    "as '1.' exactly as it is. Keep proper names and mantra syllables in "
    "transliteration rather than translating them."
)

# --- batching -------------------------------------------------------------
# DharmaMitra's own agent chunks source into 3-5 sentence units (~80-150 source
# words) per cat-translate call and formats one sentence per line. This corpus's
# median block is 4 lines / ~152 chars, so 3 blocks lands squarely in that band.
# Latency is near-constant in input size (1 block ~8s, 5 blocks ~8s), so the
# batch is what turns a multi-hour run into a sub-hour one.
MARKER_RE = re.compile(r"^[ \t]*\[\[(\d+)\]\][ \t]*$", re.M)
MARKER_OVERHEAD = 8  # "[[12]]\n"

MARKER_CLAUSE = (
    "\n\nSEGMENTS: the source is divided into {n} numbered segments by marker lines "
    "of the form [[1]] through [[{n}]]. Translate every segment. Reproduce EVERY "
    "marker line exactly as it appears, on its own line, immediately before that "
    "segment's translation. Never translate, renumber, merge, split, reorder or "
    "omit a marker, and never add a marker that is not in the source."
)

SOURCE_LANG_FIELDS = {
    "tibetan": "input_tibetan",
    "sanskrit": "input_sanskrit",
    "chinese": "input_chinese",
    "pali": "input_pali",
}


# ---------------------------------------------------------------- parsing


def parse_source(path):
    """Return (frontmatter_dict_partial, [unit, ...]).

    unit = {"kind": "heading"|"block", "id": str|None, "text": str,
            "lines": [str], "heading": str|None}
    """
    raw = pathlib.Path(path).read_text(encoding="utf-8")
    lines = raw.split("\n")

    meta = {}
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                for fm_line in lines[1:i]:
                    m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", fm_line)
                    if m:
                        meta[m.group(1)] = m.group(2).strip().strip('"')
                lines = lines[i + 1:]
                break

    units, buf, current_heading = [], [], None

    def flush():
        nonlocal buf
        if not buf:
            return
        body = [l for l in buf if l.strip()]
        buf = []
        if not body:
            return
        m = BLOCK_ID_RE.search(body[-1])
        block_id = m.group(1) if m else None
        if m:
            body[-1] = body[-1][: m.start()].rstrip()
        units.append({
            "kind": "block",
            "id": block_id,
            "lines": body,
            "text": "\n".join(body),
            "heading": current_heading,
        })

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        if stripped.startswith("#"):
            flush()
            m = BLOCK_ID_RE.search(stripped)
            hid = m.group(1) if m else None
            htext = stripped[: m.start()].rstrip() if m else stripped
            level = len(htext) - len(htext.lstrip("#"))
            htext = htext.lstrip("#").strip()
            if level >= 2:
                current_heading = htext
            units.append({
                "kind": "heading", "id": hid, "text": htext,
                "lines": [htext], "heading": current_heading, "level": level,
            })
            continue
        buf.append(line.rstrip())
    flush()
    return meta, units


# ---------------------------------------------------------------- context


def load_glossary(path):
    """Read `source term<TAB or ' -> '>target rendering` lines. Comments with #."""
    if not path:
        return []
    entries = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for sep in ("\t", " -> ", " → ", "|"):
            if sep in line:
                src, tgt = line.split(sep, 1)
                entries.append((src.strip().strip("|").strip(), tgt.strip().strip("|").strip()))
                break
    return [e for e in entries if e[0] and e[1]]


def build_context(header, done, unit, glossary, window, char_cap):
    """Compose the `context` field: work header + glossary hits + rolling prior blocks."""
    parts = [header.strip()] if header.strip() else []

    hits = [f"{s} → {t}" for s, t in glossary if s and s in unit["text"]]
    if hits:
        parts.append("Terminology already fixed for this text:\n" + "\n".join(hits[:15]))

    rolling = []
    for rec in done[-window:] if window > 0 else []:
        rolling.append(
            f"[{rec['block_id']}] source:\n{rec['source']}\n"
            f"[{rec['block_id']}] translation already produced for this document:\n{rec['translation']}"
        )
    if rolling:
        parts.append(
            "Preceding blocks of this same document and their translations — "
            "match this terminology, register and line shape:\n\n" + "\n\n".join(rolling)
        )

    ctx = "\n\n".join(parts)
    # Trim oldest rolling entries first until under the cap.
    while len(ctx) > char_cap and rolling:
        rolling.pop(0)
        parts[-1] = (
            "Preceding blocks of this same document and their translations — "
            "match this terminology, register and line shape:\n\n" + "\n\n".join(rolling)
        )
        ctx = "\n\n".join(parts)
    return ctx[:char_cap]


# ---------------------------------------------------------------- track seeding


ABOUT_TEMPLATE = """---
title: "{title} — DharmaMitra zero-shot ({lang})"
track_type: machine-baseline
target_language: {lang}
lang_tag: {tag}
translation_of: {src}
generator: dharmamitra cat-translate v1
endpoint: {endpoint}
rails_used: none
termbase: none
status: draft
seeded: {today}
---

# {tag}-dharmamitra-zeroshot — about this track

A **machine baseline**, not a rails-governed translation track.

Every file here is raw output of DharmaMitra's public `cat-translate` endpoint,
produced in small batches of adjacent block IDs by
`4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py`, then split back
apart on segment markers so each block keeps its own record. Nothing in it
passed through `2-RAILS/`: no verse-context package, no consolidated bilingual
glossary, no per-track `termbase.md`, no human review. It therefore does **not**
satisfy the Translation-track contract in
[`../About Transformations.md`](../About%20Transformations.md) §3, and it is not
eligible to be marked `status: complete` or to be cited by any other
transformation.

## What it is for

- A comparison baseline against which a rails-governed translation can be judged.
- A drafting aid and a source of candidate renderings for
  `2-RAILS/Bilingual-Glossaries/` (via `glossary-extract-raw`).
- A fast first look at a text in a language no track covers yet.

## What governs it

| File | Role |
| --- | --- |
| `style.md` | The `style_instruction` string, sent **verbatim** to the API on every call. Edit it, then re-run with `--force` to regenerate. |
| `context-header.md` | A work-NEUTRAL, track-wide preamble prepended to every call's `context`. The per-text `Work: …` line is derived from each source's own metadata and appended after it. |
| `work/{tag}.jsonl` | Append-only ledger: one record per API call — source, translation, the exact context sent, timings. The audit trail and the resume point. |
| `{slug}-{tag}.md` | The rendered translation, block-ID aligned to the source. |

## Provenance

- Endpoint: `{endpoint}` (public, unauthenticated)
- Source: [`{src}`]({src})
- Granularity: up to 3 adjacent source block IDs per API call, never crossing a
  heading; each block still gets its own ledger record and its own block ID.
- Rolling context: the preceding translated blocks of this same document are
  threaded into each call so terminology and register stay coherent.

Regenerate or extend with:

```bash
python3 4-SYSTEM/Skills/dharmamitra-translate/scripts/dm_translate.py \\
  --source "{src}" --lang {lang}
```
"""


def seed_track(out_dir, meta, args, src_rel, slug):
    """Write the track's human-editable governing files if they are missing."""
    about = out_dir / "about.md"
    if not about.exists():
        about.write_text(ABOUT_TEMPLATE.format(
            title=meta.get("title_in_english") or meta.get("title") or src_rel,
            lang=args.lang, tag=args.lang_tag, src=src_rel, slug=slug,
            endpoint=ENDPOINT, today=_dt.date.today().isoformat(),
        ), encoding="utf-8")
        print(f"seeded {about}")
    style_md = out_dir / "style.md"
    if not style_md.exists():
        style_md.write_text(args.style.strip() + "\n", encoding="utf-8")
        print(f"seeded {style_md}")
    ch = out_dir / "context-header.md"
    if not ch.exists():
        # FORK(liturgy-rails): seed a WORK-NEUTRAL preamble. Seeding this with
        # the first text's own header is what made every later text claim to be
        # that first work; the per-text "Work:" line is appended at call time.
        ch.write_text(DEFAULT_TRACK_PREAMBLE.strip() + "\n", encoding="utf-8")
        print(f"seeded {ch}")


# ---------------------------------------------------------------- batching


def effective_char_cap(args):
    """Source-char cap for one batch, after the prompt's own cost is reserved.

    The payload the endpoint actually sees is context + style_instruction +
    source, so the batch may only spend what those leave over.
    """
    reserved = args.context_cap + len(args.style) + len(MARKER_CLAUSE) + 64
    return max(200, min(args.batch_max_chars, args.payload_cap - reserved))


def make_batches(todo, args):
    """Group blocks into API batches, largest-safe-first.

    A batch is closed when it would exceed the block, line or char cap, or when
    the next block sits under a different heading -- sections are not mixed. A
    block that alone busts a cap is sent on its own.
    """
    cap_chars = effective_char_cap(args)
    batches, cur, cur_chars, cur_lines = [], [], 0, 0
    for b in todo:
        cost_c = len(b["text"]) + MARKER_OVERHEAD
        cost_l = len(b["lines"]) + 1
        if cur and (
            len(cur) >= args.batch
            or b["heading"] != cur[-1]["heading"]
            or cur_chars + cost_c > cap_chars
            or cur_lines + cost_l > args.batch_max_lines
        ):
            batches.append(cur)
            cur, cur_chars, cur_lines = [], 0, 0
        cur.append(b)
        cur_chars += cost_c
        cur_lines += cost_l
    if cur:
        batches.append(cur)
    return batches


def split_batch_response(text, n):
    """Split a marked response into n segments; None if the markers are wrong.

    None is the signal to re-run the batch one block per call. Alignment is
    never guessed at -- a response that does not carry exactly [[1]]..[[n]],
    in order, each followed by non-empty text, is not trusted to be split.
    """
    if n == 1:
        return [text.strip()] if text.strip() else None
    hits = list(MARKER_RE.finditer(text))
    if [int(m.group(1)) for m in hits] != list(range(1, n + 1)):
        return None
    segs = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        # Strip any marker token that survived inline (own-line ones are the
        # split points); they are transport, never translation.
        seg = re.sub(r"\[\[\d+\]\]", "", text[m.end():end]).strip()
        if not seg:
            return None
        segs.append(seg)
    return segs


def build_body(batch, ctx, args):
    """Compose the request for one batch. Solo calls send style.md verbatim."""
    if len(batch) > 1:
        src = "\n".join(f"[[{i}]]\n{u['text']}" for i, u in enumerate(batch, 1))
        style = args.style + MARKER_CLAUSE.format(n=len(batch))
    else:
        src, style = batch[0]["text"], args.style
    body = {"input_tibetan": "", "input_chinese": "", "input_pali": "",
            "input_sanskrit": "", "context": ctx, "focus": args.focus,
            "target_language": args.lang, "style_instruction": style}
    body[SOURCE_LANG_FIELDS[args.source_language]] = src
    return body


# ---------------------------------------------------------------- api


def call_api(body, timeout, retries, verbose=False):
    """POST one block. Backs off hard on 429 — the endpoint is public and shared."""
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if API_KEY:
        headers["X-API-Key"] = API_KEY
    last = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(ENDPOINT, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            text = (payload.get("translation") or "").strip()
            if not text:
                raise ValueError(f"empty translation in response: {payload!r}")
            return text
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 429:
                try:
                    detail = exc.read().decode("utf-8", "replace")[:200]
                except Exception:  # noqa: BLE001 — body already consumed
                    detail = ""
                if DAILY_LIMIT_RE.search(detail):
                    raise DailyQuotaExceeded(
                        f"daily quota spent ({detail.strip()}). Retrying today will not "
                        f"help — resume tomorrow; finished blocks are already saved."
                    ) from exc
                # Shared public endpoint: throttle rather than hammer.
                wait = int(exc.headers.get("Retry-After") or 0) or RATE_LIMIT_BACKOFF[
                    min(attempt - 1, len(RATE_LIMIT_BACKOFF) - 1)]
                print(f"    ! 429 rate-limited; waiting {wait}s (attempt {attempt}/{retries})",
                      file=sys.stderr)
                time.sleep(wait)
                continue
            wait = 2 ** attempt
            print(f"    ! HTTP {exc.code} (attempt {attempt}/{retries}); retrying in {wait}s",
                  file=sys.stderr)
            time.sleep(wait)
        except Exception as exc:  # noqa: BLE001 — network/parse failures, then back off
            last = exc
            if attempt < retries:
                wait = 2 ** attempt
                print(f"    ! attempt {attempt}/{retries} failed ({exc}); retrying in {wait}s",
                      file=sys.stderr)
                time.sleep(wait)
    raise RuntimeError(f"cat-translate failed after {retries} attempts: {last}")


# ---------------------------------------------------------------- render


DM_WARNING = (
    "> [!warning] Machine baseline — not a rails-governed translation.\n"
    "> Every line below is raw DharmaMitra `cat-translate` output, produced in "
    "small batches of adjacent blocks with no termbase, no verse-context rails, "
    "and no human review. It is a comparison baseline and a drafting aid only. "
    "See `about.md` in this folder."
)


def read_frontmatter(path):
    """The `key: value` pairs of an existing note's frontmatter (quotes stripped).
    Multi-line YAML values are not handled — this vault's tracks do not use them."""
    path = pathlib.Path(path)
    if not path.exists():
        return {}
    meta = {}
    lines = path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].strip() != "---":
        return meta
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"')
    return meta


def is_heading_record(rec):
    return rec.get("kind") == "heading"


def latest_by_id(ledger):
    """-> (blocks {id: rec}, headings {id: rec}) — the newest record per id."""
    blocks, heads = {}, {}
    for r in ledger:
        (heads if is_heading_record(r) else blocks)[r["block_id"]] = r
    return blocks, heads


def render(out_md, units, ledger, meta, args, source_rel, prov=None, extra_fm=None):
    """Write the block-ID-aligned markdown for one text.

    `prov` lets a sibling generator (the gemini-translate skill) reuse this
    exact renderer — same body shape, same frontmatter skeleton — while naming
    itself honestly. It is a dict with `label` (the title suffix), `generator`,
    `endpoint`, `fields` (an ordered dict of generator-specific frontmatter
    keys that sit where `focus`/`context_blocks`/`batching` sit here) and
    `warning` (the callout text).

    SINGLE-TEXT VAULT — three things differ from the Liturgy renderer:

    * Frontmatter keys the renderer cannot know (backend ids, researched
      titles, import provenance — PRESERVE_FM_KEYS) are carried over from the
      file being overwritten, and `extra_fm` (a dict) overrides them. There is
      no separate stamping pass in this vault.
    * The frontmatter is what the vault linter expects of a `file_type:
      translation` note: `title` is the work's title in the target language,
      `root_text` points at the Tibetan, `language`/`lang_tag`/`category_id`/
      `license`/`source`/`edition_type` are present.
    * Layout `transclusion` (the default) puts an Obsidian transclusion of
      the Tibetan block above each translated block instead of a blockquote
      copy — that is what the vault parser reads the alignment from, and it
      never goes stale when the root is edited. A section heading is rendered
      from its own ledger record (kind: heading, see --headings) when one
      exists, otherwise the Tibetan heading is reproduced verbatim. The H1 is
      always the work's title from the frontmatter.
    """
    by_id, heads = latest_by_id(ledger)
    n_blocks_total = sum(1 for u in units if u["kind"] == "block" and u["id"])
    n_blocks_done = sum(1 for u in units if u["kind"] == "block" and u["id"] and u["id"] in by_id)
    if prov is None:
        prov = {
            "label": "DharmaMitra zero-shot",
            "generator": "dharmamitra cat-translate v1",
            "endpoint": ENDPOINT,
            "site": "https://dharmamitra.org",
            "fields": {
                "focus": args.focus,
                "context_blocks": args.context_blocks,
                "batching": f"<={getattr(args, 'batch', 1)} blocks/call, "
                            f"<={getattr(args, 'batch_max_chars', 0)} src chars, "
                            f"<={getattr(args, 'payload_cap', 0)} payload chars",
            },
            "warning": DM_WARNING,
        }

    kept = read_frontmatter(out_md)
    kept.update(extra_fm or {})
    source_stem = pathlib.Path(source_rel).stem
    composite = f'{meta.get("title_in_english") or meta.get("title") or source_stem} — {prov["label"]} ({args.lang})'

    def keep(key, default=""):
        v = kept.get(key)
        return v if v not in (None, "") else default

    fm = {
        "title": keep("title", composite),
        "track": f'{prov["label"]} ({args.lang})',
        "title_original": keep("title_original", meta.get("title_in_source") or meta.get("title") or ""),
        "title_attested": keep("title_attested"),
        "title_source": keep("title_source"),
        "alt_titles": keep("alt_titles"),
        "language": LANG_NAMES.get(args.lang_tag, args.lang.title()),
        "lang_tag": args.lang_tag,
        "file_type": "translation",
        "track_type": "machine-baseline",
        "root_text": source_rel,
        "translation_of_text_id": keep("translation_of_text_id", meta.get("text_id") or ""),
        "translation_of_edition_id": keep("translation_of_edition_id", meta.get("edition_id") or ""),
        "text_id": keep("text_id"),
        "edition_id": keep("edition_id"),
        "toc_id": keep("toc_id"),
        "previous_edition_id": keep("previous_edition_id"),
        "category_id": keep("category_id", meta.get("category_id") or ""),
        "license": keep("license", "public"),
        "translator": keep("translator", prov["generator"]),
        "source": keep("source", prov.get("site", "")),
        "edition_type": keep("edition_type", "critical"),
        "bdrc_work_id": keep("bdrc_work_id"),
        "source_language": args.source_language,
        "target_language": args.lang,
        "generator": prov["generator"],
        "endpoint": prov["endpoint"],
        **prov["fields"],
        "style_instruction": args.style,
        "rails_used": "none",
        "generated": _dt.date.today().isoformat(),
        "blocks_translated": n_blocks_done,
        "blocks_total": n_blocks_total,
        "headings_translated": sum(1 for u in units if u["kind"] == "heading" and u["id"] in heads),
        "imported_from": keep("imported_from"),
        "import_note": keep("import_note"),
        # SINGLE-TEXT VAULT: the machine-baseline warning lives HERE, not as a
        # callout in the body — the vault linter requires every body block that
        # is not a transclusion to end in a block id, so a callout fails lint.
        "note": re.sub(r"^> ?(\[!warning\] )?", "", prov["warning"], flags=re.M).replace("\n", " ").strip(),
        "status": "draft",
    }
    # Optional keys that carry nothing are dropped rather than written empty,
    # except the backend id slots, which stay visible as empty placeholders.
    always = {"text_id", "edition_id", "toc_id", "translation_of_text_id",
              "translation_of_edition_id", "category_id"}
    lines = ["---"]
    for k, v in fm.items():
        if v in ("", None) and k not in always:
            continue
        if isinstance(v, str) and ("\n" in v or ": " in v or v.startswith(("'", '"', "[", "{", "*", "&", "!", "%", "@", "`")) or '"' in v or v.endswith(":")):
            v = '"' + v.replace('"', "'").replace("\n", " ") + '"'
        lines.append(f"{k}: {v}" if v not in ("", None) else f"{k}:")
    lines.append("---")
    lines.append("")

    link_target = getattr(args, "transclusion_target", None) or source_stem
    for unit in units:
        if unit["kind"] == "heading":
            level = unit.get("level", 2)
            hashes = "#" * level
            hid = f" ^{unit['id']}" if unit["id"] else ""
            if level == 1:
                text = fm["title"]
            elif unit["id"] in heads:
                text = heads[unit["id"]]["translation"].strip().split("\n")[0]
            else:
                text = unit["text"]
            lines.append(f"{hashes} {text}{hid}")
            lines.append("")
            continue
        if not unit["id"]:
            continue
        rec = by_id.get(unit["id"])
        if args.layout == "parallel":
            for sl in unit["lines"]:
                lines.append(f"> {sl}")
            lines.append("")
        elif args.layout == "transclusion":
            lines.append(f"![[{link_target}#^{unit['id']}]]")
            lines.append("")
        if rec:
            tlines = rec["translation"].split("\n")
            tlines = [t for t in tlines if t.strip()]
            if not tlines:
                tlines = ["[empty]"]
            tlines[-1] = f"{tlines[-1]} ^{unit['id']}"
            lines.extend(tlines)
        else:
            lines.append(f"*[not yet translated]* ^{unit['id']}")
        lines.append("")

    pathlib.Path(out_md).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True, help="block-ID'd source file under 1-SOURCES/")
    p.add_argument("--lang", default="english", help="target language LABEL, not ISO code")
    p.add_argument("--lang-tag", default=None, help="override the vault lang tag (en, de, …)")
    p.add_argument("--source-language", default="tibetan",
                   choices=sorted(SOURCE_LANG_FIELDS), help="which input_* field to fill")
    p.add_argument("--focus", default="tibetan",
                   choices=["equal", "tibetan", "chinese", "pali", "sanskrit"])
    p.add_argument("--out", default=None, help="track folder (default: derived, see --track)")
    p.add_argument("--track", default=None,
                   help="track slug (default: <lang-tag>-dharmamitra-zeroshot)")
    p.add_argument("--style", default=None, help="style_instruction, verbatim to the API")
    p.add_argument("--style-file", default=None, help="file whose contents are the style_instruction")
    p.add_argument("--context-header", default=None,
                   help="file with the fixed work-level context prepended to every call")
    p.add_argument("--glossary", default=None,
                   help="optional 'source<TAB>target' lines; matching entries join the context")
    p.add_argument("--context-blocks", type=int, default=3,
                   help="how many prior translated blocks to thread back in (0 disables)")
    p.add_argument("--context-cap", type=int, default=3000, help="max chars of context")
    p.add_argument("--batch", type=int, default=3,
                   help="max blocks per API call (1 = one block per call, the old behaviour)")
    p.add_argument("--batch-max-chars", type=int, default=900,
                   help="max source chars in one batch (~DharmaMitra's 80-150 source words)")
    p.add_argument("--batch-max-lines", type=int, default=32,
                   help="max source lines in one batch; caps how long the output can run")
    p.add_argument("--payload-cap", type=int, default=6000,
                   help="max chars of context + style_instruction + source per call")
    p.add_argument("--only", default=None, help="comma-separated block IDs")
    p.add_argument("--limit", type=int, default=0, help="stop after N new blocks (0 = all)")
    p.add_argument("--sleep", type=float, default=None,
                   help="seconds between calls in each lane (default: 4 anonymous — the public "
                        "endpoint rate-limits above ~10/min — or 0.5 with an API key)")
    p.add_argument("--workers", type=int, default=1,
                   help="concurrent lanes for this file (default 1). Blocks are split into N "
                        "contiguous lanes, each keeping its own rolling context; headings are "
                        "sent N at a time. Needs DHARMAMITRA_API_KEY (refused anonymously).")
    p.add_argument("--timeout", type=int, default=90, help="per-call timeout (do not lower)")
    p.add_argument("--retries", type=int, default=6)
    p.add_argument("--layout", default="transclusion",
                   choices=["transclusion", "parallel", "translation-only"],
                   help="transclusion (default): an Obsidian ![[src#^id]] above each block; "
                        "parallel: a blockquote copy of the Tibetan; translation-only: neither")
    p.add_argument("--transclusion-target", default=None,
                   help="link target for the transclusion layout (default: the source stem)")
    p.add_argument("--headings", action="store_true",
                   help="translate the section headings (^N-0 units) instead of the blocks, "
                        "one call each under --heading-style; the H1 is never translated")
    p.add_argument("--heading-style", default=HEADING_STYLE,
                   help="style_instruction for --headings (default: HEADING_STYLE); append e.g. "
                        "a script requirement to match the rest of the track")
    p.add_argument("--extra-fm", default=None,
                   help="JSON file of frontmatter keys to seed/override on render "
                        "(researched title, backend ids, import provenance)")
    p.add_argument("--force", action="store_true", help="re-translate blocks already in the ledger")
    p.add_argument("--render-only", action="store_true", help="re-render markdown from the ledger")
    p.add_argument("--list", action="store_true", help="print parsed units and exit")
    p.add_argument("--dry-run", action="store_true", help="print request bodies, make no calls")
    args = p.parse_args()
    if args.sleep is None:
        args.sleep = 0.5 if API_KEY else 4.0
    args.workers = max(1, args.workers)
    if args.workers > 1 and not API_KEY and not (args.list or args.render_only or args.dry_run):
        sys.exit(f"--workers {args.workers} needs {API_KEY_VAR} (the anonymous endpoint allows "
                 f"400 calls/day and rate-limits bursts). Put it in the git-ignored "
                 f"4-SYSTEM/scripts/.env, or run with --workers 1.")

    src_path = pathlib.Path(args.source)
    if not src_path.exists():
        sys.exit(f"source not found: {src_path}")
    if "1-SOURCES" not in str(src_path.resolve()):
        print(f"note: source is outside 1-SOURCES/ ({src_path})", file=sys.stderr)

    meta, units = parse_source(src_path)
    blocks = [u for u in units if u["kind"] == "block" and u["id"]]

    if args.list:
        for u in units:
            kind = "H" if u["kind"] == "heading" else " "
            print(f"{kind} ^{u['id'] or '-':<6} {len(u['lines'])} line(s)  {u['lines'][0][:48]}")
        print(f"\n{len(blocks)} translatable blocks, "
              f"{sum(1 for u in units if u['kind'] == 'heading')} headings")
        return

    args.lang = args.lang.strip().lower()
    args.lang_tag = args.lang_tag or LANG_TAGS.get(args.lang) or re.sub(r"[^a-z]", "", args.lang)[:3]
    # SINGLE-TEXT VAULT: default track folder is <DEFAULT_TRACK_ROOT>/<tag>;
    # --track keeps the old <tag>-dharmamitra-zeroshot shape for anyone who wants it.
    if args.out:
        out_dir = pathlib.Path(args.out)
    elif args.track:
        out_dir = pathlib.Path(f"3-TRANSFORMATIONS/Translations/{args.track}")
    else:
        out_dir = pathlib.Path(f"{DEFAULT_TRACK_ROOT}/{args.lang_tag}")
    work_dir = out_dir / "work"
    work_dir.mkdir(parents=True, exist_ok=True)
    extra_fm = json.loads(pathlib.Path(args.extra_fm).read_text(encoding="utf-8")) if args.extra_fm else None

    if args.style_file:
        args.style = pathlib.Path(args.style_file).read_text(encoding="utf-8").strip()
    elif not args.style:
        style_md = out_dir / "style.md"
        args.style = (style_md.read_text(encoding="utf-8").strip()
                      if style_md.exists() else DEFAULT_STYLE)

    # FORK(liturgy-rails): the per-text "Work:" line is ALWAYS derived from the
    # text being translated. `context-header.md` is a track-wide PREAMBLE that
    # is prepended to it, never a substitute for it. It used to be seeded from
    # whichever text ran first and then read back by every later text, which
    # silently told the API that all 95 English texts were that first work.
    title = meta.get("title_in_english") or meta.get("title") or src_path.stem
    author = meta.get("author_in_english") or meta.get("author") or "unknown"
    # Authority tags ("Name [bdrc:P123]") are for the uploader, not the translator.
    title, author = (re.sub(r"\s*\[(?:bdrc|op):[^\]]*\]", "", str(x)).strip() for x in (title, author))
    work_line = (f"Work: {title} (author: {author}). A canonical Tibetan text; "
                 f"the blocks below are being translated one at a time, in order.")

    if args.context_header:
        preamble = pathlib.Path(args.context_header).read_text(encoding="utf-8").strip()
    else:
        ch = out_dir / "context-header.md"
        preamble = ch.read_text(encoding="utf-8").strip() if ch.exists() else ""

    args.context_header_text = f"{preamble}\n\n{work_line}".strip() if preamble else work_line
    args.track_preamble_text = preamble
    header = args.context_header_text

    glossary = load_glossary(args.glossary)
    # FORK(liturgy-rails): ledger is per SOURCE TEXT, not per track. This
    # corpus numbers blocks ^1, ^2 ... within each text, so one shared
    # ledger would mix blocks of different texts under the same id.
    _stem = re.sub(r'[/\\:*?"<>|]', "", src_path.stem).strip() or "text"
    ledger_path = work_dir / f"{_stem}-{args.lang_tag}.jsonl"
    ledger = []
    if ledger_path.exists():
        for line in ledger_path.read_text(encoding="utf-8").split("\n"):
            if line.strip():
                ledger.append(json.loads(line))

    # SINGLE-TEXT VAULT: the rendered file is ALWAYS <source stem>-<tag>.md,
    # never an English slug — the vault's linter/parser/uploader derive the
    # source stem from that filename, and the Gemini track already names files
    # this way.
    slug = _stem
    out_md = out_dir / f"{slug}-{args.lang_tag}.md"
    src_rel = str(src_path)

    if not args.dry_run:
        seed_track(out_dir, meta, args, src_rel, slug)
    if not args.render_only:
        print(f"auth       : {'X-API-Key from ' + API_KEY_SOURCE if API_KEY else 'none (public quota: 400 calls/day)'}"
              f"   workers={args.workers} sleep={args.sleep}s")

    def latest_records():
        """Newest record per id, blocks in source order, then headings."""
        by_block, by_head = latest_by_id(ledger)
        ordered = [by_block[b["id"]] for b in blocks if b["id"] in by_block]
        ordered += [by_head[u["id"]] for u in units
                    if u["kind"] == "heading" and u["id"] in by_head]
        return ordered

    if args.render_only:
        render(out_md, units, latest_records(), meta, args, src_rel, extra_fm=extra_fm)
        print(f"rendered {out_md} from {len(ledger)} ledger entries")
        return

    # --headings: the ^N-0 units (level >= 2) are the work list; blocks are not touched.
    if args.headings:
        heading_units = [u for u in units
                         if u["kind"] == "heading" and u["id"] and u.get("level", 2) >= 2]
        for hu in heading_units:
            hu["heading"] = None   # headings are never batched with each other's context
        _, done_heads = latest_by_id(ledger)
        wanted = [b.strip() for b in args.only.split(",")] if args.only else None
        todo = [h for h in heading_units
                if (wanted is None or h["id"] in wanted)
                and (args.force or h["id"] not in done_heads)]
        args.style = args.heading_style
        args.batch = 1
        print(f"source     : {src_path}")
        print(f"target     : {args.lang} ({args.lang_tag})   mode=headings")
        print(f"track      : {out_dir}")
        print(f"headings   : {len(heading_units)} total, {len(done_heads)} already in ledger, {len(todo)} to do")
        if args.dry_run:
            for i, hu in enumerate(todo, 1):
                print(f"[{i}/{len(todo)}] ^{hu['id']}  {hu['text'][:40]} … (dry run)")
                print(json.dumps(build_body([hu], header, args), ensure_ascii=False, indent=2))
            return
        lock, stop = threading.Lock(), threading.Event()
        n_done = 0

        def do_heading(i, hu):
            nonlocal n_done
            if stop.is_set():
                return
            body = build_body([hu], header, args)
            t0 = time.time()
            try:
                one = call_api(body, args.timeout, args.retries)
            except RuntimeError as exc:
                stop.set()
                print(f"STOPPED at ^{hu['id']}: {exc}", file=sys.stderr, flush=True)
                return
            el = time.time() - t0
            translation = one.strip().split("\n")[0].strip().strip('"').strip("'")
            rec = {
                "block_id": hu["id"], "kind": "heading", "heading": None,
                "source": hu["text"], "translation": translation,
                "target_language": args.lang, "focus": args.focus,
                "style_instruction": args.style, "context": header, "endpoint": ENDPOINT,
                "batch_size": 1, "batch_block_ids": [hu["id"]], "batch_fallback": False,
                "elapsed_s": round(el, 2),
                "ts": _dt.datetime.now().isoformat(timespec="seconds"),
            }
            with lock:
                ledger.append(rec)
                with ledger_path.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_done += 1
                print(f"[{i}/{len(todo)}] ^{hu['id']}  {hu['text'][:40]} … {el:.1f}s  {translation[:60]}",
                      flush=True)
            if args.sleep:
                time.sleep(args.sleep)

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            for fut in [pool.submit(do_heading, i, hu) for i, hu in enumerate(todo, 1)]:
                fut.result()
        if not args.dry_run:
            render(out_md, units, latest_records(), meta, args, src_rel, extra_fm=extra_fm)
            print(f"\nwrote {out_md}  ({n_done} heading(s) translated this run)")
        return

    done_ids = {r["block_id"] for r in ledger if not is_heading_record(r)}
    wanted = [b.strip() for b in args.only.split(",")] if args.only else None
    todo = [b for b in blocks
            if (wanted is None or b["id"] in wanted)
            and (args.force or b["id"] not in done_ids)]
    if args.limit:
        todo = todo[: args.limit]

    print(f"source     : {src_path}")
    print(f"target     : {args.lang} ({args.lang_tag})   focus={args.focus}")
    print(f"track      : {out_dir}")
    print(f"blocks     : {len(blocks)} total, {len(done_ids)} already in ledger, {len(todo)} to do")
    if not todo:
        render(out_md, units, latest_records(), meta, args, src_rel, extra_fm=extra_fm)
        print(f"nothing to translate; re-rendered {out_md}")
        return

    args.batch = max(1, args.batch)
    batches = make_batches(todo, args)
    print(f"batching   : {len(batches)} calls for {len(todo)} blocks "
          f"(<={args.batch} blocks, <={effective_char_cap(args)} chars, "
          f"<={args.batch_max_lines} lines per call)")

    fallbacks, diverged, n_done, stopped_at = [], [], 0, None
    lock, stop = threading.Lock(), threading.Event()   # the ledger is shared by the lanes

    def record(unit, translation, elapsed, batch_ids, ctx, fell_back):
        """Append one block's result to the ledger. One record per block ID."""
        nonlocal ledger
        rec = {
            "block_id": unit["id"],
            "heading": unit["heading"],
            "source": unit["text"],
            "translation": translation,
            "target_language": args.lang,
            "focus": args.focus,
            "style_instruction": args.style,
            "context": ctx,
            "endpoint": ENDPOINT,
            "batch_size": len(batch_ids),
            "batch_block_ids": batch_ids,
            "batch_fallback": fell_back,
            "elapsed_s": round(elapsed, 2),
            "ts": _dt.datetime.now().isoformat(timespec="seconds"),
        }
        with lock:
            ledger = [r for r in ledger if r["block_id"] != unit["id"]] + [rec]
            with ledger_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            got, want = len(translation.split("\n")), len(unit["lines"])
            if got != want:
                diverged.append((unit["id"], want, got))

    order = {b["id"]: i for i, b in enumerate(blocks)}

    def context_for(batch):
        """Rolling context: the blocks of this text that PRECEDE the batch, in
        source order (never headings, never a later block). With --workers > 1 a
        lane's first batch sees only what earlier lanes or runs have finished."""
        ids = {u["id"] for u in batch}
        first_pos = min(order[u["id"]] for u in batch)
        with lock:
            by_block, _ = latest_by_id(list(ledger))
        prior = [r for i, r in sorted((order[b], r) for b, r in by_block.items()
                                      if b in order and b not in ids and order[b] < first_pos)]
        combined = {"text": "\n".join(u["text"] for u in batch)}
        return build_context(header, prior, combined, glossary,
                             args.context_blocks, args.context_cap)

    def log(msg, err=False):
        with lock:
            print(msg, file=sys.stderr if err else sys.stdout, flush=True)

    def run_batch(bi, batch, tag):
        """Translate one batch; returns False if the run must stop."""
        nonlocal n_done, stopped_at
        ids = [u["id"] for u in batch]
        ctx = context_for(batch)
        body = build_body(batch, ctx, args)
        src_field = body[SOURCE_LANG_FIELDS[args.source_language]]
        payload = len(ctx) + len(body["style_instruction"]) + len(src_field)
        label = f"{tag}[{bi}/{len(batches)}] ^" + ",^".join(ids) + \
            f"  ({len(batch)} blk, {len(src_field)} src, {payload} payload)"
        if args.dry_run:
            log(label + " … (dry run)\n" + json.dumps(body, ensure_ascii=False, indent=2))
            return True
        t0 = time.time()
        try:
            translation = call_api(body, args.timeout, args.retries)
        except RuntimeError as exc:
            with lock:
                stopped_at = stopped_at or ids[0]
            stop.set()
            log(f"STOPPED at ^{ids[0]}: {exc}\nLedger is intact; nothing done so far is lost. "
                "Resume with the same command (already-translated blocks are skipped).", err=True)
            return False
        elapsed = time.time() - t0
        segs = split_batch_response(translation, len(batch))
        if segs is not None:
            for unit, seg in zip(batch, segs):
                record(unit, seg, elapsed, ids, ctx, False)
            with lock:
                n_done += len(batch)
            log(f"{label} … {elapsed:.1f}s  {segs[0].split(chr(10))[0][:52]}")
            return True
        # Markers came back wrong -- never guess the split. Re-run one per call.
        with lock:
            fallbacks.append(ids)
        log(f"{label} … {elapsed:.1f}s  ! marker split failed; retrying {len(batch)} blocks singly")
        for unit in batch:
            if args.sleep:
                time.sleep(args.sleep)
            solo_ctx = context_for([unit])
            solo = build_body([unit], solo_ctx, args)
            t0 = time.time()
            try:
                one = call_api(solo, args.timeout, args.retries)
            except RuntimeError as exc:
                with lock:
                    stopped_at = stopped_at or unit["id"]
                stop.set()
                log(f"STOPPED at ^{unit['id']}: {exc}", err=True)
                return False
            el = time.time() - t0
            record(unit, one.strip(), el, [unit["id"]], solo_ctx, True)
            with lock:
                n_done += 1
            log(f"{tag}    ^{unit['id']} … {el:.1f}s  {one.strip().split(chr(10))[0][:52]}")
        return True

    def run_lane(lane, tag):
        for bi, batch in lane:
            if stop.is_set():
                return
            if not run_batch(bi, batch, tag):
                return
            if args.sleep and not args.dry_run:
                time.sleep(args.sleep)

    numbered = list(enumerate(batches, 1))
    n_lanes = min(args.workers, len(numbered))
    if n_lanes <= 1:
        run_lane(numbered, "")
    else:
        # Contiguous lanes of roughly equal source size, so each keeps its own
        # rolling context; batches never cross a heading, so neither does a cut.
        sizes = [sum(len(u["text"]) for u in b) for _, b in numbered]
        target, lanes, cur, acc = sum(sizes) / n_lanes, [], [], 0
        for item, size in zip(numbered, sizes):
            cur.append(item)
            acc += size
            if acc >= target * (len(lanes) + 1) and len(lanes) < n_lanes - 1:
                lanes.append(cur)
                cur = []
        if cur:
            lanes.append(cur)
        print(f"lanes      : {len(lanes)} — " + "; ".join(
            f"L{k + 1} ^{ln[0][1][0]['id']}…^{ln[-1][1][-1]['id']} ({len(ln)} calls)"
            for k, ln in enumerate(lanes)))
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(lanes)) as pool:
            futs = [pool.submit(run_lane, ln, f"L{k + 1} ") for k, ln in enumerate(lanes)]
            for fut in futs:
                fut.result()

    if not args.dry_run:
        # Ledger is append-only; keep the last record per block for rendering.
        ordered = latest_records()
        render(out_md, units, ordered, meta, args, src_rel, extra_fm=extra_fm)
        n_blk = sum(1 for r in ordered if not is_heading_record(r))
        print(f"\nwrote {out_md}  ({n_blk}/{len(blocks)} blocks)")
        print(f"ledger {ledger_path}")
        print(f"calls  {len(batches)} planned for {len(todo)} blocks; {n_done} blocks translated")
        if fallbacks:
            print(f"note   {len(fallbacks)} batch(es) fell back to one-block calls: "
                  + "; ".join("^" + ",^".join(f) for f in fallbacks[:5])
                  + (" …" if len(fallbacks) > 5 else ""))
        if diverged:
            print(f"note   {len(diverged)} block(s) where the translation's line count "
                  f"differs from the source's (id: source→output): "
                  + ", ".join(f"^{i}: {w}→{g}" for i, w, g in diverged[:10])
                  + (" …" if len(diverged) > 10 else ""))
        if stopped_at:
            print(f"note   run stopped early at ^{stopped_at}; re-run to resume")


if __name__ == "__main__":
    main()
