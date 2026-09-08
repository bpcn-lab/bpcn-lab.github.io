# bpcn-lab.github.io

Website of the **Department of Biological Psychology and Cognitive Neuroscience (BPCN)**, Faculty of Social and Behavioural Sciences, Friedrich Schiller University Jena.

Built with [Quarto](https://quarto.org) and deployed to GitHub Pages. Owned and maintained by the `bpcn-lab` organization. This site links to, but is independent from, the [Archila Research](https://github.com/ArchilaResearch) site.

## Local development

Requires [Quarto ≥ 1.6](https://quarto.org/docs/get-started/) and Node ≥ 20.

```bash
quarto preview          # live local preview
quarto render           # one-command build → _site/
npm run check           # validate metadata + internal links (after a render)
```

`npm run check` runs the same gates as CI: metadata validation and internal-link checking. External links are checked separately on a weekly schedule (warning only).

## Where things live

| Path | What |
|---|---|
| `_variables.yml` | **Site settings**: names, affiliation, contacts. Edit here, not in pages. |
| `_quarto.yml` | Navigation, footer, theme wiring. |
| `*.qmd` | Page content (home, research, people, publications, join, about, contact, legal pages). |
| `content/` | Structured content (people, research, publications), empty at launch. |
| `styles/theme.scss` | Design tokens (institutional identity). |
| `scripts/` | `validate.mjs`, `check-internal-links.mjs`. |
| `.github/` | CI workflows and issue forms. |

## Contributing

You don't need to write code. Use an [issue form](../../issues/new/choose). See [`CONTRIBUTING.md`](CONTRIBUTING.md). Governance, ownership, domains, handover, and backups are in [`GOVERNANCE.md`](GOVERNANCE.md).

## Deployment

Pushing to `main` triggers build → validate → internal-link check → deploy to GitHub Pages (`.github/workflows/publish.yml`). `main` stays deployable; work on branches and open pull requests.
