#!/usr/bin/env python3
# merge_into_master.py - append unique lines from a folder into master dedupe
import sys, glob
from pathlib import Path
if len(sys.argv) < 3:
    print('Usage: merge_into_master.py cleaned_folder master_dedupe.txt')
    raise SystemExit(1)
clean_dir = Path(sys.argv[1])
master = Path(sys.argv[2])
master_lines = set(master.read_text(encoding='utf-8').splitlines()) if master.exists() else set()
added = 0
for f in sorted(clean_dir.glob('*.txt')):
    for line in f.read_text(encoding='utf-8').splitlines():
        s = line.strip()
        if s and s not in master_lines:
            master_lines.add(s); added += 1
if added:
    master.write_text('\n'.join(sorted(master_lines)), encoding='utf-8')
print(f'Added {added} new lines to {master}')
