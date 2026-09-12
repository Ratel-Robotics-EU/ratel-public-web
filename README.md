# ratelrobotics.eu

Static site for Ratel Robotics OÜ and the Badger UGV. No build step, no dependencies.

## Layout

- `index.html` — Badger, specifications, programme status, sales contact
- `company.html` — company, team, partners, registry details
- `careers.html` — disciplines and open application
- `assets/style.css`, `assets/fonts.css`, `assets/favicon.svg`
- `assets/fonts/` — Archivo variable (SIL OFL), self-hosted, no third-party requests
- `assets/img/` — WebP, each sized to the width it actually displays at
- `PRODUCT.md` — product decisions and durable constraints. Read before changing copy or specs.
- `local/` — working files: source documents, original photography, notes. Gitignored.

## Deploy

`.github/workflows/pages.yml` publishes on every push to `main`. It copies only the three
pages and `assets/`, so `PRODUCT.md`, `README.md` and `local/` are versioned but never
served.

One-time setup: **Settings → Pages → Source: GitHub Actions**. The site then lands on
`https://<owner>.github.io/<repo>/` — share that with the team.

### Adding the custom domain later

There is deliberately **no `CNAME` file**. Adding one makes Pages redirect the `github.io`
URL to the custom domain, which would break team sharing before DNS is ready.

When you want `ratelrobotics.eu` live:

1. DNS at Zone.ee — apex `A` records to `185.199.108.153`, `185.199.109.153`,
   `185.199.110.153`, `185.199.111.153`.
2. Settings → Pages → Custom domain → `ratelrobotics.eu`, then wait for the check to pass.
3. Tick **Enforce HTTPS**.
4. Add `echo ratelrobotics.eu > _site/CNAME` to the workflow's staging step.
5. Redirect `ratelrobotics.com` and `ratelrobotics.ee` to `ratelrobotics.eu`.

## Making changes

Every push or merge to `main` redeploys automatically. There is no manual publish step.

    git switch -c tweak-the-specs
    # edit, then check it locally
    python3 -m http.server 8000
    git commit -am "Update payload figure"
    git push -u origin tweak-the-specs
    gh pr create --fill

Opening the PR runs `tools/check-links.py`, which fails if any page points at a file or an
anchor that does not exist. Merging deploys; a run takes about 20 seconds. Watch it with
`gh run watch --repo Ratel-Robotics-EU/ratel-public-web`.

Small fixes can go straight to `main` — push and it ships. The same check runs before the
deploy step, so a broken reference stops the release rather than shipping.

Run the check yourself before pushing:

    python3 tools/check-links.py

Read `PRODUCT.md` before changing copy, specifications or claims. It records which figures
are confirmed, which were superseded, and what must not be published.

## Local preview

    python3 -m http.server 8000

## Before launch

- `sales@ratelrobotics.eu` and `jobs@ratelrobotics.eu` are published on the site but do not
  exist yet. Mail runs on `.eu` only; `.com` and `.ee` have no MX record.
- Five images are AI renders, each carrying a visible badge and a `class="render"` marker.
  `index.html` has a TODO naming the files. Replace with real photography, then delete the
  class, the `<span class="render-badge">` and the `.render` rules in `assets/style.css`.

## Design notes

Typeface is Archivo variable (weight 400–900, width 62–125%). The `impeccable detect` scan
reports `cramped-padding` on `<section>` and `.row`; measured insets are 61px and 27px, so
those are heuristic misfires on bordered wrappers, not defects.
