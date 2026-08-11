# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md`
- **Translation audited:** `factcheck-benchmark/padmakara-ch3-test.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 3, verses 3-1 to 3-33 (full chapter) |

## Note on commentary bucket extraction — cascading shift

The chapter-3 extraction shows a confirmed cascading shift starting at the
verse-2/verse-3 boundary: bucket `3-2` ends with an orphaned root-verse couplet
("skyob pa rnams kyi byang chub dang / rgyal sras sa la'ang yi rang ngo") that
plainly does not belong to bucket 3-2's own commentary; its gloss ("byang chub
sku gsum ye shes yon tan... rgyal sras kyi sa dang po gnyis pa gsum pa nas sa
bcu'i...") is found at the *head* of bucket `3-3`, before bucket 3-3's own root
quatrain and its own commentary. This same +1 pattern (bucket label N holds the
root text whose own explanation reads naturally, but content that is one verse
"ahead" of the label) recurs through most of the chapter's bucket boundaries.
This was resolved throughout by content-matching each English verse against the
Tibetan passage that actually explains it (verified via the commentary's own
explicit glosses), not by naively using the bucket number matching the verse
label. No English verse was skipped or double-checked because of this.

**Separately, a structural finding, not a wording error:** the content behind
the English's own `^3-33` tag ("Living beings! Wayfarers upon life's paths...")
matches the Tibetan "guest-wanderer" simile (`'gro ba'i mgron po srid pa'i lam
rgyu zhing...`). The chapter's actual closing benediction verse — "Today, in
the presence of all the Protectors ... I have invited beings as guests to
buddhahood and to happiness in between; may the gods and asuras rejoice"
(`bdag gis de ring skyob pa thams cad kyi spyan sngar...lha dang lha min la
sogs dgar bar gyis`) — appears in the commentary immediately after that, but
has **no corresponding English verse anywhere in this file**. Different
editions of the root text split verses 3.3/3.4 differently and end up with
32-33-34 total verses for the chapter depending on convention, so this may
reflect an edition/numbering choice rather than an outright omission — but as
delivered, this file's chapter 3 does not contain a translation of the closing
"invite beings as guests, rejoice gods and asuras" verse. Flagging for
specialist review rather than logging as a term-level error, since it's a
structural/completeness question, not a mistranslation of an existing line.

### Chapter 3 — verses 3-1–3-33

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 3-2 | ⚠ ERROR | བྱང་ཆུབ (byang chub) | "byang chub thob pa'i rgyu" — the cause of attaining śrāvaka/pratyekabuddha **enlightenment/liberation** (confirmed by the verse's own next line: liberation from saṃsāra's suffering) | "cause of gaining **a better rebirth**" | byang chub = enlightenment/awakening, not rebirth; this turns a supramundane liberation into a mundane samsaric upgrade |
| 3-3 | ⚠ ERROR | བྱང་ཆུབ (byang chub, in "skyob pa rnams kyi byang chub") | glossed explicitly as "byang chub **sku gsum** ye shes yon tan dang bcas pa" — enlightenment endowed with the **three kāyas**, wisdom, and qualities | "wisdom-**mind** of the protectors" | byang chub = enlightenment (comprising three kāyas + wisdom), not merely "mind" — drops the kāya dimension the commentary explicitly names |
| 3-4 | ⚠ ERROR | སེམས་ཅན་ཐམས་ཅད (sems can thams cad) | "sems can thams cad gnas skabs dang mthar thug kun tu phan pa dang bder mdzad pa'i" — brings benefit/happiness to **ALL** beings, doubly emphasized ("kun tu") | "seeks to place **some** beings in the state of bliss" | thams cad = all, not some; scope reduced from universal to partial |
| 3-6 | ⚠ ERROR | བསྐལ་པ་གྲངས་མེད (bskal pa grangs med) | "bskal pa bskal chen grangs med pa du ma" — **countless**, many great eons | "stay among us for **a hundred** ages" | grangs med = countless/innumerable, not a specific finite number |
| 3-7 | ⚠ ERROR | སེམས་ཅན་ཐམས་ཅད (sems can thams cad) | "mkha' khyab kyi sems can thams cad kyi... sdug bsngal" — the suffering of **ALL** beings pervading space | "may all the pain of **many** a living being" | thams cad = all, not many; scope reduced |
| 3-10 | ⚠ ERROR | མི་ཟད་གཏེར (mi zad gter) | "rgyu nor longs spyod rnam pa kun tu **mi zad pa'i** gter" — an **inexhaustible** (never-depleting) treasure | "a treasure **sometimes** plentiful" | mi zad = inexhaustible/permanent, not intermittent — "sometimes" nearly inverts the meaning |
| 3-13 | ⚠ ERROR | ལུས (lus) | "rang gi **lus** 'di nyid ni ci bde bar longs spyad par bya ba'i ched du... byin zin pa" — I have given my **body** for them to use as they please | "This **mind** I have now resigned to serve the pleasure of all living beings" | lus = body, not mind — a body/mind referent swap (contrast verse 3-14 in the same file, which correctly says "my body") |
| 3-16 | ⚠ ERROR | དེ་དག་གི་དོན་ཀུན (de dag gi don kun) | "de nyid dus rtag tu sems can de dag gi yid la bsam pa'i don kun 'grub pa'i rgyur" — may it be the cause of fulfilling **their** (the beings who feel anger/faith) aims | "may these states always be the cause whereby **my** good and wishes are fulfilled" | the beneficiary is the other being, not "me" — wrong agent/grammatical role |
| 3-17 | ⚠ ERROR | ཐམས་ཅད་བྱང་ཆུབ་སྐལ་ལྡན་གྱུར (thams cad byang chub skal ldan gyur) | "de thams cad bla na med pa rdzogs pa'i byang chub kyi skal ba dang ldan par gyur cig" — may **they** (all beings who wrong/harm me) attain the fortune of enlightenment | "may **I** attain the fortune of enlightenment!" | the wish is for the wrongdoers' enlightenment, not the speaker's — wrong agent/subject |
| 3-22 | ⚠ ERROR | ནམ་མཁའི་མཐས་གཏུགས་པའི (nam mkha'i mthas gtugs pa'i) | "nam mkhas gar khyab kyi sems can gyi khams" — beings pervading the **entirety of space**, unbounded | "for everything that lives, **as far as the eye can see**" | reduces an unbounded, cosmic scope to a finite visual horizon |
| 3-23 | ⚠ ERROR | བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ (byang chub sems dpa'i bslab pa) | commentary repeatedly glosses this as the **bodhisattva's** training (six pāramitās, four means of gathering, three types of discipline) — no mention of śrāvakas anywhere | "in the precepts of the **Śrāvakas** step-by-step abode and trained" | bodhisattva ≠ śrāvaka — wrong vehicle/named category, and this verse is specifically about the Buddhas' past bodhisattva training, central to the chapter's theme |
| 3-28 | ⚠ ERROR | ཕྱག་དར་ཕུང་པོ (phyag dar phung po) | "lam po che'i nyal nyul mi gtsang ba rug rug byas te spungs pa" — a heap of **filth/rubbish** swept from the roadway | "a precious gem inside a heap of **gold**" | phyag dar phung po = rubbish heap, not gold; inverts the simile's logic (contrast of worthless vs. precious becomes value-next-to-value) |
| 3-29 | ⚠ ERROR | འཇོམས་བྱེད་པའི (...bdud rtsi 'joms byed pa'i) | "'gro ba sems can gzhan rnams kyi 'chi bdag gi bdud gang yin pa de **'joms par byed pa'i**" — the nectar that **destroys/conquers** the Lord of Death | "the supreme draft of immortality that **is slain by** the Lord of Death" | agent/action reversed — the nectar (bodhicitta) defeats Death; the English has Death defeating the nectar |
| 3-30 | ⚠ ERROR | རབ་ཞི (rab zhi) / commentary's ཐམས་ཅད | "nyon mongs pa brgyad khri bzhi stong gi nad **thams cad** 'joms pa'am spong bar byed pa'i" — completely pacifies **all** 84,000 kinds of affliction/sickness | "perfectly allays **most** maladies" | thams cad = all, not most; scope reduced |
| 3-31 | ⚠ ERROR | སེམས་ཀྱི་ཟླ་བ (sems kyi zla ba) | "sems kyi rgyud na yod pa'i nyon mongs pa'i tsha gdung thams cad sel bar byed nus pa... **sems kyi** dkyil nas shar ba'i zla ba" — the moon that rises from within the **mind**, triple-confirmed | "the rising moon of the **enlightened body**" | sems (mind) ≠ kāya (body) — a mind→body swap, the doctrinal-category error class the second pass specifically targets |
| 3-32 | ⚠ ERROR | དམ་ཆོས་འོ་མ (dam chos 'o ma) | "dam pa'i chos te rdzogs pa'i sangs rgyas kyi gsung rab sde snod... thos bsam sgom gsum gyi shes rab kyis bsrubs pa" — butter churned from the milk of the holy **Dharma** (the Buddha's teachings) | "churned from the **milk of the wish-granting cow**" | replaces "the Dharma" with an unrelated cow-image (borrowed from verse 3-20's simile); the churning agent/source is wrong |

**Softening / non-error notes** (dropped supplementary detail, not a referent
swap — logged for the editor's awareness, not counted as errors):

- 3-11: "dus gsum" (three times — past/present/future) rendered as "gained and
  to be gained," which reads as past+future and under-states the present-tense
  virtue the commentary names separately (sgrub bzhin pa). Minor.
- 3-11: "sems can **kun**" (all beings) compressed to "the benefit of beings"
  without "all" — minor, implicit universality is a common compression.
- 3-21: "sems can **dpag tu med pa**" (commentary: "grangs med pa dpag tu med
  pa," countless *and* immeasurable) rendered as "many multitudes" — softer
  than "countless," but still conveys vastness, unlike the flat "some/many"
  downgrades logged as errors elsewhere. Borderline; logged as a note.

**Result: 17/33 clean, 16 errors, 3 softening notes, 1 structural finding (see
cascading-shift note above) flagged for specialist review.**
