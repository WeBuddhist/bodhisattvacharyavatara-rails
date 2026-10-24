#!/usr/bin/env python3
"""Write the track contracts (requirements.md + audience.md) that do not exist yet.

  python3 make_contracts.py            # every language in gm_variant_translate.LANGS x academic/children/easy/wbw
  python3 make_contracts.py --dry-run  # list what would be written

Existing files are never touched (the en/zh/hi academic and children contracts are hand-made).
New contracts are in English and name the target language, script and register (multilang/PLAN.md §4).
They follow the en-academic / en-children contracts of this text: same sources, verse-form and term rules.
  easy = easy-to-read for adult general readers, retold from the same language's academic track, with
         the academic locked terms and the academic line structure (one plain line per verse line).
  wbw  = word-by-word: each Tibetan word in order with its contextual gloss; en-wbw fixes the word split.
"""
import argparse
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from gm_variant_translate import LANGS, VARIANTS, track_dir  # noqa: E402

TEXT = "Bodhicaryāvatāra (Śāntideva), Tibetan root bo-བློ་ལྡན་ཤེས་རབ།"
COMMS = "three aligned Tibetan commentaries (Khenpo Kunpal, Khenpo Shenga, Gyaltsab Je)"
IAST = ("IAST, with diacritics (Śāntideva, Mañjuśrī, Samantabhadra)",
        "without diacritics (Shantideva, Manjushri, Samantabhadra)")
SKT = "Sanskrit kept only where the termbase keeps it, with IAST diacritics."

