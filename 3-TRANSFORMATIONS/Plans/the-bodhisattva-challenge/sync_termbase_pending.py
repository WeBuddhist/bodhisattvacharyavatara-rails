"""Append-only sync of day-file `pending_terms:` into both termbase Pending tables.
Run from the-bodhisattva-challenge/ :  python3 sync_termbase_pending.py
Only adds rows whose Tibetan key is not already in the table; never rewrites existing rows.
Check `git diff` afterwards: it must be purely additive."""
import re, os, glob

def day_num(path):
    m = re.match(r'(\d+)-', os.path.basename(path))
    return int(m.group(1)) if m else None

def extract_pending(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    fm = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm:
        return []
    m = re.search(r'pending_terms:\s*(\[\])?\n?((?:\s*-\s*"[^"]*"\n?)*)', fm.group(1))
    if not m or m.group(1) == '[]':
        return []
    return re.findall(r'-\s*"([^"]*)"', m.group(2))

def build_entries(lang):
    entries = {}
    for path in glob.glob(os.path.join(lang, 'Days', '*', '*.md')):
        d = day_num(path)
        if d is None:
            continue
        for t in extract_pending(path):
            tib, ren = (t.split('→', 1) + [''])[:2] if '→' in t else (t, '')
            tib, ren = tib.strip(), ren.strip()
            if tib not in entries or d < entries[tib][0]:
                entries[tib] = (d, ren)
    return entries

HEADINGS = {'en': '## Pending terms', 'hi': '## लंबित शब्द'}
STATUS = {'en': 'pending', 'hi': 'लंबित'}

for lang in ('en', 'hi'):
    entries = build_entries(lang)
    tb_path = os.path.join(lang, 'termbase-translation.md')
    with open(tb_path, encoding='utf-8') as f:
        lines = f.readlines()
    h = next((i for i, l in enumerate(lines) if l.strip() == HEADINGS[lang]), None)
    if h is None:
        raise SystemExit(f"{lang}: heading {HEADINGS[lang]!r} not found")
    hdr = next((i for i in range(h, len(lines))
                if lines[i].strip().startswith('|') and ('Tibetan' in lines[i] or 'तिब्बती' in lines[i])), None)
    if hdr is None:
        raise SystemExit(f"{lang}: table header not found")
    start = hdr + 2
    end = start
    existing = set()
    while end < len(lines) and lines[end].strip().startswith('|'):
        existing.add(lines[end].split('|')[1].strip())
        end += 1
    new = [(t, d, r) for t, (d, r) in sorted(entries.items(), key=lambda kv: kv[1][0]) if t not in existing]
    if not new:
        print(f"{lang}: nothing new")
        continue
    sample = lines[end - 1] if end > start else ''
    padded = re.search(r'  +\|', sample) is not None
    rows = []
    if padded:
        widths = [len(c.strip()) for c in lines[hdr].strip().strip('|').split('|')]
        for t, d, r in new:
            widths = [max(w, len(v)) for w, v in zip(widths, [t, r, f"Day {d}", STATUS[lang]])]
        for t, d, r in new:
            rows.append("| " + " | ".join(v.ljust(w) for v, w in zip([t, r, f"Day {d}", STATUS[lang]], widths)) + " |\n")
    else:
        rows = [f"| {t} | {r} | Day {d} | {STATUS[lang]} |\n" for t, d, r in new]
    with open(tb_path, 'w', encoding='utf-8') as f:
        f.writelines(lines[:end] + rows + lines[end:])
    print(f"{lang}: appended {len(new)} row(s)")
