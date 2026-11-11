# The first campaign

## Amazon's starting advice

- Amazon recommends that a new advertiser start with automatic Sponsored Products and use its search term report to find manual targets. (L10)
- Amazon's guides differ on when to add manual targeting: about two weeks in one, at the start in another. (L10)
- Search term reports: ../ads-review/references/reports.md; their reading: ../ads-search-terms/SKILL.md.

## How a campaign is built

- Amazon's guides build a campaign by separate creates in order: campaign, ad group, product ad (by SKU for sellers, by ASIN for vendors), then targets. (L20)
- An auto campaign is complete and serves once it has an active campaign, ad group and product ad, before any negative exists. (L20)
- Both create APIs, SP v1 and SP 3.0, accept `PAUSED` as the first state. (L20)

## Recommendations before a campaign exists

- For a campaign that does not exist yet, the API returns keyword suggestions for ASINs, bids for a new ad group and an initial budget recommendation. (L11)
- The initial budget recommendation is `-1` when there is not enough information, and comes with up to five special-event budgets. (L11)
- Amazon's guide Best practices for your Sponsored Products ads (https://advertising.amazon.com/library/guides/sponsored-products-best-practices) suggests a starting daily budget above the API's minimum daily budget, which the Ads API *Limits, constraints, and quotas* page (https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits) gives per marketplace and currency. (L11)

## Amazon's time marks

- Amazon's guides set time marks for a new campaign: in the first week, monitor metrics at least twice a week; test match types for at least one to two weeks before pausing keywords. (L12)
- In the same guides a keyword is evaluated after at least 20 clicks before it is added as a negative, and negatives run for two weeks or more before a change of strategy. (L12)

## Practitioners' launches

- Canopy Management structures a launch as exploration, intent capture and brand presence and opens bids above Amazon's suggestion. (L19)
- Ad Badger opens manual bids conservatively. (L19)
- ecomcrew starts narrow with exact match and high bids and widens later. (L19)
- Canopy Management, EightX and My Amazon Guy each publish launch-stage ACoS or TACoS bands above their mature bands; the bands do not agree with one another, and each firm calls its bands starting points or guidelines. (L19)
- ACoS and TACoS as figures: ../ads-review/references/metrics.md.
