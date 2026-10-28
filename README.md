# Jingzhou Hu — Personal Website

Source for [jingzhouhu.github.io](https://jingzhouhu.github.io), built with Jekyll, with a dedicated profile layout and retained AcademicPages templates for supporting pages. The site remains static and works without JavaScript.

## Maintain content

- `_pages/about.md`: biography, research focus, and academic service.
- `_data/selected_publications.yml`: ordered publication records, shared by the homepage and `/publications/`.
- `_includes/publication-card.html`: one shared card template.
- `_layouts/profile.html` and `_sass/_profile.scss`: homepage and Publications layout, typography, and responsive styling.
- `_sass/_custom.scss`: overrides for retained AcademicPages layouts.
- `_config.yml`: metadata and profile links. `author.links` supports a label, icon, and URL.
- `_pages/more.md`: an unpublished draft. Replace its placeholder prose before setting `published: true`; the homepage discovers and links the published page automatically.

The homepage navigation links to its Research, Publications, and About sections. A CV page remains disabled. Legacy theme JavaScript remains in the repository for reference but is not loaded; the active layout uses CSS and native HTML. `package.json` is the legacy theme build configuration, not a required build step for this site.

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

## Future updates

Add new papers and public research progress when ready. See [the release checklist](docs/release-checklist.md). Use a pull request for each update; merging into the configured GitHub Pages source branch publishes the changes.
