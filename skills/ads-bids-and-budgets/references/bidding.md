# Bidding strategies and adjustments

## Sponsored Products strategies

- Sponsored Products has four bidding strategies, in the 3.0 API `LEGACY_FOR_SALES` (dynamic down only), `AUTO_FOR_SALES` (up and down), `MANUAL` (fixed) and `RULE_BASED`. (B5)
- A campaign created through the API with no strategy gets `LEGACY_FOR_SALES`. (B5)
- Down only may lower a bid by up to 100% for clicks Amazon judges less likely to convert, and never raises it. (B5)
- Fixed uses the exact bid plus placement adjustments with no dynamic bidding, which Amazon says may give more impressions but fewer conversions for the spend. (B5)
- Under up and down, Amazon's current help, library guide and SP 3.0 and v1 models say Amazon may raise or lower a bid by up to 100% for all placements, while the author-facing guide still gives 100% for top of search and 50% elsewhere; no page dates a change. (B6)

## Placement adjustments

- SP placement adjustments raise a bid 0–900% for top of search (up to the first five positions of the top row on desktop, four on mobile), rest of search, product pages and Amazon Business. (B7)
- An adjustment applies only when the ad competes for that placement. (B7)
- Dynamic bidding works on the placement-adjusted bid, so a $1 bid with +50% top of search can reach $3 under up and down. (B7)

## Audiences

- In Sponsored Products, adjustments of different kinds multiply (placement × audience × video). (B8)
- An SP 3.0 campaign may boost up to 10 audiences (Amazon or AMC audiences; one outside the US), each 0–900%. (B8)
- When a shopper is in several boosted audiences only the highest boost applies, ties going to one audience at random. (B8)
- In v1 the field `bidAdjustments.audienceBidAdjustments[]` takes at most one per campaign. (B8)
- Audience ids come from `POST /targetableEntities/list`, and "Only the audiences retrieved using these filters are usable". (B8)
- A Sponsored Brands campaign takes one audience group, Amazon-built or AMC, not both. (B8)

## Off-Amazon placements and site restrictions

- SP off-Amazon placements are on by default and use the campaign's own bid and budget. (B9)
- They take no top-of-search, rest-of-search or product-page adjustments, while dynamic and rule-based bidding still apply. (B9)
- Amazon bids them on third-party sites by predicted click-through and conversion and submits them to the publisher, who decides which ads show. (B9)
- `offAmazonBudgetControlStrategy` governs them: `MAXIMIZE_REACH`, the console default, or `MINIMIZE_SPEND`. (B9)
- Their cost shows in the placement report and, since 2026-06-08, in a US bulksheet column, not in Campaign Manager. (B9)
- PPC Land's Luis Rijo reports that from 2026-08-10 SP ads may also serve through Amazon Influencer Program creators, enrolled by default at existing bids and budgets. (B9)
- The placement report itself is in ../ads-review/references/reports.md.
- A site restriction (Amazon Business only, or Amazon Haul in the US) is set at creation, cannot be changed and has its own program-eligibility reason. (B10)
- A site-restricted campaign has no audience (shopper-cohort) bid adjustments and no Amazon Business placement adjustment. (B10)

## Rule-based bidding

- Rule-based bidding adjusts base bids per impression toward a ROAS guardrail that Amazon bases on the previous 21 days and does not guarantee. (B11)
- It can raise a bid up to five times the adjusted bid, and sets a goal itself when none is given. (B11)
- Amazon warns that it can reduce conversions under an aggressive guardrail. (B11)
- It needs a campaign running at least 10 days with at least 10 conversions in the last 30, at or above a marketplace minimum daily budget, whose figure this skill does not hold, so a newly launched campaign is not eligible. (B11)
- A comparison of rule-based campaigns with ineligible ones mixes the rule's effect with that gate. (B11)
- Amazon switches it off when 20-day ROAS falls below 30% of the prior 20-to-40-day ROAS, restoring the earlier strategy and bids. (B11)

## Schedule bid rules

- Schedule bid rules are SP only and only raise bids, by an integer 1–100% of the base bid, for an hour window, weekday, date range or event ("Recurring Events" in JP only, "Individual Events" worldwide). (B12)
- Several rules add together and the total adds to the placement adjustment: Amazon's example is $1.00 with top of search +10% and a Monday rule +20% giving $1.30. (B12)
- A rule change takes effect within 24 hours, and a campaign carries at most 20 rules. (B12)
- They cannot be applied to a campaign with rule-based bidding active, and go on hold if the campaign switches to rule-based bidding. (B12)

## Sponsored Brands

- In Sponsored Brands only top of search and rest of search can be adjusted, positive adjustments going up to 900% for both (announced 2025-06-19; rest of search was limited to 99% before). (B15)
- Automated bidding lets Amazon optimize placements below top of search, and in the 4.0 API `bidOptimization: true` makes Amazon ignore `bidAdjustmentsByPlacement`. (B15)
- New negative SB placement adjustments are not accepted from 2026-06-15, while existing ones keep running with their current settings. (B15)
- Under the goal "drive page visits" Amazon may raise a bid by up to 300% for an auction and lower it where conversion looks less likely. (B15)

## Cost control and display

- Sponsored Brands and display cost control set a target average CPC, not a maximum: the average may be higher than entered. (B16)
- With placement or audience adjustments, the highest possible CPC exceeds the target. (B16)
- In Sponsored Brands, cost control is on automatically, and only available, for the goal "drive page visits". (B16)
- Under display cost control, bids are set automatically, cannot be edited by hand and come with no suggested bids. (B16)
- Display may raise a bid up to 300% under any optimization strategy. (B17)
- The display optimization strategy (reach on vCPM; page visits, conversions or leads on CPC) is fixed at creation. (B17)
- vCPM charges per 1,000 viewable impressions under the MRC definition. (B17)

## Placement isolation

- Placement isolation is the same exact keyword in a campaign with a low base bid and a high top-of-search adjustment, beside a campaign for the other placements. (B18)
- The Helium 10 Team (2019), Feedvisor, Perpetua and Ad Badger (2020, 2023) argue for it. (B18)
- Ad Badger (2023) also says a very low base bid may not enter the auction ("Amazon doesn't quite play along with that idea"). (B18)
- m19 (2026) advises against one-keyword top-of-search campaigns, naming minimum budgets, cost and management load. (B18)
- Pacvue's moderate-base-bid argument is known only from search summaries. (B18)

## Strategies and hours in practitioner data

- BidX (Lena Einschütz), in observational data on about 130,000 campaigns in February 2024, found down-only campaigns with the lowest ACOS and better conversion than up and down despite higher CPCs. (B19)
- BidX found the worst ACOS where down-only campaigns carried a product-page adjustment above 0%. (B19)
- Perpetua (Stephen Bench-Capon), from six weeks of US SP data in spring 2022, found CPC falling from $1.13 early in the day to $0.84 by its end, which it attributes to advertisers exhausting budgets. (B19)
- Perpetua found conversion around 20% at a 6–10 am Pacific peak against 6–8% at night, and ACOS of 20–23% by day against 41% in the 11 pm hour. (B19)
- Clear Ads Agency (George Meressa, 2026) holds that most sellers should not daypart, and treats a 2× best-to-worst-hour conversion gap, 30 days of hourly data and about $20,000 a month in spend as minimums. (B19)
- Practitioners disagree on the best hours: Perpetua 6–10 am Pacific, Clear Ads 6–10 pm, Kepler's apparel client 4 pm to midnight. (B19)
