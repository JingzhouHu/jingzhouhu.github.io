# Jingzhou Hu — Personal Website

Source for [jingzhouhu.github.io](https://jingzhouhu.github.io), built with Jekyll and AcademicPages. The site remains static and works without JavaScript.

## Maintain content

- `_pages/about.md`: biography, research focus, and academic service.
- `_data/selected_publications.yml`: ordered publication records, shared by the homepage and `/publications/`.
- `_includes/publication-card.html`: one shared card template.
- `_sass/_custom.scss`: site-specific layout and components; keep changes out of the theme styles.
- `_config.yml`: metadata and profile links. `author.links` supports a label, icon, and URL.
- `_pages/more.md`: an unpublished draft. Replace its placeholder prose before setting `published: true`; the homepage discovers and links the published page automatically.

Top navigation items and a CV page remain intentionally disabled. Legacy theme JavaScript remains in the repository for reference but is not loaded; the active layout uses CSS and native HTML. `package.json` is the legacy theme build configuration, not a required build step for this site.

## Publications

Keep records in display order. Required fields: `title`, `url` (paper URL), `venue`, `year`, and `contribution`. Optional fields: `authors`, `image`, `image_alt`, `code_url`, `project_url`, and multiline `bibtex`. Omitted resources do not render buttons. BibTeX uses a native expandable block and does not require a script.

Use a short, factual contribution sentence. Add only verified public URLs and bibliographic information. Thumbnail images should show the complete figure; the current 800 × 600 WebP derivatives preserve the original PNG files in `assets/img/papers/`.

## Local preview and checks

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. To validate a release:

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

The pull-request workflow builds with the GitHub Pages dependencies and validates generated routes and local links. It does not deploy. External paper and profile URLs should also be checked before release.

## Release later

Keep the preparation branch unmerged until the research update is ready. See [the release checklist](docs/release-checklist.md). Merging into the configured GitHub Pages source branch may publish the changes.
