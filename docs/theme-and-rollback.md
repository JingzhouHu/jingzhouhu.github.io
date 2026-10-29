# Theme provenance and rollback

## Active theme

The homepage and Publications page adapt [Minimal Light by Yaoyao Liu](https://github.com/yaoyao-liu/minimal-light), upstream commit `dd114c3fef2d97adc1c6b6d46901e0d96ab83a7c`.

- `_sass/_minimal-light-base.scss` vendors the upstream light-only stylesheet, `_sass/minimal-light-no-dark-mode.scss`.
- `_layouts/minimal-light.html` adapts its sidebar-and-content layout with semantic HTML, the existing SEO include, explicit profile-link labels, and section navigation.
- `_sass/_minimal-light-overrides.scss` customizes the palette to white (`#ffffff`), navy (`#17283c`), and blue (`#284fc5`), and uses system sans-serif fonts. It also replaces fixed positioning with a sticky sidebar, adds mobile and keyboard support, and styles the existing data-driven publication cards.
- No upstream demo content, tracking, external font/icon libraries, or JavaScript is loaded.
- The upstream CC0 license is retained at `docs/licenses/minimal-light-CC0.txt`. The existing repository license remains unchanged.

The three selected papers' author names and order were checked against the NeurIPS proceedings and Kejun Huang's public publication list at https://cise.ufl.edu/~kejun/papers.html. All three list Jingzhou Hu followed by Kejun Huang.

## Saved previous version

The complete previous custom profile is preserved in the remote branch:

`archive/custom-profile-2026-10-28`

Its commit is `fa2d20ea03fdca014c40f2bc17f6c22c2b381bbc`. It includes the compact portrait, gray-white background, publication-first layout, and hidden GitHub profile link as they were immediately before this migration. Keep this archive branch unchanged.

The old `_layouts/profile.html`, `_sass/_profile.scss`, and `assets/css/profile.scss` are also retained in the active tree. Restoring those alone is insufficient because the page markup changed.

## Rollback procedure

For an immediate rollback, revert the single squash commit for the Minimal Light migration in a new branch, run the production build and link checks, then merge through a pull request. This preserves Git history and triggers the normal Pages deployment.

If later content changes must be retained, restore the previous layout and styling from the archive branch and adapt the current page content to its markup. Review the publication data separately so new papers are not lost.

Do not force-reset the deployment branch. After either rollback, check the live homepage, Publications page, and legacy `/me/` redirects.
