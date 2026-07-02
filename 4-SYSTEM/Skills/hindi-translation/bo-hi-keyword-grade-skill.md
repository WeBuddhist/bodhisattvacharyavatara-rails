---
name: bo-hi-keyword-grade
description: Enriches the existing English-Tibetan keyword JSON with Hindi translations and audience-grade classifications, producing four separate output files (beginner / general / intermediate / advanced). Loads the pre-built base termbase, optionally extends it from a raw Hindi translation file, then adapts hi values per audience level. Stores verse_id in the termbase. Triggers on: "Tibetan Hindi keyword", "grade-level keywords", "bo-hi keyword", "audience grade enrichment", "update termbase from Hindi".
---

# bo-hi-keyword-grade

This skill extends the existing verse-keyword JSON
(`4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json`)
with new fields per verse (`bo_text`, `hi_text`) and two new fields per keyword (`hi`, `grade`),
then writes grade-specific output files.

The keyword Hindi meanings come from **two layered sources**:
1. The pre-built base termbase (`en-bo-hi-termbase-general.json`) — always loaded first
2. A raw Hindi translation file — optionally provided to extend/correct the base termbase

From the general-level base, grade variants (beginner / intermediate / advanced) are derived
using the adaptation rules below.

---

## Inputs

| Input | Required | Description | Path / format |
|---|---|---|---|
| **Tibetan source** | ✓ | Canonical Tibetan verse text with `^verse_id` markers. | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| **Existing keyword JSON** | ✓ | English verse text + keywords enriched with Tibetan `bo` field. | `4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json` |
| **Base termbase** | ✓ | Pre-built en→{bo, hi} termbase at general level. Always load first. | `4-SYSTEM/scripts/english_keyword/output/en-bo-hi-termbase-general.json` |
| **Raw Hindi translation file** | optional | Ungraded Hindi translation used to extend/correct the base termbase. | Path provided by user at run time |
| **Target grade(s)** | ✓ | `beginner`, `general`, `intermediate`, `advanced`, or `all`. | Specified by user |

### Raw Hindi file format

One verse per line; verse ID is the `^verse_id` marker at the end of the line:

```
सुगत, उनके पुत्रों और धर्मकाय सहित सभी वन्दनीयों को प्रणाम करके... ^1-1
```

Every verse in this file is treated as **general / intermediate grade**. It is used to:
1. Populate `hi_text` directly for general/intermediate output files
2. Identify how English keywords were rendered in that Hindi verse — update the working termbase
   for any keyword whose Hindi form differs from the base termbase

If no raw Hindi file is provided, base termbase alone supplies all `hi` values; `hi_text` for
each verse is assembled by locking the keyword Hindi forms into a translation of `text`.

---

## Termbase structure

The base termbase (`en-bo-hi-termbase-general.json`) and any updates use this structure:

```json
{
  "keyword_english": {
    "bo": "Tibetan meaning",
    "hi": "Hindi meaning at general level",
    "rank": 0,
    "verse_ids": ["1-1", "2-3"]
  }
}
```

**`verse_ids`** — list of verse IDs where this keyword occurs. Populated from the keyword JSON
during the build step. Allows tracing every keyword back to the verses it appears in.

---

## Grade levels

| Grade | Audience | Language style | Keyword rank cutoff |
|---|---|---|---|
| `beginner` | General public, new to Buddhism | Plain modern Hindi, everyday words, no unglossed Sanskrit. | rank ≤ 200 |
| `general` | Educated general reader | Modern standard Hindi. Common Sanskrit Buddhist terms used freely. | rank ≤ 500 |
| `intermediate` | Students with basic Buddhist study | Mix of Hindi and classical Sanskrit terms. Precise but readable. | rank ≤ 500 |
| `advanced` | Scholars, monks, serious practitioners | Sanskrit-rich, technical Abhidharma / Madhyamaka vocabulary. | all ranks |

### Grade classification — keywords

