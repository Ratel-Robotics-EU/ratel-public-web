# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Delegated. Plain static HTML and CSS, no framework and no build step, because the user
fixed GitHub Pages in this repo as the deploy target. Archivo variable is self-hosted so
the site makes no third-party request. Contact is email only; there is no backend and no
form handler.

## Users

**Primary — defence procurement officers, systems integrators and consortium partners.**
They arrive from a conference handout, a LinkedIn post, ERR coverage or a search, and they
decide in well under a minute whether this company is real enough to email. They want to
know what it carries, how far it goes, what stage it is at, and who else has validated it.

**Secondary — investors** assessing an early-stage European defence hardware company.
**Tertiary — engineers in Estonia** deciding whether to write an open application.

When the three conflict, the defence buyer wins.

## Product Purpose

Ratel Robotics builds **Badger**, an electric unmanned ground vehicle that carries 250 kg
so an infantry squad does not have to: resupply, sensor carriage, drone charging and light
casualty evacuation on one modular platform.

The site exists to do three things, in order:
1. Produce qualified sales and partnership enquiries at `sales@ratelrobotics.eu`.
2. Bring engineers to `jobs@ratelrobotics.eu` as an open application.
3. Make the company read as credible to an investor who lands on it unprompted.

## Positioning

Electric-first, squad-sized, and dual-use by design — smaller and cheaper than Milrem
THeMIS, and built from the start to serve both a military and a civil buyer rather than
being converted to one later. Designed, fabricated and assembled in Estonia: EU, NATO and
eurozone.

**Durable constraint — name collision.** An unrelated Ratel Robotics in Kyiv (Taras
Ostapchuk, the Ratel S/H/M/X UGVs) was acquired by Swarmer on 2026-09-10 for up to $224M
and owns the search results for the company name. The answer is to brand on **Badger**,
state Tallinn and Estonia early on every page, and carry the registry code in structured
data and the footer. Do not attempt to win "Ratel Robotics" in search. Do not rename the
product — the MoD grant, the ERR segment and the January conference handout all say Badger.

## Repository Layout

Published site at the repo root: `index.html`, `company.html`, `careers.html`, `assets/`.
`local/` holds working files — source documents, original photography, scratch notes — and
is gitignored. `.github/workflows/pages.yml` publishes only the site files, so `PRODUCT.md`
and `README.md` are versioned but never served.

## Operating Context

- Primary domain `ratelrobotics.eu`. `.com` and `.ee` are owned and should redirect to it.
- Mail runs on Google Workspace on `.eu` only. `.com` and `.ee` have **no MX record**, so
  `rakylm@ratelrobotics.com` — printed on the January 2026 conference handout — bounces.
- `sales@` and `jobs@ratelrobotics.eu` are published on the site but not yet created.
- Buyers reach the company through the Defence Estonia cluster, Tehnopol, conferences and
  Estonian defence press, not through paid acquisition.

## Capabilities and Constraints

Published specification, locked with the founder on 2026-09-12. Geometry comes from the
dimensioned drawing; performance figures are founder-confirmed.

| | |
|---|---|
| Payload | 250 kg |
| Curb weight | approx. 450 kg (founder estimate, 2026-09-14) |
| Range | up to 150 km, terrain and profile dependent |
| Maximum speed | 30 km/h |
| Power | 48 V lithium-ion with BMS, 15 kWh |
| Dimensions | 1800 × 1250 × 1050 mm, wheelbase 1200 mm, clearance 350 mm |
| Suspension | independent, upgrade-ready |
| Signature | low acoustic, low thermal |
| Control | teleoperated; waypoint and autonomy in development |
| Communications | Estonian-built radio, Starlink, repeater drone |
| CASEVAC | up to two casualties on the bed |
| Towing and recovery | trailer hitch and winch; no rated capacity published |

Superseded, never republish: 300 kg payload, 200 km range, 350 kg weight, 1500×1200×900
dimensions, 250 mm clearance, 35 or 38 km/h.

- **Teleoperated today.** No autonomy ships. Earlier source material contradicted itself on
  this; the resolved truth is "teleoperated, autonomy in development".
- TRL 6. Field testing with Kaitseliit. Roadmap is undated after 2026: operational
  validation with defence users, then design-for-manufacture and low-rate production. Do
  not publish quarter or year targets for TRL 7 or production.
- Pre-revenue. Zero revenue and zero employees on payroll in every quarter since
  incorporation — this is public in the Estonian register and cannot be hidden.
- Four equal shareholders, one board member (Rain-Alari Külm).
- English only. No Estonian version.

**Never publish:** component suppliers, subcontractors, bill-of-materials detail, or the
proportion of non-Chinese content. Everything else is ordinary commercial discretion.

## Brand Commitments

- Product name **Badger**; legal entity **Ratel Robotics OÜ**. Badger leads, the company is
  secondary. *Mäger* is the Estonian name and earns a short heritage note on the company
  page — it is not a second product name.
- Voice: plain, short sentences, active verbs. No defence-marketing inflation. State the
  early-stage truth rather than dressing it up.
- Olive accent `#b6cf5e` on a dark ground; Archivo variable, self-hosted.
- **The badger mark in the header and favicon is a placeholder**, not a binding asset.
  Future work may replace it freely. The LinkedIn logo is still an unedited stock template
  reading "REMARK HERE".

## Evidence on Hand

**Real, and usable:**
- Estonian Ministry of Defence development grant, €22,800, one of fourteen projects from
  thirty-one applications, paid 07.11.2025.
- EAS / ERDF project 2021-2027.1.01.25-1260, running to 31.07.2026; disbursed amount not public.
- ERR Terevisioon segment "Mäger Ukrainasse", 08.10.2025.
- Tehnopol Defence Business Lab; Defence Estonia cluster membership.
- Batcomms communications module integration since 10.11.2025.
- One genuine photograph: `assets/img/badger-photo.webp`, conference stand, Tallinn, January 2026.
- Genuine dimensioned engineering drawing: `assets/img/badger-drawing-dark.webp`.

**AI renders — must never be presented as photographs.** `badger-terrain`, `badger-payload`,
`badger-3q`, `badger-scale`, `badger-detail` all carry a visible "Render" badge and a
`class="render"` marker until real photography replaces them. The founder can shoot
replacements at the workshop; industrial and nature backgrounds are both available.

**Absent. Do not fabricate:** no customers, no contracts, no procurement wins, no units
delivered, no revenue. No CE marking, no MIL-STD compliance, no IP rating, no NATO stock
number. No employee headcount above zero. No radar-cross-section measurement.

## Product Principles

1. **The buyer decides in under a minute.** Lead with what it carries and what stage it is
   at, not with company narrative.
2. **A published figure is read as a commitment.** Publish measured values, or label the
   target as a target. Never publish an aspiration as a specification.
3. **A render never passes as a photograph.** The badge stays until real photography lands.
4. **Disambiguate on every page.** Tallinn, Estonia, and the registry code.
5. **Say the early-stage truth plainly.** The register is public; pre-revenue stated with
   confidence beats pre-revenue discovered by a reader.

## Accessibility & Inclusion

WCAG 2.1 AA. The company sells into EU public bodies, where EN 301 549 cites this baseline.
