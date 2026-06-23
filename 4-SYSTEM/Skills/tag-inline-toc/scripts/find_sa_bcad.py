#!/usr/bin/env python3
"""
DEPRECATED — do not use.

This was a rule/regex pre-filter for sa bcad detection. It has been retired:
Phase 1 of the tag-inline-toc skill is now done ENTIRELY by the model, reading
for meaning. Rule-based detection cannot separate genuine sa bcad from
look-alikes (verse quotations, incidental lists) and cannot find verbatim term
boundaries — every rule spawns exceptions, and tuning it is an endless loop.

The only script in this skill is the Phase-2 renderer, tag_inline_toc.py.

See SKILL.md → "Phase 1 is model-only" and the Procedure (Steps 1-5).
"""
import sys

print(__doc__, file=sys.stderr)
sys.exit(2)
