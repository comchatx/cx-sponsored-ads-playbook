---
name: ads-review
description: "How a seller's Sponsored Products, Sponsored Brands and Sponsored Display ads serve and perform, and why: the Featured Offer and stock behind an ad, serving statuses and money stops, what each metric counts and when it settles, which report or stream carries each figure, and a vendor's supply. For reviewing, watching or diagnosing a seller's sponsored ads."
---

## Serving

A Sponsored Products or display ad serves only while its product holds the Featured Offer and is in stock when the shopper views it; without the Featured Offer it gets zero impressions even when the campaign runs (A8).
When another seller holds the Featured Offer on a brand's own ASIN, its Sponsored Brands ads keep serving and send shoppers to a page whose default offer is the other seller's (A9).
Amazon announced on 2026-07-06 a removal of seller eligibility requirements for the Featured Offer completing by the end of 2026, not changing how it is selected; the ads guides read on 2026-11-09 still require eligibility (A10).
SP v3 serving statuses (`AD_NOT_IN_BUYBOX`, `AD_OUT_OF_STOCK`, …) and v1 `deliveryReasons` distinguish campaign, portfolio and account out of budget, payment failure and prepay balance (A15, A16, A17).

## Diagnosis

On a cost-per-click row spend equals impressions × CTR × CPC (A7).
Practitioners order a conversion drop's causes differently (A7): references/decomposition.md.

## Metrics

Sponsored ads report a conversion on the date of the ad interaction, which may differ from the conversion date (M1).
Sponsored Products credits 7 days of clicks for sellers and 14 for vendors and authors (M3).
Conversions are restated up to 42 days for a 14-day window, and no report marks a day final (M14).

## Reports

Reporting v3, Sponsored Ads v2 reporting and Marketing Stream v1 stop delivering data on 2027-06-30; Reporting v1 and Stream v2 have been generally available since 2026-09-30 (R1).
Reporting v1 keeps hourly rows for a shorter span than daily rows (R12).
Marketing Stream v2 delivers hourly records, keyed by placement, target and search term, to an S3 bucket and SQS queue in the subscriber's own AWS account (R15, R20).
ComChatX runs no such destination, so hourly data beyond Reporting v1's span is out of cx's reach, which cx can tell a seller who asks for it (R15).
How a report is asked for and landed: the amazon-ads skill's references/door.md.

## References

[serving.md](references/serving.md): Featured Offer, eligibility, statuses, money stops.
[reads.md](references/reads.md): hosts, profiles, global accounts, offer reads.
[metrics.md](references/metrics.md): attribution, definitions, invalid traffic, settling.
[reports.md](references/reports.md): v3, v1, limits, Stream, console data.
[decomposition.md](references/decomposition.md): metric chain, benchmarks, change methods.
[vendors.md](references/vendors.md): vendor profiles, purchase orders, supply.
