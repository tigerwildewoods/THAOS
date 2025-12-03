#!/usr/bin/env python3
# cleaner.py - simplified Stage A-E cleaning
import re, sys
from pathlib import Path
def clean_text(t):
    t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)   # fix hyphenated breaks
    t = re.sub(r'\r', '\n', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    t = re.sub(r'[ \t]+', ' ', t)
    lines = [ln.strip() for ln in t.splitlines() if ln.strip() and not ln.strip().isdigit()]
    return '\n'.join(lines)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: cleaner.py input.txt output.txt')
        sys.exit(1)
    s = Path(sys.argv[1]).read_text(encoding='utf-8')
    Path(sys.argv[2]).write_text(clean_text(s), encoding='utf-8')
