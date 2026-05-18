---
name: json-to-commentary
description: Convert tipitaka.org Atthakatha and Tiká JSON exports into properly formatted Markdown commentary files for 1-SOURCES/Commentaries/. Handles heading hierarchy, continuous ^1-V verse IDs, root-text transclusions from inline verse references, and gatha stanza grouping.
---

# JSON to Commentary

Converts tipitaka.org Atthakathā / Ṭīkā JSON exports into Markdown commentary files
that follow `4-SYSTEM/Guidelines/source-formatting.md`, placing output in `1-SOURCES/Commentaries/`.

Source files covered:

| JSON file | Commentary | Output |
|-----------|-----------|--------|
| `abh01a.json` | Aṭṭhasālinī (Dhammasaṅgaṇī-aṭṭhakathā) | `pi-dhammasangani-atthakatha.md` |
| `abh01t.json` | Dhammasaṅgaṇī-mūlaṭīkā | `pi-dhammasangani-mulatiika.md` |
| `abh04t.json` | Dhammasaṅgaṇī-anuṭīkā | `pi-dhammasangani-anutiika.md` |

---

## Output structure

```
# Abhidhammapiṭake (aṭṭhakathā) ^atthakatha-0   ← h1  pitaka
## <book title> ^1-0                              ← h2  this commentary
### <chapter> ^1-<ch>-0                           ← h3  JSON source chapter
#### <sub-section> ^1-<ch>-<n>-0                 ← h4  title/subhead within ch
##### <deeper section> ^1-<ch>-<n>-<m>-0         ← h5  subhead after a title

![[1-SOURCES/Text/pi-dhammasangani.md#^1-0a-1]]   ← transclusion of root verse

Commentary paragraph text. ^1-V                   ← two-level verse ID
```

**Heading IDs** carry the full number depth: `^1-4-2-3-0` means book 1, chapter 4, h4 section 2, h5 section 3.

**Verse IDs** are always two levels: `^1-V` where `1` = Dhammasaṅgaṇī (book 1 of the pitaka commentary) and `V` is a **continuous counter through the whole file** — it never resets at chapter or section boundaries.

**Inline numbers** in the source (e.g. `"1. Kusalā dhammā…"`, `"1-6. Dukamātikāyaṃ…"`) are **root-text verse references**, not commentary verse numbers. The converter strips them and inserts the corresponding root-text transclusion(s) before the paragraph. The stripped paragraph then gets its own sequential `^1-V` commentary ID.

---

## Running the converter

**Standard run** (bypasses .pyc cache — required on this mounted filesystem):

```python
python3 -c "
import sys, pathlib, types, os
os.chdir('path/to/abhidhamma-rails')  # set to vault root
src = pathlib.Path('4-SYSTEM/Skills/json-to-commentary/scripts/converters/tipitaka_org_atthakatha.py').read_bytes().rstrip(b'\x00').decode('utf-8')
mod = types.ModuleType('conv')
exec(compile(src, 'tipitaka_org_atthakatha.py', 'exec'), mod.__dict__)
mod.convert_json_to_commentary(
    '0-INBOX/raw-data/abh01a.json',
    '0-INBOX/temp/pi-dhammasangani-atthakatha.md')
"
```

Output goes to `0-INBOX/temp/` for review. Once verified, move to `1-SOURCES/Commentaries/`.

> **Important — null bytes:** Files written through the Cowork mounted filesystem are sometimes padded with null bytes. The `read_bytes().rstrip(b'\x00')` call in the run snippet handles this automatically. If running the converter produces a `SyntaxError: source code string cannot contain null bytes`, strip them first:
> ```python
> python3 -c "
> import pathlib
> p = pathlib.Path('4-SYSTEM/Skills/json-to-commentary/scripts/converters/tipitaka_org_atthakatha.py')
> p.write_bytes(p.read_bytes().rstrip(b'\x00'))
> "
> ```

---

## Configuring for a new source file

The converter has two sections to adjust before running on `abh01t.json` or `abh04t.json`:

### 1. Inspect the JSON chapters

