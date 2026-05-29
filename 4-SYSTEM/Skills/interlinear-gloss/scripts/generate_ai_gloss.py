#!/usr/bin/env python3
"""Generate an interlinear gloss file for the AI translation using the Rhys Davids gloss as reference.

Reads the Rhys Davids gloss file (pi-en-rd-gloss.md) and the AI translation file (en-dhammasangani-ai.md).
For each block, it aligns the Pāli tokens and matches the Rhys Davids gloss tokens against the AI translation's free translation.
If a word (or its synonym) is found in the AI translation, it uses it verbatim.
Otherwise, it falls back to the Rhys Davids gloss in parentheses.

Usage:
    python3 generate_ai_gloss.py
"""
import re
import sys
from pathlib import Path

# Determine vault root relative to this script's directory
SCRIPT_DIR = Path(__file__).resolve().parent
# Since this script is in 4-SYSTEM/Skills/interlinear-gloss/scripts/ (4 levels deep),
# the vault root is 4 levels up.
if len(SCRIPT_DIR.parents) >= 4:
    VAULT_ROOT = SCRIPT_DIR.parents[3]
else:
    VAULT_ROOT = Path(".")

# Paths resolved relative to the vault root
RD_GLOSS_PATH = VAULT_ROOT / "2-RAILS/Bilingual-Glossaries/Raw/pi-en-rd-gloss.md"
AI_TRANS_PATH = VAULT_ROOT / "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md"
OUTPUT_PATH = VAULT_ROOT / "2-RAILS/Bilingual-Glossaries/Raw/pi-en-ai-gloss.md"

# Synonym mapping for smart alignment
SYNONYMS = {
    "good": ["wholesome", "good"],
    "bad": ["unwholesome", "bad"],
    "states": ["states", "phenomena", "phenomenon", "state"],
    "pleasure": ["pleasant", "happiness", "joy", "pleasure"],
    "ease": ["happiness", "pleasant", "ease"],
    "neutral": ["neither-painful-nor-pleasant", "neutral", "neither-painful-nor-pleasant-feeling"],
    "indifference": ["equanimity", "indifference"],
    "applied_thinking": ["initial_application", "applied_thought", "initial-application"],
    "applied_thought": ["initial_application", "applied_thought", "initial-application"],
    "sustained_thinking": ["sustained_application", "sustained_thought", "sustained-application"],
    "disinterestedness": ["non-greed", "disinterestedness", "non-greediness"],
    "absence_of_hate": ["non-hatred", "absence_of_hate", "non-ill-will"],
    "absence_of_dullness": ["non-delusion", "absence_of_dullness", "non-delusion-root"],
    "absence_of_covetousness": ["non-covetousness", "absence_of_covetousness"],
    "absence_of_malice": ["non-ill-will", "absence_of_malice", "non-ill-will"],
    "right_disposing": ["right_intention", "right-intention"],
    "right_disposing_": ["right_intention", "right-intention"],
    "right_endeavour": ["right_effort", "right-effort", "right_endeavour"],
    "representative_intellection": ["mind-consciousness", "representative_intellection", "mind-consciousness-element"],
    "representative_imagination": ["mind", "representative_imagination", "mind-faculty"],
    "ideation": ["mind", "ideation", "mind-base"],
    "intellection": ["consciousness", "intellection", "cognition"],
    "skandha_of_intellection": ["consciousness_aggregate", "aggregate_of_consciousness"],
    "skandha_of_consciousness": ["consciousness_aggregate", "aggregate_of_consciousness"],
    "skandha_of_feeling": ["feeling_aggregate", "aggregate_of_feeling"],
    "skandha_of_perception": ["perception_aggregate", "aggregate_of_perception"],
    "skandha_of_synergies": ["volitional_formations_aggregate", "aggregate_of_mental_formations", "aggregate_of_formations", "formations_aggregate"],
    "synergies": ["formations", "mental_formations", "volitional_formations"]
}

# Reverse mapping for quick lookup of base keys
SYN_LOOKUP = {}
for k, vals in SYNONYMS.items():
    for val in vals:
        SYN_LOOKUP[val.lower()] = k

def clean_word(w):
    """Strip parentheses, punctuation, and convert to lowercase."""
    cleaned = w.strip("().,;:!?\"'()[]{}—–").lower()
    return cleaned

def parse_blocks(path):
    """Return {block_id: paragraph_text} for translation file. Skip headings and frontmatter."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    blocks = {}
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph or paragraph.startswith("#"):
            continue
        match = re.search(r"\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", paragraph)
        if not match:
            continue
        block_id = match.group(1)
        body = paragraph[: match.start()].rstrip()
        blocks[block_id] = body
    return blocks

def parse_rd_gloss(path):
    """Parse the reference gloss file and return a list of block dicts."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+\^([0-9A-Za-z][0-9A-Za-z\-]*)\s*$", text, flags=re.MULTILINE)
    blocks = []
    for i in range(1, len(parts), 2):
        block_id = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""
        
        # Extract \gla and \glb lines
        gloss_match = re.search(r"```gloss\s*\n(.*?)\n```", section, re.DOTALL)
        if gloss_match:
            lines = gloss_match.group(1).strip().splitlines()
            gla_tokens = []
            glb_tokens = []
            for line in lines:
                if line.startswith("\\gla"):
                    gla_tokens = line[4:].strip().split()
                elif line.startswith("\\glb"):
                    glb_tokens = line[4:].strip().split()
            if gla_tokens and glb_tokens:
                blocks.append({
                    "block_id": block_id,
                    "gla_tokens": gla_tokens,
                    "glb_tokens": glb_tokens
                })
    return blocks

