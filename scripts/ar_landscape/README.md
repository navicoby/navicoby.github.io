# 증강현실과 조경 웹판 관리

Published route: `/augmented-reality-landscape/`.

This folder builds the static library from the checked-in Markdown in
`static/augmented-reality-landscape/text/`. It does not read or modify the local
Obsidian vault. The original Markdown/PDF downloads are immutable snapshots;
their hashes and source filenames are in `downloads/source-manifest.json`.

## Update

1. Edit chapter Markdown, the three editorial articles, or `text/chapters.json`.
2. Install the pinned build dependencies in an isolated environment:
   `python3 -m pip install -r scripts/ar_landscape/requirements.txt`.
3. Run `python3 scripts/ar_landscape/build.py`.
4. Run `python3 scripts/ar_landscape/check.py` and `node --check static/augmented-reality-landscape/assets/site.js`.
5. Build Hugo and run the repository's `scripts/check_static_navigation.py`.
6. Commit source and generated files together. The existing `main` workflow
   publishes them through Hugo to `gh-pages`; do not update only `gh-pages`.

The HTML contains the full reading content without requiring JavaScript or a
remote Markdown parser. JavaScript progressively adds local full-text search,
literature filters, and mobile table-of-contents behavior. All new assets are
local. `v1.html` and `manuscript-v1.md` preserve the prior web edition unchanged.

## Editorial scope

The 33 chapter numbers contain 29 full chapters and four explicitly planned
chapters (2, 3, 7, 8). Chapters 20 and 21 were recovered from the collected
Obsidian manuscript. Chapters 26, 28 and 33 have scoped editorial corrections;
the website records these corrections. The 140 literature entries are source
records, not a deduplicated count of independent studies. The website does not
claim that every original factual assertion has been reverified.

Validation covers local links and fragments, nontruncated chapter exports,
unique headings, search targets, record counts, original file hashes and local
path disclosure. Browser checks should cover search, empty search results,
literature filters and resets, chapter navigation, mobile layout and tables.
