# THAOS Wiki — MkDocs source

This repository contains the MkDocs source for the THAOS Wiki.

To publish:
1. Push this repo to GitHub (example: tigerwildewoods/THAOS).
2. Ensure the GitHub Action `Deploy MkDocs site` exists (it is included).
3. On push to `main`/`master`, the Action will build the site and publish to GitHub Pages.

Files of interest:
- `mkdocs.yml` — site configuration
- `docs/` — markdown content (index + sections)
- `assets/` — images and maps
- `.github/workflows/mkdocs.yml` — CI workflow to build & deploy

You can edit and extend the `docs/` folder to add characters, locations, and more.
