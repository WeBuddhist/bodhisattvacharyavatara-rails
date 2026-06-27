#!/usr/bin/env python3
"""
List Gemini models available to your API key that support generateContent.

Usage (from project root, venv activated, GEMINI_API_KEY in environment):
    python 4-SYSTEM/Skills/block-resegmentation/scripts/list_models.py
"""
import os
import sys


def main():
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Error: set GEMINI_API_KEY (or GOOGLE_API_KEY) in the environment.")

    try:
        from google import genai
    except ImportError:
        sys.exit("Error: google-genai not installed. Run: pip install google-genai")

    client = genai.Client(api_key=api_key)

    rows = []
    for m in client.models.list():
        methods = getattr(m, "supported_actions", None) or \
                  getattr(m, "supported_generation_methods", None) or []
        if "generateContent" in methods:
            rows.append(m.name)

    if not rows:
        print("No models supporting generateContent were returned for this key.")
        return

    print("Models supporting generateContent:\n")
    for name in sorted(rows):
        print("  " + name.replace("models/", ""))
    print(f"\n{len(rows)} model(s). Pass one to resegment.py with --model <name>.")


if __name__ == "__main__":
    main()
