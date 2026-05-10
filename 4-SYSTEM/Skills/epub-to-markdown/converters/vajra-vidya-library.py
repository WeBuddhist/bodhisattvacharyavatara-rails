#!/usr/bin/env python3
"""
Converter: Vajra Vidya Library
Generated: 2026-05-10
Template:  epub_to_markdown.py

Publisher profile:
  Vajra Vidya Library (Sarnath / Hong Kong)
  Tibetan Buddhist texts typeset in Sigil, distributed via Thrangu Vajravidya.

CSS class → callout mapping for this publisher:
  .root  (#BB5500, orange-red) → > [!root]   Root text verses (Skt/Tib source stanzas)
  .lung  (#7D6608, dark gold)  → > [!lung]   Scriptural citations (lung = canonical quote)
  .bold  (#003377, blue)       → > [!toc]    TOC enumeration / outline items
  .normal (#000000, black)     → plain text  Ordinary body paragraphs (no callout)

Additional metadata extracted vs. generic script:
  publisher, title_en (from calibre:title_sort), source_id (BookId URN)

Structure:
  TOC injected after frontmatter.
  Horizontal rule + H2 chapter heading inserted between spine documents
  when the document matches a known chapter file (Chapter\d+.xhtml).

Requirements: ebooklib, beautifulsoup4, PyYAML
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import yaml


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

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


def extract_metadata(book):
    meta = opf_meta(book)
    source_id = None
    for val, attrs in book.get_metadata('DC', 'identifier') or []:
        if 'BookId' in str(attrs.get('id', '')):
            source_id = val
            break

    d = {
        'title': dc(book, 'title') or 'Unknown Title',
        'author': dc(book, 'creator') or 'Unknown Author',
        'publisher': dc(book, 'publisher'),
        'language': dc(book, 'language') or 'bo',
        'date': dc(book, 'date'),
        'source_description': 'Extracted from EPUB source (Vajra Vidya Library)',
    }
    title_en = meta.get('calibre:title_sort')
    if title_en:
        d['title_en'] = title_en
    if source_id:
        d['source_id'] = source_id
    return d


# ---------------------------------------------------------------------------
# TOC
# ---------------------------------------------------------------------------

def build_toc_md(toc, depth=0):
    lines = []
    for entry in toc:
        if isinstance(entry, epub.Link):
            indent = '  ' * depth
            lines.append(indent + '- ' + (entry.title or ''))
            # No reliable in-doc anchors across merged docs; omit href
        elif isinstance(entry, tuple):
            section, children = entry
            indent = '  ' * depth
            title = section.title if hasattr(section, 'title') else ''
            if title:
                lines.append(indent + '- **' + title + '**')
            lines.extend(build_toc_md(children, depth + 1))
    return lines


def toc_block(book):
    lines = build_toc_md(book.toc)
    if not lines:
        return ''
    return '## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(lines) + '\n\n---\n\n'


# ---------------------------------------------------------------------------
# Chapter title lookup
# ---------------------------------------------------------------------------

def build_chapter_map(book):
    """Map spine filename → TOC title."""
    chapter_map = {}
    def walk(toc):
        for entry in toc:
            if isinstance(entry, epub.Link):
                fname = entry.href.split('#')[0].split('/')[-1]
                chapter_map[fname] = entry.title or ''
            elif isinstance(entry, tuple):
                section, children = entry
                if hasattr(section, 'href') and section.href:
                    fname = section.href.split('#')[0].split('/')[-1]
                    chapter_map[fname] = section.title or ''
                walk(children)
    walk(book.toc)
    return chapter_map


# ---------------------------------------------------------------------------
# Inline formatting & colour class detection
# ---------------------------------------------------------------------------

def get_color_class(element):
    classes = element.get('class', [])
    if 'root' in classes:
        return 'root'
    if 'lung' in classes:
        return 'lung'
    if 'bold' in classes:
        return 'toc'
    return None


def inline_formats(element):
    for s in element.find_all(['strong', 'b']):
        s.replace_with('**' + s.get_text() + '**')
    for i in element.find_all(['em', 'i']):
        i.replace_with('*' + i.get_text() + '*')
    for a in element.find_all('a', href=True):
        a.replace_with('[' + a.get_text() + '](' + a['href'] + ')')
    return element.get_text().strip()


def wrap_callout(callout_type, text):
    lines = text.split('\n')
    body = '\n'.join('> ' + line for line in lines)
    return '> [!' + callout_type + ']\n' + body + '\n\n'


# ---------------------------------------------------------------------------
# Element processing
# ---------------------------------------------------------------------------

FRONT_MATTER_DOCS = {'cover.xhtml', 'Incover.xhtml', 'Publisher.xhtml', 'team.xhtml', 'Contents.xhtml'}

def process_element(element):
    tag = element.name

    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        return '#' * level + ' ' + element.get_text().strip() + '\n\n'

    elif tag == 'p':
        color_class = get_color_class(element)
        text = inline_formats(element)
        if not text:
            return ''
        if color_class == 'root':
            return wrap_callout('root', text)
        elif color_class == 'lung':
            return wrap_callout('lung', text)
        elif color_class == 'toc':
            return wrap_callout('toc', text)
        else:
            return text + '\n\n'

    elif tag == 'ul':
        md = ''
        for li in element.find_all('li', recursive=False):
            md += '- ' + li.get_text().strip() + '\n'
        return md + '\n'

    elif tag == 'ol':
        md = ''
        for i, li in enumerate(element.find_all('li', recursive=False), 1):
            md += str(i) + '. ' + li.get_text().strip() + '\n'
        return md + '\n'

    elif tag == 'blockquote':
        lines = element.get_text().strip().split('\n')
        body = '\n'.join('> ' + line for line in lines)
        return body + '\n\n'

    return ''


# ---------------------------------------------------------------------------
# Main conversion
# ---------------------------------------------------------------------------

def convert_epub_to_markdown(epub_path, output_path):
    try:
        book = epub.read_epub(epub_path)
    except Exception as e:
        print('Error reading EPUB: ' + str(e))
        return

    metadata = extract_metadata(book)
    md = '---\n' + yaml.dump(metadata, allow_unicode=True, sort_keys=False) + '---\n\n'

    # Inject structured TOC
    md += toc_block(book)

    chapter_map = build_chapter_map(book)
    chapter_re = re.compile(r'Chapter(\d+)\.xhtml', re.IGNORECASE)

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]

        # Skip cover/publisher boilerplate
        if fname in FRONT_MATTER_DOCS:
            continue

        # Insert chapter heading separator
        ch_match = chapter_re.match(fname)
        if ch_match:
            ch_title = chapter_map.get(fname, '')
            md += '\n---\n\n'
            if ch_title:
                md += '## ' + ch_title + '\n\n'

        soup = BeautifulSoup(item.get_content(), 'html.parser')
        for tag in soup(['script', 'style']):
            tag.decompose()
        body = soup.find('body')
        if not body:
            continue
        for child in body.find_all(recursive=False):
            md += process_element(child)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Successfully extracted content to ' + output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EPUB to Markdown — Vajra Vidya Library')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
