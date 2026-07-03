---
name: bo-vi-keyword-grade
description: Enriches the existing English-Tibetan keyword JSON with Vietnamese translations and audience-grade classifications, producing four separate output files (beginner / general / intermediate / advanced). Loads the pre-built base termbase, optionally extends it from a raw Vietnamese translation file, then adapts vi values per audience level. Stores verse_id in the termbase. Triggers on: "Tibetan Vietnamese keyword", "grade-level keywords", "bo-vi keyword", "audience grade enrichment", "update termbase from Vietnamese".
---

# bo-vi-keyword-grade

This skill extends the existing verse-keyword JSON
(`4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json`)
with new fields per verse (`bo_text`, `vi_text`) and two new fields per keyword (`vi`, `grade`),
then writes grade-specific output files.

The keyword Vietnamese meanings come from **two layered sources**:
1. The pre-built base termbase (`en-bo-vi-termbase-general.json`) — always loaded first
2. A raw Vietnamese translation file — optionally provided to extend/correct the base termbase

From the general-level base, grade variants (beginner / intermediate / advanced) are derived
using the adaptation rules below.

---

## Inputs

| Input | Required | Description | Path / format |
|---|---|---|---|
| **Tibetan source** | ✓ | Canonical Tibetan verse text with `^verse_id` markers. | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| **Existing keyword JSON** | ✓ | English verse text + keywords enriched with Tibetan `bo` field. | `4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json` |
| **Base termbase** | ✓ | Pre-built en→{bo, vi} termbase at general level. Always load first. | `4-SYSTEM/scripts/english_keyword/output/en-bo-vi-termbase-general.json` |
| **Raw Vietnamese translation file** | optional | Attested Vietnamese translation used to extend/correct the base termbase. | Path provided by user at run time — e.g. `3-TRANSFORMATIONS/Translations/vi-beginner-audience/BCA-Full-Beginner-Vietnamese.md` |
| **Target grade(s)** | ✓ | `beginner`, `general`, `intermediate`, `advanced`, or `all`. | Specified by user |

### Raw Vietnamese file format

A full markdown translation, one or more verses per chapter, each block closed by its
`^verse_id` marker (multi-line verses are joined into one block):

```
Con xin cúi đầu kính lễ Đức Phật — bậc đã hoàn toàn giác ngộ — và các vị Bồ Tát...
theo đúng lời Phật dạy, về cách một người bắt đầu con đường trở thành Bồ Tát. ^1-1
```

Chapter headings (`## Chương N: ...`) and closing `*Thus ends Chapter N...*` notes are not
verse content — skip them when parsing.

Every verse in this file is treated as **general / intermediate grade** unless the file's
frontmatter states otherwise (e.g. `track: vi-beginner-audience` marks it as beginner-register
source instead — adjust which output grade it seeds accordingly). It is used to:
1. Populate `vi_text` directly for the matching-grade output file
2. Identify how English keywords were rendered in that Vietnamese verse — update the working
   termbase for any keyword whose Vietnamese form differs from the base termbase

If no raw Vietnamese file is provided, base termbase alone supplies all `vi` values; `vi_text`
for each verse is assembled by locking the keyword Vietnamese forms into a translation of `text`.

---

## Termbase structure

The base termbase (`en-bo-vi-termbase-general.json`) and any updates use this structure:

```json
{
  "keyword_english": {
    "bo": "Tibetan meaning",
    "vi": "Vietnamese meaning at general level",
    "rank": 0,
    "verse_ids": ["1-1", "2-3"]
  }
}
```

**`verse_ids`** — list of verse IDs where this keyword occurs. Populated from the keyword JSON
during the build step. Allows tracing every keyword back to the verses it appears in.

If `en-bo-vi-termbase-general.json` does not exist yet, build it from scratch: start from
`en-bo-hi-termbase-general.json`'s keys (same English keyword set), drop the `hi` field, and
populate `vi` using the grade classification and adaptation rules below — cross-checking
against any raw Vietnamese file provided.

---

