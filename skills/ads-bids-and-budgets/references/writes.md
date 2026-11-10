# Writing bids and budgets

Paths, headers, origins, the token and the reply's handling are the amazon-ads skill's references/door.md.

## Bid limits

- Amazon publishes minimum and maximum SP, SB and SD bids per marketplace and currency on the API limits page. (B14)
- On 2026-11-09 the SP minimum was 0.02 in USD, CAD, GBP, EUR, AUD and SGD, 2 in JPY and 1 in INR. (B14)
- The page contains at least one apparent error (EG SP maximum 5.50). (B14)
- A refused SP 3.0 bid carries a `biddingError` with its reason and the marketplace's `lowerLimit` and `upperLimit`. (B14, B20)

## Bid writes

- In SP 3.0, bids are written with `PUT /sp/keywords`, `/sp/targets` and `/sp/adGroups`, and strategy, placement and audience adjustments with `PUT /sp/campaigns`, each under its own versioned media type, up to 1,000 per call. (B20)
- An SP 3.0 bid write answers 207 with per-index errors. (B20)
- In v1, bids are written with `update/targets`, `update/adGroups` and `update/campaigns`, under per-product ceilings: SP 1,000; SB 10 campaigns or ad groups and 1,000 targets; SD 100 campaigns or ad groups and 1,000 targets. (B20)
- In SB, bids are written with `PUT /sb/keywords` and `/sb/targets`, 100 per call, and placement and audience adjustments with `PUT /sb/v4/campaigns`, 10 per call. (B20)
- An SB keyword or target bid is mutable only when its campaign has no enabled optimization rule. (B20)
- In SD, bids are written with `PUT /sd/targets` and `/sd/adGroups`; an optimization rule on the ad group overrides manual target bids, and under display cost control "Bids can’t be manually edited". (B20)
- Amazon's v1 overview lists SD as supported and publishes an SD v1 model with update operations, with no dated GA note. (B20)

## Budget writes

- In v1, a budget's `recurrenceTimePeriod` is `DAILY`, `LIFETIME` or `MONTHLY`. (B30)
- A global SP campaign carries a separate budget per marketplace, in local currency, in `marketplaceSettings`. (B30)
- Budgets are in the marketplace's currency, and Amazon refuses a budget outside the marketplace's range, below the campaign's bids or in a mismatched currency, naming the reason in the error. (B30)
- In SB, budget amounts are written with `PUT /sb/v4/campaigns`, 1–10 per call, where `budgetType` is accepted at create only. (B32)
- In SD v3, budget amounts are written with `PUT /sd/campaigns`, at most 100 per call, where `budgetType` is `daily` only and the 207 reply does not carry the new budget. (B32)
- The SD v1 update-budget schema lacks the `recurrenceTimePeriod` the read model requires. (B32)
- Developers report an SD v1 budget update without `recurrenceTimePeriod` returning 207 with no error while the budget is unchanged (issue 475, open with no Amazon reply on 2026-11-09). (B32)
- Developers also report an SP prompt-extension pause reverting by the next day, and a required `statusMessage` missing from `query/advertiserAccounts`. (B32)
