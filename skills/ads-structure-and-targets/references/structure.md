# Campaign structure

## The Sponsored Products hierarchy

- In Sponsored Products the hierarchy is campaign, ad group, then product ads and targets, with negatives at campaign or ad-group level. (T1)
- Products in one ad group share its bids and targeting, ad group names are unique within a campaign, and one ad group cannot hold both keyword and product targets. (T1)
- The budget, the bidding strategy with its placement adjustments, the dates, the portfolio, the site restriction, the off-Amazon setting and the tags live on the SP campaign, and an ad group has no budget. (T3)
- Amazon reports that ad groups of similar products sold 6% more units on average. (T14)
- Amazon marks a campaign it manages with `autoManageCampaign`. (T16)
- Ads API v1 models campaigns, ad groups, ads, targets and ad associations across SP, SB, SD, Sponsored TV and DSP in one schema. (T10)

## Fixed at creation

- Fixed at creation: whether an SP campaign is auto or manual (`targetingType`), a keyword's match type, a Sponsored Brands campaign's goal, and several other fields Amazon lists per ad product. (T4)
- Changing one of them means archiving and recreating; a keyword in another match type can be added beside the old one. (T4)
- While both run, the higher-bid match type of the two is used on a query both match; Amazon's pages do not say whether this reaches across ad groups or campaigns. (T4, T22)

## Archiving

- `ARCHIVED` is terminal: Amazon's model calls it "permanently stopped and cannot be reactivated". (T6)
- Every API reaches `ARCHIVED` through a delete. (T6)
- An archived parent refuses updates and creations of its children, and a bulksheet archive cascades. (T6)

## Portfolios

- A campaign belongs to at most one portfolio, and portfolios do not compete with each other. (T7)
- Portfolios are managed per profile, in that marketplace's currency. (T7)
- Amazon suggests organising portfolios by brand, category or season. (T7)

## Limits

- Entity limits are published on Amazon's *Sponsored ads campaign limits* page, which says Amazon raises limits as an account nears them. (T8)
- A write past a quota is refused with `QUOTA_EXCEEDED` or `NON_ARCHIVED_QUOTA_EXCEEDED`. (T8)
- Third-party limit tables disagree with each other and with Amazon. (T8)
- Campaign names are limited to 128 characters for sellers and 116 for vendors, ad group names to 255, and an entity takes up to 50 tags. (T9)

## Global campaigns and other marketplaces

- A global SP campaign (`marketplaceScope` `GLOBAL`) holds one budget per marketplace in local currency. (T11)
- It carries a top-level delivery status with a per-marketplace one, and its targets carry a `marketplaces` list, where a child's marketplaces are a subset of its parent's. (T11)
- Only the `spCampaigns` report surfaces global campaigns. (T11)
- The Localization API maps keywords, products, targeting expressions and currencies between marketplaces. (T12)
- Amazon's keyword translation combines machine translation, linguists and closest local terms. (T12)
- Valid scripts and symbols differ by marketplace, and the API accepts hiragana, katakana, kanji and both widths in keywords. (T12)
- Amazon publishes a checklist for new international ad campaigns. (T12)

## Bulksheets and exports

- A bulksheet row carries a product, an entity and an operation, over the same entities as the API. (T15)
- An export from the Exports API is a snapshot of current metadata with no history, with five jobs per endpoint and a download link valid for one hour. (T15)

## Vendors and sellers

- Vendors identify a Sponsored Products product ad by ASIN and sellers by SKU; in Sponsored Display vendors use the `asin` field where sellers use `sku`. (T49)
- The v3 advertised-SKU column is not available for vendors, and Review Requests take an ASIN from both. (T49)
- Only vendors may give a Sponsored Brands campaign a custom landing page URL, which must include the ASINs of at least three products advertised in the campaign and cannot be combined with an `asins` list; the merged model's `CUSTOM_URL` landing-page type is "Available for vendors only". (T49)
- Amazon's *Sponsored Products 3.0* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json, defines custom text ads only for KDP authors and book vendors, in the marketplaces it names, and its brand negative-target recommendations are "Only available for Sellers and Vendors". (T49)

## Which products are advertised

- Amazon labels products "suggested" on the create page and sorts ASINs by life cycle and sales in its ASIN matrix guide. (T21)
- Amazon advises distinct complementary products, not variations, in a collection. (T21)
- m19 advises advertising "only the top-performing children" of a family, and Canopy's Chuck Kessler gives "the 20% of products driving 80% of revenue" a defensive budget. (T21)

## Practitioner structures

- Perpetua isolates search terms per ASIN across auto, manual and exact campaigns. (T17)
- Helium 10 names four SP campaigns. (T17)
- Seller Labs lists signs of over- and under-structure. (T17)
- Single-keyword campaigns have advocates (Scale Insights, Quartile, JumpFly) and critics. (T17)
- Mina Elias keeps one ad group per campaign against "keyword bullying". (T17)
- Ad Badger segments by targeting type. (T17)
- Ad Badger calls a branded/non-branded campaign split "more of a reporting strategy than a performance strategy". (T18)
- Practitioners' naming conventions put ad product, product, targeting and goal in the name. (T17)
- AMZ Pathfinder names scattered ASINs the most visible audit problem. (T17)
