# Governance: bpcn-lab.github.io

This single document covers ownership, domains/services, handover, and backups.

## Ownership & decision rights

- **Institutional identity, branding, and claims:** Prof. Dr. Gyula Kovács and authorized department representatives have final authority.
- **Technical maintenance:** the repository maintainers.
- **This repository must have at least two authorized owners.** List them here once appointed.

| Owner | Role | GitHub | Since |
|---|---|---|---|
| _TBD_ | Owner | _TBD_ | n/a |
| _TBD_ | Owner (backup) | _TBD_ | n/a |

## Content ownership register

Lab-wide identity, people, facilities, and institutional content are owned here. The product owner's biography, independently led projects, courses, software, and future-group identity are owned by **[Archila Research](https://github.com/ArchilaResearch)** and only summarized-and-linked here. Joint items record their single canonical owner in the item's metadata.

## Domain & service register

| Service | Address | Controlled by |
|---|---|---|
| Site (fallback) | `bpcn-lab.github.io` | GitHub org `bpcn-lab` |
| Custom domain | _TBD (e.g. a `uni-jena.de` subdomain, per institutional policy)_ | Institution |
| Contact email | `sekretariat.bpcn@uni-jena.de` | Department |
| Source | `github.com/bpcn-lab/bpcn-lab.github.io` | GitHub org |

## Handover / departure checklist

- [ ] At least two org owners with 2FA enabled.
- [ ] No single maintainer holds sole access to domain or deployment.
- [ ] A second maintainer has completed a test deploy.
- [ ] `_variables.yml` holds all site-specific settings (no secrets in the repo).
- [ ] Backup of content verified (see below).

## Backup & recovery

The full site is version-controlled in Git; the repository is the backup. To recover: clone, run the build (see `README.md`), and redeploy via the GitHub Actions workflow. Keep GitHub org recovery codes in an institutional secure store.

## Security

See [`SECURITY.md`](SECURITY.md).
