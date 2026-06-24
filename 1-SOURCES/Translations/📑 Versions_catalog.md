---
title: "སྤྱོད་འཇུག་གི་འགྱུར་མ་དཀར་ཆག — Versions / Translations Catalog"
file_type: reference
language: bo, en
lang_tag: bo
source_description: "Records the root-text versions and translations of the Bodhisattvacaryāvatāra held in 1-SOURCES/Translations/, with their vault-internal book_id catalog codes."
last_updated: 2026-06-24
---

# སྤྱོད་འཇུག་གི་འགྱུར་མ་དཀར་ཆག
## Versions / Translations Catalog — *Bodhisattvacaryāvatāra*

This catalog lists the direct versions and translations of the *Bodhisattvacaryāvatāra* (བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ།) by Śāntideva that are held in `1-SOURCES/Translations/`. Each row carries the translator, the languages and verse coverage recorded in the file's frontmatter, and the vault-internal `book_id` catalog code. Commentaries are cataloged separately in [`../Commentaries/📑 Commentaries_catalog.md`](../Commentaries/📑%20Commentaries_catalog.md).

---

## Summary Statistics

| Language | Versions |
| -------- | -------- |
| Tibetan (canonical) | 1 |
| English | 3 |
| Chinese | 5 |
| **Total** | **9** |

---

## Book IDs (catalog codes)

Each version carries a vault-internal catalog code in its `book_id` frontmatter field, built per the cataloging convention in [`../About Sources.md`](../About%20Sources.md) §3a:

```
[Root Title]-[Language & Resource Type]-[Century][Author Code]
```

**Root-title code:** `BCA` — *Bodhicaryāvatāra*. **Language codes:** `EN` English · `BO` Tibetan · `SA` Sanskrit · `ZH` Chinese (vault extension). **Resource type:** `V` version/direct translation of the root text · `C` commentary.

Translator codes are the uppercase initials of the translator; for Tibetan and Chinese translators the initials are taken from the romanised name. The century is the century in which the version was made. Centuries marked ⚑ are inferred and should be confirmed against the colophon or publication record before the code is finalised.

| # | Language | Title | Translator | `book_id` | Coverage | Century basis |
| - | -------- | ----- | ---------- | --------- | -------- | ------------- |
| 1 | Tibetan | བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། | Sarvajñādeva & Bande Paltsek; rev. Dharmaśrībhadra, Rinchen Zangpo, Śākya-blo-gros; fin. Sumatikīrti & Blo ldan shes rab | `BCA-BOV-11BLS` ⚑ | 1-1–10-61 | Canonical Kangyur translation; final revision c. 11th c. (first translation 9th c.) — verify |
| 2 | English | Entering the Way of the Bodhisattva | David Karma Choephel (bhikshu Karma Lodrö Choephel) | `BCA-ENV-21DKC` | 0-1–10-58 | Contemporary (21st c.) |
| 3 | English | The Way of the Bodhisattva | Padmakara Translation Group | `BCA-ENV-21PTG` | 0-1–10-58 | 2006 |
| 4 | English | A Guide to the Bodhisattva Way of Life | Vesna A. Wallace & B. Alan Wallace | `BCA-ENV-21W` | 1-1–10-58 | 2009 |
| 5 | Chinese | 入菩薩行論 | 如石法師 (Shi Rushi) | `BCA-ZHV-20RS` ⚑ | 1-1–10-58 | Late 20th c. — verify |
| 6 | Chinese | 入菩薩行論 | 索達吉堪布 (Sodargye) | `BCA-ZHV-21SDJ` ⚑ | 0-1–10-68 | Contemporary (21st c.) — verify |
| 7 | Chinese | 入菩薩行論 | 蔣揚仁欽譯師 (Jamyang Rinchen) | `BCA-ZHV-21JR` ⚑ | 1-1–10-58 | Contemporary (21st c.) — verify |
| 8 | Chinese | 入菩薩行論 | 隆蓮法師 (Longlian) | `BCA-ZHV-20LL` ⚑ | 0-1–10-60 | Mid-20th c. — verify |
| 9 | Chinese | 入菩薩行論廣解 | 隆蓮法師 (Longlian) | `BCA-ZHC-20LL` | 0-1–10-58 | 1950s — Chinese translation of 傑操大師 (Gyaltsab) commentary; cataloged with the `C` marker ⚑ |

⚑ Row 9 is a translation of Gyaltsab's commentary (廣解), not of the root text, so it takes the `C` resource marker even though it lives in `Translations/`. It may alternatively be cross-listed in the commentaries catalog.

---

## Notes

- **Scope**: This catalog covers only the version/translation files in `1-SOURCES/Translations/`. The Sanskrit Devanāgarī root text itself lives in `1-SOURCES/Text/` and is the source all these versions render.
- **Coverage**: The `Coverage` column reproduces the `covers_verses` range from each file's frontmatter; differences (e.g. 10-61, 10-68) reflect the verse count of the edition each translation follows.
- **Translator codes**: Codes for Tibetan and Chinese translators use romanised initials; confirm the preferred romanisation before treating a code as final.
