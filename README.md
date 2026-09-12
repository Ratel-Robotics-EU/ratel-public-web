# ratelrobotics.eu

Static site for Ratel Robotics OÜ and the Badger UGV. No build step, no dependencies.

## Layout
- `index.html` — Badger, specs, status, sales contact
- `company.html` — company, team, partners, registry details
- `careers.html` — disciplines and open application
- `assets/style.css`, `assets/fonts.css`, `assets/favicon.svg`
- `assets/fonts/` — Archivo variable (SIL OFL), self-hosted, no third-party requests
- `assets/img/`
- `CNAME` — custom domain for GitHub Pages

## Deploy
GitHub Pages, from the default branch, root folder.
Point `ratelrobotics.eu` at GitHub Pages, then enable Enforce HTTPS.
`ratelrobotics.com` and `ratelrobotics.ee` should redirect to `ratelrobotics.eu`.

## Local preview
    python3 -m http.server 8000

## Not in this repo
`content/` and `media/` hold internal notes and source documents. They are gitignored
because GitHub Pages serves everything in the published branch.

## Design notes
Typeface is Archivo variable (weight 400-900, width 62-125%), self-hosted so the site
makes no third-party request. The `impeccable detect` scan reports `cramped-padding` on
`<section>` and `.row`; measured insets are 61px and 27px, so those are heuristic
misfires on bordered wrappers, not defects.
