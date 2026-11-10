---
name: ads-seasons
description: "Sponsored ads around Amazon's sales events: the Prime Day, Prime Big Deal Days and Black Friday calendars by region, the Ads API's events and event themes, what Amazon and practitioners report on budgets, CPC and conversion before, during and after a peak, how attribution and benchmarks read across a moving event, and the deals, promotions and claim rules beside the ads. For reading or changing a seller's sponsored ads around a sales event."
---

## Calendar

An event's dates and length differ by marketplace and year; SP's events operation returns suggested date ranges for the advertiser's marketplace. (E1, E2, E3)
Since 2019 Prime Day's start has moved between June and October; in 2025 it went from 48 to 96 hours. (E1)

## Events in the Ads API

Budget-rule event recommendations (`EVENTS_FOR_EXISTING_CAMPAIGN`) give an SP or SB campaign Amazon's recommended events, each with a `suggestedBudgetIncreasePercent`; a rule tied to an unannounced event is created with empty dates that Amazon fills in on announcement. (E3)
Theme-based bid recommendations offer `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT` and `BFCM_HOLIDAY`. (E4)

## Spend and performance

Amazon advises daily budgets +20–30% around Black Friday and Cyber Monday, three to five days ahead, as guidance, not limits; Ad Badger recommends 2–3× on Prime event days. (E5, E6)
How a budget rule raises a budget: ../ads-bids-and-budgets/references/budgets.md.
Amazon says conversion rates often drop during major sales events and that a temporary ACOS spike is read against TACOS. (E7)
Practitioners disagree on post-event spend and on December 26 to mid-January, their "Q5", unused by any Amazon page read 2026-11-09. (E16, E20, E5)

## Reading an event

SP attributes seller conversions over 7 days, SB and SD over 14, dated to the ad interaction; Amazon advises checking 7–14-day attribution before changing campaigns after a peak. (E8)
A moving event lands in different Data Kiosk year-over-year benchmark weeks. (E15)
Store-level scanner research puts the post-promotion dip at 4–25% of the promotion's current sales effect, usually missed by simple models and visual inspection. (E18)

## Deals and claims

An advertised deal must be live whenever the ad is; sponsored ads mention Prime Day only through dynamically pulled detail-page information such as deal badges. (E13)
Amazon's ad policy bounds an event's name in an ad, such as "Black Friday Week", by the event's length, as its Event days page for that marketplace states (https://advertising.amazon.com/help/GQ3SJ5QCWCQCKCYQ). (E1, E13)

## References

- references/calendar.md: where event dates are read; history.
- references/api-events.md: events, budget-rule events, themes.
- references/spend.md: budgets, CPC, conversion, post-event.
- references/measurement.md: attribution, benchmarks, promotion research.
- references/deals.md: deals, fees, promotions, emails.
- references/claims.md: badges, ad policy, Stores, EU prices.
- references/vendors.md: vendor promotions.
- The amazon-ads skill's references/door.md: report requests.
- ../ads-change/references/history.md: change history.
