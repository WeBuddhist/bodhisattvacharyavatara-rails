#!/usr/bin/env python3
"""
Correlate the English terms in glossary.md against three keyword-extraction methods:

  1. YAKE     - en-n-gram-keyword.json
  2. TF-IDF   - en-tfidf.md
  3. Combined - en-keywords-fused-pmi.md  (RRF fusion of the two, NPMI-gated)

For every glossary term we decide whether it is present in a method's ranking as an
exact match, a partial match, or not at all, and write CORRELATION_REPORT.md.

Standard library only.
"""

import json
import re
from collections import OrderedDict
from pathlib import Path

BASE = Path(__file__).resolve().parent

GLOSSARY = BASE / 'glossary.md'
YAKE_JSON = BASE / 'en-n-gram-keyword.json'
TFIDF_MD = BASE / 'en-tfidf.md'
FUSED_MD = BASE / 'en-keywords-fused-pmi.md'

REPORT = BASE / 'CORRELATION_REPORT.md'
SUMMARY = BASE / 'CORRELATION_SUMMARY.md'
DUMP = BASE / 'correlation_analysis_results.txt'

# The three methods being compared. TF-IDF here is the pure single-word list:
# en-tfidf.md also carries 1,558 YAKE phrases, which are not TF-IDF results.
PRIMARY = OrderedDict([
    ('YAKE', 'YAKE'),
    ('TF-IDF (pure unigram)', 'TF-IDF'),
    ('Fused / Combined', 'Combined'),
])

# Words ignored when deciding whether a reverse partial is meaningful.
STOPWORDS = {
    'of', 'and', 'the', 'a', 'an', 'in', 'to', 'for', 'from', 'with', 'or',
    'on', 'at', 'by', 'as', 'is', 'be', 'its', 'his', 'her', 'their',
}

TOP_K = (100, 250, 500, 1000, 2000)


# --------------------------------------------------------------------------
# Normalization
# --------------------------------------------------------------------------

def normalize(text):
    """Lowercase, drop markdown bold, parentheticals and punctuation."""
    text = text.replace('**', '').strip().lower()
    text = re.sub(r'\([^)]*\)', ' ', text)          # "Bliss (experience)" -> "bliss"
    text = text.replace('’', "'").replace('‘', "'")
    text = re.sub(r"[^a-z0-9'\- ]", ' ', text)
    text = text.replace('-', ' ')
    return re.sub(r'\s+', ' ', text).strip()


def singularize(word):
    """Light plural stripper - enough to align 'teachings' with 'teaching'."""
    if len(word) > 3 and word.endswith('ies'):
        return word[:-3] + 'y'
    if len(word) > 3 and word.endswith('es') and word[-3] in 'sxzh':
        return word[:-2]
    if len(word) > 3 and word.endswith('s') and not word.endswith('ss'):
        return word[:-1]
    return word


def tokenize(text):
    """Normalized token tuple - the unit every comparison works on."""
    return tuple(singularize(w) for w in normalize(text).split() if w)


def fold_transliteration(token):
    """
    Collapse Sanskrit romanisation variants so that the glossary's 'Manjushri'
    can be recognised as the corpus's 'manjusri'. Used only for the supplementary
    transliteration pass, never for the headline counts.
    """
    for a, b in (('sh', 's'), ('ch', 'c'), ('ph', 'p'), ('th', 't'),
                 ('kh', 'k'), ('gh', 'g'), ('bh', 'b'), ('dh', 'd'),
                 ('jh', 'j'), ('ee', 'i'), ('oo', 'u'), ('v', 'w')):
        token = token.replace(a, b)
    return re.sub(r'(.)\1+', r'\1', token)


def fold_key(tokens):
    return tuple(fold_transliteration(t) for t in tokens)


def is_meaningful(tokens):
    """A run of tokens worth calling a match - not purely stopwords or stubs."""
    return any(t not in STOPWORDS and len(t) > 2 for t in tokens)


def contains_run(haystack, needle):
    """True if `needle` occurs as a contiguous whole-token run inside `haystack`."""
    n = len(needle)
    if n == 0 or n > len(haystack):
        return False
    return any(haystack[i:i + n] == needle for i in range(len(haystack) - n + 1))


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

def load_glossary(path):
    """English terms from the 3-column glossary table, in file order."""
    terms = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')]
        if len(cells) < 3:
            continue
        term = cells[1]
        # Skip the header row and the `| ----- |` separator.
        if not term or term == 'English term' or set(term) <= set('- '):
            continue
        terms.append(term)
    return terms


