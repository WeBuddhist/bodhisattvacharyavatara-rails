# Vault Annex — Bodhisattvacaryāvatāra conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: the **Bodhisattvacaryāvatāra**.

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 1. The text

This vault serves **Śāntideva's *Bodhisattvacaryāvatāra*** (བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།, *Entering the Way of the Bodhisattva*) — a 8th-century Indian Buddhist verse text in 10 chapters, composed in Sanskrit and preserved primarily through its Tibetan translation. It is one of the foundational texts of the Mahāyāna tradition, widely studied and commentated across all schools of Tibetan Buddhism.

Source-text files in `1-SOURCES/Text/` correspond to the following editions:

| Order | Edition / File | Filename |
| ----- | -------------- | -------- |
| 1 | Sanskrit Devanāgarī root text | `sk-dev-root-text.md` |

The primary text currently being railed out is the **Tibetan translation** as preserved in the Kangyur, read through the major Tibetan commentaries. Work will proceed chapter by chapter beginning with Chapter 1.

---

## 2. Addressing scheme

The *Bodhisattvacaryāvatāra* uses a standard **chapter-verse** addressing scheme across all sources.

**`verse_id_format`:** `chapter-verse`

**Format example:** `^1-1`, `^6-33`, `^10-58`

Verse numbers restart at 1 for each chapter. The text has 10 chapters; the final verse is `^10-58` (traditionally counted). Pre-chapter material (colophons, title lines, homage verses) goes under `## 0. Introduction ^0-0` with IDs `^0-1`, `^0-2`, etc.

### Heading hierarchy

