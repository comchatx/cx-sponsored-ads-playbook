---
name: ads-bids-and-budgets
description: "What a sponsored ad's click costs and how its spend runs: Amazon's auction and reserves, Sponsored Products bidding strategies, placement and audience adjustments, bid and budget rules, Sponsored Brands and display cost control, daily, lifetime and portfolio budgets and their pacing, how bids and budgets are written, and the changes Amazon and outside tools make themselves. For reading, judging or changing a seller's bids and budgets in Sponsored Products, Sponsored Brands and Sponsored Display."
---

## Auction

- A bid is the most an advertiser authorises per click or 1,000 viewable impressions; Amazon states it never charges above the maximum effective bid, adjustments and strategy included, and its soft reserves can make a winner pay its own bid. (B1)

## Bidding

- SP strategies: `LEGACY_FOR_SALES` (down only), `AUTO_FOR_SALES` (up and down), `MANUAL`, `RULE_BASED`; an API-created campaign with no strategy gets `LEGACY_FOR_SALES`, so down only may be nobody's choice. (B5)
- Under up and down, Amazon's help and API models allow up to 100% at every placement, while its author-facing guide still gives 50% outside top of search; no page dates a change. (B6)
- SP placement adjustments run 0–900%; dynamic bidding works on the adjusted bid; kinds of adjustment multiply. (B7, B8)
- Rule-based bidding needs at least 10 days running, 10 conversions in the last 30 and a marketplace minimum daily budget (figure not held). (B11)
- Its ROAS guardrail rests on the previous 21 days and is not guaranteed; Amazon warns an aggressive one can reduce conversions. (B11)
- SB and display cost control set a target average CPC, not a maximum. (B16)

## Budgets

- A daily budget is averaged over the calendar month; one day may spend up to 100% more (25% if opted out). (B22)
- Sponsored-ads budgets are not paced; an out-of-budget campaign waits for midnight. (B23)
- `POST /{sp,sb,sd}/campaigns/budget/usage` returns `budgetUsagePercent`, spend over the day's effective budget, with `usageUpdatedTimestamp`; Trellis advises recording when each campaign ran out. (B25, B33)
- The SP budget recommendation returns a suggested daily budget, the last 7 days' share in budget and estimated missed impressions, clicks and sales, "not a guarantee"; missed sales are click-attributed, not ad-caused. (B26)
- Budget rules only raise budgets; SP reads the raised one as `budget.effectiveBudget`. (B27)
- A portfolio cap stops its campaigns with `PORTFOLIO_OUT_OF_BUDGET`. (B28)

## References

- references/auction.md: reserves, FTC case, position research.
- references/bidding.md: strategies, placement caps, rule-based and schedule rules, adjustments, practitioners.
- references/budgets.md: averaging, pacing, usage, recommendations, budget rules, portfolios, tools.
- references/writes.md: limits, refusals, bid and budget writes.
- references/automation.md: Amazon's own changes, recommendations, agents, bid tools, lifts.
- API paths and headers: the amazon-ads skill's references/door.md.
- Metrics, reports: ../ads-review/references/metrics.md, ../ads-review/references/reports.md.
