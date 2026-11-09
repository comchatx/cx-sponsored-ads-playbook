# Launching a product with ads

Read 2026-11-09 by the research seat.

Tags: [official] is an Amazon page, cited by page name and URL and read 2026-11-09 unless another date is given. [opinion] is a named practitioner or vendor, with the person or firm given. [research] is a paper, a patent or an academic working paper. [seat] is this seat's own reading and is never a position. Figures (percentages, dollar amounts, day counts) are recorded with page and date **for human readers only**. A skill reads the live figure at run time from the operation named in *What cx must read at run time*.

## What this covers

This file covers what Amazon requires and advises when an ASIN starts advertising with no sales history. "New" here means one of three things: an ASIN that is new to the catalog, an ASIN that is new to advertising, or a seller who is new to Amazon. The file covers:

- the retail readiness gates (Featured Offer, stock, detail page, reviews, eligibility);
- the new-seller and brand programs and ad credits current in 2026;
- auto campaigns as discovery, and Amazon's suggested campaigns and products;
- bids and budgets when there is no history;
- the "honeymoon" or new-release claims, and what Amazon itself says about newness;
- coupons, Vine, deals, Review Requests and how they meet ads;
- organic-rank claims made about launch advertising;
- the timeline of a launch as data accrues;
- research on cold start in product search and on advertising for new firms.

It stays in its lane. Mechanics that hold for any campaign are owned elsewhere and only cross-referenced here:

- campaign shapes: `campaign-structure.md`;
- keyword, product and category targets and their match types: `keyword-and-product-targeting.md`;
- harvesting and negating search terms: `search-terms-and-negatives.md`;
- bid strategies and placement adjustments in general: `bids-and-placements.md`;
- budget rules, out-of-budget and monthly averaging: `budgets-and-pacing.md`;
- events and deal calendars: `seasons-and-deals.md`;
- organic rank and total sales: `ads-organic-and-total.md`;
- why an ad does not deliver: `diagnosis.md`;
- which ad products a seller can use (SB, SD, video, Stores): `beyond/ad-products-and-eligibility.md`;
- attribution windows, ACOS, TACoS and new-to-brand: `beyond/metrics-and-attribution.md`;
- margins and break-even: `beyond/goals-and-economics.md`;
- branded search and competitor defense: `beyond/brand-defense-and-competition.md`;
- Amazon's own automation, rules and recommendations: `beyond/automation-and-amazon-tools.md`;
- endpoint lists and headers: `method/ads-api-surface.md`;
- report lifecycles: `method/reporting.md`;
- before-and-after windows: `method/change-measurement.md`.

This file says what is specific to the launch case, and where Amazon's launch guidance differs from its general guidance.

Out of scope: DSP and Amazon-managed services, beyond noting that they exist for launches (New Product Campaigns); live seller ads; and listing copy, which belongs to the listing playbook.

## Amazon's own rules and guidance

Each claim is marked RULE (Amazon states it as a requirement, or the API enforces it) or GUIDANCE (Amazon recommends it). Amazon's launch guidance is spread over three hosts:

- advertising.amazon.com guides and blogs;
- sell.amazon.com pages, blogs and PDFs;
- the Ads API documentation and its OpenAPI specifications.

They do not always agree, and the disagreements are recorded where they occur.

### A. Who may advertise, and what may be advertised

- RULE: "you must have an active professional seller or vendor account". The same guide continues: "we do not support adult products, used products, refurbished products, and products in closed categories". [official] *New advertiser success guide*, https://advertising.amazon.com/library/guides/new-advertiser-success-guide
- RULE: "products must also be eligible for the featured offer". The same guide: "if your products aren't presenting the featured offer or are out of stock, your ad will not display". [official] *New advertiser success guide* (as above)
- RULE: "In order to advertise, your product must be eligible to be the featured offer." And: "If a product you are advertising goes out of stock, it will be automatically paused within your campaign." [official] *How to improve your product detail page for advertising*, https://advertising.amazon.com/library/guides/improve-your-products-for-advertising
- RULE: "Products must be in stock in order for the ad to serve." A seller's product ad is created with a SKU. [official] Ads API guide *Sponsored Products product ads*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-ads.md
- RULE: a Professional selling plan is needed to advertise, and Brand Registry is required for Stores, Sponsored Brands and display ads. [official] *Advertising | Sell on Amazon*, https://sell.amazon.com/advertising. Which ad products a seller can use is owned by `beyond/ad-products-and-eligibility.md`.
- RULE (Featured Offer, changed 2026): a capture of the Seller Central help page *Featured Offer eligibility* (G200418100) reads "This page has been removed. As of September 2026, Amazon no longer maintains a seller eligibility requirement". The page *Featured Offer* (G37911) is also removed. The page *Becoming the Featured Offer* (G201687550) defines the Featured Offer percentage over page views and says "the Featured Offer is determined separately for each variation". [official, via capture] These captures were made on 2026-10-14 by the listing-playbook seat (`cx-listing-playbook/research/method/help-page-access.md`, section C7). This seat did not re-read them, because the help hub serves its content only through a call this seat may not make.
  - [seat] The ads guides read today still say "eligible to be the featured offer". The two statements fit if the per-offer Featured Offer requirement for ads still stands and only the seller-level eligibility gate was removed. The ads guides do not say which reading is meant. See Open questions.

### B. Retail readiness before the first campaign

Amazon frames readiness as GUIDANCE, apart from the gates in A.

- GUIDANCE: "Review your product detail pages, inventory levels, and pricing before launching campaigns". [official] *Intermediate and advanced new ASIN playbook*, https://advertising.amazon.com/library/guides/intermediate-and-advanced-new-asin-playbook
- GUIDANCE (Featured Offer rate): aim at "winning the featured offer at the highest rate—ideally 90% or higher". The figure is read in Business Reports, *Detail Page Sales and Traffic by Child Item*. [official] *New advertiser success guide*
- GUIDANCE (reviews): "five or more customer reviews—with a rating of 3.5 stars or higher". [official] *New advertiser success guide*; repeated on *How to improve your product detail page for advertising*.
  - This is advice, not a gate. Nothing in the eligibility API reads a review count (see C). Coupons, deals and Vine set their own review rules (J, K).
- GUIDANCE (detail page): titles of about 60 characters; four or more images; at least three bullets. [official] *New advertiser success guide*. Images in which the product fills 80% of the frame, at 1000 px. The Prime badge appears in the creative. [official] *How to improve your product detail page for advertising*
  - The 60-character figure is advertising guidance about truncation. The listing title rules (a 75-character title rule that Canopy reports as effective 2026-07-27) belong to the listing playbook.
- GUIDANCE (feeding the page from ads): use the "search term report available in Amazon Ads Agent" and "add these to your product title, bullet points, and/or product description". [official] *How to improve your product detail page for advertising*
- GUIDANCE (sell.amazon.com prelaunch list): the *30 days to new product success* quick guide (Amazon PDF, footer "3.0 | 050126", created 2026-05-01) lists these prelaunch actions:
  - Brand Registry;
  - FBA, and FBA New Selection;
  - a competitive price;
  - a complete listing, and A+ content;
  - Vine (up to 30 reviews);
  - "Build a Sponsored Products ad campaign";
  - Brand Referral Bonus;
  - Creator Connections.

  Its pro tip: "Complete all prelaunch actions to qualify for complimentary marketing placements across Amazon channels, like in social media or collections on Amazon.com." [official] https://m.media-amazon.com/images/G/01/bx-marketing/Quickguide_30-days-to-new-product-success.pdf
- GUIDANCE: the *Tips for new product success* blog (sell.amazon.com, by Mickey Toogood) has a matching sentence: "Complete all pre-launch and day-one actions in the checklist to qualify for complimentary marketing placements across Amazon channels". [official] https://sell.amazon.com/blog/new-product-success
  - Neither page says what the placements are beyond "social media or collections on Amazon.com", or how qualification is checked.

### C. Eligibility as the API reports it

The ads system exposes the gates in A as machine-readable reasons. These are the launch-day checks.

