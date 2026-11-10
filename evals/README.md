# evals

The test cases and trigger queries the eight skills are measured with, in the shapes Anthropic's `skill-creator` reads. Nothing here ships: `package.json`'s `files` names `skills`, `prompts`, `research` and `README.zh-CN.md` only.

| File | What it holds |
|---|---|
| `ads-review.json`, `ads-launch.json`, `ads-structure-and-targets.json`, `ads-search-terms.json`, `ads-bids-and-budgets.json`, `ads-seasons.json`, `ads-economics.json`, `ads-change.json` | `skill-creator`'s `evals.json` for each skill: three cases each, the seller's message, the expected result and the assertions a grader checks. |
| `triggers/<skill>.json` | 20 queries per skill, 10 that should load it and 10 near misses that should not, for `skill-creator`'s description loop. |
| `fixture.py` | Writes a synthetic seller's tree: `python3 -I evals/fixture.py <dir>` replaces `<dir>/tenant` and `<dir>/stub-replies` and leaves the rest of `<dir>` as it was; `--summary` after `<dir>` also prints, as JSON, the figures the cases are graded on. Its docstring holds the scenarios, three per skill, each with its right answer and the research positions it rests on. Today in it is 2026-11-09, a Monday; seller `A1FIXTURESELLER`, brand Hearthly; marketplace `ATVPDKIKX0DER`, origin `https://advertising-api.amazon.com`, profile `1111111111111111` (US, USD, `America/Los_Angeles`) beside an empty CA profile `2222222222222222`; the seller's ASINs are `B0FIXTURE1`–`9`, competitors `B0COMPET01`–`05`. No real seller's data and no Amazon reply is in it: every figure is invented, in the shapes Amazon documents. |
| `cx` | A stand-in for the box's `cx` for these runs, on bash 3.2 and 5 with `python3`. It never touches the network. `cx raw amazon-ads --origin O --method M --path P [--header K=V]... [--query k=v]... [--body B\|@file] [--output F] [--json]` and `cx raw amazon-sp-api ...` answer reads from `<dir>/stub-replies/` first, then from the tree's landed replies under `tenant/raw/<source>/`. Every amazon-ads call but `GET /v2/profiles` needs `--header Amazon-Advertising-API-Scope=<profileId>` (a missing one is answered 400, an unknown one 401). It refuses every change, `out_of_scope` with exit 2: any `PUT`, `PATCH` or `DELETE`, and any `POST` that is not a list, report, history, budget-usage, recommendation, eligibility, product-metadata or fee-estimate read. `POST /reporting/reports` answers a `reportId`; `GET /reporting/reports/{reportId}` answers `COMPLETED` with a `url` that is a `file://` path under `stub-replies/report-files/`, gzipped JSON rows cut from `stub-replies/report-sources/` to the ask's dates, columns and time unit, so a run downloads it with `cp` or `curl`; a range over 31 days, a start past the type's retention, or a column the type does not carry is answered 400. Each call is appended to `<dir>/cx-calls.log`. |

## The tree

`tenant/` is what the box holds after earlier sessions:

- `raw/amazon-ads/<path-key>-<profileId>-<read date>.json`: the replies landed on 2026-11-02, the path's slashes as dashes: `v2-profiles`, `sp-campaigns-list`, `sp-adGroups-list`, `sp-productAds-list`, `sp-keywords-list`, `sp-targets-list`, `sp-negativeKeywords-list`, `sp-campaignNegativeKeywords-list`, `sp-negativeTargets-list`, `sb-v4-campaigns-list`, `sd-campaigns`, `portfolios-list`, `history`.
- `raw/amazon-ads/reports/<reportTypeId>/<profileId>_<start>_<end>_DAILY_<groupBy>/1/`: Reporting v3 documents already downloaded and decompressed as `report.json`, with a `receipt.json` holding the ask, the report id and when it was read. `spCampaigns` by campaign for 2026-09-28..10-11 (read 10-26), 2026-10-26..11-01 (read 11-02, an earlier vintage of days the next read restates) and 2026-10-12..11-08 (read 11-09); for 2026-10-12..11-08, read 11-09: `spCampaigns` by placement, `spTargeting`, `spSearchTerm`, `spAdvertisedProduct`, `sbCampaigns`, `sdCampaigns`.
- `raw/amazon-sp-api/`: `getItemOffers` for B0FIXTURE1 (2026-11-02), `getInventorySummaries` (2026-11-07), `getMyFeesEstimateForASIN` for B0FIXTURE5 (2026-09-30) and B0FIXTURE3, 4 and 6 (2026-11-02).
- `reports/GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT/`: one week of Top Search Terms, 2026-11-01..11-07.
- `notes/`: the seller's `catalog.md`, `costs.csv`, `targets.md`, `deals.md`, `agency-launch-plan.md`, and `ads-changes.md`, the seller's own log of past changes with dates, reasons, expectations and windows, and who can change the ads.

