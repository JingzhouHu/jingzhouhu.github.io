# Jingzhou Hu — Personal Website

Source for [jingzhouhu.github.io](https://jingzhouhu.github.io), built with Jekyll using an adapted Minimal Light layout with a white background, navy headings, and blue links. AcademicPages templates remain for supporting pages. The site stays static and works without JavaScript.

## Maintain content

- `_pages/about.md`: biography, research focus, and academic service.
- `_data/selected_publications.yml`: ordered publication records, shared by the homepage and `/publications/`.
- `_includes/publication-card.html`: one shared card template.
- `_layouts/minimal-light.html`: active two-column layout, profile, and navigation.
- `_sass/_minimal-light-base.scss`: vendored Minimal Light styles; keep upstream attribution.
- `_sass/_minimal-light-overrides.scss`: local colors, typography, publication cards, and responsive styling.
- `_layouts/profile.html` and `_sass/_profile.scss`: retained previous custom layout; the complete previous version is also archived in Git.
- `_sass/_custom.scss`: overrides for retained AcademicPages layouts.
- `_config.yml`: metadata and profile links. `author.links` supports a label, icon, and URL.
- `_pages/more.md`: an unpublished draft. Replace its placeholder prose before setting `published: true`; the homepage discovers and links the published page automatically.

The homepage navigation links to About, Publications, Research, and Service. A CV page remains disabled, and the GitHub profile link stays hidden until configured. Legacy theme JavaScript remains in the repository for reference but is not loaded; the active layout uses system fonts, CSS, and native HTML. `package.json` is the legacy theme build configuration, not a required build step for this site. See [theme provenance and rollback](docs/theme-and-rollback.md) for upstream details and the saved previous version.

## Publications

Keep records in display order. Required fields: `title`, `url` (paper URL), `venue`, `year`, and `contribution`. Optional fields: `author_list` (ordered array of full names), `authors` (legacy plain text), `image`, `image_alt`, `code_url`, `project_url`, and multiline `bibtex`. `author_list` highlights the exact name configured in `site.author.name`. Omitted resources do not render buttons. BibTeX uses a native expandable block and does not require a script.

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