def load_yake(path):
    """YAKE keys, kept in file order (ascending score = descending importance)."""
    data = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=OrderedDict)
    return list(data.keys())


def load_ranked_table(path, header_prefix):
    """
    Rows of the markdown table beginning at `header_prefix`, stopping at the next
    `##` heading. The stop condition is what keeps the fused file's `## Gated out`
    table - phrases the NPMI gate *rejected* - out of the results.
    """
    rows, inside = [], False
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith(header_prefix):
            inside = True
            continue
        if not inside:
            continue
        if line.startswith('##'):
            break
        if not line.startswith('|') or line.startswith('|--'):
            continue
        rows.append([c.strip() for c in line.split('|')])
    return rows


def glossary_check_counts(path, header_prefix):
    """Tally the pre-existing `Glossary` column (checkmark / tilde / dash)."""
    ticks = 0
    for row in load_ranked_table(path, header_prefix):
        if len(row) >= 3 and row[-2].startswith('✓'):
            ticks += 1
    return ticks


# --------------------------------------------------------------------------
# Matching
# --------------------------------------------------------------------------

class Method:
    """One ranking, with its terms pre-tokenized and indexed."""

    def __init__(self, name, terms, note=''):
        self.name = name
        self.note = note
        self.terms = terms
        self.keys = [tokenize(t) for t in terms]
        self.exact_index = {}
        for term, key in zip(terms, self.keys):
            self.exact_index.setdefault(key, term)
        self.folded_index = {}
        for term, key in zip(terms, self.keys):
            self.folded_index.setdefault(fold_key(key), term)

    def classify(self, glossary_term):
        """
        -> (tier, matching_ranking_term)

        tier is one of: exact, partial_fwd, partial_rev, none

          exact        normalized token sequences are equal
          partial_fwd  glossary term sits inside a longer ranking term
                       ("guru" within "guru rinpoche")   <- primary definition
          partial_rev  a ranking term sits inside a longer glossary term
                       ("space" for "Absolute space")
        """
        gkey = tokenize(glossary_term)
        if not gkey:
            return 'none', None

        if gkey in self.exact_index:
            return 'exact', self.exact_index[gkey]

        rev_hit = None
        for term, tkey in zip(self.terms, self.keys):
            if len(tkey) > len(gkey) and contains_run(tkey, gkey):
                return 'partial_fwd', term
            if rev_hit is None and len(tkey) < len(gkey) \
                    and contains_run(gkey, tkey) and is_meaningful(tkey):
                rev_hit = term

        if rev_hit is not None:
            return 'partial_rev', rev_hit
        return 'none', None

    def folded_exact(self, glossary_term):
        """Exact match after transliteration folding; None if it adds nothing."""
        return self.folded_index.get(fold_key(tokenize(glossary_term)))

    def precision_at(self, glossary_keys, k):
        """How many of the top-k ranked terms are themselves glossary terms."""
        return sum(1 for key in self.keys[:k] if key in glossary_keys)


def analyze(method, glossary):
    """Bucket every glossary term for one method."""
    buckets = {'exact': OrderedDict(), 'partial_fwd': OrderedDict(),
               'partial_rev': OrderedDict(), 'none': []}
    for term in glossary:
        tier, hit = method.classify(term)
        if tier == 'none':
            buckets['none'].append(term)
        else:
            buckets[tier][term] = hit
    return buckets


def covered(buckets):
    """Glossary terms the method reached by any tier."""
    return set(buckets['exact']) | set(buckets['partial_fwd']) | set(buckets['partial_rev'])


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def fmt_pct(n, total):
    return f'{n / total * 100:.1f}%'


