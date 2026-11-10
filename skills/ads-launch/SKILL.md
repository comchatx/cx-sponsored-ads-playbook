---
name: ads-launch
description: "Who may run sponsored ads on Amazon and what a new product's first campaign meets: seller, vendor and Brand Registry eligibility, product and program eligibility reads, the ad products and their placements, ad policy, moderation, billing and API terms, launch programs (new-seller credits, Vine, coupons, Review Requests), how a first campaign is built, its budget suggestions and time marks, practitioners' opening bids, and what is known of new-product ranking. For opening an account's sponsored ads or launching a product's ads."
---

## Door

The amazon-ads skill (cx-amazon-ads) carries every call; its references/door.md: headers, paths, reports.

## Who may advertise

- Sponsored Products needs a Professional plan or vendor account and an eligible category; variation parents and suppressed listings cannot be advertised (L1).
- Sponsored Brands, display ads, Streaming TV and Stores need Brand Registry or a vendor account; vendors need not enroll to advertise (L2, L22).
- Product eligibility rates each product and ad type `ELIGIBLE`, `ELIGIBLE_WITH_WARNING` or `INELIGIBLE` with reasons (P1).
- No eligibility reason reads reviews; Amazon's five or more reviews at 3.5 stars is guidance (L3).

## New products

- Product metadata returns `createdDate`, the item's first-available date on Amazon (L4).
- Review Requests (US beta): an SP campaign with goal `ENGAGEMENT`, billed per rating or review left on its ad card (L15).
- No Amazon page claims a "honeymoon" ranking boost in Amazon's own voice; practitioners disagree (L13).

## First campaign

- Amazon recommends a new advertiser start with automatic Sponsored Products and use its search term report to find manual targets; its guides differ on when manual targeting joins (L10).
- Amazon's guides build a campaign by separate creates, in order: campaign, ad group, product ad (SKU for sellers, ASIN for vendors), then targets; an auto campaign serves once those three are active, before any negative; both create APIs accept `PAUSED` as first state (L20).
- Before a campaign exists, the API suggests keywords, new-ad-group bids and an initial budget (`-1` when information is short); Amazon suggests $10 a day, above the API minimum (L11).
- Amazon's new-campaign time marks: metrics checked at least twice weekly in week one; match types tested at least one to two weeks before keywords pause; at least 20 clicks before a keyword becomes a negative; negatives left two weeks or more before a strategy change (L12).
- Practitioners' opening bids: Canopy Management above Amazon's suggestion, Ad Badger conservative on manual bids, ecomcrew narrow on exact match, high bids, widening later (L19).

## References

- references/accounts.md: sellers, vendors, Brand Registry; references/products-and-policy.md: eligibility, ad products, policy, moderation, billing, terms; references/new-products.md: credits, Vine, roadmap, coupons, rank manipulation; references/first-campaign.md: launch ACoS bands; references/new-product-ranking.md: cold start, launch multiples.
- Existing campaigns' serving and budget: ../ads-review/references/serving.md, ../ads-bids-and-budgets/references/budgets.md.
