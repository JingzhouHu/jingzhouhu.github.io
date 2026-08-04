# Jingzhou Hu — Personal Website

Source for [jingzhouhu.github.io](https://jingzhouhu.github.io), built with Jekyll and the AcademicPages theme.

## Content

- `_pages/about.md`: main page
- `_pages/more.md`: mentoring, side projects, and interests page
- `_data/selected_publications.yml`: publication cards shown on the site
- `_config.yml`: site metadata, author links, and build exclusions
- `_sass/_page.scss`: custom page components

The top navigation and CV page are intentionally disabled. Template demo content remains in the repository for reference but is excluded from the generated site.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000` after the server starts.
