#!/usr/bin/env python3
"""Citation-integrity verifier for Local-Wiki articles (Railroad vault).

Checks, for every attestation blockquote in every article:
  1. QUOTE-EXISTS: the quoted text appears verbatim (whitespace-collapsed) in the cited file.
  2. ANCHOR-EXISTS: the cited anchor resolves — either a real block ID (line ending ^id)
     or a root-verse transclusion line containing #^id]] in the cited file.
  3. POSITION: for transclusion anchors, the quote's position in the source lies after the
     cited anchor's transclusion line and before the next transclusion line (i.e. the quote
     really is commentary on that verse). Reported as WARN, not FAIL, because front-matter
     and TOC-structured files legitimately deviate.

Exit code 1 if any FAIL.
"""
import re, sys, glob, os

VAULT = "/Users/tashitsering/Desktop/work/Obsidian/bodhisattvacharyavatara-rails"
WIKI = os.path.join(VAULT, "2-RAILS", "Local-Wiki")

def collapse(s: str) -> str:
    return re.sub(r"\s+", "", s)

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

CITE_RE = re.compile(r"\((1-SOURCES/[^)#]+)(?:#\^([\w-]+))?\)")
TRANS_RE = re.compile(r"!\[\[[^\]]*#\^([\w-]+)\]\]")

def parse_attestations(text):
    """Yield (quote_lines, cite_path, anchor, lineno) for each blockquote whose last line is a citation."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith(">"):
            j = i
            block = []
            while j < len(lines) and lines[j].startswith(">"):
                block.append(lines[j].lstrip("> ").rstrip())
                j += 1
            # find citation line(s) within block
            cites = [m for l in block for m in CITE_RE.finditer(l)]
            quote = "".join(l for l in block if not CITE_RE.search(l))
            if cites and quote.strip():
                for m in cites:
                    yield quote, m.group(1), m.group(2), i + 1
            i = j
        else:
            i += 1

def main():
    fails, warns, oks = [], [], 0
    articles = sorted(glob.glob(os.path.join(WIKI, "*.md")))
    if not articles:
        print("No articles found in", WIKI); sys.exit(1)
    src_cache = {}
    for art in articles:
        name = os.path.basename(art)
        text = load(art)
        n_att = 0
        for quote, cite_path, anchor, lineno in parse_attestations(text):
            n_att += 1
            full = os.path.join(VAULT, cite_path)
            if not os.path.exists(full):
                fails.append(f"{name}:{lineno} MISSING-FILE {cite_path}")
                continue
            if full not in src_cache:
                raw = load(full)
                src_cache[full] = (raw, collapse(raw), raw.splitlines())
            raw, flat, srclines = src_cache[full]
            q = collapse(quote)
            if len(q) < 10:
                warns.append(f"{name}:{lineno} SHORT-QUOTE ({len(q)} chars)")
            if q not in flat:
                fails.append(f"{name}:{lineno} QUOTE-NOT-VERBATIM in {os.path.basename(cite_path)} (first 40: {quote[:40]}...)")
                continue
            if anchor:
                # anchor resolves? real block id or transclusion
                block_id_line = next((k for k, l in enumerate(srclines) if l.rstrip().endswith("^" + anchor)), None)
                trans_lines = [(k, m.group(1)) for k, l in enumerate(srclines) for m in TRANS_RE.finditer(l)]
                trans_line = next((k for k, a in trans_lines if a == anchor), None)
                if block_id_line is None and trans_line is None:
                    fails.append(f"{name}:{lineno} ANCHOR-UNRESOLVED ^{anchor} in {os.path.basename(cite_path)}")
                    continue
                if trans_line is not None and block_id_line is None:
                    # position check: quote should sit between this transclusion and the next
                    nxt = next((k for k, a in trans_lines if k > trans_line), len(srclines))
                    seg = collapse("\n".join(srclines[trans_line:nxt]))
                    if q not in seg:
                        warns.append(f"{name}:{lineno} POSITION ^{anchor}: quote not within that verse's segment of {os.path.basename(cite_path)}")
                        continue
            oks += 1
        print(f"{name}: {n_att} attestation citations checked")
    print("\n== RESULT ==")
    print(f"OK: {oks}  WARN: {len(warns)}  FAIL: {len(fails)}")
    for w in warns: print("WARN ", w)
    for f in fails: print("FAIL ", f)
    sys.exit(1 if fails else 0)

main()
