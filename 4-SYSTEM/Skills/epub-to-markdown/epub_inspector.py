#!/usr/bin/env python3
"""
epub_inspector.py
-----------------
Analyses an EPUB file and outputs a structured JSON profile that Claude uses
to decide whether an existing custom converter already covers this publisher,
or whether to generate a new one.

Output (stdout, JSON):
  publisher        - DC publisher string or null
  title            - DC title
  title_en         - calibre:title_sort if present (often the English title)
  author           - DC creator
  language         - DC language code
  date             - DC date
  source_id        - BookId identifier (uuid/urn)
  sigil_version    - Sigil version used to build epub, if present
  publisher_slug   - filesystem-safe slug derived from publisher name
  css_classes      - list of {name, color, element_count, sample_text, suggested_callout}
  heading_colors   - dict of h1..h6 color values found in CSS
  spine_docs       - list of spine document filenames in order
  toc              - nested list of {title, href, children}
  all_metadata     - raw dump of all DC and OPF metadata

Usage:
  python epub_inspector.py path/to/book.epub
"""

import json
import re
import sys
import unicodedata
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


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
    """Return dict of name->content from OPF <meta> tags."""
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
    """
    Parse all stylesheet items and return:
      {class_name: {color, element_count, sample_texts}}
    Also returns heading_colors {h1: color, ...}.
    """
    raw_css = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_STYLE:
            raw_css += item.get_content().decode('utf-8', errors='replace') + '\n'

    # Extract class rules: .classname { ... color: #xxx ... }
    class_rules = {}
    heading_colors = {}

    for block_match in re.finditer(r'([^{]+)\{([^}]+)\}', raw_css):
        selector = block_match.group(1).strip()
        body = block_match.group(2)
        color_match = re.search(r'color\s*:\s*([^;]+)', body, re.IGNORECASE)
        if not color_match:
            continue
        color = color_match.group(1).strip().rstrip(';').strip()

        # Heading selectors
        for h in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if re.fullmatch(rf'\s*{h}\s*', selector):
                heading_colors[h] = color

        # Class selectors
        for cls_match in re.finditer(r'\.([\w-]+)', selector):
            cls_name = cls_match.group(1)
            class_rules[cls_name] = {'color': color}

    # Count elements and collect samples from spine
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

    # Build output list, only classes that actually appear in content
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
            'suggested_callout': None,  # Claude fills this in
        })

    result.sort(key=lambda x: -x['element_count'])
    return result, heading_colors


# ---------------------------------------------------------------------------
# TOC
# ---------------------------------------------------------------------------

def flatten_toc(toc, depth=0):
    entries = []
    for entry in toc:
        if isinstance(entry, epub.Link):
            entries.append({'title': entry.title, 'href': entry.href, 'depth': depth, 'children': []})
        elif isinstance(entry, tuple):
            section, children = entry
            node = {'title': section.title if hasattr(section, 'title') else str(section),
                    'href': section.href if hasattr(section, 'href') else None,
                    'depth': depth,
                    'children': flatten_toc(children, depth + 1)}
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

    # All raw metadata for reference
    all_metadata = {}
    for ns, items in book.metadata.items():
        for key, values in items.items():
            for val, attrs in values:
                all_metadata[f"{ns}#{key}"] = {'value': val, 'attrs': attrs}

    # Identifiers
    source_id = None
    for val, attrs in book.get_metadata('DC', 'identifier') or []:
        if 'BookId' in str(attrs.get('id', '')):
            source_id = val
            break
    if not source_id:
        ids = book.get_metadata('DC', 'identifier')
        if ids:
            source_id = ids[0][0]

    profile = {
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
        'spine_docs': [book.get_item_with_id(iid).get_name()
                       for iid, _ in book.spine
                       if book.get_item_with_id(iid)],
        'toc': flatten_toc(book.toc),
    }

    return profile


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: epub_inspector.py <epub_path>', file=sys.stderr)
        sys.exit(1)
    profile = inspect_epub(sys.argv[1])
    print(json.dumps(profile, ensure_ascii=False, indent=2))
