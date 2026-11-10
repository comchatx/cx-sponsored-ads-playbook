---
name: ads-launch
description: "Who may run sponsored ads on Amazon and what a new product's first campaign meets: seller, vendor and Brand Registry eligibility, product and program eligibility reads, the ad products and their placements, ad policy, moderation, billing and API terms, launch programs (new-seller credits, Vine, coupons, Review Requests), how a first campaign is built, and what is known of new-product ranking. For opening an account's sponsored ads or launching a product's ads."
---

## Door

The amazon-ads skill (cx-amazon-ads) carries every call; its references/door.md holds origins, headers, token, paths and reports.

## Who may advertise

- Sponsored Products needs a Professional plan or vendor account and an eligible category; variation parents and suppressed listings cannot be advertised (L1).
- Sponsored Brands, display ads, Streaming TV and Stores need Brand Registry or a vendor account; Amazon states vendors need not enroll in Brand Registry to advertise (L2, L22).
- `POST /eligibility/product/list` rates each product and ad type `ELIGIBLE`, `ELIGIBLE_WITH_WARNING` or `INELIGIBLE` with reasons; `POST /eligibility/programs` reads per marketplace the account's access to `SB`, `SD` and other programs (P1, P2).
- No eligibility reason reads reviews; Amazon's five or more reviews at 3.5 stars is guidance (L3).

## New products

- `POST /product/metadata` returns `createdDate`, the date the item was first available on Amazon; recommendations group unadvertised, recently added ASINs as `NEW_ASIN` (L4).
- Amazon's 30-day roadmap puts active listings with stock, Sponsored Products campaigns and coupons on day one (L9).
- Review Requests (US beta) is a Sponsored Products campaign with goal `ENGAGEMENT`, billed per rating or review left on the ad card (L15).
- No Amazon page claims a "honeymoon" ranking boost in Amazon's own voice, and practitioners disagree (L13).

## First campaign

- Amazon recommends a new advertiser start with automatic Sponsored Products and use its search term report to find manual targets; its guides differ on when manual targeting joins (L10).
- An auto campaign serves once it has an active campaign, ad group and product ad, before any negative; both create APIs accept `PAUSED` as the first state (L20).
- For a campaign not yet created, the API returns keyword suggestions, new-ad-group bids and an initial budget, `-1` when information is short (L11).

## Policy and billing

- Moderation usually ends within 24 hours, up to 3 business days; `POST /moderation/results` reports SP, SB and display status with reasons (P9).
- A payment failure pauses campaigns (P13, P20).

## References

- references/accounts.md: sellers, vendors, Brand Registry, links.
- references/products-and-policy.md: eligibility, ad products, policy, moderation, billing, terms.
- references/new-products.md: credits, Vine, coupons, Review Requests, rank rules.
- references/first-campaign.md: build order, recommendations, time marks, practitioners.
- references/new-product-ranking.md: honeymoon, cold start, launch multiples, research.
