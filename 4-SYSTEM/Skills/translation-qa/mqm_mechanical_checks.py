#!/usr/bin/env python3
"""
mqm_mechanical_checks.py - Stage 0 of the translation-qa skill.

Runs the DETERMINISTIC MQM checks on a translation file: the things a script can
decide without judgement (Markup/BlockID and Accuracy/Omission dimensions). It
catches structural defects a holistic read misses: mislabeled verse IDs, dropped
verses, untranslated spans, stray latin, CRLF.

It does NOT judge meaning, terminology, fluency, or register - that is Stage 1
(LLM, line by line, against the rails). Run this first; feed its findings into
qa-report.md alongside the Stage 1 annotations.

Usage:
    python3 mqm_mechanical_checks.py TRANSLATION.md [--source SOURCE.md] [--json OUT.json]
"""
import argparse
import json
import re
import sys

BLOCK_RE = re.compile(r'\^([A-Za-z0-9]+-[A-Za-z0-9]+)\s*$')
TRANSCLUDE_RE = re.compile(r'^!\[\[.*?#\^([A-Za-z0-9]+-[A-Za-z0-9]+)\]\]')
LATIN_RE = re.compile(r'[A-Za-z]')


def is_heading_id(vid):
    return vid.split('-')[-1] == '0'


def read_lines(path):
    raw = open(path, encoding='utf-8').read()
    crlf = '\r\n' in raw
    return raw.replace('\r\n', '\n').replace('\r', '\n').split('\n'), crlf


def parse(path):
    lines, crlf = read_lines(path)
    transclusions = []
    body_ids = []
    records = []
    untranslated = []
    stray_latin = []
    pending = None
    buf = []
    fm = False
    for i, s in enumerate(lines, 1):
        stripped = s.strip()
        if i == 1 and stripped == '---':
            fm = True
            continue
        if fm:
            if stripped == '---':
                fm = False
            continue
        tm = TRANSCLUDE_RE.match(s)
        if tm:
            if pending is not None:
                records.append({'transclusion': pending, 'body_id': None,
                                'lines': len([b for b in buf if b.strip()])})
            pending = tm.group(1)
            transclusions.append(pending)
            buf = []
            continue
        if stripped.startswith('#') or stripped == '':
            continue
        bm = BLOCK_RE.search(s)
        text = BLOCK_RE.sub('', s).strip()
        if text:
            buf.append(text)
            if LATIN_RE.search(text) and 'UNTRANSLATED' not in text:
                stray_latin.append((i, text[:60]))
            if 'UNTRANSLATED' in text and pending:
                untranslated.append(pending)
        if bm and not is_heading_id(bm.group(1)):
            vid = bm.group(1)
            body_ids.append(vid)
            records.append({'transclusion': pending, 'body_id': vid,
                            'lines': len([b for b in buf if b.strip()])})
            pending = None
            buf = []
    if pending is not None:
        records.append({'transclusion': pending, 'body_id': None,
                        'lines': len([b for b in buf if b.strip()])})
    return {'records': records, 'transclusions': transclusions,
            'body_ids': body_ids, 'untranslated': untranslated,
            'stray_latin': stray_latin, 'crlf': crlf}


def source_ids(path):
    lines, _ = read_lines(path)
    ids = []
    for s in lines:
        m = BLOCK_RE.search(s)
        if m and not is_heading_id(m.group(1)):
            ids.append(m.group(1))
    return ids


def analyse(path, source=None):
    p = parse(path)
    findings = []
    for r in p['records']:
        t, b = r['transclusion'], r['body_id']
        if t is None:
            continue
        if b is None:
            findings.append({'severity': 'critical', 'dimension': 'Accuracy/Omission',
                             'verse': t, 'detail': 'transclusion ^%s has no translated body / no body block ID' % t})
        elif b != t:
            findings.append({'severity': 'critical', 'dimension': 'Markup/BlockID',
                             'verse': t, 'detail': 'body under transclusion ^%s is tagged ^%s (mislabeled)' % (t, b)})
    seen = {}
    for v in p['body_ids']:
        seen[v] = seen.get(v, 0) + 1
    for v, n in seen.items():
        if n > 1:
            findings.append({'severity': 'major', 'dimension': 'Markup/BlockID',
                             'verse': v, 'detail': 'block ID ^%s appears %d times' % (v, n)})
    if source:
        src = source_ids(source)
        have = set(p['body_ids']) | set(p['transclusions'])
        for v in src:
            if v not in have:
                findings.append({'severity': 'critical', 'dimension': 'Accuracy/Omission',
                                 'verse': v, 'detail': 'verse ^%s in source is absent from translation' % v})
    for v in p['untranslated']:
        findings.append({'severity': 'critical', 'dimension': 'Accuracy/Untranslated',
                         'verse': v, 'detail': 'contains UNTRANSLATED placeholder'})
    for ln, txt in p['stray_latin']:
        findings.append({'severity': 'minor', 'dimension': 'LocaleConvention',
                         'verse': 'line %d' % ln, 'detail': 'latin characters in content: "%s"' % txt})
    if p['crlf']:
        findings.append({'severity': 'minor', 'dimension': 'Markup/Format',
                         'verse': '(file)', 'detail': 'file uses CRLF line endings (vault standard is LF)'})
    counts = {'critical': 0, 'major': 0, 'minor': 0}
    for f in findings:
        counts[f['severity']] += 1
    return {'file': path, 'verse_count': len(set(p['body_ids'])),
            'transclusion_count': len(p['transclusions']), 'counts': counts,
            'gate_stage0': 'FAIL' if (counts['critical'] or counts['major']) else 'PASS-so-far',
            'findings': findings}


def render(result):
    out = []
    out.append("# Stage 0 mechanical checks - %s\n" % result['file'])
    out.append("- Distinct verse IDs: **%d**" % result['verse_count'])
    out.append("- Transclusions: **%d**" % result['transclusion_count'])
    c = result['counts']
    out.append("- Findings: **%d critical, %d major, %d minor**" % (c['critical'], c['major'], c['minor']))
    out.append("- Stage-0 gate: **%s**  (any critical/major here is an automatic FAIL regardless of Stage 1)\n" % result['gate_stage0'])
    if result['transclusion_count'] == 0:
        out.append("> No transclusions found - this file inlines its verses. The transclusion-vs-body "
                   "mislabel check is skipped; omission/mislabel detection relies on --source coverage + "
                   "duplicate-ID checks, so always pass --source for an inlined file.\n")
    if not result['findings']:
        out.append("No mechanical issues found. Proceed to Stage 1 (semantic MQM).")
    else:
        out.append("| Severity | Dimension | Verse | Detail |")
        out.append("|---|---|---|---|")
        order = {'critical': 0, 'major': 1, 'minor': 2}
        for f in sorted(result['findings'], key=lambda x: order[x['severity']]):
            out.append("| %s | %s | %s | %s |" % (f['severity'].upper(), f['dimension'], f['verse'], f['detail']))
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('translation')
    ap.add_argument('--source', help='source file to check verse coverage against')
    ap.add_argument('--json', help='also write machine-readable JSON here')
    args = ap.parse_args()
    res = analyse(args.translation, args.source)
    print(render(res))
    if args.json:
        json.dump(res, open(args.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print("\n[JSON written to %s]" % args.json, file=sys.stderr)


if __name__ == '__main__':
    main()
