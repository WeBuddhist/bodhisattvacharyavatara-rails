# SKILL: translate-plain-english

> **Draft skill** — move this file to `4-SYSTEM/Skills/translate-plain-english/SKILL.md`
> to register it in the project skill catalog.

---

## Purpose

Translate one or more chapters of the BCA into plain English at Grade 8–10 reading level,
using the Sanskrit root text (`1-SOURCES/Text/sk-dev.md`) as the primary source and
the `2-RAILS/Verses/` context packages as the interpretive authority for each verse.
Saves the result as a standalone `.md` file in the project root.

## Trigger phrases

- "translate chapter N to grade 8"
- "plain english translation of chapter N"
- "run translate-plain-english for chapter N"
- "create a grade 8 version of chapter N"

---

## Prerequisites

Before running this skill, verify:

1. `1-SOURCES/Text/sk-dev.md` exists and contains the target chapter.
2. `3-TRANSFORMATIONS/Translations/en-plain-english/requirements.md` is present.
3. `3-TRANSFORMATIONS/Translations/en-plain-english/termbase.md` is present.
4. `2-RAILS/Verses/{ch}-{v}.md` files exist for the target chapter (optional but
   strongly preferred — translation quality is higher when rails are available).

---

## Workflow

### Step 1 — Read the style contract

Read both contract files in full before writing a single verse:

```
3-TRANSFORMATIONS/Translations/en-plain-english/requirements.md
3-TRANSFORMATIONS/Translations/en-plain-english/termbase.md
```

Key rules to internalize:
- Grade 8–10 reading level. Target 15–20 words per sentence.
- Active voice. Short paragraphs (3–5 sentences).
- **No transliteration** of Sanskrit or Tibetan terms.
- Use termbase locked renderings (see table below).
- Render each verse as one prose paragraph, not poetry.
- Append the block ID (e.g. `^2-1`) at the end of the paragraph on the same line.

### Step 2 — Extract source verses from Sanskrit

Read `1-SOURCES/Text/sk-dev.md` and locate the target chapter section
(e.g. `## 2. पापदेशना...`). Extract all stanzas up to the next chapter header.
Each stanza ends with a block ID tag like `^2-1`.

Skip lines that contain `[Ed:` — these are editorial notes, not root verses.

### Step 3 — Load the rail for each verse

For each verse `^{ch}-{v}`, read `2-RAILS/Verses/{ch}-{v}.md`.

Check the YAML frontmatter: only use the rail if `status: complete`.

Extract the `## Synthesis (original language)` section. Skip lines that are:
- Obsidian transclusion refs (`![[...]]`) — these are cross-file pointers, not text
- Subsection headings (`### kunpal`, `### Consensus`, etc.)

The remaining lines are actual Tibetan summary sentences from each commentator
plus a consensus statement. These are your interpretive authority for this verse.

If no rail exists or `status` is not `complete`, proceed with Sanskrit-only (Step 4).

### Step 4 — Translate verse by verse

For each (block_id, sanskrit_stanza, synthesis?) tuple:

1. Read the Sanskrit stanza.
2. If synthesis is available: use it to resolve ambiguity in the Sanskrit. The Tibetan
   synthesis represents what four traditional commentators agree the verse means.
   Do NOT translate the Tibetan directly — use it only as an interpretive guide.
3. Apply the style contract.
4. Output: one prose paragraph + block ID inline.

**Locked term renderings (termbase)**

| Sanskrit concept | Plain English rendering |
|---|---|
| bodhicitta | the Mind of Enlightenment |
| bodhisattva / jina-putra | Hero of Enlightenment |
| sugata / tathāgata | the Blissful Ones / the Awakened One |
| dharma | the Teaching / the Truth |
| saṃsāra | the cycle of life |
| nirvāṇa | final peace / liberation |
| dharmakāya | Truth Body |
| pāpa / duṣkṛta | harmful deeds / wrongdoing |
| puṇya / kuśala | goodness / helpful deeds |
| śūnyatā | Emptiness |

> Proper names of bodhisattvas (Avalokita, Mañjughoṣa, etc.) may be kept as-is
> since they are names, not technical terms.

### Step 5 — Assemble and save the output file

File name convention:
- Single chapter: `BCA-Chapter-{N}-Plain-English.md`
- Range: `BCA-Chapters-{start}-{end}-Plain-English.md`

Save to the project root (`D:\monlam_dharmaduta\bodhisattvachartavatara-rails\`).

File structure:

```markdown
# A Guide to the Bodhisattva's Way of Life
### Plain English Translation (Grade 8)
*Translated from the Sanskrit of Śāntideva, informed by Tibetan commentary*

---

## Chapter N: [Title]

[verse paragraphs with block IDs...]

_Thus ends Chapter N: "[Title]."_

---

*Source: ...*
```

### Step 6 — Present the file

Call `mcp__cowork__present_files` with the output path so the user can open it.

---

## Automated alternative

For batch runs without an interactive session, use the Python script:

```
0-INBOX/translate-plain-english.py
```

```bash
# Install dependency (once)
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY=sk-...

# Run
python 0-INBOX/translate-plain-english.py --chapter 2
python 0-INBOX/translate-plain-english.py --chapter 1-3
python 0-INBOX/translate-plain-english.py --chapter all
```

The script automatically:
1. Reads each verse's rail from `2-RAILS/Verses/` (status: complete only)
2. Extracts the Tibetan synthesis (skipping transclusion lines)
3. Passes Sanskrit + synthesis together to the Claude API
4. Reports how many verses had rail context vs. Sanskrit-only

---

## Chapter title reference

| # | Sanskrit title | Plain English title |
|---|---|---|
| 1 | Bodhicittānuśaṃsa | The Benefits of the Mind of Enlightenment |
| 2 | Pāpadeśanā | Confessing Wrongdoing |
| 3 | Bodhicittaparigraha | Taking Up the Mind of Enlightenment |
| 4 | Bodhicittāpramāda | Carefulness |
| 5 | Saṃprajanyarakṣaṇa | Guarding Awareness |
| 6 | Kṣāntipāramitā | The Perfection of Patience |
| 7 | Vīryapāramitā | The Perfection of Effort |
| 8 | Dhyānapāramitā | The Perfection of Meditation |
| 9 | Prajñāpāramitā | The Perfection of Wisdom |
| 10 | Pariṇāmanā | Dedication |

---

## Notes

- Verse `^3-2` is absent from this Sanskrit edition (`sk-dev.md`). Insert a note:
  `*[Note: Verse 3-2 is absent from this edition of the Sanskrit text.]*`
- Variant verses marked `[Ed: Variant verse; absent from sanskrit-final.md]` are skipped.
- Rails exist for Ch1–3 only (136 verse files). Ch4–10 will use Sanskrit-only until
  verse-context-batch is run for those chapters.
- The citation chain for this skill is:
  `sk-dev.md (1-SOURCES) + 2-RAILS/Verses/ → plain-English output (3-TRANSFORMATIONS)`
- This is the only en-plain-english skill that reads Sanskrit directly. The 2-RAILS
  synthesis acts as the bridge between the Tibetan-based rail pipeline and the
  Sanskrit source text.
