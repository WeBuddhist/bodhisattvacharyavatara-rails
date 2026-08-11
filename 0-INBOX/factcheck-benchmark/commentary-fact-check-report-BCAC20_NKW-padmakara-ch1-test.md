# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/Commentaries/Transcluded/BCAC20_NKW_bo_segmented.md` (Khenpo Ngakwang Kunga Wangchuk, BCAC20_NKW)
- **Translation audited:** `factcheck-benchmark/padmakara-ch1-test.md` (Padmakara Translation Group, adapted, 2006 — draft, single-line-per-verse)

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1, verses 1-1 to 1-36 (full chapter) |

### Chapter 1 — verses 1–36

**Extraction note:** `extract_commentary.py` produced 36/36 verse buckets for chapter
1 with 0 empty passages (auto-detected `link_base: bo-བློ་ལྡན་ཤེས་རབ།`).
`extract_translation.py` parsed 36/36 verse blocks. Two verses (1-18 and 1-29) have
a **cascading shift**: their commentary bucket holds only the root-verse quote, and
the explanatory prose sits at the *start* of the next verse's bucket (1-19 and 1-30
respectively). Both were resolved by reading the recovered prose before judging —
noted here, not reported as translation defects.

A full term-by-term alignment table was built for every verse against the
commentary's own glosses before any verdict was assigned, followed by a dedicated
second pass restricted to kāya/dharma/mind, named entities, and number/scope across
the whole chapter (this second pass caught the 1-30 enumeration-order swap that the
first pass missed).

**Result: 19/36 verses clean, 17 ERROR rows (across 15 verses), 4 softening notes.**

---

