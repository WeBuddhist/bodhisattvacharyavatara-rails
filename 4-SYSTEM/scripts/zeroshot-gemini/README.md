# zeroshot-gemini

Zero-shot translation driver for Railroads source files, using the Gemini API.

Translates a block-ID'd source into any target language while keeping the output
**structurally interchangeable with the source**: same block IDs, same order,
same line counts. The style of the translation is not decided here — it comes
entirely from a track's `requirements.md`, which is injected into the prompt
verbatim and treated as authoritative.

That separation is the point. Anything about register, vocabulary, loanwords,
punctuation or layout belongs in `requirements.md`, where a human can read and
edit it. Anything about structure belongs in this code, where a machine can
enforce it.

---

## Sources

The vault defaults, overridable on every run:

| Role | Default path |
|---|---|
| Meaning base (authoritative) | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| Disambiguation reference | `1-SOURCES/Text/BCAV08_SH_sk.md` |

The Sanskrit is supplied per block, aligned by block ID, and the prompt is
explicit that it exists only to resolve ambiguity — the Tibetan is the meaning
base and wins wherever the two genuinely differ. Alignment is reported at the
start of every run (currently 920 of 927 source blocks have a Sanskrit
parallel).

No other source is read. No translation witnesses, no rails, no glossary,
unless you pass `--termbase` explicitly.

---

## Install

```bash
pip install google-genai        # required
pip install python-dotenv       # optional; the script also parses .env itself
```

The API key is read from `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) in the project
`.env` or the environment.

---

## Usage

Always dry-run first. It builds and saves every prompt, makes no API call, and
spends nothing:

```bash
python 4-SYSTEM/scripts/zeroshot-gemini/translate.py \
  --requirements "3-TRANSFORMATIONS/Translations/en-verse-plain/requirements.md" \
  --target-lang  "English" \
  --track        "en-verse-plain" \
  --chapters     1 \
  --dry-run
```

Then translate for real:

```bash
python 4-SYSTEM/scripts/zeroshot-gemini/translate.py \
  --requirements "3-TRANSFORMATIONS/Translations/en-verse-plain/requirements.md" \
  --target-lang  "English" \
  --track        "en-verse-plain" \
  --chapters     1
```

Resume an interrupted run — accepted windows come from cache and cost nothing:

```bash
... --chapters 1-10 --resume
```

Another language, another contract — same driver:

```bash
python 4-SYSTEM/scripts/zeroshot-gemini/translate.py \
  --requirements "3-TRANSFORMATIONS/Translations/hi-poetic/requirements.md" \
  --target-lang  "Hindi" \
  --track        "hi-poetic" \
  --chapters     all
```

A prose track, where the verse hard-break convention does not apply:

```bash
... --requirements ".../en-plain-english/requirements.md" --no-hard-breaks
```

### Scope syntax

`--chapters` accepts `all`, a single chapter `3`, a range `1-3`, a list
`1,4,7`, `front` (the `^I-*` title block), or `back` (colophons `^a-*`, `^b-*`).

### Key options

| Option | Default | Why you'd change it |
|---|---|---|
| `--model` | `gemini-2.5-pro` | `gemini-2.5-flash` for cheap smoke tests |
| `--max-blocks` | 25 | Lower it if long chapters drift or truncate |
| `--max-chars` | 6000 | Same |
| `--repair-attempts` | 2 | Structural round-trips before the run stops |
| `--termbase` | none | Point at a `termbase.md` to lock renderings |
| `--no-hard-breaks` | off | Prose tracks |
| `--allow-editorial` | off | Tracks that permit `[Ed: …]` notes |
| `--temperature` | 0.3 | |

---

## What it guarantees

Every window of blocks is validated against the source *before* it is accepted:

| Check | Rule |
|---|---|
| V1 | Block-ID set and order identical to the source window |
| V2 | Output line count per block == source line count |
| V3 | Final line ends with a single space then the block ID |
| V4 | No Tibetan or Devanagari leaked into the output |
| V5 | No `[Ed: …]` notes, no footnote markers (unless allowed) |
| V6 | Two trailing spaces on non-final lines (applied mechanically) |

A window that fails goes back to Gemini with the specific errors listed, up to
`--repair-attempts` times. If it still fails, **the run stops** — the failed
outputs are left in the work directory for inspection. A chapter is never
shipped with a missing verse or a collapsed stanza.

The mechanical contract was calibrated against
`4-SYSTEM/Skills/translate-zero-shot-verse/reference/gold-chapter-01.md`: the
human-approved gold chapter passes the validator with zero errors and survives a
byte-identical round trip. The checks enforce the house style rather than
fighting it.

What it does **not** check is meaning, register, or terminology. Run
`translation-qa` for those.

---

## Output

```
3-TRANSFORMATIONS/Translations/<track>/Chapter-01.md   … Chapter-10.md
                                      Section-I.md, Section-a.md, Section-b.md
0-INBOX/zeroshot-gemini/<track>/                       prompts, caches, failures
```

Every generated file carries `status: draft` plus `context_packages`,
`style_contract` and the generating model. Nothing is ever written to
`1-SOURCES/`. **Only a domain specialist promotes a file to `status: complete`,
and only after `translation-qa` runs clean of critical and major errors.**

---

## Files

| File | Role |
|---|---|
| `translate.py` | CLI, windowing, Gemini calls, retry/repair/resume, output assembly |
| `structure.py` | Parses a block-ID'd source into `Document` → `Section` → `Block` |
| `prompt.py` | Assembles the prompt; keeps style (from `requirements.md`) and structure (from code) separate |
| `validate.py` | The V1–V6 conformance checks and block normalisation |

`structure.py` doubles as a structural audit tool:

```bash
python 4-SYSTEM/scripts/zeroshot-gemini/structure.py \
  "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
```
