# Jingzhou Hu — Personal Website

Source for [jingzhouhu.github.io](https://jingzhouhu.github.io), built with Jekyll and the AcademicPages theme.

## Content

- `_pages/about.md`: main page
- `_pages/more.md`: mentoring, side projects, and interests page
- `_data/selected_publications.yml`: publication cards shown on the site
- `_config.yml`: site metadata, author links, and build exclusions
- `_sass/_page.scss`: custom page components

The top navigation and CV page are intentionally disabled. Unused AcademicPages demo content has been removed so the repository contains only the active site and its theme dependencies.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000` after the server starts.
