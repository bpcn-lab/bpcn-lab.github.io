# Security policy: bpcn-lab.github.io

## Reporting

Report security or privacy concerns (including accidentally published sensitive data) to **sekretariat.bpcn@uni-jena.de**. Please do not open a public issue for sensitive reports.

## Practices

- Two-factor authentication is required for all org members; no shared accounts.
- The `main` branch is protected; changes go through pull requests.
- Deployment uses least-privilege GitHub Actions permissions (`contents: read`, `pages: write`, `id-token: write`).
- No secrets are stored in the repository; `_variables.yml` contains only public information.
- Third-party actions are pinned; dependencies are reviewed.

## Incident procedure (accidental sensitive publication)

1. Remove public access (unpublish / make repo private).
2. Rotate any exposed credentials.
3. Notify relevant institutional contacts.
4. Purge repository history if necessary.
5. Invalidate caches where possible.
6. Document the event and strengthen preventive controls.
