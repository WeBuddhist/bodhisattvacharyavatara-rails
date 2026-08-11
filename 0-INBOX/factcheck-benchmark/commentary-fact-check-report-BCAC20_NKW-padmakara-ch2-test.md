# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md`
- **Translation audited:** `factcheck-benchmark/padmakara-ch2-test.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 2, verses 2-1 to 2-65 (full chapter) |

## Extraction notes

- `extract_commentary.py` on `BCAC20_NKW_bo_segmented.md`: 910 transclusions, 0
  empty buckets, chapter 2 = 65/65 verses recovered cleanly. No cascading-shift
  artifacts observed in chapter 2.
- `extract_translation.py --chapter 2` on `padmakara-ch2-test.md`: 65/65 verse
  blocks parsed. One-verse-per-line format, no missing IDs.

### Chapter 2 — verses 1–65

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 2-1 | ⚠ ERROR | རིན་ཆེན་སེམས (rin chen sems) | "that precious mind" — glossed explicitly as bodhicitta: "byang chub kyi sems... rin po che... rang gzhan gyi rgyud la bzung bar bya ba'am bskyed par bya ba'i phyir" (in order to take hold of/generate that precious **mind** of bodhicitta in one's own and others' being) | "that I might gain this precious **form**" | *sems* = mind/bodhicitta, not "form" — this is the purpose clause of the whole offering (to generate bodhicitta), not a wish for a body/form |
| 2-8 | ⚠ ERROR | ལུས་ཀུན་གཏན་དུ་དབུལ་བར་བགྱི (lus kun gtan du dbul bar bgyi) | commentary glosses the offered body as covering **both** this life and every future body: "lus 'di dang... ma 'ongs pa na lus rten gang ji snyed cig blang bar 'gyur ba'i lus can thams cad dus **gtan du** yar dbul bar bgyi" (this body, and all bodies to be taken in future lives, I offer **forever**) | "I offer you my body **for the rest of this life**" | *gtan du* = forever/permanently (across all future lives), not limited to the remainder of this one life — scope wrongly narrowed |
| 2-13 | ⚠ ERROR | འཇིག་རྟེན་དབང་ཕྱུག (\'jig rten dbang phyug) | commentary glosses this by name: "'jig rten dbang phyug **ste spyan ras gzigs**" (Lokeshvara, i.e. **Avalokiteśvara**) | "I will grace sublime Samantabhadra, Mañjughoṣha, **Maitreya**, and their kin" | Wrong named entity — the third figure is Avalokiteśvara, not Maitreya (Maitreya is not named anywhere in this verse's commentary) |
| 2-14 | ⚠ ERROR | ཐུབ་དབང་ཀུན་གྱི་སྐུ (thub dbang kun gyi sku) | commentary: "...sangs rgyas bcom ldan 'das kun gyi **sku lus** la... byug par bgyi" (I will anoint the **bodies** of all the perfect Buddhas) | "I will anoint the **minds** of the mighty Sages" | *sku* = body/kāya, not mind — classic kāya→mind swap |
| 2-24 | ⚠ ERROR | ཞིང་རྡུལ་ཀུན་གྱི་གྲངས་སྙེད (zhing rdul kun gyi grangs snyed) | commentary: "zhing khams rab 'byams kyi rdul la grangs ji snyed cig yod pa de dag gi grangs dang mnyam pa'i rang gi lus sprul nas" (emanating bodies equal in number to the dust-motes of boundless/countless buddha-fields) | "with bodies many as the grains of dust **upon my palm**" | Scope collapsed from "dust-motes of all buddha-realms" (a vast/countless number) to a mundane handful of dust on one's palm |
| 2-28 | ⚠ ERROR | བགྱིད་དུ་སྩལ་བ (bgyid du stsal ba) | commentary: "gang zag gzhan la srog gcod pa la sogs pa'i las **bgyid du bstsal ba'am byed du bcug pa**" (**causing** another person to commit acts like killing, i.e. making/causing them to do it) — "I" is the agent instigating others | "and **was incited by others** to commit the same" | Agent reversed: the text says "I caused/incited others to sin," not "others incited me" |
| 2-45 | ⚠ ERROR | བྲེད་ཤ་ཐོན་པའི་མིག་བགྲད་ནས (bred sha thon pa'i mig bgrad nas) | commentary describes eyes wide/staring in terror: "mig yar yar sngon por gyur nas mig lpags kyi nang du yar bsdus" (eyes rolled up and blue, eyelids retracted) — root anchors on **mig** (eyes) | "seeking help, with **panic-stricken hands**" | Body part swapped — the text specifies bulging/staring eyes, not hands |
| 2-50 | ⚠ ERROR | སྤྱན་རས་གཟིགས་མགོན (spyan ras gzigs mgon) | commentary names the deity explicitly: "spyan ras gzigs mgon de **'phags mchog phyag na pad mo** de nyid" (the protector **Avalokiteśvara**, supreme noble Lotus-in-Hand) | "my lord **Vajrapaṇi**, I cry out..." | Wrong named entity — this verse is addressed to Avalokiteśvara (Lotus-Holder), not Vajrapāṇi (Vajra-Holder, who is the addressee of 2-52) |
| 2-52 | ⚠ ERROR | ཕྱག་ན་རྡོ་རྗེ་ཅན (phyag na rdo rje can) | commentary: "byang chub sems dpa' **phyag na rdo rje can** gang zhig mthong nas..." (Bodhisattva **Vajrapāṇi**, seeing whom...) | "To **Samantabhadra** I shall fly..." | Wrong named entity — this verse is addressed to Vajrapāṇi ("Vajra-in-hand"), not Samantabhadra (already correctly used in 2-49) |
| 2-56 | ⚠ ERROR | ཟུག་རྔུ་ཐམས་ཅད་འབྱིན་པ (zug rngu thams cad 'byin pa) | commentary: "nyon mongs pa 'dod chags la sogs pa'i zug rngu'am sdug bsngal **ma lus pa thams cad** rtsa ba nas 'byin par byed pa" (words that uproot **every single one, without exception,** of the afflictions/sufferings) | "words of the all-knowing doctor, which uproot **a few** of our ills" | *thams cad* = all/every one, not "a few" — the meaning is inverted (total efficacy misrendered as partial) |

**Result: 46/65 clean, 10 errors, 9 softening notes.**

### Softening / mismatch notes (not hard errors, logged for triage)

| Verse | Note |
|---|---|
| 2-9 | *sdig las yang dag 'da' bgyid* ("properly pass beyond/transgress past sin") rendered as "leave behind the **mistakes** of my past" — softens "sdig pa" (sin/wrongdoing) to "mistakes." |
| 2-21 | *mchod rten* (stupas) is one of three named objects (Dharma jewel / stupas / images); English collapses it into the generic "all supports for offering," losing the specific "stupas." |
| 2-25 | Enumeration order: commentary/root lists **mkhan po** (preceptor, "who bestows the vows") before **slob dpon** (teacher/master); English lists "learned master" before "abbots who transmit the vows," reversing the pair. |
| 2-29 | *rjes su yi rang* is glossed specifically as rejoicing in sins **committed by others** ("gzhan gyis... sdig pa bgyis pa de 'dra... rjes su yi rang ba"); English "I have taken pleasure in such sin" doesn't make clear whose sin is being rejoiced in. |
| 2-38 | Three poisons reordered: root/commentary order is gti mug (ignorance) → chags (attachment) → zhe sdang (hatred); English gives "hatred, lust, and ignorance." |
| 2-48 | *chos* (the Dharma Jewel, one of the Three Jewels, "realized in [the Buddha's] mind") is paraphrased as "the wisdom they hold in their hearts" — defensible as gloss, but loses the explicit Dharma-Jewel referent. |
| 2-60 | *bla ma'i bka'* is glossed broadly (Buddha + preceptors + teachers + spiritual friends); English narrows this to "my teacher's precepts" (singular). |
| 2-62 | Root: non-virtue (mi dge ba) is the **cause** of suffering, and one asks how to escape suffering. English "rid myself of sorrow, only cause of evil" reads (on a literal parse) as reversing the cause/effect relationship. |
| 2-65 | Root: "accept that my **sins** are indeed faults" (object = the sins). English: "take **me** as I am, a sinful man" (object shifted to the person). Minor personalization, not a referent error. |

## Second pass — kāya / dharma / mind, named entities, number & scope

Dedicated second sweep confirms and adds nothing beyond the first pass:

- **kāya/mind:** 2-1 (sems→"form") and 2-14 (sku→"minds") are the two hard swaps
  in this chapter — both caught in the first pass. No further instances found on
  re-check of 2-21 (sku gzugs → "images," correct), 2-24, 2-30, 2-31 (lus/ngag/yid
  triads all correctly kept as body/speech/mind).
- **Named entities:** three swaps found — 2-13 (Avalokiteśvara→"Maitreya"), 2-50
  (Avalokiteśvara→"Vajrapaṇi"), 2-52 (Vajrapāṇi→"Samantabhadra"). Verses 2-22,
  2-49, 2-51 were re-checked and are correctly named (Mañjughoṣa; Samantabhadra/
  Mañjughoṣa; Ākāśagarbha/Kṣitigarbha). The 2-50/2-52 pair looks like a one-step
  shift (Avalokiteśvara's verse got Vajrapāṇi's name, Vajrapāṇi's verse got
  Samantabhadra's name) — flagged explicitly since it's a coherent pattern, not
  independent noise.
- **Number/scope:** three instances — 2-8 ("forever" → "for the rest of this
  life"), 2-24 ("dust-motes of all buddha-realms" → "grains of dust upon my
  palm"), 2-56 ("uproots all ills" → "uproots a few of our ills," which inverts
  rather than merely softens the claim).

## Completion check

- [x] Commentary, translation file, and bounded scope (ch. 2, all 65 verses) established before starting.
- [x] Commentary extracted; 0 empty buckets, no cascading shift in chapter 2.
- [x] Every verse (2-1–2-65) got a term-alignment pass anchored on the commentary's own glosses before any verdict.
- [x] Second pass on kāya/entity/number swaps completed (see above).
- [x] ERRORs (wrong referent) kept distinct from softening/style notes.
- [x] Report appended to the commentary×translation report file; write re-read and confirmed (see below).
- [x] Every ERROR surfaced to the user in chat with its Tibetan + commentary citation.