## Grade levels

| Grade | Audience | Language style | Keyword rank cutoff |
|---|---|---|---|
| `beginner` | General public, new to Buddhism | Plain modern Vietnamese, everyday words, Sino-Vietnamese Buddhist terms glossed in parentheses on first use. | rank ≤ 200 |
| `general` | Educated general reader | Modern standard Vietnamese. Common Sino-Vietnamese Buddhist terms used freely (Phật, Pháp, Bồ Tát, từ bi, tâm bồ đề). | rank ≤ 500 |
| `intermediate` | Students with basic Buddhist study | Mix of plain Vietnamese and precise Sino-Vietnamese terms. Readable but exact. | rank ≤ 500 |
| `advanced` | Scholars, monks, serious practitioners | Sino-Vietnamese-rich, technical Abhidharma / Madhyamaka vocabulary, Sanskrit terms transliterated or in parentheses. | all ranks |

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

### Vietnamese keyword meanings — grade-differentiated examples

| English | beginner `vi` | general `vi` | intermediate `vi` | advanced `vi` |
|---|---|---|---|---|
| compassion | lòng thương người | từ bi | từ bi | từ bi (đại bi tâm) |
| emptiness | sự trống rỗng của mọi thứ | tánh không | tánh không | tánh không (vô tự tính) |
| merit | việc tốt, phước đức | công đức | công đức / phước đức | phước đức, công đức |
| bodhichitta | tâm muốn giúp tất cả mọi người | tâm bồ đề | tâm bồ đề | tâm bồ đề (bồ đề tâm) |
| suffering | khổ, nỗi khổ | khổ đau | khổ đau | khổ đau (khổ đế) |
| bodhisattva | vị Bồ Tát, người phát nguyện cứu giúp chúng sinh | Bồ Tát | Bồ Tát | Bồ Tát (Bồ-đề-tát-đỏa) |
| samsara | vòng sinh tử luân hồi | luân hồi | luân hồi | luân hồi (sinh tử luân hồi) |
| nirvana | sự giải thoát hoàn toàn khỏi khổ đau | niết bàn | niết bàn | Niết-bàn (Nirvāṇa) |
| afflictions (kleshas) | cảm xúc xấu | phiền não | phiền não | phiền não (kleśa) |
| mindfulness | luôn để ý, tỉnh táo | chánh niệm | chánh niệm | chánh niệm (smṛti) |
| dedication | chia sẻ công đức cho người khác | hồi hướng | hồi hướng | hồi hướng công đức |
| patience | kiên nhẫn, nhịn nhục | nhẫn nhục | nhẫn nhục | nhẫn nhục ba-la-mật |
| diligence | cố gắng, chăm chỉ | tinh tấn | tinh tấn | tinh tấn ba-la-mật |
| refuge | nương tựa | quy y | quy y, nương tựa | quy y Tam Bảo |

Keep `vi` values short (1–6 words). Match Buddhist context, not generic dictionary meaning.
Prefer forms already attested in an existing Vietnamese translation over inventing new ones.

---

## Adapting grades from the general base

The base termbase holds general-level `vi` values. Adapt them per grade:

- **general → beginner**: Replace Sino-Vietnamese/Sanskrit terms with plain Vietnamese
  equivalents or short glosses. Remove jargon.
  E.g. `tâm bồ đề` → `tâm muốn giúp tất cả mọi người`, `từ bi` → `lòng thương người`,
  `tánh không` → `sự trống rỗng của mọi thứ`.
- **general → intermediate**: Keep Sino-Vietnamese Buddhist terms. May add a precision
  qualifier. E.g. `công đức` → `công đức / phước đức`.
- **general → advanced**: Add Sanskrit/Pali technical terms in parentheses, increase
  precision. E.g. `tánh không` → `tánh không (vô tự tính)`.

For `vi_text` (verse-level translation):
- **beginner missing** → take general `vi_text`, simplify register, gloss Sino-Vietnamese
  terms in parentheses on first use.
