# bodhisattvacaryavatara-rails

བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། · *Bodhisattvacaryāvatāra* · Śāntideva

A 🛤️ **Railroads** repo for Śāntideva's *Bodhisattvacaryāvatāra* — gathering the classical commentary tradition and compiling it into machine-readable context that lets any AI model do reliable, tradition-grounded work on this text.

---

## What this repo contains

This is one repo per text. Everything here is about the *Bodhisattvacaryāvatāra* and nothing else.

The repo holds two layers of content:

**Human reference material** (`1-SOURCES/`) — editions, translations, commentaries, sub-commentaries, secondary literature, dictionaries. This is received material, formatted for navigation but not interpreted.

**The Rails** (`2-RAILS/`) — compact, structured interpretive packages compiled from the sources above. One package per verse, plus per-chapter summaries, a local concept wiki, and bilingual glossaries. Every claim in the rails cites the human source that grounds it.

Once the rails are laid for a verse, any AI model can run any transformation on that verse — translation, adaptation, summary, lesson — without redoing the philological work each time.

---

## Why "rails"

The standard way to use AI on a classical text is to give it the source plus some commentary and ask it to translate. This fails because the model has to do interpretive work (compound analysis, sense disambiguation, syntactic parsing) at the same time as producing fluent output, and nothing it learns persists between sessions.

🛤️ Railroads inverts this: lay the interpretive track once, in a form humans can review and machines can read, then run transformations on top of it. The model generating a translation does stylistic work only — it does not decide what *dharmakāya* means in this verse, how the syntax goes, or how Prajñākaramati reads the compound. All of that is already in the package, already cited.

The authority behind every claim in the rails is the human commentary tradition. The LLM is the extraction and formatting agent; it adds no interpretation of its own.

---

## Folder structure

```
0-INBOX/            drafts and scratch
1-SOURCES/          human-produced material — read-only ground truth
   Root Text/
   Commentaries/
   Translations/
   References/      secondary literature, dictionaries
2-RAILS/            structured interpretive context (the rails)
   Verses/
   Sections/
   Local-Wiki/
   Glossaries/
3-TRANSFORMATIONS/  outputs generated from the rails
4-SYSTEM/           guidelines (CLAUDE.md and contributor docs)
```

For the full schema — frontmatter, block-ID format, package layout, citation chain, naming rules — see [`4-SYSTEM/CLAUDE.md`](4-SYSTEM/CLAUDE.md).

---

## What the rails are for

The rails are a foundation that many downstream projects can run on. The first projects this repo is being built to support:

**Reviewing and improving existing English translations.** With every verse's interpretive decisions made explicit and cited, an existing translation can be checked against the commentary tradition systematically — flagging where the translator chose a sense the commentaries rule out, where a compound was read differently, where a divergence was flattened.

**Generating translations and adaptations in other languages.** Once the rails for a verse are complete, the same package can drive a scholarly Swahili translation, a literary Chinese rendering, or a spoken-Tibetan adaptation — all grounded in the same commentary-backed interpretive choices, without re-doing the philology in each language.

**Shantideva in 365 days — a daily reading plan in our mobile app.** Five minutes of content per day, generated from the rails:

- a daily notification
- a reading guide for the day's verse(s)
- *reading for meaning* in the user's language
- commentaries from the user's tradition
- a shareable image

Each piece of content is generated from the same underlying verse package, adapted to format and audience.

Other transformations the rails are designed to support: thematic summaries, study courses, sermon prompts, classroom materials, contemplative reading guides.

---

## How to contribute

If you are a domain specialist (philologist, scholar, traditional teacher) reviewing or correcting AI-generated content: focus on `2-RAILS/`. Set `status: complete` only on packages whose claims you can stand behind. Flag divergences with ⚑ rather than smoothing them.

If you are adding a new source to `1-SOURCES/`: follow the naming and frontmatter rules in [`4-SYSTEM/CLAUDE.md`](4-SYSTEM/CLAUDE.md). Do not add interpretation to source files — interpretive notes belong in `2-RAILS/`.

If you are designing AI workflows or transformations: read `4-SYSTEM/CLAUDE.md` end to end, then look at completed verse packages in `2-RAILS/Verses/` for the shape of context the transformations consume.

---

## Status

Early stage. Sources are being ingested; the first verse packages are in draft. The methodology is settling in this repo first and will be generalised to other texts once it is proven here.