#### ERROR rows (wrong referent — not style)

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-1 | ⚠ ERROR | ཆོས་ཀྱི་སྐུ (chos kyi sku) | Glossed at length as the **Dharma Jewel** (chos dkon mchog): the cessation-truth and path-truth wisdom that "serves as a basis of qualities... therefore called *sku* [body]" — dharmakāya, a buddha-body | "the dharma they embody" | Should read "dharmakāya" / "truth body," not "the dharma" — collapses kāya into "dharma" |
| 1-1 | ⚠ ERROR | སྡོམ (sdom, from *bde gshegs sras kyi sdom la 'jug pa*) | Defined explicitly: restraining body/speech/mind from unfavorable conduct; divided into the three bodhisattva śīlas (restraint, gathering virtue, benefiting beings) — "vow" / "discipline" | "the practice of the Bodhisattva way of life" | *sdom* = vow/discipline, not "way of life" |
| 1-5 | ⚠ ERROR | (simile) གློག་... ཡུལ་རི་ར་བ་བྲག་ཁང་ཁྱིམ་སེམས་ཅན་ལ་སོགས་པ་གསལ་བར་སྣང་བ | Lightning briefly illuminates **forms** — mountains, walls, houses, sentient beings — not the sky itself | "the sudden lightning glares and the whole sky is illuminated" | Wrong simile tenor: lightning reveals *forms*, not "the sky" |
| 1-6 | ⚠ ERROR | དགེ་བ (dge ba) | Glossed as "the actual cause of attaining higher rebirth and, ultimately, liberation and omniscience" — virtue/wholesome action broadly | "Kindness, thus, is weak" | *dge ba* = virtue/goodness, not "kindness" |
| 1-7 | ⚠ ERROR | ཐུབ་དབང་རྣམས (thub dbang rnams, plural) | "the Blessed Buddhas, among those Sages... [rdzogs pa'i sangs rgyas bcom ldan 'das de dag rnams]" — plural, all the Buddhas | "the mighty King" (singular) | Should be plural "the mighty Sages/Buddhas," not a singular "King" |
| 1-9 | ⚠ ERROR | བདེ་གཤེགས་རྣམས (bde gshegs rnams, plural) | Root verse marks *rnams* (plural) on Sugatas — "children of the Sugatas [pl.]" | "children of the Blissful One" (singular) | Plural "Sugatas/Blissful Ones," not singular "the Blissful One" |
| 1-10 | ⚠ ERROR | མི་གཙང་ལུས (mi gtsang lus) | Glossed explicitly and at length as the impure physical **body** — "snot, saliva, phlegm, pus, blood, fat, lymph" (snabs, mchil ma, bad kan, rnag, khrag, zhag, chu ser) — analogized to iron transmuted to gold | "it takes our confused perceptions" | *lus* = body (physical), not "perceptions" — wrong referent entirely |
| 1-11 | ⚠ ERROR | འགྲོ་བའི་དེད་དཔོན་གཅིག་པུ ('gro ba'i ded dpon **gcig pu**) | "*gcig pu*" = sole/alone — glossed as the Buddha alone, likened to a ship's sole captain who leads beings across saṃsāra | "the boundless wisdom of the **many** guides of beings" | *gcig pu* = "sole/alone" (the Buddha alone), not "many guides" — number reversed |
| 1-14 | ⚠ ERROR | བྱམས་མགོན་བློ་དང་ལྡན་པས་ནོར་བཟང་བཤད (byams mgon blo dang ldan pas **nor bzang** bshad) | Explicit narrative: Maitreya (byams mgon, "the Loving Protector") **explained** bodhicitta's benefits **to the youth Sudhana** (nor bzang), per the Gaṇḍavyūha | "as the Wise and Loving Lord explained **to Maitreya**" | Agent/recipient reversed: Maitreya is the teacher, Sudhana the recipient — "Sudhana" is dropped and Maitreya wrongly cast as the one taught |
| 1-19 | ⚠ ERROR | ནམ་མཁའ་མཉམ་པ (nam mkha' mnyam pa) | Glossed via sutra citation: "if [bodhicitta's merit] had form, it would fill the entire realm of **space** (nam mkha'i khams) and exceed even that" | "rises equal to the depths of **the ocean**" | *nam mkha'* = space/sky, not "ocean" — wrong referent |
| 1-20 | ⚠ ERROR | ལག་བཟངས (lag bzangs, Subāhu) | "the sūtra requested by the young bodhisattva **Subāhu** (lag bzangs)" | "in the sūtra **Sāriputra** requested" | Named entity wrong: Subāhu (lag bzangs), not Sāriputra |
| 1-21 | ⚠ ERROR | ཀླད་ནད (klad nad) | Illustrated by the jātaka: the suffering of a **head** pained by a burning iron wheel (klad pa na ba) — a headache, a deliberately trivial physical ailment | "soothe the aching **hearts**" | *klad nad* = headache (physical), not "aching hearts" (emotional) |
| 1-22 | ⚠ ERROR | སེམས་ཅན་རེ་རེ (sems can **re re**) | "*re re*" = each and every one — the immeasurable suffering of every single being, individually, i.e. all beings | "the endless pain of **a few** living beings" | *re re* = "each and every" (all beings, one by one), not "a few" — scope reversed |
| 1-23 | ⚠ ERROR | ཚངས་པ (tshangs pa) | "even the Great **Brahmā** (tshangs pa chen po), who has trained his mind in the four immeasurables" | "even **Indra** harbor such benevolence" | Named entity wrong: Brahmā (tshangs pa), not Indra |
| 1-25 | ⚠ ERROR | སེམས་ཀྱི་རིན་ཆེན་ཁྱད་པར (sems kyi rin chen khyad par) | "a supremely exalted **mind** among minds (sems), like a wish-fulfilling jewel-mind" — bodhicitta explicitly glossed as *sems*, mind | "this noble, jewellike form of **buddha-body**" | *sems* = mind, not "buddha-body" — kāya/mind swap |
| 1-28 | ⚠ ERROR | མངོན་པར་རྒྱུག (mngon par rgyug) | Beings (the subject) "run headlong toward suffering itself" — self-defeating action; beings are the agent | "but **misery itself pursues them**" | Agent reversed: beings run toward suffering; suffering is not the one doing the pursuing |
| 1-33 | ⚠ ERROR | སེམས་ཅན་གྲངས་མཐའ་ཡས (sems can **grangs mtha' yas**) | Explicitly contrasted with the previous verse's "a few" (nyung zad): "not five, ten, fifteen, a hundred... but those of **infinite, uncountable** number" | "bestow on **a handful of followers**" | *grangs mtha' yas* = infinite/boundless in number, not "a handful" — scope reversed, and "followers" is invented |
| 1-30 | ⚠ ERROR (order) | དགེ་(མཚུངས) ... བཤེས་... བསོད་ནམས (dge / bshes / bsod nams) | Root verse enumerates in this order: (1) virtue equal to this? (2) such a friend? (3) such merit? | "what **friend**... what **virtue**... what merit" | Enumeration order swapped: should be virtue → friend → merit, not friend → virtue → merit |

#### Softening / style notes (not hard errors — referent not renamed)

| Verse | Tibetan (Wylie) | Commentary gloss | English | Note |
|---|---|---|---|---|
| 1-1 | ཕྱག་འོས་ཀུན (phyag 'os kun) | "worthy of prostration" — śrāvakas, pratyekabuddhas, one's own abbot/teacher/parents, as a field of merit | "all those worthy of respect" | Softened from "prostration/homage" to "respect"; acceptable given "I reverently bow" carries the verb separately |
| 1-4 | སྐྱེས་བུ (skyes bu) | Glossed explicitly: "one endowed with strength and capacity" — the individual practitioner who has attained this human life | "...whereby **the aims of beings** may be gained" | Scope shift from the specific capable individual to generic "beings"; likely acceptable poetic gender-neutral compression, flagged for editor review |
| 1-20 | དམན་མོས་སེམས་ཅན (dman mos sems can) | Beings inclined toward the lesser/inferior vehicle (dman pa) | "those inclined to **simpler paths**" | Softened from "lesser/inferior vehicle" to "simpler paths" |
| 1-27 | སེམས་ཅན་མ་ལུས་ཐམས་ཅད (sems can ma lus thams cad) | "ALL beings without exception" | "...bring about the weal and benefit of **beings**" | "All without exception" dropped to generic "beings" — likely fine, flagged for completeness |

---

## Second-pass note (kāya/dharma/mind, named entities, number/scope)

The dedicated second sweep confirmed the first-pass findings and added one new
catch: the **1-30 enumeration-order swap** (virtue/friend/merit → friend/virtue/merit),
which a first pass focused on referent-correctness alone did not flag. All three
kāya-class errors found (1-1 chos kyi sku→"dharma"; 1-10 mi gtsang lus→"perceptions";
1-25 sems→"buddha-body") and all three named-entity errors (1-14 Sudhana↔Maitreya
swap; 1-20 Subāhu→"Sāriputra"; 1-23 Brahmā→"Indra") were located during this
targeted re-scan of every *sku*/*chos*/*sems* occurrence and every proper name in the
chapter. No further doctrinal-category swaps were found beyond what is listed above.
