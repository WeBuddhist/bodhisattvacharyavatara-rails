# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` (Khenpo Ngakwang Kunga Wangchuk, Dzongsar Shedra)
- **Translation audited:** `padmakara-ch4-baseline-lines.md` (clean baseline — wording identical to the published Padmakara 2006 translation, reformatted to one line per verse; no injected errors)

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1, verses I-1 and 1-1–1-36 (BCAC20_NKW, see companion ch1 report) |
| Chapter 2, verses 2-1–2-65 (BCAC20_NKW, clean baseline) |
| Chapter 3, verses 3-1–3-33 (BCAC20_NKW, clean baseline) |
| Chapter 4, verses 4-1–4-48 (BCAC20_NKW, clean baseline) |

## Chapter 4 — verses 4-1–4-48 (clean audit, real Padmakara wording only)

### Extraction note — verse count and a single empty-bucket artifact (not a cascading shift)

`extract_commentary.py` splits `BCAC20_NKW_bo_segmented.md` on its transclusion
markers and reports **48** chapter-4 buckets keyed `4-1`…`4-48`. The raw source
`en-Padmakara_2006.md` was independently checked: the "## 4. Carefulness ^4-0"
heading runs through verse `^4-48`, immediately followed by "## 5. Vigilant
Introspection ^5-0" — also 48 English verses, with no extra trailing quatrain
this time (unlike chapter 3's stray `^3-34`). Bucket keys and English verse
numbers line up 1:1 for the whole chapter — **no cascading shift** of the kind
found in chapter 3.

One isolated **empty-bucket** artifact was found and resolved per the skill's
own Step 1 instructions: JSON key `4-26` holds only the quoted root verse
("shin tu rnyed dka' phan pa'i sa / ji zhig ltar stes rnyed gyur nas / bdag
nyid shes dang ldan bzhin du / phyir yang dmyal ba der khrid na," = English
4-26) with **no** "zhes pa ni…" prose explanation. That explanation was
absorbed into the *next* bucket: `4-27` opens with a two-line partial quote of
verse 4-27's own root text, then gives the *4-26* explanation (the hard-won,
precious human rebirth, obtained by luck, squandered back into hell through
laziness — illustrated with the "bewitched by a mantra" simile), and only
afterward quotes and glosses 4-27's own remaining two lines ("I do not know
what dulls my wits… what is inside me?" → answer: the afflictions). Both
verses' content was recovered and checked against their correct semantic
match, not against naive JSON-key equality; neither 4-26 nor 4-27 was used as
an anchor verse for any injected error or negative control in this
benchmark, so the artifact does not affect scoring, but it is recorded here
per the skill's instructions since a full-chapter audit passes through it.

### Method

Every verse's commentary passage was read in full (with the 4-26/4-27 repair
above) and, for each anchor the commentary explicitly glosses, names, counts,
or illustrates, the real Padmakara English was checked term-by-term. Anchors
checked include: the *lus* vs *sems* (body vs mind) pairs at 4-16 ("body…
briefly lent"), 4-25 (body burns / mind is tormented, kept distinct), and
4-46 (afflictions driven from the *mind*); the named "heirs" of the Buddhas
at 4-3 (Mañjuśrī, Maitreya, Avalokiteśvara — not śrāvakas) and the Omniscient
Buddha's exclusive domain at 4-7 (explicitly *not* the Bodhisattvas' domain);
the *thams cad / grangs med* ("all/countless") scope words at 4-4, 4-13,
4-17, 4-19, and 4-30; the fixed illness→bondage→laceration sequence at 4-14
and the fisherman→butcher→farmer sequence at 4-40; the agent/patient
direction of "who harms whom" at 4-29, 4-31, and 4-33; and the turtle/yoke/
ocean simile's target (human birth, not generic bliss) at 4-20 and the
illusion simile's target (the afflictions, not the body) at 4-47. A dedicated
second pass then re-scanned specifically for kāya↔dharma↔mind swaps, wrong
named entities, and wrong numbers/scope; none were found beyond what is
listed below.

**Result: 45/48 verses clean with no notes at all, 3/48 carrying a soft
style/softening note, 0/48 carrying a hard ERROR.**

All of the following checked correct in the real translation and are *not*
flagged: the *lus*/*sems* distinction stayed correct at 4-16 ("my body," not
mind), 4-25 ("my body burns" / "my mind… will also be tormented," both kept
distinct), and 4-46 ("driven from my mind," not body); the named heirs at
4-3 stayed "their heirs" (not misnamed as śrāvakas) and the Omniscient at 4-7
stayed correctly attributed (not the Bodhisattvas); every *thams cad/grangs
med* scope word checked (4-4 "every being," 4-13 "Unnumbered Buddhas," 4-17
"virtues none," 4-19 "a hundred million ages," 4-30 "all the gods and
demigods") kept its full, unbounded scope; the illness→bondage→laceration
order at 4-14 and the fisherman→butcher→farmer order at 4-40 both matched
the commentary's sequence; the agent direction stayed correct at 4-29
(afflictions harm "me," not the reverse), 4-31 (the affliction-fiend flings
"me" down, not the reverse), and 4-33 (the speaker serves the afflictions,
they do not serve the speaker); the turtle/yoke/ocean simile at 4-20 kept its
target as "this human birth," not generic bliss; and the illusion ("simple
mirages") simile at 4-47 kept its target as the defilements, not the body.

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|---|
| 4-6 | ◦ style/softening | 'གྲོ་བ་ཐམས་ཅད (‘gro ba thams cad) | ALL (thams cad) wandering beings are summoned to the bliss of unsurpassed enlightenment | "Wandering beings to the highest bliss" — drops the explicit "all," left as a bare plural | not a renamed referent (still reads as beings in general), kept as a style note only |
| 4-12 | ◦ style/softening | གུས་པས (gus pas) | with **respect/reverence** (gus pas) I will accomplish [my promise] | "I will act attentively" — softens "with reverence/respect" to the vaguer "attentively" | not a renamed referent, kept as a style note only |
| 4-17 | ◦ style/softening | སྡིག་པ་འབའ་ཞིག (sdig pa 'ba' zhig) | ONLY/EXCLUSIVELY ('ba' zhig) misdeeds — reinforced by the commentary's own gloss that the opportunity for virtue is, in every way, completely absent | "My evils will be many" — "many" loosens the exclusivity of "only ever" misdeeds implied by 'ba' zhig | the paired clause "virtues none" (dge ba med) is itself exact; only the "only/exclusively" nuance on the evils-clause is softened, kept as a style note only |

No ERROR rows were found anywhere in the chapter. In particular, all 20
verses that also serve as this benchmark's fault-injection sites (4-3, 4-4,
4-6, 4-7, 4-9, 4-13, 4-14, 4-16, 4-17, 4-18, 4-19, 4-20, 4-25, 4-29, 4-30,
4-31, 4-33, 4-40, 4-46, 4-47) and the five designated negative-control verses
(4-2, 4-11, 4-24, 4-36, 4-45) were all confirmed clean here, in the
*unmodified* baseline — confirming those anchors are genuinely sound in the
real translation before any error was deliberately introduced for the
separate test file. (Verses 4-6 and 4-17 each carry one of the softening
notes above, independent of and unrelated to their role as fault-injection
sites — the softening was already present in the real 2006 wording before
this benchmark's edit was applied elsewhere in the same line; 4-12 is
unrelated to any benchmark item.)

**Result: 45/48 clean, 0 errors, 3 softening notes.**
