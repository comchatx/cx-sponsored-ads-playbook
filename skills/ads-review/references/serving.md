# Serving: the Featured Offer, statuses and money stops

## The Featured Offer

- A Sponsored Products or display ad serves only while the advertised product holds the Featured Offer and is in stock, judged at the moment the shopper views it (A8).
- An advertised product that goes out of stock is paused within its campaign, and a product without the Featured Offer gets zero impressions even when the campaign runs (A8).
- Amazon's ad rules bind each ad to its own advertiser's offer: SP and Display serve only for the advertised ASIN or SKU that holds the Featured Offer, and the previous holder's impressions stop immediately when it shifts (A25).
- The Eligibility API answers only for products sold by the profile's merchant, and vendor SP attribution counts only products sold by Amazon (A25).
- For books, SP ads from an author ads account show only when Amazon itself, not a third-party seller, is the Featured Offer, and a seller's ads only when the seller's own offer is (A25).
- When another seller holds the Featured Offer on a brand's own ASIN, the brand's SP and display ads for that ASIN serve no impressions, while its Sponsored Brands ads keep serving and send shoppers to a page whose default offer is the other seller's (A9).
- Amazon routes that case to Seller Support: "Advertising Support can't directly restore Featured Offer eligibility" (A9).
- Canopy Management, Pattern UK and a seller in the Seller Forums describe spend reaching the other seller's offer (A9).
- Trellis's page says SP ads "keep running" after a Buy Box loss, against Amazon's page (A9).
- Rel.ai names Buy Box loss as the most common cause of a sudden SP impression drop, with the console showing a campaign as delivering while its ads are skipped (A9).
- Amazon's Japanese seller page states that Sponsored Products and Sponsored Display require Featured Offer eligibility, while Sponsored Brands ads are shown even when the advertiser's product is not the Featured Offer (A26).
- Amazon's AMS-era agency toolkit (August 2017) stated that "ASINs must meet retail financial thresholds to be eligible for promotion through Amazon Marketing Services", that an SP ad paused when the vendor lost the buy box or the ASIN went out of stock and resumed automatically, and that Headline Search needed at least three ASINs in stock and one past the financial threshold (A26).
- The same toolkit stated that Headline Search and Product Display ads continued to serve when the buy box was lost; for Display, the current Featured Offer page above supersedes it (A26).
- Ad products and their policy: ../ads-launch/references/products-and-policy.md.

## Featured Offer eligibility in 2026

- Amazon announced on 2026-07-06 that "Starting in July 2026, we'll begin removing seller eligibility requirements for the Featured Offer", rolling out gradually and completing by the end of 2026, and that "We're not changing how the Featured Offer is selected" (A10).
- Seller Central's *Featured Offer eligibility* page as captured on 2026-10-14 reads "As of September 2026, Amazon no longer maintains a seller eligibility requirement", while the ads guides read on 2026-11-09 still say an advertised product "must be eligible to be the featured offer" (A10).

## Product eligibility

- The Eligibility API's product eligibility check takes ASINs, SKU optional, and an ad type (`sp` by default, `sb`, `sd` or `dsp`), and returns per-product statuses, each `INELIGIBLE` or `ELIGIBLE_WITH_WARNING`, that include `NOT_IN_BUYBOX`, `OUT_OF_STOCK` and `INELIGIBLE_PRODUCT_COST` (A27).
- The SP 3.0 serving-status reasons include `CP_INELIGIBLE`, `CP_INELIGIBLE_ASIN`, `CP_INELIGIBLE_UNKNOWN` and `CP_INELIGIBLE_VENDOR`, which Amazon's model does not describe (A27).
- CNBC reported in 2019 that Amazon emailed vendors that products "no longer qualif[y] for advertising" because their sale "currently results in a loss to Amazon", glossing the practice as CRaP ("Can't Realize a Profit"), a term no Amazon page read in 2026 uses (A27).
- Flywheel (Gabe Fishbein, 2024) reports a rise in ASINs becoming ineligible for Sponsored Products after Amazon re-evaluated "safe-listed" unprofitable ASINs, in their account only SP placements being affected and some ASINs restored through Amazon reps (A27).
- MerchantSpring (Rachel Seiton) and SellerApp (Brij Purohit) state that a CRaP-flagged product loses Sponsored Products or advertising eligibility and that Amazon may then stop issuing purchase orders for it (A27).

## Serving statuses and delivery reasons

- Sponsored Products v3 returns the serving status of every entity in `extendedData` when extended data is requested, with values such as `AD_NOT_IN_BUYBOX`, `AD_OUT_OF_STOCK` and `AD_NO_PURCHASABLE_OFFER` (A15).
- Sponsored Brands and Sponsored Display keep their own, largely shared enums (A15).
- The extended-data flag's request description and the response schema name the fields differently, and extended-data list calls weigh five times a standard call against the rate limit (A15).
- In Ads API v1 an entity carries a user-set `state` (`DRAFT`, `PROPOSED`, `ENABLED`, `PAUSED`, `ARCHIVED`) and a separate `status.deliveryStatus` (`DELIVERING`, `LIMITED`, `NOT_DELIVERING`, `UNAVAILABLE`) with `deliveryReasons` (A16).
- SP v1 writes accept `ENABLED` and `PAUSED` only (A16).
- Amazon Ads Status publishes six months of incidents by region and category (ad delivery, campaign management, reports, Marketing Stream) as a page and a `history.json` (A19).

## Money stops

- Every money stop has a name: SP serving statuses and v1 delivery reasons distinguish campaign, portfolio and account out of budget, payment failure and prepay balance (A17).
- A portfolio's state shows in its campaigns' reasons (A17).
- Sponsored Brands v4 lists `PORTFOLIO_OUT_OF_BUDGET`, although the common enums page does not (A17).
- When Amazon cannot charge the default payment method the account's campaigns pause, while a backup method, if one is set, is charged without pausing them (A18).
- Amazon retries at a fixed frequency and reactivates when a payment succeeds (A18).
- Seller-account charges come from Funds Available, not Total Balance (A18).
- Billing notifications carry an impact (`CAMPAIGNS_SUSPENDED` or `NO_IMPACT`), a severity and a suspension date, and the billing API reports each account's billing state (A18).