def build_report(glossary, methods, results, translit, checks):
    total = len(glossary)
    out = []
    w = out.append

    primary = ['YAKE', 'TF-IDF (pure unigram)', 'Fused / Combined']
    y, t, f = (covered(results[n]) for n in primary)
    ye, te, fe = (set(results[n]['exact']) for n in primary)
    any_cov = y | t | f
    all_cov = y & t & f

    single = sum(1 for g in glossary if len(tokenize(g)) == 1)

    w('# Glossary Coverage Across Three Keyword-Extraction Methods')
    w('')
    w('**Question:** how many of the English terms in `glossary.md` are surfaced by '
      'YAKE, by TF-IDF, and by the combined (fused) method &mdash; exactly, and partially?')
    w('')
    w(f'**Corpus:** {total} glossary terms ({single} single-word, {total - single} multi-word) '
      'checked against three rankings over the same English text.')
    w('')
    w('> This report replaces an earlier version of `CORRELATION_REPORT.md` whose numbers were '
      'invalid. That version reported TF-IDF at 0.2% coverage and zero terms shared between the '
      'three methods; both were parser artifacts. See *Corrections* at the end.')
    w('')
    w('---')
    w('')

    # ---------------- headline ----------------
    w('## 1. Headline results')
    w('')
    w('| Method | Terms ranked | Exact | Partial | **Total found** | **Coverage** |')
    w('|---|---:|---:|---:|---:|---:|')
    for name in ['YAKE', 'TF-IDF (pure unigram)', 'TF-IDF (file as published)', 'Fused / Combined']:
        b = results[name]
        ex = len(b['exact'])
        pa = len(b['partial_fwd']) + len(b['partial_rev'])
        tot = ex + pa
        w(f'| {name} | {len(methods[name].terms):,} | {ex} | {pa} | **{tot}** | '
          f'**{fmt_pct(tot, total)}** |')
    w('')
    w('Read this table with the next one before drawing conclusions: most of the *partial* '
      'column is the loose reverse-containment tier, which is far weaker evidence than an exact '
      'match. On **exact matches alone**, coverage runs '
      f'{fmt_pct(len(results["YAKE"]["exact"]), total)}&ndash;'
      f'{fmt_pct(len(results["TF-IDF (file as published)"]["exact"]), total)}.')
    w('')

    # ---------------- tiers ----------------
    w('## 2. The same numbers split by match tier')
    w('')
    w('| Method | Exact | Partial &mdash; forward | Partial &mdash; reverse | None |')
    w('|---|---:|---:|---:|---:|')
    for name in ['YAKE', 'TF-IDF (pure unigram)', 'TF-IDF (file as published)', 'Fused / Combined']:
        b = results[name]
        w(f'| {name} | {len(b["exact"])} | {len(b["partial_fwd"])} | '
          f'{len(b["partial_rev"])} | {len(b["none"])} |')
    w('')
    w('**Tier definitions**')
    w('')
    w('| Tier | Rule | Example |')
    w('|---|---|---|')
    w('| **Exact** | the two normalized token sequences are identical | glossary `Bodhicitta` = ranked `bodhicitta` |')
    w('| **Partial &mdash; forward** | the glossary term appears as a whole-token run *inside a longer ranked term* | glossary `Amitayus` inside ranked `buddha protector amitayus` |')
    w('| **Partial &mdash; reverse** | a ranked term appears as a whole-token run *inside a longer glossary term* | ranked `space` for glossary `Absolute space` |')
    w('| **None** | neither direction matches | glossary `Chenrezi` |')
    w('')
    w('Forward partial is the stricter, more useful reading: the glossary concept is genuinely '
      'present in the ranking, just carrying extra context. Reverse partial only tells you that '
      'one component word of a compound glossary entry showed up somewhere, which is much weaker '
      '&mdash; `space` is not evidence that the ranking captured *Absolute space*.')
    w('')
    w('Why forward partial is near zero for two methods: TF-IDF proper ranks **single words only**, '
      'and a single word cannot contain a multi-word phrase. The fused list keeps only 310 '
      'multi-word phrases after NPMI gating, so it has almost no longer terms to absorb a glossary '
      'entry either. YAKE is the only method whose n-grams produce meaningful forward partials.')
    w('')
    w('Worked forward-partial examples from YAKE:')
    w('')
    for g, hit in list(results['YAKE']['partial_fwd'].items())[:8]:
        w(f'- glossary **{g}** &rarr; ranked `{hit}`')
    w('')

    # ---------------- normalization ----------------
    w('## 3. How terms were compared')
    w('')
    w('Both sides pass through the same pipeline before comparison:')
    w('')
    w('1. strip markdown bold, lowercase;')
    w('2. drop parentheticals &mdash; `Bliss (experience)` &rarr; `bliss`;')
    w('3. strip punctuation, hyphens become spaces;')
    w('4. light singularization &mdash; `teachings` &rarr; `teaching`;')
    w('5. compare as **token sequences**, never as raw substrings.')
    w('')
    w('Step 5 matters. A raw substring test makes `bell` match `rebellion` and lets any '
      'single-letter parsing artifact match every term in the glossary; that is exactly how the '
      'previous report reached its numbers.')
    w('')

    # ---------------- overlap ----------------
    w('## 4. Overlap between the three methods')
    w('')
    w('Comparing the three genuine methods (TF-IDF here is the pure unigram list &mdash; see &sect;6).')
    w('')
    w('| Reached by | Exact match only | Any tier |')
    w('|---|---:|---:|')
    w(f'| All three methods | {len(ye & te & fe)} | {len(all_cov)} |')
    w(f'| At least one method | {len(ye | te | fe)} | {len(any_cov)} |')
    w(f'| No method | {total - len(ye | te | fe)} | {total - len(any_cov)} |')
    w('')
    w('| Unique contribution | Exact match only | Any tier |')
    w('|---|---:|---:|')
    w(f'| Only YAKE finds it | {len(ye - te - fe)} | {len(y - t - f)} |')
    w(f'| Only TF-IDF finds it | {len(te - ye - fe)} | {len(t - y - f)} |')
    w(f'| Only Fused finds it | {len(fe - ye - te)} | {len(f - y - t)} |')
    w('')
    only_yake = sorted(ye - te - fe)
    if only_yake:
        w(f'The {len(only_yake)} terms **only YAKE** matches exactly are all multi-word phrases '
          'that a unigram ranking structurally cannot represent:')
        w('')
        w('> ' + ', '.join(f'`{t}`' for t in only_yake))
        w('')
    w('TF-IDF and the fused list contribute nothing that the other two miss. Their vocabularies '
      'are supersets built from the same unigram pool, so they add depth, not new concepts.')
    w('')

    # ---------------- rank ----------------
    w('## 5. Where glossary terms land in each ranking')
    w('')
    w('Coverage says whether a term appears anywhere in a list of several thousand. This says '
      'whether a method puts glossary terms *near the top*, which is what matters if the ranking '
      'is used to propose glossary candidates.')
    w('')
    w('Each cell: glossary terms found in the top-k, and what share of that top-k they represent.')
    w('')
    w('| Method | ' + ' | '.join(f'top {k:,}' for k in TOP_K) + ' |')
    w('|---|' + '---:|' * len(TOP_K))
    gkeys = {tokenize(g) for g in glossary}
    for name in primary:
        cells = []
        for k in TOP_K:
            hits = methods[name].precision_at(gkeys, k)
            cells.append(f'{hits} ({fmt_pct(hits, k)})')
        w(f'| {name} | ' + ' | '.join(cells) + ' |')
    w('')
    w('The three are close at the very top. Past the first few hundred terms the fused ranking '
      'keeps the highest concentration of glossary terms, which is the behaviour the RRF fusion '
      'was designed to produce &mdash; it is a better *ranking*, even though its raw coverage is '
      'similar to TF-IDF\'s.')
    w('')

    # ---------------- tfidf caveat ----------------
    w('## 6. A caveat about `en-tfidf.md`')
    w('')
    tf_pure = len(methods['TF-IDF (pure unigram)'].terms)
    tf_file = len(methods['TF-IDF (file as published)'].terms)
    w(f'The "Full Ranked Table" in `en-tfidf.md` holds **{tf_file:,}** rows, but only '
      f'**{tf_pure:,}** are TF-IDF results. The remaining **{tf_file - tf_pure:,}** rows are '
      'multi-word **YAKE phrases appended to the same table** (the file marks them with `-` in '
      'the Count, TF-IDF, IDF and Band columns).')
    w('')
    w('So the file is a merged artifact, not a TF-IDF ranking. Treating it as one credits TF-IDF '
      'with YAKE\'s phrase extraction &mdash; worth '
      f'{len(results["TF-IDF (file as published)"]["exact"]) - len(results["TF-IDF (pure unigram)"]["exact"])} '
      'extra exact matches. Both readings are reported above; the pure unigram list is the one '
      'used in the method comparison.')
    w('')
    w('Similarly, `en-keywords-fused-pmi.md` contains a second table under `## Gated out` listing '
      'phrases the NPMI gate **rejected**. Those are not results and are excluded.')
    w('')

    # ---------------- crosscheck ----------------
    w('## 7. Cross-check against the files\' own annotations')
    w('')
    w('Both markdown files already carry a `Glossary` column marking rows as `✓` (exact), '
      '`~` (partial) or `—` (none), produced independently of this analysis.')
    w('')
    w('| File | Its own `✓` count | Exact matches computed here | Difference |')
    w('|---|---:|---:|---:|')
    for label, key, path_key in [
        ('en-tfidf.md', 'TF-IDF (file as published)', 'tfidf'),
        ('en-keywords-fused-pmi.md', 'Fused / Combined', 'fused'),
    ]:
        theirs = checks[path_key]
        ours = len(results[key]['exact'])
        w(f'| `{label}` | {theirs} | {ours} | +{ours - theirs} |')
    w('')
    w('The counts agree closely and this analysis finds slightly more, because normalization here '
      'also folds plurals and parentheticals. The agreement is a useful independent confirmation '
      'that the exact-match layer is sound.')
    w('')

    # ---------------- translit ----------------
    w('## 8. Transliteration is hiding real matches')
    w('')
    w(f'{len(translit)} glossary terms score as "not found" purely because the glossary and the '
      'source text romanise Sanskrit differently &mdash; the glossary writes `sh`, the text writes '
      '`s`:')
    w('')
    w('| Glossary spelling | Spelling in the rankings |')
    w('|---|---|')
    for g, hit in translit.items():
        w(f'| {g} | `{hit}` |')
    w('')
    w('These are the *same terms*, so the exact-match figures in &sect;1 are conservative by '
      f'roughly {len(translit)} terms. Normalising transliteration on ingest would be the single '
      'highest-value fix to the extraction pipeline.')
    w('')

    # ---------------- gaps ----------------
    w('## 9. Terms no method finds')
    w('')
    missing = sorted(set(glossary) - any_cov)
    strict_missing = sorted(set(glossary) - (ye | te | fe))
    w(f'{len(missing)} glossary terms are absent from all three rankings under any tier '
      f'({len(strict_missing)} under exact match alone).')
    w('')
    translit_missing = [m for m in missing if m in translit]
    true_missing = [m for m in missing if m not in translit]
    if translit_missing:
        w(f'**Spelling variants ({len(translit_missing)})** &mdash; present in the text, missed by '
          'string matching (see &sect;8):')
        w('')
        w('> ' + ', '.join(f'`{t}`' for t in translit_missing))
        w('')
    w(f'**Not matched by any spelling rule ({len(true_missing)})** &mdash; mostly proper nouns that '
      'fall below the minimum-count thresholds, or that belong to material the glossary covers '
      'but this text does not:')
    w('')
    w('> ' + ', '.join(f'`{t}`' for t in true_missing))
    w('')
    w('A few of these are not truly absent, just unreachable by the folding rules used here. '
      '`Shri Singha` appears as `sri simha` (a different nasal, *ngh* vs *mh*), and '
      '`Shantarakshita` survives only as the truncated token `santarak`. Terms such as '
      '`Chenrezi`, `Garuda`, `Nalanda` and `Yaksha` have no near-form anywhere in the three '
      'rankings and are genuinely missing from the extracted vocabulary.')
    w('')

    # ---------------- conclusions ----------------
    w('## 10. What this means')
    w('')
    w('**The three methods are far more alike than different.** They draw on one shared unigram '
      f'vocabulary: {len(ye & te & fe)} glossary terms are matched exactly by all three '
      f'({len(all_cov)} once partial tiers count), and neither TF-IDF nor the fused list finds a '
      'single term the others miss. Any claim that one method dramatically outperforms another on '
      'this data is an artifact.')
    w('')
    w('**YAKE\'s value is phrases, not volume.** It ranks the fewest terms '
      f'({len(methods["YAKE"].terms):,} vs {tf_pure:,}) and has the lowest raw coverage, but it is '
      f'the only method contributing unique exact matches ({len(ye - te - fe)}), all multi-word. '
      'For a glossary that is 57% multi-word entries, that capability is not optional.')
    w('')
    w('**The fused method does its job.** Its coverage matches TF-IDF while its ranking places '
      'more glossary terms in the top few hundred than either input alone. Fusion improved the '
      'ordering, which is what RRF optimises &mdash; it was never going to expand the vocabulary.')
    w('')
    w('**Exact-match coverage is the honest headline: about '
      f'{fmt_pct(len(ye | te | fe), total)} of the glossary, rising to '
      f'{fmt_pct(len(any_cov), total)} only if loose single-word overlap is counted.** The gap '
      'between those figures is the real state of things, and the two biggest recoverable losses '
      f'are transliteration variance ({len(translit)} terms) and multi-word entries that only '
      'n-gram extraction can reach.')
    w('')

    # ---------------- corrections ----------------
    w('## Corrections to the previous report')
    w('')
    w('The prior `CORRELATION_REPORT.md` was generated by a script version with three defects, '
      'all fixed in `analyze_correlation.py`:')
    w('')
    w('| Defect | Effect |')
    w('|---|---|')
    w('| A lazy regex `(.+?)` followed only by optional groups captured **one character** per '
      'numbered-list row | Injected single letters (`a`, `s`, `h`, &hellip;) into the term sets |')
    w('| Partial matching used bare substring tests in both directions | Every single letter '
      'matched every glossary term, so "partial" was ~100% noise |')
    w('| The separator row `\\| ----- \\|` was parsed as a glossary entry | Term count inflated to '
      f'532; the true count is {total} |')
    w('')
    w('Corrected headline figures: TF-IDF matches '
      f'{len(te)} glossary terms exactly ({fmt_pct(len(te), total)}) and reaches '
      f'{fmt_pct(len(covered(results["TF-IDF (pure unigram)"])), total)} once partial tiers count '
      f'&mdash; not 0.2%. And {len(ye & te & fe)} terms are matched exactly by all three methods '
      f'({len(all_cov)} under any tier), not 0.')
    w('')
    w('---')
    w('')
    w(f'Generated by `analyze_correlation.py` from `glossary.md`, `en-n-gram-keyword.json`, '
      f'`en-tfidf.md` and `en-keywords-fused-pmi.md`. Full matched-term lists: `{DUMP.name}`.')
    w('')

    return '\n'.join(out)