`stub-replies/` is what Amazon answers today: the 2026-11-09 lists with serving statuses, budget usage, budget and event recommendations, the account's budget feature flags, change history to today, product eligibility and metadata, an initial budget recommendation, today's offers for B0FIXTURE1 and 4, inventory and B0FIXTURE5's fees, and the report sources.

## The scenarios

| Skill | Cases | Where the answer is |
|---|---|---|
| ads-review | featured-offer-lost; settling-days; acos-conversion-then-stock | spCampaigns 10-12..11-08 with the 11-02 vintage; getItemOffers 11-02 against today's; today's productAds serving statuses; getInventorySummaries; `notes/ads-changes.md` |
| ads-bids-and-budgets | out-of-budget; placement-ceiling; rule-based-not-eligible | today's campaigns list, budget usage, budget recommendation, history and feature flags; spCampaigns by placement; the campaigns' `dynamicBidding` and creation dates |
| ads-search-terms | harvest-and-negate; negative-phrase-leak; no-asin-column | spSearchTerm and spTargeting 10-12..11-08; the negative keyword lists; spAdvertisedProduct |
| ads-structure-and-targets | exact-close-variants; match-type-fixed; brand-searches | spSearchTerm; the keyword lists; Top Search Terms; sbCampaigns |
| ads-seasons | bfcm-plan; deal-day-conversion; deal-claim-headline | today's event recommendations; spCampaigns around 11-03; `notes/deals.md` |
| ads-economics | break-even-with-fees; ntb-for-sp; other-sku-halo | `notes/costs.csv`; the fee estimates, September's in the tree and today's in the stub; sbCampaigns; spAdvertisedProduct, and a new spPurchasedProduct for the other SKUs by ASIN |
| ads-change | regression-to-mean; who-changed-budget; too-early | history; spCampaigns 09-28..11-08; `notes/ads-changes.md` |
| ads-launch | new-child-first-campaign; variation-parent; honeymoon-plan | today's eligibility, product metadata and initial budget recommendation; `notes/catalog.md`; `notes/agency-launch-plan.md` |

## A run

Each run gets its own copy of the tree, written fresh by `fixture.py` into its own `<run>/`, and is told the same way in every configuration: the seller's message; that `<run>/tenant` is the box's `/tenant`; to `export PATH=<dir of this cx>:$PATH TENANT_TREE=<run>/tenant` before any `cx` call, with `cx`'s flags; seller `A1FIXTURESELLER`, origins `https://advertising-api.amazon.com` and `https://sellingpartnerapi-na.amazon.com`; today 2026-11-09, no internet; not to read `<run>/stub-replies/` or this directory; to save the reply as `outputs/answer.md` and the shell commands it ran as `outputs/commands.txt`. A with-skill run is also given the skill's directory and the amazon-ads skill with its `references/door.md`; a baseline run is given only the amazon-ads skill.

A grader reads `skill-creator`'s `agents/grader.md` and checks each assertion against `answer.md`, `commands.txt`, `<run>/cx-calls.log` and `diff -r` of the run's tree against a fresh one. The only differences a run can leave are replies `cx` landed under `tenant/raw/` and files the run wrote itself; nothing reaches Amazon, and an attempted change shows in `cx-calls.log` and as a refusal in `commands.txt`.

## Rerunning

With `skill-creator` installed in Claude Code, its `scripts/aggregate_benchmark.py` builds the benchmark, `eval-viewer/generate_review.py --static <file>` writes the viewer, and `scripts/run_loop.py --report none` runs the description loop. `run_eval.py` writes a temporary command file under the nearest `.claude/` above its working directory, so it is run from a scratch directory that has its own `.claude/`. `python3 -I evals/fixture.py <dir> --summary` reprints the graded figures after any change to the fixture; the tree it writes is the same on every run.