# Per language: script, a note on the language itself, names (academic, children), term convention,
# readership, and optional register notes per variant. Where the termbase decides, it wins.
NOTES = {
    "en": dict(script="Latin script", note="International English; no archaism.", names=IAST, terms=SKT,
               geo="international English readership; many read English as a second language"),
    "zh": dict(script="Traditional Chinese characters",
               note="Modern written Chinese (書面白話) in Traditional characters with full-width punctuation, like the other zh tracks; no classical (文言) sentence patterns.",
               names=("the customary Chinese Buddhist forms (寂天、文殊、普賢、觀世音)",) * 2,
               terms="Established Chinese Buddhist terminology in Traditional characters, as the termbase sets it.",
               geo="Taiwan, Hong Kong, overseas Chinese and other readers of Traditional Chinese", short=True),
    "hi": dict(script="Devanagari", note="Modern standard Hindi in Devanagari.",
               names=("Sanskrit forms in Devanagari (सुभूति, शारिपुत्र, मैत्रेय)",) * 2,
               terms="Buddhist technical terms in Sanskrit (tatsama) form; no Hindu-devotional or Urdu-Persian alternatives for technical terms.",
               geo="Hindi readers in India and Nepal; Buddhist study centres in India"),
    "es": dict(script="Latin script",
               note="Neutral international Spanish, usable in Latin America and Spain: no regionalisms, no voseo, \"ustedes\" for plural address.",
               names=IAST, terms=SKT, geo="Spanish readers in Latin America, Spain and the United States"),
    "pt": dict(script="Latin script",
               note="Brazilian Portuguese: Brazilian spelling (1990 orthographic agreement) and usage; \"você\" for informal address.",
               names=IAST, terms=SKT, geo="Brazil, and Portuguese readers elsewhere"),
    "fr": dict(script="Latin script", note="Modern standard French; French punctuation conventions (« » for quotations).",
               names=IAST, terms=SKT, geo="France, Belgium, Switzerland, Québec and francophone Africa"),
    "it": dict(script="Latin script", note="Modern standard Italian.", names=IAST, terms=SKT,
               geo="Italy and Italian-speaking Switzerland"),
    "id": dict(script="Latin script", note="Standard Indonesian (Bahasa Indonesia baku, EYD spelling).", names=IAST,
               terms="Buddhist terms as Indonesian Buddhist communities use them (Sanskrit and Pāli loans), as the termbase sets them.",
               geo="Indonesia (Buddhist communities, universities) and Malay readers in Malaysia"),
    "sw": dict(script="Latin script", note="Standard Swahili (Kiswahili sanifu) as written in Tanzania and Kenya.",
               names=IAST,
               terms="Swahili has little established Buddhist vocabulary: the termbase renderings (Swahili descriptions or loanwords) decide.",
               geo="Tanzania, Kenya, Uganda and the wider East African Swahili readership"),
    "ja": dict(script="kanji and kana",
               note="Natural modern written Japanese (現代日本語); no kanbun-style (訓読) phrasing.",
               names=("the customary Japanese Buddhist forms in kanji (寂天, 文殊, 普賢, 観音)",) * 2,
               terms="Established Japanese Buddhist terminology in kanji (e.g. 菩提心, 菩薩, 空, 涅槃), as the termbase sets it.",
               geo="Japan", short=True,
               reg={"academic": "Plain written style (である調).",
                    "children": "Polite style (です・ます調); kanji a ten-year-old can read, other words in kana.",
                    "easy": "Polite style (です・ます調); common kanji only."}),
    "ko": dict(script="Hangul",
               note="Modern standard Korean in Hangul, without Hanja in the text.",
               names=("the customary Korean Buddhist forms (적천, 문수, 보현, 관세음)",) * 2,
               terms="Established Korean Buddhist terminology (Sino-Korean, e.g. 보리심, 보살, 공, 열반) in Hangul, as the termbase sets it.",
               geo="South Korea and Korean readers abroad",
               reg={"academic": "Plain written style (한다체).", "children": "Friendly polite style (해요체).",
                    "easy": "Polite style (합니다체)."}),
    "vi": dict(script="Latin script with full Vietnamese diacritics",
               note="Modern standard Vietnamese with full diacritics (Unicode NFC).",
               names=("the customary Vietnamese Buddhist forms (Tịch Thiên, Văn Thù, Phổ Hiền, Quán Thế Âm)",) * 2,
               terms="Established Sino-Vietnamese Buddhist terminology (e.g. Bồ Đề Tâm, Bồ Tát, Niết Bàn), as the termbase sets it.",
               geo="Vietnam and the Vietnamese diaspora"),
    "th": dict(script="Thai script",
               note="Modern standard written Thai; spaces only between phrases and sentences, as Thai is written.",
               names=("the customary Thai Buddhist forms (ศานติเทวะ, มัญชุศรี, สมันตภัทร)",) * 2,
               terms="Established Thai Buddhist vocabulary (Pāli and Sanskrit loans as Thai readers know them), as the termbase sets it.",
               geo="Thailand", short=True),
    "ne": dict(script="Devanagari", note="Modern standard Nepali in Devanagari.",
               names=("Sanskrit forms in Devanagari (सुभूति, शारिपुत्र, मैत्रेय)",) * 2,
               terms="Buddhist technical terms in Sanskrit (tatsama) form, as the termbase sets them.",
               geo="Nepal, and Nepali readers in Sikkim, Darjeeling and Bhutan"),
    "mr": dict(script="Devanagari", note="Modern standard Marathi in Devanagari.",
               names=("Sanskrit forms in Devanagari (सुभूति, शारिपुत्र, मैत्रेय)",) * 2,
               terms=("Buddhist technical terms in Sanskrit (tatsama) form, as the termbase sets them. Many Marathi Buddhist readers "
                      "know Pāli forms (धम्म, निब्बान) from the Ambedkarite tradition; this Mahāyāna text, translated from Tibetan, "
                      "uses the termbase's Sanskrit forms."),
               geo="Maharashtra (India), including the Ambedkarite Buddhist community"),
    "si": dict(script="Sinhala script", note="Modern written Sinhala in Sinhala script (not colloquial spoken Sinhala).",
               names=("the established Sinhala Buddhist forms (e.g. ශාන්තිදේව)",) * 2,
               terms=("Sri Lankan readers know Pāli forms from the Theravāda tradition; this Mahāyāna text uses the termbase renderings."),
               geo="Sri Lanka"),
    "mn": dict(script="Cyrillic script", note="Modern Khalkha Mongolian in Cyrillic script (not the traditional Mongolian script).",
               names=("the customary Mongolian Buddhist forms (Шантидэва, Манзушир, Самантабадра)",) * 2,
               terms="Established Mongolian Buddhist terminology (e.g. бодьсадва, хоосон чанар, нирваан), as the termbase sets it.",
               geo="Mongolia (Khalkha readers)"),
}

