#!/usr/bin/env python3
"""
epub_inspector.py
-----------------
Analyses an EPUB and outputs a structured JSON profile Claude uses to decide
whether an existing custom converter covers this publisher, or whether to
generate a new one.

Key output fields:
  publisher / publisher_slug   - identifies which converter to reuse
  css_classes                  - all semantic CSS classes with colour, count, samples
  mixed_class_patterns         - paragraphs where inline <span> overrides parent <p>
                                 class mid-sentence (requires run-based converter)
  heading_colors               - h1..h6 colour values
  toc                          - structured table of contents
  spine_docs                   - ordered content documents

Usage:
  python epub_inspector.py path/to/book.epub
"""

import json
import re
import sys
import unicodedata
from collections import defaultdict
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString


SEMANTIC_CLASSES = {'root', 'lung', 'bold', 'normal'}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text):
    text = str(text).lower().strip()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text or 'unknown'


def dc(book, key):
    raw = book.get_metadata('DC', key)
    return raw[0][0] if raw else None


def opf_meta(book):
    result = {}
    for val, attrs in book.metadata.get('http://www.idpf.org/2007/opf', {}).get('meta', []):
        name = attrs.get('name') or attrs.get('property')
        content = attrs.get('content') or val
        if name:
            result[name] = content
    return result


# ---------------------------------------------------------------------------
# CSS analysis
# ---------------------------------------------------------------------------

def parse_css_classes(book):
    raw_css = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_STYLE:
            raw_css += item.get_content().decode('utf-8', errors='replace') + '\n'

    class_rules = {}
    heading_colors = {}

    for block_match in re.finditer(r'([^{]+)\{([^}]+)\}', raw_css):
        selector = block_match.group(1).strip()
        body = block_match.group(2)
        color_match = re.search(r'color\s*:\s*([^;]+)', body, re.IGNORECASE)
        if not color_match:
            continue
        color = color_match.group(1).strip().rstrip(';').strip()

        for h in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if re.fullmatch(rf'\s*{h}\s*', selector):
                heading_colors[h] = color

        for cls_match in re.finditer(r'\.([\w-]+)', selector):
            class_rules[cls_match.group(1)] = {'color': color}

    class_counts = {k: 0 for k in class_rules}
    class_samples = {k: [] for k in class_rules}

    for item_id, _ in book.spine:
        item = book.get_item_with_id(item_id)
        if item and item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for el in soup.find_all(True):
                for cls in el.get('class', []):
                    if cls in class_rules:
                        class_counts[cls] = class_counts.get(cls, 0) + 1
                        if len(class_samples.get(cls, [])) < 3:
                            sample = el.get_text()[:120].strip().replace('\n', ' ')
                            if sample:
                                class_samples.setdefault(cls, []).append(sample)

    result = []
    for cls, rule in class_rules.items():
        count = class_counts.get(cls, 0)
        if count == 0:
            continue
        result.append({
            'name': cls,
            'color': rule['color'],
            'element_count': count,
            'sample_texts': class_samples.get(cls, []),
            'suggested_callout': None,
        })

    result.sort(key=lambda x: -x['element_count'])
    return result, heading_colors


# ---------------------------------------------------------------------------
# Mixed-class paragraph detection
# ---------------------------------------------------------------------------

def find_mixed_class_paragraphs(book):
    """
    Detect <p> elements where inline <span> children carry a DIFFERENT semantic
    class from the parent <p> (or introduce a semantic class into an unclassed <p>).

    This signals that the epub uses sub-paragraph colour coding: semantic colour
    can apply to partial sentences, trailing connectives, or embedded labels.
    A paragraph-level callout approach will merge content incorrectly; the
    converter must use a run-based approach instead.

    Common patterns found in Tibetan Buddhist EPUBs:
      <p class=lung> + <span class=normal>
          Citation paragraph ending with a plain-text connective like
          'ཞེས་དང༌།' or 'ཞེས་སོ།།'. The connective should be plain text,
          not inside the [!lung] callout.
      <p class=plain> + <span class=bold>
          Outline label (blue) at the start of a commentary paragraph.
          Should be split into [!toc] callout + plain commentary.

    Returns list of {pattern, count, samples} sorted by frequency.
    """
    pattern_counts = defaultdict(int)
    pattern_samples = defaultdict(list)

    for item_id, _ in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        body = soup.find('body')
        if not body:
            continue
        for p in body.find_all('p'):
            p_sem = set(p.get('class', [])) & SEMANTIC_CLASSES
            inline_sems = set()
            for child in p.children:
                if not hasattr(child, 'get'):
                    continue
                span_sem = set(child.get('class', [])) & SEMANTIC_CLASSES
                if span_sem and span_sem != p_sem:
                    inline_sems.update(span_sem)
            if not inline_sems:
                continue
            p_label = ','.join(sorted(p_sem)) if p_sem else 'plain'
            span_label = ','.join(sorted(inline_sems))
            pattern = '<p class=' + p_label + '> contains inline <span class=' + span_label + '>'
            pattern_counts[pattern] += 1
            if len(pattern_samples[pattern]) < 2:
                pattern_samples[pattern].append(p.get_text()[:120].strip())

    return [
        {'pattern': pat, 'count': cnt, 'samples': pattern_samples[pat]}
        for pat, cnt in sorted(pattern_counts.items(), key=lambda x: -x[1])
    ]


# ---------------------------------------------------------------------------
# TOC
# ---------------------------------------------------------------------------

def flatten_toc(toc, depth=0):
    entries = []
    for entry in toc:
        if isinstance(entry, epub.Link):
            entries.append({
                'title': entry.title,
                'href': entry.href,
                'depth': depth,
                'children': []
            })
        elif isinstance(entry, tuple):
            section, children = entry
            node = {
                'title': section.title if hasattr(section, 'title') else str(section),
                'href': section.href if hasattr(section, 'href') else None,
                'depth': depth,
                'children': flatten_toc(children, depth + 1)
            }
            entries.append(node)
    return entries


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def inspect_epub(epub_path):
    book = epub.read_epub(epub_path)
    meta = opf_meta(book)
    publisher = dc(book, 'publisher')

    css_classes, heading_colors = parse_css_classes(book)
    mixed_class_patterns = find_mixed_class_paragraphs(book)

    source_id = None
    for val, attrs in book.get_metadata('DC', 'identifier') or []:
        if 'BookId' in str(attrs.get('id', '')):
            source_id = val
            break
    if not source_id:
        ids = book.get_metadata('DC', 'identifier')
        if ids:
            source_id = ids[0][0]

    return {
        'publisher': publisher,
        'publisher_slug': slugify(publisher) if publisher else 'unknown',
        'title': dc(book, 'title'),
        'title_en': meta.get('calibre:title_sort'),
        'author': dc(book, 'creator'),
        'language': dc(book, 'language'),
        'date': dc(book, 'date'),
        'source_id': source_id,
        'sigil_version': meta.get('Sigil version'),
        'css_classes': css_classes,
        'heading_colors': heading_colors,
        'mixed_class_patterns': mixed_class_patterns,
        'spine_docs': [
            book.get_item_with_id(iid).get_name()
            for iid, _ in book.spine
            if book.get_item_with_id(iid)
        ],
        'toc': flatten_toc(book.toc),
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: epub_inspector.py <epub_path>', file=sys.stderr)
        sys.exit(1)
    profile = inspect_epub(sys.argv[1])
    print(json.dumps(profile, ensure_ascii=False, indent=2))
