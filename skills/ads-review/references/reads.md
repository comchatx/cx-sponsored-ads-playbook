# Reads: hosts, profiles, accounts and the offer behind an ad

## Hosts, tokens and permissions

- Origins, headers, the token trade and the refresh token's expiry: the amazon-ads skill's references/door.md.
- The Ads API's three regional hosts, NA, EU and FE, each have their own marketplace list; Ireland is a country code that the Profiles model tables under region EU, while Amazon's endpoint tables omit it (A1).
- Login with Amazon tokens are valid in every region, and an access token lives 60 minutes (A2).
- The `advertising::campaign_management` scope lets an application act with whatever advertising permissions the authorising user holds; each operation names the permissions it requires, and too little permission answers 401 (A3).

## Profiles and global accounts

- A profile is one advertiser account in one marketplace; the profile list returns nothing for an account that has never created a campaign, and types each profile as `seller`, `vendor` or `agency`, with `KDP_AUTHOR` as a sub-type (A4).
- The United Kingdom is `UK` in the Profiles model and `GB` in the v1 `Marketplace` and `CountryCode` enums (A6).
- Ads API v1 reporting, v1 recommendations and Stream v2 identify the advertiser by a global account id (`amzn1.ads-account.g.*`), not by profile (A5).
- v1's advertiser-account query maps each global account to its per-marketplace `profileId`s, paging by `nextToken`, with pages that can be empty while a `nextToken` remains (A5).
- Amazon names it the replacement for the legacy `adsAccounts` operations, which answer `Warning: 299` from July 2026, block new client integrations (existing callers continue "through an allowlist") and answer `404` from July 2027 (A5).
- Stream v2 takes no manager account id, Vendor Group id or Seller Central merchant id (A5).

## The offer behind an ad

- Amazon states that an offer whose price plus shipping is above the Competitive External Price, where one exists, or above recent prices is ineligible to be the Featured Offer at that price "regardless of changes to price or stock of competitors" (A11).
- SP-API exposes the reference prices (`PRICING_HEALTH`), the price at or below which an offer can expect to win, which Amazon says "is not guaranteed" (`getFeaturedOfferExpectedPriceBatch`, up to 40 SKUs), and the winner per customer segment (`getCompetitiveSummary`) (A11).
- Landed price subtracts points, a program that exists only in Japan (A11).
- Repricer.com and AMALYZE hold that price moves Featured Offer status and conversion, without publishing data or a method (A11).
- The Buy Box holder over time is in Keepa's histories, `-1` when no offer or seller qualified, and the current holder in SP-API `getItemOffers` as `IsBuyBoxWinner` (A12).
- Sales and Traffic's `buyBoxPercentage` is the share of page views with a buy box, and that report's `refundRate` description reads inverted (A12).
- A listing can be hidden from search by the Listings Items enforcement action `SEARCH_SUPPRESSED`, and Catalog Items returns variation relationships (A13).
- Between 2026-02-12 and 2026-05-31, by category, Amazon stopped sharing reviews between variations "with significant differences", which Amazon says may affect a product's overall star ratings and review counts (A13).
- PPC Land's Luis Rijo states that the star rating under a sponsored product comes from the same shared or non-shared review pool, so a variation that loses shared reviews shows a lower rating in its ad unit (A13).
- SP-API notifications (`ANY_OFFER_CHANGED`, `PRICING_HEALTH`, `FBA_INVENTORY_AVAILABILITY_CHANGES`, listing issues) need an SQS or EventBridge destination; the same facts can be polled from documented reads (A14).
