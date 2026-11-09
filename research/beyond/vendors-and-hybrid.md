# Vendors and hybrid brands: advertising a 1P book, and a brand with both a 1P and a 3P offer

Read 2026-11-09 by the research seat.

Tags: [official] is an Amazon page, cited by page name and URL and read 2026-11-09 unless another date is given. That covers Amazon Ads help, library guides, API guides as CloudFront Markdown, OpenAPI models, SP-API documentation on developer-docs.amazon, the public `amzn/selling-partner-api-models` repository, Amazon PDFs on m.media-amazon.com, Amazon Science, and Amazon staff replies in Seller Forums. [opinion] is a named practitioner, agency or paid tool, with the person or firm given. [press] is a news report, kept apart from both. [research] is a paper or academic working paper. [seat] is this seat's own reading and is never a position. Figures (percentages, dollar amounts, day counts, lag hours, character limits) are recorded with page and date **for human readers only**. A skill reads the live figure at run time from the operation named in *What cx must read at run time*.

## What this covers

This file covers what changes when the advertiser on a cx-amazon-ads profile is an Amazon **vendor**, meaning a first-party (1P) supplier who sells to Amazon, which then resells to shoppers. It also covers the **hybrid** brand that has both a vendor relationship and a Seller Central (3P) offer, sometimes on the same ASIN. The file covers:

- the vendor profile type, and what the Ads API does differently for vendors (ASIN against SKU, attribution windows, eligibility, Brand Registry, payment fields, names, landing pages);
- attribution for vendors: the 14-day window, brand halo, and the "sold by Amazon" limit;
- why a vendor's ASIN stops serving: stock driven by Amazon's purchase orders, the Featured Offer, "financial thresholds" and CRaP, and the eligibility statuses the API returns;
- Net PPM as Amazon defines it, and what Amazon's own fields say about advertising inside it;
- the purchase-order mechanism (the Vendor Orders API) and the retail-analytics fields that read availability and supply;
- the SP-API Vendor Retail Analytics reports and the Data Kiosk vendor dataset as the vendor's total-sales denominator: the manufacturing and sourcing views, ordered against shipped revenue, Pacific time, and lags;
- Brand Analytics for vendors: which reports exist, and the absence of Search Query Performance;
- vendor-funded promotions (Best Deal, Lightning Deal, Price Discount, Promo Code, vendor-powered coupons): their funding, their reporting, and their lead times as Amazon last published them;
- hybrid brands: which offer an ad serves, the Featured Offer between Amazon retail and the brand's own offer, two advertising accounts, and the attribution rule that separates merchant and brand;
- named practitioners who run vendor books;
- research on reseller (wholesale) against marketplace (agency) models, and on co-op advertising and pass-through, where it bears on ads.

It stays in its lane. Mechanics that hold for any advertiser are owned elsewhere and only cross-referenced here:

- the attribution table for every ad product, and window suffixes in reports: `beyond/metrics-and-attribution.md` (P-metrics-and-attribution-3, P-metrics-and-attribution-11) and `method/reporting.md` (P-reporting-17);
- which ad products a vendor may buy, Stores, Streaming TV and payment methods in general: `beyond/ad-products-and-eligibility.md` (P-ad-products-and-eligibility-1 to 5, 19, 41);
- TACoS as Amazon names it, and the seller-side total-sales denominator: `areas/ads-organic-and-total.md` (P-ads-organic-and-total-6). Its D8 to D11 and P-ads-organic-and-total-21 to 23 already state the Vendor Sales report fields, Pacific time and the AMC Manufacturing match. This file adds the sourcing view, Data Kiosk, the inventory and PO fields, and the question of which view is the denominator;
- profile types and duplicate names in the API surface: `method/ads-api-surface.md` (P-ads-api-surface-9, 19, 37);
- campaign name lengths: `areas/campaign-structure.md` (P-campaign-structure-19). The create-sequence consequence of duplicate vendor names: `areas/launch.md` (P-launch-41, P-launch-44);
- campaign-level negative product targets on manual campaigns, which the API guide calls vendor-only: `areas/keyword-and-product-targeting.md` (P-keyword-and-product-targeting-23), `areas/search-terms-and-negatives.md` (P-search-terms-and-negatives-17) and `beyond/brand-defense-and-competition.md` (P-brand-defense-and-competition-17);
- budget-rule windows: `areas/budgets-and-pacing.md` (P-budgets-and-pacing-19) and `areas/seasons-and-deals.md` (P-seasons-and-deals-9). The billing API: P-budgets-and-pacing-35;
- deal and event calendars for sellers, and the AMC Amazon Retail Purchases promotion columns: `areas/seasons-and-deals.md` (P-seasons-and-deals-44);
- serving statuses in general: `areas/diagnosis.md`;
- goals and seller margin: `beyond/goals-and-economics.md`. It names the Net PPM report but leaves vendor margin out, and this file takes that up;
- listing content, A+ and content precedence between a vendor and a seller contribution, and the Featured Offer's own mechanics (pricing health, EU commitments, Keepa's Amazon-offer fields): the listing pack's `cx-listing-playbook/research/angles/vendor-and-hybrid.md` (read 2026-10-14). Nothing from that file is cited here unless the page was re-opened today.

Out of scope: Amazon DSP buying by vendors; Vendor Central operations that do not meet ads (chargebacks, shipment compliance, invoicing); direct fulfillment (DF) logistics beyond its place in the SP eligibility criteria.

## Amazon's own rules and guidance

Each claim is marked RULE (Amazon states it as how the system works) or GUIDANCE (Amazon advises it). Help pages are cited by node id (`advertising.amazon.com/help/<id>`) with their `lastModified`. Library guides are cited with their `dateModified`. API guides are cited by their CloudFront Markdown path under `https://d3a0d0y2hgofx6.cloudfront.net/en-us/`.

### A. Who a vendor is, and how a vendor reaches the advertising console

**A1. RULE: the definition.** Amazon's Ads FAQ: "Vendors sell their items directly to Amazon, who then sells them to customers." The Well-Architected framework guide uses the same words: "**Amazon vendor**: Vendors sell their items directly to Amazon, who then sells them to customers." [official] *FAQs - Advertising questions and resources*, https://advertising.amazon.com/resources/faq; *Amazon Ads Well-Architected Framework, fundamental component*, `guides/amazon-ads-well-architected-framework/fundamental-component.md`.

**A2. RULE: which vendors may run Sponsored Products.** The FAQ lists the Sponsored Products vendor criteria as "Vendors can be a (must meet at least ONE criterion)": Hardlines vendor, Softlines vendor, "Supplier Express vendor (aka Vendor Express vendors) with a confirmed purchase order or direct fulfillment order", Media vendor, Books vendor, Consumables vendor. It adds: "In addition, listings advertised on Sponsored Products must be eligible for the Featured Offer", and "Ads that are not eligible are flagged in the campaign manager." For Sponsored Brands its vendor list ("must meet at least ONE criterion") is Hardlines, Softlines, Media, Books and "Consumables (non-Pantry/Fresh)" vendors, with no Supplier Express line. [official] *FAQs - Advertising questions and resources* (the Amazon Ads FAQ).

**A3. RULE: Brand Registry is a seller requirement, not a vendor one.** The FAQ: "Only sellers must enroll in Amazon Brand Registry—vendors do not need to enroll." The help pages agree for the ad products:

- *Understand Sponsored Brands*: "Sponsored Brands is only available to vendors and professional sellers enrolled in the Amazon Brand Registry."
- *Understand Display*: "If you're a vendor or professional seller enrolled in Amazon Brand Registry, you can reach audiences wherever they spend their time in Amazon-owned and partner networks."
- *Sponsored Brands eligibility requirements*: "You must have an active Professional Seller account or be an approved Amazon Vendor."

Sources: [official] help GGWFYHL27MFXLHS6 (lastModified 2026-10-20); GHYXY6HJRDM5VCCY (2026-11-02); G5DAD7ZM3N639QF4 (2026-08-27).

The SP-API Brand Analytics reports are a separate case. Their availability line requires Brand Registry for sellers and vendors alike (see H2). So "a vendor needs no Brand Registry" holds for the ad products. It does not hold for the Brand Analytics reports a skill might read beside them.

**A4. RULE: Brand Registry accounts reuse the Vendor Central login.** Brand Registry's public pages: "If you have a Seller Central or Vendor Central account, use the same username and password to create your Brand Registry account." [official] *Amazon Brand Registry | Sell on Amazon*, https://sell.amazon.com/brand-registry. The three `brandservices.amazon.com` addresses (home, /eligibility, /faq) now redirect to that one page; the sentence is in its FAQ block.

**A5. RULE: linking a Vendor Central account to an advertising account.** The help page *Link a Vendor Central account to your advertising account* (G2P4Y4LNP84V8DST, lastModified 2026-02-23) says:

- the link is made in Access and Settings > Selling Accounts;
- "An advertising account can only be linked to 1 Vendor Central account."
- it addresses the case "If you only see vendor codes or nothing linked";
- a representative can request the link; the vendor signs in with Vendor Central credentials to approve it, and a vendor user who "aren't eligible to approve" can forward the request to "someone who has admin privileges on the Vendor Central account".

[official].

**A6. RULE: the vendor guide's two portals.** *Advertising solutions for Amazon vendors* (library guide, datePublished 2020-05-18, dateModified 2026-10-09) names "Vendor Central or Advantage Central" as the vendor's selling portal. It states the attribution window in the vendor's terms: "A sale is attributed to a campaign when a shopper that clicks an ad purchases your brand's products on Amazon within 14 days." [official] https://advertising.amazon.com/library/guides/vendors.

**A7. RULE: selling accounts in the API registration flow.** The registration guide says:

- "A selling account is an Amazon retail relationship. Commonly, these represent Seller Central, Vendor Central, Author Central, and similar portals."
- `POST /adsApi/v1/query/sellingAccounts` will "Fetch all Amazon retail selling accounts (for example, Seller, Vendor, Author, KDP, etc.) that a given user has access to".
- The query-advertiser-accounts guide: "The `sellingAccountLinkRequests` array contains tokens representing relationships between advertiser accounts and selling entities (seller, vendor, author)."

[official] `guides/account-management/registration.md`; `guides/account-management/query-advertiser-accounts.md`.

**A8. RULE: vendor codes.** The test-accounts guide: "A vendor code is a five-character code for a registered vendor. Test accounts created with a vendor code can use the product `ASIN`s and metadata of the linked vendor for test campaign creation." A test vendor account is created with `"accountType": "VENDOR"` and an optional `accountMetaData.vendorCode`. The guide shows where the code is found: Administration > Access and settings > Selling account > Account Associations. [official] `guides/account-management/test-accounts/create-test-accounts.md`. The test-account rule itself is P-ads-api-surface-37.

The SP-API Data Kiosk schema describes the code hierarchy: "The hierarchy of vendor codes (parent-child relationships) plays an important role in the storage and retrieval of vendor item information, for example, cost (VCS) and external IDs (VXPS). Child codes are generally assumed to be ordering codes that are for the same vendor, represented by the parent vendor code." [official] `analytics_vendorAnalytics_2024_09_30.graphql`, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_vendorAnalytics_2024_09_30.graphql.

**A9. RULE: vendor permissions are set in the advertising console, seller permissions in Seller Central.** The permissions guide:

- "For vendor accounts, permission can be shared in the advertising console according to three default tiers": Viewer, Editor, Admin;
- the granular permissions include `advertiser_campaign_view` and `advertiser_campaign_edit`, `nemo_report_view` and `nemo_report_edit`, `amazon_stores_edit`, and `nemo_transactions_view` and `nemo_transactions_edit`;
- "For seller accounts, admin users can manage granular permissions in Seller Central after inviting another user."

[official] `guides/account-management/permissions.md`.

**A10. RULE: Stream v2 does not take a vendor group id.** The Stream v2 subscription guide lists identifiers that are "**not** accepted", among them selling-partner IDs such as "a **Seller Central account ID** (MCID...)" or a "Vendor Group" ID. The advertiser id must be "a Global Account ID or an Amazon DSP (ADSP) advertiser account ID". [official] `guides/amazon-marketing-stream/v2/create-a-subscription.md`; `guides/amazon-marketing-stream/v2/get-started.md`. P-ads-api-surface-11 covers the seller side of the same rule.

### B. The vendor profile in the Ads API

**B1. RULE: profile type and what it serves.** The profiles guide's account-type table: "`vendor` | Vendor | The account is a vendor account. Vendor accounts are used with Sponsored Products, Sponsored Brands, and Sponsored Display only." The Profiles 3.0 model: "The `seller` and `vendor` account types are associated with Sponsored Ads APIs. The `agency` account type is associated with DSP and Data Provider APIs." [official] `guides/account-management/authorization/profiles.md`; *Profiles 3.0* OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml. The enum itself is P-ads-api-surface-9 and P-ad-products-and-eligibility-5.

**B2. RULE: the fields that differ on a vendor profile.** From the Profiles 3.0 model:

- `accountInfo.validPaymentMethod`: "Only present for Vendors, this returns whether the Advertiser has set up a valid payment method or not."
- The `validPaymentMethodFilter` query parameter: "Setting this filter to `true` returns only profiles with either no `validPaymentMethod` field, or the `validPaymentMethod` field set to `true`. Setting this to `false` returns profiles with the `validPaymentMethod` field set to `false` only."
- The profile `dailyBudget`: "Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts."
- `PUT /v2/profiles`: "Note that this operation is only used for Sellers using Sponsored Products. This operation is not enabled for vendor type accounts."
- `accountInfo.id`: "Identifier for sellers and vendors. Note that this value is not unique and may be the same across marketplace."

[official] *Profiles 3.0* OpenAPI.

**B3. RULE: a vendor advertises an ASIN; a seller advertises a SKU.**

- The SP product-ads guide: "Each product ad is associated to a single product, either by `SKU` (sellers) or `ASIN` (vendors and authors)." Also: "To create a product ad, you must include `adGroupId`, `asin` (vendors and KDP authors) or `sku` (sellers), and `state`." And: "Vendors should include an `ASIN` in the request body." [official] `guides/sponsored-products/product-ads.md`.
- The SP v2 model: `asin` "The ASIN associated with the product. Defined for vendors only."; `sku` "The SKU associated with the product. Defined for seller accounts only." [official] *Sponsored Products 2.0* OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-products/2-0/openapi.yaml. The SP 3.0 JSON model repeats "The ASIN associated with the product. Defined for vendors only." [official] `SponsoredProducts_prod_3p.json`, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json.
- Sponsored Display: "In the request, vendors use the `asin` field where sellers use the `sku` field. Both fields can accept an `ASIN`." [official] `guides/sponsored-display/audience-targeting.md`.
- The v3 report columns: advertised SKU, "The `SKU` being advertised. Not available for vendors." [official] `guides/reporting/v3/columns.md`.
- The Stream campaign-management dataset: `asin` "Relevant for Sponsored Products and Sponsored Display vendors and KDP." [official] `guides/amazon-marketing-stream/datasets/sponsored-ads-campaign-management.md`.
- The Recommendations model: "ASIN associated with the product. Defined for vendors only." [official] `Recommendations_prod_3p.json`.
- The exception is Review Requests: "Both vendors and sellers supply the ASIN in `customerActionSettings.product.productId` with `productIdType: ASIN`. A SKU is not required." [official] `guides/review-requests/faq.md`.

**B4. RULE: vendors may hold duplicate campaign names; sellers may not.** The SP v2 model's campaign `name`: "A name for the campaign. Note that idempotency for this field works different for sellers and vendors. Sellers aren't allowed to have duplicate campaign names, but vendors can have duplicate campaign names." [official] *Sponsored Products 2.0* OpenAPI. This is P-ads-api-surface-19 (which also cites SB v3). The create-sequence consequence is P-launch-44: a repeated create with the same name is refused for a seller and is not refused for a vendor. The length limit (116 characters for vendors, 128 for sellers) is P-campaign-structure-19.

**B5. RULE: landing pages that only vendors may set.**

- The SB model: "URL of a Store page. Vendors may also specify the URL of a custom landing page. If a custom URL is specified, the landing page must include the ASINs of at least three products that are advertised as part of the campaign. Do not include this property in the request if the asins property is also included, these properties are mutually exclusive."
- The SB keyword recommendations: "Creates an array of keyword recommendation objects for a set of ASINs included either on a landing page or a Stores page. Vendors may also specify a custom landing page."
- The merged model's `ProductCollectionLandingPageType`: "`CUSTOM_URL` | A custom landing page. Available for vendors only."

[official] `SponsoredBrands_prod_3p.json`; `AmazonAdsAPIALLMerged_prod_3p.json` (https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/).

**B6. RULE: other vendor-specific API lines.**

- SP custom text ads: "The custom text to use for creating a custom text ad for the associated ASIN. Defined only for KDP Authors and Book Vendors in US marketplace." [official] `SponsoredProducts_prod_3p.json`.
- Brand negative-target recommendations: `GET /sp/negativeTargets/brands/recommendations` "Returns brands recommended for negative targeting. Only available for Sellers and Vendors. These recommendations include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands." [official] `SponsoredProducts_prod_3p.json`; `SponsoredBrands_prod_3p.json`.
- Product selector paging: "For author, this value will be ignored, should use cursorToken instead. For seller and vendor, results are capped at 10k ((pageIndex + 1) * pageSize)." [official] `ProductSelector_prod_3p.json`.
- Campaign-level negative product targeting: "Campaign-level negative product targeting for manual campaigns is only available for vendors. Sellers can add campaign-level negative targeting to auto campaigns, but not manual." [official] `guides/sponsored-products/negative-targeting/product-brand.md`. The conflict with the 2025-05-22 release note is P-keyword-and-product-targeting-23 and P-search-terms-and-negatives-17.
- Sponsored Display tactics: "These campaign types are available to both **seller brand owners** and **vendors**. Note that advertisers that do not sell on Amazon can only use Audience targeting." Contextual targeting `T00020` is "Seller, vendor"; Audiences `T00030` is "Seller, vendor, advertisers that do not sell on Amazon." [official] `guides/sponsored-display/overview.md`.
- New-to-brand columns: v3 new-to-brand metrics carry "Not available for book vendors." [official] `guides/reporting/v3/columns.md`.
- Amazon Attribution and Brand Metrics: Attribution "is currently available in beta to professional seller brand owners enrolled in Amazon Brand Registry and vendors that sell products on Amazon" in listed markets. Brand Metrics "is in open beta and available to professional sellers enrolled in Amazon Brand Registry and vendors that sell products on Amazon". [official] `guides/amazon-attribution/overview.md`; `guides/reporting/brand-metrics/overview.md`.

**B7. RULE: the Eligibility API is bound to the profile's merchant.** `POST /eligibility/product/list`: "Gets a list of advertising eligibility objects for a set of products. Requests are permitted only for products sold by the merchant associated with the profile. Note that the request object is a list of ASINs, but multiple SKUs are returned if there is more than one SKU associated with an ASIN. If a product is not eligible for advertising, the response includes an object describing the reasons for ineligibility." `ProductDetails` "requires" `asin`; `sku` is optional ("A seller product identifier"). [official] *Eligibility* OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json; the product-ads guide names the same endpoint.

The `EligibilityStatus.name` enum is:

- ADULT_PRODUCT
- CLOSED_CATEGORY
- INELIGIBLE_CONDITION
- INELIGIBLE_OFFER
- INELIGIBLE_PRODUCT_COST
- LISTING_SUPRESSED (Amazon's spelling)
- MISSING_IMAGE
- MISSING_TITLE
- NOT_IN_BUYBOX
- OUT_OF_STOCK
- RESTRICTED_CATEGORY
- VARIATION_PARENT

The product request carries an `adType` of `sp` (the default), `sb`, `sd` or `dsp`: "Set to 'sp' to check product eligibility for Sponsored Products advertisements. Set to 'sb' to check product eligibility for Sponsored Brands advertisements…". Each status carries a `severity`: "If set to `INELIGIBLE`, the product cannot be included in an advertisement. If set to `ELIGIBLE_WITH_WARNING`, the product may not receive impressions when included in an advertisement." The advertiser-level eligibility objects are keyed by ad program, an `AdProgram` enum of DTC, MAAS, SB, SD and SPOT, and carry reason codes. Those codes include ADVERTISER_TYPE_NOT_SUPPORTED, BILL_TO_CC and BUSINESS_THRESHOLDS_NOT_MET; the model gives the reason codes no descriptions. [official] *Eligibility* OpenAPI (version 3.0).

**B8. RULE: the serving-status reasons that name a vendor.** The SP 3.0 model's `SponsoredProductsAdServingStatusReason` enum includes CP_INELIGIBLE, CP_INELIGIBLE_ASIN, CP_INELIGIBLE_UNKNOWN and CP_INELIGIBLE_VENDOR, beside ASIN_QUARANTINED, BRAND_REMOVED, CBA_NOT_SUPPORTED, CLOSED_GL, INELIGIBLE_CONDITION, INVENTORY_INCOMPLETE, ITEM_MISSING, LANDING_PAGE_INELIGIBLE and others. The model gives the CP_ values no description. [official] `SponsoredProducts_prod_3p.json`. Serving statuses in general are `areas/diagnosis.md`'s. The meaning of "CP" is open question 1.

[seat] "CP" may stand for contribution profit. The Data Kiosk schema uses "CP (Contribution Profit Amount)" in its `salesDiscount` definition (E3), and a CP_INELIGIBLE_VENDOR value would then be a vendor-level profitability block. No Amazon page read today says this, so it enters no position.

### C. Attribution for vendors

**C1. RULE: 14 days, brand halo, and only products sold by Amazon.** The help page *Ad campaign attribution* (GX7KDKHMWQYMJ385, lastModified 2026-10-20) gives the vendor and author row of its table as a 14-day window with brand halo, and adds: "Only products sold by Amazon are attributed." The full table, by ad product and advertiser, is P-metrics-and-attribution-3. This file adds two vendor consequences:

- A vendor's SP attributed sales count only purchases of the brand's products where Amazon was the seller.
- The same brand's 3P sales, when a hybrid brand also sells on Seller Central, are outside its vendor SP attribution.

The same table gives Sponsored Brands and Display a 14-day window for "All advertisers (must be registered brand owners)", with: "Attributed purchases may include sales by Amazon or third-party sellers, in New or Used condition." So a vendor's SB and SD attribution, unlike its SP attribution, is not limited to sales by Amazon. The vendor SP row is "Clicks only", and the page adds "Book products don't have a brand halo."

[official].

**C2. RULE: brand-level competition for attribution, and the merchant exception.** The same page:

- "Amazon will attribute a conversion to no more than 1 ad interaction across all campaigns and all advertisers";
- it ranks interactions: promoted-ASIN clicks first, then brand-halo clicks, then promoted views, then halo views;
- "Sponsored Products for sellers is a merchant-based ad program that doesn't normally compete for attribution with brands. However, if the same advertiser wins attribution as both a merchant and a brand, attribution will choose the more relevant ad".

[official] GX7KDKHMWQYMJ385.

[seat] For a hybrid brand the page names two cases. A seller's SP is merchant-based and does not normally compete with brand ads (vendor SP, SB, SD). Where the same advertiser wins as both merchant and brand, one ad gets the credit. The page does not say how "the same advertiser" is decided across a seller and a vendor account of one company. That is open question 2.

**C3. RULE: other clocks on the same page.** Cancellations within 72 hours are deducted, and the deduction can take up to 7 days to show. Conversions appear within up to 12 hours. "Attributed sales don't reflect any discounts applied in the cart. Attributed sales don't include tax." [official] GX7KDKHMWQYMJ385. These clocks are the same for vendors. They matter beside the retail-analytics clocks in G, which run on a different calendar.

**C4. RULE: the window in rules, reports and the console.**

- Budget rules: "These metrics are calculated using data from the previous 7 days for sellers and 14 days for vendors". Performance-based rules: "For sellers, the time period used for metric calculation is within 7 days of an ad click. For vendors, metrics are calculated within 14 days of an ad click." [official] `guides/rules/budget-rules/overview.md`; `guides/rules/budget-rules/performance-based.md`.
- The v1 reporting overview: "Base metrics automatically align with campaign defaults—7-day look-back for sellers and 14-day look-back for vendors—consistent with the advertising console and downloadable reports." Each v1 purchases metric maps to v3 names marked "[SP: 7d sellers / 14d vendors]". [official] `guides/reporting/ads-v1/overview.md`; `guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md`.
- The v2 advertising-console mapping has a heading "Sponsored Products (vendors), Sponsored Brands, & Sponsored Display" and a block "**Sponsored Products vendors**", which maps the console's vendor columns to "14 Day Total Orders" and "14 Day Total Sales". [official] `guides/reporting/v2/advertising-console.md`.

These are P-budgets-and-pacing-19, P-seasons-and-deals-9 and 24, P-search-terms-and-negatives-24 and P-reporting-17. The point for vendors is that a 7-day figure and a 14-day figure are not comparable across a hybrid brand's two profiles.

**C5. RULE: the vendor's attributed sales are retail prices, not wholesale.** The help page says attributed sales exclude cart discounts and tax (C3). The vendor's own revenue from Amazon is wholesale: `shippedCogs` is "the price Amazon paid to a vendor for item procurement" (E3). [official] GX7KDKHMWQYMJ385; Data Kiosk vendor schema.

[seat] A vendor ACOS computed on attributed sales measures spend against Amazon's retail revenue, not against the vendor's receipts. Its margin meaning differs from a seller's ACOS. No Amazon page says this in these words.

### D. Why a vendor's ASIN stops serving: stock, the Featured Offer, and "financial thresholds"

**D1. RULE: the Featured Offer and stock gates.**

- The Ads FAQ: "If your product isn't the Featured Offer or is out of stock, your ad will not display."
- *Best practices for your Sponsored Products ads* (library guide at `/library/guides/sponsored-products-best-practices`, dateModified 2026-09-28): "Your products need to be in stock to be the featured offer and eligible for advertising."
- *How to improve your product detail page for advertising* (library guide at `/library/guides/improve-your-products-for-advertising`, dateModified 2026-10-09): "Your products need to be in-stock in order to be the featured offer and be eligible for inclusion in a Sponsored Products campaign. If a product you are advertising goes out of stock, it will be automatically paused within your campaign."
- The product-ads guide: "Products must be in stock in order for the ad to serve".
- *Understand Featured Offer eligibility* (help GYVDGT5WNNW23LJ5, lastModified 2026-10-16), written for "a seller or vendor": "Failing to hold the Featured Offer directly prevents Sponsored Products and Sponsored Display ads from serving impressions, regardless of campaign status shown in the campaign manager." "Sponsored Products and Display campaigns generate 0 impressions when the advertised ASIN or SKU doesn't hold the Featured Offer, even when the campaign shows "Delivering" status in Amazon Ads Agent. Sponsored Brands campaigns, including Sponsored Brands video, aren't affected and continue to serve even when another seller holds the Featured Offer, as long as the advertised product is available to buy on Amazon." "When multiple SKUs exist for 1 ASIN, only the SKU that holds the Featured Offer is eligible to serve ads." "When status shifts, impressions for the previous holder stop immediately."

[official] FAQ; the two library guides; `guides/sponsored-products/product-ads.md`; help GYVDGT5WNNW23LJ5.

**D2. GUIDANCE: where a vendor reads stock.** *How to improve your product detail page for advertising* (dateModified 2026-10-09): "You can monitor your inventory under "Manage inventory" in Seller Central, or within the Inventory Dashboard in Vendor Central." For the Featured Offer it says only: "You can refer to your business reports to see how often your products are the featured offer." The seller-only line is on *Guide to Sponsored Products for new advertisers* (`/library/guides/new-advertiser-success-guide`, dateModified 2026-10-09): "make sure you're winning the featured offer at the highest rate-ideally 90% or higher. If you are a seller, you can check your featured offer rate under the 'Reports' tab in Seller Central." [official] both guides. Neither page names a vendor "featured offer rate" report. The nearest vendor fields are `lostFeaturedOffer` and the glance-view definitions in G4.

**D3. RULE: a book vendor's and an author's ads need Amazon to be the Featured Offer; a seller's need its own offer.** *Sponsored Products eligibility requirements* (GMJYF5GN8RNYB6HD, lastModified 2026-10-20) says:

- the advertiser must be a "Professional seller, vendor, or author";
- "Sponsored Products ads created through your author ads account will only be shown to shoppers when Amazon itself (not a third-party seller) is the Featured Offer for your book. If you're selling books through a Seller Central account, use your seller ads account... your offer will only be eligible to be shown to shoppers if your offer is the Featured Offer."
- vendors can advertise audiobooks in AU, CA, FR, DE, IT, JP, ES, UK and US;
- virtual bundles are not compatible, and only child variations are eligible.

[official].

This page states the retail-account and seller-account split for books only. For any category, *Understand Featured Offer eligibility* (D1) states the rule per advertised ASIN or SKU: SP and Display serve 0 impressions when "the advertised ASIN or SKU doesn't hold the Featured Offer", and Sponsored Brands keeps serving while the product is buyable. The 2017 agency toolkit (D5) stated the vendor rule as "The advertiser / vendor must be winning the buy box for this unit to serve."

**D4. RULE (Japan): SB serves without the Featured Offer; SP and SD do not.** Amazon's Japanese seller advertising page:

- "スポンサープロダクト広告とスポンサー広告によるディスプレイ広告を利用するには、商品がおすすめ出品への掲載対象であることが必要です" (to use Sponsored Products and Sponsored Display, the product must be eligible for the Featured Offer);
- "スポンサーブランド広告は、広告主様の商品がおすすめ出品になっていなくても、広告がAmazonで買い物をしているお客様に表示されます" (Sponsored Brands ads are shown to shoppers even if the advertiser's product is not the Featured Offer);
- "おすすめ出品への掲載対象ではない商品の広告を作成した場合、その広告はAmazonで買い物をしているお客様に表示されません" (an ad created for a product not eligible for the Featured Offer is not shown).

[official] *Amazon 広告* on sell.amazon.co.jp, https://sell.amazon.co.jp/grow/advertising. The page is written for sellers.

**D5. RULE (2017, historical): the AMS agency toolkit's vendor eligibility rules.** The *Amazon Marketing Services Agency Toolkit: A Reference Guide for Agency Partners* PDF (54 pages; its title page reads "August 2017", the file was created 2017-08-01, and its naming example is "2017Q3") was written when "Amazon Marketing Services is limited to Amazon vendors only." It states:

- "ASINs must meet retail financial thresholds to be eligible for promotion through Amazon Marketing Services. Please work with your Agency Contact to ensure this requirement is met."
- "If the ASINs are not in stock, they will not be eligible for AMS promotion."
- Sponsored Products: "The advertiser / vendor must be winning the buy box for this unit to serve." "If the advertiser loses the buy box mid-flight for a certain ASIN, then the ad promoting that particular ASIN will pause, but the Sponsored Products campaign will continue to run if the campaign is promoting at least one other ASIN that is winning the buy box." Out-of-stock ASINs pause the same way, and "Ads will unpause automatically mid-flight when the ASIN is back in stock."
- Headline Search Ads (today's Sponsored Brands): "if fewer than three ASINs are eligible on the Headline Search Ads custom landing page, the campaign will pause and campaign status will show "Landing page not available." At least three ASINs must be in stock and at least one ASIN must meet the financial threshold criteria." "Unlike Sponsored Products, a Headline Search Ads campaign will continue to serve even if the advertiser / vendor is losing the buy box." An out-of-stock ASIN in the creative "will be automatically removed from the creative".
- Product Display Ads (a predecessor of Sponsored Display): "Unlike Sponsored Products, a Product Display Ads campaign will continue to serve even if the advertiser / vendor is losing the buy box."
- "Note: Amazon Third-Party sellers do have access to Sponsored Products via Seller Central and may bid on keywords to serve ads in the same placements as Amazon vendors."
- Guidance: "Select ASINs that frequently win the Buy Box." "Advertise more than 3 products per campaign to avoid being paused due to ineligibility or in-stock issues." "work with your vendor manager to maintain healthy in-stock rates and establish pricing that can profitably and consistently win the buy-box."

[official, dated] https://m.media-amazon.com/images/G/01/AmazonMarketingServices/Agency_Toolkit.pdf. These are Amazon's own words from August 2017. With the 2017 promotions guide (E4) they are the only Amazon text read today that uses "financial thresholds". No current Amazon page read today repeats them, and they are recorded as history. The current US help page (D1) contradicts the toolkit's Product Display line for today's Display ads: Display serves 0 impressions without the Featured Offer.

**D6. RULE: the eligibility statuses that map onto these gates.** The Eligibility API's status enum (B7) has a value for each gate the toolkit names: `NOT_IN_BUYBOX` (Featured Offer), `OUT_OF_STOCK` (stock) and `INELIGIBLE_PRODUCT_COST` (cost). The serving-reason enum (B8) has `CP_INELIGIBLE_VENDOR`. [official] *Eligibility* OpenAPI; SP 3.0 model. Amazon gives `INELIGIBLE_PRODUCT_COST` no description in the model read today. Whether it is the current form of the toolkit's "financial thresholds" is open question 1.

**D7. GUIDANCE: e-learning for vendors whose products are ineligible.** *Troubleshoot your products for eligibility* (GGBXM3YUBQFEX6YH, lastModified 2025-07-09) points vendors to the "Fix your products" e-learning. [official].

### E. Net PPM and CRaP as Amazon's own fields describe them

**E1. RULE: the Net PPM report.** `GET_VENDOR_NET_PURE_PRODUCT_MARGIN_REPORT`:

- the Analytics Reports page: "Contains data on Amazon's net pure product margins for selling a vendor's items", at catalog level and per ASIN, for DAY, WEEK, MONTH, QUARTER and YEAR. The only option is `reportPeriod`. Availability "Vendors". Role "Brand Analytics". The data is in Pacific time. The SLA is 48 hours after a week closes and 72 hours after a non-Saturday day closes;
- the schema: "The Net Pure Product Margin report shares data with vendors on Amazon's profit margin selling the vendor's items". `netPureProductMargin` is "A measure of Amazon's profitability considering Amazon's wholesale cost and vendor-funded cooperative marketing funds: (Product Revenue – Product COGS – Vendor Funded Coop) / Product Revenue. The value is a fraction with values between 0 and 1. To represent as a percentage, multiply the value by 100."

[official] *Analytics Reports* (updatedAt 2026-10-28), https://developer-docs.amazon/sp-api/docs/report-type-values-analytics.md; `vendorNetPureProductMarginReport.json`, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/reports/vendorNetPureProductMarginReport.json.

**E2. RULE: the Data Kiosk Net PPM definition.** The Data Kiosk vendor schema: "Net Pure Product Margin (PPM) is defined as Amazon's margin after taking into account CCOGs and sales discounts. Net PPM = (Shipped Revenue - Shipped CCOGS + CCOGS - Sales Discount) / Shipped Revenue." [official] `analytics_vendorAnalytics_2024_09_30.graphql`.

The two definitions are worded differently. The report schema subtracts "Vendor Funded Coop" from revenue minus COGS. The Data Kiosk formula adds "CCOGS" (contra-COGS) and subtracts a sales discount. They are recorded as two Amazon wordings (open question 3).

**E3. RULE: the cost components.** From the same schema:

- `shippedCogs`: "The shipped cost of goods sold (COGS), which is the price Amazon paid to a vendor for item procurement, and is a component of contribution profit."
- `contraCogs`: "The total Contra Cost of Goods Sold (COGS), equal to the dollars realized by customer outbound shipments minus Display Ads Contra COGS."
- `contraCogsPerUnit`: "The average Vendor Funded Contra-COGS (VFCC) of shipped items."
- `salesDiscount`: "Sales Discount is a transactional component of CP (Contribution Profit Amount) related to promotional activities that Amazon conducts at checkout, such as promotion code redemptions, giftcard promotions, employee discount, etc."
- `averageSalesDiscount`: "The average selling discount per unit of shipped items."

[official] Data Kiosk vendor schema.

The phrase "minus Display Ads Contra COGS" is the only place in Amazon's text read today where advertising appears inside a margin component. It is not explained. Practitioners say ad spend is outside Net PPM (*What practitioners add*). The two readings are open question 4.

**E4. RULE (dated): pass-through and financial thresholds in the 2017 promotions guide.** *Amazon Promotions: Vendor Self-Service Program* (March 2017) says:

- "Amazon sets prices independently. We generally aim to pass promotional funding amounts on to customers".
- "Amazon may choose not to pass on the funding amount if your product does not meet financial thresholds".

[official, dated] https://m.media-amazon.com/images/G/01/boost/assets/2017/Amazon_Promotions_How-to_March2017._V528747406_.pdf.

**E5. [press] What Amazon told vendors in 2019.** CNBC (Eugene Kim, 2019-03-20, updated 2019-04-01) reported vendor emails reading "One or more of your products no longer qualifies for advertising", because "the sale of this product on Amazon.com currently results in a loss to Amazon", and advising vendors to "lower the product's cost". It also quoted an Amazon spokesperson: "Like all retailers, Amazon decides which products to market and promote in our stores". CNBC glossed CRaP as "Can't Realize a Profit", typically items under $25, or up to $2,000 if bulky. https://www.cnbc.com/2019/03/20/amazon-aggressively-suspending-ads-of-unprofitable-products-as-focus-on-the-bottom-line-grows.html. The quoted email text is Amazon's, but this seat read it only as CNBC's report.

No Amazon page read today uses the word "CRaP". The nearest Amazon text is the undescribed `INELIGIBLE_PRODUCT_COST` status (D6) and the 2017 "financial thresholds" (D5, E4).

### F. Availability is set by Amazon's purchase orders

**F1. RULE: Amazon buys, and the vendor confirms.** The *Vendor Retail Procurement Orders API* (developer-docs, updated 2026-09-09; Availability "Vendors only"; roles Amazon Fulfillment or Inventory and Order Tracking) has four operations:

- `GET /vendor/orders/v1/purchaseOrders` (getPurchaseOrders);
- `GET /vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}` (getPurchaseOrder);
- `POST /vendor/orders/v1/acknowledgements` (submitAcknowledgement);
- `GET /vendor/orders/v1/purchaseOrdersStatus` (getPurchaseOrdersStatus).

The model defines:

- `purchaseOrderType`: RegularOrder, ConsignedOrder, NewProductIntroduction, RushOrder;
- `purchaseOrderState` on the order: New, Acknowledged, Closed; `purchaseOrderStatus` on the status call: OPEN, CLOSED; per-item `confirmationStatus` (ACCEPTED, PARTIALLY_ACCEPTED, REJECTED, UNCONFIRMED) and `receiveStatus` (NOT_RECEIVED, PARTIALLY_RECEIVED, RECEIVED);
- `purchaseOrderChangedDate`: "The date when purchase order was last changed by Amazon after the order was placed... vendors are required to fulfill the updated PO";
- `acknowledgementCode`: Accepted, Backordered, Rejected;
- `rejectionReason`: TemporarilyUnavailable, InvalidProductIdentifier, ObsoleteProduct;
- `isBackOrderAllowed`: "When true, we will accept backorder confirmations for this item";
- `dealCode`: "If requested by the recipient, this field will contain a promotional/deal number. The discount code line is optional. It is used to obtain a price discount on items on the order";
- `netCost` and `listPrice` per item, and `shipWindow` and `deliveryWindow` per order.

[official] https://developer-docs.amazon/sp-api/docs/vendor-retail-procurement-orders-api.md; `vendorOrders.json`, https://github.com/amzn/selling-partner-api-models/blob/main/models/vendor-orders-api-model/vendorOrders.json.

**F2. RULE: Amazon's buying systems choose quantity and supplier.** Amazon Science: "Buying systems determine the right level of product to purchase from different suppliers, while large-scale placement systems determine the optimal location for products across the hundreds of facilities belonging to Amazon's global fulfillment network." Also: "lead times from vendors are subject to natural variation due to manufacturing capacity, transportation times, weather, etc." [official] *The evolution of Amazon's inventory planning system* (Amazon Science, staff writer, published 2021-10-01, modified 2021-12-06), https://www.amazon.science/latest-news/the-evolution-of-amazons-inventory-planning-system.

**F3. RULE: the inventory report's supply-side fields.** `GET_VENDOR_INVENTORY_REPORT`: "Contains inventory and operational health metrics such as sellable on hand units and vendor confirmation rate". `distributorView` (MANUFACTURING or SOURCING), `sellingProgram` (RETAIL or FRESH) and `reportPeriod` are all required. "Refreshed data is available 72 hours after the close of the period. For example, weekly data (Sunday through Saturday dataset) is available by the end of the day Tuesday." The schema defines:

- `procurableProductOutOfStockRate`: "The out of stock rate on all products that are procurable. This is calculated by out of stock glance views on a procurable ASIN divided by the total glance views."
- `uft`: "The percentage of time an ASIN is available to be shipped to the customer from a fulfillment center, versus the selection Amazon intended to carry."
- `receiveFillRate`: "The purchase order units received by Amazon in comparison to the purchase order units confirmed by the vendor."
- `vendorConfirmationRate`: "The number of units that were confirmed by the vendor, divided by the number of units Amazon asked for... This rate can be larger than 1 if the vendor has confirmed a greater quantity of units than Amazon requested."
- `openPurchaseOrderUnits`: "Number of units contained in Amazon's confirmed purchase orders that are not yet received by Amazon."
- `averageVendorLeadTimeDays`: "Average number of days between the submission of each purchase order unit and the time of receipt in Amazon's fulfillment centers."
- `unfilledCustomerOrderedUnits`: "The number of units that have been ordered (or pre-ordered) but have not yet shipped."
- `sellableOnHandInventoryUnits`: "...in a sellable condition on the last day of the selected time window. Backorders count as negative units, and can cause this value to be negative overall."
- `sellThroughRate`, net received inventory, aged-90-plus and unhealthy inventory ("the amount of inventory beyond the forecasted demand").

[official] *Analytics Reports*; `vendorInventoryReport.json`.

**F4. RULE: the Data Kiosk supply fields, with Amazon's definitions of procurability.** From the vendor schema:

- `procurableProductOOS`: "OOS (Out of Stock) rate on all products that are procurable. Retail Out of Stock (ROOS) = Out of Stock Glance Views on Procurable ASINs / Total Glance Views. Procurability refers to whether Amazon is able to fulfill a customer delivery promise, considering the ability of known vendors to supply the ASIN in the foreseeable future."
- `sourceableROOS`: "The sourceable replenishment out of stock percentage, which is the percentage of retail that is available for all ASINs with a sourceable retail vendor."
- `ultraFastTrack`: "an hourly measure of the percentage of time an ASIN is available to be shipped to the customer from an FC via Prime shipping, versus the selection Amazon intended to carry. This metric takes into account a Customer Importance Factor (CIF)".
- `openPurchaseOrderQuantity`: "Number of units included in the Vendor's open POs (i.e., confirmed PO quantities that are not yet received)."
- `confirmedUnits`: "Number of purchase order units that are confirmed to be shipped to Amazon."
- `mostRecentSubmitted`: "The number of units Amazon has ordered in the most recent purchase orders of the week."
- `overallVendorLeadTime`: "Time (in days) from when Vendor receives a PO from Amazon, to when inventory is received in a FC."
- `receivedFillRate`: "Fill Rate = Net Received Units / Confirmed Units", "applies only to Procurable ASINs".
- `vendorConfirmationRate`: "Vendor Confirmation Rate = Confirmed Units / Submitted Units".
- `replenishmentCategory`: "Availability status for the ASIN." It is a free string with no enum.
- `unfilledOrderedUnits`: "Number of units ordered (or pre-ordered), but have not shipped."

[official] `analytics_vendorAnalytics_2024_09_30.graphql`.

**F5. RULE: the forecast Amazon buys against.** `GET_VENDOR_FORECASTING_REPORT`:

- "Contains forward looking mean, Prior 70, Prior 80, and Prior 90 weekly customer demand forecasts", at ASIN level, "for the most recent weekly forecast generation date";
- "Only the most recent forecast data is available. Historical forecast data cannot be requested.";
- one store per request;
- "Refreshed forecasting data is available within a 72-hour time frame after the week end";
- the schema's `p80ForecastUnits`: "Amazon has forecasted an 80% probability that the ASIN will not run out of stock during the date range if this many units of inventory are present at the start of the date range"; the Analytics page words P80 differently: "there is an 80% probability customer demand will not exceed the weekly forecasted units";
- `sellingProgram` RETAIL or FRESH;
- the Data Kiosk forecasting domain runs "from Week zero to Week 47".

[official] *Analytics Reports*; `vendorForecastingReport.json`; *Vendor Analytics Dataset Use Case Guide*.

**F6. RULE: the hourly stock signal.** `GET_VENDOR_REAL_TIME_INVENTORY_REPORT`:

- inventory "aggregated to an hourly granularity", with the field `highlyAvailableInventory`;
- "ASINs are included if the number of units available for purchase by customers has changed. In addition to orders and cancellations, other activities which could impact the number of units available for purchase include add-to-cart actions, processed Subscribe-and-Save orders, and new quantities being made available."
- "information can be requested five minutes after the close of each hour";
- lookback 30 days; maximum span 7 days;
- "Available to sellers and vendors as the `ITEM_INVENTORY_EVENT_CHANGE` notification."

[official] *Analytics Reports*.

**F7. RULE: what Amazon does to SP when stock runs out.** "If a product you are advertising goes out of stock, it will be automatically paused within your campaign." (D1, *How to improve your product detail page for advertising*). The 2017 toolkit says the same, and that the ad unpauses automatically (D5). [official]. Neither page says the same of SB or SD. The current Featured Offer page keeps SB serving "as long as the advertised product is available to buy on Amazon" (D1). The 2017 toolkit says an out-of-stock ASIN is removed from a Headline Search creative, and that the campaign pauses when fewer than three ASINs on its landing page are eligible.

### G. The vendor's total-sales side: Vendor Retail Analytics and the two views

`areas/ads-organic-and-total.md` D8 to D11 and P-ads-organic-and-total-21 to 23 state the Vendor Sales report's fields, the Pacific-time rule and AMC's Manufacturing match. This section adds what those leave open: what each view contains, which roles open which view, the traffic definition, the rapid reports, and the dataset that replaces the reports for some uses.

**G1. RULE: the Sales report's required options and the two views.** `GET_VENDOR_SALES_REPORT`:

- "Contains key retail sales metrics such as ordered/shipped revenue and units", at catalog level and per ASIN;
- "Requests must include the `reportPeriod`, `distributorView`, and `sellingProgram` properties";
- `distributorView` takes MANUFACTURING or SOURCING, and `sellingProgram` takes RETAIL, BUSINESS or FRESH;
- the page's note: "`distributorView: MANUFACTURING` provides data for ASINs of items manufactured by you, regardless of who sourced the products to Amazon. `distributorView: SOURCING` provides data for ASINs of items sourced directly from your vendor group."
- tip: "Average sale price = shipped revenue / shipped units".

[official] *Analytics Reports* (updatedAt 2026-10-28).

**G2. RULE: ordered figures exist only in the manufacturing view.** The schema:

- `orderedRevenue`: "Ordered product sales in the selected time frame. Adjustments are made for returns. This field is populated when distributorView is MANUFACTURING."
- `orderedUnits`: "Number of units ordered by Amazon customers. This field is populated when distributorView is MANUFACTURING."
- `shippedRevenue`: "Revenue based on units shipped in the selected time frame. Adjustments are made for returns."
- `shippedCogs`: "Revenue based on the cost of goods sold. Adjustments are made for returns."
- `shippedUnits`: "Number of units shipped to Amazon customers."
- `customerReturns`: "populated when sellingProgram is RETAIL or BUSINESS."
- `marketplaceIds`: "must match the marketplaceId of the selling partner account. Each selling partner account belongs to only one marketplaceId."

[official] `vendorSalesReport.json`, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/reports/vendorSalesReport.json.

**G3. RULE: windows, spans, the SLA and the FATAL rule.**

| `reportPeriod` | Lookback | Maximum span |
|---|---|---|
| DAY | 1,460 days | 15 days |
| WEEK | 7 weeks | 7 weeks |
| MONTH | 36 months | 15 months |
| QUARTER | 8 quarters | 4 quarters |
| YEAR | 3 years | 2 years |

- A WEEK request runs Sunday to Saturday.
- SLA: "for weekly reporting periods (for example, Saturday datasets) is the end of the day Monday, 48 hours after the close of the period. The SLA for non-Saturday daily reporting periods is 72 hours after the close of the period."
- "If you request a report for a reporting period that is not yet available, the report will not be generated and `processingStatus` for the report will be FATAL."

[official] *Analytics Reports*. The figures are for readers only.

**G4. RULE: glance views count only while Amazon retail holds the Featured Offer.**

- The rapid traffic report: "The report payload includes ASINs whose product detail page received glance views during that period where a given merchant is the featured offer, including when multiple offers for the same merchant are shown (for example, Subscribe and Save, used products, buy on Fresh). Glance Views (GVs) are calculated at the ASIN-level, and only when retail is the featured merchant."
- The Data Kiosk `glanceViews`: "Glance views where Retail is the featured offer (i.e., winning the buy box)."
- `lostFeaturedOffer`: "The percentage of product page views where your offer loses the Featured Offer position (Buy Box) to others. It is equal to the number of glance views where you do not win the Featured Offer divided by the total number of glance views."
- The weekly traffic schema gives only "Customer views of the vendor's product detail pages."

[official] *Analytics Reports*; Data Kiosk vendor schema; `vendorTrafficReport.json`.

**G5. RULE: the rapid traffic count is not the dashboard count.** "The Glance Views count in the `GET_VENDOR_REAL_TIME_TRAFFIC_REPORT` is not the same as the Glance Views count in the Vendor Central dashboard. They use different count systems based on their different time requirements. The `GET_VENDOR_REAL_TIME_TRAFFIC_REPORT` outputs data as close to real-time as possible, but is less accurate than the Vendor Central dashboard for concluded days." Traffic arrives "approximately 65 to 115 minutes after the close of an hour". Lookback is 30 days and the span 14 days. It is also "Available to sellers and vendors as the `DETAIL_PAGE_TRAFFIC_EVENT` notification." [official] *Analytics Reports*.

**G6. RULE: the rapid sales report.** `GET_VENDOR_REAL_TIME_SALES_REPORT`:

- hourly `orderedUnits` and `orderedRevenue`; "ASINs are included when they have orders or cancellations during a given hour";
- available "five minutes after the close of each hour"; lookback 30 days, span 14 days;
- "Rapid retail analytics represents cancellations based on the time of the cancellation. To represent cancellations, ordered units may be negative for a given hour and ASIN combination."
- tip: "Conversion = ordered units / glance views";
- also available "to sellers and vendors as the `ITEM_SALES_EVENT_CHANGE` notification."

[official] *Analytics Reports*.

**G7. RULE: the Data Kiosk vendor dataset and role-gated views.** The *Vendor Analytics Dataset Use Case Guide* (updatedAt 2026-09-30):

- "The `analytics_vendorAnalytics_2024_09_30` dataset has a `sourcingView` and `manufacturingView`. You access the relevant view and its associated metrics based on the role assigned to the vendor (`SOURCING` or `MANUFACTURING`)."
- "**Manufacturing** refers to any ASINs manufactured by the vendor, whereas **Sourcing** refers only to ASINs sourced directly from the vendor to Amazon (meaning the vendor is a distributor)."
- "Certain metrics such as Glance Views are not available in `sourcingView`, and that `sourcingView` is the same as distributor view."
- "If a vendor (Vendor Group) does not manufacture any ASINs, then the query for accessing manufacturing view for the vendor returns `Error: VendorGroup does not have relevant rights to perform this operation`."
- The sourcing view's metric groups: ProductAvailability, ShippedOrders, CustomerSatisfaction, Sourcing and Costs (`netPPM`, `salesDiscount`, `shippedCogs`, `contraCogs`, `contraCogsPerUnit`, `averageSalesDiscount`). The manufacturing view adds Orders (`orderedUnitsWithRevenue`, `unfilledOrderedUnits`, `netOrderedGMS`, `netShipmentGMS`), Traffic (`glanceViews`, `lostFeaturedOffer`) and Forecasting.
- "The `vendorCode` group-by field is not compatible with" `orderedUnitsWithRevenue`, `netOrderedGMS`, `netShipmentGMS`, `glanceViews`, forecasting and `lostFeaturedOffer`; and "In the **manufacturing view**, the following metrics are disabled when you select the `vendorCode` group-by field", among them `vendorConfirmationRate`, `overallVendorLeadTime`, `receivedFillRate`, `procurableProductOOS` and `openPurchaseOrderQuantity`.
- Supported periods: "**Weekly:** Eight weeks... **Monthly:** 24 Months". Daily is "Only supported for the current common date".
- "Catalog attributes (for example, ASINs and product titles) are always current and latest. There is no historical view of catalog data."
- "Partial data availability... occurs when data is requested within one to two business days. In such cases, the response for days that are unavailable contains a null value."

[official] https://developer-docs.amazon/sp-api/docs/vendor-analytics-dataset-guide.md.

**G8. RULE: the revenue definitions inside the dataset.**

- `orderedUnitsWithRevenue`: "The number of ordered units and the associated revenue in a given time period with adjustments made for prior sales, like returns/cancellations... Ordered Revenue Amount (OPS) = Product Price * Ordered Units."
- `shippedUnitsWithRevenue`: "Shipped Revenue Amount = Gross Price (the price the customer sees in the cart) * Shipped Units."
- `averageSellingPrice`: "excluding sales tax or value-added taxes".
- `netOrderedGMS`: "The net Gross Merchandise Sales (GMS) for all orders on a given day." `netShipmentGMS`: "The net shipped Gross Merchandise Sales (GMS) amount."
- `msrp`: "The manufacturer's suggested retail price (MSRP) of the item. Also known as the list price."

[official] Data Kiosk vendor schema.

**G9. RULE: AMC's retail purchases match the manufacturing view.** The AMC Amazon Retail Purchases guide: "For **Vendor Central** accounts, the scope of data in ARP will match with what is shown in the Vendor Central under **Reports > Retail Analytics > Sales > Distributor View = Manufacturing**". The paid-features overview says the same. The guide also advises: "Check the Sponsored Ads accounts configured to your AMC instance configuration to ensure the correct Vendor/Seller Central accounts are associated." [official] `guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid.md`; `guides/amazon-marketing-cloud/datasources/paid_features_overview.md`. This is P-ads-organic-and-total-23.

**G10. RULE: Amazon names no denominator for vendor TACoS.** No Amazon page read today defines TACoS for a vendor, or says which view or which revenue (ordered, shipped, or shipped COGS) is the total-sales side. Amazon's TACoS wording is the seller-side "organic and paid" of P-ads-organic-and-total-6. Amazon's own pages fix these facts:

- the vendor's SP attributed sales are retail-price sales of products sold by Amazon over 14 days (C1, C5);
- ordered revenue exists only in the manufacturing view (G2);
- the manufacturing view includes ASINs "regardless of who sourced the products to Amazon" (G1), and so includes units Amazon bought from distributors;
- the sourcing view covers only the vendor group's own supply, and has no glance views (G7);
- none of the views includes the brand's own 3P sales.

[official] as cited. Practitioner choices are in *What practitioners add*.

**G11. RULE: Rapid retail analytics as Amazon Ads markets it.** The Amazon Ads product page *Rapid retail analytics* says:

- access is through SP-API reports and notifications;
- it "can be used by advertisers of any size, both sellers and vendors";
- its use cases include hourly dayparting, budget, and "increasing Amazon Ads bids by ASIN-level during hours";
- the metrics are ordered units and revenue, glance views and highly available inventory;
- it cites Acorn-i (2023) and DemandHelm (2023) as sources.

[official] *Rapid retail analytics - Understand, measure, and optimize your ad campaigns at the product level*, https://advertising.amazon.com/measurement-analytics/rapid-retail-analytics. Its access answer reads: "Rapid retail analytics can be accessed through the Selling Partner API for both reports and notifications." Some of the page's category descriptions render garbled. The SP-API page gives each of the three reports Availability "Vendors", while the matching notifications are "Available to sellers and vendors". The two pages agree only if "both sellers and vendors" refers to the notifications (open question 5).

### H. Brand Analytics for vendors

**H1. RULE: no Search Query Performance or Search Catalog Performance for vendors.** The SP-API Analytics page gives `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` the Availability "Sellers who have the Brand Analytics Selling Partner API role and are registered in Amazon Brand Registry". Search Catalog Performance carries the same "Sellers" line. [official] *Analytics Reports* (updatedAt 2026-10-28).

**H2. RULE: Repeat Purchase, Market Basket and Search Terms are open to vendors with Brand Registry.** `GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT`:

- Availability "Sellers and vendors who have the Brand Analytics Selling Partner API role and are registered in Amazon Brand Registry";
- 18 stores: US, MX, CA, BR, ES, UK, FR, NL, DE, IT, SE, TR, SA, AE, IN, SG, AU and JP;
- periods WEEK, MONTH and QUARTER;
- the schema fields `orders`, `uniqueCustomers`, `repeatCustomersPctTotal`, `repeatPurchaseRevenue` ("Returns are not reflected") and `repeatPurchaseRevenuePctTotal`.

The Market Basket report carries the same sellers-and-vendors line. The Search Terms report's line adds a condition: "Sellers and vendors who have the Brand Analytics Selling Partner API role, are registered in Amazon Brand Registry, and are a brand representative." Every vendor retail analytics report on the page (Sales, Net PPM, Traffic, Forecasting, Inventory and the three rapid reports) also names the Brand Analytics role. [official] *Analytics Reports* (the page at `report-type-values-analytics.md`); `sellingPartnerRepeatPurchaseReport.json`.

**H3. RULE: the vendor use-case directory agrees.** *SP-API Vendor Use Cases* (2026-10-05) lists, for vendors:

- a Brand Analytics row with Market Basket, Search Terms and Repeat Purchase only;
- a Performance row with the promotion and coupon reports;
- the retail-analytics reports and the three notifications (`DETAIL_PAGE_TRAFFIC_EVENT`, `ITEM_INVENTORY_EVENT_CHANGE`, `ITEM_SALES_EVENT_CHANGE`);
- the vendor retail procurement APIs.

[official] https://developer-docs.amazon/sp-api/docs/sp-api-vendor-use-cases.md.

[seat] For a vendor, the query-level funnel that sellers read in SQP (impressions, clicks, cart adds, purchases per query for the brand) has no SP-API source in Amazon's text read today. The query-level sources left are the Ads API search-term report, which covers ad traffic only, and the Brand Analytics Search Terms report, whose fields this seat did not re-read today. For a hybrid brand, SQP is available only through the seller account, and only for what that account sells.

### I. Vendor-funded promotions: types, funding, reporting and lead times

**I1. RULE: the promotion performance report covers vendor-funded promotions.** The `promotionReport` schema:

- "The Promotion Performance report contains data to help vendors optimize their promotions and adjust their advertising strategies. Currently three promotion types are supported: Best Deal, Lightning Deal, and Price Discount. This report supports start dates up to two years before the current date."
- The `type` enum is wider than that sentence: BEST_DEAL, DEAL_OF_THE_DAY, LIGHTNING_DEAL, PRICE_DISCOUNT, SALES_DISCOUNT, COUPON, PROMO_CODE.
- `status`: APPROVED, PENDING_APPROVAL, NEEDS_YOUR_ATTENTION, CANCELED.
- `creationChannel`: SELF-SERVICE ("Created by the vendor/seller directly in Vendor/Seller Central"), FULL-SERVICE ("Created on behalf of the vendor/seller by account managers"), AUTOMATED ("Created automatically by a system in response to a trigger. For example, Deal-O-Matic."), and MANUAL ("Only used for digital point-of-sale discounts created in Vendisto").
- `vendorCode`: "associated with the promotion funding agreement. For vendors only."
- `fundingAgreementId`: "The ID for the funding agreement. For vendors only."
- `amountSpent`: "Total funding provided across all ASINs in the promotion. For vendors only." `productAmountSpent` is "Total funding provided by the vendor at the ASIN level".
- `glanceViews` and `productGlanceViews`; `unitsSold`, and `productUnitsSold` ("units sold at the promotional price").
- `revenue`: "For sellers, this is equivalent to "sales" in the Seller Central UI."
- `promotionsApiMappingId`: "Unique identifier to cross-reference promotions with the Selling Partner Promotions API."
- Times are ISO 8601 in UTC.

[official] `promotionReport.json`, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/reports/.

**I2. RULE: the vendor coupon report.** The `vendorCouponReport` schema:

- "This report contains data to help vendors optimize their coupons and adjust their advertising strategies. This report supports start dates up to two years before the current date."
- Campaign-level fields include `vendorCode`, `isSubscribeAndSave`, and `budgetType` (PER_INDIVIDUAL_COUPON or SHARED_BUDGET).
- `totalBudgetSpent`: "Total amount spent by the vendor on the campaign, including clip fees and redemption fees".
- Per coupon: `clips`; `redemptions` ("Represents a gross value, including purchases that were returned or cancelled"); `totalDiscount`; `budgetSpent` ("including clip fees and redemption fees"); `customerSegment`; `isOncePerCustomer`; and `discountType` (PERCENT_OFF_LIST_PRICE or AMOUNT_OFF_LIST_PRICE).
- `lastUpdatedDateTime` "May be up to 24 hours before the current date-time."
- Times are in UTC.

[official] `vendorCouponReport.json`.

[seat] The promotion and coupon reports are in UTC. The vendor retail analytics are in Pacific time (G). The ad reports are in the profile's time zone (`areas/ads-organic-and-total.md`). A day-level join of the three needs an explicit conversion.

**I3. RULE: the SP-API Promotions API is for sellers.** The *Promotions API* page (updated 2026-09-09) gives Availability "Sellers", with the Pricing or Product Listing role. The 2025-12-01 model's types are BASKET_BUILDING, DEAL, PRICE_DISCOUNT and COUPON, with coupon subtypes STANDARD, SUBSCRIBE_AND_SAVE and REORDER_REWARDS. [official] https://developer-docs.amazon/sp-api/docs/promotions-api.md; `promotions_2025-12-01.json`. A vendor's promotions are read through the two reports in I1 and I2, not through this API.

**I4. RULE (dated, March 2017): the vendor self-service promotion types and lead times.** *Amazon Promotions: Vendor Self-Service Program* lists four types. Its comparison chart:

| Type | Duration | Submit by | Minimum discount |
|---|---|---|---|
| Price Discount | up to 12 months | at least 24 hours ahead | any discount |
| Best Deal | up to 2 weeks | 4 or more weeks ahead | at least 10% |
| Lightning Deal | up to 6 hours | 4 or more weeks ahead | at least 15%, with a maximum unit quantity |
| Promo Code | up to 30 days | at least 24 hours ahead | at least 15%, with a maximum unit quantity |

The guide also says:

- "*Amazon recommends submitting price discounts and promo codes at least 4 weeks in advance, or Amazon may not have time to buy inventory".
- "Min % off Amazon Retail Price may increase for events like Prime Day, Black Friday and Cyber Monday" (a note on the Best Deal and Lightning Deal minimums).
- "Amazon strives to review within seven days".
- "If approved, Amazon often buys more product to prepare for the promotion".
- Funding is either a reduced promotional cost on POs (Lightning Deals only) or pay per unit sold, billed through an "Amazon CoOp invoice".
- The maximum unit quantity works as a budget, and a Lightning Deal carries one product (variations allowed).
- "Promotions often make products show up higher in search results".

[official, dated 2017] https://m.media-amazon.com/images/G/01/boost/assets/2017/Amazon_Promotions_How-to_March2017._V528747406_.pdf. The figures are for readers. No current Vendor Central page could be read (*Unreachable*), so whether these lead times stand in 2026 is open question 6.

**I5. RULE (dated, August 2017): vendor-powered coupons in ads.**

- "Vendor-Powered Coupons is a self-service mechanism for Amazon vendors to directly upload promotions into Amazon systems."
- "Leverage Vendor Powered Coupons (VPCs). Product Display Ads are the only ad unit that supports VPCs. Inquire with your client whether VPCs are available for promotion. Please note Subscribe & Save (SNS) VPCs are not eligible."
- "Advertise limited-time deals - including Lightning Deals and Savings and Sales Deals - on Product Display Ads".
- "If an associated Vendor Powered Coupon (VPC) is no longer valid, then the ad will revert back to a normal, non-VPC associated Product Display Ad format."

[official, dated] AMS *Agency Toolkit*.

**I6. RULE: promotion signals that reach ad measurement.**

- AMC Amazon Retail Purchases: "Promotional signals reflect only vendor or seller self-funded promotions." Also: "A blank promotional field means no qualifying vendor or seller self-funded promotion was identified for that purchase — it does not mean the discount was zero." [official] `amazon_retail_purchase_paid.md`. The columns are P-seasons-and-deals-44.
- The MMM data feed carries "# of vendor powered coupons clipped nationally per promo. Includes: Promo ID and clips." [official] `guides/reporting/marketing-mix-modeling/mmm-data-feed.md`.
- The PO model carries `dealCode` (F1), so a promotion can appear on a purchase order.

**I7. RULE (seller-facing, 2026): the Prime Day 2026 deal deadlines as Amazon posted them for sellers.** An Amazon staff post, "Prime Day 2026: Your Deals Deadline Extended!" (Indy_Amazon, Seller Forums, posted 2026-05-26 by the page's timestamp), says:

- "The Prime Day Deal Sourcing Deadline has been extended to June 9th, 2026"; its key deadlines list "6/9/26 - Prime-Exclusive Best Deals & Lightning Deals";
- "PEDs can be submitted until 12 hours before the event end time", and coupons "Through the end of the event";
- inventory must be in the network or in transit;
- "Deals will be suppressed if ASINs are not buyable at event time."

[official] https://sellercentral.amazon.com/seller-forums/discussions/t/9412e643-a006-464d-824a-0121d07c1b63. The post does not mention vendors. Amazon publishes vendor deadlines in Vendor Central, which could not be read.

### J. Hybrid brands: two offers, two accounts, one ASIN

**J1. RULE: an ad serves only for its own advertiser's offer.**

- For sellers and books: "your offer will only be eligible to be shown to shoppers if your offer is the Featured Offer" (D3).
- For vendors' attribution: "Only products sold by Amazon are attributed" (C1).
- For eligibility: "Requests are permitted only for products sold by the merchant associated with the profile" (B7). The status enum carries NOT_IN_BUYBOX (B7).
- The 2017 toolkit: "The advertiser / vendor must be winning the buy box for this unit to serve" (D5).

[official] as cited.

- For any advertiser: SP and Display serve 0 impressions when "the advertised ASIN or SKU doesn't hold the Featured Offer"; "only the SKU that holds the Featured Offer is eligible to serve ads"; "When status shifts, impressions for the previous holder stop immediately" (D1).

[seat] On one ASIN with both an Amazon retail offer and the brand's own 3P offer, the Featured Offer goes to one of them at a time. On Amazon's words, only the ad whose advertiser holds it can serve SP or Display impressions, and the switch is immediate. How the other profile's SP ad on that ASIN reads in the Eligibility API (NOT_IN_BUYBOX or otherwise) while the other offer holds the Featured Offer is not stated. No Amazon page read today states the hybrid case in one sentence. The statement is assembled from the rules above.

**J2. RULE: Sponsored Brands does not need the Featured Offer.** The US help page *Understand Featured Offer eligibility* states it: SB, "including Sponsored Brands video, aren't affected and continue to serve even when another seller holds the Featured Offer, as long as the advertised product is available to buy on Amazon" (D1). Amazon's Japanese page (D4) and the 2017 toolkit (D5) say the same of SB and Headline Search. [official].

**J3. RULE: one advertising account per Vendor Central account.** "An advertising account can only be linked to 1 Vendor Central account." (A5) [official]. A hybrid brand therefore has at least two advertising profiles in a marketplace: the vendor profile and the seller profile. Their windows differ (7 against 14 days, C4), their product identifiers differ (SKU against ASIN, B3), and their name rules differ (B4).

**J4. RULE: a seller's SP and a brand's ads are attributed separately, unless one advertiser wins both.** See C2. [official].

**J5. Amazon staff and seller reports in the forums (not rules).**

- In a UK Seller Forums thread ("Request to Review Feature Offer Eligibility"), a seller wrote: "There are two United States ads accounts. One is associated with my seller account and one is associated with these rogue Vendor accounts." And: "The Vendor accounts are showing as the winner of the buy box/featured offer". This was given as the reason the seller could not run Sponsored Display. The Amazon reply (Josh_Amazon) said only: "Since the case is being worked by another team, unfortunately, I am unable to take any actions yet." https://sellercentral.amazon.co.uk/seller-forums/discussions/t/899a64fd-a0b2-49be-b27f-ac2b838ea0b8.
- In a US thread ("Missing Featured Offer for My Listing – Need Assistance!"), Danny_Amazon wrote: "The Featured Offer system is something that can't be guaranteed on a listing, even if it was held previously." https://sellercentral.amazon.com/seller-forums/discussions/t/a8943ddb-0e4f-4bd6-853b-bbdace1a41eb.

The pages show "2 years ago"; their embedded timestamps date the UK thread's posts from 2024-10-25 to 2024-11-08 and the US thread's from 2025-01-17 to 2025-01-27. The vendor sentence is a seller's claim, not Amazon's. The seller's account (no seller Sponsored Display while a vendor offer is featured) matches Amazon's current Featured Offer rule for Display (D1).

**J6. RULE: the retail offer's traffic is the only traffic a vendor sees.** Glance views "only when retail is the featured merchant" (G4). `lostFeaturedOffer` measures "glance views where you do not win the Featured Offer divided by the total number of glance views" (G4). [official].

[seat] For a hybrid ASIN, a rising `lostFeaturedOffer` on the vendor side can be the brand's own 3P offer taking the Featured Offer. Amazon's definition says "to others" and does not say who the others are.

### K. Paying for vendor ads

**K1. RULE: vendor payment methods.** *Payment methods (Sponsored ads)* (GMELNQQNEEVLX456, lastModified 2026-08-03) lists three for vendors:

- a debit or credit card: "Every time your account Cost (formerly known as Spend on sponsored ads) reaches the credit limit, the invoice is issued, the card is charged, and that billing cycle ends."
- Deduct from payment (DFP): "Advertising costs are automatically deducted from your Amazon retail proceeds. Deductions will be made from the account associated with your selected vendor code. If the amount due exceeds your available funds for the designated vendor code, your payment will fail."
- Invoice: "Receive a monthly invoice that you can pay via bank check or wire transfer. Your payment is due within 30 days".

The page adds: "If your payment method fails after multiple attempts, your advertising account will be placed into payment failure status and your campaigns will be paused. If you're updating your payment method due to a payment failure, it can take up to 24 hours for your account to be enabled." [official]. The method list is P-ad-products-and-eligibility-41.

**K2. RULE: DFP and invoicing limits.**

- The vendor guide: "DFP is not available to third parties who manage payments for their clients' advertising accounts, or to accounts that haven't experienced retail activity in the last 6 months."
- The FAQ: "Invoicing is also available for vendors on an invite-only basis."
- The 2017 toolkit: "Invoicing is an invite-only option limited to vendors that meet specific criteria, which varies per country."

[official] *Advertising solutions for Amazon vendors*; FAQ; AMS *Agency Toolkit*.

[seat] Under DFP, the cost of ads comes out of the money Amazon owes the vendor for its POs. A vendor whose POs stop (F) can therefore fail to pay under DFP, and the campaigns then pause (K1). No Amazon page links the two in one sentence.

### L. Amazon's own framing of retail-aware advertising for vendors

**L1. GUIDANCE (Amazon-hosted partner voice): Intentwise on SP-API and ads for vendors.** An Amazon Ads expert-advice article, *Increasing spend efficiency in the Amazon store with Intentwise* (datePublished 2023-03-03, by Gabriella Kursman, dateModified 2026-10-09), interviews Sreenath Reddy, CEO of Intentwise, about using the Ads API and SP-API "to increase spend efficiency for vendors in the Amazon store". Reddy names:

- "retail-aware ad optimization";
- "inventory-aware advertising management—that is, automatically pausing or reducing advertising spend on ASINs if inventory levels are getting low";
- an item profitability view combining "the sales and traffic business reports from Seller Central and Vendor Central" with advertising reports;
- "Pulling back on media spend for products that are running low on inventory";
- "Correlating Best Sellers Rank (BSR) changes with ad spend".

[opinion, hosted by Amazon] https://advertising.amazon.com/library/expert-advice/how-to-increase-ad-spend-efficiency-intentwise. The words are the partner's, not Amazon's rules.

**L2. GUIDANCE: the same use cases on the Rapid retail analytics page** (G11): hourly dayparting, budget, and raising bids by ASIN during hours. [official].

## What practitioners add

Everything here is [opinion] unless marked. Each item is the named person's or firm's claim, with the date the page shows. Where a claim meets an Amazon text from above, the meeting is noted. These claims are not Amazon's rules.

### CRaP, "financial thresholds" and ad eligibility

- **Flywheel, Gabe Fishbein, "How to strategize against Amazon's recent eligibility changes" (2024-10-23).**
  - "Flywheel recently noticed an increase in ASINs becoming ineligible for Sponsored Products ads."
  - Safe-listed ASINs are "those that Amazon deems to be unprofitable, but the advertiser entered an agreement with Amazon to serve anyway".
  - The change was "a re-evaluation of the profitability issues of previously safe-listed ASINs", after "Amazon adjusted its advertising eligibility equation".
  - "the ineligibility changes only affect an advertiser's ability to serve on SP placements".
  - Replacements: "using Sponsored Brands and Sponsored Brand Video as replacements for conversion-focused goals" and "using Sponsored Display and ADSP as awareness/consideration replacements".
  - "the Amazon retail team has determined a need to be stricter".
  - "We've seen success in reaching out to Amazon reps to relist or add newly ineligible ASINs back to a safe-listed status to continue to serve on SP placements."

  The article does not name vendors or CRaP. Its "only... SP placements" agrees with the 2017 toolkit's point that Headline Search needs only one ASIN past the threshold (D5). https://www.flywheeldigital.com/blog/amazon-advertising-eligibility-changes-strategy
- **Clix Marketing, Kristin Kusiak (2017-10-24), on "financial threshold warnings".** She glosses the acronym as "Can't Realize Any Profit". She describes:
  - campaigns where every ASIN is ineligible, which then become ineligible as a whole;
  - Headline Search campaigns as the worst case: "If just one of those products becomes ineligible, the entire campaign is now ineligible", and the campaign has to be copied, not edited;
  - three remedies: whitelisting eligible products through Amazon's "Contact Us" form (a second request for already-ineligible products was denied); monitoring pricing, including "If you have your products on Amazon Seller as well, consider increasing your prices slightly there to make your products on Vendor more competitive"; and bundling an ineligible product with an eligible one into a new "combo" product to advertise.

  The article dates from the AMS era and matches the toolkit's terms. Her Headline Search account differs from the toolkit's, which needs only one ASIN past the threshold (D5). https://clixmarketing.com/ways-to-overcome-amazons-frustrating-financial-threshold-warnings/
- **AMALYZE, ad eligibility guide (undated).** "Out-of-stock ASINs lose ad eligibility within hours." https://amalyze.com/resources/guides/advertising/amazon-ppc-ad-eligibility
- **Commerce Canal (dated "Apr 15", no year).** Low-margin ASINs "are categorized as "Ineligible ASINs" and are automatically excluded from media campaigns." "these products can no longer be promoted through Amazon's advertising channels." Its formula: "Net PPM% = (Average Selling Price−Price+Terms−Sales Discount) /Average Selling Price × 100". https://www.commercecanal.com/commerce-canal-whats-new/how-does-amazon-net-ppm-affect-vendors
- **SellerApp, Brij Purohit (published 2025-12-13, modified 2026-10-10).**
  - "Products with little to no profitability may be flagged by Amazon as CRaP", with consequences "like removal of A+ Premium content from listing, loss of Buy Box privilege (maybe due to offering discontinued pricing), or withdrawal of advertising eligibility completely."
  - "If you suspect a product is CRaP (you'll often see reduced ad eligibility or no new POs, which may indicate a CRaP)".
  - "In the final phase of CRaP-out, Amazon stops ordering the product entirely".

  https://www.sellerapp.com/blog/amazon-net-ppm/
- **MerchantSpring, Rachel Seiton, "Boost vendor margins with Amazon Net PPM" (2026-04-06, updated 2026-09-11).** CRaP is "Can't Realise a Profit": "If a product's net PPM is too low or negative, Amazon may start treating it as a loss-maker." When an item is CRaPped out, "Amazon pauses your advertising and promotions on the listing" and you "can no longer run Sponsored Products or promotions on it". https://merchantspring.io/resources/boost-vendor-margins-with-amazon-net-ppm-avoid-crap-out-risks
- **MerchantSpring, Rachel Seiton, "The Hybrid Playbook" (2026-08-13).** "a product that stops turning gets tagged CRaP, its internal label for "can't realise a profit,"" and then "the purchase orders quietly stop." https://merchantspring.io/resources/the-hybrid-playbook-deciding-1p-vs-3p-product-by-product

[seat] Across these practitioners, CRaP is said to remove SP eligibility first and POs later. Amazon's own current text has `INELIGIBLE_PRODUCT_COST` and `CP_INELIGIBLE_*` values, with no description. The two meet in the claim, not in an Amazon sentence.

### Net PPM, and whether advertising sits inside it

- **Reason Automation, Andrew Hamada, "Amazon Net PPM calculation" (byline Jan 15, 2026).** He defines Net PPM as "Amazon's gross profit calculation for a product after factoring in the cost of goods sold (COGS)". The components:
  - Shipped COGS: "The item's PO cost price; the cost of goods sold that Amazon paid the vendor for the product";
  - ContraCOGS: "Vendor-provided terms like co-op agreements, accruals, and promotional investments";
  - Sales Discounts: "Discounts provided to customers that are not reflected in the selling price".

  "Multiply Net PPM % by shipped revenue to convert the PPM percentage into currency." "as of January 2026 the best place to get your Net PPM data is from the Sales report, because of a bug in the Vendor Central interface", and he names the Sales report "in Sourcing view". On advertising he says only that "You can use sponsored ads, deals, and off-Amazon media to drive sales of higher-PPM products, shifting your sales mix". https://www.reasonautomation.com/resource-library/amazon-net-ppm-calculation
- **MerchantSpring, Seiton (2026-04-06).**
  - "Amazon doesn't publicly publish net PPM benchmarks per category". Approximate targets "from industry experience": "~ 40-45% net PPM target" for hardlines, "~ 30-37%" for softlines and "~ 27-35%" for consumables. "These ranges are approximations that can vary by sub-category and over time."
  - On ads: "Since ad costs come out of your pocket, not Amazon's, they don't hurt net PPM". "Amazon sees the same revenue and cost from their side whether you advertised or not".
  - On targeting: "Sponsored Display or Product targeting ads from your high-margin ASINs onto your own low-margin ASINs' pages".
  - Net PPM is likely "a point of contention in discussions or Annual Vendor Negotiations".
- **SellerApp, Purohit (2025-12-13, modified 2026-10-10).** "Investments in Amazon Advertising, chargebacks, and payment terms are not included in the Amazon Net PPM calculation, as Amazon reports these variable investments later in its profit and loss account."
- **InsightLeap (2026-10-21).** "Net PPM shows Amazon's product-level margin after cost of goods and services". "Expect it to read higher than your landed margin, since it leaves out chargebacks, freight, and recovery amounts." https://insightleap.com/blog/selling-on-amazon/amazon-sales-analytics
- **AMALYTIX, Trutz Fries, "Amazon Retail Analytics (ARA): Reports for Vendors" (updated 2026-10-25).** "Net PPM is Amazon's net margin on your products, per ASIN and in total." https://www.amalytix.com/en/knowledge/controlling/amazon-retail-analytics-ara/

**Where this meets Amazon.** Practitioners agree that ad spend is outside Net PPM. Amazon's Data Kiosk definition of `contraCogs` subtracts "Display Ads Contra COGS" (E3). Amazon's report schema counts "Vendor Funded Coop" (E1). Neither the practitioners nor Amazon say whether a vendor's sponsored-ads cost enters either of those terms. This is open question 4.

### Stock, POs and pausing ads

- **Intentwise, Michael Waters, "How to pause ad spend when your inventory is low" (2023-07-10; the cited address now redirects to `intentwise.com/blog/how-to-pause-ad-spend-when-your-inventory-is-low`).**
  - "While Seller Central updates inventory data in close to real-time, Vendor Central is much slower on the jump."
  - "Vendor Central usually takes around 48 hours to refresh its inventory data."
  - "On a day like Prime Day, where every hour counts, that's a big delay."
  - "Amazon will automatically pause ad spend on Sponsored Products ads when a product is out of stock. But it doesn't also pause Sponsored Brands, Sponsored Display, or DSP ads."
  - He proposes rules that "pause your ad spend once your product dips below a certain inventory threshold", with no figure.

  The 48-hour figure predates the rapid inventory report (F6), which Amazon says can be requested five minutes after each hour. His "doesn't also pause Sponsored Brands [or] Sponsored Display" is about stock pauses; Amazon's current page says Display serves 0 impressions without the Featured Offer, and SB keeps serving only while the product is buyable (D1). https://www.intentwise.com/blog/amazon-advertising/how-to-pause-ad-spend-when-your-inventory-is-low/
- **Sreenath Reddy, Intentwise (Amazon-hosted, 2023).** "inventory-aware advertising management" (L1).
- **SellerApp and MerchantSpring** (above): POs stop after CRaP.

[seat] For a vendor, out of stock is downstream of POs that Amazon did not place, or that the vendor did not confirm (F1, F3, F4). The ad-side signal (paused, OUT_OF_STOCK) arrives after the retail-side signals (`openPurchaseOrderUnits`, `vendorConfirmationRate`, `procurableProductOOS`, `mostRecentSubmitted`) have moved. No practitioner read today states this sequence with a measurement.

### The manufacturing and sourcing views, and the TACoS denominator

- **m19, help page "Vendor manufacturing and sourcing metrics" (undated; footer © 2026).**
  - "The **Manufacturing metrics** are only available for manufacturer brands on Amazon." "They shows the aggregated sales and inventory performance of your brand, regardless of where the products were sourced", and "may include products sourced from distributors and wholesalers."
  - "The **Sourcing Metrics** relate directly to your account's performance."
  - Three TACoS variants: "TACOS (manufacturing): Spending as a percentage of manufacturing ordered sales"; "Shipped TACOS (manufacturing): Spending as a percentage of manufacturing shipped sales"; "TACOS (sourcing): Spending as a percentage of sourcing shipped sales".
  - "Ad Sales Share": "Percentage of manufacturing (or sourcing) sales generated through advertising."

  https://help.m19.com/vendor-manufacturing-and-sourcing-metrics
- **Pare.so, George Reid (2026-03-26), on hybrid PPC managers.** He names two TACoS denominators: "one reported in Vendor Central (ordered revenue...)" and "one in Seller Central (shipped revenue)". "Blending them without correction produces a meaningless metric." https://pare.so/blog/amazon-ppc-manager-hybrid-1p-3p-sellers-skills-vetting-guide

  [seat] Amazon's own fields read the other way round. The seller Sales and Traffic report carries ordered product sales. The vendor Sales report carries both ordered (manufacturing view only) and shipped revenue (G2). Reid's pairing looks inverted against Amazon's definitions, though his point about blending stands. Recorded as his claim.
- **InsightLeap (2026-10-21).** "Ordered Revenue and Ordered Units count customer orders before shipment, and they appear only in Manufacturing View." "Sourcing View covers the ASINs Amazon bought from you under your vendor code". "Amazon's service level for weekly reporting periods is the end of the day on Monday", so "A Monday morning review is looking at a week that hasn't landed yet". "The vendor conversion rate is shipped units divided by glance views, so you build it from two reports."

  This differs from Amazon's tip, "Conversion = ordered units / glance views", on the rapid sales report (G6).
- **AMALYTIX, Fries (2026-10-25).**
  - "Manufacturing: all ASINs you manufacture, no matter who supplied them to Amazon." "Sourcing: all ASINs Amazon bought directly from your vendor group."
  - "Ordered Revenue and Ordered Units: revenue and quantity of orders in the selected period, net of returns." "Shipped Revenue: revenue of the units Amazon shipped to customers."
  - "Amazon delivers all vendor ARA data in Pacific Time (PST), whatever the marketplace."
  - "weekly figures 48 hours after the week ends, daily figures usually 72 hours after the day ends."
  - ARA tiers: "ARA Basic was free, ARA Premium cost about $30,000 a year". Vendor Central now "shows no tiers any more".
  - Glance views are now "Featured offer page views" in ARA, and "they used to be called Glance Views". "Procurable product OOS %" is the "share of page views where a procurable product was out of stock" and replaces "RepOOS".
- **Reason Automation, Andrew Hamada, "Traffic data in Vendor Central now available" (Sep 25, 2025).**
  - "Glance views are only counted when a retail (1P) offer is featured (i.e. winning the buy box)."
  - "glance views were renamed to **featured offer page views** (FOPVs) in Vendor Central".
  - "Glance views are only available in **manufacturing** view in Retail Analytics in Vendor Central and via Amazon's SP-API."
  - Sessions "are not available to 1P vendors at this time."
  - On conversion: "Amazon doesn't calculate it for you".

  https://www.reasonautomation.com/resource-library/traffic-data-vendor-central-now-available

### Brand Analytics for vendors

- **AMALYTIX, Fries, ARA article (2026-10-25).** "Amazon Brand Analytics is open to sellers and vendors who have enrolled their brand in Brand Registry." Vendors see "the Top Search Terms, Repeat Purchase Behavior and Market Basket Analysis reports." "Search Query Performance and Search Catalog Performance are not there; they are for sellers only."
- **AMALYTIX, Fries, SQP article (updated 2026-10-20).** "Vendor Central does not offer the report (checked in a vendor account, October 2026)". https://www.amalytix.com/en/knowledge/controlling/amazon-search-query-performance-report/

These agree with H1 and H2. Fries's Brand Registry sentence agrees with the SP-API availability line (H2), not with the FAQ's "vendors do not need to enroll" (A3). The FAQ sentence is about advertising.

### Vendor promotions and their cost

- **AMALYTIX, Trutz Fries, Lightning Deals article (updated 2026-10-28).**
  - Vendors create deals under Merchandising › Promotions.
  - "Vendors fund the discount per unit, in local currency and excluding tax".
  - The article "names no separate deal fee for vendors (as of October 2026)".

  https://www.amalytix.com/en/knowledge/marketing/amazon-lightning-deals/
- **Wake Commerce, James Wakefield, on vendor co-op agreements (2024-07-11).**
  - Co-op is also called ContraCoGS.
  - It runs through a Co-Op Portal, with deductions through PO invoices.
  - Price protection is one of the agreement types.

  https://www.wakecommerce.co.uk/blog/amazon-vendor-coop-agreements
- **Quartile, Adely Priszkulnik (2026-08-04).** Seller deal deadlines for 2026: Prime Big Deal Days early on Aug 5 and final on Sep 8; Black Friday and Cyber Monday on Sep 5 and Oct 20. No vendor dates. https://www.quartile.com/blog/amazon-2026-holiday-deal-deadlines-is-your-promotion-strategy-ready

  A search snippet credited to My Amazon Guy gave an extended Prime Big Deal Days deadline of Sep 22. The page was not opened, so the date is not cited (open question 6).

### Hybrid brands

- **MerchantSpring, Seiton, "The Hybrid Playbook" (2026-08-13).**
  - "one brand, one content standard, but two distinct advertising strategies", "which is how the channels reinforce rather than cannibalise each other."
  - "Treat 1P products as upper-funnel workhorses": "their higher conversion lets you afford broad category terms and awareness plays."
  - "Run 3P on the lower funnel, retargeting, defensive branded terms and conversion promotions", "where your pricing control lets you actually close the deal."
  - If "your advertising budget is too small to fund both channels properly", "hybrid will likely make you underperform on both fronts."
  - 1P "moves at Amazon's purchase-order pace".
  - "Since late 2024, Amazon has been terminating smaller vendor relationships in waves, consolidating Vendor Central around its largest suppliers and pushing US brands under roughly five million dollars in annual sales out to Seller Central", citing ChannelEngine; "The most recent wave carried a termination date of 2 August 2026." No Amazon page read today states this.
- **Pare.so, Reid (2026-03-26).** The two TACoS denominators; see above.
- **JumpFly, Shannon O'Connell (2021-01-12), on Sponsored Display.** "For sellers, Sponsored Display ads will only serve when their seller offer is in the buy box. Vendor ads, on the other hand, will only serve if Amazon.com is the featured offer in the buy box for any of the Amazon Standard Identification Numbers (ASINs) in the display campaigns." It cites no Amazon source. It agrees with Amazon's current Featured Offer page for Display (D1), and not with the 2017 toolkit's Product Display rule (D5). https://www.jumpfly.com/blog/increase-your-visibility-with-amazon-sponsored-display-ads/

### Amazon-hosted partner voices on vendors

- **Intentwise (Reddy), 2023**: L1.
- **Acorn-i and DemandHelm (2023)** are cited on the Rapid retail analytics page (G11). Their pages were not opened.

## Published research

These papers were read today as abstracts, through Crossref, NBER or arXiv, not as full texts. Nothing below is stated beyond what the abstract says. None of them studies Amazon advertising directly. They bear on why a reseller (1P) and a marketplace (3P) seller face different ad economics.

### Reseller against marketplace: who controls the marketing variable

- **Hagiu and Wright, "Marketplace or Reseller?", *Management Science* 61(1):184–203, 2015 (doi:10.1287/mnsc.2014.2042).** They model the choice as one of "whether control rights over a noncontractible decision variable (the choice of some marketing activity) are better held by suppliers (the marketplace mode) or by the intermediary (the reseller mode)". The trade-off "is shifted toward the reseller mode when marketing activities create spillovers across products". Transfer to ads [seat]: in the 1P mode the retailer holds the price and much of the merchandising, while the vendor still buys the sponsored ads. The vendor therefore controls the marketing activity the model assigns to the intermediary in reseller mode only in part.
- **Abhishek, Jerath and Zhang, "Agency Selling or Reselling? Channel Structures in Electronic Retailing", *Management Science* 62(8):2259–2280, 2016 (doi:10.1287/mnsc.2015.2230).** "agency selling is more efficient than reselling and leads to lower retail prices; however, the e-tailers end up giving control over retail prices to the manufacturer." When "e-tailers benefit from positive externalities from the sales of the focal product (such as additional profits from sales of associated products), retail prices may be lower under reselling than under agency selling".
- **Tian, Vakharia, Tan and Xu, "Marketplace, Reseller, or Hybrid: Strategic Analysis of an Emerging E-Commerce Model", *Production and Operations Management* 27(8):1595–1610, 2018 (doi:10.1111/poms.12885).** "the hybrid mode is preferred when order‐fulfillment costs are moderate and suppliers' products are somewhat similar". The intuition "hinges on the trade‐off between transfer of pricing rights and the responsibility for order fulfillment."
- **Etro, "Hybrid Marketplaces with Free Entry of Sellers", *Review of Industrial Organization* 62(2):119–148, 2023 (online 2022-12-29; doi:10.1007/s11151-022-09893-8).** A hybrid marketplace "such as Amazon that sells its own products and sets commissions on third-party sellers". The introduction of its own products "is neutral for consumer welfare for a given commission", with an ambiguous effect through the commission.
- **Hagiu, Teh and Wright, "Should platforms be allowed to sell on their own marketplaces?", *RAND Journal of Economics* 53(2):297–327, 2022 (doi:10.1111/1756-2171.12408).** It studies the "dual mode". "policies that prevent platform imitation and self‐preferencing generate better outcomes than an outright ban on the dual mode."

### Amazon as retailer beside its marketplace sellers

- **Jiang, Jerath and Srinivasan, "Firm Strategies in the 'Mid Tail' of Platform-Based Retailing", SSRN working paper 2010 (doi:10.2139/ssrn.1633150).** "Empirical evidence clearly suggests that Amazon tends to sell high-demand products and leave long-tail products for independent sellers to offer." The platform may "strategically learn from these sellers' early sales which of the "mid-tail" products are worthwhile for its direct selling".
- **Zhu and Liu, "Competing with complementors: An empirical look at Amazon.com", *Strategic Management Journal* 39(10):2618–2642, 2018 (doi:10.1002/smj.2932).** "Amazon is more likely to target successful product spaces", and "less likely to enter product spaces that require greater seller efforts to grow". "While Amazon's entry discourages affected third‐party sellers from subsequently pursuing growth on the platform, it increases product demand and reduces shipping costs for consumers."
- **Farronato, Fradkin and MacKay, "Self-Preferencing at Amazon: Evidence from Search Rankings", NBER Working Paper 30894, 2023 (doi:10.3386/w30894).** Using browser-extension panel data: "Amazon branded products are indeed ranked higher than observably similar products in consumer search results. The prominence given to Amazon brands is 30% to 60% of the prominence granted to sponsored products." This is about Amazon's own brands, not about the retail offer on a vendor's ASIN.
- **Dubé, "Amazon Private Brands: Self-Preferencing vs Traditional Retailing", SSRN 2022 (doi:10.2139/ssrn.4205988).** An argument that "Amazon's private brand practices mimic those used by established retailers for decades". It reports no ad measurement.
- **Seibel and Dendorfer, "What's In the Box? The Effect Of Self-Preferencing On Amazon Marketplace" (SSRN 2026, doi:10.2139/ssrn.6181653; earlier version 10.2139/ssrn.5219585).** Crossref now serves the 2026 abstract. It studies Amazon's "Similar item to consider" box, which on the Canadian site "systematically suppresses" recommendations of alternatives to Amazon Basics products, and finds that non-Amazon-Basics products "that merit a recommendation in the US but are denied one in Canada suffer a 11% decrease in the volume of sales". This is about Amazon's own brand, not the retail offer on a vendor's ASIN.
- Hartzell, "Platform Preferencing and Price Competition II: Evidence From Amazon" (SSRN 2025, doi:10.2139/ssrn.5126920). Only the title was seen in Crossref today, with no abstract, so it is listed as a lead and is not cited for any finding.

### Vendor-funded marketing and pass-through

- **Bergen and John, "Understanding Cooperative Advertising Participation Rates in Conventional Channels", *Journal of Marketing Research* 34(3):357–369, 1997 (doi:10.1177/002224379703400305).** "Cooperative advertising plans... make up the majority of marketing funds in some product categories." Their models show "that more generous participation rates are called for with less targetable media, less differentiated retailers, more differentiated brands, and more upscale products within a category." Transfer [seat]: Amazon's co-op ("Vendor Funded Coop" in the Net PPM schema) is the same family of instrument. The sponsored ads a vendor buys are self-serve and highly targetable, which in their model calls for lower participation.
- **Besanko, Dubé and Gupta, "Own-Brand and Cross-Brand Retail Pass-Through", *Marketing Science* 24(1):123–137, 2005 (doi:10.1287/mksc.1030.0043).** From one US supermarket chain: "pass-through varies substantially across products and across categories. Own-brand pass-through rates are, on average, more than 60% for 9 of 11 categories". They also find "substantial evidence of cross-brand pass-through effects". Transfer [seat]: Amazon's 2017 promotion guide says it "generally" aims to pass promotional funding on, and "may choose not to" below financial thresholds (E4). The research shows that pass-through by a reseller is an empirical quantity, not a given.

### Amazon's demand forecasting (bears on POs, not ads)

- **Wen, Torkkola, Narayanaswamy and Madeka, "A Multi-Horizon Quantile Recurrent Forecaster" (arXiv:1711.11053, 2017).** A quantile forecasting framework "demonstrated in an application to predict the future demand of items sold on Amazon.com", including "future planned event spikes and cold-starts". The vendor forecasting report's P70, P80 and P90 levels (F5) are quantile forecasts of this kind. The paper is not stated to be the system behind the report.
- **Amazon Science, "The evolution of Amazon's inventory planning system" (2021).** See F2. [official].

[seat] No paper read today measures how a vendor's sponsored ads change Amazon's purchase orders, or how ad spend changes Net PPM. Both are open (questions 4 and 8).

## Stable enough for a skill

These items are Amazon's own words on current pages, or fields in current models, and are unlikely to change without a model or guide change a skill would see. Figures stay out of the skill (see the tags line).

1. A profile's `accountInfo.type` says whether the advertiser is a vendor. A vendor profile has `validPaymentMethod`, and has no profile `dailyBudget` and no `PUT /v2/profiles` (B1, B2).
2. A vendor's product ads, SD ads and recommendations carry an `asin`. A seller's carry a `sku`. The v3 SKU column is empty for vendors (B3).
3. A vendor may hold several campaigns with one name. A seller may not. An id, not a name, identifies a vendor's campaign (B4; P-ads-api-surface-19; P-launch-44).
4. Vendor SP attribution is 14 days, with brand halo, and counts only products sold by Amazon. Seller SP is 7 days. SB and Display attribution may include sales by third-party sellers. The same 7/14 split runs through budget rules, the v1 base metrics and the v2 console columns (C1, C4).
5. Only vendors may set a custom landing page URL in SB, and it must show at least three advertised ASINs (B5).
6. The Eligibility API answers only for products sold by the profile's merchant, and its statuses include NOT_IN_BUYBOX, OUT_OF_STOCK and INELIGIBLE_PRODUCT_COST (B7).
7. SP pauses an advertised product that goes out of stock. SP and Display serve no impressions for an ASIN or SKU that does not hold the Featured Offer, and Sponsored Brands keeps serving while the product is buyable (D1, F7, J2).
8. A vendor's ordered revenue and units exist only in the manufacturing view. The sourcing view has no glance views. Glance views count only while Amazon retail holds the Featured Offer (G2, G4, G7).
9. Vendor Retail Analytics data is in Pacific time. Amazon's SLA for the Sales and Net PPM reports is end of day Monday for a week and 72 hours for a non-Saturday day; a request made too early ends FATAL (G3; P-ads-organic-and-total-22).
10. AMC Amazon Retail Purchases matches the manufacturing view for vendors (G9).
11. Search Query Performance and Search Catalog Performance are sellers-only. Repeat Purchase, Market Basket and Search Terms are open to vendors who hold the Brand Analytics role and Brand Registry, and Search Terms also needs a brand representative (H1, H2).
12. The promotion performance and vendor coupon reports carry vendor funding (`amountSpent`, `budgetSpent`), are in UTC, and reach back two years. The Promotions API is sellers-only (I1 to I3).
13. Amazon's purchase-order model has PO types, OPEN or CLOSED states, and acknowledgement codes with rejection reasons. The supply fields that precede a stock-out (confirmed, open PO, fill rate, lead time, most recent submitted) are in the inventory report and Data Kiosk (F1, F3, F4).
14. Amazon gives two current wordings of Net PPM. Both are Amazon's margin, not the vendor's (E1, E2).
15. One advertising account links to one Vendor Central account, so a hybrid brand has at least two advertising profiles per marketplace (A5, J3).

## What cx must read at run time

The door is `cx raw amazon-ads`, with `--origin` (NA, EU or FE), `--method`, `--path` and the profile in `Amazon-Advertising-API-Scope` (`references/door.md` in the cx-amazon-ads skill, read 2026-11-09). As read, the door reaches Amazon Ads API origins only. The SP-API operations below are on SP-API hosts. This seat did not call them, and the door as read names no SP-API route (open question 10).

**Through the door (Ads API).**

- `GET /v2/profiles`: `accountInfo.type` (seller, vendor, agency; `KDP_AUTHOR` subtype), `accountInfo.validPaymentMethod` (vendors only), `accountInfo.id` (not unique across marketplaces), `countryCode`, `timezone`. A hybrid brand has a seller profile and a vendor profile in the same marketplace (J3).
- SP campaigns, ad groups and product ads lists (SP 3.0): on a vendor profile, product ads carry `asin`. Campaigns are identified by `campaignId`, because names may repeat (B4).
- `POST /eligibility/product/list` with the ASINs and an `adType` (`sp` by default; `sb`, `sd`, `dsp`). It returns `EligibilityStatus.name` values with a `severity` per product, and answers only for the profile's merchant (B7). The door's gate reads a POST list call as a change (`references/door.md`), so this read goes through the gate like a write.
- The SP serving-status reasons (`SponsoredProductsAdServingStatusReason`, including `CP_INELIGIBLE*`) on the SP 3.0 ad list, read as `areas/diagnosis.md` describes.
- Reports (v3 until 2027-06-30, or Reporting v1): on a vendor profile the SP base conversion metrics are 14-day; the v3 `advertisedSku` column is unavailable; new-to-brand is unavailable for book vendors (C4, B6).
- Billing (`areas/budgets-and-pacing.md`, P-budgets-and-pacing-35) for a payment failure, which pauses campaigns (K1).
- AMC, where the advertiser has an instance: Amazon Retail Purchases, which matches the manufacturing view, and its promotion columns, which cover self-funded promotions only (G9, I6).

**Outside the door (SP-API, vendor authorisation, Brand Analytics role).**

- `GET_VENDOR_SALES_REPORT` with `distributorView` MANUFACTURING and SOURCING, `sellingProgram` RETAIL (and BUSINESS or FRESH where relevant), and `reportPeriod` DAY or WEEK: ordered revenue and units (manufacturing only), shipped revenue, shipped COGS and shipped units (G1 to G3).
- `GET_VENDOR_TRAFFIC_REPORT` and `GET_VENDOR_REAL_TIME_TRAFFIC_REPORT`: glance views while retail is featured (G4, G5).
- `GET_VENDOR_INVENTORY_REPORT`, `GET_VENDOR_REAL_TIME_INVENTORY_REPORT` and `GET_VENDOR_FORECASTING_REPORT`: stock, procurable out-of-stock, confirmation and fill rates, open PO units, lead time and forecasts (F3, F5, F6).
- `GET_VENDOR_REAL_TIME_SALES_REPORT`: hourly ordered units and revenue, which can be negative (G6).
- `GET_VENDOR_NET_PURE_PRODUCT_MARGIN_REPORT`, or Data Kiosk `netPPM`, `contraCogs`, `salesDiscount`: Amazon's margin per ASIN (E1 to E3).
- Data Kiosk `analytics_vendorAnalytics_2024_09_30`: `lostFeaturedOffer`, `procurableProductOOS`, `sourceableROOS`, `openPurchaseOrderQuantity`, `confirmedUnits`, `mostRecentSubmitted`, `overallVendorLeadTime`, `replenishmentCategory`, `msrp` (F4, G7, G8).
- Vendor Orders API: `getPurchaseOrders` and `getPurchaseOrdersStatus`, for PO types, states, acknowledgement and `dealCode` (F1).
- The promotion performance and vendor coupon reports (I1, I2).
- `GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT`, the Market Basket report and the Search Terms report. SQP is not available to a vendor account (H1, H2).
- The notifications `ITEM_INVENTORY_EVENT_CHANGE`, `ITEM_SALES_EVENT_CHANGE` and `DETAIL_PAGE_TRAFFIC_EVENT` (F6, G5, G6).

**For a hybrid brand, on the seller side.** The seller's Featured Offer share (Business Reports, named in D2), the seller Sales and Traffic report (`areas/ads-organic-and-total.md`) and SQP. None of these covers the vendor's retail offer.

**Clocks to align.** The ad reports run in the profile's time zone. Vendor Retail Analytics runs in Pacific time. The promotion and coupon reports and Vendor Orders run in UTC. Vendor attribution runs 14 days and seller attribution 7.

## Pages read

All on 2026-11-09 unless the row says otherwise. "Guide" rows are CloudFront Markdown under `https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/`. "Model" rows are OpenAPI files. "Schema" rows are in `https://github.com/amzn/selling-partner-api-models/blob/main/schemas/`.

| Page | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| FAQs - Advertising questions and resources (Amazon Ads FAQ) | https://advertising.amazon.com/resources/faq | official | 2026-11-09 | Vendor definition; vendor SP and SB criteria; Featured Offer requirement; no Brand Registry for vendors; invite-only vendor invoicing |
| Advertising solutions for Amazon vendors (dateModified 2026-10-09) | https://advertising.amazon.com/library/guides/vendors | official | 2026-11-09 | 14-day vendor attribution; Vendor Central or Advantage Central; DFP limits |
| Link a Vendor Central account to your advertising account (G2P4Y4LNP84V8DST, 2026-02-23) | https://advertising.amazon.com/help/G2P4Y4LNP84V8DST | official | 2026-11-09 | One VC account per advertising account; Selling Accounts link; vendor-code-only case |
| Ad campaign attribution (GX7KDKHMWQYMJ385, 2026-10-20) | https://advertising.amazon.com/help/GX7KDKHMWQYMJ385 | official | 2026-11-09 | "Only products sold by Amazon are attributed"; ranking; merchant against brand; clocks |
| Sponsored Products eligibility requirements (GMJYF5GN8RNYB6HD, 2026-10-20) | https://advertising.amazon.com/help/GMJYF5GN8RNYB6HD | official | 2026-11-09 | Author ads need Amazon as Featured Offer; seller ads need own offer; vendor audiobooks |
| Troubleshoot your products for eligibility (GGBXM3YUBQFEX6YH, 2025-07-09) | https://advertising.amazon.com/help/GGBXM3YUBQFEX6YH | official | 2026-11-09 | "Fix your products" e-learning for vendors |
| Sponsored Brands eligibility requirements (G5DAD7ZM3N639QF4, 2026-08-27) | https://advertising.amazon.com/help/G5DAD7ZM3N639QF4 | official | 2026-11-09 | "approved Amazon Vendor"; vendor audiobooks |
| Understand Sponsored Brands (GGWFYHL27MFXLHS6, 2026-10-20) | https://advertising.amazon.com/help/GGWFYHL27MFXLHS6 | official | 2026-11-09 | SB for vendors and Brand Registry sellers |
| Understand Display (GHYXY6HJRDM5VCCY, 2026-11-02) | https://advertising.amazon.com/help/GHYXY6HJRDM5VCCY | official | 2026-11-09 | Display for vendors and Brand Registry sellers |
| Payment methods, sponsored ads (GMELNQQNEEVLX456, 2026-08-03) | https://advertising.amazon.com/help/GMELNQQNEEVLX456 | official | 2026-11-09 | Vendor card, DFP by vendor code, invoice; payment failure pauses campaigns |
| Understand Featured Offer eligibility (GYVDGT5WNNW23LJ5, 2026-10-16) — added by the verifier | https://advertising.amazon.com/help/GYVDGT5WNNW23LJ5 | official | 2026-11-09 | SP and Display 0 impressions without the Featured Offer; SB unaffected while buyable; SKU-specific; immediate switch |
| Rapid retail analytics - Understand, measure, and optimize your ad campaigns at the product level | https://advertising.amazon.com/measurement-analytics/rapid-retail-analytics | official | 2026-11-09 | "both sellers and vendors"; access through SP-API; hourly use cases; metrics |
| Best practices for your Sponsored Products ads (2026-09-28) | https://advertising.amazon.com/library/guides/sponsored-products-best-practices | official | 2026-11-09 | In stock to be featured |
| Guide to Sponsored Products for new advertisers (2026-10-09) | https://advertising.amazon.com/library/guides/new-advertiser-success-guide | official | 2026-11-09 | Seller featured offer rate in Business Reports, "ideally 90% or higher"; vendor registration path |
| How to improve your product detail page for advertising (2026-10-09) | https://advertising.amazon.com/library/guides/improve-your-products-for-advertising | official | 2026-11-09 | Inventory Dashboard in Vendor Central; automatic pause when out of stock; business reports for featured-offer share |
| Increasing spend efficiency in the Amazon store with Intentwise (2023-03-03; modified 2026-10-09) | https://advertising.amazon.com/library/expert-advice/how-to-increase-ad-spend-efficiency-intentwise | opinion (Amazon-hosted) | 2026-11-09 | Retail-aware and inventory-aware advertising for vendors |
| AMS Agency Toolkit: A Reference Guide for Agency Partners (August 2017) | https://m.media-amazon.com/images/G/01/AmazonMarketingServices/Agency_Toolkit.pdf | official, dated | 2026-11-09 | Financial thresholds; buy box rules by ad type; VPCs on Product Display Ads only |
| Amazon Promotions: Vendor Self-Service Program (March 2017) | https://m.media-amazon.com/images/G/01/boost/assets/2017/Amazon_Promotions_How-to_March2017._V528747406_.pdf | official, dated | 2026-11-09 | Four types; durations, lead times, minimums; funding; pass-through and financial thresholds |
| Amazon 広告 (sell.amazon.co.jp) | https://sell.amazon.co.jp/grow/advertising | official | 2026-11-09 | SP and SD need Featured Offer eligibility; SB serves without it |
| Product ads (SP) | guides/sponsored-products/product-ads.md | official guide | 2026-11-09 | SKU for sellers, ASIN for vendors; in stock to serve; eligibility endpoint |
| Profiles | guides/account-management/authorization/profiles.md | official guide | 2026-11-09 | Vendor accounts for SP, SB, SD only |
| Retrieve profiles | guides/get-started/retrieve-profiles.md | official guide | 2026-11-09 | Vendor profile example |
| Permissions | guides/account-management/permissions.md | official guide | 2026-11-09 | Vendor tiers in the console; granular permissions; seller permissions in Seller Central |
| Registration | guides/account-management/registration.md | official guide | 2026-11-09 | Selling accounts; `POST /adsApi/v1/query/sellingAccounts` |
| Query advertiser accounts | guides/account-management/query-advertiser-accounts.md | official guide | 2026-11-09 | `sellingAccountLinkRequests` |
| Create test accounts | guides/account-management/test-accounts/create-test-accounts.md | official guide | 2026-11-09 | Five-character vendor code; where to find it |
| Use test accounts | guides/account-management/test-accounts/use-test-accounts.md | official guide | 2026-11-09 | Vendor test profile; product metadata by vendor code |
| Well-Architected framework, fundamental component | guides/amazon-ads-well-architected-framework/fundamental-component.md | official guide | 2026-11-09 | Vendor definition |
| Amazon Attribution overview | guides/amazon-attribution/overview.md | official guide | 2026-11-09 | Open to vendors |
| AMC Amazon Retail Purchases | guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid.md | official guide | 2026-11-09 | Manufacturing match; self-funded promotion signals only |
| AMC paid features overview | guides/amazon-marketing-cloud/datasources/paid_features_overview.md | official guide | 2026-11-09 | Manufacturing match; eligibility |
| Stream campaign-management dataset | guides/amazon-marketing-stream/datasets/sponsored-ads-campaign-management.md | official guide | 2026-11-09 | `asin` for SP and SD vendors |
| Stream v2, create a subscription | guides/amazon-marketing-stream/v2/create-a-subscription.md | official guide | 2026-11-09 | No vendor group id |
| Stream v2, get started | guides/amazon-marketing-stream/v2/get-started.md | official guide | 2026-11-09 | Accepted advertiser ids |
| Reporting v1 overview | guides/reporting/ads-v1/overview.md | official guide | 2026-11-09 | 7-day sellers, 14-day vendors base metrics |
| Reporting v1 purchases metrics | guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md | official guide | 2026-11-09 | "[SP: 7d sellers / 14d vendors]" mappings |
| Brand Metrics overview | guides/reporting/brand-metrics/overview.md | official guide | 2026-11-09 | Open to vendors |
| MMM data feed | guides/reporting/marketing-mix-modeling/mmm-data-feed.md | official guide | 2026-11-09 | Vendor-powered coupons clipped |
| Reporting v2 advertising console | guides/reporting/v2/advertising-console.md | official guide | 2026-11-09 | SP vendor columns are 14-day |
| Reporting v3 columns | guides/reporting/v3/columns.md | official guide | 2026-11-09 | SKU not for vendors; NTB not for book vendors |
| Review Requests FAQ | guides/review-requests/faq.md | official guide | 2026-11-09 | ASIN for vendors and sellers |
| Budget rules overview | guides/rules/budget-rules/overview.md | official guide | 2026-11-09 | 7 and 14 days |
| Performance-based budget rules | guides/rules/budget-rules/performance-based.md | official guide | 2026-11-09 | 14 days for vendors |
| Sponsored Brands overview | guides/sponsored-brands/overview.md | official guide | 2026-11-09 | SB for vendors and sellers |
| SD audience targeting | guides/sponsored-display/audience-targeting.md | official guide | 2026-11-09 | `asin` for vendors, `sku` for sellers |
| SD overview | guides/sponsored-display/overview.md | official guide | 2026-11-09 | Tactics by advertiser type |
| SP negative product and brand targeting | guides/sponsored-products/negative-targeting/product-brand.md | official guide | 2026-11-09 | Manual-campaign negatives vendor-only |
| SP overview | guides/sponsored-products/overview.md | official guide | 2026-11-09 | SP for vendors, sellers, KDP |
| Profiles 3.0 model | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml | official model | 2026-11-09 | `validPaymentMethod`; seller-only `dailyBudget` and PUT; id not unique |
| Sponsored Products 2.0 model | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-products/2-0/openapi.yaml | official model | 2026-11-09 | Duplicate names for vendors; `asin` and `sku` |
| Sponsored Products 3.0 (merged JSON) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official model | 2026-11-09 | `CP_INELIGIBLE*` reasons; custom text for book vendors; brand negatives |
| Sponsored Brands (merged JSON) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | official model | 2026-11-09 | Vendor custom landing page, three ASINs |
| Amazon Ads API all merged | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official model | 2026-11-09 | `CUSTOM_URL` vendors only |
| Product selector | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json | official model | 2026-11-09 | 10k cap for sellers and vendors |
| Recommendations | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json | official model | 2026-11-09 | ASIN defined for vendors only |
| Eligibility | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json | official model | 2026-11-09 | Merchant-bound requests; status and reason enums |
| Analytics Reports (`report-type-values-analytics`, updatedAt 2026-10-28) | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics.md | official | 2026-11-09 | All vendor retail analytics reports; Brand Analytics availability |
| SP-API Vendor Use Cases (2026-10-05) | https://developer-docs.amazon/sp-api/docs/sp-api-vendor-use-cases.md | official | 2026-11-09 | Vendor report and notification directory |
| Vendor Analytics Dataset Use Case Guide (2026-09-30) | https://developer-docs.amazon/sp-api/docs/vendor-analytics-dataset-guide.md | official | 2026-11-09 | Views by role; metric groups; compatibility; periods |
| Vendor Retail Procurement Orders API (2026-09-09) | https://developer-docs.amazon/sp-api/docs/vendor-retail-procurement-orders-api.md | official | 2026-11-09 | Operations; roles; vendors only |
| Promotions API (2026-09-09) | https://developer-docs.amazon/sp-api/docs/promotions-api.md | official | 2026-11-09 | Sellers only; types |
| vendorNetPureProductMarginReport schema | schemas/reports/vendorNetPureProductMarginReport.json | official schema | 2026-11-09 | Net PPM definition with vendor-funded coop |
| vendorSalesReport schema | schemas/reports/vendorSalesReport.json | official schema | 2026-11-09 | Ordered fields only in manufacturing view |
| vendorInventoryReport schema | schemas/reports/vendorInventoryReport.json | official schema | 2026-11-09 | Supply and stock field definitions |
| vendorTrafficReport schema | schemas/reports/vendorTrafficReport.json | official schema | 2026-11-09 | Glance views |
| vendorForecastingReport schema | schemas/reports/vendorForecastingReport.json | official schema | 2026-11-09 | Mean and P70/P80/P90 definitions |
| vendorRealTime{Sales,Traffic,Inventory}Report schemas | schemas/reports/ | official schema | 2026-11-09 | Hourly fields |
| vendorCouponReport schema | schemas/reports/vendorCouponReport.json | official schema | 2026-11-09 | Coupon funding, clips, redemptions; UTC |
| promotionReport schema | schemas/reports/promotionReport.json | official schema | 2026-11-09 | Types, statuses, channels, vendor funding |
| sellingPartnerRepeatPurchaseReport schema | schemas/reports/sellingPartnerRepeatPurchaseReport.json | official schema | 2026-11-09 | Repeat purchase fields |
| Data Kiosk vendor analytics schema | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_vendorAnalytics_2024_09_30.graphql | official schema | 2026-11-09 | netPPM, contraCogs, procurability, glance views, lostFeaturedOffer, vendor codes |
| Vendor Orders model | https://github.com/amzn/selling-partner-api-models/blob/main/models/vendor-orders-api-model/vendorOrders.json | official model | 2026-11-09 | PO types, states, acknowledgement, rejection reasons, dealCode |
| Promotions 2025-12-01 model | https://github.com/amzn/selling-partner-api-models/blob/main/models/promotions-api-model/promotions_2025-12-01.json | official model | 2026-11-09 | Promotion and coupon subtypes |
| Amazon Brand Registry \| Sell on Amazon (the three `brandservices.amazon.com` addresses redirect here) | https://sell.amazon.com/brand-registry | official | 2026-11-09 | Same login as Vendor Central |
| The evolution of Amazon's inventory planning system (2021) | https://www.amazon.science/latest-news/the-evolution-of-amazons-inventory-planning-system | official | 2026-11-09 | Buying systems choose quantity per supplier; vendor lead-time variation |
| Seller Forums, "Prime Day 2026: Your Deals Deadline Extended!" (Indy_Amazon, 2026-05-26) | https://sellercentral.amazon.com/seller-forums/discussions/t/9412e643-a006-464d-824a-0121d07c1b63 | official (staff, seller-facing) | 2026-11-09 | 2026 seller deal deadlines; deals suppressed if not buyable |
| Seller Forums UK, "Request to Review Feature Offer Eligibility" (2024-10-25 to 2024-11-08) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/899a64fd-a0b2-49be-b27f-ac2b838ea0b8 | seller claim, staff reply | 2026-11-09 | Vendor account holding the Featured Offer blocks seller SD (claim) |
| Seller Forums US, "Missing Featured Offer for My Listing" (2025-01-17 to 2025-01-27) | https://sellercentral.amazon.com/seller-forums/discussions/t/a8943ddb-0e4f-4bd6-853b-bbdace1a41eb | official (staff) | 2026-11-09 | Featured Offer not guaranteed |
| CNBC, Eugene Kim (2019-03-20, updated 2019-04-01) | https://www.cnbc.com/2019/03/20/amazon-aggressively-suspending-ads-of-unprofitable-products-as-focus-on-the-bottom-line-grows.html | press | 2026-11-09 | CRaP; vendor email wording; spokesperson quote |
| Flywheel, Gabe Fishbein (2024-10-23) | https://www.flywheeldigital.com/blog/amazon-advertising-eligibility-changes-strategy | opinion | 2026-11-09 | Safe-listing; SP-only ineligibility |
| Clix Marketing, Kristin Kusiak (2017-10-24) | https://clixmarketing.com/ways-to-overcome-amazons-frustrating-financial-threshold-warnings/ | opinion | 2026-11-09 | Financial-threshold remedies: whitelisting, pricing, combos |
| AMALYZE, ad eligibility guide | https://amalyze.com/resources/guides/advertising/amazon-ppc-ad-eligibility | opinion | 2026-11-09 | OOS loses eligibility within hours |
| Commerce Canal (Apr 15, no year) | https://www.commercecanal.com/commerce-canal-whats-new/how-does-amazon-net-ppm-affect-vendors | opinion | 2026-11-09 | Ineligible ASINs excluded from media |
| SellerApp, Brij Purohit (2025-12-13, modified 2026-10-10) | https://www.sellerapp.com/blog/amazon-net-ppm/ | opinion | 2026-11-09 | Ads outside Net PPM; CRaP consequences |
| MerchantSpring, Rachel Seiton, Net PPM (2026-04-06, upd. 2026-09-11) | https://merchantspring.io/resources/boost-vendor-margins-with-amazon-net-ppm-avoid-crap-out-risks | opinion | 2026-11-09 | Targets; ads do not hurt Net PPM; CRaP stops SP |
| MerchantSpring, Seiton, The Hybrid Playbook (2026-08-13) | https://merchantspring.io/resources/the-hybrid-playbook-deciding-1p-vs-3p-product-by-product | opinion | 2026-11-09 | Two ad strategies; POs stop after CRaP; vendor terminations in waves |
| Reason Automation, Andrew Hamada, Net PPM (Jan 15, 2026) | https://www.reasonautomation.com/resource-library/amazon-net-ppm-calculation | opinion | 2026-11-09 | Components; Sales report as source in 2026 |
| Reason Automation, Hamada, traffic data (Sep 25, 2025) | https://www.reasonautomation.com/resource-library/traffic-data-vendor-central-now-available | opinion | 2026-11-09 | FOPV rename; manufacturing only; no sessions |
| Intentwise, Michael Waters (2023-07-10) | https://www.intentwise.com/blog/amazon-advertising/how-to-pause-ad-spend-when-your-inventory-is-low/ (redirects to `/blog/how-to-pause-ad-spend-when-your-inventory-is-low`) | opinion | 2026-11-09 | VC 48-hour inventory lag; SB/SD/DSP not auto-paused |
| m19 help, vendor manufacturing and sourcing metrics | https://help.m19.com/vendor-manufacturing-and-sourcing-metrics | opinion (tool) | 2026-11-09 | Three TACoS denominators |
| InsightLeap (2026-10-21) | https://insightleap.com/blog/selling-on-amazon/amazon-sales-analytics | opinion (tool) | 2026-11-09 | Views; Monday SLA; conversion from shipped units |
| Pare.so, George Reid (2026-03-26) | https://pare.so/blog/amazon-ppc-manager-hybrid-1p-3p-sellers-skills-vetting-guide | opinion | 2026-11-09 | Hybrid TACoS denominators |
| JumpFly, Shannon O'Connell (2021-01-12) | https://www.jumpfly.com/blog/increase-your-visibility-with-amazon-sponsored-display-ads/ | opinion | 2026-11-09 | Vendor SD serves only when Amazon is featured |
| AMALYTIX, Trutz Fries, ARA (upd. 2026-10-25) | https://www.amalytix.com/en/knowledge/controlling/amazon-retail-analytics-ara/ | opinion | 2026-11-09 | Vendor Brand Analytics set; views; PST; lags |
| AMALYTIX, Fries, SQP (upd. 2026-10-20) | https://www.amalytix.com/en/knowledge/controlling/amazon-search-query-performance-report/ | opinion | 2026-11-09 | SQP absent in Vendor Central |
| AMALYTIX, Fries, Lightning Deals (upd. 2026-10-28) | https://www.amalytix.com/en/knowledge/marketing/amazon-lightning-deals/ | opinion | 2026-11-09 | Vendor deal funding per unit |
| Wake Commerce, James Wakefield (2024-07-11) | https://www.wakecommerce.co.uk/blog/amazon-vendor-coop-agreements | opinion | 2026-11-09 | Co-op, ContraCoGS, deductions |
| Quartile, Adely Priszkulnik (2026-08-04) | https://www.quartile.com/blog/amazon-2026-holiday-deal-deadlines-is-your-promotion-strategy-ready | opinion | 2026-11-09 | 2026 seller deal deadlines |
| Hagiu and Wright 2015 (Crossref abstract) | https://doi.org/10.1287/mnsc.2014.2042 | research | 2026-11-09 | Marketplace against reseller control rights |
| Abhishek, Jerath and Zhang 2016 (Crossref abstract) | https://doi.org/10.1287/mnsc.2015.2230 | research | 2026-11-09 | Agency against reselling |
| Tian, Vakharia, Tan and Xu 2018 (Crossref abstract) | https://doi.org/10.1111/poms.12885 | research | 2026-11-09 | Hybrid mode conditions |
| Etro 2023 (online 2022; Crossref abstract) | https://doi.org/10.1007/s11151-022-09893-8 | research | 2026-11-09 | Hybrid marketplace commissions |
| Hagiu, Teh and Wright 2022 (Crossref abstract) | https://doi.org/10.1111/1756-2171.12408 | research | 2026-11-09 | Dual mode policy |
| Jiang, Jerath and Srinivasan 2010 (Crossref abstract) | https://doi.org/10.2139/ssrn.1633150 | research | 2026-11-09 | Amazon sells high-demand products |
| Zhu and Liu 2018 (Crossref abstract) | https://doi.org/10.1002/smj.2932 | research | 2026-11-09 | Amazon entry into 3P spaces |
| Farronato, Fradkin and MacKay 2023 (NBER abstract) | https://www.nber.org/papers/w30894 | research | 2026-11-09 | Amazon brands' search prominence |
| Dubé 2022 (Crossref abstract) | https://doi.org/10.2139/ssrn.4205988 | research | 2026-11-09 | Private brands and retail practice |
| Bergen and John 1997 (Crossref abstract) | https://doi.org/10.1177/002224379703400305 | research | 2026-11-09 | Co-op participation rates |
| Besanko, Dubé and Gupta 2005 (Crossref abstract) | https://doi.org/10.1287/mksc.1030.0043 | research | 2026-11-09 | Retail pass-through rates |
| Wen et al. 2017 (arXiv abstract) | https://arxiv.org/abs/1711.11053 | research | 2026-11-09 | Quantile demand forecasting at Amazon |
| Seibel and Dendorfer 2026 (Crossref abstract) — added by the verifier | https://doi.org/10.2139/ssrn.6181653 | research | 2026-11-09 | Amazon Basics recommendation suppression, 11% sales effect |

Local files read (not pages): the cx-amazon-ads skill's `SKILL.md` and `references/door.md`; this package's `areas/launch.md` (shape) and the cross-referenced files named under *What this covers*; and the listing pack's `research/angles/vendor-and-hybrid.md` (read for overlap only, with none of its claims cited).

Count: 111 rows after verification (109 from the research seat, two added by the verifier), which is 113 pages when the real-time schema row is counted as three; the Brand Registry row is now one page.

**Unreachable**

- Vendor Central help: `https://vendorcentral.amazon.com/`, `/help`, `/help/hub/reference/external/G202125300` and `/hz/vendor/members/support/help/node/G202125300` all redirect to sign-in. Not read, by the brief's rule. This is why no current Amazon text on vendor promotion lead times, CRaP or Net PPM dashboards is cited.
- Pacvue, out-of-stock advertising blog: 403 to both WebFetch and curl.
- `https://s3.amazonaws.com/vendorcentral/EN/promotions/story_content/Amazon_Promotions_US_Feb+15+16.pdf`: 403.
- Amazon Ads blog "introducing-simplified-registration-for-vendor-advertising" (US and UK): the page has been removed and redirects to the resources page.
- `https://advertising.amazon.com/solutions/products/rapid-retail-analytics` and `/solutions/products/retail-analytics`: 404. The live page is under `/measurement-analytics/`.
- `https://advertising.amazon.com/blog/sellers-manage-inventory-and-advertising-spend-with-pacvue` and `/blog/how-to-increase-ad-spend-efficiency-intentwise`: redirect to the resource library. The Intentwise piece was read at its library path.
- Amazon Ads what's-new pages `asin-eligibility-status-bulk-operations`, `asin-level-reporting-with-new-attributed-purchases-report` and `amc-dataset-amazon-retail-purchases`: the static HTML carries only the page frame, with no announcement body.
- SP-API slugs `sp-api-for-vendors` and `vendor-use-cases`: 404. The live page is `sp-api-vendor-use-cases.md`.
- `https://d3a0d0y2hgofx6.cloudfront.net/en-us/llms.txt` and `/en-us/sitemap.xml`: 404.
- Acorn-i Ignite FAQ on manufacturing and sourcing (`help.ignite.acorn-i.com/en/faq/manufacturing-and-sourcing/`): the connection closed.
- ACM Digital Library page for Chen, Mislove and Wilson (2016): 403. That paper is not cited.
- Not attempted, by rule: any Ads API host, Login with Amazon, the Amazon Ads MCP endpoints, any SP-API host, the Seller Central or Vendor Central GetHelpTopic content call, and signed-in consoles.

## Open questions

1. **What `INELIGIBLE_PRODUCT_COST` and the `CP_INELIGIBLE`, `CP_INELIGIBLE_ASIN`, `CP_INELIGIBLE_UNKNOWN` and `CP_INELIGIBLE_VENDOR` serving reasons mean.** The models give no description. The 2017 toolkit's "retail financial thresholds" and the practitioners' CRaP fit them, but no current Amazon page ties them together. The seat's reading of "CP" as contribution profit comes from the Data Kiosk wording only.
2. **Who counts as "the same advertiser"** in the attribution page's merchant-and-brand sentence, when a company holds a seller account and a vendor account. The page does not say whether the test is the advertising account, the global account or the brand.
3. **Which Net PPM formula is current.** The report schema says (Product Revenue – Product COGS – Vendor Funded Coop) / Product Revenue. Data Kiosk says (Shipped Revenue – Shipped CCOGS + CCOGS – Sales Discount) / Shipped Revenue. Reason Automation says the Vendor Central interface had a Net PPM bug in January 2026.
4. **Whether a vendor's sponsored-ads cost enters Net PPM.** Data Kiosk's `contraCogs` subtracts "Display Ads Contra COGS". Practitioners (Seiton, Purohit) say ad spend is outside Net PPM. No Amazon page read today says which.
5. **Who may use the rapid retail reports.** The Amazon Ads page says "both sellers and vendors". The SP-API reports say "Vendors", and the notifications say "sellers and vendors".
6. **Current vendor promotion lead times and 2026 event deadlines.** The only Amazon source read is the March 2017 PDF, because Vendor Central is behind sign-in. The 2026 seller deadlines differ across Amazon's staff post (Prime Day), Quartile (Prime Big Deal Days Sep 8) and a My Amazon Guy snippet (Sep 22, not opened).
7. **Resolved by the verifier: whether US Sponsored Brands and Sponsored Display serve without the Featured Offer.** *Understand Featured Offer eligibility* (help GYVDGT5WNNW23LJ5) states that SP and Display serve 0 impressions without it, and that SB keeps serving while the product is buyable (D1, J2). The 2017 toolkit's Product Display rule is superseded for today's Display ads. Still open: whether SB keeps serving when the product is out of stock everywhere, which the page's "as long as the advertised product is available to buy" suggests it does not.
8. **Whether a vendor's sponsored ads change Amazon's purchase orders.** Amazon's 2017 PDF says Amazon "often buys more product to prepare for the promotion" for promotions. No Amazon text or paper read today says the same of ads.
9. **Which revenue is the vendor TACoS denominator.** Amazon names none (G10). The candidates are manufacturing ordered, manufacturing shipped and sourcing shipped revenue, each used by m19. A hybrid brand adds its 3P sales from the seller side.
10. **Whether cx reaches SP-API for a vendor.** The door as read covers Ads API origins only. Every retail-analytics read in *What cx must read at run time* sits outside it.
11. **Whether vendor SP attribution counts Amazon Business and Fresh sales.** "Only products sold by Amazon are attributed" does not say whether Business or Fresh orders of the same ASIN count. The Sales report splits RETAIL, BUSINESS and FRESH.
12. **How quickly the eligibility status of a hybrid ASIN follows the Featured Offer** when Amazon retail and the brand's 3P offer alternate within a day. Amazon says impressions for the previous holder "stop immediately" (D1); no page says how fast the Eligibility API status or the serving-status reason follows.
13. **What `validPaymentMethod: false` does to serving** on a vendor profile, and how it relates to the billing status in `areas/budgets-and-pacing.md`. The model says only that the field reports whether a valid method is set.
14. **Whether DFP failure follows from stopped POs.** The help page says DFP fails if the vendor code's available funds are short. No page says how Amazon nets ad costs against retail payables over time.
15. **The vendor-only negative product targets on manual campaigns.** The conflict between the API guide and the 2025-05-22 release note is held in P-keyword-and-product-targeting-23 and is not settled here.
16. **What `replenishmentCategory` values exist.** The schema types it as a free string, "Availability status for the ASIN", with no list.
17. **Whether the 2017 agency toolkit's rules still hold** (Headline Search needs three eligible ASINs in stock and one past the threshold). The SP buy-box rule is restated in current form by the Featured Offer page (D1); the Product Display rule is contradicted by it. No current page restates the Headline Search threshold.

## Positions

**P-vendors-and-hybrid-1.** Amazon defines a vendor as a business that sells its items directly to Amazon, which then sells them to customers. [official] *FAQs - Advertising questions and resources*; *Well-Architected framework, fundamental component* guide.

**P-vendors-and-hybrid-2.** Amazon's FAQ lists the vendors eligible for Sponsored Products, any one criterion sufficing, as Hardlines, Softlines, Supplier Express (Vendor Express) vendors with a confirmed purchase order or direct fulfillment order, Media, Books and Consumables vendors. It requires SP listings to be eligible for the Featured Offer. Its Sponsored Brands vendor list is Hardlines, Softlines, Media, Books and Consumables (non-Pantry/Fresh). [official] *FAQs - Advertising questions and resources*.

**P-vendors-and-hybrid-3.** Amazon states that only sellers must enroll in Brand Registry to advertise, and that vendors need not. The SP-API Brand Analytics reports, by contrast, require Brand Registry for vendors and sellers alike. [official] *FAQs - Advertising questions and resources*; *Analytics Reports*.

**P-vendors-and-hybrid-4.** An advertising account can be linked to only one Vendor Central account, through Access and Settings > Selling Accounts. The vendor approves a link request by signing in with Vendor Central credentials, and a user not eligible to approve forwards it to someone with admin privileges on the Vendor Central account. [official] *Link a Vendor Central account to your advertising account* (help G2P4Y4LNP84V8DST).

**P-vendors-and-hybrid-5.** A vendor profile's `accountInfo.type` is `vendor`. Amazon says vendor accounts are used with Sponsored Products, Sponsored Brands and Sponsored Display only. [official] Profiles guide; *Profiles 3.0* model.

**P-vendors-and-hybrid-6.** In the Profiles 3.0 model, `validPaymentMethod` is present only for vendors. The profile `dailyBudget` and `PUT /v2/profiles` are for sellers only. `accountInfo.id` is not unique and may repeat across marketplaces. [official] *Profiles 3.0* model.

**P-vendors-and-hybrid-7.** Vendors identify a Sponsored Products product ad by ASIN, and sellers by SKU. In Sponsored Display, vendors use the `asin` field where sellers use `sku`. The v3 advertised-SKU column is not available for vendors. Review Requests take an ASIN from both. [official] *Product ads* guide; *Sponsored Products 2.0* model; *SD audience targeting* guide; *v3 columns* guide; *Review Requests FAQ*.

**P-vendors-and-hybrid-8.** Amazon's SP v2 model states that sellers cannot have duplicate campaign names but vendors can. A vendor's campaign is therefore identified by its id, not its name. [official] *Sponsored Products 2.0* model; see P-ads-api-surface-19 and P-launch-44.

**P-vendors-and-hybrid-9.** Only vendors may give a Sponsored Brands campaign a custom landing page URL. That page must include the ASINs of at least three products advertised in the campaign, and the property cannot be combined with an `asins` list. The merged model's `CUSTOM_URL` landing-page type is "Available for vendors only". [official] `SponsoredBrands_prod_3p.json`; `AmazonAdsAPIALLMerged_prod_3p.json`.

**P-vendors-and-hybrid-10.** Amazon's SP model defines custom text ads only for KDP authors and book vendors in the US, and its brand negative-target recommendations are "Only available for Sellers and Vendors". [official] `SponsoredProducts_prod_3p.json`.

**P-vendors-and-hybrid-11.** Vendor and author Sponsored Products attribution uses a 14-day window, clicks only, with brand halo (none for books), and "Only products sold by Amazon are attributed." For Sponsored Brands and Display, "Attributed purchases may include sales by Amazon or third-party sellers, in New or Used condition." [official] *Ad campaign attribution* (help GX7KDKHMWQYMJ385); *Advertising solutions for Amazon vendors*.

**P-vendors-and-hybrid-12.** Amazon attributes a conversion to at most one ad interaction across all campaigns and advertisers. It states that Sponsored Products for sellers is merchant-based and does not normally compete for attribution with brands, except that where the same advertiser wins as both merchant and brand, the more relevant ad is chosen. [official] help GX7KDKHMWQYMJ385.

**P-vendors-and-hybrid-13.** For vendors, budget rules and performance-based rules compute their metrics over 14 days, and sellers' over 7. The Reporting v1 base metrics follow the same split, and the v2 console maps the vendor SP columns to 14-day totals. [official] *Budget rules* guides; *Reporting v1 overview*; *Reporting v2 advertising console*.

**P-vendors-and-hybrid-14.** A vendor's attributed sales are retail sales; Amazon states they "don't reflect any discounts applied in the cart" and "don't include tax". Amazon defines the vendor's own receipts separately, as shipped COGS, "the price Amazon paid to a vendor for item procurement". [official] help GX7KDKHMWQYMJ385; Data Kiosk vendor schema.

**P-vendors-and-hybrid-15.** Amazon states that an ad does not display if the product is not the Featured Offer or is out of stock, and that an advertised SP product that goes out of stock is automatically paused within its campaign. It states that SP and Display serve 0 impressions when the advertised ASIN or SKU does not hold the Featured Offer, even while the campaign shows "Delivering"; that only the SKU holding the Featured Offer is eligible to serve; that the previous holder's impressions stop immediately when the Featured Offer shifts; and that Sponsored Brands keeps serving while the product is available to buy. [official] *FAQs - Advertising questions and resources*; *How to improve your product detail page for advertising*; *Product ads* guide; *Understand Featured Offer eligibility* (help GYVDGT5WNNW23LJ5).

**P-vendors-and-hybrid-16.** For books, Amazon states that SP ads from an author ads account show only when Amazon itself (not a third-party seller) is the Featured Offer, and that a seller's ads show only when the seller's own offer is the Featured Offer. [official] help GMJYF5GN8RNYB6HD.

**P-vendors-and-hybrid-17.** Amazon's Japanese seller page states that Sponsored Products and Sponsored Display require Featured Offer eligibility, while Sponsored Brands ads are shown even when the advertiser's product is not the Featured Offer. [official] sell.amazon.co.jp *Amazon 広告*.

**P-vendors-and-hybrid-18.** Amazon's AMS-era agency toolkit (August 2017) stated these vendor rules:

- "ASINs must meet retail financial thresholds to be eligible for promotion through Amazon Marketing Services";
- an SP ad paused when the vendor lost the buy box or the ASIN went out of stock, and resumed automatically;
- Headline Search and Product Display ads continued to serve when the buy box was lost (for Display, superseded by the current Featured Offer page, P-vendors-and-hybrid-15);
- Headline Search needed at least three ASINs in stock and one past the financial threshold.

[official, dated] *Amazon Marketing Services Agency Toolkit*.

**P-vendors-and-hybrid-19.** The Eligibility API's `POST /eligibility/product/list` answers only for products sold by the merchant associated with the profile, takes ASINs (SKU optional) and an ad type (`sp` by default, `sb`, `sd` or `dsp`), and returns per-product statuses, each `INELIGIBLE` or `ELIGIBLE_WITH_WARNING`, that include NOT_IN_BUYBOX, OUT_OF_STOCK and INELIGIBLE_PRODUCT_COST. [official] *Eligibility* model.

**P-vendors-and-hybrid-20.** The SP 3.0 serving-status reason enum includes CP_INELIGIBLE, CP_INELIGIBLE_ASIN, CP_INELIGIBLE_UNKNOWN and CP_INELIGIBLE_VENDOR, and Amazon's model gives them no description. [official] `SponsoredProducts_prod_3p.json`.

**P-vendors-and-hybrid-21.** CNBC reported in 2019 that Amazon emailed vendors that products "no longer qualif[y] for advertising" because their sale "currently results in a loss to Amazon", and glossed the practice as CRaP ("Can't Realize a Profit"). No Amazon page read in 2026 uses the term. [press] CNBC, Eugene Kim, 2019-03-20.

**P-vendors-and-hybrid-22.** Flywheel (Gabe Fishbein, 2024-10-23) reports a rise in ASINs becoming ineligible for Sponsored Products after Amazon re-evaluated "safe-listed" unprofitable ASINs. In their account only SP placements were affected, and some ASINs were restored through Amazon reps. [opinion] Flywheel.

**P-vendors-and-hybrid-23.** MerchantSpring (Rachel Seiton, 2026) and SellerApp (Brij Purohit, 2026) state that a CRaP-flagged product loses Sponsored Products or advertising eligibility, and that Amazon may then stop issuing purchase orders for it. [opinion] MerchantSpring; SellerApp.

**P-vendors-and-hybrid-24.** Amazon's Net PPM report schema defines Net PPM as "(Product Revenue – Product COGS – Vendor Funded Coop) / Product Revenue", a fraction from 0 to 1 measuring Amazon's profitability. The report is vendor-only, takes only `reportPeriod`, and is in Pacific time. [official] `vendorNetPureProductMarginReport.json`; *Analytics Reports*.

**P-vendors-and-hybrid-25.** Amazon's Data Kiosk vendor schema defines Net PPM as "(Shipped Revenue - Shipped CCOGS + CCOGS - Sales Discount) / Shipped Revenue". It defines contra-COGS as "the dollars realized by customer outbound shipments minus Display Ads Contra COGS". [official] Data Kiosk vendor schema.

**P-vendors-and-hybrid-26.** MerchantSpring (Seiton) and SellerApp (Purohit) state that a vendor's advertising spend is not part of Net PPM. Seiton gives approximate Net PPM targets of about 40–45% for hardlines, 30–37% for softlines and 27–35% for consumables, which she says vary by sub-category and over time. [opinion] MerchantSpring; SellerApp.

**P-vendors-and-hybrid-27.** Amazon places purchase orders with vendors through the Vendor Orders API. Its PO types are RegularOrder, ConsignedOrder, NewProductIntroduction and RushOrder; an order's state is New, Acknowledged or Closed, and the status call reports OPEN or CLOSED. A vendor acknowledges each line as Accepted, Backordered or Rejected, with rejection reasons TemporarilyUnavailable, InvalidProductIdentifier or ObsoleteProduct. [official] *Vendor Retail Procurement Orders API*; `vendorOrders.json`.

**P-vendors-and-hybrid-28.** Amazon Science states that Amazon's buying systems determine how much of each product to purchase from different suppliers, and that vendor lead times vary with manufacturing capacity, transport and weather. [official] Amazon Science, *The evolution of Amazon's inventory planning system*.

**P-vendors-and-hybrid-29.** The vendor inventory report and Data Kiosk report the supply chain behind a vendor's availability:

- procurable out-of-stock rate (out-of-stock glance views on procurable ASINs over total glance views);
- vendor confirmation rate (confirmed over submitted units);
- receive fill rate (received over confirmed units);
- open PO units;
- average vendor lead time;
- units in the most recent POs of the week;
- sellable on-hand units, in which backorders count as negative units.

[official] `vendorInventoryReport.json`; Data Kiosk vendor schema.

**P-vendors-and-hybrid-30.** Amazon defines procurability as "whether Amazon is able to fulfill a customer delivery promise, considering the ability of known vendors to supply the ASIN in the foreseeable future." [official] Data Kiosk vendor schema.

**P-vendors-and-hybrid-31.** The vendor real-time inventory report gives hourly highly-available inventory per ASIN. It can be requested five minutes after each hour closes, looks back 30 days and spans 7 days. It is also offered to sellers and vendors as the `ITEM_INVENTORY_EVENT_CHANGE` notification. [official] *Analytics Reports*.

**P-vendors-and-hybrid-32.** Intentwise (Michael Waters, 2023) states that Vendor Central takes about 48 hours to refresh inventory data, and that Amazon auto-pauses Sponsored Products for out-of-stock products but not Sponsored Brands, Sponsored Display or DSP. [opinion] Intentwise.

**P-vendors-and-hybrid-33.** The vendor forecasting report gives mean, P70, P80 and P90 weekly demand forecasts per ASIN for the latest forecast only, one store per request. The schema defines P80 as the units with which there is an 80% probability the ASIN will not run out of stock during the period; the Analytics page words it as an 80% probability that customer demand will not exceed the weekly forecast. [official] *Analytics Reports*; `vendorForecastingReport.json`.

**P-vendors-and-hybrid-34.** The Vendor Sales report requires `reportPeriod`, `distributorView` (MANUFACTURING or SOURCING) and `sellingProgram` (RETAIL, BUSINESS or FRESH). The manufacturing view covers ASINs the vendor manufactures, whoever sourced them to Amazon. The sourcing view covers ASINs sourced directly from the vendor group. [official] *Analytics Reports*.

**P-vendors-and-hybrid-35.** In the Vendor Sales report, `orderedRevenue` and `orderedUnits` are populated only in the manufacturing view. Shipped revenue, shipped COGS and shipped units are in both views. [official] `vendorSalesReport.json`.

**P-vendors-and-hybrid-36.** For the Vendor Sales report, Amazon's SLA is end of day Monday (48 hours) for a weekly period and 72 hours for a non-Saturday daily period. A report requested before its period is available ends with `processingStatus` FATAL. DAY data looks back 1,460 days with a 15-day maximum span. [official] *Analytics Reports*.

**P-vendors-and-hybrid-37.** Amazon counts vendor glance views only when Amazon retail is the featured merchant. Data Kiosk's `glanceViews` are "Glance views where Retail is the featured offer". Its `lostFeaturedOffer` is the share of glance views where the vendor's offer does not win the Featured Offer. [official] *Analytics Reports*; Data Kiosk vendor schema.

**P-vendors-and-hybrid-38.** Amazon states that the real-time traffic report's glance views differ from the Vendor Central dashboard's, and are less accurate for concluded days. The data arrives about 65 to 115 minutes after the hour. [official] *Analytics Reports*.

**P-vendors-and-hybrid-39.** The real-time sales report gives hourly ordered units and revenue, five minutes after the hour, with cancellations shown at their own time as negative units. Amazon's tip computes conversion as ordered units over glance views. [official] *Analytics Reports*.

**P-vendors-and-hybrid-40.** In the Data Kiosk vendor dataset, the view a vendor sees (sourcing or manufacturing) follows the role assigned to it. The sourcing view is the distributor view and has no glance views. A vendor group that manufactures nothing gets an error for the manufacturing view. Several manufacturing metrics cannot be grouped by `vendorCode`. [official] *Vendor Analytics Dataset Use Case Guide*.

**P-vendors-and-hybrid-41.** For Vendor Central accounts, AMC Amazon Retail Purchases matches Retail Analytics Sales with Distributor View = Manufacturing. Its promotion signals reflect only vendor or seller self-funded promotions. [official] *AMC Amazon Retail Purchases* guide.

**P-vendors-and-hybrid-42.** No Amazon page read on 2026-11-09 defines TACoS for a vendor or names its total-sales denominator. [official, by absence] the Amazon pages listed in *Pages read*.

**P-vendors-and-hybrid-43.** m19 offers three vendor TACoS variants: spend over manufacturing ordered sales, over manufacturing shipped sales, and over sourcing shipped sales. It says manufacturing metrics may include products sourced from distributors and wholesalers. [opinion] m19 help.

**P-vendors-and-hybrid-44.** Pare.so (George Reid, 2026) states that a hybrid brand's two TACoS denominators come from Vendor Central and Seller Central, and that blending them without correction produces a meaningless metric. [opinion] Pare.so.

**P-vendors-and-hybrid-45.** Search Query Performance and Search Catalog Performance are available through the SP-API to sellers only. Repeat Purchase (18 stores), Market Basket and Search Terms are available to sellers and vendors with the Brand Analytics role and Brand Registry; Search Terms also requires a brand representative. [official] *Analytics Reports*; *SP-API Vendor Use Cases*.

**P-vendors-and-hybrid-46.** AMALYTIX (Trutz Fries, October 2026) reports that Vendor Central offers vendors Top Search Terms, Repeat Purchase Behavior and Market Basket Analysis, but not Search Query Performance or Search Catalog Performance, as checked in a vendor account in October 2026. [opinion] AMALYTIX.

**P-vendors-and-hybrid-47.** Reason Automation (Andrew Hamada, 2025) reports that Vendor Central renamed glance views to "featured offer page views". In their account they count only when a 1P offer is featured, appear only in the manufacturing view, and come with no sessions for 1P vendors. [opinion] Reason Automation.

**P-vendors-and-hybrid-48.** Amazon's promotion performance report covers vendor promotions:

- its types include Best Deal, Deal of the Day, Lightning Deal, Price Discount, Sales Discount, Coupon and Promo Code;
- its statuses include NEEDS_YOUR_ATTENTION;
- creation channels are self-service, full-service (account managers), automated (for example Deal-O-Matic) and manual (Vendisto);
- vendor-only fields are the funding agreement id and the funding amount spent;
- times are in UTC, with two years of start dates.

[official] `promotionReport.json`.

**P-vendors-and-hybrid-49.** Amazon's vendor coupon report gives clips, gross redemptions, total discount and the vendor's budget spent, including clip and redemption fees, per coupon and campaign, with times in UTC. [official] `vendorCouponReport.json`.

**P-vendors-and-hybrid-50.** The SP-API Promotions API (2025-12-01) is available to sellers. Vendor promotions are reported through the promotion performance and coupon reports. [official] *Promotions API*; *SP-API Vendor Use Cases*.

**P-vendors-and-hybrid-51.** Amazon's March 2017 vendor self-service promotions guide listed these terms:

- Price Discount: up to 12 months, submitted at least 24 hours ahead;
- Best Deal: up to 2 weeks, at least 10% off, submitted 4 or more weeks ahead;
- Lightning Deal: up to 6 hours, at least 15% off, with a maximum unit quantity, submitted 4 or more weeks ahead;
- Promo Code: up to 30 days, at least 15% off, submitted at least 24 hours ahead.

It recommended 4 weeks for all, "or Amazon may not have time to buy inventory", and said minimum discounts may rise for Prime Day, Black Friday and Cyber Monday. [official, dated 2017] *Amazon Promotions: Vendor Self-Service Program*.

**P-vendors-and-hybrid-52.** Amazon's 2017 guide states that if a promotion is approved, Amazon often buys more product to prepare for it. It also states that Amazon sets prices independently, generally aims to pass promotional funding on to customers, and may not pass it on if the product does not meet financial thresholds. [official, dated 2017] *Amazon Promotions: Vendor Self-Service Program*.

**P-vendors-and-hybrid-53.** Amazon's August 2017 AMS toolkit stated that "Product Display Ads are the only ad unit that supports VPCs" (vendor-powered coupons), that Subscribe & Save VPCs were not eligible, and that a Product Display ad whose VPC is no longer valid reverts to the normal format. [official, dated] *Amazon Marketing Services Agency Toolkit*.

**P-vendors-and-hybrid-54.** Amazon's Prime Day 2026 staff post for sellers (2026-05-26) extended the Prime-Exclusive Best Deal and Lightning Deal deadline to 2026-06-09. It required inventory in the network or in transit, and stated that deals are suppressed if ASINs are not buyable at event time. [official, seller-facing] Seller Forums, Indy_Amazon.

**P-vendors-and-hybrid-55.** The purchase-order model carries a `dealCode`, a promotional or deal number used to obtain a price discount on items on the order. [official] `vendorOrders.json`.

**P-vendors-and-hybrid-56.** AMALYTIX (Fries, October 2026) states that vendors fund Lightning Deal discounts per unit, in local currency and excluding tax, and names no separate vendor deal fee. Wake Commerce (James Wakefield, 2024) describes co-op, also called ContraCoGS, as deducted through PO invoices. [opinion] AMALYTIX; Wake Commerce.

**P-vendors-and-hybrid-57.** Amazon's ad rules bind each ad to its own advertiser's offer:

- the Eligibility API answers only for the profile's merchant;
- vendor SP attribution counts only products sold by Amazon;
- SP and Display serve only for the advertised ASIN or SKU that holds the Featured Offer, and the previous holder's impressions stop immediately when it shifts;
- for books, a retail-account ad needs Amazon as the Featured Offer and a seller-account ad needs the seller's offer.

[official] *Eligibility* model; help GX7KDKHMWQYMJ385; help GYVDGT5WNNW23LJ5; help GMJYF5GN8RNYB6HD.

**P-vendors-and-hybrid-58.** Amazon's vendor payment methods are card (charged at each credit limit), deduction from retail proceeds by vendor code (which fails if that code's available funds are short), and monthly invoice due in 30 days. Invoicing is invite-only. DFP is not available to third parties managing payments, or to accounts without retail activity in the last 6 months. A failed payment pauses campaigns. [official] *Payment methods (Sponsored ads)* (help GMELNQQNEEVLX456); *Advertising solutions for Amazon vendors*; *FAQs - Advertising questions and resources*.

**P-vendors-and-hybrid-59.** MerchantSpring (Seiton, "The Hybrid Playbook", 2026-08-13) advises two advertising strategies for a hybrid brand: 1P products on the upper funnel and broad category terms, and 3P on the lower funnel, retargeting, branded defence and conversion promotions. She warns that a budget too small for both underperforms on both. She also states, citing ChannelEngine, that Amazon has terminated smaller vendor relationships in waves since late 2024, the latest with a termination date of 2 August 2026. [opinion] MerchantSpring.

**P-vendors-and-hybrid-60.** The Stream v2 subscription API does not accept a Vendor Group id or a Seller Central account id as the advertiser id. It takes a Global Account id or a DSP advertiser id. [official] *Stream v2 create a subscription* guide.

**P-vendors-and-hybrid-61.** Vendor permissions in the advertising console come in three default tiers: Viewer, Editor and Admin. Seller permissions are managed in Seller Central. [official] *Permissions* guide.

**P-vendors-and-hybrid-62.** Hagiu and Wright (2015) model a platform's choice between marketplace and reseller as a choice of who holds control over a noncontractible marketing activity. Spillovers across products shift the choice toward reselling. [research] *Management Science* 61(1).

**P-vendors-and-hybrid-63.** Abhishek, Jerath and Zhang (2016) find in a stylised model that agency selling is more efficient than reselling and gives the manufacturer control of retail prices. Reselling is preferred when the e-tailer gains from sales of associated products. [research] *Management Science* 62(8).

**P-vendors-and-hybrid-64.** Zhu and Liu (2018) find that Amazon is more likely to enter successful third-party product spaces, and less likely where products need greater seller effort to grow. Its entry discourages affected sellers from pursuing growth on the platform. [research] *Strategic Management Journal* 39(10).

**P-vendors-and-hybrid-65.** Farronato, Fradkin and MacKay (2023) find that Amazon-branded products rank higher than observably similar products in search, with a prominence 30–60% of that given to sponsored products. [research] NBER Working Paper 30894.

**P-vendors-and-hybrid-66.** Bergen and John (1997) model co-op advertising and find that more generous manufacturer participation rates are called for with less targetable media, less differentiated retailers, more differentiated brands and more upscale products. [research] *Journal of Marketing Research* 34(3).

**P-vendors-and-hybrid-67.** Besanko, Dubé and Gupta (2005) measure a retailer's pass-through of wholesale price changes. They find it varies widely across products and categories, averages above 60% own-brand in 9 of 11 categories, and includes cross-brand effects. [research] *Marketing Science* 24(1).

### Seat's positions (enter no skill)

- [seat] On an ASIN with both a retail and a 3P offer from one brand, the rules in P-vendors-and-hybrid-57 imply that only one of the brand's two SP ads can serve at a time: the one whose advertiser holds the Featured Offer. No single Amazon sentence states it.
- [seat] "CP" in `CP_INELIGIBLE_VENDOR` may mean contribution profit, after the Data Kiosk wording. This is unconfirmed (open question 1).
- [seat] A vendor ACOS on attributed retail sales is not a margin ratio for the vendor, because the vendor's receipts are wholesale (P-vendors-and-hybrid-14).
- [seat] For a vendor, a stock-out shows on the retail side (confirmations, open PO units, procurable out-of-stock) before the ad side (OUT_OF_STOCK, paused). This is a reading of the field definitions, not a measured sequence.
- [seat] The three clocks (profile time zone for ads, Pacific for retail analytics, UTC for promotions and POs) have to be aligned before any day-level join.
- [seat] Pare.so's pairing of ordered revenue with Vendor Central and shipped revenue with Seller Central looks inverted against Amazon's field definitions.
- [seat] Under DFP, a vendor whose POs have stopped may see its ad payments fail and its campaigns pause (P-vendors-and-hybrid-58). No Amazon page links the two.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** The file was read whole and every cited page was re-opened on 2026-11-09 by plain GET, none sampled (every row of *Pages read* answered HTTP 200 on a plain GET, the three Brand Registry addresses and the Intentwise blog after a redirect): the eight Amazon Ads help pages, with article text, title and `lastModified` taken from the content embedded in the public HTML; the FAQ, four library guides, the expert-advice article and the Rapid retail analytics page as HTML with their `datePublished`/`dateModified`; the two Amazon PDFs on m.media-amazon.com, text-extracted locally (page count and creation date checked); the Japanese sell.amazon.co.jp page; all 29 Ads API guides as markdown from `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`; the eight OpenAPI models from the `d3a0d0y2hgofx6` and `d1y2lf8k3vrkfu` CloudFront documentation hosts, parsed locally for enums, required fields and descriptions; the five SP-API documentation pages as markdown from `developer-docs.amazon` (with `updatedAt`); the eleven report schemas, the Data Kiosk schema and the two SP-API models from `raw.githubusercontent.com/amzn/selling-partner-api-models`; the Brand Registry addresses; the Amazon Science page; the three Seller Forums threads (post dates from their embedded timestamps); CNBC; all 19 practitioner pages; the research items through the Crossref API, the NBER page and the arXiv API. Each quotation was string-matched against the page text with curly quotes and dashes normalised; each page name against the page's own title; each tag against who wrote the words; each date and figure against the page. The Ads API release notes (`release-notes/index.md`, `ads-api-v1.md`, `ads-api-v0.md`, `deprecations.md`) were scanned for vendor changes that overturn a claim (none found), and web searches looked for the source of the unmatched toolkit sentences and for an Amazon statement on 2024–2026 vendor terminations (none found). The sibling files were grepped for vendor, Featured Offer, Net PPM, CRaP, attribution-window and Brand Registry statements. Positions were checked for behaviour wording under decision D233.

**Corrections (was → now).**

1. A2, P-2: the FAQ vendor list quoted as one string ("…Media, Books, Consumables") → the FAQ's own list ("must meet at least ONE criterion", "Media vendor", "Books vendor", "Consumables vendor"), its flagged-in-campaign-manager line, and the full Sponsored Brands vendor list. Page name now *FAQs - Advertising questions and resources* throughout.
2. A4, Pages read: Brand Registry cited as three `brandservices.amazon.com` pages → all three now redirect to one page, *Amazon Brand Registry | Sell on Amazon* (`sell.amazon.com/brand-registry`), which carries the quoted sentence.
3. A5, P-4: page name *Link a Vendor Central account* → *Link a Vendor Central account to your advertising account*; "the vendor approves it with admin privileges" → the vendor approves with Vendor Central credentials, and a user not eligible to approve forwards it to someone with admin privileges.
4. A6, K2, P-11, P-58: *Advertising solutions for vendors* → *Advertising solutions for Amazon vendors* (published 2020-05-18).
5. A8: "for test campaigns" → "for test campaign creation" (verbatim).
6. C1, P-11, stable item 4: added the same page's SB and Display row, "Attributed purchases may include sales by Amazon or third-party sellers, in New or Used condition", so the "sold by Amazon" limit is SP-only; added "Clicks only" and no brand halo for books.
7. C2: "attributed to no more than 1 ad interaction…" → "Amazon will attribute a conversion to no more than 1 ad interaction…" (verbatim).
8. C3, P-14: "Attributed sales exclude cart discounts and tax" → the page's two sentences ("don't reflect any discounts applied in the cart"; "don't include tax").
9. D1, F7, P-15: "If a product you are advertising goes out of stock, it will be automatically paused" cited to *Sponsored Products best practices* → it is on *How to improve your product detail page for advertising*; the best-practices guide's title is *Best practices for your Sponsored Products ads* and carries only the in-stock line.
10. D2: the seller "featured offer rate under the 'Reports' tab" line cited to the improve-your-products guide → it is on *Guide to Sponsored Products for new advertisers* (with "ideally 90% or higher"); the improve guide says to use business reports, and its Vendor Central line is quoted whole. Guide titles corrected in Pages read.
11. D3, J1, J2, P-15, P-57, stable item 7, open questions 7, 12 and 17: "the US help pages read today state no Featured Offer rule for SB" and "the only current Amazon page… for books" → added *Understand Featured Offer eligibility* (help GYVDGT5WNNW23LJ5, lastModified 2026-10-16), already cited by the sibling files: SP and Display serve 0 impressions when the advertised ASIN or SKU lacks the Featured Offer, only the featured SKU serves, impressions stop "immediately" when it shifts, and SB keeps serving while the product is buyable. Open question 7 is resolved; 12 and 17 narrowed. The seat note in J1 no longer asserts the NOT_IN_BUYBOX reading.
12. D5, P-18: toolkit "undated; its CPC tables are 'during April 2017'" → title page "August 2017", created 2017-08-01; "during April 2017" is not in the PDF. The quotations "These financial thresholds are controlled by Amazon Retail." and "In rare instances, an Amazon vendor may not meet these financial thresholds and may be blocked from promoting any of their ASINs." are not in the PDF at the cited URL, and a web search found no other source → removed; the PDF's own sentence ("…Please work with your Agency Contact to ensure this requirement is met") and its in-stock sentence replace them; the Headline Search quote completed with the "Landing page not available" sentence. Open question 1 and E5 no longer cite "controlled by Amazon Retail".
13. I5, P-53: "Vendor-powered coupons (VPCs) are available for promotion via Product Display Ads and Sponsored Products", the 72-hour Vendor Central approval sentence and "vendors may only advertise their own deals" are not in the PDF → removed; the PDF says "Product Display Ads are the only ad unit that supports VPCs" and that Subscribe & Save VPCs are not eligible.
14. B7, P-19, run-time list: added the Eligibility request's `adType` (`sp` default, `sb`, `sd`, `dsp`), the `severity` values with Amazon's definitions, and the reason code BUSINESS_THRESHOLDS_NOT_MET (undescribed).
15. F1, P-27: PO "states are OPEN and CLOSED" → the order's `purchaseOrderState` is New, Acknowledged, Closed; OPEN/CLOSED is the status call's `purchaseOrderStatus`; item confirmation and receive statuses added.
16. F5, P-33: added the Analytics page's different P80 wording ("customer demand will not exceed the weekly forecasted units"), the RETAIL/FRESH option and the verbatim 72-hour line.
17. G7: added the manufacturing-view metrics disabled under the `vendorCode` group-by.
18. H2, P-45, stable item 11: the Search Terms report's availability also requires "a brand representative"; all vendor retail analytics reports name the Brand Analytics role. Page name *Report Type Values: Analytics* → *Analytics Reports* (the page's title) throughout; *Vendor Analytics dataset guide* → *Vendor Analytics Dataset Use Case Guide*.
19. G11, Pages read: Rapid retail analytics page title given in full, with its SP-API access sentence.
20. I4: Price Discount minimum "—" → "any discount"; Promo Code also has a maximum unit quantity; quote "Min % off may increase…" → "Min % off Amazon Retail Price may increase…", a note on the Best Deal and Lightning Deal minimums.
21. I7, P-54: the Prime Day post given its title and date (2026-05-26) and verbatim deadline lines; "until 12 hours before the event" → "until 12 hours before the event end time".
22. J5, Pages read: forum threads "dated only '2 years ago'" → UK thread 2024-10-25 to 2024-11-08, US thread 2025-01-17 to 2025-01-27 (embedded timestamps).
23. L1, Pages read: *How Intentwise uses Amazon's SP-API* → the article's title, *Increasing spend efficiency in the Amazon store with Intentwise*.
24. Kusiak (Clix): "Headline Search as a way around it" and "pairing ineligible ASINs with eligible ones in multi-ASIN ads" → she calls Headline Search the worst case (one ineligible product disables the campaign) and her remedies are whitelisting, pricing (including raising the brand's Seller Central price to make the Vendor offer more competitive) and bundled "combo" products.
25. Flywheel: the reps quote completed ("…to continue to serve on SP placements").
26. SellerApp: "(2026-10-10)" → published 2025-12-13, modified 2026-10-10 (byline Brij Purohit in the page schema).
27. MerchantSpring Net PPM: targets quoted as on the page ("~ 40-45%"), with Seiton's "Amazon doesn't publicly publish net PPM benchmarks per category".
28. Reason Automation Net PPM: added that he names the Sales report "in Sourcing view"; the ads sentence completed.
29. Intentwise (Waters): the cited address now redirects to `/blog/how-to-pause-ad-spend-when-your-inventory-is-low`; his SB/SD line set against Amazon's current Featured Offer page.
30. JumpFly: quote completed (seller sentence and "for any of the ASINs in the display campaigns"); it now agrees with Amazon's current Display rule, not only with the toolkit's SP rule.
31. Research: Tian et al. full title; Etro 2022 → 62(2) 2023, online 2022-12-29; Seibel and Dendorfer now has a Crossref abstract (11% sales effect of Amazon Basics recommendation suppression), recorded as a finding about Amazon's own brand.
32. Stable item 9: "Weekly data lands about two days after the week and daily data about three" → Amazon's SLA as stated for the Sales and Net PPM reports (end of day Monday; 72 hours for a non-Saturday day).
33. Run-time list: "For a hybrid brand, list both profiles for the marketplace" (an instruction) → the fact that a hybrid brand has a seller and a vendor profile in the marketplace (J3).

**Additions found by the verifier.** *Understand Featured Offer eligibility* (help GYVDGT5WNNW23LJ5) as a cited page (correction 11). MerchantSpring's claim, citing ChannelEngine, that Amazon has terminated smaller vendor relationships in waves since late 2024, the latest with a termination date of 2 August 2026 (Hybrid brands; P-59); no Amazon page read states it. Kusiak's hybrid pricing remedy (correction 24).

**Removals.** Four quotations attributed to the 2017 Agency Toolkit that the PDF does not contain (corrections 12 and 13). No position was moved to the seat's list: positions 1–67 state definitions, Amazon's rules, documented mechanisms, measured effects with sources, or named practitioners' claims as theirs; P-59 is Seiton's advice stated as hers.

**Against the sibling files.** `method/ads-api-surface.md` P-ads-api-surface-9 says seller and vendor profiles run sponsored ads "with Sponsored Brands and Sponsored Display requiring Brand Registry". Re-opened: the *Profiles* guide puts the Brand Registry note on the `seller` row only, the FAQ says "Only sellers must enroll in Amazon Brand Registry-vendors do not need to enroll", and *Understand Sponsored Brands* reads "vendors and professional sellers enrolled in the Amazon Brand Registry". This file (A3, P-3) holds; P-ads-api-surface-9 overstates the rule for vendors. `beyond/ad-products-and-eligibility.md` (P-ad-products-and-eligibility-6) and `beyond/brand-defense-and-competition.md` §K already cited the Featured Offer page that this file lacked; this file now agrees with them. The attribution windows (P-metrics-and-attribution-3, P-reporting-17, P-budgets-and-pacing-19), name lengths (P-campaign-structure-19), duplicate names (P-ads-api-surface-19, P-launch-44), the negative-targeting conflict (P-keyword-and-product-targeting-23) and the Vendor Retail Analytics positions (P-ads-organic-and-total-21 to 23) agree with this file.

**Pages unreachable on re-check.** Vendor Central help (`/help/hub/reference/external/G202125300`) answers 302 to `/ap/signin`, not followed. The S3 promotions PDF: 403. `advertising.amazon.com/solutions/products/rapid-retail-analytics`: 404. The simplified-registration vendor blog: 301 to the resource library. SP-API slug `sp-api-for-vendors`: 301 to the 404 page. CloudFront `llms.txt`: 404. Acorn-i Ignite FAQ: connection failed. The Pacvue blog, the ACM page and the what's-new pages were not re-attempted beyond the seat's record, since none is cited for a claim.

**Hosts.** No Ads API host (`advertising-api*.amazon.com`), no Login with Amazon (`api.amazon.com/auth`), no Amazon Ads MCP endpoint, no SP-API host, no Seller Central or Vendor Central `mons-api/GetHelpTopic` content call and no page needing sign-in was called; the Vendor Central redirect to sign-in was recorded and not followed. Hosts called: advertising.amazon.com, d3a0d0y2hgofx6.cloudfront.net, d1y2lf8k3vrkfu.cloudfront.net, developer-docs.amazon, raw.githubusercontent.com, m.media-amazon.com, sell.amazon.co.jp, brandservices.amazon.com and sell.amazon.com, www.amazon.science, sellercentral.amazon.com and sellercentral.amazon.co.uk (public forum pages only), vendorcentral.amazon.com (one unfollowed redirect), s3.amazonaws.com, api.crossref.org, www.nber.org, export.arxiv.org, the practitioner and press sites named in *Pages read*, and a web search tool. No seller data was read. No git repository was touched; the only file written is this one.
