# Research update release checklist

The visual foundation is ready to publish independently of future research announcements. Prepare subsequent content updates in a branch, then merge when the public materials are ready. There is no automatic release schedule.

## Add the research update

- Add accepted papers or public preprints to `_data/selected_publications.yml` and choose their display order.
- Verify title, author order, venue, year, public paper URL, and publication status. Do not label an unaccepted paper as accepted.
- Add available `code_url`, `project_url`, and `bibtex` fields. Do not publish empty or speculative links.
- Write one concrete contribution sentence per paper, with a figure that remains readable at thumbnail size.
- Update the biography and research focus only where the public work supports the change.
- Keep unpublished drafts unpublished. Complete `_pages/more.md` before setting `published: true`; remove `sitemap: false` when the page is ready to be indexed.

## Verify and publish

- Incorporate any intervening changes from the deployment branch and resolve conflicts.
- Run the production build and local-link check in the README; confirm the pull-request checks pass.
- Inspect the homepage and Publications page on desktop and a narrow mobile screen. Check keyboard focus and profile links.
- Verify paper, code, project, Scholar, and LinkedIn URLs manually. Check any newly added BibTeX against the source publication.
- Confirm `/me/` redirects to the homepage and `/me/publications/` redirects to Publications.
- Review the complete diff, then merge when ready to publish through GitHub Pages.
- After deployment, verify the live pages and redirects before using the site in an announcement.

`docs/` and `scripts/` are excluded from the generated website.