**beginner** — terms a newcomer understands after one teaching:
> buddha, dharma, karma, compassion, virtue, mind, suffering, body, death, birth, joy, faith, peace

**intermediate** — terms requiring study of basic Buddhist philosophy:
> bodhichitta, bodhisattva, emptiness, samsara, nirvana, merit, refuge, precepts, mindfulness,
> attachment, afflictions, wisdom, samadhi, dedication, renunciation, patience, diligence

**advanced** — technical Abhidharma, Madhyamaka, or tantric terminology:
> dharmakaya, tathagatagarbha, alayavijnana, dependent origination (technical), two truths,
> trikaya, prajnaparamita, madhyamaka, shamatha, vipashyana, any transliterated Skt/Tib term

When a keyword sits on a boundary, assign the lower (more accessible) grade.

### Hindi keyword meanings — grade-differentiated examples

| English | beginner `hi` | general `hi` | intermediate `hi` | advanced `hi` |
|---|---|---|---|---|
| compassion | दया | करुणा | करुणा | करुणा / अनुकम्पा |
| emptiness | खालीपन | शून्यता | शून्यता | शून्यता (सर्वधर्मनिःस्वभावता) |
| merit | पुण्य | पुण्य | पुण्य / कुशल | कुशलकर्म |
| bodhichitta | सबके भले की इच्छा | बोधिचित्त | बोधिचित्त | बोधिचित्त (संवोधिचित्त) |
| suffering | दुःख | दुःख | दुःख | दुःख (सर्वसंस्कारदुःखता) |

Keep `hi` values short (1–5 words). Match Buddhist context, not generic dictionary meaning.

---

## Adapting grades from the general base

The base termbase holds general-level `hi` values. Adapt them per grade:

- **general → beginner**: Replace Sanskrit terms with plain Hindi equivalents. Remove jargon.
  E.g. `बोधिचित्त` → `सबके भले की इच्छा`, `करुणा` → `दया`, `शून्यता` → `खालीपन`.
- **general → intermediate**: Keep Sanskrit Buddhist terms. May add a precision qualifier.
  E.g. `पुण्य` → `पुण्य / कुशल`.
- **general → advanced**: Add Abhidharma/Madhyamaka Sanskrit in parentheses, increase precision.
  E.g. `शून्यता` → `शून्यता (सर्वधर्मनिःस्वभावता)`.

For `hi_text` (verse-level translation):
- **beginner missing** → take general `hi_text`, simplify register, gloss Sanskrit on first use.
- **advanced missing** → take intermediate `hi_text`, add Sanskrit technical terms in parentheses.
- Never leave `hi_text` empty.

---

## Output format

```json
{
  "verse_id": {
    "text": "English — unchanged",
    "bo_text": "Tibetan source lines — added",
    "hi_text": "Hindi translation at this grade — added",
    "keywords": [
      {
        "key": "english_term",
        "rank": 0,
        "score": 0.0,
        "count": 0,
        "bo": "Tibetan meaning — unchanged",
        "hi": "Hindi meaning at this grade — added",
        "grade": "beginner"
      }
    ]
  }
}
```

**Keyword filtering per output file:**
- `beginner`: rank ≤ 200
- `general` / `intermediate`: rank ≤ 500
- `advanced`: all ranks

---

## Output files

```
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_beginner.json
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_general.json
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_intermediate.json
4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_advanced.json
```

Produce only the grade(s) the user requested (`all` = all four).

This skill writes only to `4-SYSTEM/scripts/english_keyword/output/`. It never modifies
`1-SOURCES/`, the existing enriched JSON, or the user's raw Hindi file.

### Filesystem write pattern (critical for Windows NTFS mount)

Always write to `/tmp` first, then copy:

```python
import json, shutil

REPO = '/sessions/keen-peaceful-rubin/mnt/bodhisattvacharyavatara-rails'
OUT  = f'{REPO}/4-SYSTEM/scripts/english_keyword/output'

GRADE_FILE = {
    "beginner":     "bo_hi_keyword_beginner.json",
    "general":      "bo_hi_keyword_general.json",
    "intermediate": "bo_hi_keyword_intermediate.json",
    "advanced":     "bo_hi_keyword_advanced.json",
}

for grade, data in output_data.items():
    fname = GRADE_FILE[grade]
    tmp   = f'/tmp/{fname}'
    dst   = f'{OUT}/{fname}'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    shutil.copy2(tmp, dst)
    with open(dst, encoding='utf-8') as f:
        check = json.load(f)
    print(f'{grade}: {len(check)} verses → {fname}')
```

If a destination file does not yet exist on the mount, create it with the Write tool (`{}`)
before the copy step.

---

## Procedure

### Step 1 — Load base termbase

```python
import json

REPO = '/sessions/keen-peaceful-rubin/mnt/bodhisattvacharyavatara-rails'
OUT  = f'{REPO}/4-SYSTEM/scripts/english_keyword/output'

with open(f'{OUT}/en-bo-hi-termbase-general.json', encoding='utf-8') as f:
    termbase = json.load(f)
# termbase: { "keyword": { "bo": "...", "hi": "...", "rank": N, "verse_ids": [...] } }
```

### Step 2 — Load keyword JSON and populate verse_ids

```python
with open(f'{OUT}/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json', encoding='utf-8') as f:
    kw_data = json.load(f)

# Add verse_ids to every termbase entry from the keyword JSON
for vid, verse in kw_data.items():
    for kw in verse.get('keywords', []):
        key = kw['key'].lower()
        if key in termbase:
            if 'verse_ids' not in termbase[key]:
                termbase[key]['verse_ids'] = []
            if vid not in termbase[key]['verse_ids']:
                termbase[key]['verse_ids'].append(vid)
        else:
            # New keyword not yet in termbase — add stub
            termbase[key] = {
                'bo':       kw.get('bo', ''),
                'hi':       '',           # filled in step 4
                'rank':     kw['rank'],
                'verse_ids': [vid],
            }
```

### Step 3 — Parse raw Hindi file (if provided)

```python
import re

hi_map = {}  # {verse_id: hi_text}
if hindi_file_path:
    with open(hindi_file_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            m = re.search(r'\^([\w-]+)\s*$', line)
            if not m: continue
            vid  = m.group(1)
            text = re.sub(r'\s*\^[\w-]+\s*$', '', line).strip()
            if text and not text.startswith('#') and not text.startswith('![['):
                hi_map[vid] = text
    print(f"Parsed {len(hi_map)} Hindi verses")
```

### Step 4 — Extend termbase from raw Hindi file

For each keyword that appears in the Hindi verse text, check whether the Hindi rendering in that
verse differs from the base termbase value. If it does, update `termbase[key]['hi']` to the
attested form and log the change.

```python
# For each verse, scan hi_text for known keyword Hindi forms
for vid, hi_text in hi_map.items():
    verse_kws = kw_data.get(vid, {}).get('keywords', [])
    for kw in verse_kws:
        key = kw['key'].lower()
        entry = termbase.get(key, {})
        base_hi = entry.get('hi', '')
        # If base_hi appears in the Hindi text, confirm. If a different form appears, log.
        # (Claude inspects the Hindi text to find the attested rendering for this keyword)
        if base_hi and base_hi in hi_text:
            pass  # confirmed
        elif not base_hi:
            # Try to identify how this keyword was rendered in this verse's Hindi text
            # and set termbase[key]['hi'] accordingly
            pass
```

After scanning, save the updated termbase back:

```python
tmp_tb = '/tmp/en-bo-hi-termbase-general.json'
dst_tb = f'{OUT}/en-bo-hi-termbase-general.json'
with open(tmp_tb, 'w', encoding='utf-8') as f:
    json.dump(termbase, f, ensure_ascii=False, indent=2)
shutil.copy2(tmp_tb, dst_tb)
print(f"Termbase updated: {len(termbase)} entries")
```