- **advanced missing** → take intermediate `vi_text`, add Sanskrit/Pali technical terms in
  parentheses.
- Never leave `vi_text` empty.

---

## Output format

```json
{
  "verse_id": {
    "text": "English — unchanged",
    "bo_text": "Tibetan source lines — added",
    "vi_text": "Vietnamese translation at this grade — added",
    "keywords": [
      {
        "key": "english_term",
        "rank": 0,
        "score": 0.0,
        "count": 0,
        "bo": "Tibetan meaning — unchanged",
        "vi": "Vietnamese meaning at this grade — added",
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
4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_beginner.json
4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_general.json
4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_intermediate.json
4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_advanced.json
```

Produce only the grade(s) the user requested (`all` = all four).

This skill writes only to `4-SYSTEM/scripts/english_keyword/output/`. It never modifies
`1-SOURCES/`, the existing enriched JSON, or the user's raw Vietnamese file.

### Filesystem write pattern (critical for Windows NTFS mount)

Always write to `/tmp` first, then copy:

```python
import json, shutil

REPO = '/sessions/<session-id>/mnt/bodhisattvacharyavatara-rails'
OUT  = f'{REPO}/4-SYSTEM/scripts/english_keyword/output'

GRADE_FILE = {
    "beginner":     "bo_vi_keyword_beginner.json",
    "general":      "bo_vi_keyword_general.json",
    "intermediate": "bo_vi_keyword_intermediate.json",
    "advanced":     "bo_vi_keyword_advanced.json",
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
before the copy step. Never `python3` a script directly against a file that was just written
to the mounted path in the same turn — read it back and diff against the `/tmp` source first;
this mount has been observed to silently truncate files. Prefer running any Python logic
against a `/tmp` copy of the script and inputs, then copying only the finished output back.

---

## Procedure

### Step 1 — Load base termbase

```python
import json

REPO = '/sessions/<session-id>/mnt/bodhisattvacharyavatara-rails'
OUT  = f'{REPO}/4-SYSTEM/scripts/english_keyword/output'

with open(f'{OUT}/en-bo-vi-termbase-general.json', encoding='utf-8') as f:
    termbase = json.load(f)
# termbase: { "keyword": { "bo": "...", "vi": "...", "rank": N, "verse_ids": [...] } }
```

If the file does not exist yet, build it once from `en-bo-hi-termbase-general.json` (same
keys, same `bo`/`rank`/`verse_ids`, `vi` populated per the grade-differentiated examples
table and cross-checked against any raw Vietnamese file).

### Step 2 — Load keyword JSON and populate verse_ids

```python
with open(f'{OUT}/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json', encoding='utf-8') as f:
    kw_data = json.load(f)

for vid, verse in kw_data.items():
    for kw in verse.get('keywords', []):
        key = kw['key'].lower()
        if key in termbase:
            if 'verse_ids' not in termbase[key]:
                termbase[key]['verse_ids'] = []
            if vid not in termbase[key]['verse_ids']:
                termbase[key]['verse_ids'].append(vid)
        else:
            termbase[key] = {
                'bo':       kw.get('bo', ''),
                'vi':       '',           # filled in step 4
                'rank':     kw['rank'],
                'verse_ids': [vid],
            }
```

### Step 3 — Parse raw Vietnamese file (if provided)

```python
import re

vi_map = {}  # {verse_id: vi_text}
if vietnamese_file_path:
    text = open(vietnamese_file_path, encoding='utf-8').read()
    pending = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('![[') or line.startswith('*Thus ends'):
            continue
        if re.match(r'^#{1,6}\s', line):
            continue
        m = re.search(r'\^([\w\-]+)\s*$', line)
        if m:
            vid = m.group(1)
            last = line[: m.start()].strip()
            if last:
                pending.append(last)
            vi_map[vid] = ' '.join(pending).strip()
            pending = []
        else:
            pending.append(line)
    print(f"Parsed {len(vi_map)} Vietnamese verses")
