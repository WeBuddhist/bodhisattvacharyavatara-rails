# Why rails — two analogies

A **rail** is a single Markdown file capturing the curated interpretive context for one unit of a classical text — a verse, a section, or a concept — covering morphology, the senses attested across the commentary tradition, translator decisions, and citations.

The motivation behind the methodology can be approached from two complementary angles. The **specialist-pair analogy** explains the cognitive division of labour: *why* you need two distinct layers (source-side and target-side) rather than one model trying to do both jobs at once. The **Wikipedia analogy** explains the information architecture: *how* structuring knowledge once for repeated AI consumption beats fresh inference each time.

Both views land in the same place: a Railroads vault is a pre-compiled knowledge base of one classical text, built so that any number of downstream AI passes can produce reliable, traceable, audience-appropriate output without redoing the philological work.

---

## 1. The specialist-pair analogy — *cognitive division of labour*

The ideal translation team has two specialists who work in partnership:

- A **source-language native speaker who is a domain expert** — fluent in the original language, deeply read in the commentary tradition, able to disambiguate every nuance the text contains.
- A **target-language native speaker who is an audience expert** — fluent in the target language, attuned to the audience the output is for, able to choose the register, vocabulary, and rendering that will land for *that* audience.

Neither can do the job alone. The source-language specialist can read the text but not write it for a Bengali Sunday-school class. The target-language specialist can write for the class but not read a Pāli commentary. The translation is the product of their conversation — the source specialist's expertise filtered through the target specialist's audience-craft.

**The methodology mirrors this pairing exactly:**

| Real-world specialist                                                                        | Vault counterpart                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source-language domain expert** — knows every commentary nuance, every attested sense, every compound analysis | **`2-RAILS/`** — the source specialist made permanent. A pre-built, citation-grounded knowledge base of the commentary tradition, with every claim citing the human source that grounds it.                                       |
| **Target-language audience specialist** — one per (audience × medium × language) combination | **Each track in `3-TRANSFORMATIONS/`** — one target specialist per output stream. A Translation track for English Buddhist scholars; an Adaptation track for children; a Plan track for daily-reading practitioners; and so on. Each one is bound by its own `requirements.md` (style contract) and `termbase.md` (vocabulary contract). |

**Why this matters for AI:** when you hand a raw text and stack of commentaries to a single AI model and ask for output, you're asking that one model to be both specialists at once, in the same prompt, with no preparation. That's why output drifts — the model is doing source-side interpretation under the time pressure of producing fluent target-side prose. Separating the two specialists into two artefacts makes each step doable. The source specialist's work is compiled once, reviewed by a domain specialist, and then any number of target specialists can collaborate with them.

The pairing also explains what doesn't belong where: a source specialist doesn't choose how to render *kusala* for a children's book — that's the audience specialist's decision. A target specialist doesn't decide what sense of *kusala* is active in this verse — that's the source specialist's decision. Confusing the two collapses the methodology into the same all-in-one prompt it's trying to escape.

### Different work, different timescales

The two specialists' jobs are not just different in *kind* — they're different in *shape over time*. This is what makes the methodology scale.

| Aspect                | Source specialist (`2-RAILS/`)                                                                                  | Target specialists (`3-TRANSFORMATIONS/`)                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Scope of work**     | Bounded — the source corpus is finite (a known set of commentaries on a known text).                            | Open-ended — new audiences, new languages, new formats, new cadences can always be commissioned.                                       |
| **Shape over time**   | Built once, then refined incrementally as scholarship improves or new commentaries are ingested.                | Each track evolves continuously: termbases grow as new keywords surface, requirements evolve as the audience is better understood.     |
| **Customisation**     | Minimal. The source specialist's expertise is what the commentary tradition says — not what any output needs.   | Heavy. Each track adapts the source-side expertise into its own audience-specific termbase, register, sentence rhythm, and shape.      |
| **Cost profile**      | High up-front (every verse needs its own rail, every key term its own wiki page), but **paid once**.            | Low per-track on the source-side (rails are reused), bounded by the audience and the calendar (a 200-day plan has 200 day-files).     |
| **Review cycle**      | Domain-specialist sign-off per rail; rails carry `status: complete` and rarely revert.                          | Track-team sign-off per output; outputs cycle through `draft → partial → complete` per QA pass.                                        |