VOICE = """- Keep Śāntideva's first-person voice ("I", "my mind") and his rhetorical questions as questions.
- In chapter 9, an opponent's objection stays recognisable as an objection; do not merge it into the reply."""

HARD = "Never make a deep idea false to make it simple: emptiness is not \"nothing\"; \"no self\" is not \"you don't exist\"."


def fm(code, variant, register, extra):
    n = LANGS[code]["name"]
    return "\n".join(["---", f"track: {code}-{variant}", f"text: {TEXT}",
                      f"target_language: {code} ({n}, {NOTES[code]['script']})", f"register: {register}",
                      "status: draft", "termbase: termbase.md", "contract_language: en (written in English; the translation is in the target language)",
                      *extra, "---", ""])


def reg(code, variant):
    r = NOTES[code].get("reg", {}).get(variant)
    return f" {r}" if r else ""


def sentences(code):
    return "short plain sentences" if NOTES[code].get("short") else "plain sentences (mostly under 15 words)"


def requirements(code, variant):
    n, N = LANGS[code]["name"], NOTES[code]
    head = f"## Target language\n{n}, in {N['script']}. {N['note']}\n"
    if variant == "academic":
        aids = ("the two machine drafts (DharmaMitra, Gemini) may be consulted but are not authorities" if code == "en" else
                f"the checked English academic translation (../en-academic/) is given to confirm the meaning, not as the text "
                f"to translate; the {n} machine draft may be consulted but is not an authority")
        return fm(code, variant, "academic", [
            f"source_rails: none complete yet — the KF pilot grounds each verse in the aligned Sanskrit "
            f"(1-SOURCES/Text/BCAV08_SH_sk.md) and {COMMS} instead; see 0-INBOX/kf-pilot/STATE.md"]) + f"""
# Requirements — Bodhicaryāvatāra, {n}, academic

{head}
## Audience and register
Students and practitioners reading a careful study translation; university readers of Buddhist texts (see `audience.md`). Faithful, precise, readable {n}; no archaism.{reg(code, variant)}

## Source and grounding
- Translate from the Tibetan. Use the aligned Sanskrit and the aligned commentary passages to settle the meaning of each verse; {aids}.
- Where the commentaries read a verse differently, follow the reading they share; if they truly split, follow the Tibetan's most literal sense.
- Translate the whole verse, in order: no omissions, no additions, no summary.
- Never add explanations, glosses or notes in the translation itself.

## Vocabulary
- Every term in `termbase.md` is rendered with its locked academic rendering, inflected for number and grammar as needed. Where a term has several senses, the sense assigned to that occurrence is used.
- {N['terms']}
- Proper names: {N['names'][0]}.

## Form and style
- A four-line Tibetan verse becomes four lines of {n} free verse (no rhyme, no metre), separated by line breaks, following the Tibetan line order wherever {n} syntax allows. Longer or shorter verses keep their own line count. Prose blocks (title, homage, colophon) stay prose.
- Standard modern {n} punctuation; each line must read naturally and the verse must parse as a whole.
{VOICE}
- Headings: translate the Tibetan chapter title literally and concisely.
"""
    if variant == "children":
        return fm(code, variant, "children (ages 8–12)", [
            f"built_from: the fact-checked academic translation (../{code}-academic/) — meaning comes from it, wording is new"]) + f"""
# Requirements — Bodhicaryāvatāra, {n}, children's version

{head}
## Audience and register
Children aged 8–12, reading on their own or being read to (see `audience.md`). Warm, clear, simple {n} that a ten-year-old understands on first hearing.{reg(code, variant)}

## Source of meaning
- Each verse is retold from the academic translation of the same verse, checked against the Tibetan. Keep the meaning of every verse: who speaks, what is wished for, what is compared, what is argued, what is denied.
- Do not add ideas, morals, explanations or examples that the verse does not contain. Do not drop a point the verse makes.
- Keep one children's passage per source verse, with the same id, in the same order.

## Vocabulary
- Use the locked children's rendering from `termbase.md` for every listed term, every time.
- No Sanskrit except names. Names: {N['names'][1]}.
- {HARD}
- The hells and suffering are described honestly but without graphic detail beyond what the verse says.

## Style
- Each verse becomes a short passage of {sentences(code)}; no verse form is needed. Everyday words. Active voice.
- Keep the speaker's "I" — the poem is Śāntideva talking to himself; children can follow that.
- Questions stay questions. In chapter 9, make clear when someone is objecting ("Someone might say…").
- Headings: short and plain.
"""
    if variant == "easy":
        return fm(code, variant, "easy-to-read (adult general readers)", [
            f"built_from: the fact-checked academic translation (../{code}-academic/) — meaning and locked terms come from it, wording is plain"]) + f"""
# Requirements — Bodhicaryāvatāra, {n}, easy-to-read version

{head}
## Audience and register
Adults who want to read the text without a Buddhist or academic background: general readers, readers in a second language, readers who find dense religious prose hard (see `audience.md`). Plain, modern, respectful {n} for adults — not a children's book.{reg(code, variant)}

## Source of meaning
- Each verse is retold from the academic translation of the same verse, checked against the Tibetan. Keep the meaning of every verse: who speaks, what is wished for, what is compared, what is argued, what is denied.
- Do not add ideas, explanations or examples that the verse does not contain. Do not drop a point the verse makes.
- Keep one passage per source verse, with the same id, in the same order.

## Vocabulary
- Use the locked academic rendering from `termbase.md` for every listed term, every time, so that the easy-to-read and the academic versions use the same terms. Do not explain the terms inside the text.
- Proper names as in the academic version: {N['names'][0]}.
- {HARD}

## Form and style
- Keep the line structure of the academic version: one line for each line of the verse, in the same order. Each line is a plain sentence or a clear part of one; no rhyme or metre. Prose blocks (title, homage, colophon) stay prose.
- Common words, one idea per sentence, active voice, normal word order; no archaism and no poetic inversion.
- Keep Śāntideva's first-person voice ("I", "my mind"). Questions stay questions. In chapter 9, make clear when someone is objecting ("Someone might say …") and keep the objection apart from the reply.
- Headings: short and plain.
"""
    # wbw
    ref = ("This English track defines the word split; every other language uses exactly the same `bo` entries."
           if code == "en" else
           "The word split is fixed by the English word-by-word track (../en-wbw/): use exactly its `bo` entries, in order, and write only the glosses.")
    return fm(code, variant, "word-by-word gloss", [
        f"built_from: the Tibetan root and the fact-checked academic translation (../{code}-academic/) — glosses follow its reading"]
        + ([] if code == "en" else ["word_split: ../en-wbw/ (shared by every language)"])) + f"""
# Requirements — Bodhicaryāvatāra, {n}, word-by-word

{head}
## Audience and purpose
Readers who study the Tibetan text: students of Classical Tibetan, translators, practitioners who recite the Tibetan and want to know what each word means (see `audience.md`). Each segment becomes a table: every Tibetan word, in order, with its gloss in {n}.

## Word split
- Split each segment into its words, in order, so that the entries together reproduce the whole Tibetan segment: every syllable once, nothing skipped, repeated or changed.
- One entry per word: a noun, verb, adjective or adverb together with its own syllables; compounds and names stay together; a locked term whose words stand together stays one entry. Grammatical particles (case markers, connectives, the topic marker, quotation and final particles) get their own entries.
- {ref}

## Glosses
- Each gloss gives the meaning of the word in this verse, as the academic translation reads it, in a few words of {n}: nouns in their base form, verbs in a neutral form.
- A particle gets a short gloss of its function in {n} (the word {n} would use for "of", "by", "to", "and", "as for", or the like).
- For a word that is a term in `termbase.md`, the gloss is the locked academic rendering.
- {N['terms']}
- Proper names: {N['names'][0]}.
- No notes, brackets or explanations in a gloss.
"""


