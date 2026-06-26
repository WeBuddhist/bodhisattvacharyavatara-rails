#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reflow Tibetan text by the shad (།).

Steps:
  1. Remove all existing line breaks (collapse whitespace to single spaces).
  2. Insert a line break after every shad group (one or more ། optionally
     separated by spaces, e.g. ། ། / །། / །། །། / ། ། ། །).
  3. Exception: never break after the opening header ༄༅། ། — it stays
     attached to the text that follows it.

A leading YAML frontmatter block (--- ... ---) is preserved untouched; only
the body below it is reflowed.

Usage:
    python shad_linebreak.py input.txt [output.txt]
    cat input.txt | python shad_linebreak.py        # stdin -> stdout
"""
import re
import sys

# A shad group: one shad, then any number of (spaces + shad).
# Either preceded by the yig-mgo header ༄༅ (kept, no break) or standalone (break after).
PATTERN = re.compile(r'(༄༅\s*།(?:\s*།)*)|(།(?:\s*།)*)')

# A leading YAML frontmatter block: --- on the first line, then content,
# then a closing --- (or ...) on its own line.
FRONTMATTER = re.compile(r'\A(---\r?\n.*?\r?\n(?:---|\.\.\.)[ \t]*\r?\n?)',
                         re.DOTALL)


def split_frontmatter(text: str):
    """Return (frontmatter, body). frontmatter is '' if none present."""
    m = FRONTMATTER.match(text)
    if m:
        return m.group(1), text[m.end():]
    return '', text


def reflow(text: str) -> str:
    # 1. remove all line breaks -> one continuous string (whitespace normalised)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return ''

    # 2 + 3. insert breaks after shad groups, except the ༄༅ header
    def repl(m):
        if m.group(1) is not None:       # ༄༅། ། header -> keep, no break
            return m.group(1)
        return m.group(2) + '\n'         # ordinary shad group -> break after

    out = PATTERN.sub(repl, text)

    # tidy: drop spaces sitting around the inserted newlines, collapse blanks
    out = re.sub(r'[ \t]*\n[ \t]*', '\n', out)
    out = re.sub(r'\n{2,}', '\n', out).strip()
    return out + '\n'


def main():
    args = sys.argv[1:]
    if args:
        with open(args[0], encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    front, body = split_frontmatter(text)
    result = front + reflow(body)

    if len(args) >= 2:
        with open(args[1], 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
