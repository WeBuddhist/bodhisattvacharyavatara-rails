# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` (Khenpo Ngakwang Kunga Wangchuk, Dzongsar Shedra)
- **Translation audited:** `padmakara-ch3-baseline-lines.md` (clean baseline — wording identical to the published Padmakara 2006 translation, reformatted to one line per verse; no injected errors)

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

## Chapter 3 — verses 3-1–3-33 (clean audit, real Padmakara wording only)

### Extraction note — confirmed cascading shift in the commentary JSON

`extract_commentary.py` splits `BCAC20_NKW_bo_segmented.md` on its transclusion
markers and reports 33 non-empty chapter-3 buckets keyed `3-1`…`3-33` with no
empty passages. However, key-equality is **not** verse-equality here: starting
at the boundary between the root-verse couplet "skyob pa rnams kyi byang chub
dang / rgyal sras sa la'ang yi rang ngo" (= English 3-3) and its neighbours,
the root-verse quotation for a given English verse is transcluded at the
**tail of the preceding bucket**, while the commentary's own "zhes pa ni"
explanation of that same couplet appears at the **head of the next-labeled
bucket** — together with the quotation and explanation for the *following*
English verse. From that point through the end of the chapter, every JSON key
`3-N` (N ≥ 4) actually holds the commentary passage for **English verse
N+1**, confirmed by content (e.g. JSON key `3-31` quotes and glosses "'gro
ba'i mi shes rab rib dag / dpyis 'byin nyi ma chen po yin" and "dam chos 'o ma
bsrubs pa las / mar gyi nying khu phyung ba yin," which is English **3-32**,
not 3-31; JSON key `3-32` matches English **3-33**; JSON key `3-33` matches
the quatrain the source file itself labels `^3-34`, outside this benchmark's
33-verse scope). Every anchor and gloss below was built from the
semantically-correct verse content, re-matched by reading the actual Tibetan
quotations against the English, not from naive JSON-key equality. Root text
labels 3-1 and 3-2 are unshifted (their own bucket keys already match the
correct English verse).

One further scope note: the raw source `en-Padmakara_2006.md` contains one
additional quatrain labeled `^3-34` ("And so, today, within the sight of all
protectors...") before the Chapter 4 heading. Per the task's chapter-3 scope
(33 verses), that block is excluded from both the baseline and this audit.

### Method

Every verse's (corrected) commentary passage was extracted and read; for each
anchor the commentary explicitly glosses, names, counts, or illustrates —
the tri-kāya/bhūmi pair at 3-3, the "all beings" scope words (*thams cad*,
*grangs med*, *dpag tu med pa*, *mkha' khyab*) recurring through the
rejoicing/aspiration verses 3-1–3-22, the doctor/medicine/nurse triad at 3-8,
the boat/raft/bridge and island/lamp/bed/slave enumerations at 3-18–3-19, the
three-tiered precept sequence at 3-23–3-24, the "who benefits" agent
structure at 3-16/3-17/3-29, the blind-man-and-jewel and butter-from-milk
similes at 3-28/3-32 — the real Padmakara English was checked against it
term-by-term. A dedicated second pass then re-scanned specifically for
kāya↔dharma↔mind swaps, wrong named entities, and wrong numbers/scope; none
were found beyond what is listed below. (Chapter 3's root verses name no
specific bodhisattvas, teachers, or sūtras — the entity axis of the second
pass had no anchors to check against in this chapter.)

**Result: 31/33 verses clean with no notes at all, 1/33 carrying a soft
style/scope note, 1/33 carrying a hard ERROR (enumeration order, root-verse
word order itself reversed).**

All of the following checked correct in the real translation and are *not*
flagged: the tri-kāya/bhūmi pairing at 3-3 ("Buddhahood of the protectors" /
"grounds of realization" both kept distinct from "mind"); every *thams
cad/grangs med/dpag tu med pa* ("all/countless/immeasurable") scope word
checked (3-4 "all beings," 3-6 "unnumbered ages," 3-7 "every living being,"
3-21 "boundless multitudes," 3-22 "the limits of the sky," 3-30 "all
maladies" against the commentary's explicit 84,000-affliction count) was
rendered with matching, unbounded scope; the *lus* ("body," not mind)
reference at 3-13 stayed a body; the *sems kyi zla ba* ("moon of mind," not
body) at 3-31 stayed a mind; the boat/raft/bridge order at 3-18 and the
island/lamp/bed/slave order at 3-19 both matched the commentary's sequence;
the three-tiered bodhisattva-precept structure at 3-23–3-24 was correctly
attributed to "the Bodhisattvas," never to śrāvakas; the "who benefits" agent
direction stayed correct at 3-16 (their wishes, not the speaker's), 3-17 (the
aggressors attain enlightenment, not the speaker), and 3-29 (bodhicitta slays
the Lord of Death, not the reverse); the blind-man-finds-a-jewel-in-filth
simile at 3-28 kept its "heap of dust" (not gold); and the butter-churned-
from-milk-of-the-holy-Dharma simile at 3-32 stayed Dharma, not any wish-
granting animal.

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 3-8 | ⚠ ERROR | སྨན་དང་སྨན་པ་ཉིད་དག་དང་། དེ་ཡི་ནད་གཡོག (sman dang sman pa nyid dag dang / de yi nad g.yog) | the root verse itself states the triad in the fixed order medicine (sman) → doctor (sman pa) → nurse (nad g.yog) | "the doctor, nurse, the medicine itself" — doctor → nurse → medicine, a reordering of the root verse's own word sequence | reorder to "the medicine, the doctor, the nurse" (or equivalent) to preserve the root's stated sequence; all three referents are correctly named, so this is an order deviation rather than a renamed referent |
| 3-9 | ◦ style/softening | མུ་གེའི་བསྐལ་པ་བར་མ (mu ge'i bskal pa bar ma) | specifically the **famine**-eon (*mu ge*), one of three named degeneration-kalpas (disease/famine/weapon) the commentary distinguishes | "the aeons marked by scarcity and want" — softens the specific technical term "famine" into a vaguer general phrase | not a renamed referent (still reads as deprivation/want), so kept as a style note; could tighten to "the famine-ages" if a future revision wants the precise term back |

No other ERROR or MISMATCH rows were found. In particular, the 20 verses that
also serve as this benchmark's fault-injection sites (3-2, 3-3, 3-4, 3-6,
3-7, 3-10, 3-13, 3-16, 3-17, 3-18, 3-19, 3-21, 3-22, 3-23, 3-24, 3-28, 3-29,
3-30, 3-31, 3-32) and the five designated negative-control verses (3-1, 3-9,
3-15, 3-20, 3-33) were all confirmed clean here, in the *unmodified* baseline
— confirming those anchors are genuinely sound in the real translation before
any error was deliberately introduced for the separate test file. (Verse 3-9
carries the one softening note above, independent of and unrelated to its
role as a negative control — no wording in it was altered for the benchmark.)

**Result: 31/33 clean, 1 error, 1 softening note.**