def audience(code, variant):
    n, N = LANGS[code]["name"], NOTES[code]
    body = {
        "academic": f"""## 1. Demographics and Region
- **Age range:** adult (18+).
- **Geography:** {N['geo']}.
- **Language background:** fluent readers of {n}.
- **Monastic / lay / mixed:** mixed.

## 2. Prior Knowledge and Reading Level
- **Buddhist background:** Mahāyāna study background or university-level interest.
- **Familiarity with Sanskrit/Tibetan terms:** recognises common Buddhological terms (bodhisattva, bodhicitta, Dharma, saṃsāra) in their usual {n} forms.
- **Familiarity with the text:** aware of it; may be studying it with commentaries or alongside other translations.

## 3. Use Cases and Reading Settings
Close study, citation, comparison with other translations, recitation of single verses, use alongside the Tibetan and Sanskrit.

## 4. Motivations and Pain Points
Wants accuracy and terminological consistency they can rely on; frustrated by paraphrase and by terms that change from verse to verse.""",
        "children": f"""## 1. Demographics and Region
- **Age range:** 8–12.
- **Geography:** {n}-reading children in {N['geo']}; Buddhist families, Dharma schools, curious children.
- **Language background:** {n} readers at primary-school level; some reading {n} as a second language.

## 2. Prior Knowledge and Reading Level
- **Buddhist background:** may know who the Buddha is; no technical vocabulary.
- **Familiarity with the text:** first encounter.

## 3. Use Cases and Reading Settings
Read aloud by a parent or teacher, Dharma-school lessons, independent reading a few verses at a time.

## 4. Motivations and Pain Points
Wants ideas they can try in their own life (being kind, handling anger, paying attention); lost by long sentences, foreign words and abstract lists.""",
        "easy": f"""## 1. Demographics and Region
- **Age range:** adult (18+).
- **Geography:** {N['geo']}.
- **Language background:** {n} readers of every level, including readers in a second language and readers who prefer plain language.
- **Monastic / lay / mixed:** mostly lay.

## 2. Prior Knowledge and Reading Level
- **Buddhist background:** little or none; may have heard of the Buddha, meditation or compassion.
- **Familiarity with Sanskrit/Tibetan terms:** few; meets the terms here in the same form as in the academic version.
- **Familiarity with the text:** first encounter.

## 3. Use Cases and Reading Settings
First reading of the whole text, reading groups and introductory courses, reading next to the academic version, listening (text-to-speech).

## 4. Motivations and Pain Points
Wants to understand what the text actually says without a teacher; put off by long sentences, inverted poetic word order and unexplained jargon; does not want a simplified children's text.""",
        "wbw": f"""## 1. Demographics and Region
- **Age range:** adult (16+).
- **Geography:** {N['geo']}.
- **Language background:** fluent readers of {n} who read, or are learning to read, Tibetan script.
- **Monastic / lay / mixed:** mixed; many in monastic or Dharma-centre study programmes.

## 2. Prior Knowledge and Reading Level
- **Buddhist background:** some study background.
- **Familiarity with Tibetan:** knows the script; beginner to intermediate grammar.
- **Familiarity with the text:** may recite it in Tibetan or study it with a teacher.

## 3. Use Cases and Reading Settings
Learning Classical Tibetan from a real text, following the Tibetan during recitation, checking how a translation reads a word, preparing a class.

## 4. Motivations and Pain Points
Wants to see which Tibetan word carries which meaning; frustrated when glosses skip particles, change from verse to verse, or do not match the translation they read.""",
    }[variant]
    return f"---\ntrack: {code}-{variant}\nstatus: draft\n---\n\n# Audience Profile — `{code}-{variant}`\n\n{body}\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    n = 0
    for code in LANGS:
        for variant in VARIANTS:
            d = track_dir(code, variant)
            for name, make in (("requirements.md", requirements), ("audience.md", audience)):
                f = d / name
                if f.exists():
                    continue
                n += 1
                print(("would write " if a.dry_run else "wrote ") + str(f.relative_to(d.parents[1])))
                if not a.dry_run:
                    d.mkdir(parents=True, exist_ok=True)
                    f.write_text(make(code, variant), encoding="utf-8")
    print(f"{n} files {'to write' if a.dry_run else 'written'}")


if __name__ == "__main__":
    main()