The asymmetry is the point. The expensive interpretive work — reading every commentary, disambiguating every term, recording every divergence — happens **once**, in `2-RAILS/`, and is then **amortised over every output ever produced from the vault**. A new translation into a new language, a new children's adaptation, a new daily-reading plan: each of these is a much cheaper marginal investment because the source specialist's work is already done.

---

## 2. The Wikipedia analogy — *information architecture*

**A Railroads vault is the Wikipedia of one classical text, built for AI consumption first and human reading second.**

| Category                   | Wikipedia                                                  | Rails                                                                                                                                                                                                                              | AI benefit                                                                                             |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Information density**    | Objective, encyclopedic data stripped of narrative filler. | Each rail distils one unit's commentary positions — morphology, attested senses, translator decisions — without devotional or narrative framing.                                                                                   | Transformation prompts stay within budget; the model isn't asked to wade through irrelevant material.  |
| **Structure & formatting** | Infoboxes, clear headers, uniform layouts.                 | One schema for every rail: frontmatter, the disambiguation stack (Source Text → Traditional Interpretation → Morphological → Syntactic → Semantic Gloss → Translation Dynamics), and Obsidian block IDs.                           | AI pipelines parse and ingest automatically — no per-file logic.                                       |
| **Context-window fit**     | Topic summaries fit easily in LLM memory.                  | A unit's complete interpretive context fits in a few kilobytes; the raw commentaries span thousands of pages across multiple languages.                                                                                            | One unit loads in a single prompt; large transformations stay feasible.                                |
| **Fact verification**      | Every fact links to a primary source footnote.             | Every claim cites a specific block ID in `1-SOURCES/` (e.g. `...#^1-1`). The chain `1-SOURCES → 2-RAILS → 3-TRANSFORMATIONS` is strict and one-way.                                                                                | Every claim in a generated output traces back to a specific commentary passage; supports RAG natively. |
| **Writing tone**           | Neutral (NPOV).                                            | Descriptive, not prescriptive. Rails record what each commentator attests; divergence is flagged, never collapsed into editorial preference.                                                                                       | Surfaces ambiguity instead of flattening competing traditions.                                         |
| **Legal compliance**       | Creative Commons.                                          | Public repo; classical sources long out of copyright; modern works cited and quoted within fair use.                                                                                                                               | Safe for downstream tools to build on without licensing friction.                                      |
| **Data cleanliness**       | Editor communities purge spam, vandalism, typos.           | `draft → partial → complete` lifecycle; only `complete` rails — reviewed claim-by-claim by a domain specialist — feed downstream transformations. The LLM never marks its own output complete.                                     | `complete` rails are trustable by construction; no pre-cleaning needed.                                |
| **Cross-lingual links**    | Matching concepts mapped across 300+ languages.            | Each unit anchors parallel files in Pāli, Sanskrit, Tibetan, Chinese, and modern translations through shared block IDs. `Local-Wiki/` assigns language-neutral sense IDs; `Bilingual-Glossaries/` maps term renderings per pair.   | The same anchored structure works for every target language.                                           |

---

## How the two analogies fit together

The specialist-pair analogy answers **why** the vault has two distinct interpretive layers (`2-RAILS/` and `3-TRANSFORMATIONS/`) rather than collapsing them into one prompt: because the two layers represent two different kinds of expertise that have to be done by two different specialists, and a single AI prompt can't carry both at once.

The Wikipedia analogy answers **how** the source specialist's expertise gets compiled into a form that any downstream pass can consume reliably: by being dense, structured, citation-grounded, cleanly versioned, and language-neutral at the anchor level.

The pair-and-Wikipedia framings together explain the whole methodology: separate the expertise into two specialists, then compile the source-side specialist into a Wikipedia-shaped knowledge base, so that any target-side specialist (and any number of them, over any number of sessions) can do their job cleanly against it.
