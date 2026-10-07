# bpcn-lab.github.io

Website of the **Department of Biological Psychology and Cognitive Neuroscience (BPCN)**, Faculty of Social and Behavioural Sciences, Friedrich Schiller University Jena.

Built with [Quarto](https://quarto.org) and deployed to GitHub Pages. Owned and maintained by the `bpcn-lab` organization. This site links to, but is independent from, the [Archila Research](https://github.com/ArchilaResearch) site.

## Local development

Requires [Quarto ≥ 1.6](https://quarto.org/docs/get-started/) and Node ≥ 20.

```bash
npm run build           # build both languages → _site/ (English) and _site/de/ (German)
npm run check           # validate metadata + internal links (after a build)
npm run people          # regenerate people.qmd and de/people.qmd from scripts/build_people.py
quarto preview          # live preview of the English site only
```

`npm run check` runs the same gates as CI: metadata validation and internal-link checking. External links are checked separately on a weekly schedule (warning only).

## Two languages

English is the default and lives at the site root. The German edition is a separate Quarto project in `de/` (own navigation, footer, and `_variables.yml`) that renders into `_site/de/` and shares the theme, assets, and scripts with the English site. Every English page has a German counterpart with the same file name; the navbar language link switches between them.

- Edit a page in both languages: `about.qmd` and `de/about.qmd`.
- German pages reference shared files as `../assets/...` (an `/assets/...` path would resolve inside `de/`). `de/assets` is a symlink to `../assets` so the German build can find assets referenced from the theme.
- The publication list is written once, in `_publications-list.qmd`, and included by both publication pages.
- The People pages are generated: edit `scripts/build_people.py`, then run `npm run people`.

## Where things live

| Path | What |
|---|---|
| `_variables.yml`, `de/_variables.yml` | **Site settings**: names, affiliation, contacts. Edit here, not in pages. |
| `_quarto.yml`, `de/_quarto.yml` | Navigation, footer, theme wiring for each language. |
| `*.qmd`, `de/*.qmd` | Page content in English and German. |
| `_publications-list.qmd` | The shared publication list. |
| `content/` | Structured content (people, research, publications), empty at launch. |
| `styles/theme.scss` | Design tokens (institutional identity), shared by both languages. |
| `includes/lang-switch.html` | Points the language link at the current page's counterpart. |
| `scripts/` | `validate.mjs`, `check-internal-links.mjs`, `build_people.py`. |
| `.github/` | CI workflows and issue forms. |

## Contributing

You don't need to write code. Use an [issue form](../../issues/new/choose). See [`CONTRIBUTING.md`](CONTRIBUTING.md). Governance, ownership, domains, handover, and backups are in [`GOVERNANCE.md`](GOVERNANCE.md).

## Deployment

Pushing to `main` triggers build → validate → internal-link check → deploy to GitHub Pages (`.github/workflows/publish.yml`). `main` stays deployable; work on branches and open pull requests.
