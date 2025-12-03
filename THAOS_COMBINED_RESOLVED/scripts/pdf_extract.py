#!/usr/bin/env python3
# pdf_extract.py - extract text from a PDF to a TXT file using PyPDF2
import sys
from pathlib import Path
try:
    from PyPDF2 import PdfReader
except Exception:
    print('PyPDF2 required. Install: pip install PyPDF2')
    raise
def extract(src, dest):
    reader = PdfReader(str(src))
    pages = []
    for p in reader.pages:
        pages.append(p.extract_text() or '')
    Path(dest).write_text('\n'.join(pages), encoding='utf-8')
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: pdf_extract.py input.pdf output.txt')
        sys.exit(1)
    extract(sys.argv[1], sys.argv[2])
