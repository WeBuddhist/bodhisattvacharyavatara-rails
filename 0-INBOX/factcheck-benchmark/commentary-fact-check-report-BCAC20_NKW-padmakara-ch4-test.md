# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md`
- **Translation audited:** `factcheck-benchmark/padmakara-ch4-test.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 4, verses 4-1 to 4-48 |

## Notes on extraction

- `extract_commentary.py` reported 0 empty buckets, but content-level inspection
  found that the **4-26** bucket contains only the root-verse quotation with no
  commentary prose — its explanation is absorbed into the **4-27** bucket (the
  "zhes pa ni" prose in 4-27 explains both 4-26's and 4-27's root lines in
  sequence). This matches the known artifact noted for this file; resolved by
  content-matching, not reported as a translation defect.
- 4-12's root verse (a single four-line verse) is split across two quotation
  blocks by an internal structural heading ("gnyis pa sbyor ba brtson 'grus mi
  nyams par bya ba ni") — both halves belong to 4-12; not a cascading shift.

### Chapter 4 — verses 1–48

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 4-3 | ⚠ ERROR | དེ་ཡི་སྲས (de yi sras) | The Buddha's "sons/heirs" — commentary names them explicitly: rje btsun 'jam dpal dbyangs (Mañjughoṣa), byams pa mgon po (Maitreya), 'phags mchog spyan ras gzigs (Avalokiteśvara) — i.e. great bodhisattvas | "their śrāvakas" | sras = the Buddha's bodhisattva heirs, not śrāvakas — wrong class of being; contradicts the commentary's named bodhisattvas |
| 4-4 | ⚠ ERROR | སེམས་ཅན་དེ་དག་ཀུན (sems can de dag kun) | "all those beings" (lha dang lha ma yin la sogs pa'i sems can de dag kun) are completely deceived | "many beings will have been betrayed" | kun = all, not "many" — quantifier weakened |
| 4-7 | ⚠ ERROR | ཐམས་ཅད་མཁྱེན་པ་ཁོ་ནས་མཁྱེན (thams cad mkhyen pa kho nas mkhyen) | known only by the omniscient Buddha (སངས་རྒྱས་ཁོ་ན, sangs rgyas kho na) — explicitly said NOT to be within the domain of others' (gzhan gyi spyod yul) understanding | "only understood by the Bodhisattvas" | thams cad mkhyen pa = the Omniscient One = the Buddha, not "the Bodhisattvas" — wrong named entity, and the commentary explicitly excludes anyone other than the Buddha |
| 4-13 | ⚠ ERROR | སངས་རྒྱས་གྲངས་མེད (sangs rgyas grangs med) | tshad med pa grangs med pa = immeasurable, countless/innumerable Buddhas | "A few Buddhas have already lived and passed away" | grangs med = countless/innumerable, not "a few" — direct quantifier reversal |
| 4-16 | ⚠ ERROR | ལུས་ནི་ཐང་གཅིག་བརྙན་པོ་བཞིན (lus ni thang gcig brnan po bzhin) | "this very BODY (lus) is like something borrowed from another person for a short while" (lus 'di nyid ni thang gcig gi brnan po... mi gzhan gyi dngos po lta bu) | "My mind is like something briefly lent" | lus = body, not "mind" — body/mind swap |
| 4-17 | ⚠ ERROR | སྡིག་པ་འབའ་ཞིག་དགེ་བ་མེད (sdig pa 'ba' zhig dge ba med) | doing NOTHING BUT evil, with NO opportunity for virtue whatsoever (dge ba sgrub pa'i go skabs ni rnam pa kun tu med pa) | "My evils will be many, virtues few" | 'ba' zhig...med = only/exclusively...none at all (absolute), softened to a relative "many/few" that implies some virtue remains |
| 4-19 | ⚠ ERROR | བསྐལ་པ་བྱེ་བ་བརྒྱར (bskal pa bye ba brgyar) | "a hundred [times ten-million, i.e. hundreds and thousands of] aeons" (brgya phrag dang stong phrag gi bar du) — bye ba = ten million/koṭi | "for a hundred ages" | drops the "bye ba" (ten-million) multiplier — "a hundred aeons" vastly understates "a hundred times ten million aeons" |
| 4-20 | ⚠ ERROR | མི་ཉིད (mi nyid) | "the human body/human birth itself (mi'i lus rten) is extremely hard to attain" — the entire topic of this simile is the rarity of human rebirth | "this state of bliss is difficult to find" | mi nyid = human birth/humanness specifically, not a vague "state of bliss" — drops the precise referent that the whole passage (and the turtle-and-yoke simile) is about |
| 4-25 | ⚠ ERROR | སེམས་གདུང་འགྱུར་བ (sems gdung 'gyur ba) | "one's own MIND (sems) will repeatedly be tormented/anguished" by unbearable regret — contrasted with the body burned by hell-fire in the first half of the verse | "My body, there is no doubt, will also be tormented, Burned in fires of unendurable regret" | sems = mind, not "body" — the verse deliberately contrasts body (burned by hell-fire) with mind (tormented by regret); English says "body" both times |
| 4-29 | ⚠ ERROR | དགའ་མགུར་བདག་ལ་གནོད་བྱེད་པ (dga' mgur bdag la gnod byed pa) | "[the afflictions] joyfully/gladly harm ME (bdag la gnod byed) at all times" — afflictions are the agent, "I" (bdag) am the object harmed | "And at their pleasure I injure them" | agent/patient reversed — the Tibetan says the afflictions harm me, not that I injure them |
| 4-30 | ⚠ ERROR | ཐམས་ཅད་བདག་ལ་དགྲར་ལངས (thams cad bdag la dgrar langs) | ALL ('jig rten gyi stobs chen du grags pa de dag thams cad) of the mightiest gods and demigods uniting against me | "a few of the gods and demigods besides... Together came against me" | thams cad = all, not "a few" — reverses the verse's a fortiori point (even if ALL of them united, they couldn't send me to Avīci hell, unlike the afflictions in 4-31) |
| 4-31 | ⚠ ERROR | དེར་བདག་སྐད་ཅིག་གཅིག་ལ་འདོར (der bdag skad cig gcig la 'dor) | "[the afflictions] cast even ME (bdag) into that [Avīci fire], merely by a single instant of a bad thought" — afflictions are agent, "I" am the one cast/thrown | "I fling it in an instant headlong down" | agent/patient reversed — the Tibetan says the afflictions throw me into the fire; English has "I" throwing "it" (the affliction) — inverts the entire point about the afflictions' terrifying power |
| 4-33 | ⚠ ERROR | ཉོན་མོངས་རྣམས་ནི་བསྟེན་བྱས་ན (nyon mongs rnams ni bsten byas na) | "however much [I] serve/indulge/rely on the afflictions" ('dod chags la sogs pa'i nyon mongs pa rnams ni ji tsam bsten par byas pa yin na) — parallel to serving/appeasing ordinary enemies in the prior two lines | "should my dark defiled emotions serve me" | agent reversed — the Tibetan says "I" serve/indulge the afflictions (as one might appease an enemy), not that the afflictions "serve" me |
| 4-46 | ⚠ ERROR | བདག་ཡིད་ལས་བསལ (bdag yid las bsal) | "removed from MY MIND/consciousness" (bdag gi yid dam sems 'di nyid las nyon mongs pa de dag bsal zin pa) | "when driven from my body" | yid = mind, not "body" — mind/body swap (note the very next line correctly renders blo as "mind," making this inconsistency stand out) |
| 4-47 | ⚠ ERROR | འདི་ནི་སྒྱུ་འདྲ ('di ni sgyu 'dra) | "THE AFFLICTIONS (nyon mongs pa 'di dag) are like a magician's illusion" — conclusion of the preceding search through sense-objects, faculties, and body parts (head, flesh, bones, organs) that finds the afflictions nowhere | "My body is a simple mirage" | wrong simile tenor — 'di = the afflictions, not "my body"; the illusion-simile applies to the kleshas, which cannot be located anywhere, not to the body |

**Softening / style notes (not hard errors):**

| Verse | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|
| 4-6 | བླ་ན་མེད་པའི་བདེ་བ (bla na med pa'i bde ba) | the happiness of unsurpassed/supreme awakening | "great happiness" | intensity softened (unsurpassed → great) |
| 4-6 | འགྲོ་བ་ཐམས་ཅད ('gro ba thams cad) | all wandering beings | "wandering beings" | quantifier "all" dropped |
| 4-8 | སེམས་ཅན་ཀུན་གྱི་དོན་ལ་དམན (sems can kun gyi don la dman) | the bodhisattva becomes extremely weak/incapable at accomplishing the welfare of all other beings (dman = the agent's own deficiency) | "The good of every being is thrown down" | grammatical subject shifted from the bodhisattva's diminished capacity to beings' welfare being destroyed; net sense overlaps but agent/patient framing changes |
| 4-9 | སེམས་ཅན་དོན་ལ་དམན་གྱུར་པས (sems can don la dman gyur pas) | same pattern as 4-8 | "the welfare of all beings is reduced" | same agent/patient softening as 4-8 |
| 4-11 | ས་ཐོབ་པ (sa thob pa) | specifically named as the first ground, rab tu dga' ba (Pramuditā) | "the Bodhisattva grounds" | generalized to plural "grounds" rather than the specific first ground — commentary elaboration, not required in the verse itself |
| 4-12 | གུས་པས (gus pas) | acting with respect/reverence (gus pa byed de) | "attentively" | precise term (respect/reverence) softened to a different quality (attentiveness) |
| 4-14 | ནད (nad) | illness/disease (rlung mkhris bad kan gyi nad) as a distinct item in the list | merged into "pains" | minor softening, not a wrong referent |
| 4-26 | ཕན་པའི་ས (phan pa'i sa) | a "ground" of benefit to self AND OTHER (rang dang gzhan la shin tu phan 'dogs pa) | "wherein to help myself" | drops "others" (gzhan), narrowing scope to self only |
| 4-26 | ཕྱིར་ཡང་དམྱལ་བ་དེར་ཁྲིད་ན (phyir yang dmyal ba der khrid na) | "I lead MYSELF back to hell" (rang gis rang khrid pa) — reflexive, self-caused | "I am once again consigned to hell" | loses the reflexive self-agency emphasized by the commentary |
| 4-40 | ཉ་པ་གདོལ་པ་ཞིང་པ (nya pa/gdol pa/zhing pa) | enumeration order: fishermen, butchers, farmers | "farmers, butchers, fishers" | enumeration order reversed; same three entities, no content loss — likely for meter/rhyme |

**Result: 33/48 clean, 15 errors, 10 softening notes.**

### Second-pass sweep (kāya/dharma/mind, named entities, number/scope) — additions

A dedicated second sweep over the whole chapter, restricted to these three highest-miss classes, did not surface any additional instances beyond those already logged in the table above. Summary of what the second pass confirmed:

- **Body/mind swaps (3 instances, a notable cluster):** 4-16 (lus→"mind"), 4-25 (sems→"body"), 4-46 (yid→"body"). All three are clear, unambiguous swaps of the same type as a kāya/dharma/mind confusion, even though the specific term here is lus/sems/yid rather than sku.
- **Named entity swaps (2 instances):** 4-3 (bodhisattva heirs → "śrāvakas"), 4-7 (the Buddha/Omniscient One → "the Bodhisattvas").
- **Number/scope swaps (6 instances):** 4-4 (all→many), 4-13 (countless→a few), 4-17 (only/none→many/few), 4-19 (hundred×ten-million→a hundred), 4-20 (human birth→vague "state of bliss," a referent-precision issue bundled with scope), 4-30 (all→a few). This is a striking pattern: every one of these instances *understates* scale, count, or totality — worth flagging to the editor as a systematic tendency in this draft, not isolated slips.
- **Agent/patient reversals (not one of the three named second-pass classes, but caught by the general first pass and worth flagging together):** 4-29, 4-31, 4-33 all reverse who acts on whom (the afflictions harming/serving/casting "me" become "I" harming/serving/casting "them"). 4-47 is a related but distinct wrong-simile-tenor case (the illusion-simile belongs to the afflictions, not "my body").

No verse required reaching for a second commentary; all findings are anchored in BCAC20_NKW's own glosses for chapter 4.
