#!/usr/bin/env python3
"""
find_toc_contexts.py -- rewrite [[context]] in a TOC tree with accurate body contexts.

Gemini-first approach: no string matching. Gemini acts as a Tibetan Buddhist
text expert and locates each section's body description directly.

For each TOC entry Gemini receives:
  - The full TOC structure (all entries with their decimal numbers and titles)
  - The source passage covering the expected region (numbered lines)
  - The section's position in the hierarchy (parent, preceding siblings)

Gemini returns the line number and verbatim opening words of the BODY
DESCRIPTION -- where the commentary actually explains the topic -- not the
dkar-chag heading where the title is merely listed.

The search window advances strictly after each located body line so sibling
sections never overlap.

Usage:
    python 4-SYSTEM/scripts/toc_tree_extractor/find_toc_contexts.py \\
        0-INBOX/toc-tree-BCAC20_TG_bo.md \\
        1-SOURCES/Commentaries/BCAC20_TG_bo.md
"""

import argparse
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# .env loader
# ---------------------------------------------------------------------------
def _load_dotenv():
    candidates = [Path.cwd()]
    for p in Path.cwd().parents:
        if (p / "4-SYSTEM").is_dir():
            candidates.append(p)
            break
    candidates.append(Path(__file__).parent)
    for base in candidates:
        env_file = base / ".env"
        if env_file.exists():
            with open(env_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
            return


_load_dotenv()

DEFAULT_MODEL  = "gemini-flash-latest"
DEFAULT_WINDOW = 200   # source lines per search window
SLIDE_STEP     = 50   # lines to advance when section not found in window
MAX_SLIDES     = 5     # max times to slide before giving up
MAX_RETRIES    = 5
RETRY_BACKOFF  = 6

# ---------------------------------------------------------------------------
# Tibetan helpers
# ---------------------------------------------------------------------------
_TSHEG = "་"
_SHAD_CHARS = "།༎༏༐༑༒༔"
_SHAD_OR_WS_RE = re.compile("[" + _SHAD_CHARS + r"\s]+")


def tib_canon(s):
    if not s:
        return ""
    s = _SHAD_OR_WS_RE.sub(_TSHEG, s)
    s = re.sub(re.escape(_TSHEG) + "+", _TSHEG, s)
    return s.strip(_TSHEG)


def trim_syllables(text, max_sylls=20):
    sylls = text.split(_TSHEG)
    if len(sylls) > max_sylls:
        return _TSHEG.join(sylls[:max_sylls])
    return text


# ---------------------------------------------------------------------------
# TOC tree parser / writer
# ---------------------------------------------------------------------------
_TREE_RE = re.compile(
    r"^(?P<indent>\s*\*\s+(?P<dec>\d+(?:\.\d+)*)\.?\s+)"
    r"(?P<title>[^\[]+?)(?:\s*\[\[(?P<ctx>[^\]]*)\]\])?\s*$"
)


def parse_toc(path):
    entries = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = _TREE_RE.match(raw)
        if not m:
            continue
        title = m.group("title").strip().rstrip("།").strip()
        entries.append({
            "dec":   m.group("dec"),
            "title": title,
            "ctx":   (m.group("ctx") or "").strip() or None,
            "raw":   raw,
        })
    return entries


def rewrite_toc(path, new_contexts, out_path=None):
    """Write updated toc-tree to out_path. Backs up original as .bak."""
    if out_path is None:
        out_path = path
    raw_lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    for raw in raw_lines:
        m = _TREE_RE.match(raw.rstrip("\n\r"))
        if m and m.group("dec") in new_contexts:
            dec    = m.group("dec")
            indent = m.group("indent")
            title  = m.group("title").strip().rstrip("།").strip()
            ctx    = new_contexts[dec]
            out.append(f"{indent}{title} [[{ctx}]]\n")
        else:
            out.append(raw)
    bak = path.with_suffix(path.suffix + ".bak")
    bak.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(out), encoding="utf-8")
    return bak


def find_vault_root(start):
    for p in [start] + list(start.parents):
        if (p / "4-SYSTEM").is_dir():
            return p
    return start