def find_verbatim_match(ref_token, target_words):
    """Try to find a verbatim match or synonym of ref_token in target_words."""
    # Clean the reference token
    clean_ref = clean_word(ref_token)
    if not clean_ref or clean_ref == "--":
        return None
    
    # Check if the reference token itself (without parens/underscores) is in target_words
    ref_parts = clean_ref.split("_")
    all_parts_found = True
    matched_words = []
    for part in ref_parts:
        found_part = False
        for tw in target_words:
            if clean_word(tw) == part:
                matched_words.append(tw)
                found_part = True
                break
        if not found_part:
            all_parts_found = False
            break
            
    if all_parts_found and matched_words:
        # Reconstruct with underscores using the exact casing from target_words if possible
        return "_".join(matched_words)

    # Check synonyms
    # Find the base key in synonyms
    base_key = SYN_LOOKUP.get(clean_ref)
    if not base_key:
        # Try checking if any part of the ref has a synonym
        for part in ref_parts:
            if part in SYN_LOOKUP:
                base_key = SYN_LOOKUP[part]
                break
                
    if base_key:
        syns = SYNONYMS[base_key]
        for syn in syns:
            syn_parts = syn.split("_")
            # Check if all parts of this synonym are in target_words
            all_syn_parts_found = True
            matched_syn_words = []
            for spart in syn_parts:
                found_spart = False
                for tw in target_words:
                    if clean_word(tw) == spart:
                        matched_syn_words.append(tw)
                        found_spart = True
                        break
                if not found_spart:
                    all_syn_parts_found = False
                    break
            if all_syn_parts_found and matched_syn_words:
                return "_".join(matched_syn_words)
                
    return None

def main():
    print("Loading files...")
    print(f"Vault root detected at: {VAULT_ROOT.resolve()}")
    if not RD_GLOSS_PATH.exists():
        print(f"Error: Reference gloss file not found at {RD_GLOSS_PATH}")
        sys.exit(1)
    if not AI_TRANS_PATH.exists():
        print(f"Error: AI translation file not found at {AI_TRANS_PATH}")
        sys.exit(1)
        
    rd_blocks = parse_rd_gloss(RD_GLOSS_PATH)
    ai_trans_blocks = parse_blocks(AI_TRANS_PATH)
    
    print(f"Parsed {len(rd_blocks)} reference blocks and {len(ai_trans_blocks)} AI translation blocks.")
    
    out_lines = []
    out_lines.append("---")
    out_lines.append("source_file: 1-SOURCES/Text/pi-1.md")
    out_lines.append("source_language: pi")
    out_lines.append("target_file: 3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/en-dhammasangani-ai.md")
    out_lines.append("target_language: English")
    out_lines.append("target_lang_tag: en-ai")
    out_lines.append("translator: AI (CSCD-aligned, tipitaka.org Mūla edition)")
    out_lines.append(f"total_verses: {len(rd_blocks)}")
    out_lines.append("status: draft")
    out_lines.append("---")
    out_lines.append("")
    out_lines.append("# Interlinear gloss — Pāli → English (AI)")
    out_lines.append("")
    
    matched_count = 0
    fallback_count = 0
    
    for block in rd_blocks:
        block_id = block["block_id"]
        gla_tokens = block["gla_tokens"]
        ref_glb_tokens = block["glb_tokens"]
        
        target_ex = ai_trans_blocks.get(block_id, "")
        if not target_ex:
            # If no target translation, skip or use empty
            continue
            
        # Clean target ex into words for matching
        target_words = target_ex.split()
        
        new_glb_tokens = []
        for i, gla_token in enumerate(gla_tokens):
            if i >= len(ref_glb_tokens):
                new_glb_tokens.append("--")
                continue
                
            ref_glb = ref_glb_tokens[i]
            
            # Try to find a match in the target translation
            match = find_verbatim_match(ref_glb, target_words)
            if match:
                # Keep target casing
                new_glb_tokens.append(match)
                matched_count += 1
            else:
                # Fallback to reference gloss in parentheses
                clean_ref = ref_glb.strip("()")
                new_glb_tokens.append(f"({clean_ref})")
                fallback_count += 1
                
        out_lines.append(f"## ^{block_id}")
        out_lines.append("")
        out_lines.append("```gloss")
        out_lines.append(f"\\gla    {'   '.join(gla_tokens)}")
        out_lines.append(f"\\glb    {'   '.join(new_glb_tokens)}")
        out_lines.append(f"\\ex     {target_ex}")
        out_lines.append("```")
        out_lines.append("")
        
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Successfully generated {OUTPUT_PATH}!")
    print(f"Total matched tokens: {matched_count}")
    print(f"Total fallback tokens: {fallback_count}")

if __name__ == "__main__":
    main()
