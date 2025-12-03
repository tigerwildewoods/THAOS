#!/usr/bin/env bash
OUT=THAOS_FULL_RESTORE_PACKAGE_$(date +%Y%m%d_%H%M%S).zip
echo "Creating $OUT ..."
zip -r "$OUT" data docs scripts .github LICENSE README.md || true
echo "Backup created: $OUT"
