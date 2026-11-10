---
name: ads-bids-and-budgets
description: "What a sponsored ad's click costs and how its spend runs: Amazon's auction and reserves, Sponsored Products bidding strategies, placement and audience adjustments, bid and budget rules, Sponsored Brands and display cost control, daily, lifetime and portfolio budgets and their pacing, how bids and budgets are written, and the changes Amazon and outside tools make themselves. For reading, judging or changing a seller's bids and budgets in Sponsored Products, Sponsored Brands and Sponsored Display."
---

## Auction

- A bid is the most an advertiser authorises per click or 1,000 viewable impressions; Amazon states it never charges above the maximum effective bid, adjustments and strategy included. (B1)
- Amazon describes a generalized second-price auction whose soft reserves can make a winner pay its own bid. (B1)
- The FTC and 22 states allege, in an untested complaint, that soft reserves raised advertisers' costs; Texas sues separately; Amazon disputes the characterisation. (B3)

## Bidding

- SP strategies: `LEGACY_FOR_SALES` (down only; the API default), `AUTO_FOR_SALES`, `MANUAL`, `RULE_BASED`. (B5)
- SP placement adjustments run 0–900%; dynamic bidding works on the adjusted bid; kinds of adjustment multiply. (B7, B8)
- Rule-based bidding needs at least 10 days running, 10 conversions in the last 30 and a marketplace minimum daily budget. (B11)
- Schedule bid rules only raise SP bids. (B12)
- SB and display cost control set a target average CPC, not a maximum. (B16)

## Budgets

- A daily budget is averaged over the calendar month; one day may spend up to 100% more (25% if opted out). (B22)
- Sponsored-ads budgets are not paced; an out-of-budget campaign waits for midnight. (B23)
- Budget rules only raise budgets; SP reads the raised one as `budget.effectiveBudget`. (B27)
- A portfolio cap stops its campaigns with `PORTFOLIO_OUT_OF_BUDGET`. (B28)
- `budgetUsagePercent` is spend over the day's effective budget. (B25)
- The budget recommendation's missed sales are click-attributed, not caused by the ad. (B26)

## Writes

- A refused SP 3.0 bid names its reason and the marketplace's `lowerLimit` and `upperLimit`. (B14, B20)
- Developers report an SD v1 budget update without `recurrenceTimePeriod` answering 207, the budget unchanged. (B32)
- Paths, headers, origins, the token: the amazon-ads skill's references/door.md.

## Amazon's own hands

- Amazon changes bids, budgets, targets and creative without a seller write. (B35)
- Applying a recommendation is the same write as any other change. (B36)
- Amazon's lift figures for its automation describe no randomised holdout. (B40)

## References

- references/auction.md: reserves, FTC case, position research.
- references/bidding.md: strategies, adjustments, bid rules, practitioners.
- references/budgets.md: pacing, usage, rules, portfolios, tools.
- references/writes.md: limits, bid and budget writes.
- references/automation.md: suggestions, recommendations, agents, tools, lifts.
- ../ads-review/references/metrics.md: metrics; ../ads-review/references/reports.md: reports.
