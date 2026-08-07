#!/usr/bin/env python3
"""
prompt.py — assemble the zero-shot translation prompt.

The prompt has one job: make the model produce target-language text that is
structurally interchangeable with the source. Every rule of *taste* comes from
the track's `requirements.md`, which is injected verbatim and is authoritative.
Everything this module adds is *mechanical*: which blocks, how many lines each,
and how to lay the answer out so it can be parsed back.

The split matters. If a style decision creeps into this file it becomes
invisible to the human who edits `requirements.md`, and the two drift apart.
"""

from __future__ import annotations

from structure import Block, Section

SYSTEM_INSTRUCTION = """\
You are a translator of classical Buddhist literature working inside a \
philological pipeline. Your output is parsed by a script and rejected \
automatically if its structure does not match the source exactly.

Three rules override every other consideration:

1. STRUCTURE IS A CONTRACT. Emit exactly one output block per source block, in \
source order, with exactly the number of lines the source block has, ending \
with that block's ID. Never merge, split, skip, reorder, renumber or invent a \
block.
2. MEANING IS A CONTRACT. Translate what the source says — no additions, no \
omitted lines, no explanatory clauses smuggled in, no metaphor swapped for a \
modern equivalent, no doctrinal term softened into a vague synonym.
3. THE STYLE CONTRACT GOVERNS EVERYTHING ELSE. The requirements document \
supplied in the prompt decides register, vocabulary, loanword policy, \
punctuation and layout. Where your instincts and that document disagree, the \
document wins.

Output the translated blocks and nothing else: no preamble, no commentary, no \
code fences, no notes about your choices.
"""


def _fmt_source_block(b: Block, ref_lines: list[str] | None) -> str:
    """Render one source block for the prompt, with its reference parallel."""
    lines = b.stripped_lines()
    parts = [f"[BLOCK ^{b.block_id}] ({len(lines)} line{'s' if len(lines) != 1 else ''})"]
    parts += [f"  {ln}" for ln in lines]
    if ref_lines:
        parts.append("  --- reference parallel (for disambiguation only, do not translate from it):")
        parts += [f"  > {ln}" for ln in ref_lines]
    return "\n".join(parts)


def _fmt_heading_block(b: Block) -> str:
    text = b.lines[0]
    return f"[HEADING ^{b.block_id}] (markdown level {b.heading_level})\n  {text}"


def build_prompt(
    *,
    blocks: list[Block],
    reference_map: dict[str, list[str]] | None,
    requirements_text: str,
    requirements_path: str,
    source_lang: str,
    target_lang: str,
    reference_lang: str | None,
    termbase_text: str | None = None,
    carryover: str | None = None,
    repair_errors: list[str] | None = None,
    previous_attempt: str | None = None,
) -> str:
    """Assemble the full user prompt for one window of blocks."""
    sections: list[str] = []

    sections.append(
        f"# Task\n\n"
        f"Translate the {source_lang} source blocks below into {target_lang}.\n"
    )

    # --- the style contract, verbatim and authoritative ---------------------
    sections.append(
        "# Style contract (authoritative)\n\n"
        f"The following is `{requirements_path}`. It governs register, "
        "vocabulary, loanword policy, punctuation and layout for this track. "
        "Follow it to the letter.\n\n"
        "<requirements>\n" + requirements_text.strip() + "\n</requirements>\n"
    )

    if termbase_text:
        sections.append(
            "# Termbase (locked renderings)\n\n"
            "Every term listed here must be rendered exactly as specified. Do "
            "not substitute a synonym.\n\n"
            "<termbase>\n" + termbase_text.strip() + "\n</termbase>\n"
        )

    # --- the mechanical contract -------------------------------------------
    ref_note = ""
    if reference_map and reference_lang:
        ref_note = (
            f"\nSome blocks carry a {reference_lang} reference parallel, marked "
            f"`>`. It exists to resolve ambiguity in the {source_lang} — a "
            f"homonym, an unclear line break, a philosophical term. The "
            f"{source_lang} is the meaning base and wins wherever the two "
            f"genuinely differ. Never translate from the reference, and never "
            f"reproduce it in your output.\n"
        )

    sections.append(
        "# Output format (mechanically enforced)\n\n"
        "For each source block, emit the translated lines followed by the "
        "block ID, then one blank line. Layout:\n\n"
        "```\n"
        "<translated line 1>\n"
        "<translated line 2>\n"
        "<translated final line> ^<BLOCK-ID>\n"
        "```\n\n"
        "- The block ID goes on the final line, preceded by a single space.\n"
        "- The line count of each output block must equal the line count "
        "stated for that source block.\n"
        "- Emit the blocks in the order given, all of them, none extra.\n"
        "- For a `[HEADING …]` block, emit a single line: the same markdown "
        "heading marker, the same numeric prefix if present, the translated "
        "heading text, then the block ID.\n"
        "- Line-break style (hard breaks, trailing spaces, capitalisation) is "
        "governed by the style contract above.\n"
        + ref_note
    )

    if carryover:
        sections.append(
            "# Preceding context (already translated — do not re-emit)\n\n"
            "The block immediately before this window came out as:\n\n"
            "<preceding>\n" + carryover.strip() + "\n</preceding>\n\n"
            "Continue from it without repeating it. If a sentence runs across "
            "the boundary, honour it.\n"
        )

    # --- the blocks ---------------------------------------------------------
    rendered: list[str] = []
    for b in blocks:
        if b.is_heading:
            rendered.append(_fmt_heading_block(b))
        else:
            ref = reference_map.get(b.block_id) if reference_map else None
            rendered.append(_fmt_source_block(b, ref))

    sections.append(
        f"# Source blocks ({len(blocks)} to translate)\n\n"
        + "\n\n".join(rendered)
        + "\n"
    )

    # --- repair pass --------------------------------------------------------
    if repair_errors:
        sections.append(
            "# Repair required\n\n"
            "Your previous attempt failed the structural check with these "
            "errors:\n\n"
            + "\n".join(f"- {e}" for e in repair_errors)
            + "\n\nRe-emit the complete set of blocks, fixing every error "
            "listed. Keep the wording you already had wherever it was not at "
            "fault; change only what the errors require.\n"
        )
        if previous_attempt:
            sections.append(
                "<previous_attempt>\n" + previous_attempt.strip()
                + "\n</previous_attempt>\n"
            )

    sections.append(
        f"Now output the {len(blocks)} translated blocks in {target_lang}, and "
        "nothing else."
    )

    return "\n\n---\n\n".join(sections)


def window_label(section: Section, index: int, total: int) -> str:
    if total == 1:
        return f"section-{section.key}"
    return f"section-{section.key}-part-{index + 1:02d}"