def build_summary(glossary, methods, results, translit):
    """Short, plain-language version. Same numbers, no jargon, one TF-IDF column."""
    total = len(glossary)
    out = []
    w = out.append

    names = list(PRIMARY)
    y, t, f = (covered(results[n]) for n in names)
    ye, te, fe = (set(results[n]['exact']) for n in names)
    single = sum(1 for g in glossary if len(tokenize(g)) == 1)

    w('# Glossary Coverage: YAKE vs TF-IDF vs Combined')
    w('')
    w(f'We took the **{total} English terms** in `glossary.md` ({single} single words, '
      f'{total - single} phrases) and checked how many of them each keyword method actually found.')
    w('')
    w('---')
    w('')

    # 1 -------------------------------------------------------------
    w('## 1. The answer')
    w('')
    w('| Method | Keywords it produced | Found exactly | Found inside a longer keyword | '
      'Only part of it found | **Total found** | **Coverage** |')
    w('|---|---:|---:|---:|---:|---:|---:|')
    for key in names:
        b = results[key]
        ex, pf, pr = (len(b[k]) for k in ('exact', 'partial_fwd', 'partial_rev'))
        tot = ex + pf + pr
        w(f'| {PRIMARY[key]} | {len(methods[key].terms):,} | {ex} | {pf} | {pr} | '
          f'**{tot}** | **{fmt_pct(tot, total)}** |')
    w('')
    w('**Read the last column with care.** Those 78&ndash;91% figures lean heavily on the weakest '
      'kind of match &mdash; "only part of it found", where a single word like `absolute` is '
      'counted as covering the glossary entry *Absolute space*. That is not really finding the '
      'term.')
    w('')
    solid = {k: len(results[k]['exact']) + len(results[k]['partial_fwd']) for k in names}
    w('If you drop that column and count only the two real kinds of match, coverage is '
      + ', '.join(f'**{fmt_pct(solid[k], total)} for {PRIMARY[k]}**' for k in names)
      + '. Those are the honest numbers.')
    w('')

    # 2 -------------------------------------------------------------
    w('## 2. What counts as a match')
    w('')
    w('| Result | What it means | Example |')
    w('|---|---|---|')
    w('| **Found exactly** | the keyword is the glossary term | glossary *Bodhicitta* &rarr; keyword `bodhicitta` |')
    w('| **Inside a longer keyword** | the whole glossary term sits inside a bigger keyword | glossary *Amitayus* &rarr; keyword `buddha protector amitayus` |')
    w('| **Only part of it found** | just one word of a multi-word glossary term turned up | glossary *Absolute space* &rarr; keyword `absolute` |')
    w('| **Not found** | nothing matched | glossary *Chenrezi* |')
    w('')
    w('The first two are real hits. The third is weak evidence and is kept in its own column so it '
      'never gets mistaken for the others.')
    w('')
    w('This also explains the zeros in the "inside a longer keyword" column above. **TF-IDF ranks '
      'single words only**, and a single word cannot contain a two-word glossary phrase. Combined '
      'keeps just 310 phrases out of 7,978, so it has almost nothing longer to match against '
      'either. YAKE is the only method producing phrases in quantity.')
    w('')

    # 3 -------------------------------------------------------------
    w('## 3. The three methods mostly agree')
    w('')
    w('| | Exact matches only | Counting every kind of match |')
    w('|---|---:|---:|')
    w(f'| Found by all three methods | {len(ye & te & fe)} | {len(y & t & f)} |')
    w(f'| Found by at least one | {len(ye | te | fe)} | {len(y | t | f)} |')
    w(f'| Found by none | {total - len(ye | te | fe)} | {total - len(y | t | f)} |')
    w('')
    only_yake = sorted(ye - te - fe)
    w(f'They are not really competing methods &mdash; they draw on the same vocabulary. '
      f'**TF-IDF and Combined find nothing that the others miss.** Only YAKE contributes anything '
      f'unique: {len(only_yake)} terms, every one of them a phrase:')
    w('')
    w('> ' + ', '.join(f'*{term}*' for term in only_yake))
    w('')
    w('That is the practical case for keeping YAKE: **'
      f'{fmt_pct(total - single, total)} of the glossary is multi-word**, and a single-word method '
      'can never reach those entries.')
    w('')

    # 4 -------------------------------------------------------------
    w('## 4. Which method puts glossary terms near the top?')
    w('')
    w('Coverage only asks whether a term appears somewhere in a list of thousands. This asks '
      'something more useful: if you read the top of each list, how many glossary terms do you get?')
    w('')
    ks = (100, 500, 2000)
    w('| Method | ' + ' | '.join(f'in the top {k:,}' for k in ks) + ' |')
    w('|---|' + '---:|' * len(ks))
    gkeys = {tokenize(g) for g in glossary}
    for key in names:
        cells = [f'{methods[key].precision_at(gkeys, k)}' for k in ks]
        w(f'| {PRIMARY[key]} | ' + ' | '.join(cells) + ' |')
    w('')
    w('All three are similar in the first 100. Deeper down, **Combined stays richest in glossary '
      'terms** &mdash; which is exactly what merging the two rankings was supposed to achieve. It '
      'did not find *more* terms than TF-IDF, but it orders them better.')
    w('')

    # 5 -------------------------------------------------------------
    w('## 5. What was missed, and why')
    w('')
    missing = sorted(set(glossary) - (y | t | f))
    translit_missing = [m for m in missing if m in translit]
    true_missing = [m for m in missing if m not in translit]
    w(f'{len(missing)} glossary terms were not found by any method. They split into two very '
      'different groups.')
    w('')
    w(f'**{len(translit_missing)} are just spelling differences.** The glossary and the source '
      'text romanise Sanskrit names differently &mdash; the glossary writes `sh` where the text '
      'writes `s`. These terms *are* in the text; the matching simply could not see them:')
    w('')
    w('| Glossary spells it | The text spells it |')
    w('|---|---|')
    for term, hit in list(translit.items())[:6]:
        w(f'| {term} | `{hit}` |')
    w(f'| &hellip;and {len(translit) - 6} more | |')
    w('')
    w('**Fixing this is the single most valuable change to the pipeline** &mdash; it recovers '
      f'{len(translit)} terms for one normalisation rule.')
    w('')
    w(f'**{len(true_missing)} are genuinely absent** from the extracted keywords, such as '
      '*Chenrezi*, *Garuda*, *Nalanda* and *Yaksha*. These are mostly rare proper nouns that fall '
      'below the minimum-frequency cutoffs, or belong to material the glossary covers but this '
      'text does not. (Two near-misses: *Shri Singha* is present as `sri simha`, and '
      '*Shantarakshita* only as the cut-off token `santarak`.)')
    w('')

    # 6 -------------------------------------------------------------
    w('## 6. Bottom line')
    w('')
    w(f'- **The three methods are far more alike than different.** {len(ye & te & fe)} glossary '
      'terms are found exactly by all three, and two of the three add nothing unique.')
    w('- **Keep YAKE for phrases.** It produces the fewest keywords and the lowest coverage, but '
      'it is the only method that can reach the 57% of the glossary that is multi-word.')
    w('- **Combined is the best-ordered list.** Same coverage as TF-IDF, but more glossary terms '
      'near the top &mdash; use it if you want a ranked shortlist.')
    w(f'- **Put all three together and they match {fmt_pct(len(ye | te | fe), total)} of the '
      f'glossary exactly &mdash; not 91%.** The difference is weak part-word matches, plus '
      f'{len(translit)} terms lost to spelling alone.')
    w('')
    w('---')
    w('')
    w('*Note: `en-tfidf.md` contains 9,190 rows, but only the 7,632 with an actual TF-IDF score '
      'are used here as "TF-IDF" &mdash; the other 1,558 are YAKE phrases stored in the same '
      'table.*')
    w('')
    w('*Full detail: `CORRELATION_REPORT.md`. Every matched term, one per line: '
      '`correlation_analysis_results.txt`.*')
    w('')

    return '\n'.join(out)