def toc_summary(entries):
    """Full TOC as a compact reference string to give Gemini structural context."""
    lines = []
    for e in entries:
        depth  = len(e["dec"].split("."))
        indent = "  " * (depth - 1)
        ctx    = f" [[{e['ctx']}]]" if e["ctx"] and e["ctx"] != "?" else ""
        lines.append(f"{indent}{e['dec']}. {e['title']}{ctx}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Gemini client
# ---------------------------------------------------------------------------
def get_client():
    try:
        from google import genai
    except ImportError:
        sys.exit("Error: google-genai not installed. Run: pip install google-genai")
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Error: GEMINI_API_KEY not set.")
    return genai.Client(api_key=api_key)


# ---------------------------------------------------------------------------
# Core: Gemini locates the body description
# ---------------------------------------------------------------------------
def gemini_locate_body(client, model,
                       lines, start_line, end_line,
                       dec, title,
                       toc_ref,
                       parent_dec=None, parent_title=None,
                       prev_siblings=None):
    """
    Ask Gemini -- as a Tibetan Buddhist text expert -- to find where section
    `dec` (`title`) is DESCRIBED in the body commentary, within the passage
    lines[start_line:end_line].

    The passage is presented with line numbers so Gemini can cite the exact line.

    Returns (snippet, body_line_idx) where:
      snippet        -- verbatim opening ≤20 syllables of the body description
      body_line_idx  -- 0-based index in `lines` (None if not determinable)

    Returns (None, None) if Gemini cannot locate the section.
    """
    import time as _t
    from google.genai import types

    end_line = min(end_line, len(lines))
    passage_lines = lines[start_line:end_line]
    if not passage_lines:
        return None, None

    numbered = "".join(
        f"[L{start_line + i + 1}] {ln}"
        for i, ln in enumerate(passage_lines)
    )

    hier_parts = []
    if parent_dec and parent_title:
        hier_parts.append(f"Parent: {parent_dec}. {parent_title}")
    if prev_siblings:
        hier_parts.append("Preceding siblings (already located):")
        for s in prev_siblings[-4:]:
            hier_parts.append(f"  {s}")
    hier_block = ("\n\nHIERARCHY:\n" + "\n".join(hier_parts)) if hier_parts else ""

    prompt = (
        "You are an expert in Tibetan Buddhist texts and commentaries.\n\n"
        "FULL TABLE OF CONTENTS (for structural reference):\n"
        f"{toc_ref}\n"
        f"{hier_block}\n\n"
        "YOUR TASK:\n"
        f"Locate section  {dec}. {title}\n\n"
        "Find the line in the NUMBERED PASSAGE below where the commentary\n"
        "BODY DESCRIPTION of this section begins -- that is, the line where\n"
        "the text actually starts EXPLAINING or DISCUSSING this topic.\n\n"
        "IMPORTANT RULES:\n"
        "  1. Do NOT return a line that is part of a dkar-chag (preview listing\n"
        "     of upcoming section titles). A dkar-chag lists several titles in\n"
        "     sequence without explanation.\n"
        "  2. Do NOT return a bare heading line that merely states the section\n"
        "     title without any following commentary prose.\n"
        "  3. In Tibetan commentaries the body description of sub-section N\n"
        "     typically begins with an ordinal marker (དང་པོ་ནི།, གཉིས་པ་ནི།,\n"
        "     གསུམ་པ་ནི། …) IMMEDIATELY followed by substantive prose on the\n"
        "     same line -- that combination is the body opening.\n"
        "  4. Use the TOC and hierarchy context to understand WHICH section's\n"
        "     body you are looking for. If the passage contains body descriptions\n"
        "     for multiple siblings, return only the one for section {dec}.\n\n"
        "NUMBERED PASSAGE:\n"
        f"{numbered}\n\n"
        "REPLY FORMAT (two lines, nothing else):\n"
        "LINE: <[L…] tag of the body-description opening line, or NONE>\n"
        "TEXT: <verbatim opening 15-20 Tibetan syllables of that line>"
    )

    config = types.GenerateContentConfig(
        temperature=0.0,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    )
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp   = client.models.generate_content(
                model=model, contents=prompt, config=config)
            raw    = (resp.text or "").strip()

            line_num = None
            snippet  = None
            for ln in raw.splitlines():
                ln = ln.strip()
                if ln.upper().startswith("LINE:"):
                    val = ln.split(":", 1)[1].strip()
                    if val.upper() == "NONE":
                        return None, None
                    m = re.search(r"L(\d+)", val, re.IGNORECASE)
                    if m:
                        line_num = int(m.group(1)) - 1   # 0-based
                elif ln.upper().startswith("TEXT:"):
                    snippet = ln.split(":", 1)[1].strip().strip("[]\"'")

            if not snippet:
                return None, None

            snippet = trim_syllables(snippet)

            # Validate line_num is within our window
            if line_num is not None and not (start_line <= line_num < end_line):
                line_num = None

            # If no valid line_num, try to find snippet in passage
            if line_num is None:
                canon_snip = tib_canon(snippet)
                half = max(4, len(canon_snip) // 2)
                prefix = canon_snip[:half]
                for i, pline in enumerate(passage_lines):
                    if prefix and prefix in tib_canon(pline):
                        line_num = start_line + i
                        break

            return snippet, line_num

        except Exception as e:
            last_err = e
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF * (2 ** (attempt - 1))
                print(f"      ! Gemini error (attempt {attempt}): {e}; "
                      f"retrying in {wait}s", file=sys.stderr)
                _t.sleep(wait)

    print(f"      ! gemini_locate_body failed after retries: {last_err}",
          file=sys.stderr)
    return None, None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Rewrite [[context]] in a TOC tree using Gemini as Buddhist text expert.")
    ap.add_argument("toc_file",    help="toc-tree-<id>.md")
    ap.add_argument("source_file", help="Commentary .md")
    ap.add_argument("--model",  default=DEFAULT_MODEL,
                    help=f"Gemini model (default: {DEFAULT_MODEL})")
    ap.add_argument("--window", type=int, default=DEFAULT_WINDOW,
                    help=f"Source lines per search window (default: {DEFAULT_WINDOW})")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print proposed contexts without writing the file")
    args = ap.parse_args()

    toc_path = Path(args.toc_file).expanduser().resolve()
    src_path = Path(args.source_file).expanduser().resolve()
    for p in (toc_path, src_path):
        if not p.exists():
            sys.exit(f"Error: not found: {p}")

    entries = parse_toc(toc_path)
    if not entries:
        sys.exit("No TOC entries found.")

    lines    = src_path.read_text(encoding="utf-8").splitlines(keepends=True)
    toc_ref  = toc_summary(entries)
    client   = get_client()

    print(f"TOC:    {toc_path}  ({len(entries)} entries)")
    print(f"Source: {src_path}  ({len(lines)} lines)")
    print()

    # dec -> {body_line, ctx}  accumulated as we go
    dec_body_line = {}   # 0-based line where body description was found
    dec_ctx       = {}   # resolved snippet
    dec_title     = {e["dec"]: e["title"] for e in entries}
    new_contexts  = {}

    def parent_dec(dec):
        parts = dec.split(".")
        return ".".join(parts[:-1]) if len(parts) > 1 else None

    def ancestors(dec):
        """All ancestor decs from root down."""
        parts = dec.split(".")
        return [".".join(parts[:i]) for i in range(1, len(parts))]

    def search_start_for(dec):
        """
        Best lower bound for the search window:
        - previous sibling's body line + 1   (strongest: section must follow)
        - parent's body line + 1             (fallback)
        - 0                                  (root fallback)
        """
        cur_parts = dec.split(".")
        # look for preceding sibling
        for e in reversed(entries):
            e_parts = e["dec"].split(".")
            if (len(e_parts) == len(cur_parts) and
                    e_parts[:-1] == cur_parts[:-1] and
                    e["dec"] < dec):
                bl = dec_body_line.get(e["dec"])
                if bl is not None:
                    return bl + 1
        # parent
        pdec = parent_dec(dec)
        if pdec:
            bl = dec_body_line.get(pdec)
            if bl is not None:
                return bl + 1
        return 0

    def prev_siblings_info(dec):
        cur_parts = dec.split(".")
        siblings  = []
        for e in entries:
            e_parts = e["dec"].split(".")
            if (len(e_parts) == len(cur_parts) and
                    e_parts[:-1] == cur_parts[:-1] and
                    e["dec"] < dec):
                ctx = dec_ctx.get(e["dec"], "?")
                siblings.append(f"{e['dec']}. {e['title']} [[{ctx}]]")
        return siblings

    for entry in entries:
        dec   = entry["dec"]
        title = entry["title"]
        depth = len(dec.split("."))

        # Hierarchy context
        pdec  = parent_dec(dec)
        ptitle = dec_title.get(pdec, "") if pdec else None
        prev_sibs = prev_siblings_info(dec)

        start = search_start_for(dec)
        snippet   = None
        body_line = None

        # Slide the window forward if not found on first attempt
        for slide in range(MAX_SLIDES):
            w_start = start + slide * SLIDE_STEP
            w_end   = w_start + args.window
            if w_start >= len(lines):
                break

            if slide > 0:
                print(f"  [{dec}] not found in window, sliding +{slide * SLIDE_STEP} lines …",
                      flush=True)

            snippet, body_line = gemini_locate_body(
                client, args.model,
                lines, w_start, w_end,
                dec, title,
                toc_ref,
                parent_dec=pdec, parent_title=ptitle,
                prev_siblings=prev_sibs,
            )
            if snippet:
                break

        if snippet:
            new_contexts[dec] = snippet
            dec_ctx[dec]      = snippet
            if body_line is not None:
                dec_body_line[dec] = body_line
                line_tag = f"line {body_line + 1:4}"
            else:
                line_tag = "line ?"
            slides_tag = f" (slide×{slide})" if slide > 0 else ""
            print(f"  [{dec}] {line_tag}{slides_tag}  ctx: {snippet[:60]}",
                  flush=True)
        else:
            # Keep existing context rather than losing data
            fallback = entry["ctx"] or "?"
            new_contexts[dec] = fallback
            dec_ctx[dec]      = fallback
            print(f"  [{dec}] NOT FOUND -- kept: {fallback[:50]}", flush=True)

    print()

    if args.dry_run:
        print("Dry run -- no file written.")
        return

    commentary_id = re.sub(r"^toc-tree-", "", toc_path.stem)
    vault_root    = find_vault_root(toc_path)
    out_path      = (vault_root / "0-INBOX" / "temp"
                     / f"TOC-{commentary_id}" / toc_path.name)

    bak = rewrite_toc(toc_path, new_contexts, out_path=out_path)
    print(f"Written -> {out_path}")
    print(f"Backup  -> {bak}")


if __name__ == "__main__":
    main()