Run a quick inspection to see which chapter numbers exist and what their titles are:

```python
python3 -c "
import json
with open('0-INBOX/raw-data/abh01t.json') as f:
    data = json.load(f)
segs = data['segments']
seen = {}
for s in segs:
    ch = s['chapter']
    if ch not in seen and s.get('css_class') == 'chapter':
        seen[ch] = s['content']
for ch, title in sorted(seen.items()):
    print(f'ch{ch}: {title!r}')
"
```

### 2. Update `CHAPTER_ROOT_TEXT_CONTEXT`

In `tipitaka_org_atthakatha.py`, find the `CHAPTER_ROOT_TEXT_CONTEXT` dict and add entries for the new file's chapters:

```python
CHAPTER_ROOT_TEXT_CONTEXT: dict[int, str | None] = {
    # abh01t — Dhammasaṅgaṇī-mūlaṭīkā (inspect chapters first)
    0: None,       # intro — no root-text refs
    1: "toc_a",    # adjust based on chapter titles
    2: "toc_b",
    3: "main",
    # ... add more as needed
}
```

Resolution tokens:

| Token | Resolves to | Root-text section |
|-------|------------|-------------------|
| `"toc_a"` | `^1-0a-N` | Tikamātikā verses |
| `"toc_b"` | `^1-0b-N` | Dukamātikā verses |
| `"main"` | `^1-N` | Main text (Cittuppādakaṇḍa onwards) |
| `None` | no transclusion | Intro / heading-only chapters |

---

## Post-conversion review

### Frontmatter

Check that `root_text`, `source_description`, `source_url`, and `other_ids` are populated. The `registered_id` field is not generated automatically — add it manually after checking `4-SYSTEM/CLAUDE.md`.

### Heading IDs

Every `###`, `####`, and `#####` heading must end with `^1-<ch>-...-0`. Sample check:

```bash
grep "^###\|^####\|^#####" 0-INBOX/temp/<output>.md | head -20
```

### Verse IDs

Verse IDs run `^1-1` through `^1-N` continuously. Check first and last:

```bash
grep " \^1-[0-9]*$" 0-INBOX/temp/<output>.md | head -3
grep " \^1-[0-9]*$" 0-INBOX/temp/<output>.md | tail -3
```

### Transclusions

Transclusions appear immediately before commentary paragraphs. Spot-check that:
- Tikamātikā chapter references resolve to `^1-0a-N`
- Dukamātikā range references (`"1-6. …"`) produce the correct number of transclusion lines
- Main-text references resolve to `^1-N`

```bash
grep "!\[\[" 0-INBOX/temp/<output>.md | head -10
```

### Content fidelity

Compare `total_segments` in the JSON against the paragraph count in the output. The converter skips structural segments (nikaya, book, chapter headings) and merges gatha lines into stanzas, so the output paragraph count is always lower than `total_segments`. A rough guide: expect roughly 70–80% of `total_segments` to become verse blocks.

---

## CSS class → output role reference

| CSS class | Role | Output |
|-----------|------|--------|
| `chapter` | h3 heading | `### <title> ^1-ch-0` |
| `title` | h4 heading | `#### <title> ^1-ch-n-0` |
| `subhead` | h4 or h5 | `####` before title; `#####` after |
| `subsubhead` | h4 or h5 | same as subhead |
| `bodytext` | verse | detect inline N., emit transclusion + `^1-V` |
| `indent` | verse | same as bodytext |
| `unindented` | verse | same as bodytext |
| `gatha1/2/3` | gatha line (accumulate) | no ID until `gathalast` |
| `gathalast` | gatha stanza end | emit accumulated lines + `^1-V` |
| `centered` | closing summary | emit as verse + `^1-V` |
| `nikaya` | pitaka heading | extracted to `# … ^atthakatha-0` |
| `book` | book heading | extracted to `## … ^1-0` |

---

## Converter script location

```
4-SYSTEM/Skills/json-to-commentary/
├── SKILL.md           ← this file
└── scripts/
    └── converters/
        └── tipitaka_org_atthakatha.py
```
