# Developing cx-sponsored-ads-playbook

The README is written for a seller, in English (`README.md`) and Chinese (`README.zh-CN.md`); the Plugins page draws it. These are the notes for whoever works on the package.

A [pi](https://pi.dev) package for the work on a seller's Sponsored Products, Sponsored Brands and Sponsored Display ads: how they serve and perform and why, launching a product into ads, structure and targets, search terms, bids and budgets, Amazon's events, the economics of an ad sale, and what a change leaves behind and how its effect is read. It is written for the assistant in a [ComChatX](https://comchatx.com) seller's box, and reads the seller's ads through the box's `cx` command and the [`@comchatx/cx-amazon-ads`](https://github.com/comchatx/cx-amazon-ads) package.

It is text only: no script, no extension, no dependency. Its changes are in [CHANGELOG.md](CHANGELOG.md). Every line of the skills ends with the position it rests on, as `(A8)` or `(B1, B4)`, and the positions are in [`research/README.md`](research/README.md); a line without one only points to another file.

## What it holds

| | What the model reads | Positions |
|---|---|---|
| `skills/ads-review` | How ads serve and why not: the Featured Offer and stock behind an ad, serving statuses and money stops, decomposing a move, and the shared homes for metrics (`references/metrics.md`) and reports (`references/reports.md`) | A, M, R |
| `skills/ads-launch` | Getting a product, seller or brand advertising: gates, programs, the first campaigns, and the shared home for ad products and policy (`references/products-and-policy.md`) | L, P |
| `skills/ads-structure-and-targets` | Campaign structure, what each match type and target matches, brand defence and conquesting | T |
| `skills/ads-search-terms` | The search-term report, harvesting, negatives and how little data a judgement rests on | S |
| `skills/ads-bids-and-budgets` | The auction, bidding strategies and placements, rules, budgets and pacing, Amazon's automation | B |
| `skills/ads-seasons` | Amazon's events, deals and coupons, and what they do to clicks, costs and sales | E |
| `skills/ads-economics` | Fees and margin, break-even ACOS, total and organic sales, new-to-brand, a vendor's figures | G |
| `skills/ads-change` | Amazon's change history and its gaps, write replies, Amazon's tests and their absence, and what research finds on reading an effect | C |
| `prompts/*.md` | `/ads-review`, `/ads-launch`, `/ads-harvest`, `/ads-season`, `/ads-margin`, `/ads-brand`, `/ads-change-review`: each hands the seller's words to cx | |

Each template's `description:` is one English sentence; its Chinese is `comchatx.prompts.<name>.zh` in `package.json`, beside each skill's words in `comchatx.skills`, as the Plugins page reads them.

How a call is made and how a report is asked for and landed is the `amazon-ads` skill's (`references/door.md`), never this package's. Where a skill reads the seller's store or Keepa, `cx-amazon-sp-api` and `cx-keepa` serve it; neither is required.

Ten positions of the research left with the split of 2026-11-10 and no skill cites them: S16, E17, G13, G29, C11, M18 and R25 (to `cx-amc-playbook`), G24 (to `cx-brand-measurement` and `cx-dva-playbook`), P5 and P18 (to `cx-brand-creative`); G10 enters without its AMC clause.

## What it needs

pi, and in the box the `cx` command with the Amazon Ads source; Amazon SP-API and Keepa where a skill names their reads. It reaches no network itself.

## Install

```bash
pi install npm:@comchatx/cx-sponsored-ads-playbook        # for you, in ~/.pi/agent/settings.json
pi install -l npm:@comchatx/cx-sponsored-ads-playbook     # for one project, in .pi/settings.json
pi remove npm:@comchatx/cx-sponsored-ads-playbook
```

On ComChatX, a seller installs it from the Plugins page.

## Develop and release

```bash
npm ci
npm run typecheck
npm test               # pi at the pin loads the package and its tarball and expands every template;
                       # every line of the skills cites a position that exists, none of the ten moved ones,
                       # and each of the 323 that stay is cited; each SKILL.md body is at most 371 words
```

The skills were measured with Anthropic's `skill-creator`; the cases, the fixture and the stand-in `cx` are in [`evals/`](evals/README.md), and nothing there ships.

A release is a version in `package.json`, its entry in `CHANGELOG.md`, and a tag `v<version>` on `main`: `release.yml` publishes on that tag by npm trusted publishing, after the typecheck and the tests, and checks that the tag names the version.

## Licence

MIT. See [LICENSE](LICENSE).
