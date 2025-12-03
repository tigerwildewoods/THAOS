#!/usr/bin/env bash
# doink_run.sh - example driver for the DOINK pipeline
set -e
INBOX="inbox/pdfs"
EXTRACTED="work/extracted"
CLEANED="work/cleaned"
MASTER="data/THAOS_MASTER_COMBINED_DEDUPE.txt"
mkdir -p "$EXTRACTED" "$CLEANED"
for pdf in "$INBOX"/*.pdf; do
  base=$(basename "$pdf" .pdf)
  python3 scripts/pdf_extract.py "$pdf" "$EXTRACTED/$base.txt"
  python3 scripts/cleaner.py "$EXTRACTED/$base.txt" "$CLEANED/$base.cleaned.txt"
done
python3 scripts/merge_into_master.py "$CLEANED" "$MASTER"
echo "DOINK completed."
