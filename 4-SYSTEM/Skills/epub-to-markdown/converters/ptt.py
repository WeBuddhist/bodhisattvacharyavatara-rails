#!/usr/bin/env python3
"""
Converter: PTT (དཔའ་བོ་གཙུག་ལག་ཕྲེང་བ། commentary on BCA)
Generated: 2026-06-30

Source epub: PTT.epub — VVI-012 spine, publisher unknown (likely Vajra Vidya)
Author: དཔའ་བོ་སྐུ་ཕྲེང་གཉིས་པ་གཙུག་ལག་ཕྲེང་བ།

CSS class -> semantic mapping:
  Tibetan-Root-Text*           (#8b1409, red)   -> root   Root text verses
  Tibetan-External-Citations*  (#897335, gold)  -> lung   Scriptural citations
  Tibetan-Citations-in-Verse*  (#897335, gold)  -> lung   Verse-form citations
  Tibetan-Sabche*              (#005e7f, blue)  -> toc    Structural outline (ས་བཅད)
  Tibetan-Commentary*          (#343233, black) -> plain  Commentary body
  Tibetan-Regular-Indented     (#343233)        -> plain  Indented commentary
  Tibetan-Commentary-Non-Indent(#343233)        -> plain  Non-indented commentary
  Tibetan-Commentry-small-letter(#343233)       -> plain  Small-letter commentary
  English-Number-Before-Text   (#343233)        -> plain  Inline numbering
  Tibetan-Chapter / Chapters   (#343233)        -> (heading)
  Basic-Paragraph              (#000000)        -> plain

Processing: run-based (same approach as vajra-vidya-library.py).
Extensive mixed-class patterns: span class takes priority over paragraph class.
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString
import yaml


# ---------------------------------------------------------------------------
# Semantic class resolution
# ---------------------------------------------------------------------------

def resolve_class(class_set):
    """
    Given a set of CSS class names, return a semantic string:
    'root', 'lung', 'toc', or 'plain'.
    """
    if not class_set:
        return 'plain'

    joined = ' '.join(class_set)

    # Root text (red)
    if 'Root-Text' in joined:
        return 'root'

    # Scriptural citations (gold) — check both External-Citations and Citations-in-Verse
    if 'External-Citations' in joined or 'Citations-in-Verse' in joined:
        return 'lung'

    # Structural outline (blue)
    if 'Sabche' in joined:
        return 'toc'

    # Everything else is plain commentary
    return 'plain'


# ---------------------------------------------------------------------------
# Sa-bcad detection patterns (for truly unclassed runs)
# ---------------------------------------------------------------------------

_ORDINAL_START = re.compile(
    r'^(དང་པོ་?[ཉིའི]?|གཅིག་པ་|གཉིས་པ་|གསུམ་པ་|བཞི་པ་|ལྔ་པ་|'
    r'དྲུག་པ་|བདུན་པ་|བརྒྱད་པ་|དགུ་པ་|བཅུ་པ་)'
)
_STRUCTURAL_CLOSE = re.compile(
    r'(ནི།|ནི། །|ལ་གཉིས|ལ་གསུམ|ལ་བཞི|ལ་ལྔ|ལ་དྲུག|ལ་བདུན|'
    r'གཉིས་[ཏས][ེི]|གསུམ་[ཏས][ེི]|བཞི་[ཏས][ེི]|'
    r'ལྔ་[ཏས][ེི]|དྲུག་[ཏས][ེི])'
)
_EMBEDDED_OUTLINE = re.compile(
    r'[།།]\s*(གཉིས་པ་|གསུམ་པ་|བཞི་པ་|ལྔ་པ་|དྲུག་པ་|བདུན་པ་|བརྒྱད་པ་)'
    r'.{5,80}(ལ་གཉིས|ལ་གསུམ|ལ་བཞི|ལ་ལྔ|གཉིས་[ཏས][ེི]|གསུམ་[ཏས][ེི]|དང་པོ་ནི།)'
)


def is_outline_label(text):
    if _ORDINAL_START.match(text) and _STRUCTURAL_CLOSE.search(text):
        return True
    if _EMBEDDED_OUTLINE.search(text):
        return True
    return False


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
        'publisher': dc(book, 'publisher') or 'Unknown (VVI series)',
        'language': 'bo',
        'date': dc(book, 'date'),
        'source_description': 'Extracted from EPUB (PTT / VVI-012)',
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
            lines.append('  ' * depth + '- ' + (entry.title or ''))
        elif isinstance(entry, tuple):
            section, children = entry
            title = section.title if hasattr(section, 'title') else ''
            if title:
                lines.append('  ' * depth + '- **' + title + '**')
            lines.extend(build_toc_md(children, depth + 1))
    return lines


def toc_block(book):
    lines = build_toc_md(book.toc)
    if not lines:
        return ''
    return '## དཀར་ཆག / Table of Contents\n\n' + '\n'.join(lines) + '\n\n---\n\n'


def build_chapter_map(book):
    chapter_map = {}
    def walk(toc):
        for entry in toc:
            if isinstance(entry, epub.Link):
                fname = entry.href.split('#')[0].split('/')[-1]
                if fname not in chapter_map:
                    chapter_map[fname] = entry.title or ''
            elif isinstance(entry, tuple):
                section, children = entry
                if hasattr(section, 'href') and section.href:
                    fname = section.href.split('#')[0].split('/')[-1]
                    if fname not in chapter_map:
                        chapter_map[fname] = section.title or ''
                walk(children)
    walk(book.toc)
    return chapter_map


# ---------------------------------------------------------------------------
# Run-based paragraph processing
# ---------------------------------------------------------------------------

def extract_runs(element):
    """
    Walk a <p> element's children and return a list of (effective_class, text) pairs,
    where consecutive content sharing the same semantic class is merged into one run.

    effective_class is one of: 'root', 'lung', 'toc', 'plain'
      - Resolved from the element's CSS classes using resolve_class()
      - Span class takes priority over paragraph class
      - <br/> becomes '\n' within the current run
    """
    p_classes = set(element.get('class', []))
    # Strip utility/override classes for resolution
    p_clean = {c for c in p_classes if not c.startswith('_') and 'Override' not in c and 'ParaOverride' not in c}
    p_semantic = resolve_class(p_clean)

    def resolve_child(cls_set):
        if not cls_set:
            return p_semantic
        clean = {c for c in cls_set if not c.startswith('_') and 'Override' not in c}
        if not clean:
            return p_semantic
        child_sem = resolve_class(clean)
        # If child resolves to 'plain' but parent has a semantic class,
        # only override if child explicitly has a commentary/plain class
        if child_sem == 'plain' and p_semantic != 'plain':
            # Check if child has an explicit plain-type class
            joined = ' '.join(clean)
            if ('Commentary' in joined or 'Regular' in joined or
                'Number-Before' in joined or 'Basic' in joined or
                'small-letter' in joined):
                return 'plain'
            return p_semantic
        return child_sem

    runs = []
    cur_cls = None
    cur_parts = []

    def flush():
        if cur_parts:
            text = ''.join(cur_parts).strip()
            if text:
                runs.append((cur_cls, text))

    for child in element.children:
        if isinstance(child, NavigableString):
            text = str(child)
            if not text.strip():
                continue
            child_cls = p_semantic
            if child_cls == cur_cls:
                cur_parts.append(text)
            else:
                flush()
                cur_cls = child_cls
                cur_parts = [text]

        elif child.name == 'br':
            cur_parts.append('\n')

        elif child.name in ('a',):
            href = child.get('href', '')
            link_text = child.get_text()
            text = '[' + link_text + '](' + href + ')' if href else link_text
            child_cls = p_semantic
            if child_cls == cur_cls:
                cur_parts.append(text)
            else:
                flush()
                cur_cls = child_cls
                cur_parts = [text]

        else:
            # <span> or other inline element
            span_classes = set(child.get('class', []))
            child_cls = resolve_child(span_classes)

            # Collect text inside span, handling nested elements
            inner_parts = []
            for sub in child.children:
                if isinstance(sub, NavigableString):
                    inner_parts.append(str(sub))
                elif sub.name == 'br':
                    inner_parts.append('\n')
                else:
                    inner_parts.append(sub.get_text())
            text = ''.join(inner_parts)
            if not text.strip():
                continue

            if child_cls == cur_cls:
                cur_parts.append(text)
            else:
                flush()
                cur_cls = child_cls
                cur_parts = [text]

    flush()
    return runs


def wrap_callout(callout_type, text):
    text = re.sub(r'\n{2,}', '\n', text.strip())
    lines = text.split('\n')
    body = '\n'.join('> ' + line.strip() for line in lines if line.strip())
    return '> [!' + callout_type + ']\n' + body + '\n\n'


def emit_run(cls, text):
    """Emit a single run as the appropriate Markdown block."""
    text = text.strip()
    if not text:
        return ''
    if cls == 'root':
        return wrap_callout('root', text)
    if cls == 'lung':
        return wrap_callout('lung', text)
    if cls == 'toc':
        return wrap_callout('toc', text)
    # plain
    if is_outline_label(text):
        return wrap_callout('toc', text)
    return text + '\n\n'


def process_paragraph(element):
    runs = extract_runs(element)
    if not runs:
        return ''
    if len(runs) == 1:
        return emit_run(runs[0][0], runs[0][1])
    return ''.join(emit_run(cls, text) for cls, text in runs)


# ---------------------------------------------------------------------------
# Element processing
# ---------------------------------------------------------------------------

FRONT_MATTER_DOCS = {'cover.xhtml'}


def is_chapter_heading(element):
    """Check if paragraph is a chapter heading by its class."""
    classes = set(element.get('class', []))
    joined = ' '.join(classes)
    return 'Tibetan-Chapter' in joined or 'Tibetan-Chapters' in joined


def process_element(element):
    tag = element.name

    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        return '#' * level + ' ' + element.get_text().strip() + '\n\n'

    elif tag == 'p':
        # Check for chapter-heading class paragraphs
        if is_chapter_heading(element):
            text = element.get_text().strip()
            if text:
                return '## ' + text + '\n\n'
            return ''
        return process_paragraph(element)

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

    # Recurse into divs and sections
    elif tag in ('div', 'section'):
        md = ''
        for child in element.find_all(recursive=False):
            md += process_element(child)
        return md

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
    md += toc_block(book)

    chapter_map = build_chapter_map(book)
    first_content = True

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]
        if fname in FRONT_MATTER_DOCS:
            continue

        # Add separator between spine documents (except the first)
        if not first_content:
            ch_title = chapter_map.get(fname, '')
            md += '\n---\n\n'
            if ch_title:
                md += '## ' + ch_title + '\n\n'
        first_content = False

        soup = BeautifulSoup(item.get_content(), 'html.parser')
        for t in soup(['script', 'style']):
            t.decompose()
        body = soup.find('body')
        if not body:
            continue
        for child in body.find_all(recursive=False):
            md += process_element(child)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print('Successfully extracted content to ' + output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EPUB to Markdown - PTT')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
