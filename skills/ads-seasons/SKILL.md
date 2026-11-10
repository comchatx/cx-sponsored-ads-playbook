---
name: ads-seasons
description: "Sponsored ads around Amazon's sales events: the Prime Day, Prime Big Deal Days and Black Friday calendars by region, the Ads API's events and event themes, what Amazon and practitioners report on budgets, CPC and conversion before, during and after a peak, how attribution and benchmarks read across a moving event, and the deals, promotions and claim rules beside the ads. For reading or changing a seller's sponsored ads around a sales event."
---

## Calendar

Prime Day 2026 ran June 23–26 PDT in 23 countries; since 2019 its start has ranged from June 21 to October 13. (E1)
Black Friday 2026 is November 27; Amazon had not published US Black Friday Week dates on 2026-11-09. (E1)
Regional dates and times differ. (E2)

## Events in the Ads API

`POST /sp/v1/events` returns special events with suggested date ranges; budget-rule event recommendations carry a `suggestedBudgetIncreasePercent` per SP or SB campaign. (E3)
Theme-based bid recommendations offer `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT` and `BFCM_HOLIDAY`; the v1 theme target `KEYWORDS_RELATED_TO_PRIME_DAY` matches queries only through Prime Day's end. (E4)

## Spend and performance

Amazon advises daily budgets +20–30% around Black Friday and Cyber Monday, three to five days ahead, as guidance, not limits; Ad Badger recommends 2–3× on Prime event days. (E5, E6)
Amazon says conversion rates often drop during major sales events and that a temporary ACOS spike is read against TACOS. (E7)
Practitioners disagree on post-event spend and on December 26 to mid-January, their "Q5"; no Amazon page read uses the term. (E16, E20, E5)

## Reading an event

SP attributes seller conversions over 7 days, SB and SD over 14, dated to the ad interaction. (E8)
Amazon advises checking 7–14-day attribution before changing campaigns after a peak, as peak-event sales often come days after the click. (E8)
A moving event lands in different Data Kiosk year-over-year benchmark weeks. (E15)
Scanner research puts the post-promotion dip at 4–25% of a promotion's current sales effect. (E18)

## Deals and claims

Deals carry rating, deadline and fee rules; coupons and Brand Tailored Promotions their own limits; Customer Engagement emails are free. (E9, E10, E21, E22)
An advertised deal must be live whenever the ad is; sponsored ads mention Prime Day only through dynamically pulled detail-page information such as deal badges. (E13)
The SP-API Promotions API is read-only for sellers. (E14)
Vendor promotions have their own reports and funding. (E24, E25, E27)

## References

- references/calendar.md: dates by region.
- references/api-events.md: events, themes, Amazon Business.
- references/spend.md: budgets, CPC, conversion.
- references/measurement.md: attribution, benchmarks, research.
- references/deals.md: deals, fees, promotions, emails.
- references/claims.md: badges, ad policy, Stores, EU prices.
- references/vendors.md: vendor reports, guides, funding.
- The amazon-ads skill's references/door.md: asking for reports.
