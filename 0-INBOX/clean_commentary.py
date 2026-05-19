import re

def clean_commentary(root_path, comm_path, output_path):
    # Read root verses
    with open(root_path, 'r', encoding='utf-8') as f:
        root_content = f.read()
    
    root_phrases = set()
    for line in root_content.split('\n'):
        # Remove markdown numbering and leading spaces
        line = re.sub(r'^\s*\d+\.\s*', '', line)
        # Split by various delimiters
        parts = re.split(r'[\s \u3000,，。！？]+', line)
        for p in parts:
            p = p.strip()
            # Only consider phrases that look like verses (length >= 4)
            if len(p) >= 4:
                root_phrases.add(p)
    
    # Read commentary
    with open(comm_path, 'r', encoding='utf-8') as f:
        comm_content = f.read()
    
    lines = comm_content.split('\n')
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_lines.append(line)
            continue
            
        # Check if line is a verse block
        # Verses in the commentary often have punctuation like ， and 。
        parts = re.split(r'[\s \u3000,，。！？]+', stripped)
        is_verse = True
        has_content = False
        for p in parts:
            p = p.strip()
            if not p:
                continue
            has_content = True
            # If any non-empty part is NOT a known root phrase, it's commentary
            if p not in root_phrases:
                is_verse = False
                break
        
        if is_verse and has_content:
            # Skip verse line
            continue
        else:
            new_lines.append(line)
            
    # Write cleaned content
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

if __name__ == "__main__":
    import sys
    import os
    
    # In a real environment, we'd use the tool's paths
    # Here I will simulate the logic in the main block
    pass