| Markdown | Role | Block ID format | Example |
| -------- | ---- | --------------- | ------- |
| `#` | Title of the work | none | `# Bodhisattvacaryāvatāra` |
| `##` | Chapter | `^N-0` | `## 1. བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཕན་ཡོན། ^1-0` |
| `###` | Section (from author's own structural outline) | `^N-N-0` | `### 1.1 མདོར་བསྟན་པ། ^1-1-0` |
| `####` | Sub-section | `^N-N-N-0` | `#### 1.1.1 Sub-section ^1-1-1-0` |

Content blocks under a heading use the same numeric path with the trailing `0` replaced by a sequential number starting at `1`:

```
## 1. ལེའུ་དང་པོ། ^1-0

བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །  ^1-1

### 1.1 མདོར་བསྟན་པ། ^1-1-0

First prose block. ^1-1-1
Second prose block. ^1-1-2
```

### Verse numbering rule

Verse numbers restart at 1 at each chapter boundary. `^6-33` means chapter 6, verse 33 — not the 33rd verse of the whole text. This applies even where a source uses continuous numbering across the whole text; always convert to per-chapter IDs for block IDs, noting the continuous number in an editorial note if useful.

### Inline TOC phrases — wikilink tagging

Buddhist texts frequently contain **inline structural announcements**: sentences where the author enumerates the upcoming sections. Wrap each announced term in a wikilink pointing to the block ID of the heading it sources:

```markdown
[[#^1-0|ལེའུ་དང་པོ་]]ལ་[[#^1-1-0|མདོར་བསྟན་པ་]]དང་[[#^1-2-0|རྒྱས་པར་བཤད་པ་]]གཉིས་ཡོད་པ་ལས།
```

In the body of each section, the repetition of the section title also links to its own heading (self-referential by design). For cross-file links (e.g. a commentary tagging terms from the root text structure): `[[filename#^N-N-0|term]]`. Full rules in [`../CLAUDE.md`](../CLAUDE.md) §5b.

---

## 3. Registered commentary IDs

Every commentary file in `1-SOURCES/Commentaries/` declares a `registered_id` in its frontmatter. That short ID is the only string used to attribute claims to the commentary throughout `2-RAILS/`. Once assigned, a `registered_id` never changes.

| `registered_id` | Author (Tibetan / English) | Tier | Language | File |
| --------------- | -------------------------- | ---- | -------- | ---- |
| `kunpal` | མཁན་པོ་ཀུན་དཔལ། / Khenpo Kunpal | commentary | Tibetan | `bo-མཁན་པོ་ཀུན་དཔལ།.md` |
| `prajnakaramati` | ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། / Prajñākaramati | sub-commentary (Sanskrit/Tibetan) | Tibetan | `bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md` |
| `mipham` | འཇུ་མི་ཕམ། / Ju Mipham Rinpoche | commentary | Tibetan | `bo-འཇུ་མི་ཕམ།.md` |
| `khenpo-zhengah` | མཁན་པོ་གཞན་དགའ། / Khenpo Zhenga | commentary | Tibetan | `bo-མཁན་པོ་གཞན་དགའ།.md` |
| `gyaltsab` | རྒྱལ་ཚབ་དར་མ་རིན་ཆེན། / Gyaltsab Darma Rinchen | commentary | Tibetan | `bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md` |
| `minyak-kunzang-sonam` | མི་ཉག་ཀུན་བསོད། / Mi Nyag Kunzang Sönam | commentary | Tibetan | `bo-མི་ཉག་ཀུན་བསོད།.md` |
| `karma-lodo` | ཀརྨ་བློ་གྲོས་ཆོས་དཔལ་བཟང་པོ། / Karma Lodrö Chöpelzangpo | commentary | Tibetan | `bo-ཀརྨ་བློ་གྲོས་ཆོས་དཔལ་བཟང་པོ།.md` |
| `khenpo-kunga` | མཁན་པོ་ཀུན་དགའ་དབང་ཕྱུག | commentary | Tibetan | `bo-མཁན་པོ་ཀུན་དགའ་དབང་ཕྱུག.md` |
| `ngulchu-thogmed` | དངུལ་ཆུ་ཐོགས་མེད། / Ngülchu Thogmé | commentary | Tibetan | `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` |
| `tsawa-nyag` | ཚྭ་ཉག་ཤེས་རབ་མཐར་ཕྱིན། | commentary | Tibetan | `bo-ཚྭ་ཉག་ཤེས་རབ་མཐར་ཕྱིན།.md` |
| `drak-gyap` | བྲག་གཡབ་བློ་གྲོས། / Drakgyap Lodrö | commentary | Tibetan | `bo-བྲག་གཡབ་བློ་གྲོས།.md` |
| `tsechenrab` | གནམ་ལྕགས་སྦྲིས་གྱི་སྐྱིལ་ (placeholder) | commentary | Tibetan | `bo-སྨུག་སངས་ཀརྨ་ཚེ་དཔལ།.md` |
| `sabzang` | ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན། / Sabzang Mati Paṇchen | commentary | Tibetan | `bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md` |
| `lozang-pelzang` | ལོ་ཙཱ་བ་བློ་གྲོས་དཔལ་བཟང། | commentary | Tibetan | `bo-ལོ་ཙཱ་བ་བློ་གྲོས་དཔལ་བཟང།.md` |
| `nakpopa` | ནག་པོ་པ། / Kṛṣṇapāda | commentary | Tibetan | `bo-ནག་པོ་པ།.md` |
| `ksemadeva` | དགེ་བའི་ལྷ། / Kṣemadeva | commentary | Tibetan | `bo-དགེ་བའི་ལྷ། Kṣemadeva.md` |
| `zhechen-gyaltshab` | ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་རྣམ་རྒྱལ། / Zhechen Gyaltsab | commentary | Tibetan | `bo-ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་རྣམ་རྒྱལ།.md` |
| `druk-kunkhyen` | འབྲུག་ཀུན་མཁྱེན་པདྨ་དཀར་པོ། / Druk Kunkhyen Pema Karpo | commentary | Tibetan | `bo-འབྲུག་ཀུན་མཁྱེན་པདྨ་དཀར་པོ།.md` |
| `wuzheng` | 无著菩萨 (Wúzhuó Púsà) | commentary | Chinese | `zh-无著菩萨 造索达吉堪布译.md` |
| `dalai-lama-14` | 第十四世達賴喇嘛 | commentary | Chinese | `zh-第十四世達賴喇嘛.md` |

**Tier ordering** within a verse package's Traditional Interpretation section: lead with the primary Indian/Sanskrit source (`prajnakaramati`) if it addresses the verse, then Tibetan scholarly commentaries ordered by tradition (`kunpal`, `mipham`, `khenpo-zhengah`, `gyaltsab`), then supplementary Tibetan sources, then Chinese sources.

---

## 4. Language tracks

| Tag | Language | Script | Translation track | Plan stream |
| --- | -------- | ------ | ----------------- | ----------- |
| `-sk` | Sanskrit | Devanāgarī | — (source) | — |
| `-bo` | Tibetan | Unicode | — (primary analysis language for rails) | `bo/` |
| `-en` | English | Latin | `Translations/en-contemporary/` *(planned)* | `en/` |
| `-zh` | Chinese | Traditional Unicode | `Translations/zh-contemporary/` *(planned)* | — |

The primary analysis language for `2-RAILS/` per-commentary summaries and verse syntheses is **Tibetan** (the language most commentaries are written in). The `Local-Wiki/` and Word Analysis sections are in Tibetan; the Synthesis and Translation Notes sections are in English.

---

## 5. Bilingual glossary pairs

The consolidated bilingual glossaries in `2-RAILS/Bilingual-Glossaries/` will cover the following source→target combinations when those translation tracks are created:

| File | Source language | Target language | Status |
| ---- | --------------- | --------------- | ------ |
| `sk-bo.md` | Sanskrit | Tibetan | `draft` (planned) |
| `sk-en.md` | Sanskrit | English | `draft` (planned) |
| `bo-en.md` | Tibetan | English | `draft` (planned) |

---

## 6. Active transformation tracks

| Track folder | Category | Description | Status |
| ------------ | -------- | ----------- | ------ |
| `Adaptations/bo-kunpal-sa-bcad/` | Adaptation | Khenpo Kunpal structural outline (sa-bcad) — Tibetan | active |
| `Adaptations/bo-mchan-grel/` | Adaptation | Annotation commentary compilation — Tibetan | active |
| `Plans/spyod-jug-365/` | Plan | Bodhisattvacaryāvatāra 365-day daily study — Tibetan/English | active |
| `Translations/en-contemporary/` | Translation | Contemporary English translation | planned |

---

## 7. Source-language tags used in this vault

| Tag | Script / System | Use in this vault |
| --- | --------------- | ----------------- |
| `-sk` | Devanāgarī | Sanskrit root text (default Sanskrit tag) |
| `-sk-iast` | IAST romanisation | Sanskrit in edition files, IAST romanisation |
| `-bo` | Unicode Tibetan script | Tibetan commentaries and translations (default Tibetan tag) |
| `-bo-wy` | Wylie transliteration | Wylie edition files for computational use |
| `-zh` | Unicode Traditional Chinese | Chinese commentaries |
| `-en` | Latin | English translations and analysis |

The default for every Tibetan source is `-bo`. The default for every Sanskrit source is `-sk` (Devanāgarī).

---

## 8. Where to look next

- [`0-VAULT-Structure.md`](0-VAULT-Structure.md) — the architecture in full.
- [`../../1-SOURCES/About Sources.md`](../../1-SOURCES/About%20Sources.md) — source-file rules.
- [`../../2-RAILS/About Rails.md`](../../2-RAILS/About%20Rails.md) — rails schema.
- [`../../3-TRANSFORMATIONS/About Transformations.md`](../../3-TRANSFORMATIONS/About%20Transformations.md) — track and output rules.
- [Top-level `README.md`](../../README.md) — pipeline overview and reading paths.
