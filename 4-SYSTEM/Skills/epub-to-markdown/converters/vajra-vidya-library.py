#!/usr/bin/env python3
"""
Converter: Vajra Vidya Library
Generated: 2026-05-10

CSS class -> callout mapping:
  .root   (#BB5500) -> > [!root]   Root text verses
  .lung   (#7D6608) -> > [!lung]   Scriptural citations
  .bold   (#003377) -> > [!toc]    TOC enumeration / outline items
  .normal (#000000) -> plain text  Explicit revert-to-plain inside colored block

Processing approach — run-based, not paragraph-level:
  Each <p> is walked child-by-child. Consecutive text nodes and spans that share
  the same effective semantic class are merged into a "run". Each run is then
  emitted as its own block (callout or plain text). This correctly handles:

    1. Trailing .normal span in .lung/.root paragraph:
         <p class="lung">verse...<span class="normal">ཞེས་དང༌།</span></p>
         -> [!lung] callout for verse + plain text for ཞེས་དང༌།

    2. Leading <span class="bold"> in plain <p> (outline label + commentary):
         <p><span class="bold">label</span> commentary...</p>
         -> [!toc] callout for label + plain text for commentary

    3. Inline .bold single-word emphasis inside .lung paragraph:
         stays inside the [!lung] callout (no semantic split needed for 1-2 word emphasis)

    4. Truly unclassed <p> sa-bcad labels (ordinal-start or transition+outline):
         detected by text pattern and emitted as [!toc] callout.

Additional metadata: publisher, title_en, source_id.
Structure: TOC injected after frontmatter. Chapter separators from spine.
"""

import argparse
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup, NavigableString
import yaml


# ---------------------------------------------------------------------------
# Semantic class constants
# ---------------------------------------------------------------------------

SEMANTIC_CLASSES = {'root', 'lung', 'bold', 'normal'}


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
# Run-based paragraph processing
# ---------------------------------------------------------------------------

def extract_runs(element):
    """
    Walk a <p> element's children and return a list of (effective_class, text) pairs,
    where consecutive content sharing the same semantic class is merged into one run.

    effective_class is one of: 'root', 'lung', 'toc', 'normal', 'plain'
      - Inherited from the <p>'s own class unless overridden by an inline <span>
      - 'normal' and empty map to 'plain' for emission purposes
      - .bold maps to 'toc'
      - <br/> becomes '\n' within the current run
    """
    p_classes = set(element.get('class', []))
    p_semantic = p_classes & SEMANTIC_CLASSES

    def resolve(cls_set):
        effective = cls_set & SEMANTIC_CLASSES if cls_set else p_semantic
        if not effective:
            return 'plain'
        if 'root' in effective:
            return 'root'
        if 'lung' in effective:
            return 'lung'
        if 'bold' in effective:
            return 'toc'
        return 'plain'  # 'normal' -> plain

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
            child_cls = resolve(None)
            if child_cls == cur_cls:
                cur_parts.append(text)
            else:
                flush()
                cur_cls = child_cls
                cur_parts = [text]

        elif child.name == 'br':
            cur_parts.append('\n')

        elif child.name in ('a',):
            # Links: inherit parent class, format as markdown link
            href = child.get('href', '')
            link_text = child.get_text()
            text = '[' + link_text + '](' + href + ')' if href else link_text
            child_cls = resolve(None)
            if child_cls == cur_cls:
                cur_parts.append(text)
            else:
                flush()
                cur_cls = child_cls
                cur_parts = [text]

        else:
            # <span> or other inline element
            span_classes = set(child.get('class', []))
            child_cls = resolve(span_classes)

            # Collect text inside span, handling nested <br/>
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
    # Collapse consecutive newlines so no blank lines appear within the callout block.
    # Consecutive shlokas are already separated because each is its own callout block.
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
    # plain / normal
    if is_outline_label(text):
        return wrap_callout('toc', text)
    return text + '\n\n'


def process_paragraph(element):
    runs = extract_runs(element)
    if not runs:
        return ''
    # Single-run fast path (the common case)
    if len(runs) == 1:
        return emit_run(runs[0][0], runs[0][1])
    # Multi-run: emit each separately
    return ''.join(emit_run(cls, text) for cls, text in runs)


# ---------------------------------------------------------------------------
# Element processing
# ---------------------------------------------------------------------------

FRONT_MATTER_DOCS = {'cover.xhtml', 'Incover.xhtml', 'Publisher.xhtml',
                     'team.xhtml', 'Contents.xhtml'}


def process_element(element):
    tag = element.name

    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag[1])
        return '#' * level + ' ' + element.get_text().strip() + '\n\n'

    elif tag == 'p':
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
    chapter_re = re.compile(r'Chapter(\d+)\.xhtml', re.IGNORECASE)

    for item_id, linear in book.spine:
        item = book.get_item_with_id(item_id)
        if not item or item.get_type() != ebooklib.ITEM_DOCUMENT:
            continue

        fname = item.get_name().split('/')[-1]
        if fname in FRONT_MATTER_DOCS:
            continue

        ch_match = chapter_re.match(fname)
        if ch_match:
            ch_title = chapter_map.get(fname, '')
            md += '\n---\n\n'
            if ch_title:
                md += '## ' + ch_title + '\n\n'

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
    parser = argparse.ArgumentParser(description='EPUB to Markdown - Vajra Vidya Library')
    parser.add_argument('epub_path', help='Path to the source EPUB file')
    parser.add_argument('output_path', help='Path to the output Markdown file')
    args = parser.parse_args()
    convert_epub_to_markdown(args.epub_path, args.output_path)
