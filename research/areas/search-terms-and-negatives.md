# Harvesting search terms and negatives

Read 2026-11-09 by the research seat. Tags: [official] Amazon's own words (Amazon Ads help, library, API guides, OpenAPI models, release notes, deprecation notices; the SP-API models repository); [opinion] a named practitioner, agency or paid tool, said to be theirs; [research] published research; [seat] the seat's own reasoning, never a position. Every page below was opened on 2026-11-09; Ads API guides were read as their markdown sources on `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`, OpenAPI models from the URLs in the docs site's contract index (`https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json`), and Amazon Ads help pages (`https://advertising.amazon.com/help/<id>`) from the article text the page carries inside its own HTML, by a plain GET. Figures marked *(figure)* may change and are read at run time; the ones a skill must never carry are listed under "What cx must read at run time".

## What this covers

**The seller's work.** Every keyword, auto target, category target and broad or phrase keyword buys traffic on queries the seller did not write. The search term report is the only place Amazon shows, query by query, what that traffic was and what it bought. This file covers four jobs on that report:

1. **Reading it.** What a row is, what it leaves out, and how the console, the API, bulksheets, unified reporting and AMC each cut it differently.
2. **Harvesting.** Moving a query that converts into a target the seller controls: an exact or phrase keyword, or an ASIN target.
3. **Negating.** Negative keywords (exact and phrase, and the API's broad), negative ASINs and negative brands, at campaign or ad-group level. How negatives act inside auto ad groups, broad keywords and product-targeting ad groups.
4. **Judging a term.** Waiting out attribution and restatement, the statistics of a term with clicks and no orders, and the thresholds practitioners use, each as theirs. Search-term impression share and rank come in here too, as the reach side of a term.

**Why a senior Amazon advertising lead cares.** Search terms are where wasted spend and missed demand are both visible, row by row. They are also where the most common mechanical errors happen:

- negating a term in the wrong campaign or at the wrong level;
- a negative phrase that blocks a profitable long tail;
- an "exact" negative that also blocks plurals and misspellings, because Amazon matches close variants;
- judging yesterday's term before its orders have arrived;
- reading an ASIN-shaped row as a query;
- forgetting that the API omits zero-click terms the console may once have shown.

On 2026-11-09 several of these surfaces are mid-migration:

- v3 reporting stops on 2027-06-30;
- the console's legacy report pages close on 2026-12-31;
- Sponsored Brands v2 search-term impression share stops returning values on 2026-11-10.

So a skill that names one path as "the" search term report will be wrong within months.

**Lanes.** Choosing what to target in the first place is areas/keyword-and-product-targeting.md's. How harvested terms are laid out into campaigns (isolation, single-keyword groups, cannibalisation between campaigns) is areas/campaign-structure.md's. Bids on harvested targets and placement multipliers are areas/bids-and-placements.md's. Attribution windows and metric definitions in depth are beyond/metrics-and-attribution.md's. Report lifecycle (create, poll, download) is method/reporting.md's. Whether a paid term cannibalises organic sales is areas/ads-organic-and-total.md's. Negating competitor and own-brand terms as a defence question is beyond/brand-defense-and-competition.md's. Target promotion and Amazon's own automation are also beyond/automation-and-amazon-tools.md's, which this file only touches where they move terms. Judging whether a negative "worked" is method/change-measurement.md's.

## Amazon's own rules and guidance

RULE marks something Amazon enforces: an API shape, an enum, a limit, a deprecation, a stated system behaviour. GUIDANCE marks a recommendation. Figures are recorded with the page; they are for human readers unless a section says otherwise.

### A. What a search term row is

**A1. RULE: A row is a customer search term under one keyword or targeting expression.** "Search term reports contain search term performance metrics broken down by targeting expressions and keywords." [official] (Search term reports [v3], https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term, read 2026-11-09)

The same query can therefore appear on several rows: one per campaign, ad group and keyword or target it matched. In v3 the row carries:

- `searchTerm`: "The search term used by the customer. Same as query."
- `keyword`: "Text of the keyword or a representation of the targeting expression (for Sponsored Products)". In Sponsored Brands it is `keywordText`.
- `targeting`: "A string representation of the expression object used in the targeting clause".
- `matchType` and `keywordType`: "For keywords, one of: BROAD, PHRASE, or EXACT. For Sponsored Products reports, keywordType can also contain the type of targeting expressions, one of: TARGETING_EXPRESSION or TARGETING_EXPRESSION_PREDEFINED". The note under `matchType` adds: "The Amazon Ads Console uses "-" in place of `TARGETING_EXPRESSION` or `TARGETING_EXPRESSION_PREDEFINED` in generated reports."
- `adKeywordStatus`: "Current status of a keyword".
- the campaign and ad group ids, names and budget fields.

[official] (Reporting columns (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/columns, read 2026-11-09)

**A2. RULE: The v3 SP search term report has no advertised-product column.** The Sponsored Products base-metric list of `spSearchTerm` holds no `advertisedAsin` or `advertisedSku`. [official] (Search term reports [v3], full column list read 2026-11-09)

A term is tied to a product only through its ad group's product ads. Where an ad group advertises several ASINs, the v3 row cannot say which ASIN's ad was shown. [seat: reading of the column list]

In v1 the advertised product is a dimension (`advertisedProduct.id`; v3 name `advertisedAsin`). Its dimension page, read 2026-11-09, no longer prints a compatible-dimensions list, so whether `searchTerm.value` and `advertisedProduct.id` combine in one v1 report is not stated on a page read here (Open questions). [official] (Advertised product (Product), https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/product/advertised-product, read 2026-11-09)

**A3. RULE: Only terms with a click appear in the API report.** "Note that search term reports only include impressions that resulted in at least one ad click." [official] (Search term reports [v3])

The v3 FAQ sets this against the console: "The search term report in the advertising console contains all search terms that had an impression, regardless of if that term resulted in a click. The API search term report only contains impressions that also had at least one click. Therefore you will see a difference in the number of entries between the console and API reports." [official] (Sponsored ads reporting FAQ (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/faq, read 2026-11-09)

**A4. RULE, and Amazon's pages now disagree on the console.** The console's own help page says the console report is clicked-only too:

- "The search term report includes only the search terms that resulted in at least 1 ad click, so the impressions in the report may not match the impressions in the campaign manager." [official] (Search term report for Sponsored Products, https://advertising.amazon.com/help/G3HEFZYWZF84NPS9, read 2026-11-09)
- Amazon's best-practice guide says the same: "Find the shopping terms used by customers shopping on Amazon that resulted in at least one click on your ad." [official] (Best practices for your Sponsored Products ads, https://advertising.amazon.com/library/guides/sponsored-products-best-practices, page `dateModified` 2026-09-28, read 2026-11-09)
- The bulksheet page explains its impression gap the same way: "If you compare impressions in the search term report with what you see in the advertising console, the numbers might be different. This is because the search term report includes only the terms that resulted in at least one ad click." [official] (Search term reports in bulksheets, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-search-term-report, read 2026-11-09)

So three Amazon pages say clicked-only everywhere, and the v3 FAQ alone says the console holds impression-only terms. A vendor reports a change: "In mid-July 2026, Amazon changed how customer search terms populate in its advertising reports", "Search-term text is now returned only for queries that actually earned a click", "the change applied retroactively across accounts". [opinion] (WisePPC, "WisePPC new analytics suite 2026", unsigned, published 2026-07-30, https://wiseppc.com/blog/wiseppc-new-analytics-suite-2026/, read 2026-11-09)

The vendor's sentence goes on: "the long tail of impression-only queries is no longer exposed anywhere in that API"; it speaks of "its advertising reports" and an API field its own Unified Report read, and does not name the console. [opinion] (WisePPC, same page)

No Amazon page read here dates such a change. The bulksheet page's own column definition for "Customer Search Term" reads "The term or phrase the customer typed into the search bar when they encountered your ad", which differs from the console help's "or inferred by Amazon in non-search contexts" (A7). [official] (Search term reports in bulksheets) [seat] Either way, a term whose rows all have zero clicks is not visible in the search term report today. The sums of a search term report's impressions are lower than the campaign's or target's impressions by the impressions of unclicked queries.

**A5. RULE: The `*` row.** "If a placement does not have a search keyword associated with it on a product detail page, the search term in the report will be an asterisk `*`." [official] (Search term reports [v3])

**A6. RULE: ASIN-shaped rows are pages, not queries.** "You may notice alphanumeric entries such as "b00ipgvvz4" in addition to more traditional search terms such as "phone case." These alphanumeric entries correspond to `ASIN`s and the related product detail page on which your ad displayed. You will only see `ASIN`-related entries listed as customer search terms for your Sponsored Products automatic-targeted campaigns and product-attribute-targeted ad groups. You can block `ASIN`s through negative targeting, or bid for `ASIN`s in manually targeted campaigns." [official] (Search term reports in bulksheets; the same text on Search term report for Sponsored Products, G3HEFZYWZF84NPS9)

Amazon's targeting guide gives the shape: "An ASIN is always 10 characters long, and either entirely numeric (e.g. 0015366456) or starts with a "B" (e.g. "B00JPFUVUU")." [official] (A guide to targeting with Sponsored Products, https://advertising.amazon.com/library/guides/targeting-with-sponsored-products, `dateModified` 2026-10-09, read 2026-11-09)

The report prints these ASINs in lower case (Amazon's own example is "b00ipgvvz4"). A negative or positive ASIN target takes the ASIN as the catalogue writes it. [seat: the case observation is from Amazon's example; whether the API normalises case is not stated]

Category targeting surfaces the individual ASINs under a category: "The search terms report will then show the individual ASINs under this category that generated specific clicks and conversions. This information can be used to refine targeting to individual ASINs". [official] (A guide to targeting with Sponsored Products)

**A7. RULE: Some "search terms" were never typed.**

- The help page's column definition reads: "Customer Search Term: The search term used by the customer or inferred by Amazon in non-search contexts."
- Its opening says the report shows terms customers use "or when they are inferred as best match to your product in non search context (such as off Amazon placements on social sites)." [official] (Search term report for Sponsored Products, G3HEFZYWZF84NPS9)
- The match-type help adds: "When a customer search term is not available, Amazon will infer a search term from the context that best matches your keywords and show your ads in relevant placements." [official] (Understand keyword match types, https://advertising.amazon.com/help/GHTRFDZRJPW6764R, read 2026-11-09)

Sponsored Products off-Amazon serving has its own bulksheet column since 2026-06-08 ("`Off-Amazon ad serving` … allows advertisers to update settings for ads served off amazon", US). [official] (All releases, https://advertising.amazon.com/API/docs/en-us/release-notes/index, entry of June 8, 2026, read 2026-11-09)

A practitioner draws the consequence: "An inferred term can pass your rule without a shopper ever typing it. Before graduating an odd-looking term, check that it reads like a real search for your product." [opinion] (Ayush Chaudhary, Adbrew, "Amazon Keyword Harvesting: How to Automate the Funnel", byline 2026-10-27, https://adbrew.io/blog/amazon-ppc-how-to-automate-a-keyword-harvesting-funnel, read 2026-11-09)

No Amazon field read here flags which rows are inferred. [seat]

**A8. RULE: The keyword in a broad, phrase or exact row need not appear in the query.** Amazon's match-type help:

- "In manual targeting campaigns, you have 3 options. They all account for plurals, misspellings, and translations."
- Broad: "may include singulars, plurals, variations, synonyms, and related terms as determined by the meaning of the keyword and the context of the advertised products. The keyword itself may not be contained in the customer shopping query."
- Phrase: "your keyword phrase or sequence of words, as well as their close variations like misspellings, plural forms, acronyms, translations appear in shopper queries".
- Exact: "your keyword or sequence of words exactly match shopper queries as well as their close variations like misspellings, plural forms, acronyms, translations. … if your exact match keyword is "outside lights," your ad can still appear when a customer searches for "outdoor lights"."

[official] (Understand keyword match types, GHTRFDZRJPW6764R)

Amazon's keyword guide gives a word-order example for exact: "the exact match keyword "white running shoes" would only show for that exact phrase or extremely close variants like "running shoes white."" [official] (What is Keyword Targeting? How It Works, Benefits, Examples, https://advertising.amazon.com/library/guides/keyword-targeting, `dateModified` 2026-10-09, read 2026-11-09)

The model's enum text for v1: `BROAD` "expands matching on user intent beyond PHRASE", `PHRASE` "expands matching on user intent beyond EXACT". [official] (Amazon Ads API v1 merged OpenAPI, `KeywordMatchType`, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json, read 2026-11-09)

The export enum describes Sponsored Brands phrase differently: "In Sponsored Brands campaigns, this match type includes search terms matching the meaning of the keyword." [official] (Exports enums, https://advertising.amazon.com/API/docs/en-us/guides/exports/entities/enums, read 2026-11-09)

On Sponsored Brands: "Keyword targeting in Sponsored Brands has semantic matching. Instead of having word-to-word matching only, it uses a meaning-based approach." [official] (What is Keyword Targeting?)

**A9. RULE: One query, several of the seller's keywords.** "If you set multiple match types with different bids for the same keyword, then the match type with the highest bid will be used for any matching shopping query." [official] (Understand keyword match types, GHTRFDZRJPW6764R)

How Amazon chooses among the seller's own eligible ads across different campaigns is not stated on a page read here; it is areas/campaign-structure.md's question.

**A9b. RULE and GUIDANCE: what Amazon says that bears on the unit of a negative or a harvest (gap fill 2026-11-09).**

- The highest-bid sentence above is scoped to "multiple match types with different bids for the same keyword"; the help page does not say whether it reaches across campaigns or ad groups. [official] (Understand keyword match types, GHTRFDZRJPW6764R, `lastModified` 2026-07-29, read 2026-11-09)
- Amazon's targeting guide: "And don’t worry, you won’t be bidding against yourself by adding different match types on the same keyword." On several campaigns: "if you have multiple campaigns where you’re bidding on category keywords that are relevant to multiple advertised products, set bids based on your priority for each product; this will give your top priority product the best opportunity to get top ad placements, while still giving your lower priority product(s) a chance to also appear on the search results page." [official] (A guide to targeting with Sponsored Products, `dateModified` 2026-10-09, read 2026-11-09)
- One sale, one credit: "Amazon will attribute a conversion to no more than 1 ad interaction across all campaigns and all advertisers. A sale won't, for example, be attributed to 2 campaigns in both a promoted and brand halo context, or as both a view-through and click-through conversion. It's attributed once to the most relevant ad interaction." [official] (Ad campaign attribution, https://advertising.amazon.com/help/GX7KDKHMWQYMJ385, `lastModified` 2026-10-20, read 2026-11-09)
- v1 aggregates by the dimensions requested: "When you request a report with a specific dimension, each row will represent a unique value for that dimension, with all metrics aggregated accordingly." [official] (Helpful concepts [Reporting v1], https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/helpful-concepts, read 2026-11-09)
- Search Query Performance counts the ASIN's own funnel on the query, paid and unpaid together, from the search results page: `asinImpressionCount` is "The total number of impressions that originate from the search results page for the current ASIN with the current query", and `asinClickCount`, `asinCartAddCount` and `asinPurchaseCount` are the ASIN's counts on the query; `reportPeriod` is `WEEK`, `MONTH` or `QUARTER`. [official] (sellingPartnerSearchQueryPerformanceReport.json, read 2026-11-09) The SP-API report type is `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT`, for "Sellers who have the Brand Analytics Selling Partner API role and are registered in Amazon Brand Registry". [official] (Analytics Reports, https://developer-docs.amazon/sp-api/docs/report-type-values-analytics, read 2026-11-09) The help page that states the organic-and-sponsored inclusion in words is behind the Seller Central content call and was not read (see areas/ads-organic-and-total.md §E2).
- Global Sponsored Products campaigns: "Only the `spCampaigns` report surfaces global campaigns." [official] (Global campaigns for Sponsored Products, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/global-campaigns, read 2026-11-09)

[seat] Read together: a search term is a query, and its rows sit under every campaign, ad group and target that served it (A1). A negative in one campaign removes that campaign's rows; the same query can still be served by any other eligible target of the seller's, and Amazon credits each sale once, to one ad interaction. So the spend and sales a negative "saves", and the sales a harvested exact keyword "gains", are first of all moves between the seller's own rows. The net effect on ads is the query's rows summed across all campaigns before and after (a v1 report with `searchTerm.value` and no campaign or target field aggregates them, per the helpful-concepts sentence, if the service accepts that field set), and the net effect on the product is the ASIN's SQP counts on that query, weekly at the finest. A global SP campaign's rows are not in a search-term report, per the global-campaigns guide. method/change-measurement.md S6 names "spend on the negated term" as a negative's first-order metric; that reads the negated target's rows only.

**A10. RULE: Auto groups and theme targets report as targeting expressions.** Auto ad groups get "four auto targeting expressions" automatically. They are created as `ThemeTargets` in v1. [official] (Sponsored Products auto targeting, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/auto-targeting, read 2026-11-09)

Amazon's match-type help defines the four groups by where they serve: close match and loose match on "search terms closely [or loosely] related to your products"; substitutes and complements on "product detail pages" of similar or complementary products. [official] (Understand keyword match types, GHTRFDZRJPW6764R, section "Automatic targeting groups") The v1 `MatchType` enum names them `KEYWORDS_CLOSE_MATCH`, `KEYWORDS_LOOSE_MATCH`, `PRODUCT_SUBSTITUTES` and `PRODUCT_COMPLEMENTS`. [official] (Amazon Ads API v1 merged OpenAPI, `MatchType`)

The export enum maps them:

- `SEARCH_CLOSE_MATCH` ↔ SP `QUERY_HIGH_REL_MATCHES`;
- `SEARCH_LOOSE_MATCH` ↔ `QUERY_BROAD_REL_MATCHES`;
- `PRODUCT_SUBSTITUTES` ↔ `ASIN_SUBSTITUTE_RELATED`;
- `PRODUCT_COMPLEMENTS` ↔ `ASIN_ACCESSORY_RELATED`.

[official] (Exports enums)

The bulksheet's "Product Targeting Expression" column reads `close-match`, `loose-match`, `substitutes` or `complements` "For bids set at the targeting group level". [official] (Search term reports in bulksheets)

The v1 `MatchType` enum also lists theme types that produce search terms without a keyword the seller wrote: `KEYWORDS_RELATED_TO_YOUR_BRAND`, `KEYWORDS_RELATED_TO_GIFTS`, `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`, `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` ("products from other brands in the category of your advertised products. The peer brands are selected automatically") and `KEYWORDS_RELATED_TO_PRIME_DAY` ("These keywords will only match queries through the end of Prime Day"). [official] (Amazon Ads API v1 merged OpenAPI, `MatchType`)

Keyword Groups (beta, US, 2024-04-23) also report through the search terms report: "Once a Keyword Group specification is created, the performance of Keyword Groups will be available in the search terms report." [official] (All releases, entry of April 23, 2024)

The v3 SB targeting report accepts a `keywordType` value `THEME` that the search term report's filter list does not include. [official] (Targeting reports [v3], https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/targeting; Search term reports [v3]; both read 2026-11-09)

**A11. RULE: Prompts are a separate report.** "Prompts with clicks will show in your existing Sponsored Products or Sponsored Brands reporting". Prompt-level data sits in `spPromptAdExtension` and `sbPromptAdExtension` (v3; maximum range 90 days, retention 95 days *(figure)*). [official] (Prompt Ad Extension reports, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/prompt-ad-extension, read 2026-11-09)

A 2024 note said "Your campaign reports will not include Rufus metrics" for Rufus-related placements. [official] (All releases, entry of September 5, 2024) Since May 2026 Rufus is part of Alexa for Shopping (US), where existing sponsored ads campaigns are "automatically eligible to serve"; Alexa+ on Alexa-enabled devices carries "Alexa+ Conversational Ads" with automatic enrolment (see "Report contents, as practitioners see them" for the two pages). [official] (Meet Alexa for Shopping…; What agentic shopping means for advertising; both read 2026-11-09) Whether the 2024 line still holds for Alexa for Shopping is not stated on either page.

The prompts launch page says campaigns "will be automatically enrolled in prompts and leverage existing campaign parameters (e.g., campaign targeting)", that prompts "can appear in shopping results and product detail pages", that "When clicked, prompts may open a dialog in Rufus", and that at US general availability "we will begin to charge for these ads as part of your CPC bidding and billing parameters". [official] (Sponsored Products prompts and Sponsored Brands prompts, https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts, `datePublished` 2026-03-10, read 2026-11-09) Whether a campaign's negative keywords also suppress its prompts is not stated there.

No page read here says whether prompt or conversational-surface clicks carry a row in the search term report, and under what text. That is an open question.

### B. The surfaces: console, unified reporting, API v3, API v1, Stream, bulksheets, AMC

**B1. RULE: v3 report shape.**

| | Sponsored Products | Sponsored Brands |
|---|---|---|
| `reportTypeId` | `spSearchTerm` | `sbSearchTerm` |
| Maximum date range | 31 days *(figure)* | 31 days *(figure)* |
| Data retention | 65 days *(figure)* | 60 days *(figure)* |
| `timeUnit` | `SUMMARY` or `DAILY` | `SUMMARY` or `DAILY` |
| `groupBy` | `searchTerm` | `searchTerm` |
| Filter | `keywordType`: `BROAD`, `PHRASE`, `EXACT`, `TARGETING_EXPRESSION`, `TARGETING_EXPRESSION_PREDEFINED` | same |

The SB report "is currently available in preview. During the preview period, data related to Sponsored Brands campaigns with flag `isMultiAdGroupsEnabled` set to `FALSE` will not be available." [official] (Search term reports [v3])

The SP base metrics include 1d, 7d, 14d and 30d variants of `purchases`, `purchasesSameSku`, `unitsSoldClicks`, `sales`, `attributedSalesSameSku` and `unitsSoldSameSku`, plus `salesOtherSku7d`, `unitsSoldOtherSku7d`, `acosClicks7d`/`14d` and `roasClicks7d`/`14d`. The SB list carries `purchases`, `purchasesClicks`, `sales`, `salesClicks`, `unitsSold`, `costType` and video and viewability metrics. [official] (Search term reports [v3])

**B2. RULE: v3 is deprecated; the date is fixed.** "Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting will stop delivering data on June 30, 2027." The Exports API "is not affected". [official] (Deprecations, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations, entry "September 2026 - Deprecation of Amazon Marketing Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting", read 2026-11-09)

The same page has an SB-specific shutoff: "`searchTermImpressionRank` and `searchTermImpressionShare` will stop returning values in the v2 Sponsored Ads reporting API for Sponsored Brands reports on November 10, 2026." The replacement is named "Unified Reporting (v4 reporting API)" with "`metric.impressionShare` and `metric.impressionShareRank`". [official] (Deprecations, entry "October 2026")

Amazon's pages name the new API both "Reporting API v1" and, on this one entry, "v4 reporting API". The field names are the same. [seat]

**B3. RULE: v1 is field-based.** v1 has no report types. The migration page for `spSearchTerm` maps the v3 request to `POST /adsApi/v1/create/reports` with fields:

- `searchTerm.value`;
- `target.value` and `target.matchType`;
- `adGroup.id`, `adGroup.name`;
- `campaign.id`, `campaign.name`, `campaign.deliveryStatus`, `campaign.budgetAmount`, `campaign.budgetType`, `campaign.currencyCode`;
- `portfolio.portfolioId`, `metric.impressions`, `metric.addToList` and `dateRange.value`.

The request carries `accessRequestedAccounts[].advertiserAccountId` and `periods[].datePeriod`. [official] (Migrating from: spSearchTerm, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/report-types/sp-search-term, read 2026-11-09)

The dimension pages name the targeting fields differently:

- `adGroupTarget.id`, `adGroupTarget.bid`, `adGroupTarget.targetType`, `adGroupTarget.status` (Target);
- `targeting.value`: "The keyword, product or category you choose to reach shoppers" (Targeting);
- `targetingMatchType.value`: "The type of matching for keywords used in a bid" (Targeting match type).

The search-term dimension is `searchTerm.value`, "The search term used by the customer", for SP and SB. [official] (Target (Targeting); Targeting (Targeting); Targeting match type (Targeting); Search term (Targeting); all under https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/targeting/, read 2026-11-09)

The migration page lists `target.value` twice, standing for both v3 `keyword` and v3 `targeting`. The dimension pages for `targeting.value` and `targetingMatchType.value` print "Ad Product availability: N/A". The v1 New features page's own sample response marks `target.value` with the warning code `PENDING_DEPRECATION` ("This field is scheduled to be deprecated but is not deprecated yet. It continues to return data for now"); the page presents it as an example, not as a notice. [official] (Migrating from: spSearchTerm; Targeting (Targeting); Targeting match type (Targeting); New features [Reporting v1]; all read 2026-11-09)

The migration page's `target.value`/`target.matchType` and the dimension pages' `targeting.value`/`targetingMatchType.value` are two spellings on Amazon's own pages. Re-read on 2026-11-09 (gap fill): the Dimensions library's targeting folder holds six pages (frequency group, matched target, search term, target, targeting, targeting match type) and none defines a `target.value` or `target.matchType`; the Target page defines only `adGroupTarget.id` (primary key; "Sponsored Products, Sponsored Brands, Sponsored Display, Sponsored TV"), `.bid`, `.targetType` and `.status`. `target.value` appears only in the migration examples and in the New features page's warning example, where it carries `PENDING_DEPRECATION`. [official] (Target (Targeting); Targeting (Targeting); Targeting match type (Targeting); Migrating from: spSearchTerm; New features [Reporting v1]; read 2026-11-09) The library's names are the documented ones; method/reporting.md §H owns this and reads the same. Whether the service still accepts `target.value`, and with which warning, is in the service's reply and its `warnings` array. [seat]

**B4. RULE: `matchedTarget.value` is Sponsored Display only (as of today's page).** "Matched target … `matchedTarget.value` … Ad Product availability: Sponsored Display … The product page where the ad appeared … Version 3 Reporting Name (Sponsored Ads): `matchedTargetAsin`." [official] (Matched target (Targeting), read 2026-11-09)

The prior research read of 2026-10-14 (cx-listing-playbook, angles/paid-keywords.md §K) recorded this dimension as compatible with `searchTerm.value`; the page read today names only Sponsored Display. For SP, the page an ASIN-shaped row stands for is the row's own `searchTerm` (A6). [seat]

**B5. RULE: v1 conversion metrics carry no window suffix.**

- "Sponsored Products: Base metrics automatically align with campaign defaults—7-day look-back for sellers and 14-day look-back for vendors". "Other campaign types: The standard look-back is 14 days".
- "All conversion metrics are now reported on "traffic date," meaning conversions are reported on the date of the ad interaction".
- Each metric has Promoted and Halo forms, and "terms such as "Brand Halo" and "Other SKU" are now standardized as "Halo"".
- SP and SB CPC "will continue to report 0 for conversions from views".

[official] (Overview of the Reporting v1 API, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/overview, read 2026-11-09)

Metric definitions in depth are beyond/metrics-and-attribution.md's.

**B6. RULE: v1 retention and range.**

| Time dimension | Retention *(figure)* | Max range *(figure)* |
|---|---|---|
| `hour.value` | 14 days | 14 days |
| `date.value` | 24 months | 120 days |
| `week.value` | 24 months | 15 months |
| `month.value` | 6 years | 25 months |
| `dateRange.value` | 6 years | 6 years |

The page's "Dimensions with limited history" lists only the benchmark dimensions, not search term. Aggregation is "based on each campaign timezone". [official] (Dates and historical data retention, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dates, read 2026-11-09)

Read literally, v1 search-term history reaches 24 months where v3 reached 65 days and the console help says "The lookback window for the search term report is 65 days" (G3HEFZYWZF84NPS9). No page read here states search-term retention in v1 by name (Open questions). [seat]

**B7. RULE: v1 limits.**

- "Reporting API v1 applies its rate and concurrency limits per client ID … Limits are not applied per advertiser account."
- "The concurrency limit restricts the number of simultaneously running report generation requests to as low as 1, while the rate limit can be as low as 1 request per second".
- A report too large "may fail immediately, or may fail after a period of attempting to process", and "Repeating the same request may result in repetitive failures if the report is too large to process."

[official] (Limits and best practices [Reporting v1], https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/limits, read 2026-11-09)

The overview's note reads "one concurrent report per client ID, not per advertiser account"; the 2026-09-30 release note reads "one concurrent report per advertiser". [official] (Overview of the Reporting v1 API; All releases, entry of September 30, 2026). Amazon's two pages disagree; the limits page is the more specific. [seat]

A finished v1 report may carry `warnings` with `warningCodes` such as `NO_PERMISSION` (values redacted), `PENDING_DEPRECATION` and `DATE_LIMITED` ("Data for this field is not available for the entire date range you requested"); the page says to "handle `warningCodes` as an open-ended list". [official] (New features [Reporting v1], https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/new-features; All releases, entry of October 5, 2026; both read 2026-11-09)

**B8. RULE: Stream v2 carries search terms.** The Ads Performance Dataset (`ads-performance-v1`) "consolidates data previously available across multiple v3 report types (campaign, ad group, ad, advertised product, search term, targeting, placement, inventory, geography, and technology reports) into a single unified schema", updated "as often as every 15 minutes". It delivers "total metric values (not deltas)" and, on restatement, "you receive it again with its new total, and you keep the highest `streamBatch.version` per record." [official] (All releases, entry of September 30, 2026)

Stream v2 offers "automated backfill up to 70 days on subscription creation" *(figure)*. [official] (Amazon Ads reporting overview, https://advertising.amazon.com/API/docs/en-us/guides/reporting/overview, read 2026-11-09)

Stream needs an AWS destination (S3 bucket and SQS queue), which the cx door does not provide. [seat]

**B9. RULE: Console, legacy and unified.**

- "Unified reporting is now generally available in Ads Console … (Measurement and Reporting > Reporting)". It offers "up to 15 months of daily or weekly data and up to 6 years of monthly, yearly, or summary-grain data" *(figure)*.
- "standardized metrics, dimensions and attribution methodology (from conversion to traffic based attribution)".
- "we're sunsetting Sponsored Ads reports (Measurement and reporting > Sponsored Ads reports) and Amazon DSP reports … by December 31, 2026."

[official] (Streamline campaign analysis with unified reporting, https://advertising.amazon.com/resources/whats-new/streamline-campaign-analysis-with-unified-reporting, `datePublished` 2026-06-07, read 2026-11-09)

A trade publication describes the unified template as "Search Term, for search queries that resulted in at least one click across Sponsored Products and Sponsored Brands". [opinion] (Luís Rijo, PPC Land, "Amazon Ads unified reporting exits beta - and takes two old tools with it", 2026-06-10, https://ppc.land/amazon-ads-unified-reporting-exits-beta-and-takes-two-old-tools-with-it/, read 2026-11-09)

The console is now named Amazon Ads Agent: "Amazon Ads Agent is the unified buying experience that brings together what was formerly the DSP and Ads Console". [official] (unBoxed 2026 news: Explore the latest advertising announcements, https://advertising.amazon.com/library/news/unboxed-2026-news-announcements, `datePublished` 2026-09-29, read 2026-11-09) The site-wide navigation on advertising.amazon.com carries the line "We made it simpler to advertise with Amazon Ads by bringing together the ads console and Amazon DSP into a single buying surface we call Amazon Ads Agent." [official] (navigation text, same page and others)

The targeting guide's navigation now reads "clicking on your campaign name in Amazon Ads Agent and navigating to the 'Negative keywords' tab". The same guide states: "Once the campaign is live, you will not be able to change the campaign targeting". [official] (A guide to targeting with Sponsored Products)

Unified reporting's downloads are files the seller exports; cx reads one only when the seller places it in the tree. Each file is read by its own header row. [seat]

**B10. RULE: The console help's column set and naming.** The SP search term report help lists the seller columns under their new names, which a downloaded file may carry:

- "Sales (promoted) (formerly known as 7 day advertised SKU sales)";
- "Units sold (promoted)";
- "Purchase rate (formerly known as 7 day conversion rate)" defined as "The number of ad-attributed purchases over ad attributed clicks occurring within 7 days of your ad being clicked";
- "Sales (halo) (formerly known as 7 day other SKU sales)";
- "Purchases (formerly known as 7 day total orders)";
- "Sales", "Units sold", "Click-Thru Rate (CTR)" ("calculated as clicks divided by impressions"), "Cost Per Click (CPC)", "Customer Search Term", "Match Type", "Targeting", "Spend", "Total Return on Advertising Spend (ROAS)";
- vendor 14-day columns.

"The search term report has 2 time units available: summary or daily." [official] (Search term report for Sponsored Products, G3HEFZYWZF84NPS9)

By contrast the targeting report "provides insights into sales and performance metrics for targets in all campaigns that received at least 1 impression", with a 90-day lookback *(figure)*. [official] (Targeting report for Sponsored Products, https://advertising.amazon.com/help/GPDYPV4AAYCAJFKP, read 2026-11-09)

The targeting report therefore carries a target's full impressions; the search term report carries only its clicked queries. [seat]

**B11. RULE: Bulksheets.**

- "The lookback window in bulksheets search term reports is always 7 days for both vendors and sellers". The bulk file's date range "does not affect the search term report metrics".
- "some seller- and vendor-specific lookback metrics (for example, 7-day advertised SKU sales, and 14-day advertised `ASIN` sales) are not included".
- The tab carries `Campaign Id`, `Ad Group Id`, `Keyword Id (Read only)` and `Product Targeting Id (Read only)` ("Use this ID in the relevant entity row to update keywords or product targeting").
- Sponsored Brands search terms joined bulksheets on 2024-01-22, "in a new tab", with "the entity IDs available, so you can quickly make adjustments if needed". [official] (All releases, entry of January 22, 2024)
- The sheet "is read-only, so you should not make changes in this sheet".

[official] (Search term reports in bulksheets)

**Amazon's bulksheet page inverts two definitions:** "Click-through Rate … calculated as impressions divided by clicks" and "Conversion Rate … The total number of orders divided by sales". The console help (B10) and the v3 columns have them right. [official] (Search term reports in bulksheets; Search term report for Sponsored Products) A reader computes rates from the counts. [seat]

Bulksheet negative keyword rows take "Match type (`negativeExact` or `negativePhrase`)" for both "Campaign negative keyword" and "Negative keyword" entities. [official] (How to create Sponsored Products campaigns in bulksheets, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/create-sp-campaign, read 2026-11-09)

Since 2026-09-09 exports in bulk operations can leave out performance data ("Uncheck the Performance data checkbox"). [official] (All releases, entry of September 9, 2026)

**B12. RULE: AMC has impression-level search terms.**

- `sponsored_ads_traffic` holds "1 record per sponsored ads impression event and 1 record per click event" across SP, SB, SD and Sponsored TV.
- Its `customer_search_term` is "Search term entered by a shopper on Amazon that led to the traffic event … the actual text that shoppers type into the Amazon search bar, as opposed to advertiser-defined keywords", with aggregation threshold `LOW`.
- `match_type` takes `BROAD`, `PHRASE`, `EXACT` or `NULL`.

[official] (Sponsored ads traffic [AMC], https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/sponsored_ads_traffic, read 2026-11-09)

"Low: Values from this column can only be included in the output of workflows if the row contains at least two distinct users … The aggregation threshold is 2". [official] (Data aggregation thresholds in AMC, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/aggregation-threshold, read 2026-11-09)

AMC is the Amazon surface read here that can show a search term with impressions and no click. A row needs at least two distinct users before the term's text is shown. [seat: combination of the two pages]

The MCP server offers an "AMC SQL Generator tool" in closed beta. [official] (Overview [MCP], https://advertising.amazon.com/API/docs/en-us/mcp/mcp-overview, read 2026-11-09)

**B13. RULE: Freshness and restatement.**

- "Initial impression and click data is available using the API within 12 hours. … small changes to impression and click data may happen up to three days after the initial click date".
- "Initial conversion data is available within 24 hours … Restatements of conversion data occur 1, 7, and 28 days after the conversion event. Because conversions are reported on the date of the ad interaction, restatement includes all dates in your attribution window. For example, if your attribution window is 14 days, restatement can update attribution up to 42 days (14 plus 28) after the report date."

[official] (Sponsored ads reporting FAQ (version 3))

GUIDANCE:

- "The invalid traffic detection system monitors traffic data for up to 30 days after the fact … We recommend waiting at least 5 days for the most accurate click data to be available before evaluating campaign performance."
- "Conversion data … is subject to change for up to 60 days back from the current date. We recommend re-retrieving reports monthly".

[official] (Amazon Ads reporting overview)

The service-limits table gives "Impression/click event to availability via API" 12h and "Impression/click invalidation" 72h as P99 guarantees *(figure)*. [official] (Limits, constraints, and quotas, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, read 2026-11-09)

Traffic validation: "Most post-impression IVT is invalidated in real time. Some takes longer to detect, so we monitor traffic for up to 30 days after it occurs. IVT detected in this window is automatically removed from invoices and advertiser reports". Also: "if you notice a significant drop in IVR, with an anomalous increase in select campaign metrics like click-through rate (CTR) or Impressions or Clicks, it could suggest undetected IVT … For Sponsored Ads campaigns, a drop in Conversion Rate (CVR) along with the above changes in metrics, is a higher confidence indicator". [official] (Traffic validation, https://advertising.amazon.com/help/GBYPYH79NGJJ5JPS, read 2026-11-09)

Clicks and impressions in the reports exclude "general and sophisticated invalid traffic". [official] (Search term report for Sponsored Products)

### C. Negative keywords

**C1. RULE: What a negative keyword blocks.**

- "Negative keywords help prevent ads from appearing on shopping results pages that do not meet your campaign objectives. Negative keyword targeting can be used at either the campaign level or ad group level. … When using negative keyword targeting at the campaign level, the targeting will apply to all ad groups created under that specific campaign. When the negative keyword targeting is done at the ad group level, it will only apply to that specific ad group." [official] (Negative keyword targeting [SP], https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/negative-targeting/keywords, read 2026-11-09)
- The console help separates the two kinds of exclusion: "Negative keywords prevent your ads from appearing in shopping results that match specific search queries. To prevent your ads from appearing on specific product detail pages, use negative product targeting". [official] (Add negative keywords or negative products targeting, https://advertising.amazon.com/help/G8W49VU65XQ4T2NS — the page served carries node id GTEHPEG5BXY9UX5W and `lastModified` 2026-10-20 — read 2026-11-09)
- The 2025 release note says the same: "Negatively targeting a keyword prevents your ad from showing on search results pages for that keyword, while `ASIN` and brand negative targeting prevents your ad from showing on the product detail page for that `ASIN` or `ASIN`s with that brand." [official] (All releases, entry of May 22, 2025)

So a negative keyword in an auto ad group acts on the search-results side (close and loose match, which the match-type help defines by "search terms", A10, and any product or category target that serves on results pages). It does not stop substitutes and complements, which the same help defines by "product detail pages", from serving there. [seat: reading of the pages together]

**C2. RULE: Match types, word and character limits.** The console help:

- "Negative keywords can be used with phrase and exact match types".
- "Negative phrase: Ads don't show on shopping queries that contain the complete phrase or close variations. There's a maximum limit of 4 words per negative keyword. There's an 80 character limit."
- "Negative exact: Ads don't show on shopping queries that contain the exact phrase or close variation. There's a maximum limit of 10 words per negative keyword. There's an 80 character limit."
- "You can't change the match type of an existing negative keyword."

[official] (Add negative keywords or negative products targeting, G8W49VU65XQ4T2NS; the same limits on Understand keyword match types, GHTRFDZRJPW6764R)

The API's character rules: "The maximum length of characters in a keyword is **80**. The maximum number of parts for a positive keyword is **10**. The maximum number of parts for a negative keyword is **4**. For `negativeExact` match type, the negative keyword can have up to **10** parts." The rules also bar leading or trailing spaces and limit `.`, `-` and `+` to the middle of keywords. A `"` must be paired ("`40" screen`" is "not supported"). "The reserved phrase `Automatically Selected Keywords` is not accepted". Each marketplace accepts its own scripts. [official] (Limits, constraints, and quotas, "Keyword character constraints") *(figures)*

The SP 3.0 model has three negative match types: `SponsoredProductsCreateOrUpdateNegativeMatchType` = `NEGATIVE_BROAD`, `NEGATIVE_EXACT`, `NEGATIVE_PHRASE`; the read enum adds `OTHER`. [official] (Sponsored Products 3.0 OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json, read 2026-11-09)

The v1 model gives a negative keyword the positive enum `KeywordMatchType` (`BROAD`, `EXACT`, `PHRASE`) with `negative: true`. [official] (Amazon Ads API v1 merged OpenAPI, `KeywordTarget`, `TargetCreate`)

Amazon's keyword guide says negatives come "with options for exact, phrase, or broad match types". [official] (What is Keyword Targeting?)

**Amazon's pages disagree on negative broad.** The console help, the bulksheet entity (`negativeExact` or `negativePhrase`) and the targeting guide ("We recommend using phrase or exact match with negative keywords") name two types. The SP 3.0 model, the v1 model and the keyword guide admit broad. [official] (pages above)

No page read here defines what a negative broad blocks, or whether every ad product accepts it. A write's `207` reply is where acceptance is read. [seat]

**C3. RULE: Close variants apply to negatives.** Both negative definitions say "or close variation(s)" (C2). With the positive definitions in A8 ("plurals, misspellings, and translations"; "outside lights" matching "outdoor lights"), a negative exact on a term may block more queries than the exact string. [official] (Add negative keywords or negative products targeting; Understand keyword match types)

How far "close variation" reaches for a negative is not quantified on any page read. [seat]

**C4. RULE: Negatives take time to act.** "Please note the following buffer periods for negative targeting to take effect: Negative keywords: 72 hours. Negative products/ASINs: 96 hours" *(figures)*. [official] (Add negative keywords or negative products targeting, G8W49VU65XQ4T2NS)

A practitioner repeats Amazon's figures: "Amazon says negative keywords take up to 72 hours to apply and negative ASINs up to 96." [opinion, restating the official page] (Ayush Chaudhary, Adbrew, above)

Spend on a just-negated term during the buffer is expected behaviour, not a failed write. [seat]

**C5. RULE: Endpoints (SP).**

- v1: one operation for every negative. `POST /adsApi/v1/create/targets` with `negative: true`, `targetType` `KEYWORD` and `targetDetails.keywordTarget` {`keyword`, `matchType`}. A `campaignId` alone makes it campaign-level, an `adGroupId` makes it ad-group-level. The reply is `207` with `success` and `error` arrays, each entry carrying its `index`, and the created target shows `targetLevel` `CAMPAIGN` or `AD_GROUP`. [official] (Negative keyword targeting [SP])
- `CreateTargetRequest.targets` takes up to 1000 items *(figure)*.
- `TargetCreate.campaignId` is "Only used for campaign-level targets"; `TargetCreate.adGroupId` is "Only used for ad-group level targets".
- `POST /adsApi/v1/query/targets` requires `adProductFilter` and filters by `negativeFilter`, `matchTypeFilter`, `keywordFilter`, `adGroupIdFilter`, `campaignIdFilter`, `targetTypeFilter`, `stateFilter` and more, with `maxResults` up to 5000 *(figure)*.
- Deletes go through `POST /adsApi/v1/delete/targets`.

[official] (Amazon Ads API v1 merged OpenAPI, `CreateTargetRequest`, `QueryTargetRequest`, `TargetNegativeFilter`, paths)

SP 3.0 endpoints remain in the model:

- `/sp/negativeKeywords` and `/sp/campaignNegativeKeywords` (create `POST`, update `PUT`, `/list`, `/delete`), under `application/vnd.spNegativeKeyword.v3+json` and `application/vnd.spCampaignNegativeKeyword.v3+json`;
- each create request takes up to 1000 items *(figure)*;
- an ad-group negative needs `adGroupId`, `campaignId`, `keywordText`, `matchType` and `state`, and may carry `nativeLanguageKeyword`/`nativeLanguageLocale`.

[official] (Sponsored Products 3.0 OpenAPI)

The 1000 is a per-request batch size. The account caps are on a help page: "Campaign negative keywords 10,000", "Ad group negative keywords 10,000", "Negative products in an ad group (product targeting) 10,000", "Keywords in an account (including negative keywords) 2,000,000" *(figures)*; the page adds "Amazon now increases customer limits as they approach a limit beyond the limits listed below" and that the limits "apply to Sponsored Products, Sponsored Brands, and Display campaigns across all advertiser types". [official] (Sponsored ads campaign limits, https://advertising.amazon.com/help/G86H2227323T8T4Q, `lastModified` 2026-07-29, read 2026-11-09)

The auto-targeting guide's own example lists a group's targets with `POST /adsApi/v1/create/targets` and a filter body. The model's list operation is `POST /adsApi/v1/query/targets`. [official] (Sponsored Products auto targeting; Amazon Ads API v1 merged OpenAPI) The SP auto-campaign guide gets the same ids the model's way: "You get the auto targeting expression IDs to use in the `PUT` operation by calling POST /adsApi/v1/query/targets", and says "Negative targets can be applied at the campaign and ad group level." [official] (Get started with auto campaigns, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/get-started/auto-campaigns, read 2026-11-09) The auto-targeting example's path is a create; sent as written it is a write. [seat]

**C6. RULE: Negatives on every campaign type, with one stated exception.**

- "We have expanded negative targeting so every campaign and ad group has the same options, regardless of targeting type. Now you can negatively target a keyword, `ASIN`, or brand during campaign creation or on any existing campaign or ad group." The entry is headed "in US marketplace". [official] (All releases, entry of May 22, 2025)
- The SP API guide still warns: "Campaign-level negative product targeting for manual campaigns is only available for vendors. Sellers can add campaign-level negative targeting to auto campaigns, but not manual." [official] (Sponsored Products negative product and brand targeting overview, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/negative-targeting/product-brand, read 2026-11-09)
- The SP 3.0 model's `campaignId` on a campaign negative targeting clause says "CampaignNegativeTargetingClauses are only available for AUTO campaigns". [official] (Sponsored Products 3.0 OpenAPI, `SponsoredProductsCreateCampaignNegativeTargetingClause`)

**Amazon's pages disagree.** Outside the US, or for a seller's manual campaign, the reply to the write is where it is read. [seat]

**C7. RULE: Sponsored Brands negatives.**

- "Negative keywords prevent your keyword targeted ads from displaying when the shopping queries of a shopper match your negative keywords. … Negative keyword targeting can be used at the ad group level". "For Sponsored Brands, there is no campaign-level negative targeting."
- The legacy endpoint is `POST /sb/negativeKeywords` with `matchType` such as `negativeExact`.
- SB negative product targets take `asinBrandSameAs` or `asinSameAs` at ad-group level.

[official] (Sponsored Brands negative keyword targeting, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/targeting/negative-keyword-targeting; Sponsored Brands negative product targeting, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/targeting/negative-product-targeting; both read 2026-11-09)

The SB guide also points to a "negative keyword recommendations" resource in the SB 3.0 API; the link's target is `sponsored-brands/3-0/openapi#tag/Negative-keywords/operation/listNegativeKeywords`, which is `GET /sb/negativeKeywords`, the list of the ad group's existing negatives, and the SB 3.0 YAML model holds no negative-keyword recommendation path (§C9). Amazon's keyword guide, by contrast, says negatives can be added "to Sponsored Brands keyword targeting campaigns" and that "These negative keywords, products, or brand targets can be applied at the campaign or ad group level", without separating SB from SP on level. [official] (Sponsored Brands negative keyword targeting; What is Keyword Targeting?)

The exports page says campaign-level support is "negative Sponsored Products targets only" for `KEYWORD`, `PRODUCT_CATEGORY` and `PRODUCT`. [official] (Exports: Target, https://advertising.amazon.com/API/docs/en-us/guides/exports/entities/targets, read 2026-11-09)

Amazon publishes three Sponsored Brands models, and they split the negative paths (settled 2026-11-09, gap fill):

| Model (title in `info`) | URL | Negative paths |
|---|---|---|
| "Amazon Ads API - Sponsored Brands 3.0" (YAML, 26 paths) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | `/sb/negativeKeywords` (GET list, POST, PUT), `/sb/negativeKeywords/{keywordId}` (GET, DELETE archive), `/sb/negativeTargets` (POST, PUT), `/sb/negativeTargets/list`, `/sb/negativeTargets/{negativeTargetId}` (GET, DELETE archive) |
| "Sponsored Brands 3.0" (JSON, 50 paths) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | `/sb/negativeTargets/brands/recommendations` (GET) only; the rest of its paths are the `/sb/v4/...` campaign, ad group and ad paths plus budget-rule, optimization-rule, recommendation and category paths |
| "Sponsored Brands campaign management 4.0" (JSON, 48 paths) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | `/sb/negativeTargets/brands/recommendations` (GET) only |

[official] (the three models, parsed 2026-11-09) So `/sb/negativeKeywords` is on the SB 3.0 YAML (as method/ads-api-surface.md §I says), and the brand-recommendation path is on both the JSON file titled "Sponsored Brands 3.0" and the SB 4.0 model (as this file and keyword-targeting/brand-defense said, each of one file). The JSON "Sponsored Brands 3.0" file's path set is the SB 4.0 set plus `/sb/recommendations/keyword` and `/sb/campaigns/budgetRules/recommendations`. [seat: comparison of the path lists]

The v1 Targets object covers SB negatives ("Sponsored Brands" column in the v1 target entity table, with `negative` required). [official] (Targets [campaign management entity guide], https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/target, read 2026-11-09)

The SB broad-match modifier "+": "the ad will match only the searches that contain the word "kids."" [official] (Understand keyword match types)

**C8. RULE: No negative scope above the campaign was found (gap fill 2026-11-09).**

- The v1 models (`AmazonAdsAPIALLMerged_prod_3p.json` and the `_ALL` file that adds betas) define `TargetLevel` as `AD_GROUP` ("Target applied at the ad group level") and `CAMPAIGN` ("Target applied at the campaign level") only. No v1 create path names a negative list, shared list or exclusion list (the `_ALL` file's 147 paths were listed; its only "exclusion"-named schemas are DSP brand-safety and converter-exclusion types). [official] (Amazon Ads API v1 merged OpenAPI; v1 merged OpenAPI incl. beta, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p_ALL.json; read 2026-11-09)
- The SP 3.0 model's negative paths are ad-group level (`/sp/negativeKeywords`, `/sp/negativeTargets`) and campaign level (`/sp/campaignNegativeKeywords`, `/sp/campaignNegativeTargets`); SB and SD negatives are ad-group level only (C7, C9). [official] (Sponsored Products 3.0 OpenAPI; Sponsored Brands 3.0 YAML; Sponsored Display 3.0 YAML)
- A portfolio carries a budget, not targeting. The help page: "Use portfolio budget caps to set and manage your spending for a group of campaigns", with "No budget cap", "Recurring monthly budget cap" and "Date range budget cap". [official] (Portfolio budgets, https://advertising.amazon.com/help/GU7E77PGF96FMW3X, read 2026-11-09) The bulksheet "Portfolios" tab's columns are Product, Entity, Operation, Portfolio ID, Portfolio Name, Budget Amount, Budget Currency, Budget Policy, Budget Start Date, Budget End Date, State and In Budget, and nothing else. [official] (Use portfolios with bulksheets, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-portfolios, read 2026-11-09)
- A bulksheet negative row names its campaign: "Campaign negative keyword entity fields: Campaign ID, State, Keyword text, Match type (`negativeExact` or `negativePhrase`)"; "Negative keyword entity fields: Campaign ID, Ad group ID, State, Keyword text, Match type". [official] (How to create Sponsored Products campaigns in bulksheets) A row whose "Operation" is blank "will be ignored in the upload process". [official] (Bulksheets FAQs, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/faqs, read 2026-11-09)
- The one cross-border scope: a global Sponsored Products campaign (v1, `marketplaceScope` `GLOBAL`) lets one target carry a `marketplaces` list, "a child's list must be a subset of its parent's", with `marketplaceConfigurations` "per-marketplace overrides"; its writes return `207` with `success`, `error` and `partialSuccess` arrays. The guide's own example adds a Spanish keyword as a separate target with `"marketplaces": ["ES"]`. [official] (Global campaigns for Sponsored Products; Amazon Ads API v1 merged OpenAPI, `MarketplaceScope` = `GLOBAL`, `SINGLE_MARKETPLACE`) It is still a campaign-level or ad-group-level target.
- Searches on 2026-11-09 for an Amazon announcement of account-level, brand-level, portfolio-level or shared negative keywords found none on an Amazon page (search terms in Pages read). [seat]

[seat] A negative that should hold for a product group across N campaigns is therefore N campaign-level writes (or N×M ad-group writes in SB and SD), each read back from its own reply; the per-request batch sizes are in C5 and C9, the per-campaign caps on "Sponsored ads campaign limits".

**C9. RULE: The per-product (v3) negative endpoints, and what v1 covers (gap fill 2026-11-09).** Each path below is on its model as read today; the Deprecations page lists no shutoff for any of them. SP 3.0 `sp/negativeKeywords`, `sp/campaignNegativeKeywords`, `sp/negativeTargets` and `sp/campaignNegativeTargets`, and SB 3.0 `/sb/negativeKeywords`, appear there only as the replacements for the SP v1/v2 endpoints shut off on 2023-06-30 and the SB v2/HSA endpoints shut off on 2022-12-31. [official] (Deprecations, read 2026-11-09)

| Ad product | Level | Create / update / delete / list | Body and enums | Reply |
|---|---|---|---|---|
| SP 3.0 | ad group | `POST /sp/negativeKeywords`, `PUT /sp/negativeKeywords`, `POST /sp/negativeKeywords/delete`, `POST /sp/negativeKeywords/list` | media type `application/vnd.spNegativeKeyword.v3+json`; required `adGroupId`, `campaignId`, `keywordText`, `matchType`, `state`; `matchType` `NEGATIVE_BROAD`, `NEGATIVE_EXACT`, `NEGATIVE_PHRASE`; `state` `ENABLED`, `PAUSED`, `PROPOSED` | `207`: `negativeKeywords.success[]` (`index`, `negativeKeywordId`, and `negativeKeyword` when `Prefer: return=representation`) and `negativeKeywords.error[]` (`index`, `errors[]` of `errorType` + `errorValue`) |
| SP 3.0 | campaign | `/sp/campaignNegativeKeywords` (same four operations) | `application/vnd.spCampaignNegativeKeyword.v3+json`; required `campaignId`, `keywordText`, `matchType`, `state`; same enums | `207`, same shape under `campaignNegativeKeywords` |
| SP 3.0 | ad group | `/sp/negativeTargets` (same four operations) | `application/vnd.spNegativeTargetingClause.v3+json`; required `adGroupId`, `campaignId`, `expression`, `state`; predicates `ASIN_BRAND_SAME_AS`, `ASIN_SAME_AS` | `207`, `negativeTargetingClauses.success[]`/`error[]` |
| SP 3.0 | campaign | `/sp/campaignNegativeTargets` (same four operations) | `application/vnd.spCampaignNegativeTargetingClause.v3+json`; required `campaignId`, `expression`, `state`; `campaignId` "CampaignNegativeTargetingClauses are only available for AUTO campaigns" | `207` |
| SB 3.0 (YAML) | ad group | `POST /sb/negativeKeywords`, `PUT /sb/negativeKeywords`, `GET /sb/negativeKeywords` (filters `matchTypeFilter`, `keywordText`, `stateFilter`, `campaignIdFilter`, `adGroupIdFilter`, `keywordIdFilter`, `creativeType`), `GET` and `DELETE /sb/negativeKeywords/{keywordId}` | JSON array, "maximum list size of 100 negative keywords"; `adGroupId`, `campaignId`, `keywordText`, `matchType` `negativeExact` or `negativePhrase`; "The `bid` and `state` can't be set at negative keyword creation" | `207`: an array "in the order of the request", each `code`, `description`, `keywordId`, `errors[]` |
| SB 3.0 (YAML) | ad group | `POST /sb/negativeTargets`, `PUT /sb/negativeTargets`, `POST /sb/negativeTargets/list`, `GET` and `DELETE /sb/negativeTargets/{negativeTargetId}` | `{negativeTargets: [...]}`, 1–100 items; `adGroupId`, `campaignId`, `expressions[]` of `type` `asinBrandSameAs` or `asinSameAs` and `value` | `200`: `createTargetSuccessResults[]` and `createTargetErrorResults[]`, each keyed by `targetRequestIndex` |
| SD 3.0 (YAML) | ad group | `POST /sd/negativeTargets`, `PUT /sd/negativeTargets` (mutable field `state`, up to 100), `GET /sd/negativeTargets`, `GET /sd/negativeTargets/extended`, `GET /sd/negativeTargets/{negativeTargetId}`, `DELETE /sd/negativeTargets/{negativeTargetId}` (archive) | JSON array, "up to 100"; required `adGroupId`, `expressionType` (`manual`, `auto`), `expression`, `state` (`enabled`, `paused`, `archived`); `type` `asinSameAs` or `asinBrandSameAs`; "Only one brand may be specified per targeting expression. Only one asin may be specified per targeting expression." | `207`: an array of `TargetResponse` (`code`, `description`, `targetId`) |

[official] (Sponsored Products 3.0 OpenAPI; Sponsored Brands 3.0 YAML; Sponsored Display 3.0 YAML, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml; all parsed 2026-11-09)

More from the same models and guides:

- SP 3.0 writes take a `Prefer` header: "return=representation - return the full object when doing create/update/delete operations instead of ids." [official] (Sponsored Products 3.0 OpenAPI, `CreateSponsoredProductsNegativeKeywords` parameters)
- SB 3.0: "negative keywords *can not* be recreated for a campaign if the negative keyword has previously been associated with a campaign and subsequently archived", and negatives "can be created on campaigns where campaign's serving status is not one of `archived`, `terminated`, `rejected`, or `ended`". "Negative keywords associated with BrandVideo ad groups are only available in v3.2 version" (`application/vnd.sbnegativekeyword.v3.2+json`). [official] (Sponsored Brands 3.0 YAML, `createNegativeKeywords`, `listNegativeKeywords`)
- SB 3.0 `SBNegativeMatchType` and `NegativeMatchType` are `negativeExact` and `negativePhrase` only. [official] (Sponsored Brands 3.0 YAML)
- SD: "Negative Targeting is available to contextual targeting campaigns using the `/sd/negativeTargets` resource. This resource follows the same format as regular targeting expressions defined in `/sd/targets` with the exception being that all targeting expressions are negated within the ad group." The SD 3.0 model has no negative keyword path. [official] (Sponsored Display contextual targeting guide, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/contextual-targeting, read 2026-11-09; Sponsored Display 3.0 YAML)
- The two SB 3.0 reply shapes differ: negative keywords return `207` with a top-level array; negative targets return `200` with success and error arrays keyed by `targetRequestIndex`. [official] (Sponsored Brands 3.0 YAML)

**What v1 covers for Sponsored Display.**

- The v1 model's `AdProduct` enum includes `SPONSORED_DISPLAY`, and the campaign-management overview lists "Sponsored Display" among the ad products it "currently supports". [official] (Amazon Ads API v1 merged OpenAPI; Campaign management overview, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview, read 2026-11-09)
- The v1 target entity tables (entity guide and common-model page) have columns for Common model, Sponsored Products, Sponsored Brands and Amazon DSP only; there is no Sponsored Display column, so no v1 page read states which target types or negatives SD accepts. [official] (Targets [campaign management entity guide]; The target entity in the Amazon Ads API [common models], https://advertising.amazon.com/API/docs/en-us/reference/common-models/targets; read 2026-11-09)
- The general-availability notes of 2025-08-01 and 2025-12-01 cover "Sponsored Products, Sponsored Brands, and Amazon DSP" and promise "Sponsored Display and Sponsored TV later" ("later in 2025"; "later this year"). No 2026 entry read on All releases announces Sponsored Display in the v1 Campaign Management API. [official] (All releases, entries of August 1, 2025 and December 1, 2025, read 2026-11-09)

[seat] For SD the documented negative write is `POST /sd/negativeTargets`; whether `POST /adsApi/v1/create/targets` with `adProduct` `SPONSORED_DISPLAY` and `negative: true` is accepted is read from its reply. For SP and SB both the v1 and the v3 paths are documented; the v3 path is the fallback the models carry where a v1 write is refused.

### D. Negative product and brand targets

**D1. RULE.**

- "Both auto and manual Sponsored Products campaigns can use negative product targeting. Negative product targeting allows you to exclude certain products and brands from your targeting. … Any campaign-level negative product targeting expression will impact all ad groups using product targeting in the campaign." [official] (Sponsored Products negative product and brand targeting overview)
- The console help on scope: "These product targets prevent your product targeted or automatically targeted ads from displaying when the ASIN of a product page matches the negative product target. Negative product targets created at the ad group level affect product attribute targets or automatic targets configured in the same ad group. Negative product targets created at the campaign level affect product attribute targets or automatic targets in any ad group within the campaign." [official] (Add negative keywords or negative products targeting)
- On whose pages: "To keep your Sponsored Products ads off specific product detail pages, whether your own or a competitor, use negative product targeting." [official] (same page)

**D2. RULE: Shapes.**

- v1: an ASIN negative is `targetType` `PRODUCT` with `productTarget` {`matchType` `PRODUCT_EXACT`, `product.productId`, `productIdType` `ASIN`}.
- A brand negative is `targetType` `PRODUCT_CATEGORY` with `productCategoryRefinement` carrying `productBrandId` and `productCategoryId`.

[official] (Sponsored Products negative product and brand targeting overview)

SP 3.0 negative expression predicates are only `ASIN_BRAND_SAME_AS` and `ASIN_SAME_AS` (read enum adds `OTHER`), up to 1000 expressions per clause *(figure)*. [official] (Sponsored Products 3.0 OpenAPI, `SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType`)

Brand ids come from:

- `GET /sp/negativeTargets/brands/recommendations`: "Returns brands recommended for negative targeting. Only available for Sellers and Vendors. These recommendations include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands."
- `POST /sp/negativeTargets/brands/search`: "Returns up to 100 brands related to keyword input".

[official] (Sponsored Products 3.0 OpenAPI, path descriptions)

**D3. GUIDANCE: Amazon's own examples of what to exclude.**

- "Keyword targeting: Low-performing keywords; Shopping terms you don't want your ads to appear against. Product targeting: Low-performing ASINs; ASINs you don't want your ads to show against; Non-complementary ASINs in an ad group".
- The camera-lens example: "your ad … appearing next to a non-compatible camera. By adding this camera as a negative ASIN, you can stop your ad from appearing there".

[official] (A guide to targeting with Sponsored Products; the camera-lens example also appears, worded "a noncompatible camera", on Best practices for your Sponsored Products ads)

**D4. RULE: How negatives meet auto, broad and product-attribute targets.** Reading C1 and D1 together [official]:

- A negative keyword acts on search-results queries, in any ad group it covers: keyword ad groups, auto ad groups and product-targeting ad groups. Amazon's keyword guide names "Sponsored Products automatic, product, and keyword campaigns".
- A negative ASIN or brand acts on detail pages. It covers "product attribute targets or automatic targets", meaning auto targets and ASIN or category targets.
- Neither kind is said to affect a positive keyword's match on a query the negative does not cover.

(What is Keyword Targeting?; Add negative keywords or negative products targeting)

A negative exact on a harvested query in a broad or auto ad group leaves the broad keyword or auto target serving every other query it matches. A negative phrase removes every query containing the phrase (with close variants). [seat: from the definitions in C2]

### E. Harvesting: Amazon's own descriptions

**E1. GUIDANCE: Auto first, then manual from its report.**

- "We recommend that you let your automatic campaign run for about two weeks before creating a manual campaign." *(figure)*
- "By using metrics from the automatic campaign search term report, you can gain insight on the best keywords or products to target for your manual targeting campaign."
- On product targeting: "Targeted ASINs that generate clicks or conversions show up in the “search term” column. … These can be added to product targeting campaigns as targets".
- Automatic targeting is "based on previous shopping queries and your product information".

[official] (A guide to targeting with Sponsored Products)

The keyword guide says auto "analyzes your product details, including titles and descriptions" and advises: "Start with broader match types to discover valuable search terms, then add high-performing queries as exact match keywords to help optimize performance"; "After your campaign has been running for a couple of weeks, you can use the search term report to learn which keywords perform best for your products, and leverage those in campaigns with manual targeting." [official] (What is Keyword Targeting?)

**E2. GUIDANCE: Harvest to exact, raise the bid.** "Search term report: Find the shopping terms used by customers shopping on Amazon that resulted in at least one click on your ad." Then: "First, check the search term report to identify keywords and products that are resulting in higher sales and conversion rate. Then increase the bid on those and add them as exact match type to optimize. Also, identify the keywords and products with low sales and conversion rates and decrease your bids on them." [official] (Best practices for your Sponsored Products ads)

Amazon's 2022 keyword-strategy blog says to move high performers into exact. It gives "cheap" as a negative example for a luxury product. [official] (How to start and improve your keyword strategy, https://advertising.amazon.com/blog/how-to-start-and-improve-your-keyword-strategy, `dateModified` 2026-10-09, read 2026-11-09)

The help page: "For Sponsored Products campaigns, you can copy these settings from the Search terms section of your ad group to new ad groups, to convert these performance insights into targeting expressions across ad groups. For example, you may add high-performing keywords and products as new targeting parameters to an ad group, and low-performing keywords and products as negatively targeted." It also names the expanded product targeting feature: "you can identify the expanded targets that satisfy your performance criteria to promote them as individual targets." [official] (Search term report for Sponsored Products)

**E3. RULE: Target Promotion is Amazon's own harvest mechanism.** It was released 2023-10-23 (All releases). The guide: "This combines the common practice of target harvesting, which identifies targets to move from broader targeting (for example, automatic targeting) to more focused targeting (for example, manual targeting with broad match), with optimized bids and budget changes." `POST /sp/targetPromotionGroups` "creates a target promotion group and an associated manual keyword targeting campaign, ad group, and ads, as well as an associated manual product targeting campaign, ad group, and ads, based on the `adGroupId` of the given auto-targeting campaign". [official] (Target Promotion, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/target-promotion, read 2026-11-09)

Endpoints:

- `POST /sp/targetPromotionGroups`;
- `POST /sp/targetPromotionGroups/list`;
- `POST /sp/targetPromotionGroups/recommendations`;
- `POST /sp/targetPromotionGroups/targets` and `/targets/list`.

The guide's sample recommendations carry `recommendationReasons` such as `HISTORICAL_PERF` with `CLICKS` and `CONVERSIONS` data; the model describes the list as "optimized targets for the request, as recommended by Amazon heuristics" and the reason object as "a reason for why this target is being recommended for harvesting". [official] (Sponsored Products 3.0 OpenAPI; Target Promotion)

No page read here says Target Promotion adds a negative in the source ad group. [seat]

A practitioner says of Prompts and Amazon Ads Agent: "Neither negates a term at its source for you", and "A one-click keyword doesn't add the matching negative in your research campaigns". [opinion] (Ayush Chaudhary, Adbrew)

**E3b. RULE (announced): Seller Assistant's ad auto-optimization adds and pauses search terms.** At Accelerate 2026 Amazon described a capability that, after a drafted campaign goes live, "keeps working while the seller is doing something else: adding search terms that are performing, pausing those that aren't, and holding every bid under a maximum the seller sets", and said "new campaigns using it saw a first sale 40 percent faster" *(figure)*. [official] (At Accelerate 2026, Amazon shares new AI tools as a force multiplier for independent sellers, https://sellingpartners.aboutamazon.com/accelerate-2026-recap, `datePublished` 2026-09-29, read 2026-11-09) The page states no threshold for "performing" and nothing about negatives at the source; no API page read here documents the capability. [seat]

**E4. RULE: MCP describes harvesting as a workflow, with no harvest tool.**

- Release note: MCP workflows "automate keyword harvesting from automatic to manual campaigns". [official] (All releases, entry of February 18, 2026)
- The campaign-management tool list read today has 32 tools, including `create_target`, `update_target`, `query_target`, `delete_target` and `create_singleshot_sp_campaign`. None is named for harvest or negatives. [official] (MCP campaign management tool definitions, https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/campaign_management.json, read 2026-11-09)

**E5. RULE: Each row names its source.** The bulksheet search term tab carries `Keyword Id (Read only)` ("Use this ID in the "keyword" entity row to update keywords") and `Product Targeting Id (Read only)` with the source `Campaign Id` and `Ad Group Id`; the tab itself "is read-only", and changes go into the campaign tab. Its "Match Type" column "cannot be updated, but you can create new keywords with the match type you want". [official] (Search term reports in bulksheets)

In v3 the same is `keywordId`, `adGroupId` and `campaignId` on each row. [official] (Search term reports [v3])

### F. Judging a term: Amazon's own numbers

**F1. GUIDANCE: 20 clicks, then two weeks.**

- "Before deciding to add a keyword as a negative target, we recommend evaluating its performance after it has received at least 20 clicks." *(figure)*
- "Remember, adding negative targets is not a permanent action, you can always remove them. However, let your negative keywords run for two weeks or more, before making any changes to your strategy." *(figure)*

[official] (A guide to targeting with Sponsored Products)

These are the only numeric negation thresholds found on an Amazon page in this read. They are stated as recommendations, not rules. [seat]

**F2. GUIDANCE: Wait for clicks and conversions to settle.** "Wait at least 5 days for the most accurate click data" (B13). Conversions are subject to change up to 60 days back. With a 14-day window, restatement can reach 42 days after the report date (B13). [official] (Amazon Ads reporting overview; Sponsored ads reporting FAQ (version 3))

The console and API count a click's purchases for 7 days (SP sellers) or 14 days (SP vendors, SB) after it (B5). A term clicked on the last day of a pull has had no time to convert. [official, with seat reading]

**F3. Not Amazon's guidance: an opinion on Amazon's domain.** An Amazon-hosted Ad Intel article by a named agency founder:

- under "Problem 1: Ineffective use of keyword match types" recommends "a layered strategy with segmentation by match type, migration of successful search terms to tighter match types, and consistent application of negative keywords";
- writes "I recommend monitoring and optimizing for CTR as much as you do for return on ad spend (ROAS) to avoid sending a bad signal to Amazon";
- under "Problem 4: Not harmonizing product detail page with shopper searches" ties clicks that don't turn into sales to a gap between the ad and the detail page.

[opinion] (Brent Zahradnik, Founder & CEO of AMZ Pathfinder, "Ad Intel: 5 common sponsored ads campaign mistakes (and how to fix them)", Amazon Ads, 2025-08-05, https://advertising.amazon.com/library/expert-advice/common-sponsored-ads-mistakes-and-solutions, `dateModified` 2026-10-09, read 2026-11-09)

Ad Intel pieces carry the author's name and agency, and are opinion even on Amazon's domain. [seat]

### G. Search term impression share and rank

**G1. RULE: Console report.** "You can now understand how your Sponsored Products impression share compares to other advertisers with the search term impression share report, now available in the Report Center. The report shows how your account-wide impression share for each search term compares to other advertisers, and the overall percentage of ad impressions you receive compared to other advertisers over a selected time period." (announced 2021-03-22). Its example is dated: "if you have a Sponsored Products impression share of 20% for a search term on a given date, it means that you won 20% of all Sponsored Products ad impressions for that search term on that date." The SB search term rank report came earlier (2020-10-30). [official] (Search term impression share report for Sponsored Products, https://advertising.amazon.com/resources/whats-new/search-term-impression-report-sponsored-products, read 2026-11-09; Introducing the search term impression rank report, https://advertising.amazon.com/resources/whats-new/search-term-rank-report, read 2026-11-09)

**G2. RULE: v1 metrics are account-wide.**

- `metric.impressionShare` and `metric.impressionShareRank` require `adProduct.value`, `advertiserAccount.id` and `searchTerm.value`.
- They are incompatible with campaign, ad group, ad, target, advertised product, placement and the time-of-day dimensions.
- `metric.topOfSearchImpressionShare` is compatible with campaign but "incompatible" with ad group, target and search term.

[official] (Impression share metrics [search], https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/metrics/impression-share/search, read 2026-11-09)

- `metric.impressionShare` and `metric.impressionShareRank` list Date, Day, Week, Month, Year and Date range among compatible dimensions.

So the search-term share is the account's share on that query across all its campaigns. It cannot be split by the keyword that won it, but the v1 page lets it be read per date. [seat]

**G3. RULE: v3 places it on campaigns and targeting.** `topOfSearchImpressionShare` is listed for `spCampaigns`, `sbCampaigns` and `sbTargeting`; it is not on `spSearchTerm`. [official] (Reporting columns (version 3))

SB v2 `searchTermImpressionShare` and `searchTermImpressionRank` stop returning values on 2026-11-10 (B2). [official] (Deprecations)

**G4. RULE: Keyword recommendations carry share for targeted keywords.** In SP 3.0 keyword recommendations, `searchTermImpressionShare` and `searchTermImpressionRank` are "account-level", for "the last 30 days" *(figure)*, and "only available for keywords the advertiser targeted with ad impressions". [official] (Sponsored Products 3.0 OpenAPI, keyword recommendation response) The Sponsored Brands keyword recommendation fields of 2023 describe share "over last 7 days" *(figure)*. [official] (All releases, entry of May 25, 2023)

**G5. RULE: Brand-term share.** The brand impression share view reports top-of-search impression share on the advertiser's brand terms across SP and SB, rolled up across accounts. [official] (Brand impression share, https://advertising.amazon.com/help/GNU4AUAUHS76DNDR, read 2026-11-09)

Its use in defence is beyond/brand-defense-and-competition.md's.

**G6. RULE: SP-API Search Query Performance is a different object.** The Brand Analytics Search Query Performance report gives, per ASIN, `searchQuery`, `searchQueryVolume` and `searchQueryScore`, with total and ASIN impression, click, cart-add and purchase counts and shares. Periods are `WEEK`, `MONTH` or `QUARTER`, and "Requests cannot span multiple periods". [official] (sellingPartnerSearchQueryPerformanceReport.json, https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchQueryPerformanceReport.json, read 2026-11-09)

It counts organic and paid together, and is a brand-registered seller's report through SP-API, which this seat does not call. Its join to ad terms is areas/ads-organic-and-total.md's. [seat]

## What practitioners add

Everything here is [opinion]: a named person's or firm's claim, as theirs. Thresholds are theirs, not rules. Where several practitioners agree, that agreement is reported, not promoted.

### Thresholds for negating a term with no orders

| Who | Claim | Page |
|---|---|---|
| Ad Badger (Michael Erickson Facchin) | "Search terms that get your ad over 2500 impressions with less than 0.18% CTR and no conversions aren't worth your time"; "any search terms creating more than $35 in ad spend with no conversions should be eliminated"; "anything with over 34 clicks that hasn't converted yet is already suffering miserably. Kill it." "These thresholds are starting points — adjust them to your product's margin and conversion rate." "Do not apply standard non-converter thresholds to competitor brand terms." For a term that is unprofitable but relevant, one option is to add it as positive exact at a much lower bid, and "Don’t forget to block the same keyword as a negative exact for your broad match/auto campaigns". | "Amazon PPC Negative Keywords: Cut Wasted Ad Spend (2026)", published 2025-03-06, modified 2026-10-28, https://www.adbadger.com/blog/amazon-ppc-education/negative-keywords-amazon-ppc/ |
| Ad Badger (The Badger) | The same three rules as an automation ("Nightly Hunt"), scanning "the past six months". Its separate "Quick Attack" tool "has options to exclude the last two days from your data because of the 48-hour Amazon reporting delay". The body text gives 40 clicks where the rule says 34. | "The Easiest Way to Automate Negative Keywords for Amazon Ad Campaigns", published 2018-10-31, modified 2023-10-23, https://www.adbadger.com/blog/amazon-ppc-education/automate-negative-keywords/ |
| Ad Badger (The Badger, PPC Den episode page) | "Branded terms might convert every couple of clicks. Competitor terms might need fifty clicks before you see a sale." "If you use one rule across the board, you'll end up killing keywords that were slow, not bad." "Look at what your converting traffic normally does and use that as your benchmark." The episode's "75%-150% CPS range" and "1.5× CPS decision point" are named in the highlights only; the rule itself is in the audio, not read. | "How many clicks before you kill a keyword? CPS rule", 2026-01-30, https://www.adbadger.com/blog/amazon-ppc-education/how-many-clicks-before-you-kill-a-keyword-cps-rule-the-ppc-den-podcast/ |
| Scale Insights | Its negative-word rule splits search terms into single words and aggregates them per product, over "60 days of customer search terms, skipping the past 2 days" (up to 180 days, configurable). Its "Unique Word with 0 Sales" filter finds "words with at least 25 clicks but 0 orders" (customisable). The rule adds non-performing words as negative phrase to ad groups with the rule assigned, and "If the word appears in your title, the algorithm will not negate the singular/plural form of the word." | Scale Insights docs, "What is the negative word rule?", undated, https://docs.scaleinsights.com/docs/what-is-the-negative-word-rule |
| Helium 10 Team (a Prestozon article) | Over "the last 90 days", suggests a negative when "You could have expected a sale given the number of clicks" (from the product's average order value and conversion rate) or when "even if you got a sale on the next click you’d exceed your ACOS target by 50%". Suggests a keyword "Anytime a search term generates at least one sale". | "Prestozon’s Rules Engine and Why It Changes the Game", 2018-04-26, modified 2022-03-10, https://www.helium10.com/blog/amazon-ppc-keyword-management-rules/ |
| Jungle Scout (Rolando Galeana) | "any time I've paid for 10 clicks and have gotten zero sales for a search term, I add it to my negative keyword list"; "If I get between five and 10 clicks, then I usually use my best judgment." | "Million dollar case study: optimizing PPC campaigns", 2019-05-21, https://www.junglescout.com/blog/million-dollar-case-study-optimizing-ppc-campaigns/ |
| Canopy Management | Scales by price: $30–100 products 20–30 clicks; $100+ 40–50; low-margin 15–20. Negates at ACoS 2–3× target only after bid cuts fail. "Fix the offer before blocking the traffic." Uses lighter negatives at launch. | "How to Build a Negative Keyword Strategy That Protects Your Amazon Ad Budget", CANOPY Management, 2025-12-04, https://canopymanagement.com/?p=23024 |
| FiveX (Lisa van Broekhoven) | For smaller accounts, 15–25 clicks and two or more orders before scaling a query. Negative exact is "usually safer for isolating a proven query". | FiveX blog, search term isolation and profit control, 2026-08-04, https://fivex.com/blog/amazon-search-term-isolation-profit-control/ |
| Seller Labs (unsigned) | Allows "at least 7–14 days before evaluating"; avoids "Evaluating performance with fewer than 20–30 clicks". "If a keyword spends 1–1.5× your break-even CPA without a sale, evaluate reducing bids or pausing." Harvests "Every 1–2 weeks". | "Keyword Harvesting Framework: Turning Auto Campaign Data into Profitable Manual Amazon PPC", updated 2026-07-30, https://www.sellerlabs.com/knowledge-base/keyword-harvesting-framework-turning-auto-campaign-data-into-profitable-manual-amazon-ppc/ |
| Perpetua (help, Josh Lobo) | Its "Negative Exact Match Rules" strategy uses user-set "Clicks Greater Than" and "Conversions Less Than" values ("consider entering "1" as the lowest conversion value"). It runs only on "Sponsored Product (Classic Multi-Campaigns) goals that have been active for more than 30 days"; "ASIN/PAT search terms are not currently supported". | Perpetua help, "Negative exact match strategy", "Article last updated October 2024", https://help.perpetua.io/en/articles/6027156-negative-exact-match-strategy |

Across these pages the click bar runs from 10 (Jungle Scout, 2019) to 50 (Ad Badger for competitor terms; Canopy for $100+ products). Every page that gives a single number also says to adjust it by price, margin or conversion rate. [seat: summary of the table]

### Thresholds for harvesting

- **Adbrew (Ayush Chaudhary, 2026-10-27):** three layers, Research (auto, broad, category, keyword groups), Discovery (phrase) and Performance (exact, individual ASIN targets), called "practitioner defaults we start every account on, not Amazon rules".
  - Rule A: "at least 1 order in the last 30 days, ACOS up to 1.5 times target, and a relevant multi-word term" moves a term to phrase. Rule B: "at least 2 orders in the last 30 days at or under target ACOS" moves it to exact.
  - "Both rules run on a 30-day window that excludes the last 7 days." For conversion rates under 5%, a 60-day window. "Event weeks: pause graduation during Prime Day or Black Friday."
  - Worked example: a product converting at 12% needs about 17 clicks to expect two orders; at 6%, about 33.
  - Adds a negative exact in the source and in every auto, broad and phrase campaign of the product group. Reserves negative phrase for concepts that never convert.
  - [opinion] (Adbrew, above)
- **Helium 10 Team (Prestozon article, 2018, modified 2022):** a converting search term becomes "Broad match + Negative exact keywords in the Broad ad group", "Exact match new keywords in the Exact ad group" and "Negative phrase in the automatic campaign". [opinion] (Helium 10, above)
- **Helium 10 (Lauren Stair, 2026-04-02):** "A simple starting rule might specify that any search term generating two orders with ACoS below 30% in your auto campaign automatically becomes an exact match keyword in your manual campaign", reviewing "the past 30-60 days". [opinion] ("Reclaim 20+ Hours Per Week: Automated Amazon PPC", https://www.helium10.com/blog/reclaim-20-hours-per-week-how-to-automate-amazon-ppc-management/, read 2026-11-09)
- **Seller Labs:** "Profit-Based Harvesting: 2+ orders, ACoS at or below your target, Strong CVR compared to campaign average"; "Long-Tail Testing: 1 sale with low click count". "Exact Match Campaign (primary control layer)", optional phrase as "expansion layer". After moving keywords, "Add them as Negative Exact in the Auto campaign. This prevents: Internal competition, Inflated CPC, Performance dilution". "Avoid: Adding as Negative Phrase unless intentionally blocking variations." [opinion] (Seller Labs, above)
- **Canopy:** "Once you identify your top-converting terms, negative them in your auto and broad campaigns"; competitor terms go to "a separate conquesting campaign with a capped budget"; negative exact for one failing query, negative phrase when a pattern repeats. [opinion] (Canopy, above)
- **FiveX:** "every material query gets one owner, one bid, one budget rule and one commercial permission to scale". In an illustrative "scenario", halving a branded query's bid from €0.70 to €0.35 left total SKU sales "almost flat". [opinion] (FiveX, above)
- **Intentwise (Michael Waters, 2023-11-15, modified 2026-08-10):** defines harvesting as adding top-performing search terms as keywords, and says search term reports "tell you which keyword the search terms matched to (except for Auto campaigns)". [opinion] (Intentwise blog, "Explained: What is keyword harvesting on Amazon?", https://www.intentwise.com/blog/what-is-keyword-harvesting) Amazon's report does name the auto targeting expression (A10). [seat]

### Negative phrase, negative exact and word-level negatives

- Scale Insights Team (undated): negative phrase "blue shoes" would block "cheap blue shoes" but not "shoes blue"; negative exact "blue shoes" would not block "blue running shoes". The same paragraph also says a negative phrase "blue shoes" blocks "blue running shoes", which contradicts its own "exact phrase appears" definition. Recommends "reviewing and updating it at least once every two weeks" and warns that "overusing negative keywords" blocks relevant queries. [opinion] ("What Are Amazon Negative Keywords And 7 Tips To Master Them", https://scaleinsights.com/learn/amazon-negative-keyword)
- JumpFly (Shannon O'Connell, 2019-10-02): "Negative phrase match uses the keyword or string of keywords in any order as a negative", with the example that phrase "water bottle" also catches "bottle water". Scale Insights (above) and Ad Badger ("contain the selected set of words in an exact sequence") say the opposite. Amazon's definition is "contain the complete phrase or close variations" (C2); no Amazon page read here states word order for negative phrase. [opinion] (JumpFly, https://www.jumpfly.com/blog/the-5-ws-and-1-h-of-amazon-ads-negative-keywords/)
- Ad Badger states negatives "only have two match type[s]". This matches the console help, not the API models (C2). [opinion] (Ad Badger, above)
- Perpetua (Megha Natarajan, 2022-02-02) describes NLP tokenisation with statistical thresholds and reports "98% of the word tokens identified … were indeed irrelevant", with no sample size given. [opinion] (Perpetua blog, "Curbing spend on irrelevant search terms", https://perpetua.io/blog-curbing-spend-on-irrelevant-search-terms/)

### Shared and account-wide negative lists (gap fill 2026-11-09)

- **Karooya (Kirti, 2019-02-12):** "The convenience of the shared negative keyword list has been missing from Amazon Ads." Its tool keeps the list outside Amazon: "all the negative keywords in that list are added as campaign-level negative keywords in your Amazon Ads account", and "that negative keyword is then added to all the campaigns associated with that list … you make one change and it gets replicated in all the associated campaigns." [opinion] ("[New Feature] Introducing Shared Negative Keywords List for Amazon Ads", https://www.karooya.com/blog/introducing-shared-negative-keywords-list-for-amazon-ads/, read 2026-11-09)
- **SellerSprite Success Team (2026-06-16):** "Amazon allows you to create reusable Negative Keyword Lists", "You can then apply these lists to multiple campaigns with one click", and "If you use Amazon Portfolios, you can apply negative keywords across multiple campaigns." [opinion] ("Negative Keywords Guide: Reducing Wasted Ad Spend", https://www.sellersprite.ai/en/blog/Negative-Keywords-Guide-Reducing-Wasted-Ad-Spend, read 2026-11-09) No Amazon model, help page or bulksheet tab read here carries a negative list or a portfolio-level negative (C8); Amazon's own pages as read contradict the claim. [seat]
- **RedHen Labs (Rowdy Rooster Woodworks seller blog, unsigned, 2026-08-27):** "Mine is 69 distinct keywords across 43 live campaigns", "Every negative keyword on my account is set at the campaign level", "All exact match. Not one negative phrase", and "Amazon does not accept campaign-level negative keywords on Sponsored Brands at all"; its tool "watches the thresholds and brings me the candidates. It doesn't apply them." [opinion] ("Which Negative Keywords Save Money (I Run 69 Account-Wide)", https://rrw-ads.com/blog/which-negative-keywords-save-money, read 2026-11-09)
- **Adbrew (Ayush Chaudhary, 2026-10-27):** "When a term reaches exact, add it as negative exact in every auto, broad and phrase campaign of that product group, … not only the one that found it"; the page never defines "product group". [opinion] (Adbrew, above)

Where practitioners agree: a negative meant for many campaigns is held outside Amazon and written into each campaign. Where they disagree: SellerSprite says Amazon has native lists and portfolio negatives; Karooya (2019) and every Amazon page read say it does not. No practitioner page read describes the bulksheet push of one list across a product group step by step; Amazon's bulksheet rows (C8) show that such a push is one row per campaign or ad group. [seat: summary]

### Reading one query across campaigns (gap fill 2026-11-09)

- **Ad Badger (Michael Erickson Facchin and Clément Hynaux, 2023-05-03):** "You can't drive your bids up by having the same search term in several ad groups." "Amazon recognizes that all your ad groups are from the same entity, so it won't pit them against each other." "If, however, you're using different advertising accounts, you will drive the bids up because Amazon sees the different advertising accounts as different entities." Its Duplicate Hunter "shows you the aggregate performance of each search term with clickable links to the ad groups". [opinion] ("How Do I Identify And Handle Search Term Duplicates In Amazon Advertising?", https://www.adbadger.com/blog/manage-duplicate-search-terms-on-amazon/, read 2026-11-09)
- **Adbrew (Ayush Chaudhary):** without a source negative "the same search keeps serving from two campaigns at two bids, and your reports split it in half"; "Amazon picks which of your campaigns serves, and your exact bid stops being the price you actually pay". It quotes Amazon's "you won't be bidding against yourself" line and disputes it on control grounds, not price. [opinion] (Adbrew, above)
- **Pare (George Reid, 2026-05-11):** "Amazon's algorithm runs an internal auction across your own campaigns" and "The cheapest click wins the impression", citing no Amazon source; "blocking a term in one campaign doesn't stop the others from bidding on it." [opinion] ("Keyword Cannibalization Is Killing Amazon PPC in 2026", https://pare.so/blog/keyword-cannibalization-amazon-ppc-campaign-structure-2026, read 2026-11-09) "Cheapest click wins" runs against Amazon's "the match type with the highest bid will be used" (A9), within that sentence's scope. [seat]
- **Sermondo (Toby Fischer, undated):** "Amazon won’t put your bids against one another. Instead, they will choose only one of your keywords to enter in the auction", with no source; it warns that equal bids spread "clicks across all of your campaigns". [opinion] ("Amazon PPC Keyword Cannibalization: Am I Bidding Against Me?", https://sermondo.com/amazon-ppc-keyword-cannibalization/, read 2026-11-09)
- **FiveX (Lisa van Broekhoven, 2026-08-04):** "Every material search term needs one owner"; its branded-query example judges a bid cut by total SKU sales ("€5,940 versus €5,880"), not by the campaign's sales. [opinion] (FiveX, above)

Where they disagree: Ad Badger and Sermondo say the seller's own ads do not raise each other's price; Pare says an internal auction picks the cheapest click; Adbrew says Amazon picks the serving campaign and the exact bid stops setting the price. None of these pages reports a measured before-and-after of a query's account-wide rows after a negative or a harvest. [seat]

### Report contents, as practitioners see them

- **Nova (novadata docs, "checked against Nova's code on 2026-10-29", https://novadata.io/docs/advertising/search-terms-and-impression-share):** "Amazon lists a search mostly when it got at least one click". "Searches below Amazon's privacy threshold are grouped and show without the search text". Retention is about 65 days. Impression share is "only as of today, with no date and no history", over a rolling 30 days. [opinion] (Nova docs)
- **Nova news (Antoine, CEO at Nova Analytics, 2026-02-18, https://novadata.io/resources/news/amazon-term-level-bid-adjustments-sponsored-products-2026):** claims "individual bid adjustments per search term within exact-match keywords" in Sponsored Products, citing Amazon help page GYYZVM7LGSRYGWV5 as "Search Term Bid Adjustments". That page, opened today, is "Adjust Sponsored Products bids" (`lastModified` 2026-09-28): placement, audience and video adjustments; top of search is "Up to the first 5 positions … on desktop, and up to the first 4 positions on mobile"; the "up to a 900% increase (10x)" figure sits in its video section. It has no term-level bid. No v1 merged or SP 3.0 schema read has a search-term bid field. [opinion, unconfirmed against official]
- **WisePPC, 2026-07-30:** says click-only search-term text in "its advertising reports" began in mid-July 2026 and applied retroactively, naming an API field, not the console (A4). It also says Amazon's search-term report "stops at campaign, ad group and target" and cannot say "which ad served". [opinion]
- **Perpetua (Trina, 2021-01-18):** uses the impression share report to see relative volume, and sums impressions across ad groups. [opinion] ("How to Use the New Amazon Search Term Impression Rank Report", https://perpetua.io/blog-amazon-search-term-impression-share-rank-report/)
- **Ad Badger (Shazib Haseen, 2019-12-04):** SB broad can match synonyms while SP broad "never synonyms". This is contradicted by Amazon's current SP broad definition ("synonyms, and related terms", A8). [opinion, outdated] ("A Complete Overview of Sponsored Brand Search Term Reports", https://adbadger.com/?p=3336)
- **Ad Badger (The Badger, 2026-02-26):** describes a shift from single-keyword queries to conversational "Intent Cluster[s]" with Rufus, and "Semantic Search (matching meaning)". It gives no change to the search term report and no sourced figure; its claim that AI "will soon control 60% of Amazon’s product discovery" is unsourced. [opinion] (Ad Badger, "Why the 'Intent Cluster' is Replacing the 'Keyword' in the Age of Rufus", https://www.adbadger.com/blog/amazon-ppc-intent-clusters-vs-keywords-rufus/)
- **Rufus is now Alexa for Shopping; Alexa+ on devices keeps its own ad form.** Amazon's own page (2026-05-13): "Amazon brings together Rufus and Alexa+ to create ‘Alexa for Shopping’ on the Amazon Shopping app and website", "available to U.S. customers on the Amazon Shopping app and website, and Echo Show devices". [official] (Meet Alexa for Shopping, your personalized, agentic AI assistant on Amazon, https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant, `datePublished` 2026-05-13, read 2026-11-09) The Amazon Ads page of 2026-06-11 says the same for advertisers and keeps two surfaces apart: "Existing sponsored ads campaigns are automatically eligible to serve in Alexa for Shopping … without additional campaign setup", Sponsored Products and Sponsored Brands prompts "appear in shopping results and product pages, opening product-related conversations with Alexa for Shopping", and, separately, "On Alexa+, where customers can complete everyday tasks … right from their home, we have introduced Alexa+ Conversational Ads", for which "Advertisers with sponsored ads campaigns are automatically enrolled". [official] (What agentic shopping means for advertising, H1 "Agentic shopping is here. What does that mean for advertisers?", https://advertising.amazon.com/library/news/agentic-shopping-advertising, `datePublished` 2026-06-11, read 2026-11-09) Neither page says how these conversations appear in the search term report, or whether a campaign's negatives apply there. This replaces an earlier Tinuiti search-snippet lead; the settlement of the cross-file disagreement is in Verification, "Gap fill 2026-11-09".
- **Negative-keyword count caps:** Perpetua's limits page (Team Perpetua, 2026-02-12) lists "Campaign negative keywords 1,000" and "Ad group negative keywords 1,000" and links to Amazon's limits help; Karooya (Kirti, 2018-08-16) lists 10,000 each and "Negative Keywords in legacy Sponsored Brands Campaigns 1,000". Amazon's own page reads 10,000 each (C5), so Perpetua's figure is out of date against it. [opinion] (Perpetua help, "The campaigns, ad groups, target limits for each ad unit", https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit; Karooya, "Amazon Ads Negative Keyword Limits", https://www.karooya.com/blog/amazon-ads-negative-keywords-limits/; both read 2026-11-09)

## Published research

Everything here is [research], verified against OpenAlex, Crossref or arXiv metadata on 2026-11-09.

**R1. Amazon's own relevance classes.** Reddy et al., "Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search", arXiv 2206.06588 (2022; KDD Cup 2022). About 130k queries and 2.6M human judgements. The ESCI definitions:

- Exact: "satisfies all the query specifications";
- Substitute: "fails to fulfill some aspects of the query but it can be used as a functional substitute";
- Complement: "could be used in combination with an exact item";
- Irrelevant: "fails to fulfill a central aspect of the query", for example wheat bread for "gluten-free bread".

These match the auto targeting groups' names (close, loose, substitutes, complements). The paper does not say the ad system uses them. [research] (https://arxiv.org/abs/2206.06588)

**R2. Semantic matching beyond words.** Chang et al. (Amazon), "Extreme Multi-label Learning for Semantic Matching in Product Search", KDD 2021, doi 10.1145/3447548.3467092. Lexical matching "fail[s] to capture behavioral signals". The model matches queries to products over a catalogue of about 100M. It explains, at the level of mechanism, why broad and auto rows hold queries sharing no word with the keyword. [research]

**R3. Delayed conversions.** Chapelle, "Modeling delayed feedback in display advertising", KDD 2014, doi 10.1145/2623330.2623634. "Conversions can take place long after the impression -- up to a month". An unconverted example should be treated as uncertain, not negative, when "it is too early to tell". [research]

**R4. Sparse conversion data.** Lee, Orten, Dasdan & Li, "Estimating conversion rate in display advertising from past performance data", KDD 2012, doi 10.1145/2339530.2339651. The paper names "extreme data sparsity" and combines estimators along hierarchies of the data. [research]

**R5. Keyword conversion with position endogeneity.** Rutz, Bucklin & Sonnier, "A Latent Instrumental Variables Approach to Modeling Keyword Conversion in Paid Search Advertising", Journal of Marketing Research 2012, doi 10.1509/jmr.10.0354. Data: daily keyword-level paid search data (impressions, clicks, reservations) for a major lodging chain, on a general search engine, not Amazon.

- Keyword data are sparse, and position is endogenous.
- "They find that higher positions increase both the click-through and conversion rates. When advertisements are served in higher positions, approximately one-third of new conversions is due to increased click-through while approximately two-thirds are due to increased conversion rates."
- "The keyword list generated on the basis of their estimated conversion rates outperforms the status quo list as well as lists generated by observed conversion and click-through rates."

[research] (abstract re-read through OpenAlex, 2026-11-09)

**R5b. Position and conversion rate: four studies, three answers (gap fill 2026-11-09).** areas/bids-and-placements.md owns position effects; this file aligns with it.

| Study | Data and method | Conversion rate against position |
|---|---|---|
| Rutz, Bucklin & Sonnier, JMR 2012 | one lodging chain, daily keyword data; latent instrumental variables for endogenous position | "higher positions increase both the click-through and conversion rates" |
| Ghose & Yang, Management Science 2009, doi 10.1287/mnsc.1090.1054 | one retailer, several hundred Google keywords, six months; hierarchical Bayesian simultaneous equations | "conversion rates are highest at the top and decrease with rank"; "profits are often higher at the middle positions than at the top or the bottom ones" |
| Agarwal, Hosanagar & Smith, JMR 2011, doi 10.1509/jmr.08.0468 | one online retailer, several keywords; field experiment; hierarchical Bayesian model | "while click-through rate decreases with position, conversion rate increases with position and is even higher for more specific keywords" (position counts down the page, so conversion rises lower down); "the topmost position is not necessarily the revenue-or profit-maximizing position" |
| Narayanan & Kalyanam, Marketing Science 2015, doi 10.1287/mksc.2014.0893 | a focal advertiser and its major competitors, daily; regression discontinuity at auction rank boundaries | "A simple mean comparison of outcomes at two positions is likely to be biased due to these selection issues"; experiments are hard because of "competitors’ bidding behavior, which induces selection biases that cannot be eliminated by randomizing the bids for the focal advertiser"; RD effects on click-through and sales orders "are much smaller, and exist only in some of the positions"; weaker "when the keyword phrase has specific brand or product information, when the ad copy is more specific as in exact matching options" |

[research] (all four abstracts read through OpenAlex, 2026-11-09)

The three conversion findings come from three advertisers, three periods and three methods, all on general web search engines, none on Amazon. Narayanan & Kalyanam's point bears on all of them: when an auction sets position, an estimated position effect carries the selection of who wins which slot, and their selection-robust estimates are smaller and patchy. For a search term on Amazon, none of the four fixes a sign for how a term's conversion rate moves with its slot. [seat]

**R6. Hierarchical Bayesian keyword models.** Ghose & Yang, "An Empirical Analysis of Search Engine Advertising: Sponsored Search in Electronic Markets", Management Science 2009, doi 10.1287/mnsc.1090.1054. Six-month panel of several hundred keywords of a nationwide retailer advertising on Google; hierarchical Bayesian estimation across keywords; "conversion rates are highest at the top and decrease with rank". [research]

**R7. Generic to branded spillover.** Rutz & Bucklin, "From Generic to Branded: A Model of Spillover in Paid Search Advertising", JMR 2011, doi 10.1509/jmkr.48.1.87. Generic search spills over to later branded search, asymmetrically. A generic term with few direct orders may still feed branded orders. [research]

**R8. Heavy clickers.** Yao & Mela, "A Dynamic Model of Sponsored Search Advertising", Marketing Science 2011. About 10% of consumers do 90% of clicks. [research]

**R9. Brand-keyword ads may buy nothing.** Blake, Nosko & Tadelis, "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment", Econometrica 2015, doi 10.3982/ECTA12423 (eBay). "Brand keyword ads have no measurable short-term benefits". For non-brand terms, frequent users "account for most of the advertising expenses, resulting in average returns that are negative." [research] Ad-attributed orders on a term are not incremental orders; that question is areas/ads-organic-and-total.md's.

**R10. Zero numerators.** Hanley & Lippman-Hand, "If nothing goes wrong, is everything all right? Interpreting zero numerators", JAMA 1983;249(13):1743–5, PMID 6827763 (abstract not shown on PubMed). The "rule of three": with zero events in n trials, the 95% upper bound on the rate is about 3/n, from (1−p)^n = 0.05. [research] (Wikipedia, "Rule of three (statistics)", https://en.wikipedia.org/wiki/Rule_of_three_(statistics), read 2026-11-09)

**R11. Empirical Bayes.** Casella, "An Introduction to Empirical Bayes Data Analysis", The American Statistician 1985, doi 10.1080/00031305.1985.10479400. Shrinks each unit's estimate toward a group estimate learned from the data. [research]

**R12. Many tests at once.** Benjamini & Hochberg, "Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing", JRSS-B 1995, doi 10.1111/j.2517-6161.1995.tb02031.x. The paper addresses the multiple-testing problem (a per-test cut-off applied to many tests yields false positives that grow with the number tested) and proposes controlling the expected share of false discoveries instead. [research; the application to search terms is the seat's]

**R13. Ads at the top of Amazon results.** Rock, Strauss, O'Reilly & Mazzucato, "Behind the clicks: Can Amazon allocate user attention as it pleases?", Information Economics and Policy 2024, doi 10.1016/j.infoecopol.2024.101115. On 2023 Amazon search-result data: "Among the top five search results, where typically four are advertisements, we find that neither decreased relevancy nor increased price significantly sways user decisions", read as users who "satisfice". [research]

**Seat arithmetic (not research, not a position).** [seat]

- If a term's true conversion rate is p, the chance of zero orders in n independent clicks is (1−p)^n.
  - At p = 10%: n = 10 gives about 35%, n = 20 about 12%, n = 30 about 4%.
  - At p = 5%: n = 20 gives about 36%, n = 34 about 17%, n = 60 about 5%.
- Expected clicks per order are 1/p.
- With zero orders in n clicks, the rule of three bounds p below about 3/n at 95% (20 clicks: under 15%; 34 clicks: under 9%).
- A Beta(a, b) prior on p, set from the ad group's or account's rate, updates to Beta(a, b + n) after n clicks and no orders, with posterior mean a/(a+b+n). This shrinks a new term toward its group instead of to zero.
- Clicks counted inside the attribution window, or within restatement reach, are not yet n.
- A practitioner's fixed click bar is one point on the (1−p)^n curve for the conversion rate the practitioner had in mind.

## Stable enough for a skill

Each item is a definition or a documented mechanism that several Amazon pages state alike, or that an API model fixes. Figures stay out; they are read at run time.

1. **The API search term report holds only terms with at least one click.** The help page and the bulksheet page say the console and bulksheet report do too. (Search term reports [v3]; Sponsored ads reporting FAQ (version 3); Search term report for Sponsored Products; Search term reports in bulksheets; Best practices for your Sponsored Products ads)
2. **One query can appear on several rows,** one per campaign, ad group and keyword or target that matched it. Its totals are sums across rows. (Search term reports [v3]; Reporting columns (version 3))
3. **A `*` search term is a detail-page placement with no query.** A 10-character ASIN-shaped search term (lower case in Amazon's example) is the detail page the ad appeared on. Such rows appear only for auto ad groups and product-targeting ad groups. (Search term reports [v3]; Search term reports in bulksheets; A guide to targeting with Sponsored Products)
4. **Some terms are inferred by Amazon, not typed,** in non-search contexts, including off-Amazon placements. No field read marks them. (Search term report for Sponsored Products; Understand keyword match types)
5. **Broad, phrase and exact all take close variants:** plurals, misspellings, acronyms, translations, and for exact reordered forms. Broad may match queries without the keyword's words. (Understand keyword match types; What is Keyword Targeting?)
6. **Negative keywords act on shopping-results queries. Negative ASINs and brands act on detail pages.** Negative product targets affect only product-attribute and auto targets in their scope. (Add negative keywords or negative products targeting; All releases, May 22, 2025; Sponsored Products negative product and brand targeting overview)
7. **A campaign-level negative applies to every ad group in the campaign. An ad-group-level one applies to that ad group.** Sponsored Brands has no campaign-level negatives, per the SB API guide and the exports page (the general keyword guide speaks of "campaign or ad group level" without separating SB). (Negative keyword targeting [SP]; Sponsored Brands negative keyword targeting; Exports: Target; What is Keyword Targeting?)
8. **Negative phrase and negative exact both block close variants.** Negative phrase blocks any query containing the phrase; negative exact blocks the query itself. The match type of an existing negative cannot be changed. (Add negative keywords or negative products targeting)
9. **Negatives take a buffer period to act.** The figure is read from the help page. (Add negative keywords or negative products targeting)
10. **In v1 a negative is a target with `negative: true`,** written by `POST /adsApi/v1/create/targets` and read by `POST /adsApi/v1/query/targets` with `negativeFilter`. Its level is `targetLevel` `CAMPAIGN` or `AD_GROUP`. The reply is `207`, per item. (Negative keyword targeting [SP]; Amazon Ads API v1 merged OpenAPI)
11. **A negative ASIN is a `PRODUCT` target with `PRODUCT_EXACT`. A negative brand is a `PRODUCT_CATEGORY` target refined by brand id.** Brand ids come from the brand recommendation and brand search operations. (Sponsored Products negative product and brand targeting overview; Sponsored Products 3.0 OpenAPI)
12. **Clicks can be invalidated after the fact and conversions restate.** A term's latest days are incomplete; restatement reaches past the attribution window. (Sponsored ads reporting FAQ (version 3); Amazon Ads reporting overview; Traffic validation)
13. **v1 conversion metrics follow the account's default window,** on traffic date, with Promoted and Halo forms. v3 carries explicit 1/7/14/30-day columns. (Overview of the Reporting v1 API; Search term reports [v3])
14. **Search-term impression share and rank are account-wide per query.** They cannot be split by campaign, ad group or target. (Impression share metrics [search]; Search term impression share report for Sponsored Products)
15. **v3 reporting stops on 2027-06-30, and the console's legacy Sponsored Ads reports close by 2026-12-31.** SB v2 search-term impression share and rank stop returning values on 2026-11-10. (Deprecations; Streamline campaign analysis with unified reporting)
16. **Target Promotion is Amazon's documented harvest mechanism in the API.** No page read says it negates in the source. (Target Promotion)
17. **Amazon's own numeric guidance on negation is a recommendation, not a rule:** a click count before judging, and a period after adding. The figures are read from the guide. (A guide to targeting with Sponsored Products)
18. **With zero orders in n clicks, the 95% upper bound on the conversion rate is about 3/n.** The chance of zero orders at rate p is (1−p)^n. (Hanley & Lippman-Hand 1983; Rule of three (statistics))
19. **Unconverted recent clicks are uncertain, not negative.** Delayed-feedback models treat them that way. (Chapelle 2014)
20. **Amazon publishes account caps on negatives per campaign, per ad group and per ad group for negative products, separate from the API's 1000-item batch size;** the figures are read from the help page. (Sponsored ads campaign limits; Amazon Ads API v1 merged OpenAPI)
21. **The auto targeting groups split by surface:** close and loose match serve on search terms, substitutes and complements on detail pages. (Understand keyword match types; Exports enums)
22. **Negatives exist at two levels only, ad group and campaign; no account-, brand- or portfolio-level negative or shared negative list is in the v1 models, the SP/SB/SD 3.0 models, the portfolio help page or the bulksheet portfolio tab.** A portfolio carries a budget cap. (Amazon Ads API v1 merged OpenAPI, `TargetLevel`; Sponsored Products 3.0 OpenAPI; Sponsored Brands 3.0 YAML; Sponsored Display 3.0 YAML; Portfolio budgets; Use portfolios with bulksheets)
23. **Each bulksheet negative row names its Campaign ID (and Ad group ID for ad-group negatives); a row with a blank Operation is ignored.** (How to create Sponsored Products campaigns in bulksheets; Bulksheets FAQs)
24. **Per-product negative paths:** SP `/sp/negativeKeywords`, `/sp/campaignNegativeKeywords`, `/sp/negativeTargets`, `/sp/campaignNegativeTargets`; SB `/sb/negativeKeywords` and `/sb/negativeTargets` on the SB 3.0 YAML; SD `/sd/negativeTargets`; each with its own reply shape. SB negatives take `negativeExact` and `negativePhrase` only; SD has no negative keyword path. (Sponsored Products 3.0 OpenAPI; Sponsored Brands 3.0 YAML; Sponsored Display 3.0 YAML; Sponsored Display contextual targeting guide)
25. **`/sb/negativeTargets/brands/recommendations` is on the JSON model titled "Sponsored Brands 3.0" and on the SB 4.0 model; `/sb/negativeKeywords` is on the SB 3.0 YAML only.** (the three SB models)
26. **Amazon attributes a conversion to no more than one ad interaction across all campaigns and advertisers.** A sale a harvested keyword reports is a sale no other campaign of the seller's reports. (Ad campaign attribution)
27. **The v1 Dimensions library's target fields are `adGroupTarget.id`, `targeting.value` and `targetingMatchType.value`; `target.value` appears only in migration examples and in a `PENDING_DEPRECATION` warning example.** (Target, Targeting and Targeting match type dimension pages; Migrating from: spSearchTerm; New features [Reporting v1])
28. **Rufus was merged into Alexa for Shopping (US, May 2026), where existing sponsored ads campaigns are automatically eligible; Alexa+ on Alexa-enabled devices carries Alexa+ Conversational Ads with automatic enrolment.** (Meet Alexa for Shopping…; What agentic shopping means for advertising)

## What cx must read at run time

Each item is a read through the cx door (`cx raw amazon-ads`), or a file the seller places in the tree. The skill holds the operation, never the figure. Every figure in this file marked *(figure)* is for human readers only.

**Reports.**

- **v1 search-term report:** `POST /adsApi/v1/create/reports` with `searchTerm.value`, the target fields and the metric fields. Then `POST /adsApi/v1/retrieve/reports` until done, reading any `warnings` (`PENDING_DEPRECATION`, `NO_PERMISSION`, `DATE_LIMITED`). The Dimensions library's target fields are `adGroupTarget.id`, `targeting.value` and `targetingMatchType.value`; the migration page's `target.value`/`target.matchType` is the other spelling Amazon prints, flagged `PENDING_DEPRECATION` in the New features example. Whether the service accepts either, and with which warning, is in its reply. [seat]
  - **The query across the account:** the same report with `searchTerm.value` and no campaign, ad group or target field, which the helpful-concepts page says aggregates over the dimensions left out; or the per-row report summed by `searchTerm.value`. Each row also carries its campaign and target, so the rows a negative removed and the rows that kept serving the query are both in it. [seat]
  - Max range and retention come from the Dates page or from the error the service returns. The same goes for whether `advertisedProduct.id` combines with `searchTerm.value`.
  - Lifecycle is method/reporting.md's.
- **v3 search-term report**, while it lives: `POST /reporting/reports` with `reportTypeId` `spSearchTerm` or `sbSearchTerm`, then `GET /reporting/reports/{reportId}`. The current maximum range, retention and stop date come from the report-type page and the deprecation page at run time.
- **v1 impression share:** `metric.impressionShare` and `metric.impressionShareRank` with `adProduct.value`, `advertiserAccount.id` and `searchTerm.value` only.

**Entities.**

- **The source's entities:** `POST /adsApi/v1/query/targets` with the required `adProductFilter`, filtered by `adGroupIdFilter` or `campaignIdFilter`. Read with `negativeFilter` `include: [true]` for the negatives already present and `[false]` for the positives, with `targetTypeFilter`, `matchTypeFilter` and `stateFilter`. This shows whether a harvested term already exists as a positive anywhere, and whether a negative already covers it.
- **The campaign's targeting type** (auto or manual) and the account type (seller or vendor), to know whether a campaign-level negative product target is accepted. The write's own `207` reply is the final word (C6).
- **Brand ids for a brand negative:** `GET /sp/negativeTargets/brands/recommendations` or `POST /sp/negativeTargets/brands/search`; for SB, `GET /sb/negativeTargets/brands/recommendations` (SB 4.0 and the JSON "Sponsored Brands 3.0" model).
- **Existing negatives per product, v3:** `POST /sp/negativeKeywords/list`, `POST /sp/campaignNegativeKeywords/list`, `POST /sp/negativeTargets/list`, `POST /sp/campaignNegativeTargets/list`; `GET /sb/negativeKeywords` with `adGroupIdFilter`/`campaignIdFilter`; `POST /sb/negativeTargets/list`; `GET /sd/negativeTargets` or `/sd/negativeTargets/extended`.
- **The product group's campaigns:** which campaigns and ad groups advertise the ASINs a negative is meant for, from the ad and ad-group entities (`POST /adsApi/v1/query/ads`, `POST /adsApi/v1/query/adGroups`); no Amazon object holds a product group's negative list (C8).
- **SP-API, through `cx-amazon-sp-api`:** the `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` for the ASIN, with `reportPeriod` `WEEK`, `MONTH` or `QUARTER` (a request cannot span periods), read as `searchQueryData.searchQuery` with `impressionData.asinImpressionCount`, `clickData.asinClickCount`, `cartAddData.asinCartAddCount` and `purchaseData.asinPurchaseCount` against the query's totals; available to brand-registered sellers with the Brand Analytics role.

**Writes.** Each write is the seller's (decision D233); its reply is read item by item. A write is the same as any other change through the door, and the gate's rules for a POST apply.

- **Harvest write:** `POST /adsApi/v1/create/targets` with `negative: false`, a keyword or product target in the destination ad group, and the bid from areas/bids-and-placements.md's reasoning.
- **Negative write:** `POST /adsApi/v1/create/targets` with `negative: true` and `campaignId` (campaign level) or `adGroupId` (ad-group level).
- **Per-product negative writes (the v3 paths of C9):** SP `POST /sp/negativeKeywords` or `/sp/campaignNegativeKeywords` (`matchType` `NEGATIVE_EXACT`, `NEGATIVE_PHRASE`, `NEGATIVE_BROAD`; request and reply media type `application/vnd.spNegativeKeyword.v3+json` or `application/vnd.spCampaignNegativeKeyword.v3+json`), `POST /sp/negativeTargets` or `/sp/campaignNegativeTargets`; SB `POST /sb/negativeKeywords` (`negativeExact`, `negativePhrase`; up to 100 per call *(figure)*) and `POST /sb/negativeTargets`; SD `POST /sd/negativeTargets` (up to 100 *(figure)*). Each reply is read item by item: SP `success[]`/`error[]` by `index`; SB keywords an array in request order; SB targets `createTargetSuccessResults[]`/`createTargetErrorResults[]` by `targetRequestIndex`; SD an array of `code`/`targetId`.
- **A negative for many campaigns** is one write per campaign (or per ad group in SB and SD), batched up to each path's per-request size; each campaign's own reply says whether it landed.

**Figures and timing.**

- **The buffer period for a negative to act, and Amazon's click and duration guidance:** the help page (G8W49VU65XQ4T2NS) and the targeting guide.
- **Freshness:** the restatement schedule and the "wait at least N days" lines from the reporting FAQ and overview; they say which days of a pull are still subject to change.
- **Limits:** keyword character and word limits from the limits page ("Keyword character constraints"); the per-campaign and per-ad-group negative caps from "Sponsored ads campaign limits" (G86H2227323T8T4Q). A write over a limit is refused item by item in the `207` reply.

**The seller's own numbers.**

- The ad group's or account's conversion rate and the seller's target ACoS or CPA. They come from the seller's reports and goals (beyond/goals-and-economics.md). Practitioner thresholds and the (1−p)^n arithmetic are stated in terms of them. [seat]
- **A downloaded console or unified-reporting file**, when the seller places one in the tree: its header row. Column names changed (B10), and the bulksheet tab inverts two definitions (B11).

## Pages read

All read 2026-11-09. Type: official (Amazon), opinion (practitioner, vendor, trade press), research, reference.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Search term reports [v3] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term | official | 2026-11-09 | Clicked-only rule, `*` rows, SP/SB config, column lists, SB preview |
| Sponsored ads reporting FAQ (version 3) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/faq | official | 2026-11-09 | Console vs API, freshness, restatement 1/7/28 days, 42-day example, pull cadence |
| Reporting columns (version 3) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/columns | official | 2026-11-09 | searchTerm, keyword, targeting, matchType, keywordType, topOfSearchImpressionShare |
| Targeting reports [v3] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/targeting | official | 2026-11-09 | Retention per ad product; THEME keywordType for SB |
| Prompt Ad Extension reports | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/prompt-ad-extension | official | 2026-11-09 | Prompts with clicks in existing reports; prompt report range |
| Amazon Ads reporting overview | https://advertising.amazon.com/API/docs/en-us/guides/reporting/overview | official | 2026-11-09 | Wait 5 days for clicks; conversions change up to 60 days; Stream v2 backfill |
| Overview of the Reporting v1 API | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/overview | official | 2026-11-09 | Traffic-date attribution, default windows, Promoted/Halo, concurrency note |
| Dates and historical data retention [v1] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dates | official | 2026-11-09 | Retention and max range by time dimension; campaign timezone |
| Limits and best practices [Reporting v1] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/limits | official | 2026-11-09 | Per-client-ID limits; too-large reports |
| New features [Reporting v1] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/new-features | official | 2026-11-09 | Warnings array |
| Migrating from: spSearchTerm | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/report-types/sp-search-term | official | 2026-11-09 | v1 field list for search terms (`target.value`) |
| Migrating from: spTargeting | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/report-types/sp-targeting | official | 2026-11-09 | v1 targeting field names |
| Search term (Targeting) dimension | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/targeting/search-term | official | 2026-11-09 | `searchTerm.value`, SP and SB |
| Matched target (Targeting) dimension | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/targeting/matched-target | official | 2026-11-09 | Sponsored Display only |
| Target / Targeting / Targeting match type dimensions | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/targeting/ | official | 2026-11-09 | `adGroupTarget.*`, `targeting.value`, `targetingMatchType.value` |
| Advertised product (Product) dimension | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/product/advertised-product | official | 2026-11-09 | `advertisedProduct.id` needs marketplace |
| Impression share metrics [search] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/metrics/impression-share/search | official | 2026-11-09 | Account-wide share and rank; incompatibilities |
| All releases | https://advertising.amazon.com/API/docs/en-us/release-notes/index | official | 2026-11-09 | Entries 2024-04-23, 2024-09-05, 2025-05-22, 2026-02-18, 2026-06-08, 2026-09-09, 2026-09-30, 2026-10-05 |
| Deprecations | https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations | official | 2026-11-09 | v3 stop 2027-06-30; SB v2 share stop 2026-11-10 |
| Limits, constraints, and quotas | https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits | official | 2026-11-09 | Keyword character constraints; P99 data availability; bid ranges |
| Negative keyword targeting [SP] | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/negative-targeting/keywords | official | 2026-11-09 | Campaign vs ad-group, v1 create, 207 reply |
| Sponsored Products negative product and brand targeting overview | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/negative-targeting/product-brand | official | 2026-11-09 | ASIN/brand shapes; vendor-only warning |
| Sponsored Products auto targeting | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/auto-targeting | official | 2026-11-09 | Theme targets; create-vs-query example error |
| Target Promotion (SP API guide) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/target-promotion | official | 2026-11-09 | Amazon's harvest mechanism; what the create call builds |
| Get started with auto campaigns | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/get-started/auto-campaigns | official | 2026-11-09 | Negatives at campaign and ad-group level; auto target ids via query/targets |
| Sponsored Brands negative keyword targeting | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/targeting/negative-keyword-targeting | official | 2026-11-09 | No campaign-level negatives in SB |
| Sponsored Brands negative product targeting | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/targeting/negative-product-targeting | official | 2026-11-09 | asinSameAs / asinBrandSameAs |
| Targets (campaign management entity guide) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/target | official | 2026-11-09 | v1 target entity across ad products |
| Campaign management overview / example payloads | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/example-payloads | official | 2026-11-09 | v1 payload shapes |
| Target (Exports targets model overview) | https://advertising.amazon.com/API/docs/en-us/guides/exports/entities/targets | official | 2026-11-09 | Negative support per type; campaign level SP only |
| Exports enums | https://advertising.amazon.com/API/docs/en-us/guides/exports/entities/enums | official | 2026-11-09 | Match type definitions; auto expression mapping |
| Search term reports in bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-search-term-report | official | 2026-11-09 | 7-day lookback, ids, ASIN rows, inverted definitions |
| How to create Sponsored Products campaigns in bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/create-sp-campaign | official | 2026-11-09 | Negative entity fields, negativeExact/negativePhrase |
| How to update Sponsored Products campaigns | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/update-sp-campaigns | official | 2026-11-09 | Update rows (no claim cited) |
| Sponsored Products: Targeting types & entities | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-entities/sp-entities | official | 2026-11-09 | Entity list (no claim cited) |
| Amazon Marketing Stream v2 overview | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/overview | official | 2026-11-09 | Stream v2 datasets |
| Sponsored ads traffic [AMC] | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/datasources/sponsored_ads_traffic | official | 2026-11-09 | Impression-level customer_search_term |
| Data aggregation thresholds in AMC | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/aggregation-threshold | official | 2026-11-09 | LOW threshold of 2 users |
| Overview [MCP] | https://advertising.amazon.com/API/docs/en-us/mcp/mcp-overview | official | 2026-11-09 | Tools and skills; AMC SQL generator |
| MCP reporting skill page | https://advertising.amazon.com/API/docs/en-us/mcp/skills/skills-library/reporting | official | 2026-11-09 | Reporting skill exists |
| MCP campaign management tool definitions | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/campaign_management.json | official | 2026-11-09 | 32 tools, none for harvest or negatives |
| Sponsored Products 3.0 OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official | 2026-11-09 | Negative paths, enums, brand operations, target promotion, keyword rec share |
| Sponsored Brands 3.0 OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | official | 2026-11-09 | SB paths present |
| Amazon Ads API v1 merged OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official | 2026-11-09 | TargetCreate, QueryTargetRequest, match type enums, batch sizes |
| Docs contract index | https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json | official | 2026-11-09 | Model URLs |
| Search term report for Sponsored Products | https://advertising.amazon.com/help/G3HEFZYWZF84NPS9 | official | 2026-11-09 | Console columns, inferred terms, 65-day lookback, clicked-only |
| Targeting report for Sponsored Products | https://advertising.amazon.com/help/GPDYPV4AAYCAJFKP | official | 2026-11-09 | At least 1 impression; 90-day lookback |
| Understand keyword match types | https://advertising.amazon.com/help/GHTRFDZRJPW6764R | official | 2026-11-09 | Close variants, inferred terms, highest-bid rule, negative limits |
| Add negative keywords or negative products targeting | https://advertising.amazon.com/help/G8W49VU65XQ4T2NS | official | 2026-11-09 | Negative scope, limits, buffer periods (served as node GTEHPEG5BXY9UX5W, lastModified 2026-10-20) |
| Sponsored ads campaign limits | https://advertising.amazon.com/help/G86H2227323T8T4Q | official | 2026-11-09 | Negatives per campaign / ad group 10,000; negative products per ad group 10,000 |
| Traffic validation | https://advertising.amazon.com/help/GBYPYH79NGJJ5JPS | official | 2026-11-09 | 30-day IVT monitoring; IVR signals |
| Brand impression share | https://advertising.amazon.com/help/GNU4AUAUHS76DNDR | official | 2026-11-09 | Brand-term top-of-search share |
| Adjust Sponsored Products bids | https://advertising.amazon.com/help/GYYZVM7LGSRYGWV5 | official | 2026-11-09 | No term-level bid (checks Nova's claim) |
| A guide to targeting with Sponsored Products | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official | 2026-11-09 | Two weeks auto; 20 clicks; two weeks after negatives; ASIN shape |
| Best practices for your Sponsored Products ads | https://advertising.amazon.com/library/guides/sponsored-products-best-practices | official | 2026-11-09 | Harvest to exact, raise bid |
| What is Keyword Targeting? | https://advertising.amazon.com/library/guides/keyword-targeting | official | 2026-11-09 | Auto reads product details; SB semantic; negatives incl. broad |
| How to start and improve your keyword strategy | https://advertising.amazon.com/blog/how-to-start-and-improve-your-keyword-strategy | official | 2026-11-09 | High performers to exact; "cheap" negative |
| Amazon Ads FAQ | https://advertising.amazon.com/resources/faq | official | 2026-11-09 | Definition of negative matches |
| Your complete guide to Sponsored Brands | https://advertising.amazon.com/library/guides/sponsored-brands-what-to-know | official | 2026-11-09 | SB search term report use |
| Search term impression share report for Sponsored Products | https://advertising.amazon.com/resources/whats-new/search-term-impression-report-sponsored-products | official | 2026-11-09 | Account-wide share per term |
| Introducing the search term impression rank report | https://advertising.amazon.com/resources/whats-new/search-term-rank-report | official | 2026-11-09 | SB rank report, 2020-10-30 |
| Sponsored Products prompts and Sponsored Brands prompts | https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts | official | 2026-11-09 | Prompts use campaign targeting; CPC billing at GA |
| Streamline campaign analysis with unified reporting, now generally available | https://advertising.amazon.com/resources/whats-new/streamline-campaign-analysis-with-unified-reporting | official | 2026-11-09 | GA, history, sunset 2026-12-31 |
| unBoxed 2026 news: Explore the latest advertising announcements | https://advertising.amazon.com/library/news/unboxed-2026-news-announcements | official | 2026-11-09 | Amazon Ads Agent name; no search-term news |
| At Accelerate 2026, Amazon shares new AI tools as a force multiplier for independent sellers | https://sellingpartners.aboutamazon.com/accelerate-2026-recap | official | 2026-11-09 | Seller Assistant auto-optimization adds and pauses search terms |
| Meet Alexa for Shopping, your personalized, agentic AI assistant on Amazon | https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant | official | 2026-11-09 | Rufus folded into Alexa for Shopping, 2026-05-13 |
| Ad Intel: 5 common sponsored ads campaign mistakes (and how to fix them) | https://advertising.amazon.com/library/expert-advice/common-sponsored-ads-mistakes-and-solutions | opinion (Amazon-hosted) | 2026-11-09 | Migrate terms to tighter match; CTR signal |
| Search Query Performance report schema | https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchQueryPerformanceReport.json | official | 2026-11-09 | SQP fields and periods |
| Amazon PPC Negative Keywords: Cut Wasted Ad Spend (2026) (Ad Badger) | https://www.adbadger.com/blog/amazon-ppc-education/negative-keywords-amazon-ppc/ | opinion | 2026-11-09 | 2,500/0.18%, $35, 34 clicks |
| The Easiest Way to Automate Negative Keywords for Amazon Ad Campaigns (Ad Badger) | https://www.adbadger.com/blog/amazon-ppc-education/automate-negative-keywords/ | opinion | 2026-11-09 | Nightly Hunt rules; Quick Attack 48h-delay option |
| How many clicks before you kill a keyword (Ad Badger) | https://www.adbadger.com/blog/amazon-ppc-education/how-many-clicks-before-you-kill-a-keyword-cps-rule-the-ppc-den-podcast/ | opinion | 2026-11-09 | Branded vs competitor clicks per sale |
| Sponsored Brand search term reports (Ad Badger) | https://adbadger.com/?p=3336 | opinion | 2026-11-09 | SB report use; outdated broad claim |
| Why the 'Intent Cluster' is Replacing the 'Keyword' in the Age of Rufus (Ad Badger) | https://www.adbadger.com/blog/amazon-ppc-intent-clusters-vs-keywords-rufus/ | opinion | 2026-11-09 | Conversational intent; no sourced figures |
| Negative word rule (Scale Insights) | https://docs.scaleinsights.com/docs/what-is-the-negative-word-rule | opinion | 2026-11-09 | Word-level negation, 25 clicks, 60 days |
| Amazon negative keywords (Scale Insights) | https://scaleinsights.com/learn/amazon-negative-keyword | opinion | 2026-11-09 | Phrase word order examples |
| Prestozon’s Rules Engine and Why It Changes the Game (Helium 10) | https://www.helium10.com/blog/amazon-ppc-keyword-management-rules/ | opinion | 2026-11-09 | AOV/CVR-based negation; isolation |
| Reclaim 20+ Hours Per Week: Automated Amazon PPC (Helium 10, Lauren Stair) | https://www.helium10.com/blog/reclaim-20-hours-per-week-how-to-automate-amazon-ppc-management/ | opinion | 2026-11-09 | Two orders, ACoS under 30% example |
| Negative exact match strategy (Perpetua) | https://help.perpetua.io/en/articles/6027156-negative-exact-match-strategy | opinion | 2026-11-09 | Clicks > X, conversions < Y |
| The campaigns, ad groups, target limits for each ad unit (Perpetua) | https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit | opinion | 2026-11-09 | 1,000 negative caps (out of date against Amazon's page) |
| Amazon Ads Negative Keyword Limits (Karooya) | https://www.karooya.com/blog/amazon-ads-negative-keywords-limits/ | opinion | 2026-11-09 | 10,000 negative caps (2018) |
| Curbing spend on irrelevant search terms (Perpetua) | https://perpetua.io/blog-curbing-spend-on-irrelevant-search-terms/ | opinion | 2026-11-09 | NLP tokens, 98% claim |
| Search term impression rank report (Perpetua) | https://perpetua.io/blog-amazon-search-term-impression-share-rank-report/ | opinion | 2026-11-09 | Using share and rank |
| Explained: What is keyword harvesting on Amazon? (Intentwise) | https://www.intentwise.com/blog/what-is-keyword-harvesting | opinion | 2026-11-09 | Definition |
| Search term isolation and profit control (FiveX) | https://fivex.com/blog/amazon-search-term-isolation-profit-control/ | opinion | 2026-11-09 | One owner per query; thresholds |
| Negative keyword strategy (Canopy) | https://canopymanagement.com/?p=23024 | opinion | 2026-11-09 | Price-scaled thresholds |
| Keyword harvesting funnel (Adbrew) | https://adbrew.io/blog/amazon-ppc-how-to-automate-a-keyword-harvesting-funnel | opinion | 2026-11-09 | Rule A/B; source negatives; inferred terms |
| Million dollar case study (Jungle Scout) | https://www.junglescout.com/blog/million-dollar-case-study-optimizing-ppc-campaigns/ | opinion | 2026-11-09 | 10-click rule |
| Keyword harvesting framework (Seller Labs) | https://www.sellerlabs.com/knowledge-base/keyword-harvesting-framework-turning-auto-campaign-data-into-profitable-manual-amazon-ppc/ | opinion | 2026-11-09 | 7–14 days, 20–30 clicks, negative exact in auto |
| The 5 W's of negative keywords (JumpFly) | https://www.jumpfly.com/blog/the-5-ws-and-1-h-of-amazon-ads-negative-keywords/ | opinion | 2026-11-09 | Phrase word-order claim |
| Search terms and impression share (Nova docs) | https://novadata.io/docs/advertising/search-terms-and-impression-share | opinion | 2026-11-09 | Clicked-only, privacy grouping, share as of today |
| Term-level bid adjustments (Nova news) | https://novadata.io/resources/news/amazon-term-level-bid-adjustments-sponsored-products-2026 | opinion | 2026-11-09 | Unconfirmed term-level bid claim |
| WisePPC new analytics suite 2026 | https://wiseppc.com/blog/wiseppc-new-analytics-suite-2026/ | opinion | 2026-11-09 | Mid-July 2026 clicked-only change claim |
| Amazon Ads unified reporting exits beta - and takes two old tools with it (PPC Land) | https://ppc.land/amazon-ads-unified-reporting-exits-beta-and-takes-two-old-tools-with-it/ | opinion (trade press) | 2026-11-09 | Unified Search Term template is clicked-only |
| Shopping Queries Dataset (ESCI) | https://arxiv.org/abs/2206.06588 | research | 2026-11-09 | ESCI definitions |
| Chang et al. 2021 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1145/3447548.3467092 | research | 2026-11-09 | Semantic matching |
| Chapelle 2014 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1145/2623330.2623634 | research | 2026-11-09 | Delayed feedback |
| Lee et al. 2012 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1145/2339530.2339651 | research | 2026-11-09 | Sparse conversion estimation |
| Rutz, Bucklin & Sonnier 2012 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1509/jmr.10.0354 | research | 2026-11-09 | Keyword conversion, position endogeneity |
| Rutz & Bucklin 2011 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1509/jmkr.48.1.87 | research | 2026-11-09 | Generic-to-branded spillover |
| Ghose & Yang 2009 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1287/mnsc.1090.1054 | research | 2026-11-09 | Hierarchical Bayesian keyword model |
| Yao & Mela 2011 (OpenAlex search) | https://api.openalex.org/works?search=dynamic%20model%20sponsored%20search%20advertising | research | 2026-11-09 | Heavy clickers |
| Blake, Nosko & Tadelis 2015 (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.3982/ECTA12423 | research | 2026-11-09 | Brand-keyword ads, eBay experiment |
| Hanley & Lippman-Hand 1983 (PubMed E-utilities) | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=6827763&retmode=text&rettype=abstract | research | 2026-11-09 | Citation; no abstract |
| Rule of three (statistics) | https://en.wikipedia.org/wiki/Rule_of_three_(statistics) | reference | 2026-11-09 | 3/n bound derivation |
| Benjamini & Hochberg 1995 (Crossref record) | https://api.crossref.org/works/10.1111/j.2517-6161.1995.tb02031.x | research | 2026-11-09 | FDR |
| Casella 1985 (Crossref record) | https://api.crossref.org/works/10.1080/00031305.1985.10479400 | research | 2026-11-09 | Empirical Bayes |
| Rock et al. 2024, "Behind the clicks" (OpenAlex record) | https://api.openalex.org/works/https://doi.org/10.1016/j.infoecopol.2024.101115 | research | 2026-11-09 | Ads at top of Amazon results |
| **Gap fill 2026-11-09** | | | | |
| Sponsored Brands 3.0 (YAML model, "Amazon Ads API - Sponsored Brands 3.0") | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | official | 2026-11-09 | `/sb/negativeKeywords` and `/sb/negativeTargets` paths, bodies, enums, 207/200 shapes, 100-item batches, archive rule |
| Sponsored Brands campaign management 4.0 (JSON model) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | official | 2026-11-09 | Only negative path is brand recommendations |
| Sponsored Brands 3.0 (JSON model, re-read) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | official | 2026-11-09 | v4 path set plus two recommendation paths; brand recommendations text and marketplaces |
| Sponsored Display 3.0 (YAML model) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml | official | 2026-11-09 | `/sd/negativeTargets` operations, body, 207 shape, 100 per call |
| Sponsored Products 3.0 OpenAPI (re-read) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official | 2026-11-09 | Eight negative paths, media types, required fields, 207 wrappers, `Prefer` header |
| v1 merged OpenAPI incl. beta | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p_ALL.json | official | 2026-11-09 | `TargetLevel` AD_GROUP/CAMPAIGN only; no list or shared-negative path |
| The target entity in the Amazon Ads API (common models) | https://advertising.amazon.com/API/docs/en-us/reference/common-models/targets | official | 2026-11-09 | No Sponsored Display column |
| Campaign management overview | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview | official | 2026-11-09 | Lists SD among supported ad products |
| Global campaigns for Sponsored Products | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/global-campaigns | official | 2026-11-09 | `marketplaces` on targets; 207 with `partialSuccess`; only `spCampaigns` surfaces global campaigns |
| Sponsored Display contextual targeting guide | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/contextual-targeting | official | 2026-11-09 | `/sd/negativeTargets` negates expressions in the ad group |
| Creating negative keyword targeting (SB guide, re-read; H1 "Sponsored Brands negative keyword targeting") | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/targeting/negative-keyword-targeting | official | 2026-11-09 | "recommendations" link targets `listNegativeKeywords`; 207 example |
| Target (Targeting), Targeting (Targeting), Targeting match type (Targeting) dimensions (re-read) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/targeting/target (and /targeting, /targeting-match-type) | official | 2026-11-09 | No `target.value` in the library |
| Helpful concepts [Reporting v1] | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/helpful-concepts | official | 2026-11-09 | Rows aggregate by requested dimensions |
| Ad campaign attribution | https://advertising.amazon.com/help/GX7KDKHMWQYMJ385 | official | 2026-11-09 | One conversion, one ad interaction, across campaigns and advertisers |
| Portfolio budgets | https://advertising.amazon.com/help/GU7E77PGF96FMW3X | official | 2026-11-09 | Portfolios hold budget caps |
| Use portfolios with bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-portfolios | official | 2026-11-09 | Portfolio tab columns: no negatives |
| Bulksheets FAQs | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/faqs | official | 2026-11-09 | Blank Operation rows ignored |
| What agentic shopping means for advertising | https://advertising.amazon.com/library/news/agentic-shopping-advertising | official | 2026-11-09 | Rufus + Alexa+ → Alexa for Shopping; automatic eligibility; Alexa+ Conversational Ads |
| Analytics Reports (SP-API report type values) | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics | official | 2026-11-09 | SQP report type name, eligibility, periods |
| Understand keyword match types (re-read) | https://advertising.amazon.com/help/GHTRFDZRJPW6764R | official | 2026-11-09 | Highest-bid sentence's scope; `lastModified` 2026-07-29 |
| A guide to targeting with Sponsored Products (re-read) | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official | 2026-11-09 | "won't be bidding against yourself"; multiple campaigns, priority bids |
| Introducing Shared Negative Keywords List (Karooya) | https://www.karooya.com/blog/introducing-shared-negative-keywords-list-for-amazon-ads/ | opinion | 2026-11-09 | Shared list missing on Amazon; tool writes campaign-level negatives |
| Negative Keywords Guide: Reducing Wasted Ad Spend (SellerSprite) | https://www.sellersprite.ai/en/blog/Negative-Keywords-Guide-Reducing-Wasted-Ad-Spend | opinion | 2026-11-09 | Claims native lists and portfolio negatives (contradicted) |
| Which Negative Keywords Save Money (RedHen Labs) | https://rrw-ads.com/blog/which-negative-keywords-save-money | opinion | 2026-11-09 | 69 campaign-level exact negatives over 43 campaigns |
| Amazon Negative Keywords: Match Types, Limits and Workflow (Agent Central) | https://agentcentral.to/blog/amazon-negative-keywords | opinion | 2026-11-09 | Restates Amazon limits; no shared-list content (no claim cited) |
| How Do I Identify And Handle Search Term Duplicates (Ad Badger) | https://www.adbadger.com/blog/manage-duplicate-search-terms-on-amazon/ | opinion | 2026-11-09 | Same entity, no self-bidding; aggregate per term |
| Keyword Cannibalization Is Killing Amazon PPC in 2026 (Pare) | https://pare.so/blog/keyword-cannibalization-amazon-ppc-campaign-structure-2026 | opinion | 2026-11-09 | "cheapest click wins" claim, unsourced |
| Amazon PPC Keyword Cannibalization: Am I Bidding Against Me? (Sermondo) | https://sermondo.com/amazon-ppc-keyword-cannibalization/ | opinion | 2026-11-09 | "only one of your keywords" claim, unsourced |
| Keyword harvesting funnel (Adbrew, re-read) | https://adbrew.io/blog/amazon-ppc-how-to-automate-a-keyword-harvesting-funnel | opinion | 2026-11-09 | Product-group negatives; serving split between campaigns |
| Search term isolation and profit control (FiveX, re-read) | https://fivex.com/blog/amazon-search-term-isolation-profit-control/ | opinion | 2026-11-09 | Total SKU sales as the measure |
| Rutz, Bucklin & Sonnier 2012; Ghose & Yang 2009; Agarwal, Hosanagar & Smith 2011; Narayanan & Kalyanam 2015 (OpenAlex records) | https://api.openalex.org/works/https://doi.org/10.1509/jmr.10.0354 (and 10.1287/mnsc.1090.1054, 10.1509/jmr.08.0468, 10.1287/mksc.2014.0893) | research | 2026-11-09 | Abstracts for R5b |
| Searches (no page): "Amazon Ads account-level negative keywords sponsored products 2026"; "negative keyword list Amazon Ads console shared across campaigns OR portfolio"; "site:advertising.amazon.com negative keyword list apply multiple campaigns"; "Amazon Ads 2026 new feature negative keywords brand level OR account level OR portfolio level" | (web search) | search | 2026-11-09 | No Amazon page on account-, brand- or portfolio-level or shared negatives |

**Unreachable.**

- https://pacvue.com/blog/key-to-success-in-conquering-negative-keywords/: HTTP 403 to a plain GET, twice.
- https://helpdesk.scaleinsights.com/en/articles/13830678-negative-keywords-are-a-trap-we-found-a-loophole: DNS failure (host not found).
- https://help.intentwise.com/en/articles/5170239-harvest-keywords-and-targets-with-automated-rules: HTTP 404.
- https://www.teikametrics.com/blog/amazon-negative-keywords/: HTTP 404.
- https://www.junglescout.com/resources/articles/amazon-negative-keywords/: HTTP 404.
- https://advertising.amazon.com/library/webinars/optimize-negative-targeting: on 2026-11-09 it returns the Amazon Ads Academy JavaScript shell ("You need to enable JavaScript to run this app"), no webinar content.
- Amazon library guides at /library/guides/negative-keywords, /keyword-match-types, /search-term-report and /sponsored-brands-best-practices: HTTP 404.
- Amazon help pages GBA9AQKKVVBPFHXE (Target Promotion help; now serves the "Support Center Homepage" node), GRRZ6B9D598NCMH4 (a "Reports" category node) and GAVBGS8JVC6NK7A2 (a "Sponsored Products" category node): no article text by a plain GET.
- API guide paths guides/sponsored-brands/negative-targeting, guides/sponsored-brands/negative-keywords, guides/amazon-marketing-cloud/privacy (and two variants), mcp/skills/skills-library/keyword-harvesting and mcp/skills/skills-library/campaign-management: HTTP 404.
- API docs sitemap and llms.txt: JavaScript shell, no list.
- dblp search: bot wall. Semantic Scholar API: HTTP 429. PubMed web page: cookie wall (E-utilities used instead; no abstract). Chapelle's PDF on the author's site: HTTP 404 (OpenAlex abstract used).
- Seller Central help (via its content call): not attempted, outside this seat's limits.
- (Resolved by the verifier: the Perpetua limits article and the Karooya limits page, earlier seen only as search results, were opened on 2026-11-09 and are in the table.)
- Pacvue (HTTP 403), the Scale Insights helpdesk (no DNS answer), Intentwise help, Teikametrics and Jungle Scout articles (HTTP 404) and the four Amazon library guide paths (HTTP 404) were retried by the verifier on 2026-11-09 with the same results.

## Open questions

1. **Does the console still list impression-only search terms?** The v3 FAQ says it does. The console help, bulksheet page, best-practice guide and PPC Land say clicked-only. WisePPC says an API field behind "its advertising reports" narrowed to clicked queries in mid-July 2026, retroactively; it does not name the console. No Amazon page read dates a change.
2. **Can a seller add a campaign-level negative product target to a manual SP campaign?** The SP API guide says vendors only. The 2025-05-22 note says every campaign, US. The SP 3.0 model says AUTO only.
3. **Which v1 field spelling does the service accept for the target on a search-term row?** The migration page gives `target.value`/`target.matchType`; the dimension pages give `targeting.value`/`targetingMatchType.value`/`adGroupTarget.*`. The New features page's sample response flags `target.value` as `PENDING_DEPRECATION`; whether that is illustrative or real is not stated.
4. **How far back do v1 search terms go?** The dates page sets 24 months for `date.value` and names no exception for search term. The console help says 65 days, and v3 says 65 (SP) and 60 (SB).
5. **Does `advertisedProduct.id` combine with `searchTerm.value` in v1?** That would tie a term to the ASIN shown, which v3 cannot.
6. **`matchedTarget.value` is now Sponsored Display only.** Was it ever valid with SP search terms (prior research said so), or was that a misreading?
7. **What does a negative broad keyword block, and which ad products accept it?** It is in the SP 3.0 and v1 models and the keyword guide, and absent from the console help and bulksheets.
8. **Does negative phrase respect word order?** Ad Badger and Scale Insights say yes; JumpFly says no. Amazon says "contain the complete phrase or close variations".
9. **(Answered by the verifier.)** Amazon's "Sponsored ads campaign limits" help page states 10,000 campaign negative keywords and 10,000 ad-group negative keywords (C5). Open remainder: whether legacy SB campaigns differ (Karooya, 2018, says 1,000 there).
10. **Does SP have term-level bids on exact keywords (Nova, 2026-02-18)?** The cited help page does not say so.
11. **How do prompt, Rufus and Alexa-for-Shopping clicks appear in the search term report,** and under what text?
12. **What is the `*` row against Nova's "privacy threshold … grouped" row?** Is a privacy-withheld query shown as `*`, as a blank, or dropped?
13. **v1 concurrency: per client ID (limits page, overview) or per advertiser (2026-09-30 release note)?**
14. **The release notes list a "Review Requests API (beta)" entry dated 2026-11-16,** after today's read. It is unexplained; it may be a scheduled publication.
15. **Does Target Promotion, or the MCP harvesting workflow, add negatives in the source?** No page read says so.
16. **Does the v1 target create accept lower-case ASINs as printed in search term rows,** or does it need the catalogue's upper case?
17. **What does Seller Assistant's auto-optimization (Accelerate 2026) count as a "performing" search term, does it negate at the source, and do its additions appear as ordinary targets through `query/targets`?**
18. **Do a campaign's negative keywords also stop its prompts from showing,** given that prompts "leverage existing campaign parameters (e.g., campaign targeting)"?
19. **Does `POST /adsApi/v1/create/targets` accept Sponsored Display negatives?** `SPONSORED_DISPLAY` is in the v1 `AdProduct` enum and the overview lists SD, but the target entity tables have no SD column and no 2026 release note read announces SD in v1 campaign management.
20. **Does Amazon's highest-bid rule reach across campaigns and ad groups,** or only across match types of one keyword in one ad group? The help sentence is scoped to "the same keyword"; practitioners split (Ad Badger, Sermondo: no self-bidding; Pare: "cheapest click wins"; Adbrew: Amazon picks the serving campaign).
21. **Does a v1 report accept `searchTerm.value` with no campaign, ad group or target field,** returning one row per query across the account?
22. **Do global SP campaigns' search terms appear anywhere in reporting,** given "Only the `spCampaigns` report surfaces global campaigns"?
23. **Do a campaign's negatives apply to its ads in Alexa for Shopping and to Alexa+ Conversational Ads?** Both are automatic; neither page mentions negatives.

## Positions

Fact-worded. Amazon's sources come first. Every position carries its tag and page.

**P-search-terms-and-negatives-1.** The Amazon Ads API search term report "only include[s] impressions that resulted in at least one ad click"; a term with impressions and no click has no row. [official] (Search term reports [v3], read 2026-11-09)

**P-search-terms-and-negatives-2.** Amazon's console help for the SP search term report says it "includes only the search terms that resulted in at least 1 ad click", while Amazon's v3 reporting FAQ says the console report "contains all search terms that had an impression"; the two Amazon pages disagree. [official] (Search term report for Sponsored Products, G3HEFZYWZF84NPS9; Sponsored ads reporting FAQ (version 3); read 2026-11-09)

**P-search-terms-and-negatives-3.** A search term of `*` is a product-detail-page placement with no search keyword. [official] (Search term reports [v3], read 2026-11-09)

**P-search-terms-and-negatives-4.** ASIN-shaped search terms (Amazon's example "b00ipgvvz4") are the detail pages the ad appeared on, and appear only for SP automatic campaigns and product-attribute-targeted ad groups. [official] (Search term reports in bulksheets; Search term report for Sponsored Products; read 2026-11-09)

**P-search-terms-and-negatives-5.** Amazon defines the customer search term as "the search term used by the customer or inferred by Amazon in non-search contexts", including off-Amazon placements; no report field read marks which rows were inferred. [official] (Search term report for Sponsored Products, read 2026-11-09)

**P-search-terms-and-negatives-6.** The v3 SP search term report carries the keyword or targeting expression, match type, keyword id, ad group and campaign for each row, and no advertised ASIN or SKU. [official] (Search term reports [v3]; Reporting columns (version 3); read 2026-11-09)

**P-search-terms-and-negatives-7.** Broad, phrase and exact match in SP all "account for plurals, misspellings, and translations"; Amazon's exact-match example lets "outside lights" match "outdoor lights", and broad may match a query that does not contain the keyword. [official] (Understand keyword match types, GHTRFDZRJPW6764R, read 2026-11-09)

**P-search-terms-and-negatives-8.** When several match types of the same keyword with different bids match a query, "the match type with the highest bid will be used". [official] (Understand keyword match types, read 2026-11-09)

**P-search-terms-and-negatives-9.** Negative keywords stop ads on shopping-results pages for matching queries; negative ASIN and brand targets stop ads on the matching products' detail pages. [official] (Add negative keywords or negative products targeting, G8W49VU65XQ4T2NS; All releases, entry of May 22, 2025; read 2026-11-09)

**P-search-terms-and-negatives-10.** Negative product targets affect only product-attribute targets and automatic targets: at ad-group level in that ad group, at campaign level in every ad group of the campaign. [official] (Add negative keywords or negative products targeting, read 2026-11-09)

**P-search-terms-and-negatives-11.** In Sponsored Products a campaign-level negative keyword applies to all ad groups in the campaign and an ad-group-level one to that ad group only; Sponsored Brands has "no campaign-level negative targeting". [official] (Negative keyword targeting [SP]; Sponsored Brands negative keyword targeting; read 2026-11-09)

**P-search-terms-and-negatives-12.** Amazon's console help defines negative phrase as blocking queries that "contain the complete phrase or close variations" and negative exact as blocking queries that "contain the exact phrase or close variation", and states the match type of an existing negative keyword cannot be changed. [official] (Add negative keywords or negative products targeting, read 2026-11-09)

**P-search-terms-and-negatives-13.** Amazon's help gives word and character limits for negative phrase and negative exact keywords, and the API limits page gives part and character limits per match type; the figures are read from those pages. [official] (Add negative keywords or negative products targeting; Limits, constraints, and quotas, "Keyword character constraints"; read 2026-11-09)

**P-search-terms-and-negatives-14.** Amazon's help states a buffer period before negative keywords and negative products take effect, longer for negative products than for negative keywords. [official] (Add negative keywords or negative products targeting, read 2026-11-09)

**P-search-terms-and-negatives-15.** The console help and bulksheets offer negative exact and negative phrase only; the SP 3.0 and v1 API models also accept a broad match type for negative keywords, and Amazon's keyword guide mentions "exact, phrase, or broad". [official] (Add negative keywords or negative products targeting; How to create Sponsored Products campaigns in bulksheets; Sponsored Products 3.0 OpenAPI; Amazon Ads API v1 merged OpenAPI; What is Keyword Targeting?; read 2026-11-09)

**P-search-terms-and-negatives-16.** In API v1 a negative keyword, ASIN or brand is created with `POST /adsApi/v1/create/targets` and `negative: true`; a `campaignId` alone makes it campaign-level, an `adGroupId` makes it ad-group-level, and the reply is a per-item `207`. [official] (Negative keyword targeting [SP]; Sponsored Products negative product and brand targeting overview; read 2026-11-09)

**P-search-terms-and-negatives-17.** Amazon's SP API guide says campaign-level negative product targeting in manual campaigns is available only to vendors, while the 2025-05-22 release note says every campaign and ad group in the US has the same negative options regardless of targeting type; the SP 3.0 model says campaign negative targeting clauses are only for AUTO campaigns. [official] (Sponsored Products negative product and brand targeting overview; All releases, entry of May 22, 2025; Sponsored Products 3.0 OpenAPI; read 2026-11-09)

**P-search-terms-and-negatives-18.** Amazon's SP brand-negative recommendations "include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands." [official] (Sponsored Products 3.0 OpenAPI, `GET /sp/negativeTargets/brands/recommendations`, read 2026-11-09)

**P-search-terms-and-negatives-19.** Amazon's targeting guide recommends evaluating a keyword's performance after a stated minimum number of clicks before adding it as a negative, and letting negatives run for a stated period before evaluating them; it recommends phrase or exact match for negative keywords. [official] (A guide to targeting with Sponsored Products, read 2026-11-09)

**P-search-terms-and-negatives-20.** Amazon's guidance recommends running an automatic campaign for a stated period, then using its search term report to find keywords and ASINs for manual campaigns, and adding well-performing search terms as exact match with a raised bid. [official] (A guide to targeting with Sponsored Products; Best practices for your Sponsored Products ads; What is Keyword Targeting?; read 2026-11-09)

**P-search-terms-and-negatives-21.** Target Promotion is the API's mechanism to promote targets from broader to more focused targeting, using recommendations "as recommended by Amazon heuristics" from clicks and conversions; its guide does not describe adding negatives in the source. [official] (Target Promotion; Sponsored Products 3.0 OpenAPI; read 2026-11-09)

**P-search-terms-and-negatives-22.** Amazon's reporting FAQ states that impression and click data can change for up to three days and that conversion data is restated 1, 7 and 28 days after the conversion event, so with a 14-day window attribution can update up to 42 days after the report date. [official] (Sponsored ads reporting FAQ (version 3), read 2026-11-09)

**P-search-terms-and-negatives-23.** Amazon's reporting overview recommends waiting a stated number of days for the most accurate click data, says conversion data is subject to change for a stated period back, and says invalid traffic is monitored for up to 30 days and removed from reports. [official] (Amazon Ads reporting overview; Traffic validation, GBYPYH79NGJJ5JPS; read 2026-11-09)

**P-search-terms-and-negatives-24.** Reporting API v1 reports SP conversions on the account's default look-back (seller 7-day, vendor 14-day) and all conversions on traffic date, with Promoted and Halo forms replacing "Other SKU". [official] (Overview of the Reporting v1 API, read 2026-11-09)

**P-search-terms-and-negatives-25.** v1 search-term impression share and rank require `adProduct.value`, `advertiserAccount.id` and `searchTerm.value` and are incompatible with campaign, ad group, target and advertised product dimensions; they are the account's share on the query. [official] (Impression share metrics [search], read 2026-11-09)

**P-search-terms-and-negatives-26.** Sponsored Brands v2 `searchTermImpressionShare` and `searchTermImpressionRank` stop returning values on 2026-11-10; v3 reporting stops delivering data on 2027-06-30; the console's legacy Sponsored Ads reports are sunset by 2026-12-31. [official] (Deprecations; Streamline campaign analysis with unified reporting; read 2026-11-09)

**P-search-terms-and-negatives-27.** The bulksheet search term tab always uses a 7-day lookback regardless of the bulk file's date range, carries the source campaign, ad group, keyword and product-targeting ids, and its page defines CTR and conversion rate inverted. [official] (Search term reports in bulksheets, read 2026-11-09)

**P-search-terms-and-negatives-28.** AMC's `sponsored_ads_traffic` holds impression and click events with `customer_search_term`, the text the shopper typed, released only for rows with at least two distinct users. [official] (Sponsored ads traffic [AMC]; Data aggregation thresholds in AMC; read 2026-11-09)

**P-search-terms-and-negatives-29.** The MCP server's campaign-management tools read today number 32 and include none named for harvesting or negatives, while its 2026-02-18 release note describes workflows that "automate keyword harvesting from automatic to manual campaigns". [official] (MCP campaign management tool definitions; All releases, entry of February 18, 2026; read 2026-11-09)

**P-search-terms-and-negatives-30.** Ad Badger (Michael Erickson Facchin) negates terms at 2,500 impressions with CTR under 0.18% and no conversions, more than $35 spend with no conversions, or more than 34 clicks without a conversion, calls these "starting points", and exempts competitor brand terms. [opinion] (Ad Badger, "Amazon PPC Negative Keywords: Cut Wasted Ad Spend (2026)", 2025-03-06, modified 2026-10-28, read 2026-11-09)

**P-search-terms-and-negatives-31.** Several practitioners put the click count before negating a non-converting term between 10 and 50 and tie it to price, margin or conversion rate: Jungle Scout (Galeana) 10, Ad Badger 34, Scale Insights' default "Unique Word with 0 Sales" filter 25 (per word, not per term), Seller Labs 20–30, Canopy 20–30 for $30–100 products and 40–50 above $100. [opinion] (pages in "What practitioners add", read 2026-11-09)

**P-search-terms-and-negatives-32.** Several practitioners add a term moved to exact as negative exact where it came from: Seller Labs in the auto campaign ("This prevents: Internal competition, Inflated CPC, Performance dilution"), Canopy in auto and broad, Adbrew in every auto, broad and phrase campaign of the product group, Ad Badger in broad and auto for a term kept in exact at a lower bid; Helium 10's Prestozon rule puts negative exact in the broad ad group and negative phrase in the auto campaign. [opinion] (pages in "What practitioners add", read 2026-11-09)

**P-search-terms-and-negatives-33.** Adbrew (Ayush Chaudhary) moves a term to phrase at one order in 30 days within 1.5× target ACoS and to exact at two orders at or under target, excludes the last 7 days, calls these "practitioner defaults … not Amazon rules", and works an example in which two orders need about 17 clicks at 12% conversion and about 33 at 6%. [opinion] (Adbrew, 2026-10-27, read 2026-11-09)

**P-search-terms-and-negatives-34.** Ad Badger's PPC Den page says branded terms may convert every couple of clicks while competitor terms may need fifty, and that one rule across the board kills keywords "that were slow, not bad". [opinion] (Ad Badger, 2026-01-30, read 2026-11-09)

**P-search-terms-and-negatives-35.** Scale Insights' negative word rule aggregates single words across search terms per product and adds non-performing words as ad-group negative phrase, skipping singular and plural forms of words in the product title. [opinion] (Scale Insights docs, read 2026-11-09)

**P-search-terms-and-negatives-36.** Practitioners disagree on whether negative phrase is order-sensitive: Ad Badger and Scale Insights say it blocks the words in sequence (Scale Insights' own example also lists "blue running shoes" as blocked by "blue shoes"), JumpFly says "in any order". [opinion] (Ad Badger; Scale Insights; JumpFly; read 2026-11-09)

**P-search-terms-and-negatives-37.** With zero conversions in n clicks, the 95% upper confidence bound on the conversion rate is approximately 3/n (the rule of three). [research] (Hanley & Lippman-Hand, JAMA 1983; Rule of three (statistics), read 2026-11-09)

**P-search-terms-and-negatives-38.** Conversions in advertising can arrive long after the ad interaction, and delayed-feedback models treat not-yet-converted recent clicks as uncertain rather than negative. [research] (Chapelle, KDD 2014, read 2026-11-09)

**P-search-terms-and-negatives-39.** In paid search, keyword conversion data are sparse and position is endogenous; a keyword list built on estimated conversion rates outperformed lists built on observed conversion and click-through rates. [research] (Rutz, Bucklin & Sonnier, JMR 2012, read 2026-11-09)

**P-search-terms-and-negatives-40.** In an eBay field experiment, brand-keyword ads had no measurable short-term benefit, and non-brand ad spend was dominated by frequent users not influenced by ads. [research] (Blake, Nosko & Tadelis, Econometrica 2015, read 2026-11-09)

**P-search-terms-and-negatives-41.** Amazon's ESCI dataset labels query-product pairs Exact, Substitute, Complement or Irrelevant, with "Irrelevant" meaning the product "fails to fulfill a central aspect of the query". [research] (Reddy et al., arXiv 2206.06588, read 2026-11-09)

**P-search-terms-and-negatives-42.** Amazon's "Sponsored ads campaign limits" help page states caps on campaign negative keywords, ad-group negative keywords and negative products per ad group (10,000 each on 2026-11-09, a figure read from the page), says the limits apply to SP, SB and Display across all advertiser types, and says "Amazon now increases customer limits as they approach a limit"; the API's 1000 is a per-request batch size, not a cap. [official] (Sponsored ads campaign limits, G86H2227323T8T4Q; Amazon Ads API v1 merged OpenAPI, `CreateTargetRequest`; read 2026-11-09)

**P-search-terms-and-negatives-43.** Amazon's match-type help defines the SP auto groups by surface: close match and loose match by the search terms shoppers use, substitutes and complements by the detail pages shoppers view. [official] (Understand keyword match types, GHTRFDZRJPW6764R, read 2026-11-09)

**P-search-terms-and-negatives-44.** At Accelerate 2026 Amazon announced a Seller Assistant auto-optimization that, on campaigns it drafts, keeps "adding search terms that are performing, pausing those that aren't, and holding every bid under a maximum the seller sets"; the announcement states no threshold and nothing on source negatives. [official] (At Accelerate 2026, Amazon shares new AI tools as a force multiplier for independent sellers, read 2026-11-09)

**P-search-terms-and-negatives-45.** In API v1, `POST /adsApi/v1/query/targets` requires `adProductFilter` and accepts `negativeFilter`, `adGroupIdFilter`, `campaignIdFilter`, `matchTypeFilter`, `keywordFilter`, `targetTypeFilter` and `stateFilter`; the auto-campaign guide reads auto target ids through it. [official] (Amazon Ads API v1 merged OpenAPI, `QueryTargetRequest`; Get started with auto campaigns; read 2026-11-09)

**P-search-terms-and-negatives-46.** Amazon's negatives exist at two levels only: the v1 `TargetLevel` enum is `AD_GROUP` and `CAMPAIGN`, the SP 3.0 model has ad-group and campaign negative paths, and Sponsored Brands and Sponsored Display negatives are ad-group level; no v1 or 3.0 model read holds an account-, brand- or portfolio-level negative or a shared negative list, and a portfolio carries a budget cap. [official] (Amazon Ads API v1 merged OpenAPI incl. beta; Sponsored Products 3.0 OpenAPI; Sponsored Brands 3.0 YAML; Sponsored Display 3.0 YAML; Portfolio budgets, GU7E77PGF96FMW3X; Use portfolios with bulksheets; read 2026-11-09)

**P-search-terms-and-negatives-47.** Each Sponsored Products bulksheet negative row carries its Campaign ID ("Campaign negative keyword") or its Campaign ID and Ad group ID ("Negative keyword"), with match type `negativeExact` or `negativePhrase`, and a row with a blank Operation is ignored on upload. [official] (How to create Sponsored Products campaigns in bulksheets; Bulksheets FAQs; read 2026-11-09)

**P-search-terms-and-negatives-48.** Karooya wrote in 2019 that "the shared negative keyword list has been missing from Amazon Ads" and its tool adds each list entry "as campaign-level negative keywords" in every associated campaign; RedHen Labs keeps 69 campaign-level exact negatives across 43 campaigns; Adbrew negates a term that reaches exact "in every auto, broad and phrase campaign of that product group". [opinion] (Karooya, 2019-02-12; RedHen Labs, 2026-08-27; Adbrew, 2026-10-27; read 2026-11-09)

**P-search-terms-and-negatives-49.** SellerSprite's team writes that "Amazon allows you to create reusable Negative Keyword Lists" and that portfolios can carry negatives across campaigns; no Amazon model, help page or bulksheet tab read on 2026-11-09 carries either. [opinion] (SellerSprite, 2026-06-16) [official] (pages of P-46)

**P-search-terms-and-negatives-50.** The SP 3.0 model's negative paths are `/sp/negativeKeywords` and `/sp/campaignNegativeKeywords` (`NEGATIVE_EXACT`, `NEGATIVE_PHRASE`, `NEGATIVE_BROAD`) and `/sp/negativeTargets` and `/sp/campaignNegativeTargets` (`ASIN_SAME_AS`, `ASIN_BRAND_SAME_AS`), each with create (`POST`), update (`PUT`), `/delete` and `/list`; writes return `207` with `success[]` and `error[]` arrays keyed by `index`, and campaign negative targeting clauses are "only available for AUTO campaigns". [official] (Sponsored Products 3.0 OpenAPI, read 2026-11-09)

**P-search-terms-and-negatives-51.** Sponsored Brands negative keywords are written with `POST /sb/negativeKeywords` on the SB 3.0 model, at most 100 per call *(figure)*, `matchType` `negativeExact` or `negativePhrase`, and the `207` reply is an array in request order with `code` and `keywordId`; an archived negative keyword "can not be recreated" for the campaign. [official] (Sponsored Brands 3.0 YAML; Sponsored Brands negative keyword targeting; read 2026-11-09)

**P-search-terms-and-negatives-52.** Sponsored Brands negative product targets are written with `POST /sb/negativeTargets` (`asinSameAs`, `asinBrandSameAs`; 1–100 items *(figure)*), whose reply is a `200` with `createTargetSuccessResults` and `createTargetErrorResults` keyed by `targetRequestIndex`. [official] (Sponsored Brands 3.0 YAML, read 2026-11-09)

**P-search-terms-and-negatives-53.** Sponsored Display negatives are ad-group negative targeting clauses on `POST /sd/negativeTargets` (`asinSameAs`, `asinBrandSameAs`, `expressionType` `manual` or `auto`, up to 100 per call *(figure)*), replying `207` with an array of `code`, `description` and `targetId`; the SD 3.0 model has no negative keyword path. [official] (Sponsored Display 3.0 YAML; Sponsored Display contextual targeting guide; read 2026-11-09)

**P-search-terms-and-negatives-54.** The v1 target entity tables have no Sponsored Display column, and Amazon's 2025 general-availability notes for v1 campaign management name Sponsored Products, Sponsored Brands and Amazon DSP and promise Sponsored Display "later"; no 2026 release note read announces Sponsored Display in v1 campaign management, while the v1 `AdProduct` enum and the campaign-management overview include it. [official] (Targets [campaign management entity guide]; The target entity in the Amazon Ads API [common models]; All releases, entries of August 1 and December 1, 2025; Campaign management overview; Amazon Ads API v1 merged OpenAPI; read 2026-11-09)

**P-search-terms-and-negatives-55.** `/sb/negativeKeywords` and `/sb/negativeTargets` are on the SB 3.0 YAML model ("Amazon Ads API - Sponsored Brands 3.0"); `/sb/negativeTargets/brands/recommendations` is on the JSON model titled "Sponsored Brands 3.0" and on the SB 4.0 model, neither of which carries `/sb/negativeKeywords`. [official] (the three Sponsored Brands models, read 2026-11-09)

**P-search-terms-and-negatives-56.** "Amazon will attribute a conversion to no more than 1 ad interaction across all campaigns and all advertisers", so a conversion a harvested keyword reports is reported by no other campaign of the seller's. [official] (Ad campaign attribution, GX7KDKHMWQYMJ385, read 2026-11-09)

**P-search-terms-and-negatives-57.** Amazon's targeting guide states "you won’t be bidding against yourself by adding different match types on the same keyword", and, for several campaigns bidding on keywords relevant to several products, that bids set by product priority give the top-priority product "the best opportunity to get top ad placements" while lower-priority products may "also appear on the search results page". [official] (A guide to targeting with Sponsored Products, read 2026-11-09)

**P-search-terms-and-negatives-58.** Practitioners disagree on how the seller's own campaigns meet on one query: Ad Badger says Amazon "won't pit them against each other" and Sermondo that Amazon enters "only one of your keywords", Pare says an internal auction lets "the cheapest click" win, and Adbrew says "Amazon picks which of your campaigns serves" and the exact bid stops setting the price; none cites an Amazon page or measured data. [opinion] (Ad Badger, 2023-05-03; Sermondo; Pare, 2026-05-11; Adbrew, 2026-10-27; read 2026-11-09)

**P-search-terms-and-negatives-59.** Search Query Performance gives, per ASIN and query, the ASIN's impressions, clicks, cart adds and purchases from the search results page beside the query's totals, by `WEEK`, `MONTH` or `QUARTER`, through `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` for brand-registered sellers with the Brand Analytics role. [official] (sellingPartnerSearchQueryPerformanceReport.json; Analytics Reports; read 2026-11-09)

**P-search-terms-and-negatives-60.** In May 2026 Amazon merged Rufus and Alexa+ into Alexa for Shopping on the US Amazon Shopping app, website and Echo Show, where existing sponsored ads campaigns are "automatically eligible to serve … without additional campaign setup"; on Alexa-enabled devices Alexa+ carries "Alexa+ Conversational Ads", in which advertisers with sponsored ads campaigns "are automatically enrolled". [official] (What agentic shopping means for advertising, 2026-06-11; Meet Alexa for Shopping…, 2026-05-13; read 2026-11-09)

**P-search-terms-and-negatives-61.** The v1 Dimensions library names a row's target `adGroupTarget.id` (primary key), with text `targeting.value` and match type `targetingMatchType.value`; `target.value` appears only in Amazon's migration examples and in the New features page's warning example, flagged `PENDING_DEPRECATION`. [official] (Target, Targeting and Targeting match type dimension pages; Migrating from: spSearchTerm; New features [Reporting v1]; read 2026-11-09)

**P-search-terms-and-negatives-62.** On web search engines, studies disagree on how conversion rate moves with ad position: higher positions raised it (Rutz, Bucklin & Sonnier, instrumental variables), it was highest at the top (Ghose & Yang), or it rose lower down (Agarwal, Hosanagar & Smith, field experiment); Narayanan & Kalyanam show that simple position comparisons are biased by auction selection and that regression-discontinuity effects are much smaller and present only at some positions. [research] (JMR 2012; Management Science 2009; JMR 2011; Marketing Science 2015; abstracts read 2026-11-09)

**P-search-terms-and-negatives-63.** A global Sponsored Products campaign (v1, `marketplaceScope` `GLOBAL`) gives each target a `marketplaces` list with per-marketplace overrides, its writes return `207` with `success`, `error` and `partialSuccess`, and "Only the `spCampaigns` report surfaces global campaigns." [official] (Global campaigns for Sponsored Products, read 2026-11-09)

### Seat's positions (enter no skill)

- S1. Because Amazon's pages disagree on what the console shows (P-2) and on seller campaign-level negative product targets (P-17), the service's reply, not a page, is the last word on each.
- S2. A practitioner's fixed click bar for negation corresponds to a particular assumed conversion rate through (1−p)^n; read without the seller's own rate it says little.
- S3. Judging thousands of search terms at once with one cut-off negates some terms that were merely unlucky, in proportion to the count judged (Benjamini & Hochberg 1995); shrinkage toward the ad group's rate (Casella 1985; Lee et al. 2012) is the research form of "slow, not bad".
- S4. A negative exact on a harvested query leaves the source's other matches untouched; a negative phrase can remove a long tail; close variants make both wider than their literal text.
- S5. The SP search term report cannot say which ASIN in a multi-ASIN ad group was shown; that is a reason harvest decisions in such ad groups carry an attribution question the report does not answer.
- S6. The unit of a negative or a harvest is the query, not the target: its rows summed across every campaign before and after, and the ASIN's SQP counts on it. Spend on the negated target alone shows the move out of one row, not where the query went; sales on a harvested keyword alone show the move into one row, not what the query added (A9b, P-56).
- S7. A product-group negative list is the seat's or the seller's object, not Amazon's; on Amazon it exists only as the set of per-campaign negatives the writes created, which `query/targets` or the v3 list paths read back (C8).
- S8. Where a v1 negative write is refused, the v3 path of the same ad product is documented; for Sponsored Display, `/sd/negativeTargets` is the only path a page read documents (C9).

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** Every page in "Pages read" was re-opened on 2026-11-09 by a plain GET. Ads API guides were read as their markdown sources on `d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`. The SP 3.0, SB 3.0 and v1 merged OpenAPI models and the MCP tool file were parsed as JSON. Amazon Ads help pages were read from the article JSON (`__scV2Content`) inside their HTML. Library, blog, what's-new, aboutamazon and practitioner pages were read as HTML. Papers were checked against OpenAlex (titles, authors, abstracts), Crossref, PubMed E-utilities and the arXiv HTML version. Each quoted string was searched for verbatim. Each page name was compared with the page's title or H1, and each tag with the page's owner. Searches were run for 2025–2026 Amazon announcements touching search terms, negatives and harvesting. No Ads API host (advertising-api*.amazon.com), Login with Amazon, Amazon Ads MCP server endpoint, SP-API host or Seller Central content call was called; the API sample `curl` lines on the docs pages were read as text, never run. Nothing was written outside this file.

**Corrections (was → now).**

1. E1, targeting guide: "…before creating a manual campaign. This gives you time to collect search term data" and "You can then use the search term report … generating clicks and sales…" (neither on the page) → the page's own sentences ("By using metrics from the automatic campaign search term report…"; "Targeted ASINs that generate clicks or conversions show up in the “search term” column").
2. E1, keyword guide: "discover relevant search terms"; "After a couple of weeks, review your search term report" → "discover valuable search terms … to help optimize performance"; "After your campaign has been running for a couple of weeks, you can use the search term report…".
3. F1, second targeting-guide quote: "Once you've added negative keywords, we recommend … before evaluating their performance" → "However, let your negative keywords run for two weeks or more, before making any changes to your strategy."
4. E2, best-practices quote: "If you find search terms that are performing well, increase the bid…" (not on the page) → "First, check the search term report to identify keywords and products that are resulting in higher sales and conversion rate. Then increase the bid on those and add them as exact match type to optimize."
5. E2, help-page quote: "You can also add search terms as keywords to other ad groups" (not on the page) → the page's "copy these settings from the Search terms section of your ad group to new ad groups…" passage, plus its expanded-targeting line.
6. E3, Target Promotion: "Target Promotion helps advertisers automatically promote targets…" (not on the page) → the guide's "This combines the common practice of target harvesting…" sentence and the create call's description. Page name "Sponsored Products target promotion" → "Target Promotion" (H1).
7. E5: "so you can use them to update your bids" (not on the page) → the column text "Use this ID in the relevant entity row to update keywords or product targeting"; heading GUIDANCE → RULE.
8. A7, Adbrew quote "Inferred terms … need manual review" (not on the page) → "An inferred term can pass your rule without a shopper ever typing it…".
9. C4, Adbrew quote "allow up to 72 hours…" → "Amazon says negative keywords take up to 72 hours to apply and negative ASINs up to 96", marked as a restatement of Amazon's page.
10. E3, Adbrew "don't add source negatives" (not on the page) → "Neither negates a term at its source for you"; "A one-click keyword doesn't add the matching negative in your research campaigns".
11. B9, Amazon Ads Agent quote: it was attributed to the unBoxed 2026 article, but it is the site navigation → the article's own sentence ("Amazon Ads Agent is the unified buying experience…"), with the navigation line marked as such.
12. F3: listed under Amazon's GUIDANCE with "names 'Not migrating successful search terms to tighter match types' as a mistake" (not on the page) → relabelled as opinion on Amazon's domain; quotes replaced with the article's Problem 1 and Problem 4 wording; full title and author role added.
13. C5 and practitioners: "No Amazon page read states a cap on how many negatives a campaign or ad group may hold" → Amazon's help page "Sponsored ads campaign limits" (G86H2227323T8T4Q, found through Perpetua's link) states 10,000 / 10,000 / 10,000. Perpetua and Karooya pages, earlier "leads only", opened and cited; Perpetua's 1,000 marked out of date against Amazon's page. Open question 9 answered.
14. A4 and Open question 1: "WisePPC says the console changed" → WisePPC speaks of "its advertising reports" and "that API", not the console.
15. B3: added the New features page's sample `PENDING_DEPRECATION` warning on `target.value`, `target.value` listed twice on the migration page, and "Ad Product availability: N/A" on the `targeting.value` / `targetingMatchType.value` pages. B7: added the `DATE_LIMITED` warning code.
16. Ad Badger "Automate" row: "excluding the last 2 days" was attributed to the Nightly Hunt rules → it is an option of the Quick Attack tool; title and dates corrected.
17. Ad Badger negatives row and P-32: "After harvesting, block the same keyword as negative exact…" → the line's context is a term kept as positive exact at a lower bid. P-32 rewritten with each practitioner's own placement. Helium 10's "negated exact in every other ad group" was not on the page and was removed.
18. Helium 10 row: title "Amazon PPC keyword management rules" → "Prestozon’s Rules Engine and Why It Changes the Game"; quotes are now the page's. The Lauren Stair example, marked "not re-opened", was re-opened and cited directly.
19. Scale Insights row and P-31: the 25 clicks / 0 orders figure belongs to the Ads Insights "Unique Word with 0 Sales" filter, per word → reworded. Added Scale Insights' own phrase-match example contradiction to P-36.
20. Seller Labs: "at or under break-even ACoS" → "ACoS at or below your target"; paraphrases inside quotation marks replaced with the page's words.
21. Adbrew harvesting bullet: "discovery, research and performance tiers" → Research, Discovery, Performance layers; quoted "needs ~17 clicks…" (not verbatim) → unquoted worked example; Prime Day wording corrected.
22. Intentwise: paraphrase → its words "(except for Auto campaigns)"; title corrected. Perpetua help row: quotes and author corrected.
23. Nova news: "in the US" (not on the page) removed; author added; "up to 900%" on GYYZVM7LGSRYGWV5 placed in its video section.
24. Tinuiti snippet lead (unverified) → replaced by Amazon's own Alexa for Shopping announcement of 2026-05-13.
25. R13 title "Amazon's algorithmic rents" → "Behind the clicks: Can Amazon allocate user attention as it pleases?"; claim narrowed to the abstract ("top five … typically four are advertisements"). R5, R6: data sources added. R12: what the paper does versus the seat's application, separated.
26. Page names corrected to the pages' titles or H1s: PPC Land (hyphen), unBoxed 2026, unified reporting launch, both what's-new share and rank pages, SB guide ("Your complete guide to Sponsored Brands"), Ad Badger intent-cluster page, SP auto-campaign guide, target entity, exports target, both bulksheet example pages, entity page.
27. "What cx must read at run time": wording that told cx when to read or what to do ("read when a seller asks…", "shortened before the write rather than refused", "meaningless without them") → rewritten as facts about where a figure lives and what the reply carries. Added the required `adProductFilter` on `query/targets`.

**Additions from re-reading and 2025–2026 searches.**

- A10: auto groups defined by surface on the match-type help, and their v1 enum names.
- A11: prompts launch page.
- B11: Sponsored Brands search terms in bulksheets.
- B11/A4: the bulksheet's "typed into the search bar" definition.
- C5: `TargetCreate` level fields, and the auto-campaign guide's query-based id read.
- C7: the keyword guide's campaign-or-ad-group wording.
- D2: "Only available for Sellers and Vendors".
- E3b: Seller Assistant auto-optimization (Accelerate 2026).
- G1: dated share example.
- G2: v1 share by date.
- G4: SB keyword-recommendation share over 7 days.
- Stable items 20–21, positions 42–45 and open questions 17–18.

**Removals.** The unverified Tinuiti snippet, and the Helium 10 "negated exact in every other ad group" clause. No position was found unsourced or worded as behaviour beyond the edits above, so the seat's list kept its five items.

**Still unreachable (retried 2026-11-09).**

- Pacvue blog: HTTP 403.
- helpdesk.scaleinsights.com: no DNS answer.
- Intentwise help article, Teikametrics and Jungle Scout negative-keyword articles: HTTP 404.
- Amazon library guides /negative-keywords, /keyword-match-types, /search-term-report and /sponsored-brands-best-practices: HTTP 404.
- The optimize-negative-targeting webinar: Academy JavaScript shell.
- Help ids GBA9AQKKVVBPFHXE, GRRZ6B9D598NCMH4 and GAVBGS8JVC6NK7A2: category or home nodes with no article.
- MCP skills-library keyword-harvesting and campaign-management paths, and the skills-library index: HTTP 404.
- The ad-product research items whose full texts sit behind publishers: read through their OpenAlex abstracts only. The ESCI definitions were read in the arXiv HTML full text.

**Gap fill 2026-11-09** (research seat, after three completeness critics). Every page cited for the items below was opened on 2026-11-09 by a plain GET: OpenAPI models parsed as JSON or YAML, Ads API guides as their cloudfront markdown, help pages from the article text in their HTML, practitioner pages as HTML. No Ads API host, Login with Amazon, MCP endpoint, SP-API host or Seller Central content call was called.

Gaps added:

1. **Account-wide or portfolio-wide negatives (gap 1).** Added A-section C8 (no scope above the campaign: v1 `TargetLevel`, SP/SB/SD 3.0 paths, portfolio budgets help, bulksheet portfolio tab, bulksheet negative rows, global SP campaigns, searches finding no Amazon page), practitioners subsection "Shared and account-wide negative lists" (Karooya, SellerSprite, RedHen Labs, Adbrew), Stable 22–23, run-time reads for the product group's campaigns and the fan-out write, P-46 to P-49, seat S7. No practitioner page read describes the bulksheet push of one master list step by step; that part of the lead is recorded as not found, with Amazon's row shape standing in.
2. **v3 and per-product negative paths (gap 2).** Added C9 (table of SP 3.0 ad-group and campaign negative keyword and target paths, SB 3.0 negative keyword and target paths, SD `/sd/negativeTargets`, each with media type, required fields, enums, batch size and reply shape; the `Prefer` header; the SB archive rule; the SD guide's sentence), the v1 Sponsored Display coverage paragraph, Stable 24, run-time writes and list reads, P-50 to P-54, seat S8, Open question 19. The critic's "SD `/sd/negativeTargets` with its 207 shape" holds: the SD model's create replies `207`. One detail differs from the critic's frame: the SB 3.0 negative *targets* create replies `200` with success and error arrays, not `207`; only SB negative keywords reply `207`.
3. **Unit of measurement (gap 3).** Added A9b (the highest-bid sentence's scope; the targeting guide's "won't be bidding against yourself" and multi-campaign priority sentences; one conversion, one ad interaction; v1 aggregation by requested dimensions; SQP fields and report type; global campaigns only in `spCampaigns`), practitioners subsection "Reading one query across campaigns" (Ad Badger, Adbrew, Pare, Sermondo, FiveX), Stable 26, run-time "the query across the account" and SQP reads, P-56 to P-59, seat S6, Open questions 20–22. The critic's premise is right with one narrowing: GHTRFDZRJPW6764R's highest-bid sentence is scoped to "multiple match types with different bids for the same keyword" and does not on its face reach across campaigns; the account-wide reading rests on A1 (one row per serving target) and the one-credit attribution rule, not on that sentence alone. method/change-measurement.md S6 ("negative → spend on the negated term") is not this file's; the seat's note in A9b and S6 records what that metric reads.

Contradictions settled:

1. **Rufus and Alexa+ (owner beyond/ad-products-and-eligibility.md).** Re-opened *What agentic shopping means for advertising* (advertising.amazon.com, `datePublished` 2026-06-11, `dateModified` 2026-10-09) and *Meet Alexa for Shopping…* (aboutamazon, 2026-05-13). Both say Amazon merged Rufus and Alexa+ into Alexa for Shopping in May 2026, on the US Amazon Shopping app, website and Echo Show; the Ads page says existing sponsored ads campaigns are automatically eligible there, and separately names "Alexa+ Conversational Ads" on Alexa-enabled devices with automatic enrolment. So "Alexa for Shopping" does appear on an Amazon Ads page, and Rufus is no longer a separate surface; Alexa+ remains a separate device surface with its own ad form. This file's bullet was widened (US scope, the Ads page, the two surfaces), A11 points to it, Stable 28 and P-60 added, Open question 23 added.
2. **`target.value` (owner method/reporting.md).** Re-read the six pages of the v1 Dimensions library's targeting folder, the spSearchTerm migration page and New features. The library defines `adGroupTarget.id/.bid/.targetType/.status`, `targeting.value` and `targetingMatchType.value`, and no `target.value`; `target.value` is in the migration examples (twice in the spSearchTerm one) and in New features' warning example with `PENDING_DEPRECATION`. This agrees with method/reporting.md §H. B3 and the run-time list now name the library fields first; Stable 27 and P-61 added. Whether the service still accepts `target.value` stays open (Open question 3).
3. **SB negative paths (owner method/ads-api-surface.md).** Parsed all three SB models. `/sb/negativeKeywords` and `/sb/negativeTargets` are on the YAML "Amazon Ads API - Sponsored Brands 3.0" model (ads-api-surface §I is right). The JSON file `SponsoredBrands_prod_3p.json`, also titled "Sponsored Brands 3.0", carries the SB 4.0 path set plus two recommendation paths and holds `/sb/negativeTargets/brands/recommendations` but no `/sb/negativeKeywords` (this file's earlier sentence was right about that file, but read it as "the" SB 3.0 model). The SB 4.0 model also holds `/sb/negativeTargets/brands/recommendations` (keyword-targeting and brand-defense are right). C7's sentence replaced by a three-model table; the SB guide's "negative keyword recommendations" link was found to point at `listNegativeKeywords`, not a recommendation path. Stable 25 and P-55 added.
4. **Position and conversion rate (owner areas/bids-and-placements.md).** Re-read the four abstracts through OpenAlex. Rutz, Bucklin & Sonnier: "higher positions increase both the click-through and conversion rates" (instrumental variables, one lodging chain). Ghose & Yang: "conversion rates are highest at the top and decrease with rank" (one retailer, Google). Agarwal, Hosanagar & Smith: "conversion rate increases with position" counting down the page (field experiment, one retailer). Narayanan & Kalyanam: simple comparisons are biased by auction selection; RD effects "much smaller, and exist only in some of the positions". The three findings are each true of their own data; none is on Amazon. R5's bullet now quotes the abstract, R5b adds the table and the reconciliation, P-62 added. P-39 is unchanged (it states sparsity, endogeneity and the keyword-list result, not a direction).

Declined: none. Narrowings of a gap's premise are stated in items 2 and 3 above.
