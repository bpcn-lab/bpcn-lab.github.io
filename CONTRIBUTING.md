# Contributing: bpcn-lab.github.io

Thank you for helping keep the site accurate. You do **not** need to edit code to contribute.

## Easiest: open an issue

Use an [issue form](https://github.com/bpcn-lab/bpcn-lab.github.io/issues/new/choose) to request a profile update, publication addition, news item, or accessibility/privacy correction. A maintainer will implement it.

## For maintainers: editing content

- Site-wide settings (names, contacts, affiliation) live in `_variables.yml`. Edit there, not in pages.
- Page content is in `*.qmd` files; structured content will live under `content/`.
- Work on a short-lived branch and open a pull request. `main` stays deployable.
- Automated checks (build, metadata, internal links) must pass before merge.

## Adding a person to the People page

Copy this block into the right section of `people.qmd`. **Blank lines around every `:::` fence are required**, otherwise the inner blocks are swallowed into the paragraph above.

```markdown
::: {.person}

::: {.person-photo .placeholder}
AB
:::

::: {.person-body}

### Full Name {#full-name}

::: {.person-role}
Role, BPCN
:::

One short paragraph on research interests and background.

::: {.person-links}
[Email](mailto:) · [Google Scholar]() · [GitHub]() · [Website]()
:::

:::

:::
```

Notes:

- **Portrait.** Put a square image in `assets/people/` and replace the placeholder block with
  `![](assets/people/name.jpg){.person-photo fig-alt="Portrait of Full Name"}`. The two-letter
  placeholder is the fallback until a consented portrait exists.
- **Heading id.** Always give the heading an explicit `{#slug}`. Without it, a name containing a
  `{{< var >}}` shortcode produces a broken anchor, and deep links to the profile stop working.
- **Links.** Delete any that do not apply; do not leave empty `()` targets.
- **Alumni.** Use `::: {.person .alum}` and omit the portrait. Close with a
  `::: {.person-now}Currently: role, organisation:::` line where the destination is known.

## Image & personal-data consent (required)

Before publishing anyone's name, photo, or biography:

1. Obtain the person's consent to appear on the public site.
2. Record it (set `consent_recorded: true` in their entry and note who/when).
3. For every image, record its **source**, **rights basis**, and **alt text**.
4. Honour correction and removal requests promptly.

Do not commit participant data, clinical/imaging data, student assessments, secrets, or build output (`_site/`).

## Local build

See [`README.md`](README.md).