```

### Step 4 — Extend termbase from raw Vietnamese file

For each keyword that appears in the Vietnamese verse text, check whether the Vietnamese
rendering in that verse differs from the base termbase value. If it does, update
`termbase[key]['vi']` to the attested form and log the change.

```python
for vid, vi_text in vi_map.items():
    verse_kws = kw_data.get(vid, {}).get('keywords', [])
    for kw in verse_kws:
        key = kw['key'].lower()
        entry = termbase.get(key, {})
        base_vi = entry.get('vi', '')
        if base_vi and base_vi in vi_text:
            pass  # confirmed
        elif not base_vi:
            # Inspect vi_text to identify how this keyword was rendered
            # in this verse and set termbase[key]['vi'] accordingly
            pass
```

After scanning, save the updated termbase back (via the `/tmp`-then-copy pattern above):

```python
tmp_tb = '/tmp/en-bo-vi-termbase-general.json'
dst_tb = f'{OUT}/en-bo-vi-termbase-general.json'
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

For each grade to produce, derive grade-specific `vi` values from the general base:

```python
def adapt_vi(key, base_vi, grade):
    """Adapt a general-level vi value to the target grade."""
    # beginner: plain Vietnamese, gloss/replace Sino-Vietnamese terms
    # intermediate: keep Sino-Vietnamese terms, minor precision additions
    # advanced: add Sanskrit/Pali technical terms in parentheses
    # Consult the grade-differentiated examples table for key Buddhist terms.
    ...

grade_termbase = {}
for grade in target_grades:
    grade_termbase[grade] = {}
    for key, entry in termbase.items():
        grade_termbase[grade][key] = adapt_vi(key, entry.get('vi',''), grade)
```

### Step 7 — Build output files

For each target grade:

```python
RANK_CUTOFF = {'beginner': 200, 'general': 500, 'intermediate': 500, 'advanced': 9_999_999}

output_data = {grade: {} for grade in target_grades}

for vid, verse in kw_data.items():
    bo_text = bo_map.get(vid, '')
    base_vi_text = vi_map.get(vid, '')

    for grade in target_grades:
        cutoff = RANK_CUTOFF[grade]
        vi_text = derive_grade_vi_text(base_vi_text, grade)  # adapt register if needed

        filtered_kws = []
        for kw in verse.get('keywords', []):
            if kw['rank'] > cutoff:
                continue
            key = kw['key'].lower()
            vi  = grade_termbase[grade].get(key, kw['key'])  # fallback to English key
            filtered_kws.append({
                'key':   kw['key'],
                'rank':  kw['rank'],
                'score': kw['score'],
                'count': kw['count'],
                'bo':    kw.get('bo', ''),
                'vi':    vi,
                'grade': grade,
            })

        output_data[grade][vid] = {
            'text':     verse.get('text', ''),
            'bo_text':  bo_text,
            'vi_text':  vi_text,
            'keywords': filtered_kws,
        }
```

### Step 8 — Save outputs and verify

Use the filesystem write pattern in the Output files section above.
Print a summary for each grade file: verse count, keyword count, any empty `vi` values.

---

## Completion check

- [ ] Base termbase loaded from `en-bo-vi-termbase-general.json` (built from
      `en-bo-hi-termbase-general.json`'s keys if it did not already exist).
- [ ] `verse_ids` populated in termbase from keyword JSON.
- [ ] Raw Vietnamese file parsed (if provided): `{verse_id → vi_text}` built.
- [ ] Termbase extended/corrected from raw Vietnamese file; updated termbase saved back.
- [ ] Tibetan source parsed: `{verse_id → bo_text}` built for all verses.
- [ ] Existing keyword JSON loaded; all original fields kept unchanged.
- [ ] Grade-adapted `vi` values derived for each target grade.
- [ ] `bo_text` and `vi_text` set for every verse in each output file.
- [ ] Every keyword has `vi` and `grade` fields; rank cutoff applied.
- [ ] Output files saved via `/tmp` → `shutil.copy2`; verified with `json.load`.
- [ ] No `1-SOURCES/` file or the existing enriched JSON modified.