- RULE (Eligibility 3.0, product eligibility): `POST /eligibility/product/list` takes `adType` (sp, sb, sd or dsp; default sp), up to 50 `productDetailsList` entries (asin, sku, globalStoreSetting) and a `locale`. [official] Eligibility OpenAPI, `Eligibility_prod_3p.json` (contracts index https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json)
  - It returns an `overallStatus` of ELIGIBLE, ELIGIBLE_WITH_WARNING or INELIGIBLE, and an `eligibilityStatusList` of `{name, message, helpUrl, severity}`.
  - The `name` values are ADULT_PRODUCT, CLOSED_CATEGORY, INELIGIBLE_CONDITION, INELIGIBLE_OFFER, INELIGIBLE_PRODUCT_COST, LISTING_SUPRESSED (Amazon's spelling), MISSING_IMAGE, MISSING_TITLE, NOT_IN_BUYBOX, OUT_OF_STOCK, RESTRICTED_CATEGORY and VARIATION_PARENT.
  - Severity, verbatim: "If set to `INELIGIBLE`, the product cannot be included in an advertisement. If set to `ELIGIBLE_WITH_WARNING`, the product may not receive impressions".
  - A 404 "may occur if a product is not associated with the given profile/merchant, or a product is no longer in the catalog". [seat] A freshly created listing that the ads system has not yet picked up is one plausible case of this 404. The spec does not say how long that lag can be.
- RULE (Eligibility 3.0, program eligibility): `POST /eligibility/programs` reports per program (SB, SD, DTC, MAAS, SPOT) at the levels INELIGIBLE and INELIGIBLE_WITH_RESOLUTION, with reason codes. The codes include:
  - NOT_BRAND_REPRESENTATIVE and NO_BRAND_RELATIONS (the brand gates for Sponsored Brands and display);
  - ADS_TERMS_NOT_ACCEPTED and PAYMENT_METHOD_NOT_FOUND (account setup);
  - BUSINESS_THRESHOLDS_NOT_MET;
  - AUTONOMOUS_CAMPAIGNS_FEATURE_NOT_ELIGIBLE, SMART_CAMPAIGNS_FEATURE_NOT_ELIGIBLE and EXPERT_CAMPAIGNS_FEATURE_NOT_ELIGIBLE. [official] Eligibility OpenAPI
- RULE (Product Selector 3.0): `POST /product/metadata` (content type `application/vnd.productmetadatarequest.v1+json`) returns per item:
  - `createdDate`, described as "Date the item was first available on Amazon";
  - `availability`: IN_STOCK, IN_STOCK_SCARCE, OUT_OF_STOCK, PREORDER, LEADTIME or AVAILABLE_DATE;
  - `bestSellerRank`, `priceToPay`, `basisPrice` and `variationList`;
  - with `checkEligibility` set, `eligibilityStatus`, `ineligibilityCodes` and `ineligibilityReasons`.

  `sortBy` accepts CREATED_DATE or SUGGESTED, where "Suggested products are those most likely to engage customers". `pageSize` is at most 300, and results are capped at 10,000. [official] Product Selector OpenAPI, `ProductSelector_prod_3p.json`
- RULE (delivery after launch): v1 entities carry `status.deliveryStatus` (DELIVERING, LIMITED, NOT_DELIVERING or UNAVAILABLE) and `deliveryReasons`. The reasons a launch most often meets are:
  - NOT_IN_BUYBOX, OUT_OF_STOCK, NOT_BUYABLE, NO_PURCHASABLE_OFFER and NO_INVENTORY;
  - AD_MISSING_IMAGE and AD_MISSING_DECORATION;
  - CAMPAIGN_PENDING_START_DATE;
  - AD_GROUP_LOW_BID;
  - CAMPAIGN_OUT_OF_BUDGET and ADVERTISER_OUT_OF_BUDGET;
  - LANDING_PAGE_NOT_AVAILABLE;
  - the MODERATION_* family. [official] Amazon Ads API v1 merged OpenAPI, `AmazonAdsAPIALLMerged_prod_3p.json`

  What each reason means and how to resolve it is owned by `diagnosis.md`.
- RULE (start): "If the campaign start date is set to today, your campaign starts serving immediately". [official] Ads API guide *Sponsored Products auto campaigns*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/auto-campaigns.md

### D. New-seller and brand programs, and ad credits, as of 2026

Amazon publishes the incentive figures in several places, and they differ. The figures below are **for human readers only**. A skill reads the seller's own offers at run time (see *What cx must read at run time*).

**D1. New Seller Incentives (sell.amazon.com).** [official] *New Seller Incentives | Sell on Amazon*, https://sell.amazon.com/incentives (https://sell.amazon.com/grow redirects there)
- Headline: "Get over $50,000 in incentives". The program is "available to new-to-Amazon sellers with Professional selling plans", and its dashboard is in Seller Central.
- New Seller Incentives combine with the Brand Referral Bonus ("10% back on your first $50,000 in branded sales, then 5% back on your next $950,000"). The same page also speaks of "up to $52,500 in automatic referral-fee waivers for your first year". The Brand Registry page words the bonus as running "until you reach $1,000,000".
- Sponsored Products: "$50 credit when you spend $50 / $200 credit when you spend $200 / $1,000 credit when you spend $1,000". The condition: "Create a Sponsored Products campaign for an eligible product within 90 days of listing and spend in ad credits within 30 days of campaign launch. Credit will appear in the Amazon Ads Campaign Manager within two weeks".
- Vine: a $200 credit. Brand Registry must come within six months of the first eligible listing, and the Vine enrollment within 90 days. "Credit expires 90 days after enrollment in Brand Registry".
- Coupons: a $50 credit for a coupon created within 90 days of listing.
- FBA:
  - a $100 Partner Carrier credit, $200 for Amazon Global Logistics and $400 for inbound placement;
  - FBA New Selection;
  - exemptions from the low-inventory and storage surcharges;
  - Multi-Channel Fulfillment at 25% off the first 100 units.
- The Professional plan costs $39.99 a month.
- The older Amazon PDF *New product success* full guide (created 2025-09-12) lists a different set: a $50 Sponsored Products credit, and MCF at 10%. [official] https://m.media-amazon.com/images/G/01/bx-marketing/FullGuide_new-product-success.pdf
  - [seat] Treat the PDF as a past version of the offer. The grow page is the current public statement as read today.

**D2. The Sponsored Products credit, in its terms.** [official] *New Seller Sponsored Products Promotion (2024)* terms, https://advertising.amazon.com/legal/terms-conditions/new-seller-sponsored-products-promotion-2024
- Eligibility: Professional sellers whose first buyable ASIN was listed within the last 90 days, in 19 listed marketplaces.
- Part 1: create the first Sponsored Products campaign, in the same marketplace, within the 90 days.
- Part 2: spend and pay within a 30-day window. The US tiers in the terms body are $50–199.99 spent for a $50 credit, $200–999.99 for a $200 credit, and "$1,000 or more" for a $1,000 credit. There is an AUD 75 / 300 / 1,500 ladder.
- Payout: the "Ad Credit within 14 days after the 30-day Window". "The Ad Credits are valid for 30 days… but not to pay for the ads purchased during the 30-day Window".
- Limits: one advertising ID per seller. Promotions are found under Administration > Billing > Promotions.
- The Amazon Ads Sponsored Products product page carries the banner "Get up to $1000 USD* in ad credits when you launch and spend on Sponsored Products". Its footnote: "Sellers on the Professional selling plan who have listed their first buyable ASIN in the Amazon store in an eligible marketplace within the last 90 days". The banner continues: "New sellers** can earn up to $1000 in ad credits when they launch and spend on Sponsored Products within 30 days of launching their first campaign." [official] *Sponsored Products - Help increase product sales | Amazon Ads*, https://advertising.amazon.com/solutions/products/sponsored-products (the older URL https://advertising.amazon.com/blog/new-bidding-and-targeting-options-for-sponsored-products redirects there)
- RULE (consequence): the credit pays for later ads, not for the spend that earned it. During the 30-day window the seller pays for every click.
  - A seller's post on the EU forum quotes an invitation promotion whose terms read: "Advertisers will be charged for any clicks received before the promotional clicks are applied". [opinion, a seller, not Amazon] *Warning to New Sellers: How Promotional Click Credits… Really Work*, Seller Forums EU, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/151c81a5-d319-4fd7-a990-d0e1b13a943f

**D3. Other ads promotions.**
- *Sponsored Products New ASIN Adoption Promotion*: an invitation-only offer. The seller launches a campaign that advertises the suggested product, or adds that product to an existing campaign. A single credit is issued within 14 business days and is valid for 30 days. [official] https://advertising.amazon.com/legal/terms-conditions/sponsored-products-new-asin-adoption-promotion
- *Sponsored Brands Launch Promotion* (https://advertising.amazon.com/legal/terms-conditions/sponsored-brands-launch-promotion) is a separate offer: "To earn credits, create and launch your first Sponsored Brands campaign." Its FAQ says "Unused credits expire 30 days after the award date." [official] This file did not mine it for amounts.
- The sign-up promotion URL (`…/sponsored-ads-signup-promotion`) and `…/sponsored-ads-new-seller-incentives-promotion` both redirect to the Amazon Ads *About us* page (read 2026-11-09), and are listed as unreachable.

**D4. The credits as the API exposes them (BETA).** [official] Amazon Ads API v1 BETA merged OpenAPI, `AmazonAdsAPIALLMerged_prod_3p_BETA.json` (contracts index)
- `POST /adsApi/v1/query/promotionOffers` lists a global account's offers. Their statuses are AVAILABLE, IN_PROGRESS, MISSED and REWARDED.
  - Each offer has up to two `fulfilmentCriteria`: a CampaignLaunchFulfilmentCriterion (start and end time, status) and a SpendsFulfilmentCriterion (spend, tiers, dates).
  - `promotionCampaign` carries `adProduct`, `title` and `tncUrl`.
  - The schema's own example is "launching a Sponsored Products campaign first, and then spending $500 within 30 days to receive a $300 reward".
- `POST /adsApi/v1/query/promotionRewards` lists rewards: `reward`, `remainingReward`, start and end time, `promotionRewardType` (ADHOC, SIGNUP or PROMO_CODE) and per-invoice consumptions.
- `POST /adsApi/v1/create/promotionCodeRedemptions` redeems a code ("promotion code redemptions for affiliate codes").
- The permissions are `nemo_transactions_view` and `nemo_transactions_edit`.
- [seat] This is the only place a seller's own launch-credit deadline (`endDateTime`) and tier can be read without the console. It is BETA; see Open questions.

**D5. Brand Registry and the brand programs.** [official] *Amazon Brand Registry | Sell on Amazon*, https://sell.amazon.com/brand-registry
- RULE: enrollment needs a logo with the brand name on the product or its packaging, and a pending or registered trademark. IP Accelerator is offered.
- The page names the New Seller Success program, which "pairs select brands with a dedicated Amazon account representative for up to 12 months".
- The page's own figures (for human readers only): Basic A+ "up to 8%", Premium A+ "up to 20%", Stores 53.9% and 71.3%, and Subscribe & Save 1.8x.
- Brand Registry is what opens Sponsored Brands, Sponsored Display and Stores to a seller (*Advertising | Sell on Amazon*). It is also a precondition of the Vine and Brand Referral Bonus incentives (D1).

**D6. Vine.** [official] *Amazon Vine | Sell on Amazon*, https://sell.amazon.com/programs/vine
- RULE (eligibility):
  - a Professional plan;
  - a Brand Representative or Reseller role on a Brand Registry brand, "or have generic products";
  - FBA offers.
  
  Adult, digital and bundled products are not eligible.
- RULE (timing): enroll "as soon as you have a customer-ready FBA listing and set a launch date in the future". An existing product needs fewer than 30 reviews. Up to 30 reviews per parent.
- RULE (fees, per parent): up to 2 units, $0; 3–10 units, $75 (CAD 100 / GBP 60 / EUR 70 / JPY 10,000); 11–30 units, $200 (CAD 240 / GBP 140 / EUR 170 / JPY 22,000). "You aren't charged until 30 days after enrollment and after your first review is published", and if no review is published "within 90 days… you aren't charged".
- GUIDANCE: "we recommend enrolling in Vine and having your inventory available… at least three weeks before your planned launch date".
- Marketplaces: US, CA, UK, FR, DE, IT, ES, AU and JP.
- Amazon's figure (for human readers only): "Boost sales an average of 30%", from Amazon internal data.
- The full guide PDF adds that Vine reviews can arrive before the product goes live, so that "on day one, shoppers can see the Vine badge". It also gives a Vine timeline in steps of "3 days / 2 days / 7 days". [official] *New product success* full guide PDF

**D7. FBA New Selection.** [official] *What is the FBA New Selection program?*, https://sell.amazon.com/blog/fba-new-selection-program
- RULE (requirements):
  - a Professional plan;
  - FBA registration;
  - parent ASINs "that are new to FBA, meaning they have never been received at an Amazon fulfillment center before";
  - an Inventory Performance Index of 300 or higher ("if you haven't been assigned a score yet, you can still enroll"), maintained through enrollment.
- RULE (enrollment): "If you're a new seller, you'll be enrolled in the program automatically if you create your first shipment within 90 days of listing your first buyable product".
- Benefits (for human readers only):
  - "a $75 credit for Vine enrollment for 3 to 10 units per parent ASIN", where the product must be received and enrolled in Vine "within 60 days of listing a buyable offer";
  - "a $50 coupon credit applied to coupon variable fees";
  - no monthly storage and certain surcharge waivers for the first 200 units of each new parent ASIN for 120 days;
  - waived returns processing.
- The blog is dated Jan 14, 2026. PPC Land reports a "New Selection Program (2026)" for branded ASINs listed after July 30, 2026: new FBA sellers are enrolled once "their first FBA shipment of a branded new-to-FBA product is received" within 90 days of listing, existing enrollees had to accept updated terms by October 31, 2026, the referral fee is capped at 10% on the first 100 units and 5% on the next 100, and the $75 Vine and $50 coupon credits apply within 60 days of a buyable offer. [opinion] PPC Land, *Amazon gives sellers until October 31 to lock in FBA fee credits*, https://ppc.land/amazon-gives-sellers-until-october-31-to-lock-in-fba-fee-credits/ (it cites Seller Central documentation without naming a page; no Amazon page read here confirms the 2026 terms).
- [seat] The Vine and coupon credits here differ from the New Seller Incentives figures in D1 ($200 Vine credit, 90 days). They may be two programs that stack, or two versions of one offer. The pages do not say. The program is about fees, not ads. It is recorded because it decides what Vine and coupons cost in the launch window (`beyond/goals-and-economics.md`).

### E. Amazon's launch guidance: the first campaign, suggested products and labels

- GUIDANCE (start with Sponsored Products, then widen): "We recommend launching a Sponsored Products campaign first… As your products start to get more engagement, consider adding Sponsored Brands or display ads". The same page: "Consider using Sponsored Products for new offers". [official] *Advertising | Sell on Amazon*
- GUIDANCE (the getting-started guide):
  - "We recommend for new advertisers to start with Sponsored Products".
  - A minimum daily budget per currency (US $10, CA $10, and so on).
  - "Run your campaigns without an end date… Amazon will automatically update the shopping terms used for your automatic targeting campaigns".
  - "Launch your first Sponsored Products campaign with automatic targeting".
  - "Give each group a pair of automatic targeting and manual targeting campaigns". [official] *Getting started guide for sponsored ads*, https://advertising.amazon.com/library/guides/getting-started-with-sponsored-ads
  - The same page quotes an advertiser: "We found that Amazon Sponsored Products can effectively increase traffic for a new product, especially through keyword targeting — Wela Wen, EU Online Marketplace Team Leader, Anker". [official page, advertiser's words] This is Anker's claim published by Amazon, not Amazon's.
- GUIDANCE (start with automatic targeting, at once, open-ended): "We recommend running your campaign immediately…set your campaign with no end date". And: "Pick automatic targeting". [official] *New advertiser success guide*
- GUIDANCE (API): "If you are new to creating Sponsored Products campaigns, we recommend starting with an auto campaign". [official] Ads API guide *Sponsored Products auto campaigns*
- GUIDANCE (the 30-day roadmap, as Amazon announced it): "Day 1: Ensure your listings are active with inventory in stock, launch Sponsored Products campaigns, and create coupons to boost product visibility". "Day 30: Monitor customer reviews for insights, enhance listings with AI-powered A+ Content, and adjust inventory and advertising based on demand". The roadmap "includes benefits like complimentary marketing placements across Amazon channels when you complete pre-launch steps". [official] *New 30-day roadmap helps you launch products successfully*, Seller Forums news post, dated 2025-08-28, https://sellercentral.amazon.com/seller-forums/discussions/t/bcc285b7-28b6-41b2-bc08-4e1c86a6eea8
  - [seat] On Amazon's own roadmap, the coupon is a day-one action beside the first campaign. It is not something to add after reviews arrive.
- GUIDANCE (auto and manual together, for an intermediate advertiser):
  - under campaign setup: auto campaigns "discover new opportunities", manual campaigns "focus on specific keywords", and "Using both automatic and manual targeting creates a balanced advertising strategy";
  - "Start with the suggested bid, then adjust based on performance";
  - under "How to optimize your campaigns after launch?": "run automatic and manual targeting campaigns together". [official] *Intermediate and advanced new ASIN playbook*
- GUIDANCE (one ASIN per campaign when the catalog is small): "If you have just a few ASINs, we recommend having one ASIN per campaign". RULE: "You can add a maximum 1,000 products per ad group." Under "When to choose automatic targeting" the same guide lists "You're launching a new product in a different category and want to discover insights on shopping searches". [official] *A guide to targeting with Sponsored Products*, https://advertising.amazon.com/library/guides/targeting-with-sponsored-products
- GUIDANCE (suggested products): the campaign creation page shows gray "suggested" labels and green labels, including a "New product" label. [official] *A product advertising strategy*, https://advertising.amazon.com/library/guides/product-strategy
  - Amazon's figures attached to these (for human readers only):
    - "New products observed 36 times more clicks when advertised, compared to products that are not new" (*A product advertising strategy*; footnote "Amazon internal data, WW, 1/1/23-12/31/23. Sales referenced are ad-attributed");
    - "New products are 231 times more likely to generate ad-attributed sales when advertised, compared to products that are not new" (footnote 2, "Amazon internal data, WW, 3/26/23-4/1/23"), and "Suggested products are 321 times more likely to generate ad-attributed sales when advertised, compared to products that are not suggested" (footnote 1, "Amazon internal data, WW, Dec 2021 – May 2023. Limited to sellers with minimum Sponsored Products campaign duration of 6 months post launch") (*Best practices for your Sponsored Products ads*), https://advertising.amazon.com/library/guides/sponsored-products-best-practices;
    - "Suggested products observed 260 times more sales when advertised, compared to products that were not suggested" (*Advertising | Sell on Amazon*).
  - [seat] Each multiple compares two groups of advertised products (new against not new, suggested against not suggested) on ad-attributed outcomes; none compares advertised with unadvertised products, and none is an incrementality measurement. The groups differ in many ways besides the label, so the multiples measure selection as much as any effect of the label. `beyond/metrics-and-attribution.md` owns this reading.
- GUIDANCE (international first campaign): "we recommend advertising at least two suggested products because they have high-quality product detail pages and a high chance of being clicked if advertised". [official] *Checklist for new international ad campaigns*, https://advertising.amazon.com/library/guides/checklist-for-new-international-ad-campaigns
- GUIDANCE (categories for new products): "Use category targeting to help increase visibility of new products". And: "Create manual campaigns to supplement your automated campaign". The same guide says "You can add 1,000 products to an ad group at a time". [official] *Best practices for your Sponsored Products ads*
- GUIDANCE (beyond Sponsored Products in the launch window). [official] *Intermediate and advanced new ASIN playbook*
  - Sponsored Brands: "brand owners who use Sponsored Brands see 23% higher sales after 13 weeks" (Amazon internal data, Jan 2025).
  - Single product video ads: "Use the Drive Page Visits objective… increasing visibility and glance views to help boost organic rankings".
  - "Branded impression share campaigns: Gain top-of-search exposure for new items that don't yet have reviews".
  - Market Basket Analysis to find co-purchase opportunities.
- GUIDANCE (blog): "brands that use upper-funnel tactics within the first month of launch saw 36% higher conversion rates on average than those who waited" (Amazon internal data, US, Aug 2023–2024). The same post: "Brands that clearly messaged their products as new & notable in their ads saw an average increase of at least 22% in click-through rates", and "By driving traffic, these ads can help increase detail page views and product reviews". [official] *How to create your new product launch strategy*, https://advertising.amazon.com/blog/how-to-create-your-new-product-launch-strategy
- GUIDANCE (full guide PDF): "Both product targeting and audience campaigns can be effective for newly launched products".
  - Its combined figure: "when used with fast, free shipping, A+ Content, Vine, coupons, and Sponsored Products can help increase the likelihood of early sales by up to 85%". The source is an internal study of new items in their first 90 days, 1/1/24–9/30/24.
  - It also says: "Reviews also make your new products more discoverable in the Amazon store". [official] *New product success* full guide PDF
- GUIDANCE (sell.amazon.com): "sellers who used Sponsored Products saw 34% more sales growth… four weeks after adoption". [official] *Advertising | Sell on Amazon*
  - *5 steps to launch a product successfully* (sell.amazon.com blog, 2024-06-24) names Lightning Deals, 7-Day Deals and digital coupons beside Sponsored Products, and says to enroll in Vine "soon after listing". It says "Sellers who use the guide during their first 90 days generate approximately 6x more first-year sales on average" (Amazon internal data, FY2023, US store) about the New Seller Guide. https://sell.amazon.com/blog/product-launch
- GUIDANCE (external traffic): "Driving traffic to your Amazon listing can boost additional product sales by an average 24.5%" (footnote: "In 2022, Amazon analyzed over 11 million clicks from Amazon Attribution-related traffic to compare how behavior differs between marketing channels"). [official] *30 days to new product success* quick guide. The same guide repeats the "up to 85%" combined figure.

### F. Auto campaigns as discovery: the mechanism

- RULE: an auto campaign is created with `autoCreationSettings.autoCreateTargets` set to true. After the ad group is created, four auto targeting expressions are created automatically. [official] Ads API guides *Sponsored Products auto campaigns* and *Sponsored Products auto targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/auto-targeting.md
  - Verbatim: "Auto targets are created as `ThemeTargets`".
  - "If you do not set up any auto targeting clauses, your ad group uses the default bid you assigned during ad group creation for all targeting."
  - When an auto target is given its own bid, that bid replaces the ad group default bid.
- RULE: the auto theme match types in v1 are KEYWORDS_CLOSE_MATCH ("Search terms closely matching advertised product"), KEYWORDS_LOOSE_MATCH ("Search terms loosely matching advertised product"), PRODUCT_SUBSTITUTES and PRODUCT_COMPLEMENTS.
  - The same `ThemeMatchType` enum holds further themes that are not the four auto expressions: KEYWORDS_RELATED_TO_YOUR_BRAND, …_YOUR_PRODUCT_CATEGORY, …_PEER_BRANDS_PRODUCT_CATEGORY, …_GIFTS, …_PRIME_DAY ("These keywords will only match queries through the end of Prime Day"), …_YOUR_LANDING_PAGES, PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS and INTERESTED_AUDIENCE. [official] v1 merged OpenAPI, schema `ThemeMatchType`
- RULE: "Once the campaign is live, you will not be able to change the campaign targeting". An auto campaign stays auto. [official] *A guide to targeting with Sponsored Products*
- GUIDANCE (how long auto runs before manual): "We suggest you begin with an automatic targeting campaign… let your automatic campaign run for about two weeks before creating a manual campaign". [official] *A guide to targeting with Sponsored Products*
  - This sits beside the playbook's "run automatic and manual targeting campaigns together" (E) and the getting-started guide's "pair of automatic targeting and manual targeting campaigns". The new-advertiser guide sequences them; the intermediate and getting-started guides pair them.
- RULE (moving auto findings into manual, API): Amazon has a first-class mechanism, the target promotion group. [official] Sponsored Products 3.0 OpenAPI, `SponsoredProducts_prod_3p.json`
  - `POST /sp/targetPromotionGroups/recommendations`: "Retrieves keyword and product targets of an auto-targeting campaign as recommendations for promoting to a manual-targeting campaign. The recommendations are based on performance heuristics of the targets."
  - `POST /sp/targetPromotionGroups` "Creates a target promotion group, by grouping the auto-targeting adGroupId and manual-targeting adGroups, divided by keyword targeting adGroups, and product targeting adGroups". The V2 request takes either `existingCampaignDetails` or `newCampaignDetails`, never both. It "must contain one keyword ad group, or one product ad group, or both".
  - `POST /sp/targetPromotionGroups/targets` "Creates keyword and/or product targets in the manual adGroup".
  - `…/list` and `…/targets/list` read groups back.
  - The spec does not state the heuristics.
  - How harvested terms are negated in the source campaign is owned by `search-terms-and-negatives.md`.
- GUIDANCE (what the search term report shows): its terms are those "that resulted in at least one click". [official] *Best practices for your Sponsored Products ads*. The report and its lifecycle are owned by `method/reporting.md`.

### G. Bids at launch

- RULE (range): the Sponsored Products bid range per marketplace, for human readers only: US, UK, DE and CA 0.02–1,000; AU 0.02–1,410; MX 0.1–20,000 (local currency). Sponsored Brands CPC in the US is 0.10–49 for image and 0.25–49 for video. [official] Ads API *Limits*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md
- GUIDANCE: "Start with the suggested bid, then adjust based on performance". [official] *Intermediate and advanced new ASIN playbook*. "We recommend applying the suggested bid as a starting point for automatic targeting." [official] *Checklist for new international ad campaigns*
- RULE (what a suggested bid is): theme-based bid suggestions are "calculated from a group of recent winning bids for similar products". They come as three bids (low, median, high). [official] Ads API *Theme-based bid suggestions quickstart guide*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/bid-suggestions/theme-based-bid-suggestions-quickstart-guide.md
  - Impact metrics are "not estimates of expected performance". They assume "your campaign does not run out of budget". An ad group needs at least five keywords for impact metrics.
  - The quickstart describes the service as "being released in open beta" and says "Support for product targeting will be added in the future". The Sponsored Products 3.0 OpenAPI's version notes are later: version 4.0 "allows users to get theme-based bid recommendations for product targeting expressions", "supports keyword, auto and product targets in all marketplaces", and "removes 'impact metrics' when returning each bid suggestion". [official] Sponsored Products 3.0 OpenAPI, `/sp/targets/bid/recommendations` description.
  - [seat] Because the suggestion is built from similar products' winning bids, it exists on day one for an ASIN with no history of its own. This is what makes it the default launch anchor in Amazon's guidance.
- RULE (new ad group bids, API): `POST /sp/targets/bid/recommendations` with `recommendationType` BIDS_FOR_NEW_AD_GROUP takes `asins` and targeting expressions, and returns bids before any ad group exists. BIDS_FOR_EXISTING_AD_GROUP is the later form. [official] Sponsored Products 3.0 OpenAPI
  - The v4 content type adds the PAT_ASIN, PAT_CATEGORY, PAT_CATEGORY_REFINEMENT and KEYWORD_GROUP expressions ("This new type is only available in US marketplace" for KEYWORD_GROUP).
  - The v5 content type adds estimated impressions and `includeAnalysis` (eight bids): "New features are currently available only for existing ad group requests in US marketplace."
  - RULE (deprecation): the `application/vnd.spthemebasedbidrecommendation.v3+json` content type was deprecated with a shutoff date of May 15, 2025; callers are told to use v4. [official] *All releases* ("Deprecation announcement: v3 content type for Sponsored Products theme-based bid recommendations will be deprecated on May 15, 2025") and *Deprecations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md. The spec still lists v3, and the API auto-targeting guide's example still sends v3.
  - The quickstart's "product targeting will be added in the future" is superseded by the v4 notes above.
- RULE (keyword suggestions for a new product): `POST /sp/targets/keywords/recommendations` with `recommendationType` KEYWORDS_FOR_ASINS ranks keywords for a list of ASINs, with per-theme bid suggestions. [official] Ads API guide *Sponsored Products keyword recommendations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/suggestions.md
  - The bidding strategy can be set in the request, and `sortDimension` is clicks, conversions or default.
  - Version 4 adds "Search term impression share", "the percentage share of all ad-attributed impressions you received on that keyword in the last 30 days", and search term impression rank. "Search term information is only available for keywords the advertiser targeted with ad impressions", so for a never-advertised ASIN these fields are empty.
  - Version 5 adds the themes CONVERSION_OPPORTUNITIES and SPECIAL_DAYS.
  - The guide's two worked examples for a new ad group: "sort the keywords by clicks, and use 'Dynamic Bidding - Up and Down.'"; and "sort the keywords by conversions, use fixed bidding, and see how your own keywords perform against the suggested keywords".
  - Product and category suggestions are `POST /sp/targets/products/recommendations` and `POST /sp/targets/categories/recommendations` ("If you do not know what products to target, Amazon can recommend products based on the `ASIN`s you are advertising"; "make sure they are similar products"). [official] Ads API guide *Sponsored Products product targeting suggestions*
- RULE (bid strategies), v1 `BidStrategy`:
  - `SALES_DOWN_ONLY`: "Decreases your bids in real time when your ad is less likely to convert to a sale. Bids will never increase beyond your set bid."
  - `SALES_UP_AND_DOWN`: "Increases or decreases your bids in real time by a maximum of 100%".
  - `MANUAL`: "Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding".
  - Also `RULE_BASED`, `NEW_TO_BRAND`, `PRIORITIZE_KPI_TARGET`, `SPEND_BUDGET_IN_FULL` and `USE_CAMPAIGN_STRATEGY`. [official] v1 merged OpenAPI, schema `BidStrategy`
  - The per-product Sponsored Products v1 model narrows the enum to four: `SPBidStrategy` is `MANUAL`, `RULE_BASED`, `SALES_DOWN_ONLY` and `SALES_UP_AND_DOWN`. [official] Amazon Ads API v1, Sponsored Products model, `AmazonAdsAPISP_prod_3p.json`. The other values belong to other ad products.
  - Amazon's pages do not agree on the ceiling by placement. The library guide (published 2025-05-07, modified 2026-10-09) reads "We will increase or decrease your bids by up to 100% for all placements based on performance". [official] *Guide to dynamic bidding - up and down with Sponsored Products*, https://advertising.amazon.com/library/guides/dynamic-bidding-sponsored-products. The help page reads "We may increase or decrease your bids by up to 100% for all placements based on performance" and "Example: Amazon can adjust your bid of $1.00 up to $2.00 for all placements." [official] *Bidding strategies for Sponsored Products* (help GCU2BUWJH2W3A8Z7), https://advertising.amazon.com/help/GCU2BUWJH2W3A8Z7. The SP 3.0 and v1 models say "by a maximum of 100%" and name no placement. Against these, the author's guide (published 2023-09-07, modified 2026-10-09) reads "Bids will be increased by up to 100% for placements at the top of the first page of shopping results and by up to 50% for all other placements." [official] *An author's guide to Sponsored Products*, https://advertising.amazon.com/library/guides/authors-guide-to-sponsored-products. No Amazon page read says that the 50% figure was withdrawn, and no API field reports the ceiling in force. `areas/bids-and-placements.md` owns this conflict (its P-bids-and-placements-8) and the practitioners who use 100/50.
- GUIDANCE (which strategy first): Amazon's pages differ by context.
  - First campaign in a new country: "we recommend you choose dynamic bids - down only". [official] *Checklist for new international ad campaigns*
  - Auto campaigns: "We recommend using dynamic bidding up and down to help maximize performance, or, if you are looking to optimize based on return on ad spend (ROAS), then try a dynamic down only strategy." [official] *A guide to targeting with Sponsored Products*
  - New ad group in the API guide: up and down, sorted by clicks; or fixed bids, sorted by conversions. [official] keyword recommendations guide (as above)
  - No single Amazon page names one strategy as the launch strategy.
- GUIDANCE (match types at launch): "Test different match types for at least 1-2 weeks… before pausing any keywords". The highest bid goes on exact, then phrase, then broad. [official] *A guide to targeting with Sponsored Products*. Match-type mechanics are owned by `keyword-and-product-targeting.md`.
- RULE (placements): placement adjustments go up to 900%. [official] *Best practices for your Sponsored Products ads*. Owned by `bids-and-placements.md`.
- RULE (rule-based bidding is closed to a new campaign): "Your campaign must be running for at least 10 days prior to setting a rule and have a minimum of 10 conversions in the last 30 days". There is also a minimum daily budget per marketplace (for human readers only: US 10, IN 300, JP 600, MX 50, and so on). [official] Ads API guide *Sponsored Products rule-based bidding overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/overview.md
  - The guardrail looks back 21 days. Amazon disables the rule if "the ROAS of the campaign for the last 20 days drops to less than 30% of your ROAS over a 20-to-40-day period".
  - The API also exposes `POST /sp/rules/campaignOptimization/eligibility` ("Gets a campaign optimization rule eligibility for SP campaigns"). A brand-new campaign cannot pass these thresholds; this is the API-level form of "no history".

### H. Budgets at launch

- GUIDANCE: "Daily budget: We recommend starting with a daily budget of $10 or equivalent". [official] *Best practices for your Sponsored Products ads*. The same figure appears in the getting-started guide's per-currency table, and for new country campaigns: "We recommend starting with a minimum daily budget of $10 (or your local currency equivalent)". [official] *Checklist for new international ad campaigns*
- RULE (floor and ceiling): the Sponsored Products daily budget minimum is US 1 (IN 50, JP 100, AU 1.4, and so on), with a maximum of 1,000,000 in the US. [official] Ads API *Limits*. For human readers only.
- RULE (averaging): the daily budget is averaged over the calendar month; the guide's example is that $100 a day gives up to $3,000 a month. [official] *Best practices for your Sponsored Products ads*. Owned by `budgets-and-pacing.md`.
- RULE (initial budget recommendation, API): `POST /sp/campaigns/initialBudgetRecommendation` (content type `application/vnd.spinitialbudgetrecommendation.v3.4+json`) "Creates daily budget recommendation along with benchmark metrics when creating a new campaign". [official] Sponsored Products 3.0 OpenAPI
  - Request: exactly one ad group (`adGroups`, maxItems 1) with up to 50 `asins` and up to 100 targeting expressions (CLOSE_MATCH, LOOSE_MATCH, SUBSTITUTES, COMPLEMENTS and the three keyword match types), `bidding` with a `strategy` (AUTO_FOR_SALES, LEGACY_FOR_SALES, MANUAL or RULE_BASED) and up to two placement adjustments, `startDate` and `endDate` (YYYYMMDD), and `targetingType` (auto or manual).
  - Response: a `dailyBudget`, where "-1 means we don't have enough information". It also gives a `benchmark` with `benchmarkStatus` (success, partial or failed) and next-seven-day lower and upper ranges for impressions, clicks and conversions, plus `specialEvents` with their own daily budgets and benchmarks, and a `recommendationId`.
  - [seat] This is the only budget recommendation in the API built for a campaign that does not yet exist.
- RULE (existing campaigns): `POST /sp/campaigns/budgetRecommendations` returns a recommended daily budget, the percent of time in budget, and missed impressions, clicks and sales. [official] Sponsored Products 3.0 OpenAPI. It needs history, so it applies once a launch campaign has run.
- GUIDANCE (when to raise): "If your campaigns have depleted their budget multiple times in the past seven days, consider an increase"; also when impressions are low. [official] *Checklist for new international ad campaigns*
- GUIDANCE (managed launch): for Amazon's managed services, "Budget minimums apply". [official] *How to create your new product launch strategy*

### I. Newness, "new release" and the honeymoon question: what Amazon says

- Amazon does not claim, on any page this seat read, that new ASINs get a temporary ranking boost, and no Amazon page uses the word "honeymoon" in its own voice.
- The word appears on an Amazon page only once, in a seller quote. Kyle Goguen (CRBN Pickleball / Pawstruck): "we refer to that first 30 days as the honeymoon period…". [official page, seller's words] *Tips for new product success*, sell.amazon.com blog
  - The quote is a seller's claim published by Amazon, not Amazon's claim.
- What Amazon does say about the first weeks:
  - New Product Campaigns are "optimized full-funnel media plans… during the first 90 days of launch". [official] *How to create your new product launch strategy*
  - The announcement asks "how can a brand make an impact during the critical first 90 days?" The media mix "is optimally flighted over 30, 60, and 90-days". The service is managed by Amazon Ads ("contact an Amazon Ads account manager"). Its figures (for human readers only): "4x more glance views and sell 39% faster", and "at least 22% higher click-through rates" for new and notable creative. On this page the footnote markers on those two figures read 1 and 2, which the source list gives as Boston Consulting Group and an eMarketing/Jungle Scout report; the Amazon internal data notes are footnotes 3–5. The numbering looks mismatched, so the page does not cleanly say which source backs which figure. [official] *Amazon Ads introduces New Product Campaigns*, https://advertising.amazon.com/library/news/introducing-new-product-campaigns-from-amazon-ads (dated January 1, 2025, by Jennifer Vargas)
  - The launch announcement is a separate page: "Introducing new product campaigns from Amazon Ads, now generally available in the U.S. October 15, 2024 Announced at unBoxed 2024", "within the crucial first 90 days of launch", "This managed service provides data-driven media plans". [official] *Launch announcement: Introducing new product campaigns from Amazon Ads*, https://advertising.amazon.com/resources/whats-new/introducing-new-product-campaigns-from-amazon-ads
  - "New & Notable is a designation for products new to market in the last 12 months, subject to eligibility." [official] same page. *How to create your new product launch strategy* words it as "a creative identifier for products new to market in the last 12 months, subject to Amazon Ads' policies, eligibility, and restrictions".
  - "Engagement at the beginning of a product's launch… can help drive traffic, sales, and reviews". [official] *A product advertising strategy*
- Amazon's own systems do mark newness, as fields:
  - `createdDate` ("Date the item was first available on Amazon") on Product Selector (C);
  - the Tactical Recommendations grouping `NEW_ASIN`: "Recommendation grouping type for unadvertised ASINs that have recently been added to the catalog". [official] Recommendations OpenAPI, `Recommendations_prod_3p.json`. The spec gives no number of days for "recently".
- The plainest Amazon statement of cold start is in the Review Requests overview: "New products face a cold-start problem… It gives new products a faster path to authentic reviews." [official] Ads API guide *Review requests overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/review-requests/overview.md
- Amazon's research and patents describe cold-start mechanisms in search ranking. They are recorded under *Published research*, because neither a paper nor a patent is a statement of what runs in production.

### J. Reviews at launch: Vine, Review Requests, and the review rules ads meet

- Vine: see D6. The FBA New Selection Vine credit is in D7.
- RULE (Review Requests, beta, US): a Sponsored Products variant whose click is a review. [official] Ads API guides *Review requests: get started*, *overview* and *FAQ* (`guides/review-requests/…`); release note "November 16, 2026" in *All releases*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md
  - The campaign has `adProduct` SPONSORED_PRODUCTS and `optimizations.goalSettings.goal` ENGAGEMENT, which cannot be changed afterward. The bid strategy is MANUAL, and `autoCreateTargets` is false.
  - The target is THEME with INTERESTED_AUDIENCE. Keyword and product targets are not supported.
  - The ad has `adType` COMPONENT, with `creative.componentCreative.customerActionSettings` of `customerActionType` REVIEW_REQUEST and the product as `{productIdType: ASIN, productId}`.
  - It is billed CPC, where the billable click is a rating or review left on the card.
  - It is for products with fewer than 1,000 total reviews, and ads pause automatically at 1,000.
  - Queries need `goalFilter` ENGAGEMENT. Review-specific metrics are in the console only for now; the reporting API "returns the standard delivery metrics (impressions, clicks, click-through rate, spend, cost-per-click)" for these campaigns.
  - "During the beta, Review Requests is enabled per advertiser account. A request to create a Review Requests campaign for an account that is not yet enabled returns an error." [official] *Get started with Review Requests*.
  - The v1 `Goal` enum defines ENGAGEMENT as "customer engagement actions beyond product purchase, such as review requests or follows. Used by Sponsored Actions campaigns". [official] v1 merged OpenAPI
  - [seat] The release note is dated a week after this read. The guides are public and describe a beta. Whether an account can create one today is read from the API's response, not assumed.
- RULE (review sharing across variations): "Reviews are only shared when product variations have minor differences that don't impact the product's core functionality". [official, via capture] *Guidelines for reviews shared across product variations*, G74DLBUEHT5GY88C v3. The capture was made on 2026-10-14 by the listing-playbook seat, not re-read here.
  - Canopy reports that the narrowing rolled out between February 12 and May 31, 2026 (see practitioners).
  - [seat] For a launch this decides whether a new child ASIN arrives with its family's reviews or with none.
- RULE (coupons and the Verified Purchase badge): reviews from coupon purchases "may not always get the Amazon Verified Purchase badge". [official, via capture] *Coupon eligibility criteria*, GJHCPEFJ5JJQD52D v14 (listing-playbook capture, 2026-10-14)
- RULE (no incentives off Amazon): the 2021 policy clarification on the Amazon Seller Forums. [official] *Clarification of Amazon's Policy on Rebates, Coupons, and other Marketing Incentives*, https://sellercentral.amazon.com/seller-forums/discussions/t/5625a806dcc896ccc7d434751a65c07f
  - "we consider it a violation of the Amazon Seller Code of Conduct if off-Amazon rebates, discounts, and other schemes are designed to drive customers to products that are listed and sold without those incentives on Amazon."
  - "it is a violation of the Amazon Seller Code of Conduct to manipulate search rank to artificially boost your products' search ranking, including through 'two-step urls,' 'super urls,' 'funnels,' 'treasure hunts,' 'search-find-buy,' and any other form of false or misleading behavior. A service by any name that's intended to artificially boost search ranking or portray a discounted sale as full-price, is a violation."
  - "you are responsible for the actions taken by your account, even those handled through third-party service providers."
  - Coupons, discounts and deals are welcome "only when those incentives are part of the product offer made in our store".
  - Practitioners date this post to November 2021.
- A seller asks, in the replies to Amazon's 30-day roadmap post, whether "Amazon's review deprecation is still planned" and whether launching with Vine still makes sense. [opinion, a seller] The post this seat read has no Amazon answer to the question. See Open questions.

### K. Coupons, deals and promotions, and how they meet ads

- RULE (coupon eligibility). [official, via capture] *Coupon eligibility criteria*, GJHCPEFJ5JJQD52D v14 (listing-playbook capture, 2026-10-14)
  - "you must be a Professional seller with at least a 3.5 Seller feedback rating"; "Sellers who haven't received any feedback rating yet are also eligible".
  - "Products with 1-4 reviews must have an average rating of at least 2.5 stars." "Products with 5+ reviews must have an average rating of at least 3 stars."
  - "Product discounts must be at least 5% below the Was Price or List Price".
  - The full guide PDF adds: "Coupon quality validation rules do not apply to new products". [official] *New product success* full guide PDF
  - [seat] A product with no reviews is therefore not barred from coupons by the review rule as captured. This is the one promotion a zero-review launch can use, and it carries the coupon credits in D1 and D7.
- RULE (deal eligibility). [official, via capture] *Amazon deals*, G202111490 v25 (listing-playbook capture, 2026-10-14)
  - "To be eligible for deals, you must be a Professional seller with an overall rating of at least 3.5 stars".
  - "Products must have a sales history on Amazon and at least a 4-star rating".
  - "Amazon Deals is an invite-only program"; "Eligible ASINs are refreshed every week".
  - [seat] A day-one ASIN cannot run a deal: it has no sales history and no rating.
  - The sell.amazon.com blog *Guide to running Amazon seller promotions, deals, coupons, and discounts* (Mickey Toogood, May 27, 2026) says "You'll need a Professional selling plan and an overall rating of at least four stars to create deals" and, for coupons, "an overall rating of at least 3.5 stars". [official] https://sell.amazon.com/blog/seller-promotions (served 200 on 2026-11-09). [seat] For deals the blog's "overall rating of at least four stars" sits on the seller, while the captured help page puts 3.5 on the seller and 4 stars on the product; the two Amazon pages do not word the deal floor the same way.
- RULE (where coupons show): coupons "appear on product detail pages", and "Customers can also find coupons through search results, on the Amazon Deals page, and on products they've added to their carts". "All coupons expire after 90 days", and a coupon can hold up to 200 ASINs. [official] *Guide to running Amazon seller promotions, coupons, and deals*
  - No Amazon page this seat read says, in so many words, that the coupon badge renders inside a Sponsored Products ad. Ad Badger says it does (see practitioners). For display, the Responsive eCommerce Creatives spec says the eCommerce section is "auto-generated by Amazon with live pricing, deal badges, coupons, star ratings, and Prime eligibility pulled from your product listing", that "Coupons — savings percentage with coupon" is surfaced automatically, that "If a product has multiple active discounts, the highest value is shown", and that "Inactive coupons are removed from the optimization pool". [official] *eCommerce display creatives - Guidelines & ad specs*, https://advertising.amazon.com/resources/ad-specs/ecommerce (the older https://advertising.amazon.com/ad-specs/en/ecommerce returns 404)
- RULE (fees, for human readers only): the deal fees are a $70-a-day upfront fee plus 1.0% of sales (capped at $2,000) off-peak, and $100 per promotion plus 1.5% (capped at $5,000) at the 2026 peak events. The Prime Day Prime Member Coupon is "$5 per coupon plus 2.5% of sales". [official, via capture] *Understand deal fees*, G202111590 v27, and *Prime Day readiness playbook*, GM2ADTH3XH3A5N57 v4 (listing-playbook captures, 2026-10-14). Deal calendars are owned by `seasons-and-deals.md`.
- GUIDANCE (advertise the promoted product): for upcoming deals within two weeks, advertise the product. "Products with deals or coupons that were advertised with Sponsored Products saw an average 65% increase in sales and 75% increase in units sold". [official] *A product advertising strategy* (Amazon internal data, WW, 2023, ad-attributed). The same guide recommends advertising excess inventory (+67% units after four weeks) and grouping similar products in an ad group (+6% units). For human readers only.
- RULE (Tactical Recommendations): the groupings include `IN_SEASON_ASIN`, `INCREASE_CONVERSION_RATE` ("ASINs that have low conversion rate compared to benchmarks") and `NEW_CAMPAIGN_*`, besides `NEW_ASIN`. The `AsinContext` carries `trailing4WeeksConversionRate` and `trailing4WeeksClickthroughRate`, defined as the "Past 4 weeks conversion rate of target product type" (a product-type benchmark, not the ASIN's own rate), plus `seasonStartDate` and `seasonEndDate`. [official] Recommendations OpenAPI. These are Amazon's own launch-adjacent prompts; `beyond/automation-and-amazon-tools.md` owns how they are applied.

### L. Organic rank: what Amazon says, and does not say

- Amazon's ads pages connect launch advertising to organic visibility in soft terms only:
  - "increasing visibility and glance views to help boost organic rankings" (*Intermediate and advanced new ASIN playbook*, about single product video ads);
  - "By driving traffic, these ads can help increase detail page views and product reviews" (*How to create your new product launch strategy*);
  - "Reviews also make your new products more discoverable in the Amazon store" (*New product success* full guide PDF);
  - Best Seller Rank (BSR) "indicates how a product is selling relative to similar products", and "There are a number of ways you can improve BSR. For example, customer reviews can be a form of social proof" (*5 steps to launch a product successfully*).
- No Amazon page read here says that an ad-attributed sale counts toward organic search rank, or by how much. No Amazon page says that ads speed up indexing.
- What Amazon does prohibit is manufacturing search signals (J, the 2021 clarification).
- The organic-and-total question in general is owned by `ads-organic-and-total.md`. This file records only the launch-specific statements above and the research in *Published research*.

### M. The launch timeline in Amazon's own words

Amazon's guidance contains these time marks. Each is a recommendation unless marked RULE.

| When | What Amazon says | Source |
|---|---|---|
| ≥3 weeks before launch | Enroll in Vine with inventory available | *Amazon Vine \| Sell on Amazon* |
| Prelaunch | Complete the checklist, including "Build a Sponsored Products ad campaign", to qualify for complimentary placements | *30 days to new product success* quick guide |
| Day 1 | Listing active with stock; launch Sponsored Products; create coupons | 30-day roadmap forum post |
| Day 0 | Run immediately, no end date, automatic targeting | *New advertiser success guide*; getting-started guide |
| Day 0 | RULE: start date today means serving immediately | API *auto campaigns* |
| Within 60 days of a buyable offer | RULE: Vine enrollment for the FBA New Selection Vine credit | *What is the FBA New Selection program?* |
| Within 90 days of listing | RULE: first SP campaign for the new-seller credit; coupon for the coupon credit; first FBA shipment for FBA New Selection | *New Seller Incentives*; 2024 terms; FBA New Selection |
| Within 30 days of the first campaign | RULE: the spend that earns the credit; credit lands within 14 days after the window | 2024 terms |
| First week | "monitor your metrics at least twice a week" | *Best practices for your Sponsored Products ads* |
| ~2 weeks | Let auto run before creating manual | *A guide to targeting with Sponsored Products* |
| 1–2 weeks | Test match types before pausing keywords | same |
| ≥20 clicks | Evaluate a keyword before adding it as a negative | same |
| ≥2 weeks after adding negatives | Let negatives run before changing strategy | same |
| ≥10 days and ≥10 conversions in 30 days | RULE: rule-based bidding becomes available | API *rule-based bidding overview* |
| Every 2 weeks | Review reports (international) | *Checklist for new international ad campaigns* |
| Day 30 | Read reviews; adjust inventory and advertising to demand | 30-day roadmap forum post |
| 30 days | The seller-quoted "honeymoon" | *Tips for new product success* |
| First month | Upper-funnel tactics (Amazon's correlational figure) | *How to create your new product launch strategy* |
| 30/60/90 days | New Product Campaigns flighting | New Product Campaigns announcement |
| 13 weeks | Sponsored Brands figure | *Intermediate and advanced new ASIN playbook* |
| 120 days | FBA New Selection storage waivers end | *What is the FBA New Selection program?* |
| 12 months | New & Notable designation | New Product Campaigns announcement |

The negation marks are quoted from *A guide to targeting with Sponsored Products*: "Before deciding to add a keyword as a negative target, we recommend evaluating its performance after it has received at least 20 clicks", and "let your negative keywords run for two weeks or more, before making any changes to your strategy". The two weeks is about negatives already added, not a wait before negating. The match-type and negative mechanics are owned by `search-terms-and-negatives.md`.

### N. Amazon Ads Agent and Amazon's recommendations at launch

- "Amazon Ads Agent" is the name Amazon gave, at unBoxed 2026 (2026-09-29), to its unified advertising console. Amazon's help and guide pages now say "Amazon Ads Agent" where they used to name the console, for example "Review optimization recommendations regularly. Log into Amazon Ads Agent" (*A guide to targeting with Sponsored Products*) and "go to the advertising tab in Amazon Ads Agent" (getting-started guide). [official] *Amazon Ads Agent*, https://advertising.amazon.com/library/news/amazon-ads-agent; *unBoxed 2026 news and announcements*, https://advertising.amazon.com/library/news/unboxed-2026-news-announcements
  - The announcement promises "AI-powered guidance for sponsored ads" that advertisers can "apply them in one click", and "All of these capabilities will roll out over the coming months".
  - The Ads Agent announcement (2026-09-29) defines Amazon Ads Agent as "the new name of the unified platform, now powered by agentic AI", and says "Full-Funnel Campaigns is now available to all advertisers in the United States". The unBoxed recap (*The 11 biggest takeaways from unBoxed 2026*, 2026-09-30) gives the beta figures (for human readers only): "Beta testers saw 67% higher long-term return on ad spend and 29% lower cost to acquire new-to-brand customers".
- RULE (API recommendations): Tactical Recommendations 3.0 (`POST /recommendations/list`, `/recommendations/apply`, `PUT /recommendations/{id}`), and the v1 forms `GET /adsApi/v1/recommendations` and `POST /adsApi/v1/query/recommendations`. [official] Recommendations OpenAPI; v1 merged OpenAPI
  - The `NEW_ASIN` grouping ("unadvertised ASINs that have recently been added to the catalog") is how Amazon itself flags a new ASIN for a proposal. The `RecommendationType` enum includes NEW_CAMPAIGN, NEW_PRODUCT_AD and NEW_KEYWORD; the spec does not say which types a `NEW_ASIN` recommendation carries.
  - `GET|POST /sp/campaign/recommendations` gives "top consolidated recommendations across bid, budget, targeting… refreshed everyday". [official] Sponsored Products 3.0 OpenAPI
- RULE (campaign autonomy flag): the v1 campaign's `autoCreationSettings` holds `autoManageCampaign`, the "Flag that allows Amazon to manage the lifecycle of your Campaign", beside `autoCreateTargets` ("Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised"). [official] v1 merged OpenAPI. What it changes is owned by `beyond/automation-and-amazon-tools.md`.

### O. Amazon's own launch figures, collected

For human readers only. The figures are Amazon's own claims, nearly all footnoted as Amazon internal data and mostly ad-attributed; none is an experiment published with its method. Two exceptions in sourcing: the New Product Campaigns page's footnote markers point to non-Amazon sources (see I), and the 24.5% is Amazon's 2022 analysis of Amazon Attribution clicks. The sources are cited at their first mention above.

| Figure | Page |
|---|---|
| New products 36x more clicks when advertised, compared to products that are not new (WW 2023) | *A product advertising strategy* |
| New products 231x more likely to get ad-attributed sales when advertised, compared to products that are not new (WW 3/26/23–4/1/23); suggested products 321x compared to products not suggested (WW Dec 2021–May 2023, sellers with ≥6 months of SP campaigns) | *Best practices for your Sponsored Products ads* |
| Suggested products 260x more sales when advertised, compared to products not suggested | *Advertising \| Sell on Amazon* |
| Advertised deals or coupons +65% sales, +75% units, compared to when the same deal or coupon product was not advertised | *A product advertising strategy* |
| SP adopters +34% sales growth after four weeks | *Advertising \| Sell on Amazon* |
| Upper funnel in month one: +36% conversion rate (US Aug 2023–2024) | *How to create your new product launch strategy* |
| New and notable creative: ≥22% CTR | same; New Product Campaigns announcement |
| New Product Campaigns-like mix: 4x glance views, sell 39% faster | New Product Campaigns announcement |
| SB brand owners +23% sales after 13 weeks (Jan 2025) | *Intermediate and advanced new ASIN playbook* |
| Shipping, A+, Vine, coupons and SP together: up to 85% more likely early sales (new items' first 90 days, 2024) | *New product success* full guide PDF |
| Vine: average +30% sales | *Amazon Vine \| Sell on Amazon* |
| External traffic: +24.5% additional sales (2022) | *30 days to new product success* quick guide |
| New Seller Guide users in their first 90 days ~6x first-year sales (FY2023, US) | *5 steps to launch a product successfully* |

### P. Building the first campaign through the door: the create sequence, and what a partial failure leaves

A launch's first write is a chain of separate calls. The door carries each one as written (`cx raw amazon-ads --method POST --path …`). Amazon offers no call that creates the whole chain on the Ads API hosts. Endpoint lists, headers and write semantics in general are owned by `method/ads-api-surface.md` (its section F); this section records the launch case. All sources below were read 2026-11-09.

**P1. The entities and their order.**
- RULE: "Creating Sponsored Products campaigns using the Amazon Ads API requires making multiple calls to create the entities that make up a campaign." "Both manual and auto campaigns require you to create, at minimum, campaigns, ad groups, and product ads". A manual campaign "must also include at least one product targeting expression or keyword in each ad group". Both kinds "can also contain negative product targeting expressions or negative keywords at the campaign level (in addition to the ad group level)". [official] Ads API guide *Sponsored Products campaign structure*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/campaign-structure.md
- RULE: each step needs an id the step before returned. "To create an ad group, you must first create a campaign to get the `campaignId`." [official] Ads API guide *Sponsored Products ad groups*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/ad-groups.md. "To create a product ad, you must include `adGroupId`, `asin` (vendors and KDP authors) or `sku` (sellers), and `state`." [official] Ads API guide *Sponsored Products product ads*
- RULE (the manual sequence, in Amazon's steps): (1) `POST /adsApi/v1/create/campaigns` with `autoCreateTargets` false; (2) "Create at least one ad group" with `POST /adsApi/v1/create/adGroups`; (3) "Create at least one product ad per ad group" with `POST /adsApi/v1/create/ads`; (4) "Ad groups for manual campaigns must have at least one associated targeting expression (product or category) or keyword", created with `POST /adsApi/v1/create/targets`; (5) "(Optional) Set up negative targeting… All negative targets are also created through the targets API… by setting the `negative` field to `true`." Then: "Once you have created at least one active campaign, ad group, product ad, and targeting expression or keyword, your campaign is considered complete and ready to run. If the campaign start date is set to today and all entities have an `ACTIVE` status, your campaign starts serving immediately." [official] Ads API guide *Get started with manual campaigns*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/manual-campaigns.md
  - The guide's step 4 also places reads between the writes: product and category recommendations, `POST /sp/targets/products/count` for a refined category's size, bid recommendations, and keyword recommendations.
- RULE (the auto sequence): the same first three steps with `autoCreateTargets` true; then "(Optional) Set up auto targeting using the `PUT /adsApi/v1/update/targets` endpoint", with the auto target ids read from `POST /adsApi/v1/query/targets`; then optional negatives. "Once you have created at least one active campaign, ad group, and product ad, your campaign is considered complete and ready to run. If the campaign start date is set to today, your campaign starts serving immediately." [official] Ads API guide *Get started with auto campaigns*. The guide's step 4 names the update operation `PUT`, while the SP v1 model lists `/adsApi/v1/update/targets` only as a `POST`.
  - [seat] On Amazon's own wording, an auto campaign is complete, and serves on a start date of today, once its product ad exists. Negatives sent after that step reach a campaign that may already be serving.

**P2. The v1 request shapes (Sponsored Products).** [official] Amazon Ads API v1, Sponsored Products model, `AmazonAdsAPISP_prod_3p.json`, and the guides named.
- Campaign (`SPCampaignCreate`): required `adProduct`, `autoCreationSettings`, `budgets` (exactly one item), `marketplaceScope`, `name`, `startDateTime` and `state`. Optional `endDateTime`, `countries`, `marketplaces`, `optimizations` (bid strategy and placement adjustments), `portfolioId`, `siteRestrictions` and `tags`.
- Ad group (`SPAdGroupCreate`): required `adProduct`, `bid` (`defaultBid`), `campaignId`, `name` and `state`. "Ad group names must be unique within a campaign, but you can use the same ad group name in different campaigns." The default bid "applies to all child entities… if you do not define bids for the child entities explicitly". (*Sponsored Products ad groups*.)
- Ad (`SPAdCreate`): required `adGroupId`, `adProduct`, `adType` (`PRODUCT_AD`), `creative` and `state`; the product is `creative.productCreative.productCreativeSettings.advertisedProduct` with `productIdType` `SKU` for a seller and `ASIN` for a vendor. "Each product ad is associated to a single product, either by `SKU` (sellers) or `ASIN` (vendors and authors)." A seller who knows only the ASIN can read the SKU from Product Selector's product metadata endpoint. (*Sponsored Products product ads*.)
- Target (`SPTargetCreate`): required `adProduct`, `negative`, `state`, `targetDetails` and `targetType` (`KEYWORD`, `LOCATION`, `PRODUCT`, `PRODUCT_CATEGORY` or `THEME`); `adGroupId` is "Only used for ad-group level targets" and `campaignId` "Only used for campaign-level targets". A keyword is `targetDetails.keywordTarget {keyword, matchType}`. Campaign-level negatives apply "to all ad groups created under that specific campaign"; ad-group-level ones "only… to that specific ad group". [official] Ads API guide *Negative keyword targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/keywords.md
- States at create: `SPCreateState` is `ENABLED` or `PAUSED`; a read can also return `ARCHIVED`.
- Each create request holds 1 to 1,000 items of one entity type, and the reply is `207` with `success[]` and `error[]`, each item carrying its `index` in the request (the cross-product model adds `partialSuccess[]`; `method/ads-api-surface.md` section F). One call cannot mix a campaign with its ad group: the ad group needs the campaign's id.
- The create operations take three header parameters (account id, client id, scope) and a JSON body. No idempotency key and no client token appear on them; this matches `method/ads-api-surface.md` (P-ads-api-surface-18), re-checked here on the SP v1 model.

**P3. The SP 3.0 sequence.** [official] Sponsored Products 3.0 OpenAPI, `SponsoredProducts_prod_3p.json`
- `POST /sp/campaigns` (`application/vnd.spCampaign.v3+json`; required `budget`, `name`, `state` and `targetingType` `AUTO` or `MANUAL`; `startDate` "Default: today's date"); `POST /sp/adGroups` (`application/vnd.spAdGroup.v3+json`); `POST /sp/productAds` (`application/vnd.spProductAd.v3+json`; required `adGroupId`, `campaignId` and `state`; `sku` is "Defined for seller accounts only" and `asin` "Defined for vendors only"); `POST /sp/keywords` (`application/vnd.spKeyword.v3+json`; required `adGroupId`, `campaignId`, `keywordText`, `matchType` and `state`); `POST /sp/targets` (`application/vnd.spTargetingClause.v3+json`); and for negatives `POST /sp/negativeKeywords`, `/sp/campaignNegativeKeywords`, `/sp/negativeTargets` and `/sp/campaignNegativeTargets`.
- Each takes up to 1,000 items and answers `207` with the results under the plural entity name.
- Unlike v1, SP 3.0 splits keywords, product targets and the four negative kinds into separate paths, and its product ad also needs the `campaignId`.
- States at create: `SponsoredProductsCreateOrUpdateEntityState` is `ENABLED`, `PAUSED` or `PROPOSED`, and the read-state table describes `PROPOSED` as "Proposed State (Upcoming Feature)" and `ENABLING` and `USER_DELETED` as "State for Draft Entity Only". No guide read describes an API draft that holds a whole campaign until it is submitted.
- The console has such a draft. "Draft: This means you started building a campaign and haven't submitted it. Make sure you've completed all steps in the campaign creation process and click Submit for review." [official] *Troubleshoot your campaign status* (help GEC8BVH43CU9UNYH), https://advertising.amazon.com/help/GEC8BVH43CU9UNYH

**P4. What a half-built campaign looks like to the API.**
- RULE: the SP 3.0 serving status enums carry `CAMPAIGN_INCOMPLETE` (campaign), `AD_GROUP_INCOMPLETE` and `CAMPAIGN_INCOMPLETE` (ad group), with the reasons `CAMPAIGN_INCOMPLETE_DETAIL` and `AD_GROUP_INCOMPLETE_DETAIL`, which also appear among an ad's serving status reasons. The v1 `deliveryReasons` enum carries `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE`. Neither model describes these values. [official] Sponsored Products 3.0 OpenAPI (`SponsoredProductsCampaignServingStatus`, `SponsoredProductsAdGroupServingStatus`, the `…ServingStatusReason` enums); v1 merged and SP v1 models (`DeliveryReason`, `SPDeliveryReason`). `diagnosis.md` owns their reading.
- RULE: no transaction ties the calls. Each call commits on its own, and its reply reports success or error per item (P2). No operation on the Ads API hosts rolls back an earlier call. Amazon's end states are `ARCHIVED` through the delete operations, and "Archived" is final (`method/ads-api-surface.md` section F).
- [seat] The partial results a chain can leave, read from the rules above:
  - Campaign written, ad group refused or never sent: a campaign with no ad group, no ad and nothing that can serve or spend; an `ENABLED` campaign in this state is expected to read `CAMPAIGN_INCOMPLETE`. A seller's campaign names are unique per account, so re-running the chain from its first step meets `NAME_NOT_UNIQUE` (SP 3.0) or `FIELD_VALUE_NOT_UNIQUE` (v1) on the campaign (`method/ads-api-surface.md` section F). A vendor's same-name re-run creates a second campaign.
  - Ad group written, product ad refused (for example `PRODUCT_INELIGIBLE` in v1, or a SKU not in the profile): an ad group with no ad, `AD_GROUP_INCOMPLETE`.
  - Manual ad group with ads, targets refused: by the guide's rule, a manual ad group with no target is not complete.
  - Auto campaign complete, negatives refused or not yet sent: a campaign that serves on a start date of today without its exclusions, and spends on the terms the negatives were meant to stop. This is the only partial result in the list that spends.
  - Some items of a batch refused: the campaign serves on the subset that was written; the refused items are named by `index` in `error[]`.
  - A reply lost after the request left (the door reads such a `POST` as `sent, outcome unknown`): the entity may exist. Re-sending can create a second ad group under another name, a second ad or a second target, unless Amazon refuses it as a duplicate. The models carry duplicate reasons (`DUPLICATE_VALUE` in SP 3.0; `FIELD_VALUE_NOT_UNIQUE`, `DUPLICATE_FIELD_VALUE_FOUND` and `DUPLICATE_RESOURCE_ID_FOUND` in v1), but no page read says which fields of an ad or a target are checked for duplicates. The query operations (`POST /adsApi/v1/query/campaigns`, `…/adGroups`, `…/ads`, `…/targets`, filtered by the parent id) show what exists.
  - The guides' example replies show `"deliveryStatus": "DELIVERING"` on a campaign and on an ad group just created, before any ad exists. These are example values. On the guides' own completeness rule, a create reply's status does not show that the chain is complete.
- RULE: both models accept `PAUSED` at create, and a campaign's state is changed later by its update operation. A campaign created `PAUSED` serves nothing until it is enabled, whatever its children's state. [official] SP v1 `SPCreateState`; SP 3.0 `SponsoredProductsCreateOrUpdateEntityState`; *Get started with manual campaigns* ("all entities have an `ACTIVE` status").

**P5. The MCP server's single-shot tool, which the door does not reach.**
- RULE: the Amazon Ads MCP server's `create_singleshot_sp_campaign` "Creates a complete Sponsored Products campaign (campaign + ad group + ads) across multiple marketplaces in a single operation. Supports both AUTO targeting (default) and MANUAL targeting with explicit targets. Use autoCreateTargets=false with a target field to create a MANUAL campaign. Creates ONE global campaign with country-specific budgets and ASINs, not separate campaigns per country." [official] MCP tool specification `campaign_management.json`, https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/campaign_management.json
  - Its input: `accessRequestedAccount` (an `advertiserAccountId` or a `profileId`); `oneshotCampaigns` with exactly one item (minItems 1, maxItems 1), "Each creates campaign + ad group + ads"; required `marketplaces`, `budgets` (per-marketplace daily `monetaryBudget`), `bid` (per-marketplace `defaultBid`) and `creative` (`advertisedProduct` with `productIdType` enum `ASIN` only, and a per-marketplace `productId`); optional `campaignName` ("Default: SP|Auto|Campaign [timestamp]"), `adGroupName` ("Default: SP|Auto|AdGroup [timestamp]"), `startDateTime` ("Default: current timestamp"), `portfolioId`, `autoCreateTargets` ("Defaults to true") and `target`, a single object "Required when autoCreateTargets is false".
  - The tool's `target.themeTarget.matchType` enum is the five `KEYWORDS_RELATED_TO_*` themes (brand, product category, peer brands' product category, gifts, Prime Day); the four auto expressions are not in it.
  - The specification has no `state` field and no response schema for the tool, and does not say what is left behind if a step inside the operation fails.
  - The tool's `advertisedProduct` takes only `ASIN`, while the same specification's product target says "For sellers in Sponsored Products, SKU is used instead of ASIN", and the REST guide says a seller's product ad uses a SKU. The specification does not reconcile these.
- RULE (the release note): "The single-shot campaign creation tool enables developers to create a complete advertisement—encompassing the campaign, ad group, ad, and targeting—in one call, eliminating what previously required five or more separate operations." [official] *All releases*, "Amazon Ads Model Context Protocol (MCP) Server Now in Open Beta", February 18, 2026
- RULE (where it lives): the MCP endpoints are `https://advertising-ai.amazon.com/mcp`, `https://advertising-ai-eu.amazon.com/mcp` and `https://advertising-ai-fe.amazon.com/mcp`. [official] *Connecting to the Amazon Ads MCP Server*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/get-started.md. The `cx-amazon-ads` door's origins are the three `advertising-api*` hosts (its SKILL.md), so the door cannot call this tool. Through the door, a campaign is built by the sequence in P1–P3.
- [seat] The tool is one call to the caller. Whether Amazon makes it atomic behind that call is not stated. A failure inside it may leave the same partial results as P4, and nothing in the specification says otherwise.
- Field reports: a search of the public `amzn/ads-advanced-tools-docs` issue tracker for "singleshot" and "create_singleshot_sp_campaign" (2026-11-09) returned no issues. Later searches were refused by GitHub's anonymous rate limit.

## What practitioners add

Everything in this section is [opinion], attributed to the person or firm who says it. Practitioners share one premise that Amazon's pages state only softly: a launch's advertising is judged by visibility, data and reviews more than by ACOS. They disagree on most of the specifics.

### The honeymoon question

- **Origin.** Seller Sessions (host Danny McMillan) describes Anthony Lee as "the innovator behind the term "honeymoon period" in the world of Amazon FBA". The episode is about "the history of this ranking strategy, clarifying misconceptions". [opinion] *Seller Sessions – The Man Behind the Honeymoon*, https://sellersessions.libsyn.com/seller-sessions-the-man-behind-the-honeymoon
  - The Best at Amazon newsletter says the honeymoon "is a myth and is not supported by scientific evidence", and that Lee, "who initially coined the term in 2015, has since dismissed the idea". [opinion] Best at Amazon (anonymous author, self-described former Amazon marketplace leader), *Doomed from the (Cold) Start*, about October 2024, https://bestatamazon.kit.com/posts/doomed-from-the-cold-start-what-you-need-to-know-about-launching-products-in-2024-and-beyond
  - The Seller Sessions episode *The Cold Reality of the Honeymoon Period & External Traffic Part 1* (Sep 5, 2024) says the observation was "by Anthony Lee in 2015, which he himself… denounced using scientific literature", and that the companion article cites "15 scientific papers and 2 patents". [opinion] https://sellersessions.libsyn.com/the-cold-reality-of-the-honeymoon-period-external-traffic-part-1
- **It exists, length unknown.** Helium 10 (Jonathan Dean, 2018) says "Amazon tends to favor new products by giving them a 'honeymoon' period during which the sellers are able to give less than normal units out to get to page 1". It adds: "We don't know exactly how long this honeymoon period is". [opinion] *Are Amazon product launches still valid?*, https://www.helium10.com/blog/amazon-product-launches-valid/
  - The same 2018 article describes giveaway launches through coupons, launch services and keyword-specific search links. The 2021 clarification (J) now prohibits these. The article is history, recorded so that a reader can recognise the tactic.
- **15–30 days, a by-product of the algorithm.** My Amazon Guy (Steven Pope, 2021) says the honeymoon "was not created intentionally" and is "a by-product of how their algorithm works". It is "Typically 15 – 30 days long", and he says to "start running PPC ads immediately after a product launch". [opinion] *Is there an Amazon honeymoon period…*, https://myamazonguy.com/is-there-an-amazon-honeymoon-period-and-how-do-i-grow-sales-fast/
- **A search-term-level chance, a couple of weeks.** m19 says "the Amazon algorithm gives a chance to any new product… at the search term level". The period "lasts a couple of weeks and it is impossible to know exactly its duration. It is not a hardcoded duration". [opinion] m19, *A blueprint for launching new products on Amazon with sponsored product ads*, https://www.m19.com/blog/a-blueprint-for-launching-new-products-on-amazon-with-sponsored-product-ads
  - The same post names three ways to signal relevance: listing keywords, PPC, and "search-find-buy on these keywords". [seat] The 2021 clarification (J) names "search-find-buy" as a violation of the Seller Code of Conduct.
- **The cold-start system replaces the honeymoon.** Code3 bases its reading on a Seller Sessions article and Amazon's patents, and says the "Cold Start" system "debunks the previously assumed 'Honeymoon Period' theory". [opinion] Code3, *Honeymoon Period Decoded: The Truth Behind Amazon's Cold-Start Algorithm*, https://code3.com/resources/honeymoon-period-decoded-the-truth-behind-amazons-cold-start-algorithm/
  - It claims that "Starting as soon as five days after a product is purchasable, Amazon incorporates posterior estimation values", and that visibility "within the first 90 days keeps the product eligible for cold start adjustments". It also says that "Early advertising efforts can help drive this traffic and expedite the transition from estimated to real performance-based rankings".
  - [seat] The five-day figure is not in the patent text this seat read, which gives "for example, three days" and "such as ninety days" (see *Published research*).
- **Exploration that can end early.** Best at Amazon summarises Danny McMillan and Oana Padurariu, *The Cold Reality of the Honeymoon Period and External Traffic*. It reads the patents as a three-day transition inside a 90-day window, with "spearfishing" queries. Its advice: "Prioritize early advertising… ready to launch as soon as your product listing is active". It cautions on external traffic. [opinion] Best at Amazon (as above)
- **Not planned around.** Canopy Management (Chuck Kessler): "Amazon has never confirmed one, and we don't plan launches around it." [opinion] *Amazon Product Launch Playbook: The First 90 Days of a New ASIN*, published 2026-10-01 and modified 2026-10-27, https://canopymanagement.com/amazon-product-launch-playbook/
- **Disagreement.** The claims range from 15–30 days (My Amazon Guy) and "a couple of weeks" (m19) to "a myth" (Best at Amazon), "debunks" with a posterior from about five days (Code3), and "Amazon has never confirmed one" (Canopy). What they agree on is that a new ASIN's early performance matters more than the same performance later. That shared claim matches the Amazon research on cold-start priors and early stopping, but not any stated duration.

### Structure at launch

- **Canopy's three layers.** [opinion] Canopy (as above)
  - Exploration:
    - auto;
    - broad match with 5–12 keywords;
    - product targeting on 10–20 competitor ASINs.
  - Intent capture: exact match, with the same terms negated in the exploration campaigns.
  - Brand presence: Sponsored Brands and Sponsored Display, plus a branded Sponsored Products campaign.
  - It is a 90-day sequence. Month one is reviews (Vine; Request a Review "once per order, between 5 and 30 days after delivery") plus auto discovery. Month two is harvesting and Search Query Performance. Month three lowers bids and watches whether organic holds. "A product that's still dependent on paid traffic at day 90, with complete content and a solid review base, usually has a positioning, price, or product problem."
- **Ad Badger's budget split.** Auto gets 20–30% of the budget for 7–10 days, manual exact and phrase 50–60%, and Sponsored Brands and Display 10–20%. Manual bids are conservative, campaigns are watched daily for 2–3 weeks, and TACoS is the frame. [opinion] Ad Badger ("The Badger"), *The Best Way to Structure Campaigns for a New Product Launch*, 2025-09-18, https://www.adbadger.com/blog/best-way-to-structure-amazon-campaigns-new-product-launch/
- **Destaney Wishon's five campaign jobs.** Wishon (btr media), writing for Helium 10, names five campaign types: Awareness, Rank, Efficiency, Branded and Auto, around "the RIGHT 10 to 20" keywords. [opinion] *How to Launch a Product on Amazon in 2025 With Advertising (Part 1)* (2025-04-24), https://www.helium10.com/blog/how-to-launch-a-product-on-amazon-in-2025-with-advertising/
  - Part 2 (2025-05-06) covers harvesting, looking for "Keywords with poor CVR (especially after 15–20 clicks with no sale)", and reviewing negatives regularly, "especially in the first 30–60 days post-launch". https://www.helium10.com/blog/how-to-launch-a-product-on-amazon-in-2025-with-advertising-part-2/
  - Its account data: "1,408 unique targets drove fewer than 2 orders each but had an average RoAS of $6.70". Its TACoS benchmark: "20-25% – New brands just launching". For human readers only.
- **Auto is not always the first campaign.** Ad Badger reports a method from Destaney Wishon. When Amazon has not yet indexed a new product well, its suggested keywords show it, and an auto campaign will match poorly. The fix is to lead with a broad-match keyword for the core term until indexing improves, then check the suggestions again. [opinion] Ad Badger, *When auto campaigns don't work for new product launch*, 2020-07-22, https://www.adbadger.com/blog/amazon-ppc-education/when-auto-campaigns-dont-work-for-new-product-launch/
  - [seat] Amazon's keyword recommendations for the ASIN (`KEYWORDS_FOR_ASINS`, section G) are the API form of the same check.
- **Narrow first, then widen (ecomcrew).** "In the first few weeks of your launch, you want your PPC targeting to be as narrow (i.e., exact keyword targeting) and with high bids, then gradually widen it to include broad, phrase, auto, and perhaps other ad types". [opinion] ecomcrew (Dave Bryant), *The No B.S. Amazon Product Launch Guide for 2025*, published 2025-01-29, last updated 2025-11-14, https://www.ecomcrew.com/amazon-product-launch-guide/
  - This is the reverse of Amazon's new-advertiser sequence (auto first, then manual).
- **Three phases (SellerSprite).** Phase one is rank and reviews, phase two a controlled transition (about 30 days), and phase three break-even and scale. A launch has its own target ACOS. "Start optimizing after your first sales, then expand your lookback window each week until you reach a stable 60-day routine." "Auto performs better after Amazon has more conversions and keyword data." [opinion] SellerSprite, *Amazon PPC Launch Strategy in 3 Phases*, https://www.sellersprite.com/en/blog/amazon-ppc-launch-strategy
- **Both auto and manual from the start (Seller Labs, 2020).** It recommends both, and to "Let ad campaigns run for at least 14 days before making any adjustments". It also claims that "Amazon is more likely to favor campaigns with bigger budgets". [opinion] Seller Labs (Maria Navolykina), *6 steps to using Amazon PPC for profitable product launches*, 2020-04-14, https://www.sellerlabs.com/blog/6-steps-using-amazon-ppc-profitable-product-launches/
  - [seat] No Amazon source read here supports a budget-size preference in the auction.

### Bids at launch

- **Above the suggestion.** "Bid above Amazon's suggested bid at first." [opinion] Canopy
- **Below it, conservatively.** Ad Badger favours conservative manual bids at launch. [opinion] Ad Badger (as above)
- **Top of search for rank.** Wishon's rank campaigns "push spend more aggressively to secure top-of-search placements and improve organic rank". Her bid-strategy advice: "Use fixed bids when testing or when you want full control. Use dynamic – down only if you want to protect your spend when CVR is low. Use dynamic – up and down when you have strong signals and want to scale faster." "The goal early on is to build momentum, not to be profitable". [opinion] Helium 10, Wishon part 1
- **Fixed-bid ranking campaigns with a daily raise.** Spencer Gordon, a guest on Helium 10's *Serious Sellers Podcast* episode 753 (*The 6 Figure Amazon Launch Sprint*, 2026-06-22, host Bradley Sutton), runs fixed-bid "ranking campaigns". His rule, on seven consecutive rank checks: "if I am not in the top three positions for sponsored I am raising my bid by 10% every day and until I am there", and when "my organic rank is in the top five. I have another criteria to lower my bid by 10% each day". He tests a listing for relevancy, uses "30 vines", and launches at full price, adding a discount "about a month later". [opinion]
- **Force visibility on a few terms.** m19 puts forced visibility on the top three keywords and top three competitor ASINs, and ACOS-target bidding on the rest. Its floor: "at least 5 clicks per day are needed, so for one search term, the monthly expected budget should be around 150$" at a $1 CPC. A launch "shouldn't last more than 4 months". [opinion] m19
- **Tiered automated raises (Scale Insights).** For keywords that convert better than the market (its "Conversion Delta"), Scale Insights describes rules that raise a bid by a fixed amount, for example $0.10, when a campaign has had no impressions over a 7-day observation period, inside a $0.50–$0.99 "Low tier"; if there is still no traffic, the campaign is duplicated into the next tier. [opinion] Scale Insights help, *Set up an AMC campaign system for ranking pressure*, https://help.scaleinsights.com/en/knowledge-base/set-up-an-amc-campaign-system-for-ranking-pressure
- **Disagreement.** On the opening bid relative to Amazon's suggestion, Canopy says above and Ad Badger says conservative. On strategy, Wishon uses up and down when the signals are strong, Amazon's international checklist uses down only, and Spencer uses fixed bids. Amazon's own pages also disagree with each other (G).

### Budgets at launch

- Canopy: a launch budget of about 1.3–1.5x the steady state. ACOS above target is expected. "Set a ceiling and a review date." [opinion]
- ecomcrew: "If it's 15%, then you should be spending upwards of 75% during weeks 1 and 2 of your launch… after 7-12 weeks, you should be pushing toward your long-term TACoS goal." [opinion] Bryant
- m19 sizes the budget from clicks per term (above). [opinion]
- [seat] Amazon's own launch figure is "$10 or equivalent" a day, with an initial-budget recommendation per new campaign (H). The practitioners' figures are multiples of the seller's own steady state or of target TACoS. They do not compare with Amazon's.

### Reviews, Vine and coupons around the ads

- **Review counts.** ecomcrew: "By weeks 3-6, you want to have at least 10 reviews. After about 12 weeks, you want to have at least 30 reviews, and your reviews should be purely organic", with a rating of 4.5 or above. [opinion] Bryant
  - Spencer: "I do 30 vines". [opinion]
  - Canopy: Vine, then Request a Review in the 5–30-day window after delivery. [opinion]
- **Review sharing.** Canopy reports that review sharing across variations narrowed between February 12 and May 31, 2026. It also reports that titles moved to 75 characters from July 27, 2026. [opinion] Canopy. These match the Amazon capture in J for review sharing.
- **Coupon fees.** Canopy and several vendors report that coupons have cost $5 per coupon plus 2.5% of coupon sales since June 2025. [opinion] Canopy. The Prime Day capture in K shows the same structure for the Prime Member Coupon.
- **The coupon badge in ads.** Ad Badger: "Having a coupon gives your product a little green badge that indicates savings to a potential customer. These badges signal a good deal to buyers increasing your click-through-rate (CTR) and conversion rates". It suggests naming the coupon in Sponsored Brands copy ("Save 20% with Coupon"). [opinion] Ad Badger, *How to Use Amazon Coupons to Promote Your Products*, 2024-12-12, https://www.adbadger.com/blog/amazon-coupons/
- **Banned launch tactics.** Canopy lists rebates and super URLs as banned since November 2021, along with review incentives. [opinion] Canopy. This matches the Amazon clarification in J.
  - ecomcrew still writes of giving "away a bunch of products" through services. [opinion] Bryant, 2025. [seat] Whether a giveaway is allowed turns on the clarification's test: the discount must be part of the offer in Amazon's store, and not be presented as a full-price sale.

### Timeline as data accrues

| Mark | Claim | Who |
|---|---|---|
| 7–10 days | Auto discovery window | Ad Badger |
| 2–3 weeks | Daily monitoring | Ad Badger |
| ≥14 days | No adjustments before this | Seller Labs (2020) |
| 15–20 clicks, no sale | Poor-CVR keywords to look for when negating | Wishon (Helium 10) |
| Weeks 1–2 | TACoS up to 5x the long-term target | ecomcrew |
| Weeks 3–6 | ≥10 reviews | ecomcrew |
| ~30 days | Honeymoon end | My Amazon Guy; seller quote on sell.amazon.com |
| ~30 days | Phase 2 length | SellerSprite |
| 30–60 days | Negatives reviewed regularly, especially in this window | Wishon |
| Month 2 | Harvest, Search Query Performance | Canopy |
| 60 days | Stable lookback window | SellerSprite |
| 7–12 weeks | Back toward target TACoS | ecomcrew |
| Month 3 / day 90 | Lower bids, test organic hold; still paid-dependent "usually has a positioning, price, or product problem" | Canopy |
| ≤4 months | End of launch | m19 |

[seat] These marks are practitioners' schedules, not measurements. They are recorded so that a skill can name who holds which view. None of them is a rule.

### Launch as a loop (Jungle Scout with Amazon)

Jungle Scout and Amazon published *The Amazon New Product Success Playbook*: "A repeatable, data-backed framework for launching products on Amazon — built with Amazon and powered by Jungle Scout". It is built around an "Assess-Diagnose-Act loop" run at pre-launch, launch and post-launch. It says "A launch can underperform for a dozen different reasons — weak demand, a crowded category, a pricing problem, an offer that doesn't stand out". [opinion, co-branded with Amazon] Jungle Scout (Sarah Adi), 2026-07-27, https://www.junglescout.com/resources/reports/amazon-new-product-playbook/ (the full playbook is behind a form; only the landing page was read).

## Published research

### Cold start in Amazon product search

- **Empirical Bayes priors for new products.** [research] Han, Castells, Gupta, Xu and Salaka, *Addressing Cold Start in Product Search via Empirical Bayes*, CIKM 2022 (Amazon Science), https://www.amazon.science/publications/addressing-cold-start-in-product-search-via-empirical-bayes
  - "New items typically cross the cold start barrier through very specific queries". The paper calls these "spearfishing queries".
  - "it takes a very long time for new items to be stably ranked".
  - The method gives a new item a prior estimate of its behavioural features (click and purchase rates), drawn from similar items. It then updates toward the observed data as interactions accrue.
  - A UCB-style early-stopping rule ends exploration of items that perform poorly. An over-confident prior "can take days" to correct.
  - Online A/B test on 50 million queries (for human readers only): new-product impressions +13.53%, new-product purchases +11.14%, overall purchases +0.08%.
  - The paper says: "Sponsored results, listings and promotions are also essential instruments for sellers to push their new products into the search feedback wheel". The next sentence qualifies it: "Such mechanisms are however collateral to result search relevance, involve cost and effort for sellers, and a challenging competition that is not easy to overcome."
  - It reports a test. It does not state a production deployment.
- **Priors for cold start, earlier work.** [research] Gupta, Dreossi, Bakus, Lin and Salaka, *Treating cold start in product search by priors*, The Web Conference 2020 (Amazon Science). "The online A/B test on 140MM queries shows that treatment with priors improves new products impressions and increased customers engagement". https://www.amazon.science/publications/treating-cold-start-in-product-search-by-priors
- **Borrowing behaviour from substitutes.** [research] Dong, Momma, Wang, Gao and Sun, *Behavioral Feature Boosting via Substitute Relationships for E-commerce Search*, arXiv 2602.14502 (Amazon, February 2026), https://arxiv.org/abs/2602.14502
  - New items get a warm start from the behavioural signals (clicks, add-to-carts, purchases, ratings) of their substitutes, 5 substitutes per new product on average, with the substitute data "refreshed periodically (e.g., every four hours)".
  - Four-week A/B test "on a large E-commerce platform" (for human readers only): GMV +0.11%, units +0.22%, new-product GMV +0.18%, new-product units +0.35%.
  - Verbatim: "The BFS-enhanced ranking model has been launched in production and has served customers since 2025." The paper names the platform only as "a large E-commerce platform"; the authors' addresses are @amazon.com and an author biography refers to Amazon Search.
  - [seat] This is the one source read that states a production cold-start mechanism, by Amazon authors, almost certainly in Amazon search. Under it, a new item's early ranking depends partly on how its substitutes behave, not only on its own clicks.
- **Patents.** [research] Patent text gives examples, not operating figures.
  - US20230367818A1, granted as US12346379B2 (original assignee A9.com; filed 2022-05-16; inventors Cuize Han, Parth Gupta, Xu Xu and Pablo Castells), https://patents.google.com/patent/US20230367818A1/en:
    - it defines a cold-start condition with a period: "whether the item has been available to be included as a search result for less than a period of time, such as ninety days";
    - it adds: "even if an item has recently been added to a catalog of the search system 104, but the corresponding item query pair has sufficient interaction data, then the cold-start service 110 can determine that the item is ineligible as a cold-start item". The test is per item-query pair.
  - US11269898B1 (priority 2019-12-13, published 2022-03-08; inventors Salaka, Gupta, Dreossi, Bakus and Lin), https://patents.google.com/patent/US11269898B1/en:
    - "a period of time has elapsed (for example, three days) after the item was added to a database, then the ranking service 116 can use the posterior prediction value instead of the prior prediction value";
    - it describes an administrator setting a value "to manually boost the item's visibility" as the manual curation it calls "time-consuming, impractical for a large number of items, error prone, arbitrary, and/or inefficient", i.e. the practice the method replaces, not a feature of it.
  - [seat] Under the first patent, cold-start status for an item-query pair ends on that pair's interaction data as well as on age. Under that reading, a launch that buys interactions early leaves the prior sooner. That is the mechanism behind practitioners' "use the window" advice, and also behind the risk that poor early performance is locked in. The patents do not say which matters more.

### Advertising for new firms and products

- **Who gains from advertising.** [research] Dai, Kim and Luca, *Which Firms Gain from Digital Advertising? Evidence from a Field Experiment*, NBER Working Paper 30925 (2023), https://www.nber.org/papers/w30925
  - The study is a Yelp field experiment over three months, with 18,294 restaurants, of which 7,209 were treated.
  - Results: +7–19% on purchase-intention outcomes, and +5% reviews.
  - The effects "disappear immediately after the experiment ends". The authors attach a caveat to this.
  - Larger gains went to independent firms, higher-rated firms, firms with more reviews or more organic traffic, and newer firms (entered within two years). The newer-firm gain held only for firms that were not national chains.
  - It cites Sahni and Nair (2020) for the finding that "newer firms gain more leads" from advertising. Sahni and Nair's own text words it more narrowly (next item).
  - [seat] The study is not on Amazon. Two of its findings bear on launches: ads helped firms that already had reviews and ratings more, and the effect did not persist once the ads stopped. Both cut against "ads now, organic later" unless something else (reviews, rank) carries over.
- **Advertising as a signal, and who it helps.** [research] Sahni and Nair, *Does Advertising Serve as a Signal? Evidence from a Field Experiment in Mobile Search*, Review of Economic Studies 87(3), 2020, 1529–1564, doi 10.1093/restud/rdz053 (read as the published text, copy at https://gwern.net/doc/economics/advertising/2020-sahni.pdf; earlier draft at https://web-docs.stern.nyu.edu/marketing/SahniPaper.pdf).
  - Design: on Zomato's Android app in August–September 2014, "about 200,000 users in 13 Asian cities" were randomized into a control group "shown no advertising", group A (paid listings with no ad label) and group B (the same paid listings labelled as ads), for "about 600+ local restaurants".
  - Main result: "this disclosure increases calls to the restaurant by 77%, holding fixed all other attributes of the ad". The effect "is higher when the consumer uses the platform away from his typical city of search, when the uncertainty about restaurant quality is larger, and for restaurants that have received fewer ratings in the past."
  - On newness specifically: "The interaction of the group B dummy with the age of the restaurant is not statistically significant. We see that restaurants that have fewer ratings benefit more from the ad-disclosure in terms of their call probability". The authors call the test "only suggestive", because fewer ratings and newer entry "could be proxying for other things like popularity or quality".
  - On the supply side, "newer, higher rated and more popular restaurants are found to advertise more on the platform", and among restaurants with the same 2014 rating, those that advertised in 2014 had higher ratings in 2016. The authors call these supply-side facts "only suggestive", confounded with "unobservable product and market-specific differences".
  - [seat] Transfer to Amazon. The measured effect is that of the label, ads shown against ads shown without disclosure, not ads against no ads. Every Sponsored Products ad carries Amazon's "Sponsored" label, so a seller cannot turn the label off. What transfers is the direction: in this experiment the label carried more weight for listings with fewer past ratings, the state a new ASIN is in. The paper does not support "newer firms gain more" as a treatment effect; age was not significant, and fewer ratings was.
- **Bought reviews on Amazon: what persists and what fades.** [research] He, Hollenbeck and Proserpio, *The Market for Fake Reviews*, Marketing Science 41(5), 2022, 896–921, doi 10.1287/mksc.2022.1353 (published abstract read on EconPapers, https://econpapers.repec.org/RePEc:inm:ormksc:v:41:y:2022:i:5:p:896-921; full text read as the August 2021 working paper, https://eller.arizona.edu/sites/default/files/Hollenbeck%20Paper.pdf; the published figures may differ).
  - Data: "approximately 1,500 products observed soliciting fake reviews over a nine-month period" in Facebook groups (collected weekly, October 2019 to June 2020), with Amazon ratings and reviews, sales rank from Keepa, keyword search position, sponsored listings, coupons and prices, against 2,714 competitor products never seen buying reviews.
  - Short term (published abstract): "Buying fake reviews on Facebook is associated with a significant but short-term increase in average rating and number of reviews." Working paper: "The increase in average ratings is short-lived, with ratings falling back to the previous level within two to four weeks, but the increase in the weekly number of reviews, sales rank, and position in search listings remains substantially higher more than four weeks later." The authors call these results "descriptive in nature".
  - Ads alongside: "We also observe a persistent increased use of sponsored listings suggesting that Amazon sellers complement the Facebook promotion with advertising activities", together with "a substantial negative change in prices" lasting several weeks.
  - Causal sales effect: using a temporary mass deletion of reviews by Amazon (mid-purge date March 15, 2020) as a control, "rating manipulation causes a significant increase in sales rank".
  - After the buying stops: "the increase in sales is not self-sustaining. Sales fall significantly after the fake review campaign ends." Keyword search position behaves differently: "after the Facebook campaign stops, the downward trend in search position stops but does not substantially reverse even after two months… this measure may have a high degree of inertia", and the authors conclude the sales decline "does not come from a reduced product visibility but from the lower ratings and increase in one-star reviews."
  - Cold start: products "listed for fewer than four months" with "eight or fewer reviews" saw "a larger increase in sales initially but a similar drop-off afterward"; their ratings "fall even further than for regular products", and "the use of sponsored listings decreases for 'cold-start' products while it increases for the rest of the products". Published abstract: ratings fall and one-star reviews rise "particularly for young products, indicating rating manipulation is mostly used by low-quality products".
  - Platform response: about 43% of the reviews of these products were eventually deleted (the introduction says "roughly half"), "with an average lag of over 100 days".
  - [seat] Transfer to a launch. This is Amazon data on a bought early boost to a new or young product. The bought reviews are prohibited (J), and the boost was to reviews, not ad clicks. Two findings still bear on the launch question. First, a bought rise in sales did not sustain itself once the buying stopped, and the fall came with worse ratings. Second, keyword search position held for two months after the buying stopped, while sales fell. Read together, organic position on Amazon can show inertia after a push, and position alone did not keep sales up when the product's ratings fell. The sellers also raised sponsored listings during the push, so the descriptive rise is not the reviews' effect alone.

### Why "the launch spend built the rank" cannot be read from a before-and-after

- [seat] A launch has no pre-period. Before its first day the ASIN had no sales, no rank and no search position, so a before-and-after comparison of the ASIN with itself measures the launch as a whole: the listing going live, stock arriving, Vine and coupon reviews, the cold-start prior and its exit (*Published research*, patents), the price, and the ads, all at once. Practitioners' timelines in *What practitioners add* are schedules of this whole, not measurements of the ad share in it.
- The comparisons that can separate the ads, each with its standard design:
  - **Sibling ASINs launched with different ad spend** (same brand, category and price band, launched at different times or with different budgets). This is a cross-sectional comparison and carries the selection the authors above warn about: a seller spends more behind the product they expect to sell. [seat]
  - **One product launched in several marketplaces at staggered dates**, or with ads started on different dates. [research] Athey and Imbens, *Design-based Analysis in Difference-In-Differences Settings with Staggered Adoption* (arXiv 1808.05293, 2018): "units… adopt the policy or treatment of interest at a particular point in time, and then remain exposed to this treatment at all times afterwards", and "under random assignment of the adoption date the standard Difference-In-Differences estimator is is an unbiased estimator of a particular weighted average causal effect" (the doubled "is" is in the abstract). A seller's launch dates are chosen, not random, so the condition in that sentence does not hold by design. [seat]
  - **Dose variation within the launch** (budget or bid levels changed on dates, or different spend on different keywords for the same ASIN). [research] Callaway, Goodman-Bacon and Sant'Anna, *Difference-in-Differences with a Continuous Treatment* (arXiv 2107.02637, 2021): treatment-on-the-treated parameters "are identified under a parallel trends assumption", but "comparing these parameters across treatments is challenging because parallel trends does not rule out selection bias", and "popular two-way fixed effects estimands admit multiple interpretations". On Amazon, Sponsored Products targets carry no geography (`method/change-measurement.md`, its stable item 13), so the dose varies by time or keyword, not by region.
  - **A synthetic control built from other series.** [research] Brodersen et al., *Inferring causal impact using Bayesian structural time-series models*, Annals of Applied Statistics 9(1), 2015, 247–274 (arXiv 1506.00356): it predicts "the counterfactual market response in a synthetic control that would have occurred had no intervention taken place", from covariate series that the intervention did not touch. For a launch the covariates would be the category's or the competitors' rank and price series (`cx-keepa`), not the ASIN's own past, which does not exist. [seat]
- A mechanism measured elsewhere: [research] Ju, Zhao and Aral, *Advertising Spillovers in Mobile Apps: Evidence from Ad Shutoffs and Store Rankings* (arXiv 2504.16151, 2025, preprint): at a US mobile game developer, a global ad shutoff "decreased organic installs by 20-30%"; "paid installs boost app store category rankings, thereby increasing organic visibility"; and "the relationship between organic installs and ad spend disappears once these rankings are factored in". This is the paid-sales-to-rank mechanism measured by a shutoff, in an app store whose rankings respond to installs. It is not Amazon data, and the design is a shutoff of running ads, not a launch. `ads-organic-and-total.md` owns its wider reading.
- [seat] No published study read measures, on Amazon, whether Sponsored Products spend in a launch window leaves a lasting effect on organic rank or sales after the spend ends. He et al. measure the persistence of a bought review boost; the Amazon Science cold-start papers measure ranking changes Amazon made, not seller spend.
- **Not read, listed as leads.** These are known only from search results or other files, and this seat did not read them:
  - a Flipkart retail-media field experiment (Information Systems Research, doi 10.1287/isre.2022.0188), read by `ads-organic-and-total.md`;
  - Moshary (2025) and Blake, Nosko and Tadelis (2015), read by `method/change-measurement.md` and `ads-organic-and-total.md`; and the papers the listing playbook's `angles/paid-keywords.md` cites.

  No peer-reviewed study isolating Vine's effect on sales was found. Amazon's "30%" is the only figure.

## Stable enough for a skill

These statements are stable across the sources read, or are Amazon rules or documented mechanisms. Figures in them stay out of the skill text and are read at run time.

1. An ad serves only for a product that is eligible to be the Featured Offer and is in stock. An ASIN that is out of stock is paused within its campaign automatically. (*New advertiser success guide*; *How to improve your product detail page for advertising*; API *Sponsored Products product ads*.)
2. Sponsored Products needs a Professional selling plan or a vendor account. Adult, used, refurbished and closed-category products are not supported. Sponsored Brands, display and Stores need Brand Registry. (*New advertiser success guide*; *Advertising | Sell on Amazon*.)
3. Eligibility is machine-readable before launch, with named reasons and two severities. `INELIGIBLE` means the product cannot be in an ad, and `ELIGIBLE_WITH_WARNING` means it "may not receive impressions". (Eligibility OpenAPI.)
4. Amazon's review advice for advertising (five or more reviews, 3.5 stars or higher) is guidance, not a gate. No eligibility reason reads a review count. (*New advertiser success guide*; Eligibility OpenAPI.)
5. A zero-review product can run a coupon under the captured review rule, and Amazon's roadmap names coupons as a day-one action. A deal needs a sales history and at least a 4-star rating. (*Coupon eligibility criteria* and *Amazon deals* captures; 30-day roadmap post.)
6. Amazon's first-campaign guidance for a new advertiser is Sponsored Products with automatic targeting, started at once with no end date, at the suggested bid. Amazon's intermediate guidance calls using both automatic and manual targeting "a balanced advertising strategy" and, after launch, says to run them together; the targeting guide instead suggests about two weeks of auto before creating manual. (*New advertiser success guide*; getting-started guide; *Intermediate and advanced new ASIN playbook*; *A guide to targeting with Sponsored Products*.)
7. An auto campaign's targeting type cannot be changed once it is live. Its four auto expressions are created automatically as theme targets, and each can carry its own bid. (*A guide to targeting with Sponsored Products*; API *auto targeting*.)
8. Suggested bids exist for an ASIN with no history, because they are computed from recent winning bids for similar products. Amazon says their impact metrics are not performance estimates. The v3 content type of the bid recommendation call was shut off on May 15, 2025; v4 covers keyword, auto and product targets. (API theme-based bid quickstart; Sponsored Products 3.0 OpenAPI; *Deprecations*.)
9. The API can produce bids, keywords, products, categories and a daily budget for a campaign that does not yet exist: `BIDS_FOR_NEW_AD_GROUP`, `KEYWORDS_FOR_ASINS`, the product and category recommendations, and `initialBudgetRecommendation`. The last returns `-1` when it lacks information. (Sponsored Products 3.0 OpenAPI.)
10. Rule-based bidding is closed to a campaign that is under 10 days old or has had fewer than 10 conversions in 30 days. (API *rule-based bidding overview*.)
11. The new-seller Sponsored Products credit pays for later ads, not for the spend that earned it. It is earned by a first campaign within 90 days of the first buyable listing and spend within 30 days of that campaign, and it is valid for 30 days once issued. (*New Seller Sponsored Products Promotion (2024)* terms; *New Seller Incentives*.)
12. Amazon publishes no "honeymoon" claim. The word appears on an Amazon page read here only in a seller's quote. Amazon researchers' papers and Amazon's patents describe cold-start priors, exploration with early stopping, and borrowing from substitutes; only the substitute method is stated as in production ("on a large E-commerce platform", by Amazon authors). (*Tips for new product success*; CIKM 2022; arXiv 2602.14502; patents.)
13. Off-Amazon incentives that drive customers to products sold without those incentives on Amazon, and search-rank manipulation by any name, violate the Seller Code of Conduct, including when a third party does it. (2021 forum clarification.)
14. Amazon's own launch multiples (36x, 231x, 321x, 260x) are internal, ad-attributed comparisons between groups of advertised products (new against not new, suggested against not suggested). They are not incrementality measurements. (Section O pages; `beyond/metrics-and-attribution.md`.)
15. Review Requests is a Sponsored Products ENGAGEMENT-goal campaign whose billable click is a rating or review. It is for products with fewer than 1,000 reviews, it is a US beta, and during the beta it is enabled per advertiser account. (API *Review requests* guides.)
16. A Sponsored Products campaign is built through the Ads API by separate creates: campaign, then ad group (needs the `campaignId`), then product ad (needs the `adGroupId`; SKU for a seller, ASIN for a vendor), then, for a manual campaign, at least one target or keyword per ad group, with negatives optional at campaign or ad group level. Amazon calls an auto campaign complete once its product ad exists, and a manual one once it also has a target; with a start date of today it serves at once. (API guides *Sponsored Products campaign structure*, *Get started with manual campaigns*, *Get started with auto campaigns*, *Sponsored Products ad groups*, *Sponsored Products product ads*.)
17. The calls share no transaction and take no idempotency key. Each answers 207 with per-item success and error, and the API has `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE` statuses for the half-built cases. (SP v1 and SP 3.0 models; `method/ads-api-surface.md` section F.)
18. The MCP server's `create_singleshot_sp_campaign` creates "campaign + ad group + ads" in one operation, on hosts the `cx-amazon-ads` door does not reach. Its specification does not say what a failure inside it leaves. (MCP `campaign_management.json`; *Connecting to the Amazon Ads MCP Server*; *All releases* 2026-02-18; cx-amazon-ads SKILL.md.)
19. On Amazon, products that bought reviews saw ratings rise and then fall back within two to four weeks; sales rose and then fell after the buying stopped; keyword search position held for two months. (He, Hollenbeck and Proserpio, Marketing Science 2022.)
20. A launch has no pre-period, so the ads' share of a launch's rank cannot be read from a before-and-after of the ASIN itself. The designs that can separate it (sibling launches, staggered marketplaces, dose variation, synthetic controls) each rest on a stated assumption. (Athey and Imbens; Callaway, Goodman-Bacon and Sant'Anna; Brodersen et al.)

## What cx must read at run time

Everything below is a public endpoint shape. A skill reads the seller's own values through cx at run time and never from this file. The Ads API calls go through the `cx-amazon-ads` door (`cx raw amazon-ads --origin … --method … --path …`, with the profile scope header). Headers, regions and the request lifecycle are owned by `method/ads-api-surface.md`, and report lifecycles by `method/reporting.md`.

**Is the product advertisable now, and why not?**
- `POST /eligibility/product/list`, body `{adType: "sp", productDetailsList: [{asin, sku}], locale}`. Read `overallStatus` and `eligibilityStatusList[].{name, severity, message, helpUrl}`. A 404 means not associated with the profile, or not in the catalog.
- `POST /eligibility/programs`, for the SB and SD gates. Read the reason codes, especially NOT_BRAND_REPRESENTATIVE, NO_BRAND_RELATIONS and PAYMENT_METHOD_NOT_FOUND.
- `POST /product/metadata` (content type `application/vnd.productmetadatarequest.v1+json`), with `asins` or `skus`, `checkEligibility: true` and `checkItemDetails: true`. Read `createdDate`, `availability`, `bestSellerRank`, `priceToPay`, `basisPrice`, `eligibilityStatus`, `ineligibilityCodes` and `ineligibilityReasons`. `sortBy: SUGGESTED` reads Amazon's suggested products, and `CREATED_DATE` lists the newest.
- After creation: `POST /adsApi/v1/query/ads`, `…/adGroups` and `…/campaigns`. Read `status.deliveryStatus` and `deliveryReasons` (`diagnosis.md` owns the meanings).

**What Amazon proposes for a new ASIN.**
- `POST /recommendations/list` (Tactical Recommendations 3.0), or `POST /adsApi/v1/query/recommendations`. Filter for grouping `NEW_ASIN`; the recommendation types that create things include NEW_CAMPAIGN, NEW_PRODUCT_AD and NEW_KEYWORD (the spec does not tie types to groupings). Read the recommendation body, and `AsinContext.trailing4WeeksConversionRate` where present (a product-type benchmark).
- `GET|POST /sp/campaign/recommendations`, for the consolidated daily recommendations.

**Opening bids, targets and budget for a campaign not yet created.**
- `POST /sp/targets/keywords/recommendations`, `recommendationType: KEYWORDS_FOR_ASINS`, `asins`, an optional `biddingStrategy` and `sortDimension`. Read the keywords, ranks, per-theme bid suggestions, and (v4) search term impression share and rank.
- `POST /sp/targets/bid/recommendations`, `recommendationType: BIDS_FOR_NEW_AD_GROUP`, `asins` and `targetingExpressions`. Content type `application/vnd.spthemebasedbidrecommendation.v4+json` (v3 was shut off on 2025-05-15; v5's extra fields apply only to existing US ad groups). Read the low, median and high bids per expression and theme.
- `POST /sp/targets/products/recommendations` and `POST /sp/targets/categories/recommendations`, for product and category targets for the ASINs.
- `POST /sp/campaigns/initialBudgetRecommendation` (content type `application/vnd.spinitialbudgetrecommendation.v3.4+json`). Read `dailyBudget` (`-1` means insufficient information), `benchmark.benchmarkStatus`, the benchmark ranges for impressions, clicks and conversions, and `specialEvents[]`.
- The marketplace's bid and budget limits are on the API *Limits* page. The live values are checked against the API's own validation errors when a write is refused.

**Building the campaign (writes, in order; section P).**
- v1: `POST /adsApi/v1/create/campaigns` (read `success[].campaign.campaignId`), then `POST /adsApi/v1/create/adGroups` with that `campaignId` (read `adGroupId`), then `POST /adsApi/v1/create/ads` with `adType: PRODUCT_AD` and `advertisedProduct {productIdType: SKU|ASIN, productId}`, then `POST /adsApi/v1/create/targets` (positive and `negative: true` targets, `adGroupId` or `campaignId`). For auto campaigns, the auto targets' ids are read with `POST /adsApi/v1/query/targets` before their bids are set with `/adsApi/v1/update/targets`.
- SP 3.0: `POST /sp/campaigns`, `/sp/adGroups`, `/sp/productAds`, `/sp/keywords`, `/sp/targets`, `/sp/negativeKeywords`, `/sp/campaignNegativeKeywords`, `/sp/negativeTargets`, `/sp/campaignNegativeTargets`, each under its own `application/vnd.sp….v3+json` media type.
- Each reply: the `207` body's `success[]`, `error[]` (and in the cross-product v1 model `partialSuccess[]`), matched to the request by `index`. Required fields, batch limits and enums (`SPCreateState`, `SPTargetType`, `SPBidStrategy`) are read from the SP v1 model, not from this file.
- A seller's SKU for an ASIN: `POST /product/metadata` (above).
- After the chain, or after a lost reply: `POST /adsApi/v1/query/campaigns`, `…/adGroups`, `…/ads` and `…/targets` filtered by the parent ids show what exists. Read `status.deliveryStatus` and `deliveryReasons` (`CAMPAIGN_INCOMPLETE`, `AD_GROUP_INCOMPLETE`), or SP 3.0 `extendedData.servingStatus` on `POST /sp/campaigns/list` and `/sp/adGroups/list`.

**Moving auto findings into manual.**
- `POST /sp/targetPromotionGroups/recommendations` with `adGroupIdFilter` set to the auto ad group. Then `POST /sp/targetPromotionGroups` (existing or new manual campaigns), and `POST /sp/targetPromotionGroups/targets`.
- The search term data is the underlying input. Reporting v3 (`POST /reporting/reports`, including its Sponsored Products report types) was deprecated in September 2026 and stops delivering data on June 30, 2027; the replacement is the Reporting API v1 (`POST /adsApi/v1/create/reports`, generally available) (*Deprecations*; *All releases*). `method/reporting.md` owns columns and lifecycle.

**Strategy gates as data accrues.**
- `POST /sp/rules/campaignOptimization/eligibility`, to know whether a campaign has passed the 10-day and 10-conversion threshold for rule-based bidding.
- `POST /sp/campaigns/budgetRecommendations`, once the campaign has history. Read the recommended budget, percent time in budget, and missed impressions, clicks and sales.

**The seller's own launch credits.**
- `POST /adsApi/v1/query/promotionOffers` (BETA; global account). Read `status`, `fulfilmentCriteria[]` (the campaign-launch and spend criteria with dates and tiers) and `promotionCampaign.{adProduct, title, tncUrl}`.
- `POST /adsApi/v1/query/promotionRewards` (BETA). Read `reward`, `remainingReward`, `endDateTime` and `promotionRewardType`.
- Where the BETA is not available to the account, the credit is read in the console (Administration > Billing > Promotions) by the seller. The figures on sell.amazon.com are generic and may not match the seller's offer.

**Review Requests availability.**
- Attempting `POST /adsApi/v1/create/campaigns` with `optimizations.goalSettings.goal: ENGAGEMENT` is a write; for an account not yet enabled for the beta it "returns an error" (*Get started with Review Requests*). No read operation found here reports enablement. A read of existing engagement campaigns is `POST /adsApi/v1/query/campaigns` with `goalFilter` ENGAGEMENT.

**Retail facts outside the Ads API** (read through the sibling cx packages, not this one):
- The Featured Offer percentage, sessions and conversion by child ASIN: the SP-API sales-and-traffic report (`GET_SALES_AND_TRAFFIC_REPORT`) or Data Kiosk. The sibling listing playbook notes that its Featured Offer percentage has a glance-view denominator, while the help page uses page views.
- Stock: SP-API FBA inventory (`getInventorySummaries`).
- The listing's status and issues: SP-API `getListingsItem`. Catalog attributes: `getCatalogItem`. Price and the Featured Offer competitive picture: Product Pricing v2022-05-01 `getCompetitiveSummary` and `getFeaturedOfferExpectedPriceBatch` (operation names as in the public `amzn/selling-partner-api-models` repository).
- Review topics: Customer Feedback v2024-06-01 (`getItemReviewTopics`, `getItemReviewTrends`). Review count and rating history, coupon history and the earliest listing date: Keepa product fields `csv` slots 16 and 17 (rating in tenths, and rating count), `couponHistory`, `listedSince` (earliest listing, not release) and `releaseDate`, as `cx-keepa`'s `references/product-file.md` defines them.
- Search Query Performance for the new ASIN: the SP-API Brand Analytics report `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT`. Brand-registered sellers only.
- Coupon, deal and Vine enrollment state: not exposed through any Ads API read this seat found. The seller reads them in Seller Central.

**Series for judging what the launch spend did** (*Published research*, the measurement subsection):
- The seller's own launch history: Ads API reports by day for the ASIN's campaigns (`method/reporting.md`), the change history (`POST /history`, `method/change-measurement.md`) for the dates bids and budgets changed, and SP-API sales and traffic by date and child ASIN.
- Sibling ASINs and other marketplaces: Keepa sales rank history (`csv` slot 3, the reference sales rank, and `salesRanks[category]`), `listedSince` and `releaseDate` for each sibling's launch date, and the same ASIN's history in each Keepa domain (`cx-keepa`'s `references/product-file.md`).
- Search position by term: Brand Analytics Search Query Performance (above) gives the ASIN's impressions, clicks and purchases per query by period; no Amazon read here gives organic search position itself.

## Pages read

All pages were read 2026-11-09 by plain GET, except where the row says otherwise. API guides were read as Markdown from the documentation's CloudFront host, and specifications as the OpenAPI JSON listed in its contracts index. "Fetched, light" means the page was fetched and checked, but gave nothing this file relies on beyond what the row says.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Intermediate and advanced new ASIN playbook | https://advertising.amazon.com/library/guides/intermediate-and-advanced-new-asin-playbook | official guide | 2026-11-09 | Readiness review; auto plus manual; suggested bid; SB 23%; video for organic; branded impression share for review-less items |
| How to create your new product launch strategy | https://advertising.amazon.com/blog/how-to-create-your-new-product-launch-strategy | official blog | 2026-11-09 | First 90 days; upper funnel +36%; new and notable +22% CTR; managed budget minimums |
| A product advertising strategy | https://advertising.amazon.com/library/guides/product-strategy | official guide | 2026-11-09 | Suggested and "New product" labels; 36x clicks; deals and coupons +65%; excess inventory |
| New advertiser success guide | https://advertising.amazon.com/library/guides/new-advertiser-success-guide | official guide | 2026-11-09 | Account and product rules; Featured Offer rule; 90% Featured Offer rate; 5 reviews at 3.5; run at once with no end date; auto |
| How to improve your product detail page for advertising | https://advertising.amazon.com/library/guides/improve-your-products-for-advertising | official guide | 2026-11-09 | Featured Offer rule; out-of-stock pause; detail page advice; search terms into the listing |
| Best practices for your Sponsored Products ads | https://advertising.amazon.com/library/guides/sponsored-products-best-practices | official guide | 2026-11-09 | $10 a day; monthly averaging; 900% placements; twice weekly in week one; 231x and 321x; category targeting for new products |
| A guide to targeting with Sponsored Products | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official guide | 2026-11-09 | Auto for about two weeks first; targeting fixed once live; 1–2 weeks per match type; 20 clicks before negating; one ASIN per campaign |
| Getting started guide for sponsored ads | https://advertising.amazon.com/library/guides/getting-started-with-sponsored-ads | official guide | 2026-11-09 | Start with SP; budget table; no end date; auto first; an auto and manual pair per group |
| Checklist for new international ad campaigns | https://advertising.amazon.com/library/guides/checklist-for-new-international-ad-campaigns | official guide | 2026-11-09 | Two suggested products; suggested bid; down only first; $10 minimum; raise budget after repeated depletion |
| Guide to dynamic bidding - up and down with Sponsored Products | https://advertising.amazon.com/library/guides/dynamic-bidding-sponsored-products | official guide | 2026-11-09 | Up to 100% for all placements |
| Sponsored Products - Help increase product sales | https://advertising.amazon.com/solutions/products/sponsored-products (redirect target of https://advertising.amazon.com/blog/new-bidding-and-targeting-options-for-sponsored-products) | official | 2026-11-09 | "Up to $1000" credit banner and eligibility footnote |
| Amazon Ads introduces New Product Campaigns | https://advertising.amazon.com/library/news/introducing-new-product-campaigns-from-amazon-ads | official news | 2026-11-09 | Managed 90-day full-funnel service; 30/60/90 flighting; New & Notable is 12 months; 4x glance views (footnote numbering mismatched) |
| Launch announcement: Introducing new product campaigns from Amazon Ads | https://advertising.amazon.com/resources/whats-new/introducing-new-product-campaigns-from-amazon-ads | official launch note | 2026-11-09 (verifier) | GA in the U.S. on October 15, 2024; announced at unBoxed 2024; managed service |
| Amazon Ads introduces Full-Funnel Campaigns, DVA+, and enhanced chat experience in AI-powered ad platform, Amazon Ads Agent | https://advertising.amazon.com/library/news/amazon-ads-agent | official news (2026-09-29) | 2026-11-09 | Unified platform renamed; one-click AI guidance; staged rollout; Full-Funnel Campaigns for all US advertisers |
| The 11 biggest takeaways from unBoxed 2026 | https://advertising.amazon.com/library/news/unboxed-2026-news-announcements | official news (2026-09-30) | 2026-11-09 | Full-Funnel Campaigns beta figures |
| New Seller Sponsored Products Promotion (2024) | https://advertising.amazon.com/legal/terms-conditions/new-seller-sponsored-products-promotion-2024 | official terms | 2026-11-09 | 90-day and 30-day windows; tiers; credit within 14 days, valid 30 days, not for window spend |
| Sponsored Products New ASIN Adoption Promotion | https://advertising.amazon.com/legal/terms-conditions/sponsored-products-new-asin-adoption-promotion | official terms | 2026-11-09 | Invite-only; suggested product; one credit within 14 business days, valid 30 days |
| Sponsored Brands Launch Promotion | https://advertising.amazon.com/legal/terms-conditions/sponsored-brands-launch-promotion | official terms | 2026-11-09 | Credits for a first SB campaign; credits expire 30 days after award |
| eCommerce display creatives - Guidelines & ad specs | https://advertising.amazon.com/resources/ad-specs/ecommerce | official ad specs | 2026-11-09 (verifier) | Coupons surfaced automatically as savings badges in Responsive eCommerce Creatives |
| Deprecations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md | official API doc | 2026-11-09 (verifier) | v3 bid-recommendation content type shut off 2025-05-15; v3 reporting shutoff 2027-06-30 |
| Sponsored Products auto campaigns (API guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/auto-campaigns.md | official API doc | 2026-11-09 | Start with auto; `autoCreateTargets`; start today serves immediately |
| Sponsored Products auto targeting (API guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/auto-targeting.md | official API doc | 2026-11-09 | Four auto expressions as ThemeTargets; default-bid fallback |
| Theme-based bid suggestions quickstart | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/bid-suggestions/theme-based-bid-suggestions-quickstart-guide.md | official API doc | 2026-11-09 | Winning bids of similar products; three bids; not performance estimates; PAT conflict |
| Sponsored Products keyword recommendations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/suggestions.md | official API doc | 2026-11-09 | KEYWORDS_FOR_ASINS; v4 impression share; new ad group examples |
| Sponsored Products product targeting suggestions | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/suggestions.md | official API doc | 2026-11-09 | Product recommendations by theme or by ASIN |
| Sponsored Products product ads | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-ads.md | official API doc | 2026-11-09 | In stock to serve; SKU for sellers |
| Sponsored Products campaigns | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/campaigns.md | official API doc | 2026-11-09 | Fetched, light: points to v1 campaigns |
| Sponsored Products ad groups | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/ad-groups.md | official API doc | 2026-11-09 | Fetched, light |
| Sponsored Products campaign structure | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/campaign-structure.md | official API doc | 2026-11-09 | Fetched, light (owned by campaign-structure.md) |
| Sponsored Products rule-based bidding overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/overview.md | official API doc | 2026-11-09 | 10 days and 10 conversions; guardrail; minimum budgets |
| Limits | https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md | official API doc | 2026-11-09 | Bid and budget ranges by marketplace |
| All releases | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md | official API doc | 2026-11-09 | Review Requests release note dated 2026-11-16 |
| Review requests: get started | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/review-requests/get-started.md | official API doc | 2026-11-09 | Campaign, target and ad shapes; billing; 1,000-review cap |
| Review requests overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/review-requests/overview.md | official API doc | 2026-11-09 | "New products face a cold-start problem" |
| Review requests FAQ | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/review-requests/faq.md | official API doc | 2026-11-09 | goalFilter; console-only metrics |
| Contracts index | https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json | official API doc | 2026-11-09 | OpenAPI file locations |
| Sponsored Products 3.0 OpenAPI | `SponsoredProducts_prod_3p.json` (contracts index) | official spec | 2026-11-09 | Bid, keyword, product and category recommendations; initial and existing budget recommendations; target promotion groups; campaign recommendations |
| Eligibility OpenAPI | `Eligibility_prod_3p.json` (contracts index) | official spec | 2026-11-09 | Product and program eligibility reasons and severities |
| Recommendations OpenAPI | `Recommendations_prod_3p.json` (contracts index) | official spec | 2026-11-09 | NEW_ASIN grouping; recommendation types; AsinContext |
| Amazon Ads API v1 merged OpenAPI | `AmazonAdsAPIALLMerged_prod_3p.json` (contracts index) | official spec | 2026-11-09 | deliveryReasons; BidStrategy; ThemeMatchType; Goal; autoManageCampaign |
| Amazon Ads API v1 merged OpenAPI (BETA) | `AmazonAdsAPIALLMerged_prod_3p_BETA.json` (contracts index) | official spec | 2026-11-09 | promotionOffers, promotionRewards, promotionCodeRedemptions |
| Product Selector OpenAPI | `ProductSelector_prod_3p.json` (contracts index) | official spec | 2026-11-09 | product/metadata fields incl. createdDate and availability |
| Advertising Billing OpenAPI | `AdvertisingBilling_prod_3p.json` (contracts index) | official spec | 2026-11-09 | Fetched, light: no promotion fields beyond the v1 BETA |
| Offline Report OpenAPI | `OfflineReport_prod_3p.json` (contracts index) | official spec | 2026-11-09 | Fetched, light (owned by method/reporting.md) |
| New Seller Incentives | https://sell.amazon.com/incentives | official | 2026-11-09 | Current incentive figures and windows |
| New Seller Incentives (old URL) | https://sell.amazon.com/grow | official | 2026-11-09 | Redirects to /incentives |
| Amazon Vine | https://sell.amazon.com/programs/vine | official | 2026-11-09 | Eligibility, timing, fees, three-week advice, marketplaces |
| Amazon Brand Registry | https://sell.amazon.com/brand-registry | official | 2026-11-09 | Requirements; brand programs; Brand Referral Bonus wording |
| Advertising (Sell on Amazon) | https://sell.amazon.com/advertising | official | 2026-11-09 | Up to $1,000 credit; SP first; Brand Registry gates; 34% and 260x |
| Tips for new product success | https://sell.amazon.com/blog/new-product-success | official blog | 2026-11-09 | 30-day roadmap; complimentary placements; seller "honeymoon" quote |
| 5 steps to launch a product successfully | https://sell.amazon.com/blog/product-launch | official blog | 2026-11-09 | Deals, coupons and Vine; 6x first-year sales |
| Guide to running Amazon seller promotions, deals, coupons, and discounts | https://sell.amazon.com/blog/seller-promotions | official blog (2026-05-27) | 2026-11-09 | Coupon placement and 90-day expiry; deal and coupon rating floors (served 200 to the verifier) |
| What is the FBA New Selection program? | https://sell.amazon.com/blog/fba-new-selection-program | official blog | 2026-11-09 | Requirements; auto-enrollment; Vine $75 and coupon $50 credits; 120-day waivers |
| Sell new products | https://sell.amazon.com/blog/sell-new-products | official blog | 2026-11-09 | Fetched, light: hub page |
| New product success (full guide PDF) | https://m.media-amazon.com/images/G/01/bx-marketing/FullGuide_new-product-success.pdf | official PDF | 2026-11-09 | Vine day-one badge; coupon validation exemption; 85% figure; older incentive list; Product Performance Spotlight |
| 30 days to new product success (quick guide PDF, v3.0, 05/01/26) | https://m.media-amazon.com/images/G/01/bx-marketing/Quickguide_30-days-to-new-product-success.pdf | official PDF | 2026-11-09 | Prelaunch list; complimentary placements; post-launch ad refinement; 24.5% |
| Clarification of Amazon's Policy on Rebates, Coupons, and other Marketing Incentives | https://sellercentral.amazon.com/seller-forums/discussions/t/5625a806dcc896ccc7d434751a65c07f | official forum post | 2026-11-09 | Off-Amazon incentive and rank-manipulation rules |
| New 30-day roadmap helps you launch products successfully | https://sellercentral.amazon.com/seller-forums/discussions/t/bcc285b7-28b6-41b2-bc08-4e1c86a6eea8 | official forum post | 2026-11-09 | Day 1 and Day 30 actions; seller question on review deprecation |
| Warning to New Sellers: How Promotional Click Credits… Really Work | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/151c81a5-d319-4fd7-a990-d0e1b13a943f | seller forum (opinion) | 2026-11-09 | Credit timing as a seller experienced it; quoted terms line |
| Addressing Cold Start in Product Search via Empirical Bayes | https://www.amazon.science/publications/addressing-cold-start-in-product-search-via-empirical-bayes | research (CIKM 2022) | 2026-11-09 | Priors; spearfishing queries; early stopping; A/B results |
| Addressing cold start in product search via empirical bayes (full-text PDF) | https://cdn.amazon.science/b5/2f/a9d9581d4f8eab473a4ab4a8ad35/addressing-cold-start-in-product-search-via-empirical-bayes.pdf | research | 2026-11-09 (verifier) | Full-text quotes (spearfishing, "can take days", sponsored results) |
| Treating cold start in product search by priors | https://www.amazon.science/publications/treating-cold-start-in-product-search-by-priors | research (The Web Conference 2020) | 2026-11-09 | Earlier prior method; A/B on 140MM queries |
| Behavioral Feature Boosting via Substitute Relationships for E-commerce Search | https://arxiv.org/abs/2602.14502 | research (arXiv 2026) | 2026-11-09 | Substitute warm start; in production since 2025 |
| Which Firms Gain from Digital Advertising? | https://www.nber.org/papers/w30925 | research (NBER WP) | 2026-11-09 | Field experiment; newer and better-reviewed firms gain more; no persistence |
| US20230367818A1 / US12346379B2 | https://patents.google.com/patent/US20230367818A1/en | patent | 2026-11-09 | Cold-start condition "such as ninety days"; exit on interaction data |
| US11269898B1 | https://patents.google.com/patent/US11269898B1/en | patent | 2026-11-09 | Prior to posterior "for example, three days"; manual boosting described as the curation the method replaces |
| Amazon Product Launch Playbook: The First 90 Days of a New ASIN | https://canopymanagement.com/amazon-product-launch-playbook/ | practitioner (Canopy) | 2026-11-09 | Three layers; 90-day sequence; honeymoon unconfirmed; 2026 rule changes |
| Honeymoon Period Decoded | https://code3.com/resources/honeymoon-period-decoded-the-truth-behind-amazons-cold-start-algorithm/ | practitioner (Code3) | 2026-11-09 | Patent-based five-day and 90-day claims |
| Doomed from the (Cold) Start | https://bestatamazon.kit.com/posts/doomed-from-the-cold-start-what-you-need-to-know-about-launching-products-in-2024-and-beyond | practitioner newsletter | 2026-11-09 | Honeymoon history; patent reading; early-advertising advice |
| Launch a Product with Amazon Ads, part 1 | https://www.helium10.com/blog/how-to-launch-a-product-on-amazon-in-2025-with-advertising/ | practitioner (Wishon / Helium 10) | 2026-11-09 | Five campaign jobs; top of search; strategy choice |
| Launch a Product with Amazon Ads, part 2 | https://www.helium10.com/blog/how-to-launch-a-product-on-amazon-in-2025-with-advertising-part-2/ | practitioner (Wishon / Helium 10) | 2026-11-09 | Harvest; 15–20 clicks; TACoS benchmark |
| Serious Sellers Podcast 753: The 6 Figure Amazon Launch Sprint | https://www.helium10.com/podcast/753-the-6-figure-amazon-launch-sprint/ | practitioner podcast | 2026-11-09 | Fixed-bid ranking campaigns; 10% daily raise rule; 30 Vine units |
| Serious Sellers Podcast 589: Amazon PPC for Product Launch | https://www.helium10.com/podcast/amazon-ppc-for-product-launch-and-campaign-optimization/ | practitioner podcast | 2026-11-09 | Fetched, light |
| Are Amazon product launches still valid? | https://www.helium10.com/blog/amazon-product-launches-valid/ | practitioner (Helium 10, 2018) | 2026-11-09 | Historical giveaway launches; honeymoon "length unknown" |
| The Best Way to Structure Campaigns for a New Product Launch | https://www.adbadger.com/blog/best-way-to-structure-amazon-campaigns-new-product-launch/ | practitioner (Ad Badger) | 2026-11-09 | Budget split; conservative bids; daily monitoring |
| How to Use Amazon Coupons to Promote Your Products | https://www.adbadger.com/blog/amazon-coupons/ | practitioner (Ad Badger) | 2026-11-09 | Coupon badge claim in ads |
| When auto campaigns don't work for new product launch | https://www.adbadger.com/blog/amazon-ppc-education/when-auto-campaigns-dont-work-for-new-product-launch/ | practitioner (Ad Badger, 2020) | 2026-11-09 | Indexing check before auto (Wishon method) |
| A blueprint for launching new products… with sponsored product ads | https://www.m19.com/blog/a-blueprint-for-launching-new-products-on-amazon-with-sponsored-product-ads | practitioner (m19) | 2026-11-09 | Search-term-level window; forced visibility; clicks-per-term sizing |
| The No B.S. Amazon Product Launch Guide for 2025 | https://www.ecomcrew.com/amazon-product-launch-guide/ | practitioner (ecomcrew) | 2026-11-09 | Narrow-then-widen; TACoS multiple; review counts |
| 6 steps to using Amazon PPC for profitable product launches | https://www.sellerlabs.com/blog/6-steps-using-amazon-ppc-profitable-product-launches/ | practitioner (Seller Labs, 2020) | 2026-11-09 | 14 days before adjustments; budget-preference claim |
| Amazon PPC Launch Strategy in 3 Phases | https://www.sellersprite.com/en/blog/amazon-ppc-launch-strategy | practitioner (SellerSprite) | 2026-11-09 | Three phases; lookback expansion |
| The Amazon New Product Success Playbook (landing page) | https://www.junglescout.com/resources/reports/amazon-new-product-playbook/ | practitioner, co-branded with Amazon | 2026-11-09 | Assess-Diagnose-Act loop (full playbook gated) |
| Seller Sessions – The Man Behind the Honeymoon | https://sellersessions.libsyn.com/seller-sessions-the-man-behind-the-honeymoon | practitioner podcast page | 2026-11-09 | Origin of the term (Anthony Lee) |
| The Cold Reality of the Honeymoon Period & External Traffic Part 1 | https://sellersessions.libsyn.com/the-cold-reality-of-the-honeymoon-period-external-traffic-part-1 | practitioner podcast page (2024-09-05) | 2026-11-09 (verifier) | Episode notes: Lee's 2015 observation, which he "denounced"; article cites 15 papers and 2 patents |
| Amazon gives sellers until October 31 to lock in FBA fee credits | https://ppc.land/amazon-gives-sellers-until-october-31-to-lock-in-fba-fee-credits/ | practitioner news (PPC Land) | 2026-11-09 (verifier) | Reported 2026 New Selection Program terms (not confirmed on an Amazon page) |
| Product Pricing v2022-05-01 and Customer Feedback v2024-06-01 models | https://github.com/amzn/selling-partner-api-models | official spec (public repo) | 2026-11-09 (verifier) | SP-API operation names |
| Is there an Amazon honeymoon period… | https://myamazonguy.com/is-there-an-amazon-honeymoon-period-and-how-do-i-grow-sales-fast/ | practitioner (My Amazon Guy, 2021) | 2026-11-09 | 15–30 days; by-product claim |
| Set up an AMC campaign system for ranking pressure | https://help.scaleinsights.com/en/knowledge-base/set-up-an-amc-campaign-system-for-ranking-pressure | practitioner tool help (Scale Insights) | 2026-11-09 | Tiered fixed-step bid raises for ranking |
| What Is Amazon Ads Agent? unBoxed 2026 Changes for Sellers | https://canopymanagement.com/amazon-ads-agent/ | practitioner (Canopy) | 2026-11-09 | Fetched, light |
| cx-amazon-ads skill and door reference | local package `cx-amazon-ads/skills/amazon-ads/SKILL.md`, `references/door.md` | cx package | 2026-11-09 | The open door, regional origins, scope header |
| Get started with manual campaigns (API guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/manual-campaigns.md | official API doc | 2026-11-09 (gap fill) | Five-step manual sequence; completeness rule; "all entities have an `ACTIVE` status" |
| Get started with auto campaigns (API guide, re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/auto-campaigns.md | official API doc | 2026-11-09 (gap fill) | Auto sequence; complete after the product ad; auto target ids via query/targets |
| Sponsored Products campaign structure (API guide, re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/campaign-structure.md | official API doc | 2026-11-09 (gap fill) | "requires making multiple calls"; minimum entities; campaign-level negatives |
| Sponsored Products campaigns (API guide, re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/campaigns.md | official API doc | 2026-11-09 (gap fill) | v1 create body for manual and auto; 207 reply with example DELIVERING |
| Sponsored Products ad groups (API guide, re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/ad-groups.md | official API doc | 2026-11-09 (gap fill) | campaignId first; names unique within a campaign; default bid inheritance |
| Sponsored Products product ads (API guide, re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-ads.md | official API doc | 2026-11-09 (gap fill) | SKU for sellers, ASIN for vendors; required fields; SKU from product metadata |
| Negative keyword targeting (API guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/keywords.md | official API doc | 2026-11-09 (gap fill) | Campaign- and ad-group-level negatives through create/targets |
| Amazon Ads API v1, Sponsored Products model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISP_prod_3p.json | official spec | 2026-11-09 (gap fill) | Create schemas and required fields; SPCreateState; SPTargetType; SPBidStrategy; SPDeliveryReason; no idempotency parameter |
| Sponsored Products 3.0 OpenAPI (re-read for creates) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official spec | 2026-11-09 (gap fill) | Create paths and media types; required fields; PROPOSED and draft states; INCOMPLETE serving statuses; AUTO_FOR_SALES "maximum of 100%" |
| Amazon Ads API v1 merged OpenAPI (re-read) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official spec | 2026-11-09 (gap fill) | DeliveryReason CAMPAIGN_INCOMPLETE, AD_GROUP_INCOMPLETE; error codes |
| MCP tool specification: campaign management | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/campaign_management.json | official spec | 2026-11-09 (gap fill) | `create_singleshot_sp_campaign` description and input schema; no state field, no response schema |
| Connecting to the Amazon Ads MCP Server | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/get-started.md | official API doc | 2026-11-09 (gap fill) | MCP endpoints on advertising-ai* hosts |
| All releases (re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md | official API doc | 2026-11-09 (gap fill) | MCP open beta note, 2026-02-18: single-shot "in one call… five or more separate operations" |
| Troubleshoot your campaign status (help GEC8BVH43CU9UNYH) | https://advertising.amazon.com/help/GEC8BVH43CU9UNYH | official help | 2026-11-09 (gap fill) | Console "Draft" status; other console statuses |
| Bidding strategies for Sponsored Products (help GCU2BUWJH2W3A8Z7) | https://advertising.amazon.com/help/GCU2BUWJH2W3A8Z7 | official help | 2026-11-09 (gap fill) | Up and down "up to 100% for all placements"; $1.00 to $2.00 example |
| Guide to dynamic bidding - up and down (re-read) | https://advertising.amazon.com/library/guides/dynamic-bidding-sponsored-products | official guide | 2026-11-09 (gap fill) | "up to 100% for all placements"; published 2025-05-07, modified 2026-10-09 |
| An author's guide to Sponsored Products | https://advertising.amazon.com/library/guides/authors-guide-to-sponsored-products | official guide | 2026-11-09 (gap fill) | Up and down "up to 100%" top of first page, "up to 50%" elsewhere; published 2023-09-07, modified 2026-10-09 |
| Does Advertising Serve as a Signal? (Sahni and Nair, REStud 2020) | https://gwern.net/doc/economics/advertising/2020-sahni.pdf (doi 10.1093/restud/rdz053) | research | 2026-11-09 (gap fill) | Zomato experiment; disclosure +77% calls; fewer ratings benefit more; age not significant; newer restaurants advertise more |
| Does Advertising Serve as a Signal? (2016 draft) | https://web-docs.stern.nyu.edu/marketing/SahniPaper.pdf | research | 2026-11-09 (gap fill) | Fetched, light: earlier draft, used only to confirm the design |
| The Market for Fake Reviews (published abstract) | https://econpapers.repec.org/RePEc:inm:ormksc:v:41:y:2022:i:5:p:896-921 | research (Marketing Science 41(5) 2022) | 2026-11-09 (gap fill) | Published abstract: short-term rating rise; causal sales effect; ratings fall, particularly for young products |
| The Market for Fake Reviews (August 2021 working paper) | https://eller.arizona.edu/sites/default/files/Hollenbeck%20Paper.pdf | research | 2026-11-09 (gap fill) | Data; 2–4-week rating fade; sales not self-sustaining; search position inertia; cold-start subgroup; sponsored listings rise; deletion lag |
| The Market for Fake Reviews (MPRA, January 2021) | https://mpra.ub.uni-muenchen.de/105507/ | research | 2026-11-09 (gap fill) | Fetched, light: earlier version |
| Design-based Analysis in DiD with Staggered Adoption (Athey and Imbens) | https://arxiv.org/abs/1808.05293 | research | 2026-11-09 (gap fill) | Unbiasedness under random adoption dates |
| Difference-in-Differences with a Continuous Treatment (Callaway, Goodman-Bacon and Sant'Anna) | https://arxiv.org/abs/2107.02637 | research | 2026-11-09 (gap fill) | Dose comparisons and selection bias; TWFE limits |
| Inferring causal impact using Bayesian structural time-series models (Brodersen et al.) | https://arxiv.org/abs/1506.00356 | research | 2026-11-09 (gap fill) | Synthetic control from covariate series |
| Advertising Spillovers in Mobile Apps (Ju, Zhao and Aral) | https://arxiv.org/abs/2504.16151 | research (preprint) | 2026-11-09 (gap fill) | Shutoff cut organic installs 20–30%; rank-mediated |
| amzn/ads-advanced-tools-docs issue search | https://github.com/amzn/ads-advanced-tools-docs/issues (via the public GitHub search API) | official repo, field reports | 2026-11-09 (gap fill) | No issues on the single-shot tool |
| cx-keepa product file reference (re-read) | local package `cx-keepa/skills/keepa/references/product-file.md` | cx package | 2026-11-09 (gap fill) | `csv` slot 3 reference sales rank; `salesRanks[category]` |
| cx-keepa product file reference | local package `cx-keepa/skills/keepa/references/product-file.md` | cx package | 2026-11-09 | listedSince, releaseDate, rating slots, couponHistory |
| Listing playbook help-page captures | local file `cx-listing-playbook/research/method/help-page-access.md` | cx research (captures of 2026-10-14) | 2026-11-09 | Featured Offer removal; deal, coupon, fee, review-sharing rules (captured by another seat) |

Unreachable (with reasons):
- **Seller Central help pages**: G201119120 (New Seller Incentives help), G202111490 (Amazon deals), GJHCPEFJ5JJQD52D (Coupon eligibility criteria), G202111590 (deal fees), G200418100, G37911 and G201687550 (Featured Offer), GM2ADTH3XH3A5N57 (Prime Day readiness), G74DLBUEHT5GY88C (review sharing), and the Request a Review and Vine help topics.
  - A plain GET serves only a shell with a banner. The content comes through the help hub's GetHelpTopic call, which this seat may not make.
  - Where a 2026-10-14 capture by the listing-playbook seat exists, it is cited as a capture. The Request a Review and Vine help topics have no capture here.
- **Suffixed quick-guide PDFs** (`Quickguide_30-days-to-new-product-success_Q4-2025.pdf` and the other quarter-suffixed names): 404. The unsuffixed file served.
- **API guide paths that do not exist at the guessed path**: all 404 on the CloudFront Markdown host.
  - `guides/sponsored-products/bid-suggestions/overview`;
  - `guides/sponsored-products/budget-recommendations` and `…/initial-budget-recommendations`;
  - `guides/sponsored-products/target-promotion-groups`;
  - `guides/eligibility/product/overview`;
  - `guides/campaign-management/entities/campaigns`.

  The specifications were read instead.
- **API documentation navigation index** (toc.json and similar): 404. No table of contents could be listed.
- **`advertising.amazon.com/legal/terms-conditions/sponsored-ads-new-seller-incentives-promotion`** and **`…/sponsored-ads-signup-promotion`**: both redirect to the Amazon Ads *About us* page (verifier, 2026-11-09). The sign-up promotion terms could not be read.
- **`advertising.amazon.com/ad-specs/en/ecommerce`**: 404 (verifier, 2026-11-09); the spec now lives at `/resources/ad-specs/ecommerce`.
- **Scale Insights helpdesk, *Workflow series: ranking part 3***: no response (no HTML returned). **Scale Insights blog, event recap with Anthony Nguyen**: 404.
- **Seller Sessions article *The Cold Reality of the Honeymoon Period and External Traffic* (McMillan and Padurariu)**: the article itself was not located. The verifier read the episode page (Part 1, 2024-09-05); the article's content is known only through that page and the Best at Amazon and Code3 summaries.
- **Jungle Scout and Amazon, full *New Product Success Playbook***: behind a lead form. Only the landing page was read.
- **Coupons, Deals, Vine and Promotions dashboards in Seller Central, and the Ads console's Promotions page**: these need sign-in, and were not attempted.
- **Gap fill 2026-11-09:**
  - **Marketing Science article page** for He, Hollenbeck and Proserpio (https://pubsonline.informs.org/doi/10.1287/mksc.2022.1353): HTTP 403 to a plain fetch. The published abstract was read on EconPapers and the full text as the August 2021 working paper.
  - **LandingCube, *Amazon PPC and Organic Search Rankings*** (https://landingcube.com/amazon-ppc-impact-on-organic-search-rankings/): served a bot-verification page, so no content was read. A search summary attributed a sceptical view of "every PPC sale boosts your organic rank" to it; that view is not used here.
  - **Guessed API guide paths** `guides/sponsored-products/keywords`, `…/negative-targeting`, `…/keywords/keywords`, `…/negative-keywords`, `…/product-targeting/product-targeting` and `…/targets`: 404 on the CloudFront host. The working path for negatives is `guides/sponsored-products/negative-targeting/keywords`.
  - **GitHub issue search** on `amzn/ads-advanced-tools-docs`: the first queries ran ("singleshot", "create_singleshot_sp_campaign": 0 results). Later queries ("duplicate campaign", "CAMPAIGN_INCOMPLETE", "NAME_NOT_UNIQUE") were refused by GitHub's anonymous rate limit.

## Open questions

1. **Featured Offer after September 2026.** The captured help page says Amazon "no longer maintains a seller eligibility requirement" for the Featured Offer. The ads guides read today still require the product to be "eligible to be the featured offer", and the eligibility API still has `NOT_IN_BUYBOX`. Does the ads requirement now mean only "this offer is currently the Featured Offer"? No page read says.
2. **Bid recommendations for product targets.** Largely settled by the spec's version notes: v4 "supports keyword, auto and product targets in all marketplaces", and the quickstart's "will be added in the future" predates it. What stays open is whether v4's removal of impact metrics also applies to the keyword-recommendation call's v5 impact metrics, which the keyword guide still describes.
3. **The promotions API.** `query/promotionOffers` and `query/promotionRewards` are BETA. It is not known whether they list the New Seller Incentives credit, the New ASIN Adoption credit and the sign-up credit, or only some of them, or for which accounts.
4. **Incentive figures.** The incentives page, the 2024 terms, the older full-guide PDF and the FBA New Selection page give different credit figures and windows. Examples: Vine $200 within 90 days of Brand Registry, against $75 within 60 days of a buyable offer; and an SP credit of up to $1,000 (incentives page and 2024 terms agree) against $50 in the 2025 PDF. Do the Vine credits stack, or has one replaced another? PPC Land reports a 2026 revision of FBA New Selection (D7) that no Amazon page read here confirms.
5. **"Complimentary marketing placements".** These are what completing the prelaunch checklist earns. Neither the checklist nor the roadmap post says what the placements are, how qualification is checked, or whether advertising is one of the checked steps.
6. **`NEW_ASIN` window.** The Recommendations spec says "recently been added to the catalog" without a number of days. It is also unknown how this relates to `createdDate`, to New & Notable's 12 months, and to the 90-day incentive windows.
7. **Coupon badge in Sponsored Products ads.** Ad Badger says the badge shows in the ad. No Amazon page read says so, and no ads report field marks an ad impression that showed a coupon.
8. **Review Requests.** Its general availability, its marketplaces beyond the US, review-specific API metrics (today console only; standard delivery metrics are in the reporting API), how accounts are enabled during the beta, and how its reviews are labelled to shoppers.
9. **Review deprecation.** A seller on Amazon's roadmap post asks whether "Amazon's review deprecation is still planned". Neither seat found an Amazon statement on what that refers to. Unread search results point to the variation review-sharing change and to the retirement of a Customer Reviews dashboard; neither is confirmed here.
10. **Do ad-attributed sales count toward organic rank?** No Amazon page read here answers this. It is cross-referenced to `ads-organic-and-total.md`.
11. **Production status of the empirical-Bayes prior.** The CIKM 2022 paper reports an A/B test, and the substitute-boosting paper states production use since 2025. Whether both run together is unknown.
12. **Eligibility 404 on a fresh listing.** It is unknown whether a newly created listing returns 404 from `eligibility/product/list` until the ads catalog picks it up, and if so for how long.
13. **Down only versus up and down at launch.** Amazon's pages recommend each in different contexts. No Amazon experiment comparing them for new ASINs was found.
14. **Indexing lag.** Practitioners (Ad Badger reporting Wishon) say auto campaigns match poorly until a new ASIN is indexed. Amazon states no indexing time for a new ASIN in the ads documentation read here; the listing playbook may hold one.
15. **New Product Campaigns.** It is unknown whether this managed service is still offered under Amazon Ads Agent and Full-Funnel Campaigns, and whether it is open beyond the US. The advertising.amazon.com navigation still lists "New Product Campaigns" under technology and services on 2026-11-09; it launched as GA in the U.S. on 2024-10-15.
16. **Reporting migration.** The search term data a launch harvests from comes from Reporting v3 today; v3 stops delivering data on 2027-06-30. Which Reporting API v1 report and fields carry the same search-term view is owned by `method/reporting.md`.
17. **What `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE` cover.** Neither model describes them. It is not stated whether a manual ad group with ads but no targets reads `AD_GROUP_INCOMPLETE`, or how soon after a create the status appears.
18. **Duplicate checks on ads and targets.** The models carry duplicate reasons, but no page read says whether a second identical keyword or a second product ad for the same SKU in one ad group is refused or created.
19. **The single-shot tool's failure behaviour and product identifier.** The MCP specification gives no response schema and no statement on what a failure part-way leaves. Its `advertisedProduct` takes only `ASIN`, while a seller's REST product ad uses a SKU.
20. **API drafts.** SP 3.0 lists `PROPOSED` ("Upcoming Feature") and two "Draft Entity Only" states. Whether a draft will let a whole campaign be built and submitted at once through the API is not described.
21. **Dynamic bidding ceiling outside top of search.** Amazon's help page, library guide and models say 100%, and its author's guide says 50%. Owned by `areas/bids-and-placements.md` (its open question 1).
22. **Ad spend and lasting rank on Amazon.** No published study read measures whether launch-window Sponsored Products spend leaves a lasting organic effect after the spend stops (*Published research*).

## Positions

Each position is a fact: a definition, an Amazon rule, a documented mechanism, a measured effect with its source, or a named practitioner's claim stated as theirs. Sources are Amazon-first.

**P-launch-1.** A Sponsored Products ad serves only for a product that is eligible to be the Featured Offer and in stock. An advertised product that goes out of stock is paused within its campaign automatically. [official] *New advertiser success guide*; *How to improve your product detail page for advertising*; API *Sponsored Products product ads*.

**P-launch-2.** Sponsored Products needs a Professional selling plan or a vendor account. Amazon does not support adult, used, refurbished or closed-category products in it. [official] *New advertiser success guide*.

**P-launch-3.** Sponsored Brands, display ads and Stores need Brand Registry. Brand Registry needs a logo with the brand name on the product or packaging, and a pending or registered trademark. [official] *Advertising | Sell on Amazon*; *Amazon Brand Registry | Sell on Amazon*; Eligibility OpenAPI (NOT_BRAND_REPRESENTATIVE, NO_BRAND_RELATIONS).

**P-launch-4.** `POST /eligibility/product/list` reports per product an `overallStatus` (ELIGIBLE, ELIGIBLE_WITH_WARNING or INELIGIBLE) with named reasons, including NOT_IN_BUYBOX, OUT_OF_STOCK, LISTING_SUPRESSED, MISSING_IMAGE, MISSING_TITLE and VARIATION_PARENT. Amazon defines `ELIGIBLE_WITH_WARNING` as a product that "may not receive impressions". [official] Eligibility OpenAPI.

**P-launch-5.** Amazon's advice that an advertised product have five or more reviews at 3.5 stars or higher is guidance. No eligibility reason in the Ads API reads a review count or rating. [official] *New advertiser success guide*; Eligibility OpenAPI.

**P-launch-6.** As captured on 2026-10-14, Seller Central's *Featured Offer eligibility* page reads: "As of September 2026, Amazon no longer maintains a seller eligibility requirement". The ads guides read on 2026-11-09 still state that an advertised product "must be eligible to be the featured offer". [official, via capture] G200418100 (listing-playbook capture); [official] *How to improve your product detail page for advertising*.

**P-launch-7.** Product Selector's `POST /product/metadata` returns `createdDate`, defined as "Date the item was first available on Amazon", together with `availability`, `bestSellerRank` and eligibility codes. Its `sortBy: SUGGESTED` returns the products Amazon describes as "most likely to engage customers". [official] Product Selector OpenAPI.

**P-launch-8.** Amazon's recommendation API has a grouping, `NEW_ASIN`, for "unadvertised ASINs that have recently been added to the catalog". Its recommendation types include NEW_CAMPAIGN, NEW_PRODUCT_AD and NEW_KEYWORD. [official] Recommendations OpenAPI.

**P-launch-9.** For a seller new to Amazon, Amazon offers Sponsored Products ad credits. They are earned by creating a first Sponsored Products campaign within 90 days of listing the first buyable ASIN and spending within 30 days of that campaign's launch. [official] *New Seller Incentives | Sell on Amazon*; *New Seller Sponsored Products Promotion (2024)* terms. The amounts and tiers are read from the seller's own offer at run time.

**P-launch-10.** Under the 2024 new-seller terms, the ad credit is issued within 14 days after the 30-day window and is valid for 30 days. It cannot pay for the ads bought during the window that earned it. [official] *New Seller Sponsored Products Promotion (2024)* terms.

**P-launch-11.** The BETA operations `POST /adsApi/v1/query/promotionOffers` and `POST /adsApi/v1/query/promotionRewards` expose an account's promotion offers and rewards. Offers carry status (AVAILABLE, IN_PROGRESS, MISSED or REWARDED), campaign-launch and spend criteria with dates and tiers, and a terms URL. Rewards carry the reward, remaining reward and end time. [official] Amazon Ads API v1 BETA OpenAPI.

**P-launch-12.** Amazon Vine requires a Professional plan, FBA offers, and a Brand Representative or Reseller role on a Brand Registry brand or generic products. Up to 30 reviews per parent are possible. A product can enroll before launch with a future launch date, and an existing product needs fewer than 30 reviews. [official] *Amazon Vine | Sell on Amazon*.

**P-launch-13.** Amazon recommends enrolling in Vine with inventory available at least three weeks before the planned launch date. It states that Vine reviews can be visible on day one. [official] *Amazon Vine | Sell on Amazon*; *New product success* full guide PDF.

**P-launch-14.** Under the coupon eligibility rules as captured, a product with no reviews is not barred by the rating rule. The rating floors apply to products with 1–4 reviews (2.5 stars) and 5 or more reviews (3 stars), and Amazon's full guide says "Coupon quality validation rules do not apply to new products". [official, via capture] *Coupon eligibility criteria* GJHCPEFJ5JJQD52D v14; [official] *New product success* full guide PDF.

**P-launch-15.** Amazon deals require the product to have a sales history on Amazon and at least a 4-star rating, and the seller an overall rating of at least 3.5 stars. Deals are invite-only. [official, via capture] *Amazon deals* G202111490 v25.

**P-launch-16.** Amazon's 30-day roadmap lists, for day one, active listings with inventory in stock, Sponsored Products campaigns and coupons. It lists complimentary marketing placements as a benefit of completing the prelaunch steps. [official] *New 30-day roadmap helps you launch products successfully* (Seller Forums, 2025-08-28); *30 days to new product success* quick guide.

**P-launch-17.** For a new advertiser's first campaign, Amazon recommends Sponsored Products with automatic targeting, started immediately with no end date. [official] *New advertiser success guide*; *Getting started guide for sponsored ads*; API *Sponsored Products auto campaigns*.

**P-launch-18.** Amazon's guidance on when to add manual targeting differs by guide. The targeting guide suggests letting an auto campaign run "for about two weeks before creating a manual campaign". The new ASIN playbook says "Using both automatic and manual targeting creates a balanced advertising strategy" and, under post-launch optimization, to "run automatic and manual targeting campaigns together"; the getting-started guide pairs an auto and a manual campaign per product group. [official] *A guide to targeting with Sponsored Products*; *Intermediate and advanced new ASIN playbook*; *Getting started guide for sponsored ads*.

**P-launch-19.** A Sponsored Products campaign's targeting type cannot be changed once the campaign is live. An auto ad group gets four auto targeting expressions automatically, as theme targets (close match, loose match, substitutes, complements). Without per-expression bids they use the ad group default bid. [official] *A guide to targeting with Sponsored Products*; API *Sponsored Products auto targeting*; v1 `ThemeMatchType`.

**P-launch-20.** Amazon provides a mechanism to promote an auto campaign's keyword and product targets into manual campaigns: target promotion groups. Its recommendations are described as "based on performance heuristics" that the spec does not state. [official] Sponsored Products 3.0 OpenAPI (`/sp/targetPromotionGroups/recommendations`, `/sp/targetPromotionGroups`, `/sp/targetPromotionGroups/targets`).

**P-launch-21.** Amazon's suggested bids are "calculated from a group of recent winning bids for similar products" and are offered as low, median and high. Their impact metrics "are not estimates of expected performance". Because they are computed from similar products, they exist for an ASIN with no history of its own. The v4 content type of `/sp/targets/bid/recommendations` supports keyword, auto and product targets; the v3 content type was shut off on May 15, 2025. [official] Ads API *Theme-based bid suggestions quickstart guide*; Sponsored Products 3.0 OpenAPI; *Deprecations*.

**P-launch-22.** For a campaign that does not yet exist, the API returns keyword suggestions (`KEYWORDS_FOR_ASINS`), bids (`BIDS_FOR_NEW_AD_GROUP`), product and category targets, and a daily budget (`/sp/campaigns/initialBudgetRecommendation`). The budget comes with seven-day benchmark ranges, and a `dailyBudget` of `-1` means "we don't have enough information". [official] Sponsored Products 3.0 OpenAPI; API *Sponsored Products keyword recommendations*.

**P-launch-23.** Amazon recommends starting Sponsored Products with a daily budget of $10 or the local equivalent. The API's minimum daily budget is lower (US 1). [official] *Best practices for your Sponsored Products ads*; *Getting started guide for sponsored ads*; Ads API *Limits*.

**P-launch-24.** Under "Dynamic bids - up and down", Amazon's library guide and help page say a bid may be raised or lowered by up to 100% for all placements, and the SP 3.0 and v1 models say "by a maximum of 100%". Amazon's author's guide still says up to 100% for top of the first page and up to 50% for other placements; the conflict is owned by P-bids-and-placements-8. Down only never raises a bid above the set bid. Amazon recommends down only for a first campaign in a new country. Its keyword-recommendation guide shows up and down for a new ad group sorted by clicks, and fixed bids for one sorted by conversions. [official] *Guide to dynamic bidding - up and down*; *Bidding strategies for Sponsored Products* (help GCU2BUWJH2W3A8Z7); v1 `BidStrategy`; SP 3.0 `SponsoredProductsBiddingStrategy`; *An author's guide to Sponsored Products*; *Checklist for new international ad campaigns*; API *Sponsored Products keyword recommendations*.

**P-launch-25.** Rule-based bidding needs a campaign that has run at least 10 days and has had at least 10 conversions in the last 30 days, at or above a marketplace minimum daily budget. A newly launched campaign is therefore not eligible. [official] API *Sponsored Products rule-based bidding overview*.

**P-launch-26.** Amazon's guides recommend these time marks for a new campaign:
- "In the first week, monitor your metrics at least twice a week";
- "Test different match types for at least 1-2 weeks to gather enough data before pausing any keywords";
- evaluate a keyword's performance "after it has received at least 20 clicks" before adding it as a negative, and "let your negative keywords run for two weeks or more, before making any changes to your strategy".

[official] *Best practices for your Sponsored Products ads*; *A guide to targeting with Sponsored Products*.

**P-launch-27.** No Amazon page read on 2026-11-09 claims, in Amazon's own voice, a "honeymoon" ranking boost for new products. The word appears on sell.amazon.com only in a seller's quote ("we refer to that first 30 days as the honeymoon period"). [official] *Tips for new product success*.

**P-launch-28.** Amazon's Review Requests overview states that "New products face a cold-start problem" and that the format gives them "a faster path to authentic reviews". [official] Ads API *Review requests overview*.

**P-launch-29.** Amazon researchers report that new items "typically cross the cold start barrier through very specific queries", and that a prior from similar items with early stopping raised new-product impressions and purchases in an online A/B test. The paper says sponsored results are "essential instruments for sellers to push their new products into the search feedback wheel". [research] Han et al., CIKM 2022.

**P-launch-30.** Amazon-affiliated researchers state that a ranking model that gives new items behavioural signals borrowed from their substitutes "has been launched in production and has served customers since 2025"; the paper names the platform only as "a large E-commerce platform". [research] Dong et al., arXiv 2602.14502.

**P-launch-31.** Amazon's cold-start patents give example durations, not operating figures: a cold-start condition "such as ninety days", and a switch from prior to posterior after "for example, three days". One also makes an item ineligible as a cold-start item when "the corresponding item query pair has sufficient interaction data", even if the item was recently added. [research] US20230367818A1 / US12346379B2; US11269898B1.

**P-launch-32.** Practitioners disagree on the honeymoon:
- My Amazon Guy (Steven Pope, 2021) puts it at "Typically 15 – 30 days";
- m19 at "a couple of weeks… not a hardcoded duration", at the search-term level;
- Best at Amazon calls it "a myth", and Code3 says the cold-start system "debunks" it, describing posterior estimation from "as soon as five days after a product is purchasable";
- Canopy (Chuck Kessler) says "Amazon has never confirmed one, and we don't plan launches around it."

[opinion] those pages.

**P-launch-33.** Amazon's Seller Code of Conduct, as clarified on the Seller Forums, prohibits search-rank manipulation by any name, including "two-step urls", "super urls", "funnels", "treasure hunts" and "search-find-buy". It also prohibits off-Amazon rebates or discounts that drive customers to products sold without those incentives on Amazon. The seller is responsible for third parties acting for the account. [official] *Clarification of Amazon's Policy on Rebates, Coupons, and other Marketing Incentives*.

**P-launch-34.** Amazon's launch multiples are internal data on ad-attributed outcomes that compare groups of advertised products: "New products observed 36 times more clicks when advertised, compared to products that are not new", and "New products are 231 times more likely to generate ad-attributed sales when advertised, compared to products that are not new". They are not published incrementality experiments. [official] *A product advertising strategy*; *Best practices for your Sponsored Products ads*.

**P-launch-35.** Amazon's ads guidance links launch advertising to organic visibility only in hedged terms: video ads "help boost organic rankings", and ads "can help increase detail page views and product reviews". No Amazon page read states that ad-attributed sales count toward organic rank. [official] *Intermediate and advanced new ASIN playbook*; *How to create your new product launch strategy*.

**P-launch-36.** In a Yelp field experiment, advertising raised purchase-intention outcomes by 7–19% and reviews by 5%. Newer independent firms and firms with better ratings and more reviews gained more, and the effects disappeared once the ads stopped. [research] Dai, Kim and Luca, NBER WP 30925.

**P-launch-37.** Amazon's Review Requests (US beta) is a Sponsored Products campaign with goal ENGAGEMENT, which cannot be changed afterward. It uses manual bids and an INTERESTED_AUDIENCE theme target, and is billed per rating or review left on the ad card. It serves products with fewer than 1,000 reviews and pauses at 1,000. During the beta it is enabled per advertiser account, and a create request from an account not yet enabled returns an error. [official] Ads API *Review requests* guides; v1 `Goal`.

**P-launch-38.** New & Notable is Amazon's designation for products new to market in the last 12 months, subject to eligibility. Amazon reports at least 22% higher click-through rates for ads that message newness. [official] *Amazon Ads introduces New Product Campaigns*; *How to create your new product launch strategy*.

**P-launch-39.** Canopy Management structures a launch as exploration (auto, broad, competitor product targets), intent capture (exact match with negatives back in exploration) and brand presence. It opens bids above Amazon's suggestion. Ad Badger opens manual bids conservatively. ecomcrew starts narrow with exact match and high bids and widens later. [opinion] Canopy; Ad Badger; ecomcrew.

**P-launch-40.** FBA New Selection enrolls a new seller automatically when the first shipment is created within 90 days of listing the first buyable product. For new parent ASINs, it gives Vine and coupon-fee credits and 120-day storage waivers. [official] *What is the FBA New Selection program?* (dated Jan 14, 2026; PPC Land reports revised terms from July 30, 2026, unconfirmed on an Amazon page).

**P-launch-41.** Amazon's API guides build a Sponsored Products campaign by separate creates in order: campaign, then ad group (which needs the `campaignId`), then product ad (which needs the `adGroupId`, with a SKU for a seller or an ASIN for a vendor), then, for a manual campaign, at least one target or keyword per ad group; negatives are optional, at campaign or ad group level. In v1 these are `POST /adsApi/v1/create/campaigns`, `/adGroups`, `/ads` and `/targets` (negatives with `negative: true`); in SP 3.0 they are `POST /sp/campaigns`, `/sp/adGroups`, `/sp/productAds`, `/sp/keywords`, `/sp/targets` and the four negative paths. [official] API guides *Sponsored Products campaign structure*, *Get started with manual campaigns*, *Get started with auto campaigns*, *Sponsored Products ad groups*, *Sponsored Products product ads*, *Negative keyword targeting*; SP v1 and SP 3.0 models.

**P-launch-42.** Amazon calls an auto campaign "complete and ready to run" once it has at least one active campaign, ad group and product ad, and a manual campaign once it also has a targeting expression or keyword. With a start date of today it "starts serving immediately". An auto campaign can therefore be serving before negatives sent in a later call exist. [official] *Get started with auto campaigns*; *Get started with manual campaigns*.

**P-launch-43.** The creates share no transaction and take no idempotency key. Each answers 207 with per-item `success` and `error` matched by `index`, so a chain can stop part-way and leave, for example, a campaign with no ad group or an ad group with no ad. The API reports such entities with the serving statuses and delivery reasons `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE`, which the models do not describe further. [official] SP v1 model; SP 3.0 model; v1 merged model; *Well-Architected Framework: Fundamental component* (via `method/ads-api-surface.md`).

**P-launch-44.** A seller's campaign names are unique per account, so a repeated campaign create with the same name is refused (`NAME_NOT_UNIQUE` in SP 3.0, `FIELD_VALUE_NOT_UNIQUE` in v1), while a vendor's is not. Ad group names are unique only within a campaign. [official] SP v2 and SB v3 models (via `method/ads-api-surface.md` section F); *Sponsored Products ad groups*; SP 3.0 and SP v1 models.

**P-launch-45.** Both create APIs accept `PAUSED` as the initial state (SP v1 `ENABLED` or `PAUSED`; SP 3.0 also `PROPOSED`, described as an "Upcoming Feature"), and Amazon's manual guide conditions immediate serving on "all entities" having an active status. [official] SP v1 `SPCreateState`; SP 3.0 `SponsoredProductsCreateOrUpdateEntityState` and `SponsoredProductsEntityState`; *Get started with manual campaigns*.

**P-launch-46.** The Amazon Ads MCP server's `create_singleshot_sp_campaign` "Creates a complete Sponsored Products campaign (campaign + ad group + ads) across multiple marketplaces in a single operation", as "ONE global campaign", with one campaign per call, an ASIN-only advertised product and at most one target object. Its specification states no response and no behaviour on a failure part-way. It is served on the `advertising-ai*` MCP hosts, which the `cx-amazon-ads` door, whose origins are the `advertising-api*` hosts, does not reach. [official] MCP `campaign_management.json`; *All releases* (2026-02-18); *Connecting to the Amazon Ads MCP Server*; cx-amazon-ads SKILL.md.

**P-launch-47.** In a randomized experiment on Zomato's app (about 200,000 users, 600+ restaurants, 2014), labelling a paid listing as an ad raised calls to the restaurant by 77% against the same listing unlabelled. The label's effect was larger for restaurants with fewer past ratings, and its interaction with restaurant age was not statistically significant. Newer restaurants advertised more. [research] Sahni and Nair, Review of Economic Studies 87(3), 2020.

**P-launch-48.** On Amazon, products that bought fake reviews saw a "significant but short-term increase in average rating and number of reviews", with ratings back to their earlier level within two to four weeks. Sales rose and then "fall significantly after the fake review campaign ends", while keyword search position "does not substantially reverse even after two months". Products under four months old with eight or fewer reviews gained more sales at first and saw "a similar drop-off afterward". [research] He, Hollenbeck and Proserpio, Marketing Science 41(5), 2022 (published abstract; August 2021 working paper).

**P-launch-49.** In the same Amazon data, sellers raised their use of sponsored listings and cut prices while buying reviews, and Amazon eventually deleted about 43% of these products' reviews, with an average lag of over 100 days. [research] He, Hollenbeck and Proserpio (August 2021 working paper).

**P-launch-50.** A difference-in-differences comparison across units that adopt a treatment at different dates is unbiased for a weighted average effect "under random assignment of the adoption date". With a treatment of varying dose, parallel trends identify effects on the treated, but "comparing these parameters across treatments is challenging because parallel trends does not rule out selection bias". [research] Athey and Imbens, arXiv 1808.05293; Callaway, Goodman-Bacon and Sant'Anna, arXiv 2107.02637.

**P-launch-51.** At a US mobile game developer, a global shutoff of app-install ads cut organic installs by 20–30%, and the link between ad spend and organic installs disappeared once store rankings were accounted for: paid installs raised category rank, which raised organic visibility. This is app-store data, not Amazon data. [research] Ju, Zhao and Aral, arXiv 2504.16151 (preprint).

### Seat's positions (enter no skill)

- [seat] Read together, Amazon's pages place the launch's first decisions in retail state (Featured Offer, stock, eligibility reasons) before ad settings. Every ad-side launch recommendation in Amazon's guidance assumes those gates pass.
- [seat] The API answers "what would Amazon start with" for a launch without history: suggested products, `NEW_ASIN` recommendations, bids for a new ad group, keywords for ASINs, and an initial budget. The practitioner disagreements are mostly about how far to depart from those starting points, and in which direction.
- [seat] The patent and research picture (priors from similar items or substitutes, early stopping of poor performers, exit on interaction data) explains why practitioners agree that early performance weighs more without agreeing on a duration. A duration is not in Amazon's public record.
- [seat] The new-seller credit's timing (pay first, credit later, valid 30 days, not for the earning spend) matters for a seller's cash in the first 60 days more than its amount.
- [seat] Review state decides what a launch can use: no reviews means coupons yes, deals no, Vine yes (fewer than 30), Review Requests yes (fewer than 1,000). It also decides how Amazon's own review advice for advertising reads. A launch skill reads the counts at run time.
- [seat] Of the partial results a create chain can leave (section P4), only one spends: a complete campaign whose negatives, or some of whose positive targets, were not written. The others leave entities that cannot serve and that, for a seller, hold a campaign name.
- [seat] A launch has no pre-period, so a before-and-after of the ASIN measures the whole launch, not the ads. Sibling launches, staggered marketplaces, dose changes inside the launch and synthetic controls are the comparisons that can separate the ads, and each rests on an assumption the seller's own choices usually break (spend follows expectations; launch dates are chosen).
- [seat] He et al.'s search-position inertia and falling sales, read beside the cold-start patents' exit on interaction data, fit a picture where early traffic can move a product's position for a while, and the product's ratings and conversion decide whether sales hold. This is a reading across sources, not a measured effect of ads.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** I re-opened every page the file cites by a plain GET, about 95 fetches. The Ads API guides were read as Markdown from the CloudFront host, and the eight OpenAPI specifications were downloaded from the URLs in `contracts.json` and parsed for paths, enums and descriptions. The advertising.amazon.com, sell.amazon.com, Seller Forums, Amazon Science, arXiv, NBER, Google Patents and practitioner pages were fetched as HTML and reduced to text. The two Amazon PDFs and three paper PDFs (CIKM 2022, NBER w30925, arXiv 2602.14502) were read as full text. I searched each verbatim quote in the normalised text (curly quotes and dashes folded) and read the surrounding passage to check its meaning, its attribution and its footnote. The listing-playbook captures (`help-page-access.md`) and the `cx-keepa` and `cx-amazon-ads` references were checked locally against the lines they are cited for; the Seller Central help pages themselves were not re-read, because their content comes only through the forbidden content call. I checked the API *All releases* and *Deprecations* pages for 2025–2026 changes, and ran web searches on New Product Campaigns, Vine and FBA New Selection in 2026, review-sharing changes, and the Seller Sessions article. About 300 claims were checked, and most quotes were found verbatim.

**Corrections (was → now).**
1. D4 and Pages read: BETA spec file `AmazonAdsAPIALLMerged_BETA.json` → `AmazonAdsAPIALLMerged_prod_3p_BETA.json` (the contracts index name).
2. D2: "The US tiers in the body are $50 / $200; a $1,000 tier is shown in the page header" → the terms body itself has the third tier, "$1,000 or more … to receive $1,000 in Ad Credits". Open question 4 is corrected to match.
3. D1: the primary URL is `/grow` (same content at `/incentives`) → `/incentives`, with `/grow` redirecting there.
4. D2: the SP product page URL `/blog/new-bidding-and-targeting-options-for-sponsored-products` → the redirect target `/solutions/products/sponsored-products`, under its real title; the banner's "within 30 days of launching their first campaign" sentence is added.
5. D3: "the sign-up promotion terms exist as a separate offer" → that URL redirects to *About us* and is unreadable; the claim is removed and the URL listed as unreachable. The SB launch promotion's qualifying action and 30-day expiry are added.
6. E: the getting-started guide's "We found that Amazon Sponsored Products can effectively increase traffic for a new product…" was tagged as Amazon's guidance → it is a quote from Wela Wen of Anker, an advertiser, published by Amazon.
7. E, O, Stable 14, P-launch-34: "each figure compares advertised products with unadvertised ones" → the pages say the 36x, 231x, 321x and 260x compare new with not-new products and suggested with not-suggested products, all advertised. The seat reading is rewritten.
8. E/O: the 231x figure carried footnote "WW, Dec 2021 – May 2023" → its own footnote is "WW, 3/26/23-4/1/23". The Dec 2021–May 2023 note (limited to sellers with 6+ months of SP campaigns) belongs to the 321x figure.
9. O: the +65% / +75% deals-and-coupons figure is now worded as Amazon's comparison "to when the deal or coupon product was not advertised". The 6x New Seller Guide figure gains "during their first 90 days, FY2023, US".
10. O intro: "Every figure is Amazon internal data" → noted that the New Product Campaigns page's footnote markers point to BCG and eMarketing/Jungle Scout (numbering looks mismatched), and that the 24.5% is Amazon's 2022 Amazon Attribution analysis.
11. E: "Up to 1,000 products fit in one ad group" (best practices) → best practices says "You can add 1,000 products to an ad group at a time"; the per-ad-group maximum is quoted from the targeting guide.
12. E: "You're launching a new product in a different category" placed beside one-ASIN-per-campaign → it is listed under "When to choose automatic targeting".
13. E, Stable 6, P-launch-18: "the intermediate playbook pairs auto with manual from the start" → its setup section says "Using both automatic and manual targeting creates a balanced advertising strategy", and the "run … together" sentence sits under post-launch optimization.
14. E: *5 steps to launch* "points to Lightning and 7-Day Deals, coupons, and Vine 'soon after listing'" → "soon after listing" applies to Vine only.
15. G: the PAT conflict between the quickstart and the spec was an open question → it is settled by the spec's v4 notes (product targets in all marketplaces; impact metrics removed). The quickstart is the open-beta v3 text.
16. G and What cx must read: "Content type v3 or v4" → v3 was shut off on 2025-05-15 (*All releases*, *Deprecations*). Use v4; v5's additions apply to existing US ad groups only. KEYWORD_GROUP is US-only.
17. G: added that v4 keyword-recommendation search term impression share exists "only … for keywords the advertiser targeted with ad impressions", so it is empty for a new ASIN.
18. G: rule-based eligibility path → `POST /sp/rules/campaignOptimization/eligibility` (the method was missing).
19. H: initialBudgetRecommendation "ad groups" → exactly one ad group (maxItems 1), with up to 50 ASINs and 100 expressions; the strategy enum is listed.
20. M, P-launch-26: "negate after at least 20 clicks over two weeks or more" → 20 clicks is when to evaluate a keyword before negating it, and "two weeks or more" is how long to let negatives run before changing strategy. The timeline rows are split.
21. I: "(the US announcement was at unBoxed 2024)" was not on the cited page → it is now sourced to the separate launch note (GA in the U.S. on 2024-10-15, "Announced at unBoxed 2024"), added to Pages read.
22. I: New & Notable "also *How to create your new product launch strategy*" → that page's own wording ("creative identifier … subject to Amazon Ads' policies, eligibility, and restrictions") is quoted.
23. J: the Review Requests beta is enabled per advertiser account, and a create from an account not enabled returns an error (added). The reporting API returns standard delivery metrics today (corrected from "console only"). The run-time note and P-launch-37 now say this.
24. K: the coupon-badge claim cited `ad-specs/en/ecommerce` ("Coupon" variation) → that URL returns 404. The current `/resources/ad-specs/ecommerce` page says coupons are surfaced automatically as savings badges in Responsive eCommerce Creatives.
25. K: the seller-promotions blog "served a 404 status", under the old title → it serves 200 as *Guide to running Amazon seller promotions, deals, coupons, and discounts* (2026-05-27). Its deal floor is "an overall rating of at least four stars", a seller rating that differs from the capture's 3.5 seller / 4-star product; this is noted.
26. K and What cx must read: `trailing4WeeksConversionRate` read as an ASIN figure → the spec defines it as the "Past 4 weeks conversion rate of target product type".
27. L: "Best Sellers Rank improves with reviews and sales" → the page's own words on BSR are quoted.
28. N: `autoManageCampaign` on "the v1 campaign" → it sits inside `autoCreationSettings`, beside `autoCreateTargets`.
29. N: "Full-Funnel Campaigns available to all US advertisers" was cited to the unBoxed page → that sentence is on the Ads Agent announcement (2026-09-29); the 67%/29% figures are on the unBoxed recap (2026-09-30). The page titles are corrected.
30. D7: added PPC Land's [opinion] report of a revised 2026 New Selection Program (July 30, 2026; October 31 confirmation), marked unconfirmed on an Amazon page. The Amazon blog is dated Jan 14, 2026.
31. Practitioners: Code3 was listed as holding a honeymoon of "five days to the posterior" → Code3 says the cold-start system "debunks the previously assumed 'Honeymoon Period' theory". The Best at Amazon "a myth" wording is added (P-launch-32 rewritten).
32. Practitioners: m19 also names "search-find-buy on these keywords" as a relevance signal; the conflict with the 2021 clarification is noted. Its forced-visibility set includes the top three competitor ASINs.
33. Practitioners: Canopy "points to an offer problem" → "usually has a positioning, price, or product problem", with Request a Review "once per order".
34. Practitioners: "Spencer" → Spencer Gordon. The ellipsis had cut his rule; it now includes the 10%-a-day lowering when organic rank is in the top five.
35. Practitioners: Wishon's "negatives after 15–20 clicks with no sale" and "a review in the first 30–60 days" → a poor-CVR look-for criterion, and regular review of negatives "especially in the first 30–60 days post-launch". Her bid-strategy lines are quoted and the article title corrected.
36. Practitioners: the ecomcrew title → *The No B.S. Amazon Product Launch Guide for 2025* (updated 2025-11-14). Scale Insights' rule is triggered by zero impressions over 7 days, with tier moves made by duplicating the campaign.
37. Research: the CIKM sponsored-results quote is confirmed in the full text, and its qualifying next sentence is added. The Gupta 2020 authors and venue (The Web Conference 2020) are added.
38. Research, P-launch-30: BFS "in Amazon search" → the paper says "a large E-commerce platform", with Amazon authors.
39. Research, P-launch-31: the cold-start exit "on the item's interaction data" → it is per item-query pair. US11269898B1's "option to manually boost" → manual boosting is described as the curation practice the method replaces.
40. What cx must read: "Reporting v3 search term report" → v3 reporting is deprecated, with shutoff on 2027-06-30 and the Reporting API v1 as replacement (open question 16 added). `getFeaturedOfferExpectedPrice` → `getFeaturedOfferExpectedPriceBatch`. Customer Feedback is v2024-06-01.
41. B: quick-guide version "dated 05/01/26" → the footer reads "3.0 | 050126" (created 2026-05-01).
42. N and What cx must read: "the `NEW_ASIN` grouping, with `RecommendationType` NEW_CAMPAIGN, NEW_PRODUCT_AD and NEW_KEYWORD" → the spec lists the grouping and the type enum separately and does not tie them together.

**Removals.** (1) The claim that the sign-up promotion terms page shows a separate offer (the page no longer resolves). (2) The claim that the ad specs page lists a "Coupon" variation (the cited URL is 404, and the current page has no such variation list).

**Positions.** None was worded as behaviour or left unsourced. P-launch-18, 21, 26, 30, 31, 32, 34, 37 and 40 were corrected as above.

**Pages that stayed unreachable.** The Seller Central help pages (content only through the forbidden GetHelpTopic call; cited as 2026-10-14 captures, not re-read). The sign-up and new-seller-incentives promotion terms (redirect to *About us*). The quarter-suffixed quick-guide PDFs. The API guide paths listed above. The Scale Insights workflow page and event recap. The Seller Sessions article itself (the episode page was read). The full Jungle Scout playbook (form-gated). Signed-in Seller Central and console dashboards (not attempted).

**Hosts.** No Ads API host (advertising-api*.amazon.com), no Login with Amazon endpoint, no Amazon Ads MCP endpoint, no SP-API host and no Seller Central GetHelpTopic content call was made. SP-API operation names were checked in the public `amzn/selling-partner-api-models` GitHub repository only. Fetched copies were kept in a scratch directory under `/tmp`; nothing else was written but this file.

### Gap fill 2026-11-09

Done by the research seat that owns this file, against three critics' items. Every page cited for the additions was opened on 2026-11-09 (the guides as CloudFront Markdown, the models as OpenAPI JSON, the help pages from the JSON embedded in the public page, and the papers as full text). No Ads API host, Login with Amazon endpoint, MCP endpoint, SP-API host or Seller Central content call was made.

**Added.**
1. Gap 1 (create sequence). New section P, *Building the first campaign through the door*: the order of creates and the id each step needs (P1), the v1 required fields, states, batch limits and 207 reply (P2), the SP 3.0 paths, media types and required fields, including `campaignId` on product ads and keywords (P3), the API and console draft states (P3), the `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE` statuses and the partial results a chain can leave, including the one that spends, a complete auto campaign whose negatives were not written (P4), and the MCP `create_singleshot_sp_campaign` tool, its input limits, its silence on failure, and the hosts the door does not reach (P5). Also: the SP v1 `SPBidStrategy` enum (G), a *Building the campaign* block in *What cx must read at run time*, Stable items 16–18, positions P-launch-41 to P-launch-46, open questions 17–20, and the pages-read rows.
2. Gap 2 (launch effects and measurement). Sahni and Nair (2020) and He, Hollenbeck and Proserpio (2022) read and added to *Published research*, with their designs, results and transfer to Amazon. A new subsection, *Why "the launch spend built the rank" cannot be read from a before-and-after*, states the missing pre-period and the comparisons available (sibling ASINs, staggered marketplaces, dose variation, synthetic controls), each with its research source (Athey and Imbens; Callaway, Goodman-Bacon and Sant'Anna; Brodersen et al.) and Ju, Zhao and Aral as a measured rank mechanism outside Amazon. Also: a *Series for judging what the launch spend did* block in the run-time reads, Stable items 19–20, positions P-launch-47 to P-launch-51, open question 22, and the two papers removed from the unread-leads list.

**Declined in part (wrong on the facts as worded).**
1. Gap 2 describes Sahni and Nair as showing "newer firms gaining more leads from ads". The published paper does not show this as a treatment effect. Its measured effect is that of the ad label, not ads against no ads. The label's interaction with restaurant age "is not statistically significant"; the significant interaction is with fewer past ratings. Newer restaurants are found to advertise more, a supply-side correlation the authors call "only suggestive". The file records what the paper says, and notes at the Dai, Kim and Luca entry that their citation words it more broadly.
2. Gap 2 describes He et al. as showing that bought reviews "raise ratings and rank briefly and then fade". Ratings do fade within two to four weeks, and sales fall after the buying stops. Keyword search position does not fade: it "does not substantially reverse even after two months", and the authors read the sales decline as coming from lower ratings, "not from a reduced product visibility". The file records both.
3. Gap 1's "SKU for sellers, ASIN for vendors" holds for the REST product ad. The MCP single-shot tool's `advertisedProduct` takes only `ASIN`, so the contrast with the tool is recorded as stated in its specification, with the conflict as open question 19.

**Contradictions settled.**
1. Contradiction 1 (single-value 100% positions). Re-opened on 2026-11-09: the library guide (*Guide to dynamic bidding - up and down*, published 2025-05-07, modified 2026-10-09) and the help page GCU2BUWJH2W3A8Z7 say "up to 100% for all placements"; the SP 3.0 `AUTO_FOR_SALES` and SP v1 `SALES_UP_AND_DOWN` descriptions say "by a maximum of 100%" and name no placement; the author's guide (published 2023-09-07, modified 2026-10-09) says "up to 100% for placements at the top of the first page of shopping results and by up to 50% for all other placements". In this file, the G bullet that called the 100% "confirmed for all placements" and P-launch-24 now state both Amazon readings and defer to P-bids-and-placements-8, the owner's position, which states both. `areas/diagnosis.md` P-diagnosis-37 and `beyond/automation-and-amazon-tools.md` (its item at line 63 and Stable 2) quote the library guide correctly but omit the author's guide; this seat writes only its own file and reports them to the owner.
2. Contradiction 2 (resolved or unresolved). The sources settle the wording, not the live value. Four current Amazon sources say 100% (two of them "for all placements"); one current Amazon page, the older by publication date, says 50% outside top of search. No Amazon page says the 50% was withdrawn, and no API field reports the ceiling in force. "The 50% is the older rule" is a seat inference in `areas/bids-and-placements.md` (its seat note under C), not a statement of Amazon's, and that file's P8 and open question 1 keep the conflict open. `method/change-measurement.md` P-12 and its open question 8, which present the conflict as unresolved, agree with what the sources say. This file now says the same (G, P-launch-24, open question 21).

**Corrections to the existing text.** G: "The 100% is confirmed for all placements in the console guide" → the two Amazon readings with publication dates, deferring to P-bids-and-placements-8. P-launch-24: rewritten as above. *Published research*: the Dai, Kim and Luca entry notes that Sahni and Nair word the newer-firm point more narrowly.
