#!/usr/bin/env python3
"""
root_marker_to_bold.py

Post-processes a Markdown file produced by the epub-to-markdown converter,
converting Tibetan root-text syllable markers (༷ U+0F37, TIBETAN MARK NADA)
into Markdown bold spans.

The marker ༷ appears on individual characters within a syllable to indicate
that syllable belongs to the root text being cited or commented upon.
Consecutive marked syllables are grouped into a single **bold** span.
A space is inserted before and after each bold group so the markers render
correctly in Obsidian and standard Markdown parsers.

Usage:
    python root_marker_to_bold.py input.md              # edit in place
    python root_marker_to_bold.py input.md output.md    # write to new file

Example:
    Input:  མེད་པའི་ཕྱིར་ན་འཐད༷་པ༷་བཞི་དང༷་བཅ༷ས་པ༷ར་བྱང་ཆུབ་སེམས་དཔའ་
    Output: མེད་པའི་ཕྱིར་ན་ **འཐད་པ་** བཞི་ **དང་བཅས་པར་** བྱང་ཆུབ་སེམས་དཔའ་
"""

import sys

MARKER = '༷'   # ༷  TIBETAN MARK NADA
TSHEG  = '་'   # ་  TIBETAN MARK INTERSYLLABIC TSHEG
SHAD   = '།'   # །  TIBETAN MARK SHAD


def convert_root_markers(text):
    """
    Convert ༷-marked syllables in a single text string to Markdown bold.
    The ༷ character is stripped from the output; non-marked text is unchanged.
    """
    if MARKER not in text:
        return text

    # Tokenise: walk character by character, appending each token when we
    # hit a syllable boundary (tsheg, shad, space, newline).  The boundary
    # character is included in the preceding token so tsheg spacing is preserved.
    tokens = []
    current = ''
    for ch in text:
        current += ch
        if ch in (TSHEG, SHAD, ' ', '\n'):
            tokens.append(current)
            current = ''
    if current:
        tokens.append(current)

    # Classify each token and strip the marker
    classified = [(MARKER in tok, tok.replace(MARKER, '')) for tok in tokens]

    # Group consecutive tokens with the same marking into runs
    groups = []   # list of [marked: bool, accumulated_text: str]
    for marked, clean in classified:
        if groups and groups[-1][0] == marked:
            groups[-1][1] += clean
        else:
            groups.append([marked, clean])

    # Render: wrap marked runs in **…**, adding a leading space when the
    # preceding text does not already end with one (needed for MD bold to parse).
    # Always add a trailing space after ** so the following syllable separates cleanly.
    parts = []
    for marked, content in groups:
        if marked:
            prefix = ' ' if parts and not parts[-1].endswith(' ') else ''
            parts.append(prefix + '**' + content + '** ')
        else:
            parts.append(content)

    return ''.join(parts)


def process_line(line):
    """
    Apply convert_root_markers to one Markdown line, preserving structural
    prefixes (callout '> ', heading '#', bullet '- ', etc.).
    The prefix itself is never modified — only the text content is processed.
    """
    # Callout lines: '> text'
    if line.startswith('> '):
        return '> ' + convert_root_markers(line[2:])
    return convert_root_markers(line)


def process_file(content):
    """
    Process the full content of a Markdown file.
    The YAML frontmatter block (between the opening and closing '---' lines)
    is passed through unchanged so metadata values are not altered.
    """
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    frontmatter_done = False

    for line in lines:
        if not frontmatter_done:
            if line.strip() == '---':
                if not in_frontmatter:
                    in_frontmatter = True
                else:
                    in_frontmatter = False
                    frontmatter_done = True
                result.append(line)
                continue
            if in_frontmatter:
                result.append(line)
                continue

        result.append(process_line(line))

    return '\n'.join(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python root_marker_to_bold.py input.md [output.md]')
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path

    with open(input_path, encoding='utf-8') as f:
        content = f.read()

    before = content.count(MARKER)
    result = process_file(content)
    after  = result.count(MARKER)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f'Converted {before} marker characters (remaining: {after}) -> {output_path}')