def build_dump(glossary, results):
    out = []
    w = out.append
    w('FULL MATCH LISTS - glossary terms vs keyword rankings')
    w('=' * 72)
    w(f'Glossary terms: {len(glossary)}')
    w('')
    for name, buckets in results.items():
        w('')
        w('=' * 72)
        w(name)
        w('=' * 72)
        for tier, label in [('exact', 'EXACT'),
                            ('partial_fwd', 'PARTIAL - forward (glossary term inside ranked term)'),
                            ('partial_rev', 'PARTIAL - reverse (ranked term inside glossary term)')]:
            items = buckets[tier]
            w('')
            w(f'{label}: {len(items)}')
            w('-' * 72)
            for g, hit in items.items():
                w(f'  {g:<52} <- {hit}')
        w('')
        w(f'NOT FOUND: {len(buckets["none"])}')
        w('-' * 72)
        for g in buckets['none']:
            w(f'  {g}')
    return '\n'.join(out)


# --------------------------------------------------------------------------

def main():
    glossary = load_glossary(GLOSSARY)
    assert len(glossary) == 531, f'expected 531 glossary terms, got {len(glossary)}'

    yake_terms = load_yake(YAKE_JSON)

    tfidf_rows = load_ranked_table(TFIDF_MD, '| Rank | Term | Count')
    # Rows without a TF-IDF score are YAKE phrases appended to the same table.
    tfidf_pure = [r[2].replace('**', '') for r in tfidf_rows if r[4] != '-']
    tfidf_file = [r[2].replace('**', '') for r in tfidf_rows]
    assert len(tfidf_pure) == 7632, f'expected 7632 TF-IDF unigrams, got {len(tfidf_pure)}'
    assert len(tfidf_file) - len(tfidf_pure) == 1558

    fused_rows = load_ranked_table(FUSED_MD, '| Rank | Term | W |')
    fused_terms = [r[2].replace('**', '') for r in fused_rows]
    assert len(fused_terms) == 7978, f'expected 7978 fused terms, got {len(fused_terms)}'

    # Regression guard on the old single-character parsing bug.
    for label, terms in [('yake', yake_terms), ('tfidf', tfidf_file), ('fused', fused_terms)]:
        stubs = [t for t in terms if len(t.strip()) < 2]
        assert not stubs, f'{label}: single-character terms leaked in: {stubs[:10]}'

    methods = OrderedDict()
    methods['YAKE'] = Method('YAKE', yake_terms)
    methods['TF-IDF (pure unigram)'] = Method('TF-IDF (pure unigram)', tfidf_pure)
    methods['TF-IDF (file as published)'] = Method('TF-IDF (file as published)', tfidf_file)
    methods['Fused / Combined'] = Method('Fused / Combined', fused_terms)

    results = OrderedDict((name, analyze(m, glossary)) for name, m in methods.items())

    # Terms recoverable only once Sanskrit romanisation is folded.
    translit = OrderedDict()
    unfound = set(glossary)
    for buckets in results.values():
        unfound &= set(buckets['none'])
    for term in glossary:
        if term not in unfound:
            continue
        for name in ['YAKE', 'TF-IDF (file as published)', 'Fused / Combined']:
            hit = methods[name].folded_exact(term)
            if hit:
                translit[term] = hit
                break

    checks = {
        'tfidf': glossary_check_counts(TFIDF_MD, '| Rank | Term | Count'),
        'fused': glossary_check_counts(FUSED_MD, '| Rank | Term | W |'),
    }

    REPORT.write_text(build_report(glossary, methods, results, translit, checks), encoding='utf-8')
    SUMMARY.write_text(build_summary(glossary, methods, results, translit), encoding='utf-8')
    DUMP.write_text(build_dump(glossary, results), encoding='utf-8')

    total = len(glossary)
    print(f'Glossary terms: {total}\n')
    print(f'{"method":<28}{"terms":>8}{"exact":>7}{"p-fwd":>7}{"p-rev":>7}{"total":>7}{"cover":>9}')
    for name, buckets in results.items():
        ex, pf, pr = (len(buckets[k]) for k in ('exact', 'partial_fwd', 'partial_rev'))
        tot = ex + pf + pr
        print(f'{name:<28}{len(methods[name].terms):>8,}{ex:>7}{pf:>7}{pr:>7}{tot:>7}'
              f'{tot / total * 100:>8.1f}%')
    print(f'\nRecoverable via transliteration folding: {len(translit)}')
    print(f'\nWrote {SUMMARY.name}, {REPORT.name} and {DUMP.name}')


if __name__ == '__main__':
    main()
