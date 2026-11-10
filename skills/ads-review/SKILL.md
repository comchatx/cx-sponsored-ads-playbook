---
name: ads-review
description: "How a seller's Sponsored Products, Sponsored Brands and Sponsored Display ads serve and perform, and why: the Featured Offer and stock behind an ad, serving statuses and money stops, what each metric counts and when it settles, which report or stream carries each figure, and a vendor's supply. For reviewing, watching or diagnosing a seller's sponsored ads."
---

## Serving

A Sponsored Products or display ad serves only while its product holds the Featured Offer and is in stock, judged when the shopper views it; an out-of-stock product is paused within its campaign, and one without the Featured Offer gets zero impressions even when the campaign runs (A8).
SP v3 with `includeExtendedDataFields` returns every entity's serving status, so an ad can read `AD_NOT_IN_BUYBOX` or `AD_OUT_OF_STOCK` while its campaign runs; statuses and v1 `deliveryReasons` also name each money stop (A8, A15, A16, A17).
`getItemOffers` names the current Buy Box holder (`IsBuyBoxWinner`) (A12).
When another seller holds the Featured Offer on a brand's own ASIN, its Sponsored Brands ads keep serving, sending shoppers to a page whose default offer is the other seller's; Amazon routes the case to Seller Support (A9).

## Diagnosis

On a cost-per-click row spend equals impressions × CTR × CPC (A7).

## Metrics

Sponsored ads report a conversion on the date of the ad interaction, not necessarily the conversion date (M1).
Sponsored Products credits 7 days of clicks for sellers, to the advertised product and anything else the merchant sells, and 14 for vendors; v3 carries SP 1-, 7-, 14- and 30-day purchases and sales with same-SKU and other-SKU variants (M3, M8).
Impressions and clicks change for up to three days; conversions are first reported within 24 hours and restated up to 42 days for a 14-day window, and no report marks a day final (M14).

## Reports

Reporting v3, Sponsored Ads v2 reporting and Marketing Stream v1 stop delivering data on 2027-06-30; Reporting v1 and Stream v2 have been generally available since 2026-09-30 (R1).
Reports hold only entities with activity in the range (R14).
Hourly data beyond Reporting v1's span comes only by Marketing Stream, to the subscriber's own AWS destination, which ComChatX does not run (R12, R15).
Asking for and landing a report: the amazon-ads skill's references/door.md.

## References

[serving.md](references/serving.md): Featured Offer, 2026 eligibility change, statuses, money stops.
[reads.md](references/reads.md): hosts, profiles, accounts, offer price, Buy Box history.
[metrics.md](references/metrics.md): attribution, definitions, invalid traffic, settling.
[reports.md](references/reports.md): v3, v1, hourly data, limits, Stream, console.
[decomposition.md](references/decomposition.md): metric chain, cause orders, benchmarks, shift or noise.
[vendors.md](references/vendors.md): vendor profiles, purchase orders, supply.
[history.md](../ads-change/references/history.md): change history.
