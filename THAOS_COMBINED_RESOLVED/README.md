# Merged README

## Main README

# THAOS — Full GitHub Repository (v2)

This repository is the canonical home for the THAOS worldbuilding project.
It contains data, restore tools, ingestion scripts, CI workflows, and docs.

Folders:
- `data/` — canonical THAOS files (master, categorized, pipeline, etc.)
- `scripts/` — local utilities and ingestion scripts (doink pipeline)
- `.github/workflows/` — GitHub Actions workflows (validate, deploy, backup, ingest)
- `docs/` — GitHub Pages content generated from `data/`

Instructions:
1. Replace any `PLACEHOLDER` files in `data/` with your real THAOS files.
2. Commit & push to GitHub (create a new repository named `THAOS`).
3. Enable GitHub Pages in repo settings (use `docs/` folder).
4. Optionally set secrets (GITHUB_TOKEN is provided by Actions automatically).

See `docs/` for quick reference pages.


---

## THAOS_INBOX README

# THAOS_INBOX — New Material Staging Area

Use this folder to add new worldbuilding material, loose notes, PDFs, TXT files, drafts, or any content intended to be added to the THAOS canon.

## Folder Structure
- `ideas/` — quick notes, fragments, brainstorms
- `drafts/` — early story drafts or partial chapters
- `expansions/` — lore expansions intended for canon
- `raw_txt/` — unprocessed text files
- `raw_pdf/` — PDFs for extraction
- `misc/` — everything else

### How to Ingest
After adding files, tell ChatGPT:

**"Process THAOS_INBOX"**

ChatGPT will:
1. Extract text (PDF/TXT)
2. Clean & normalize it
3. Dedupe against the master corpus
4. Classify into canonical sections
5. Merge into THAOS master files
6. Provide updated GitHub-ready files