### Step 5 — Parse Tibetan source

```python
bo_map = {}
current_lines = []
with open(f'{REPO}/1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md', encoding='utf-8') as f:
    for raw_line in f:
        line = raw_line.rstrip()
        m = re.search(r'\^([\w-]+)\s*$', line)
        if m:
            vid = m.group(1)
            this_line = re.sub(r'\s*\^[\w-]+\s*$', '', line).strip()
            all_lines = current_lines + ([this_line] if this_line else [])
            tibetan = [l for l in all_lines
                       if l and not l.startswith('![[') and not l.startswith('#')]
            if tibetan:
                bo_map[vid] = '\n'.join(tibetan)
            current_lines = []
        else:
            s = line.strip()
            current_lines = [s] if (s and not s.startswith('![[') and not s.startswith('#')) else []
```

### Step 6 — Build grade-adapted termbase variants

For each grade to produce, derive grade-specific `hi` values from the general base:

```python
def adapt_hi(key, base_hi, grade):
    """Adapt a general-level hi value to the target grade."""
    # beginner: plain Hindi, no Sanskrit
    # intermediate: keep Sanskrit terms, minor precision additions
    # advanced: add Abhidharma Sanskrit in parentheses
    # Consult the grade-differentiated examples table for key Buddhist terms.
    ...

grade_termbase = {}
for grade in target_grades:
    grade_termbase[grade] = {}
    for key, entry in termbase.items():
        grade_termbase[grade][key] = adapt_hi(key, entry.get('hi',''), grade)
```

### Step 7 — Build output files

For each target grade:

```python
RANK_CUTOFF = {'beginner': 200, 'general': 500, 'intermediate': 500, 'advanced': 9_999_999}

output_data = {grade: {} for grade in target_grades}

for vid, verse in kw_data.items():
    bo_text = bo_map.get(vid, '')
    # hi_text: use hi_map if available, else derive from English text with locked terms
    base_hi_text = hi_map.get(vid, '')

    for grade in target_grades:
        cutoff = RANK_CUTOFF[grade]
        hi_text = derive_grade_hi_text(base_hi_text, grade)  # adapt register if needed

        filtered_kws = []
        for kw in verse.get('keywords', []):
            if kw['rank'] > cutoff:
                continue
            key = kw['key'].lower()
            hi  = grade_termbase[grade].get(key, kw['key'])  # fallback to English key
            filtered_kws.append({
                'key':   kw['key'],
                'rank':  kw['rank'],
                'score': kw['score'],
                'count': kw['count'],
                'bo':    kw.get('bo', ''),
                'hi':    hi,
                'grade': grade,
            })

        output_data[grade][vid] = {
            'text':     verse.get('text', ''),
            'bo_text':  bo_text,
            'hi_text':  hi_text,
            'keywords': filtered_kws,
        }
```

### Step 8 — Save outputs and verify

Use the filesystem write pattern (Step 6 in the Output files section above).
Print a summary for each grade file: verse count, keyword count, any empty `hi` values.

---

## Completion check

- [ ] Base termbase loaded from `en-bo-hi-termbase-general.json`.
- [ ] `verse_ids` populated in termbase from keyword JSON.
- [ ] Raw Hindi file parsed (if provided): `{verse_id → hi_text}` built.
- [ ] Termbase extended/corrected from raw Hindi file; updated termbase saved back.
- [ ] Tibetan source parsed: `{verse_id → bo_text}` built for all verses.
- [ ] Existing keyword JSON loaded; all original fields kept unchanged.
- [ ] Grade-adapted `hi` values derived for each target grade.
- [ ] `bo_text` and `hi_text` set for every verse in each output file.
- [ ] Every keyword has `hi` and `grade` fields; rank cutoff applied.
- [ ] Output files saved via `/tmp` → `shutil.copy2`; verified with `json.load`.
- [ ] No `1-SOURCES/` file or the existing enriched JSON modified.
