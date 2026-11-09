# Reporting: types, lifecycle and a report reader

Read 2026-11-09 by the research seat.

Tags:
- [official]: Amazon's own words. That covers the Amazon Ads API guides and OpenAPI models, release notes, deprecation notices, Amazon Ads library pages, and the SP-API models and guides.
- [opinion]: a named practitioner, agency, tool vendor or developer, stated as theirs.
- [research]: published research.
- [seat]: the seat's own reasoning. It is allowed here but is never a position.

Every Ads API guide below was read on 2026-11-09 as Markdown from the documentation's own content host, `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`. A plain GET of the pages at `https://advertising.amazon.com/API/docs/en-us/<path>` returns only a JavaScript shell. The host's own `llms.txt` says so: "This site is a client-side rendered React app ... All documentation content is available as raw markdown files on the CDN". The URL given for each page is the `advertising.amazon.com` address a person would open; the text is the CDN copy.

The two OpenAPI models read are served from `https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/`. The v1 reports model answered `last-modified: Sun, 08 Nov 2026 09:20:19 GMT`.

Figures marked **(for human readers only)** are recorded with their page and date so that a person can check them. A skill reads the live page or Amazon's reply at run time instead of the figure.

## What this covers

**The part of a seller's ad work.** This file owns no task of its own. It is plumbing under every other file. Every number a senior Amazon advertising lead acts on reaches cx through an asynchronous report or a pushed dataset: spend by campaign, the search terms that converted, the placement split, the advertised and the "other" ASINs that sold, invalid clicks, impression share.

This file owns:
- which report types and fields exist on each surface;
- how a report is asked for, waited on, downloaded and read;
- how long Amazon keeps the data, and how far back one ask may reach;
- when a day's numbers stop moving, and which time zone a "day" is;
- how ad rows join SP-API rows;
- the facts a report-reader script rests on, for Reporting v3 and for Reporting v1. The reader creates the report, polls to a terminal status under a ceiling, downloads it, decompresses it, lands it beside a receipt, and reuses a landed report of the same ask.

**Why a senior lead cares.** Most bad ad decisions on Amazon are reading errors before they are strategy errors:
- A "last 7 days" ACOS is judged while the last few days' conversions are still arriving and being restated.
- A search-term report is taken as "all the terms we showed on", but the API version holds only terms that got a click.
- A v1 `metric.sales` is compared with a v3 `sales14d` for a seller account, but v1's base metric is the seller's 7-day figure.
- A day of ad spend is set beside a day of Business Report sales, on two different clocks.
- A report asked for twice answers `425`, or polling runs into `429`, and either is read as "Amazon is down".
- A `null` is read as zero, an `(Other)` row is read as a search term, or a halo sale is read as a sale of the advertised ASIN.

The v3 sunset on 2027-06-30 makes this urgent. Anything written against `POST /reporting/reports` stops working that day. The replacement changes field names, attribution-window conventions, account identifiers and rate-limit scope all at once.

**Cross-references (the topic is theirs, not this file's).**
- `beyond/metrics-and-attribution.md` owns what each metric means as a business measure: ACOS, ROAS, TACoS, NTB, halo, view-through, and attribution windows as concepts. This file records only the field names, windows and definitions as they bear on reading a report.
- `method/ads-api-surface.md` owns hosts, authorisation, profiles, account ids, campaign-management paths and the door. This file records only what reporting needs from them.
- `method/change-measurement.md` owns before/after reading of a change. This file supplies when a day is final and what restatement does to a window.
- `areas/search-terms-and-negatives.md` owns harvesting. This file owns the search-term report's shape and its click-only rule.
- `areas/ads-organic-and-total.md` owns ads against organic and total. This file owns the join keys and clocks between the Ads reports and SP-API reports.
- `areas/diagnosis.md` owns why spend or sales moved. This file supplies which report answers which question.
- `areas/bids-and-placements.md`, `areas/budgets-and-pacing.md`, `areas/keyword-and-product-targeting.md`, `areas/campaign-structure.md`, `areas/launch.md` and `areas/seasons-and-deals.md` read the reports described here.
- `beyond/automation-and-amazon-tools.md` owns Amazon's own agent and MCP tools as tools. This file notes only their reporting operations.
- `beyond/ad-products-and-eligibility.md` owns which ad products a seller may run. This file notes only which report types exist per product.
- `beyond/goals-and-economics.md` and `beyond/brand-defense-and-competition.md` consume the joins in section O.

## Amazon's own rules and guidance

RULE marks something Amazon enforces: an API shape, an enum, a limit, a retention, a deprecation. GUIDANCE marks a recommendation. Where Amazon's own pages disagree, both are quoted and the disagreement is named.

### A. The surfaces and their dates

- RULE. Amazon's reporting overview lists the programmatic surfaces and their state. Verbatim in the load-bearing parts:
  - "Amazon Marketing Stream (Version 2) — Complete advertising datasets delivered to your S3 bucket as Parquet files, with updates as frequent as every 15 minutes. Provides full reporting API v1 parity with total values, automated backfill up to 70 days on subscription creation, and no polling/throttling."
  - "Reporting API v1 — A new ad-hoc programmatic interface ... Combine any dimensions in a single request without selecting a report type."
  - "v3 reporting (Amazon Ads API) — **To be shutoff after June 30, 2027.** Daily and summary performance reports for sponsored ads and Amazon DSP campaigns."
  - "Amazon Marketing Stream (Version 1) — **To be shutoff after June 30, 2027.** Hourly delta-based traffic, conversion, and budget usage data delivered to Firehose or SQS."
  - "Version 2 reporting (sponsored ads) — **To be shutoff after June 30, 2027.** 1-day performance reports for sponsored ads campaigns."
  - "Amazon DSP reporting — **To be shutoff after June 30, 2027.** Performance reports for Amazon DSP campaigns."
  - Amazon Attribution (beta), Amazon Brand Metrics (beta) and Marketing Mix Modeling are listed alongside.

  [official] (Amazon Ads reporting overview, https://advertising.amazon.com/API/docs/en-us/guides/reporting/overview, read 2026-11-09)
- RULE. The deprecation notice is titled "September 2026 - Deprecation of Amazon Marketing Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting". It says:
  - "All v3 reporting endpoints and associated report types are also deprecated, including Sponsored Products, Sponsored Brands, Sponsored Display, and Amazon DSP report types available through `POST /reporting/reports`."
  - "**Hard shutoff date:** Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting will stop delivering data on June 30, 2027."
  - "The Exports API for campaign metadata is not affected."
  - Stream v1's messaging data (entity state changes, budget consumption) moves to the Campaign Management API, and its recommendation data moves to the Recommendations API: "These features are not carried forward in Stream v2."

  [official] (Deprecations, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations, read 2026-11-09)
- RULE. Two earlier shutoffs inside the reporting area, from the same page (both entries are headed October 2026):
  - Sponsored Brands Category Benchmark APIs: "Existing integrations will continue to function through December 17, 2026". The replacement is benchmark metrics in Unified Reporting (`POST /adsApi/v1/create/reports`), and "the Benchmark v3 reporting API is also on the deprecation path."
  - `searchTermImpressionRank` and `searchTermImpressionShare` in Sponsored Brands v2 reports (`/v2/hsa/keywords/report`) "will stop returning values ... on November 10, 2026". The replacements are `metric.impressionShare` and `metric.impressionShareRank`.

  [official] (Deprecations, above)
- RULE, the GA date. "Amazon Marketing Stream v2 and the new Reporting API now generally available" is dated September 30, 2026. [official] (Amazon Ads API v1 release notes, https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v1, read 2026-11-09)
- RULE, Version 2 reporting. Its own page has two notices:
  - "Sponsored Ads v2 reporting API will be deprecated on June 30, 2027."
  - "As of March 30, 2023, Sponsored Products reports are no longer supported in version 2."

  The page also says "each call to the API requests a single day of data" and "Reporting data is only available up to 60 days back from the current date via the API." [official] (Version 2 reporting overview, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v2/overview, read 2026-11-09)
- Naming. Amazon calls the new surface "Reporting API v1", "the new reporting API", "Unified Reporting" and, once, "Unified Reporting (v4 reporting API)" (in the October 2026 entry deprecating Sponsored Brands v2 `searchTermImpressionRank` and `searchTermImpressionShare`). All of these name `POST /adsApi/v1/create/reports`. [official] (Deprecations; Overview of the Reporting v1 API, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/overview; both read 2026-11-09)
- GUIDANCE, which surface for what. Amazon's table:
  - Stream v2 is for "Build responsive applications", "Intraday optimization", "Real-time dashboards", "Large-scale reports", "AI and predictive modeling" and "Simplify infrastructure".
  - Reporting API v1 is for "Predefined stakeholder-ready reports" and "Periodic or scheduled reporting".
  - "Ads Console Reports" are for "Interactive data exploration".

  The page also says: "Amazon Marketing Stream Version 2 is the primary programmatic reporting surface for Amazon Ads, built for reporting at scale in the agentic era." [official] (Amazon Ads reporting overview, above)
- RULE, reports against exports. "Reports include performance data like impressions or clicks for a chosen report type. Exports contain campaign metadata like budget or status." "While reports can include certain metadata, we recommend requesting any metadata using the export resource for improved performance." [official] (Amazon Ads reporting overview, above)

### B. Reporting v3: the call sequence and the model

- RULE, the call sequence. Three calls: "1. Request a report 2. Wait for report to generate 3. Download the report." All requests use "a single endpoint: `POST /reporting/reports`".
  - Headers: `Amazon-Ads-ClientId` (the OpenAPI model names this header `Amazon-Advertising-API-ClientId`, required); `Authorization`; `Amazon-Advertising-API-Scope` (the profile id, with "the correct base URL ... for the marketplace associated to the profile"); and `Content-Type: application/vnd.createasyncreportrequest.v3+json`.
  - `Amazon-Ads-AccountId` is described as "Required for reporting requests across all ad products including ADSP, Sponsored Products, Sponsored Brands, and Sponsored Display". Yet the same page's sample call sends only the scope header.

  [official] (Get started with version 3 reports, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/get-started, read 2026-11-09)

  The OpenAPI model lists two authorised resource types: `Amazon-Advertising-API-Scope` ("Global Ad Account ID, Profile ID") and `Amazon-Ads-AccountId` ("DSP Rodeo Entity ID, DSP Advertiser Account ID"). That reads as the scope header for sponsored ads and the account header for DSP. The model marks `Amazon-Advertising-API-Scope` `required: false` and describes `Amazon-Ads-AccountId` as "Optional", against the guide's "Required". [official] (OfflineReport_prod_3p.json, "Offline Report 3.0", `createAsyncReport`, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/OfflineReport_prod_3p.json, read 2026-11-09)

  The door attaches the client-id header itself and refuses a request that names it (`cx-amazon-ads` `references/door.md`).
- RULE, the request body (model `CreateAsyncReportRequest`, `AsyncReportConfiguration`):
  - Top level:
    - `startDate` and `endDate` are required: "YYYY-MM-DD format. The maximum lookback window supported depends on the selection of reportTypeId. Most report types support `95 days` as lookback window."
    - `name` is optional.
    - `configuration` is required.
  - Inside `configuration`:
    - `adProduct`: enum `ALL`, `DEMAND_SIDE_PLATFORM`, `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS`, `SPONSORED_TELEVISION`.
    - `reportTypeId`.
    - `groupBy`: "cannot be null or empty".
    - `columns`: "This list cannot be null or empty".
    - `timeUnit`: enum `DAILY`, `SUMMARY`.
    - `format`: the model's enum is `GZIP_JSON` only.
    - `filters`: optional list of `{field, values[]}`.
  - The model marks `adProduct`, `columns`, `format`, `groupBy`, `reportTypeId` and `timeUnit` all required inside `configuration`.

  [official] (OfflineReport_prod_3p.json, above)
- RULE, `timeUnit` and the date columns. "If you set `timeUnit` to `DAILY`, you should include `date` in your column list. If you set `timeUnit` to `SUMMARY` you can include `startDate` and `endDate` in your column list." [official] (Get started with version 3 reports, above)
- RULE, `groupBy` and filters.
  - "All report requests require the `groupBy` parameter ... If supported for the report type, you can use multiple `groupBy` values in a request."
  - "You can only use a filter that is supported by **all** `groupBy` values included in a report configuration."
  - For campaign reports, "this means that filters are only supported when you include a single `groupBy` value."

  [official] (Get started with version 3 reports; Campaign reports, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/campaign; both read 2026-11-09)
- RULE, the create reply. "A successful request results in a `200` response that includes the requested report configuration, a `reportId`, and a `status`." The model's other answers to `POST /reporting/reports` are:
  - `400` Bad Request;
  - `401`;
  - `422`: "Unprocessable entity - Failed due to invalid parameters";
  - `425`: "Too Early - Request is a duplicate of a processing request";
  - `429`: "Too Many Requests - Request was rate-limited. Retry later";
  - `500`.

  The error body (`AsyncReportingError`) has `code` ("The HTTP status code of the response") and `detail` ("A human-readable description of the response"). [official] (Get started with version 3 reports; OfflineReport_prod_3p.json; both above)
- RULE, the report record (`AsyncReport`).
  - Required: `reportId`, `status`, `configuration`, `startDate`, `endDate`, `createdAt`, `updatedAt`.
  - Optional:
    - `name`;
    - `generatedAt`;
    - `fileSize`: "The size of the report file, in bytes";
    - `url`: "URL of the generated report";
    - `urlExpiresAt`: "The date at which the download URL for the generated report expires. urlExpires at this time defaults to 3600 seconds but may vary in the future.";
    - `failureReason`: "Present for failed reports only".

  [official] (OfflineReport_prod_3p.json, above)
- RULE, statuses. The model's enum is `COMPLETED`, `FAILED`, `PENDING`, `PROCESSING`:
  - "`PENDING` - Report is created and awaiting processing."
  - "`PROCESSING` - Report is processing. Please wait."
  - "`COMPLETED` - Report has completed. Check the `url` for the output file."
  - "`FAILED` - Report generation failed. Check the `failureReason` for details."

  The guide adds: "Any successful call to the `GET` status endpoint returns a `200` status code. To check if report generation has completed, check the `status` parameter in the response body." [official] (OfflineReport_prod_3p.json; Get started with version 3 reports; both above)
- RULE, the other two operations.
  - `GET /reporting/reports/{reportId}` (`getAsyncReport`) answers `200`, `400`, `401`, `404`, `429` or `500`.
  - `DELETE /reporting/reports/{reportId}` (`deleteAsyncReport`): "Use this operation to cancel a report in a `PENDING` status."

  [official] (OfflineReport_prod_3p.json, above)
- RULE, the download.
  - "Once your report is ready, the `url` field of a `GET reporting/reports/{reportId}` contains a link to the S3 bucket where you can download your report."
  - "Once you decompress your report file, you can see the raw JSON for the report." The file is a JSON array of row objects keyed by column name. The sample rows carry `campaignId` as a JSON number, e.g. `158410630682987`.
  - "Most report types are available for download in a compressed (gzip) format. Once unzipped, report data is in a JSON format."

  [official] (Get started with version 3 reports; Sponsored ads reporting overview (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/overview; both read 2026-11-09)

  [seat] An id as large as `158410630682987` is still exact in an IEEE double (below 2^53). `jq` 1.7 keeps the literal, but a tool that parses it as a float and then prints it may change its format. The ids are safer joined as strings.
- GUIDANCE, joining metadata. "To get campaign metadata, request an export, then join the two datasets using `campaignId`." [official] (Get started with version 3 reports, above)

### C. Reporting v3: report types per ad product

RULE, Amazon's availability table. An empty cell means not offered.
- Ad: SB.
- Ad group: SB, SD.
- Advertised product: SP, SD.
- Benchmarks: ALL.
- Campaign: SP, SB, SD, ST, DSP.
- Gross and invalid traffic: SP, SB, SD.
- Placement: SB.
- Prompt Ad Extension: SP, SB.
- Purchased product: SP, SB, SD.
- Search term: SP, SB.
- Targeting: SP, SB, SD, ST.
- Video Ad Extension: SP.
- DSP only: Audience, Audio and video (beta), Bid adjustments, Brand suitability, Geo, Inventory, Product, Reach and frequency, Tech.
- All products: Conversion Path.

[official] (Sponsored ads report types (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/overview, read 2026-11-09)

RULE, configurations of the sponsored-ads types. Each row is Amazon's own table on the type's page, read 2026-11-09. Retention and range figures are **(for human readers only)**. A reader takes them from the type's page or from Amazon's refusal.

| Type | `reportTypeId` | Max range | Retention | `groupBy` | Filters | `format` (page) |
|---|---|---|---|---|---|---|
| SP campaign | `spCampaigns` | 31 d | 95 d | `campaign`, `adGroup`, or `campaignPlacement` | `campaignStatus` (campaign); `adStatus` (adGroup); `campaignSite` = `AmazonBusiness` (campaignPlacement) | `GZIP_JSON` |
| SB campaign | `sbCampaigns` | 31 d | 60 d | `campaign` | `campaignStatus` | `GZIP_JSON` |
| SD campaign | `sdCampaigns` | 31 d | 65 d | `campaign` or `matchedTarget` | none | `GZIP_JSON` |
| ST campaign | `stCampaigns` | 31 d | 95 d | `campaign` or `adGroup` | `campaignStatus`; `adStatus` | `GZIP_JSON` |
| SB ad group | `sbAdGroup` | 31 d | 60 d | `adGroup` (the page also has an SB "Group by `campaign`" section) | `adStatus` | `GZIP_JSON` |
| SD ad group | `sdAdGroup` | 31 d | 65 d | `adGroup` or `matchedTarget` | none | `GZIP_JSON` |
| SB ad | `sbAds` | 31 d | 60 d | `ads` | `adStatus` | `GZIP_JSON` |
| SB placement | `sbCampaignPlacement` | 31 d | 60 d | `campaign` (page also lists `campaignPlacement`) | — | `GZIP_JSON` |
| SP targeting | `spTargeting` | 31 d | 95 d | `targeting` | `adKeywordStatus`; `keywordType` | `GZIP_JSON` |
| SB targeting | `sbTargeting` | 31 d | 60 d | `targeting` | `adKeywordStatus`; `keywordType` (adds `THEME`) | `GZIP_JSON` |
| SD targeting | `sdTargeting` | 31 d | 65 d | `targeting`, `matchedTarget` | none | `GZIP_JSON` |
| ST targeting | `stTargeting` | 31 d | 95 d | `campaign`, `adGroup`, or `targeting` | status filters | `GZIP_JSON` |
| SP search term | `spSearchTerm` | 31 d | 65 d | `searchTerm` | `keywordType` | `GZIP_JSON` |
| SB search term | `sbSearchTerm` | 31 d | 60 d | `searchTerm` | `keywordType` | `GZIP_JSON` |
| SP advertised product | `spAdvertisedProduct` | 31 d | 95 d | `advertiser` | `adCreativeStatus` | `GZIP_JSON` |
| SD advertised product | `sdAdvertisedProduct` | 31 d | 65 d | `advertiser` | none | `GZIP_JSON` |
| SP purchased product | `spPurchasedProduct` | 31 d | 95 d | `asin` | none | `GZIP_JSON` |
| SB purchased product | `sbPurchasedProduct` | 731 d | 731 d | `purchasedAsin` | none | `GZIP_JSON` |
| SD purchased product | `sdPurchasedProduct` | 31 d | 65 d | `asin` | none | `GZIP_JSON` |
| Gross and invalid traffic | `spGrossAndInvalids`, `sbGrossAndInvalids`, `sdGrossAndInvalids` | 365 d | 365 d | `campaign` | `campaignStatus` | `GZIP_JSON` or `CSV` |
| Prompt ad extension | `spPromptAdExtension`, `sbPromptAdExtension` | 90 d | 95 d | `promptAdExtension` | `marketplaceId` = `US` | `GZIP_JSON` or `XLSX` |
| Video ad extension | `spVideoAdExtension` | 90 d | 95 d | `videoAdExtension` | `marketplaceId` = `US` | `GZIP_JSON` or `XLSX` |
| Sponsored ads benchmarks | `crossProgramBenchmarks` | 456 d (monthly, weekly); 90 d (daily) | 456 d | `brandCategoryBenchmarks` | — | `CSV` or `GZIP_JSON`; `timeUnit` `DAILY`, `WEEKLY`, `MONTHLY` (the model's `timeUnit` enum is `DAILY`, `SUMMARY` only) |
| Conversion path | `conversionPath` | 90 d | 95 d | `brandConversionPath` | — | `CSV` or `GZIP_JSON`; `timeUnit` `SUMMARY`; brand owners only |
| SP audience (bid boost) | `spAudiences` | 31 d | 95 d | `campaign_bid_boost_segment` | none | `GZIP_JSON` or `XLSX`; `timeUnit` `SUMMARY` or `DAILY` |
| SB audience (bid boost) | `sbAudiences` | 31 d | 95 d | `campaign_bid_boost_segment` | none | `GZIP_JSON` or `XLSX`; `timeUnit` `SUMMARY` or `DAILY` |

[official] (all under https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/, read 2026-11-09):
- Campaign reports, …/report-types/campaign
- Ad group reports, …/report-types/ad-group
- Ad reports, …/report-types/ad
- Placement reports, …/report-types/placement
- Targeting reports, …/report-types/targeting
- Search term reports, …/report-types/search-term
- Advertised product reports, …/report-types/advertised-product
- Purchased product reports, …/report-types/purchased-product
- Gross and invalid traffic reports, …/report-types/gross-and-invalid-traffic
- Prompt Ad Extension reports, …/report-types/prompt-ad-extension
- Video Ad Extension reports, …/report-types/video-ad-extension
- Benchmarks reports, …/report-types/benchmarks
- Conversion path reports, …/report-types/conversion-path
- Audience reports, …/report-types/audience

RULE and notes that bind a reader:
- **Audience bid-boost reports (`spAudiences`, `sbAudiences`).** Amazon's availability table on the report-types overview marks the Audience row for Amazon DSP only. The Audience reports page itself has three columns, "Amazon DSP | Sponsored Products | Sponsored Brands", with `reportTypeId` `dspAudience`, `spAudiences` and `sbAudiences`. For SP and SB the page gives: maximum range 31 days, retention 95 days, `timeUnit` `SUMMARY` or `DAILY`, `groupBy` `campaign_bid_boost_segment`, `format` `GZIP_JSON` or `XLSX`, and under the group-by "Additional metrics: segmentName Filters: None".
  - SP base metrics: `campaignId, segmentName, segmentClassCode, impressions, clicks, cost, spend`, the `purchases`, `purchasesSameSku`, `unitsSoldClicks`, `sales`, `attributedSalesSameSku` and `unitsSoldSameSku` columns at 1, 7, 14 and 30 days, `date, startDate, endDate, campaignBiddingStrategy, costPerClick, clickThroughRate, campaignName, campaignStatus, campaignBudgetAmount, campaignBudgetType, marketplaceId`.
  - SB base metrics: `campaignId, segmentName, impressions, clicks, cost, spend, purchases, sales, salesClicks, unitsSold, unitsSoldClicks, date, startDate, endDate, costPerClick, clickThroughRate, campaignName, campaignStatus, campaignBudgetAmount, campaignBudgetType, marketplaceId, segmentClassCode`.
  - Both sample requests send `"format": "XLSX"`, a value outside the OpenAPI model's `GZIP_JSON`-only enum (the format disagreement below). The model's `reportTypeId` is a free string ("The identifier of the Report Type to be generated"), not an enum, so the availability table is the only list and it omits these two.
  - The columns page defines `segmentName` as "The name of the audience segment" and `segmentClassCode` as "The class of the segment, for example behavioral or user agent". It lists their report types as `dspAudience`, `spGlobalAudiences` and (for `segmentName`) `sbAudiences`: a third name, `spGlobalAudiences`, where the type page and the usage example say `spAudiences`.
  - The release note "Audience bid boosting reports now supported for Sponsored Products and Sponsored Brands" is dated January 24, 2025 and points to the Audience report type page. Later entries (Sponsored Products preview of Amazon-built audiences, March 12, 2025; Sponsored Brands "New-to-brand shoppers", March 24, 2025; two more Sponsored Brands audiences, August 22, 2025) direct advertisers to the same report "To assess the performance of their bid boosted audiences".
  - Amazon's usage example "Sponsored Products & Brands: Audience Bid Boosting" repeats the two configurations and adds that the console shows the same data under the campaign's "Bid Adjustments" section, "Audiences" tab.
  - No v1 or Stream v2 equivalent is mapped. The Reporting API v3 Report Type Migration Guide has no `spAudiences`, `sbAudiences` or `dspAudience` section, and the `ads-performance-v1` dataset lists no audience dimension. Reporting v1 has an Audience segment dimension (`audienceSegment.id`, the primary key, requiring `audienceSegment.classCode`, `.name`, `.source`, `.type` and `audienceSegmentCountry.code`), whose "Ad Product availability" for the id is Sponsored Products, Sponsored TV and Amazon DSP, not Sponsored Brands, and whose "Version 3 Reporting Name (Sponsored Ads)" is "N/A". `metric.clicks`, `metric.impressions`, `metric.purchases`, `metric.sales` and `metric.totalCost` list Audience segment among their compatible dimensions. Helpful concepts names two of its incompatibilities: "The `convertedProduct` dimension is incompatible with the `audienceSegment` dimension" and "The `audienceSegment` dimension is incompatible with the `supplySource` dimension". Whether `audienceSegment.*` in a Sponsored Products row is the bid-boost segment of `spAudiences` is not stated.

  [official] (Audience reports, …/report-types/audience; Sponsored ads report types (version 3); Reporting columns (version 3); OfflineReport_prod_3p.json; Release notes index, https://advertising.amazon.com/API/docs/en-us/release-notes/index; Sponsored Products & Brands: Audience Bid Boosting, https://advertising.amazon.com/API/docs/en-us/knowledge-hub/blogs/usage-examples/2026-01-sp-sb-bid-boosting; Reporting API v3 Report Type Migration Guide; Ads performance dataset; Audience segment, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/audience/audience-segment; Helpful concepts; Clicks, Impressions, Purchases and Costs metric pages; all read 2026-11-09)
- **Format disagreement.** The type pages list `CSV` for gross-and-invalid and benchmarks, and `XLSX` for the extension reports. The OpenAPI model's `format` enum is `GZIP_JSON` only. The v3 FAQ still says "Support for CSV files coming soon." The v1 migration pages' v3 examples send `"format": "CSV"`. [official] (type pages above; OfflineReport_prod_3p.json; Sponsored ads reporting FAQ (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/faq; all read 2026-11-09)
- **No SP ad-group or SP placement type.**
  - "For Sponsored Products, there is not a separate ad group report. You can get ad group-level data using the ad group `groupBy` in a campaign report."
  - "For Sponsored Products, there is not a separate placement report. You can get placement-level data using the `campaignPlacement` `groupBy` in a campaign report."
  - "Grouping by campaignPlacement will generate the same report as grouping by campaign and campaignPlacement."

  [official] (Ad group reports; Placement reports; Campaign reports; all above)
- **Amazon Business.** This applies to `spCampaigns` grouped by `campaignPlacement` with the filter `campaignSite` = `AmazonBusiness`: "Amazon Business performance data is available starting 9/5/2024 onwards only." [official] (Campaign reports, above)
- **Keywords against targets.** "To see only targeting expressions, set the `keywordType` filter to `TARGETING_EXPRESSION` and `TARGETING_EXPRESSION_PREDEFINED`. To see only keywords, set the `keywordType` filter to `BROAD`, `PHRASE`, and `EXACT`." [official] (Targeting reports, above)
- **Search terms.**
  - "Note that search term reports only include impressions that resulted in at least one ad click."
  - "If a placement does not have a search keyword associated with it on a product detail page, the search term in the report will be an asterisk `*`."

  [official] (Search term reports, above). Harvesting from this report belongs to `areas/search-terms-and-negatives.md`.
- **Purchased product.**
  - Sponsored Products: "Sponsored Products purchased product reports contain performance data for products that were purchased, but were not advertised as part of a campaign. The purchased product report contains both targeting expressions and keyword IDs."
  - Sponsored Brands instead "contain[s] performance data for products that were purchased as a result of your campaign". It carries `attributionType`: "Describes whether a purchase is attributed to a promoted product or brand-halo effect".

  [official] (Purchased product reports; Reporting columns (version 3), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/columns; both read 2026-11-09)
- **Gross and invalid traffic.** The report "provides ... transparency into the nature of traffic on their campaigns ... at campaign level". Its base metrics are `campaignName, campaignStatus, clicks, date, endDate, grossClickThroughs, grossImpressions, impressions, invalidClickThroughRate, invalidClickThroughs, invalidImpressionRate, invalidImpressions, startDate`. [official] (Gross and invalid traffic reports, above)
- **Campaigns with no activity.** "Campaign reports include all campaigns of the requested sponsored ad type that have performance activity for the requested days ... all Sponsored Products campaigns that received impressions on the chosen dates." A campaign absent from the report had no impressions in the range. Whether it exists is read from an export or a list call. [official] (Campaign reports, above)
- **Sponsored Brands preview.** "Sponsored Brands reports are currently available in preview. During the preview period, data related to Sponsored Brands campaigns with flag `isMultiAdGroupsEnabled=False` will not be available." On 2026-11-09 this note is still on every SB type page and on the overview. [official] (Sponsored ads reporting overview (version 3); Sponsored ads report types (version 3); both above)
- **Prompt ads.** "Prompts are a new ad format that integrates into your existing Sponsored Products and Sponsored Brands campaigns with zero additional setup required ... Prompts with clicks will show in your existing Sponsored Products or Sponsored Brands reporting." [official] (Prompt Ad Extension reports, above)
- **Video ad extensions.** "the `campaignId`, `adGroupId`, and `adId` values in this report match the values in your other Sponsored Products reports. A single ad can serve as either video or image depending on the placement." [official] (Video Ad Extension reports, above)
- **Benchmarks.** "You must be a brand owner or representative on Amazon Stores to be eligible for benchmarks reporting." "Benchmarks are available starting from January 1, 2025 and update every 48 hours." [official] (Benchmarks reports, above)

RULE, the SP base columns. The same family recurs across `spCampaigns`, `spTargeting`, `spSearchTerm` and `spAdvertisedProduct`:
- Every one carries:
  - `impressions, clicks, cost, costPerClick, clickThroughRate` (`spend` is listed for `spCampaigns` and `spAdvertisedProduct`, not for `spTargeting` or `spSearchTerm`);
  - `purchases{1,7,14,30}d` and `purchasesSameSku{1,7,14,30}d`;
  - `unitsSoldClicks{1,7,14,30}d`;
  - `sales{1,7,14,30}d` and `attributedSalesSameSku{1,7,14,30}d`;
  - `unitsSoldSameSku{1,7,14,30}d`;
  - Kindle columns and `addToList`.
- Targeting, search-term and advertised-product reports also carry `salesOtherSku7d, unitsSoldOtherSku7d, acosClicks7d, acosClicks14d, roasClicks7d, roasClicks14d`.
- `spCampaigns` grouped by `campaign` adds `campaignBudgetAmount`, `campaignBudgetType`, `campaignRuleBasedBudgetAmount`, `campaignApplicableBudgetRuleId`, `campaignApplicableBudgetRuleName`, `campaignBudgetCurrencyCode` and `topOfSearchImpressionShare`.
- `spTargeting` carries `keywordId, keyword, keywordBid, keywordType, matchType, targeting, topOfSearchImpressionShare`.
- `spSearchTerm` adds `searchTerm`.

[official] (Campaign reports; Targeting reports; Search term reports; Advertised product reports; all above)

RULE, where `topOfSearchImpressionShare` is offered. The two kinds of page list it differently:
- The type pages list it for `spCampaigns` grouped by `campaign` and also grouped by `campaignPlacement`; for `sbCampaigns` in its base metrics and again under "Group by `campaign`"; for `spTargeting` in its base metrics; and for `sbTargeting` in its base metrics.
- The columns page's "Report types" line for the column is "spCampaigns, sbCampaigns, sbTargeting". It omits `spTargeting`, which the Targeting reports page lists.
- The Reporting API v3 Report Type Migration Guide maps `topOfSearchImpressionShare` to v1 `metric.topOfSearchImpressionShare` under `spCampaigns`, `spTargeting`, `sbCampaigns` and `sbTargeting`. Section H shows that the v1 metric page makes it incompatible with the Target and Targeting dimensions.

[official] (Campaign reports; Targeting reports; Reporting columns (version 3); Reporting API v3 Report Type Migration Guide; all read 2026-11-09)

### D. Reporting v3: column definitions a reader depends on

RULE, Amazon's definitions, verbatim (Reporting columns (version 3), above):
- `purchases7d`: "Number of attributed conversion events occurring within 7 days of an ad click." `purchases14d`: "... within 14 days of an ad click."
- `sales7d`: "Total value of sales occurring within 7 days of an ad click." `sales14d`: "Total value of sales occurring within 14 days of an ad click. Includes sales attributed to both clicks and views for `vCPM` campaigns, but only sales attributed to clicks for `CPC` campaigns."
- `salesOtherSku7d`: "... where the purchased `SKU` was different from the `SKU` advertised."
- Sponsored Brands (and Sponsored Display) `purchases`: "Number of attributed conversion events occurring within 14 days of an ad click or view." `sales`: "Total value of sales occurring within 14 days of an ad click or view." `purchasesClicks`: "... within 14 days of an ad click."
- `cost` and `spend`: both "Total cost of ad clicks." `clicks`: "Total number of clicks on an ad." `impressions`: "Total number of ad impressions."
- `clickThroughRate`: "Clicks divided by impressions." `costPerClick`: "Total cost divided by total number of clicks." `acosClicks14d`: "Advertising cost of sales based on purchases made within 14 days of an ad click."
- `date`: "Date when the ad activity ocurred in the format YYYY-MM-DD." `startDate`: "Start date of summary period for a report in the format YYYY-MM-DD." `endDate`: "End date of summary period for a report in the format YYYY-MM-DD."
- `topOfSearchImpressionShare`: "The percentage of top-of-search impressions earned out of all the top-of-search impressions that were eligible for a given date range. Various factors determine the eligibility for an impression including campaign status and targeting status."
- `placementClassification`: "The page location where an ad appeared."
- `keywordType` / `matchType`: "For keywords, one of: BROAD, PHRASE, or EXACT. For Sponsored Products reports, keywordType can also contain the type of targeting expressions, one of: TARGETING_EXPRESSION or TARGETING_EXPRESSION_PREDEFINED." The page adds: "The Amazon Ads Console uses "-" in place of `TARGETING_EXPRESSION` or `TARGETING_EXPRESSION_PREDEFINED` in generated reports."
- `advertisedAsin` and `purchasedAsin`: "The `ASIN` or retailer offer ID ... This value may differ in format and length from a standard 10-character `ASIN`."
- `grossImpressions`: "includes valid and invalid impressions such as potentially fraudulent, non-human, and other illegitimate impressions." `invalidClickThroughs`: "Clicks that were removed by the traffic quality filter."

GUIDANCE, the bulksheet page's definitions.
- Amazon's bulksheets search-term page defines Click-through Rate as "calculated as impressions divided by clicks".
- The same page defines Conversion Rate as "The total number of orders divided by sales".
- The console-against-API page (version 2) also gives SP and SD Click-Thru Rate as "impressions divided by clicks", and SP "Total Advertising Cost of Sales (ACoS)" as `cost` divided by `attributedSales14d`.
- The v3 columns page has CTR the right way round. Rates recomputed from the counts do not depend on either page's wording.

[official] (Search term reports in bulksheets, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-search-term-report; Reporting in the advertising console vs. API (version 2), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v2/advertising-console; Reporting columns (version 3); all read 2026-11-09)

### E. Reporting v3: generation time, duplicates, throttling, cadence

- RULE. "Once you have made a successful `POST` call, report generation can take up to three hours. Note that if you make duplicate requests to create a report with identical parameters, you will see a status code of `425`, indicating that it is too soon to make the additional request. If this happens, you should wait for your existing request to complete before making another request." [official] (Get started with version 3 reports, above)
- RULE. "Report generation can take as long as three hours. Repeated calls to check report status may generate a `429` response, indicating that your requests have been throttled. To retrieve reports programmatically, your application logic should institute a delay between requests." [official] (same page; Sponsored ads reporting FAQ (version 3), above)
- Disagreement on generation time.
  - Amazon's service-limits table, under "P99 Guarantee", gives "Async report generation time | 15m". Beside it are "Impression/click event to availability via API | 12h" and "Impression/click invalidation | 72h".
  - The reporting guides say "up to three hours". **(for human readers only)**

  [official] (Limits, constraints, and quotas, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, read 2026-11-09)
- RULE, `429` and `Retry-After`. "When this happens, you will receive a response with the code `429`. Contained within that response is a `Retry-After` header. The `Retry-After` value is the number of seconds that you should wait before submitting another API call. Rate limiting will occur dynamically based on the overall system load." [official] (Rate limiting, https://advertising.amazon.com/API/docs/en-us/reference/concepts/rate-limiting, read 2026-11-09)
- RULE, how report limits move. "Rate limits associated with the Sponsored Ads reporting API, Sponsored Display reports API, and the Sponsored Brands reports API depend on the size of the report generation queue. These limits are determined on a per-region basis with multiple limit tiers that correspond to the current reporting queue size in a given region. Higher utilization periods with higher report queue sizes result in lower rate limits." "Dynamic rate limits are unlikely to change over short time periods. Therefore, choose longer backoff periods for report generation." [official] (Rate limiting, above)
- GUIDANCE, retries.
  - "In general, you should retry requests that receive server or throttling errors."
  - For a "Client error: The HTTP response is a 400-level code other than `429` ... Investigate the error in your request before retrying."
  - The backoff example waits 2, 4 and 8 seconds: "You should implement a maximum delay interval, as well as a maximum number of retries."
  - The same page weighs list-extended calls at five times a plain call, and points to exports rather than listing every entity.
  - It recommends distributing report requests over time and backfilling older periods in small increments, and links Brooker's "Exponential Backoff And Jitter".
  - The Well-Architected reporting component adds that report creation should honour `Retry-After`.

  [official] (Rate limiting, above; Reporting and analytics component, below)
- GUIDANCE, cadence. "We currently recommend 1-2 report requests, per advertiser, per day, for each report type. This is based on data refresh rates." "You may experience report limiting during busy times of day. To avoid excessive rate limiting, spread report requests throughout the day rather than requesting all at once." [official] (Sponsored ads reporting FAQ (version 3), above)
- GUIDANCE, report size. "Reports that request many fields may take longer to generate. To avoid large reports, you can: specify only necessary metrics ... make report requests that do not specify metadata (for example, `campaignName`, `campaignId`, `adGroupName`, `adGroupId`) in the report request body itself. Instead, retrieve metadata fields using an export and then merge." [official] (Sponsored ads reporting FAQ (version 3), above)
- GUIDANCE, lifecycle hygiene.
  - "Implement systematic tracking of report IDs after initiating requests. Use stored IDs to retrieve reports, avoiding duplicate creation and too early responses (`425`). Remove pending reports before resubmitting identical requests."
  - "The reporting API is designed for batch data retrieval, so frequent intraday requests do not provide significant additional value."
  - "Utilize the date range capability of the reporting API to retrieve up to 31 days of data in a single request."

  [official] (Reporting and analytics component, Amazon Ads Well-Architected Framework, https://advertising.amazon.com/API/docs/en-us/guides/amazon-ads-well-architected-framework/reporting-and-analytics-component, read 2026-11-09)
- GUIDANCE. "The reporting APIs are designed to provide daily and summary performance report. If you need to receive data more frequently, you can use Amazon Marketing Stream ... Otherwise, you might experience throttling if you attempt too many consecutive calls." [official] (Sponsored ads reporting overview (version 3), above)

### F. Reporting v1 (Unified Reporting): the call sequence and the model

- RULE, operations.
  - The three operations:
    - `POST /adsApi/v1/create/reports` (`AdsApiv1CreateReport`);
    - `POST /adsApi/v1/retrieve/reports` (`AdsApiv1RetrieveReport`);
    - `POST /adsApi/v1/delete/reports` (`AdsApiv1DeleteReport`, "Delete a report by ID").
  - Each answers `207` on success. Each may answer `400`, `401`, `403`, `404`, `413`, `429`, `500`, `502`, `503` or `504`.
  - Header parameter: `Amazon-Ads-ClientId` (required). The quickstart's calls send `Amazon-Advertising-API-ClientId` instead.
  - Create "Requires one of these permissions": `ManagerAccount_Dev`, `advertiser_campaign_edit`, `nemo_report_view`, `MasterAccount_Viewer`, `MA_ReadOnly`, `advertiser_campaign_view`, `reports_edit`, `MasterAccount_Manager`, `nemo_report_edit`, `view_performance_dashboard`.
  - Servers: `https://advertising-api.amazon.com`, `-eu`, `-fe`.

  [official] (Reports API, "AmazonAdsAPIALLReportsContract_prod_3p.json", https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLReportsContract_prod_3p.json, read 2026-11-09)
- RULE, no scope header; the account is in the body. The quickstart's create call sends `Amazon-Advertising-API-ClientId`, `Authorization`, `Accept: application/json` and `Content-Type: application/json`. Its body carries `accessRequestedAccounts: [{advertiserAccountId}]`. [official] (Getting started with the Reporting API v1, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/quickstart, read 2026-11-09)

  An item of `accessRequestedAccounts` is one of `{advertiserAccountId}` ("ADSP Regional Account or Global Account") or `{managerAccountId}` ("Manager Account"). [official] (AmazonAdsAPIALLReportsContract_prod_3p.json, `ReportCreateAccessRequestedAccountItem`)
- RULE, where the account id comes from.
  - "Accounts are now global in nature and can contain multiple countries. An advertiser registered for 3 countries will usually have 1 ads account ID and 3 country-specific profile IDs, though some advertisers may have separate ads accounts per country."
  - The legacy operations `POST /adsAccounts/list` and `GET /adsAccounts/{accountId}` are deprecated. The Deprecations entry "July 2026 - Deprecation of legacy account management APIs" lists six impacted endpoints (`GET /dsp/advertisers`, `GET /dsp/advertisers/{advertiserId}`, `POST /adsAccounts`, `POST /adsAccounts/batch`, `GET /adsAccounts/{accountId}`, `POST /adsAccounts/list`), with "Deprecation Date: July 2026" and "Shutoff Date: July 2027". Its transition notes: "Starting July 2026, all six legacy endpoints return `Warning: 299` response headers indicating deprecation." "Starting July 2026, new client integrations are blocked. Existing callers continue to function through an allowlist until the shutoff date." "Beginning July 2027, requests to these endpoints will return `HTTP 404 Not Found`." The Retrieving accounts guide, read the same day, still describes the legacy calls and carries no deprecation notice.
  - The replacement for "Account retrieval and listing" is `POST /adsApi/v1/query/advertiserAccounts` (QueryAdvertiserAccount). It sends `Amazon-Ads-ClientId`, `Authorization` and `Content-Type: application/json`, with no scope header, and an empty body `{}` "Retrieve[s] all global accounts". Omitting `isGlobalAccountFilter` returns only global accounts; `{"isGlobalAccountFilter": {"include": [false]}}` returns non-global ones (`amzn1.ads1.aa1.{country}.{entityId}`). `advertiserAccountIdFilter` "only works with global account IDs". An item carries `advertiserAccountId`, `alternateIds` (for Sponsored Ads `{countryCode, entityId, profileId}`, for DSP `{dspAdvertiserId, region}`), `currencyCode`, `displayName`, `industryVertical`, `isGlobalAccount`, `timeZoneIana` (e.g. `America/New_York`), and with an id filter also `status` and `sellingAccountLinkRequests`. Paging is by `nextToken`, and "An empty `advertiserAccounts` array with a valid `nextToken` is expected behavior. Always continue paginating."
  - A global account id looks like `amzn1.ads-account.g.87rerlyohs3b1cmj2rem03xmd`.

  [official] (Retrieving accounts in the Amazon Ads API, https://advertising.amazon.com/API/docs/en-us/guides/account-management/accounts/retrieve-accounts; Deprecations; QueryAdvertiserAccount API, https://advertising.amazon.com/API/docs/en-us/guides/account-management/query-advertiser-accounts; all read 2026-11-09). `method/ads-api-surface.md` owns the account calls; this file follows it.

  Stream v2 states the same identifier rule more sharply. A Global Account id is `amzn1.ads-account.g.*`. "Other identifiers are not accepted — including a manager account ID (`amzn1.ads1.ma1.*`) and selling-partner IDs such as a Seller Central account ID (MCID, e.g. `A6DEQ9LYHIBE8`) or a Vendor Group ID". [official] (Create a subscription, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/create-a-subscription, read 2026-11-09). `method/ads-api-surface.md` owns the account model.
- RULE, the create body (model `CreateReportRequest` → `ReportCreate`):
  - `accessRequestedAccounts`: `minItems` 1, `maxItems` 2000.
  - `reports`: `minItems` 1, `maxItems` 1 ("Currently, bulk requests only support a single sub-request").
  - Each report has:
    - `format` (required);
    - `periods` (required): `maxItems` 1; one `datePeriod {startDate, endDate}`, `format: date`;
    - `query` (required): `fields` of 1–1000 strings, and an optional `filter`;
    - optional `currencyOfView` (ISO 4217);
    - optional `managerAccountDspGrouping`: `DSP_ADVERTISER_ACCOUNT` or `GLOBAL_ADVERTISER_ACCOUNT` ("This field will be deprecated after 03/2027").
  - `format` enum:
    - `CSV`: "Comma-separated values file containing plain text tabular data";
    - `GZIP_JSON`: "JSON file compressed using GZIP format";
    - `PARTITIONED_CSV`;
    - `PARTITIONED_GZIP_JSON`.
  - `filter` is exactly one of `{on: ComparisonPredicate}` or `{and: {filters: [Filter, …]}}`, where `and` holds 1–10 filters. A predicate is `{field, comparisonOperator, not, values}`, all required:
    - `field` matches `^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$`;
    - `comparisonOperator` is `EQUALS` ("exactly a single value has to be provided") or `IN` ("at least one value");
    - `values` holds 1–2000 strings.

  [official] (AmazonAdsAPIALLReportsContract_prod_3p.json, above)

  Disagreement on the number of accounts. The guide says "up to 5 accounts at the same time within the `accessRequestedAccounts` configuration". The model allows 2000. Error `400019` reads "The number of `accessRequestedAccounts` exceeds the available limit". [official] (Helpful concepts, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/helpful-concepts; Handling errors, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/error-handling; both read 2026-11-09)
- RULE, the reply shape. Create, retrieve and delete answer a multi-status body `{success: [{index, report}], error: [...]}`, each array holding at most one item. "The new API uses a bulk request model, and that also allows for partial failure scenarios via the `207: Multi-Status` status code. Currently, bulk requests only support a single sub-request, so the `207` status code is not used for errors." [official] (AmazonAdsAPIALLReportsContract_prod_3p.json, `ReportMultiStatusResponse`; Handling errors, above)
- RULE, the report record (`Report`).
  - Required: `reportId`, `status`, `format`, `periods`, `query`, `creationDateTime`, `lastUpdatedDateTime`.
  - Optional:
    - `completedDateTime`;
    - `completedReportParts`: 0–100 items of `{sizeInBytes, url, urlExpirationDateTime}`, where `sizeInBytes` "could reach up to 100GB";
    - `failureCode` and `failureReason`;
    - `currencyOfView`;
    - `managerAccountDspGrouping`;
    - `warnings`: 0–1000 items, "Absent when there are none". The New features page instead says `warnings` is `null` when there are none.
  - Retrieve takes `{reportIds: [one id]}`; delete takes the same.

  [official] (AmazonAdsAPIALLReportsContract_prod_3p.json, above)
- RULE, statuses. The enum is `COMPLETED`, `FAILED`, `PENDING`, `PROCESSING`. Amazon's table:
  - `PENDING`: "The report is pending, check back later." Not terminal.
  - `PROCESSING`: "The report is processing, check back later." Not terminal.
  - `COMPLETED`: "The report generation completed, see the `completedReportParts` for download information." Terminal.
  - `FAILED`: "The report generation failed, see the `failureCode` and `failureReason` for more information." Terminal.

  [official] (Getting started with the Reporting API v1, above)
- GUIDANCE, polling. "You can check the status of your report at any time by retrieving the report. The recommended frequency is once per minute." [official] (Getting started with the Reporting API v1, above)
- RULE, download.
  - "Each report part will include a pre-signed S3 URL, and you can then download the report using your mechanism of choice."
  - Partitioned formats: "Currently, reports are split into up-to 1GB (uncompressed) chunks. Each of the partition files will be available in the `completedReportParts` property."
  - In Amazon's partitioned example the parts' `urlExpirationDateTime` is two minutes after `completedDateTime` (00:12:50 → 00:14:50). In the quickstart example it equals `completedDateTime`. **(for human readers only)**

  [official] (Getting started with the Reporting API v1; New features, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/new-features; both read 2026-11-09)
- RULE, synchronous errors. A `400` body is `{code, message}`. In the model, `code` is a word enum (`BAD_REQUEST`, `CONTENT_TOO_LARGE`, `FORBIDDEN`, `INTERNAL_ERROR`, `NOT_FOUND`, `TOO_MANY_REQUESTS`, `UNAUTHORIZED`), while the guide's codes are numeric strings; an `error[]` item of the multi-status body is `{index, errors[{code, message, fieldLocation}]}` with 1–20 errors. With several errors the code is `400100`, and the message lists them comma-separated (`400007: …, 400015: …`). Amazon's codes:
  - `400000`: malformed JSON.
  - `400001`: generic client error.
  - `400004`: incompatible fields.
  - `400005`: "a reporting field ID that does not exist".
  - `400006`: "a field without also including its required field".
  - `400007`: start after end.
  - `400009`: "The period was in the future".
  - `400011`: "the same field multiple times".
  - `400013`: "a value that is not a properly formatted reporting field ID".
  - `400014`: no metric.
  - `400015`: no Level of Detail dimension.
  - `400016`: no Time dimension.
  - `400017`: unsupported format.
  - `400019`: too many `accessRequestedAccounts`.
  - `400020`–`400023`: filter errors.
  - `400025`: "The period exceeded the available look-back for the included time dimensions".
  - `400026`: accounts "unauthorized or do not have linked advertiser accounts".
  - `400027`: `convertedCurrency.value` "requires `currencyOfView`".
  - `404001`: "The requested `reportId` was not found".
  - `500100`: unhandled internal error.

  "This list may grow over time." [official] (Handling errors, above)
- RULE, HTTP classes.
  - "`403: Forbidden` — The data requested is not authorized for the account provided. Do not re-request the data until permissions have been explored and adjusted for the account."
  - "`429: Too Many Requests` — Requests are too frequent or too large."
  - "`500`/`503` — An internal error, please reach out to support."

  [official] (Handling errors, above)
- RULE, asynchronous failures.
  - `failureCode` `001`: "An unhandled internal failure occurred. Try again, and if the issue persists, contact support."
  - `failureCode` `002`: "The report you requested was too large. Adjust your request to reduce the date period, number of accounts, or included fields."

  [official] (Handling errors, above)
- RULE, warnings (release of October 5, 2026).
  - "Warnings are non-fatal: they never prevent a report from completing, and the data you receive is still valid."
  - Each entry is `{field, warningCodes[]}`, with 1–100 codes. The page's example flags `target.value` as `PENDING_DEPRECATION`.
  - Codes:
    - `NO_PERMISSION`: "the field's value is redacted for the accounts you are not permissioned for";
    - `PENDING_DEPRECATION`;
    - `DATE_LIMITED`: "Data for this field is not available for the entire date range you requested".
  - "The set of signals is additive — new signals may be introduced over time, so handle `warningCodes` as an open-ended list."

  [official] (New features; Amazon Ads API v1 release notes, entry of October 5, 2026; both above)
- RULE, field composition.
  - "Fields can be either metric fields (e.g. `metric.impressions`) or dimension fields (e.g. `campaign.id`) ... the aggregation will occur on all of your specified dimensions", "in a `GROUP BY` fashion". Amazon's worked example multiplies 8 days × 2 campaigns × 10 postal codes × 20 supply sources into 3,200 rows.
  - "If you want to include a dimension attribute in a report (e.g. `campaign.name`), you must also include the primary key (e.g. `campaign.id`)."
  - "The `metric.sales` field requires the `budgetCurrency.value` field."
  - "The `convertedProduct` dimension is incompatible with the `audienceSegment` dimension."
  - The two error texts are "`400004: field {FIELD_1} cannot be used along with fields: {FIELD_2}`" and "`400006: field {FIELD_1} cannot be used without also including fields: {FIELD_2}`".

  [official] (Getting started with the Reporting API v1; Helpful concepts; both above)
- RULE, default scope. "By default, the new reporting API will include data from all ad products." "By default, the new reporting API will include data from all of your campaigns." Filters narrow it, e.g. `{"on": {"field": "adProduct.value", "comparisonOperator": "EQUALS", "not": false, "values": [...]}}`. [official] (Building Queries, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/building-queries, read 2026-11-09)

  [seat] Amazon's own example writes the value as ``"`SPONSORED_BRANDS`"``, with backticks inside the string. The page does not say whether the backticks are part of the value.
- RULE, null is not zero.
  - "A missing value does not imply zero. If a numeric metric has a measured value of zero, it will be explicitly reported as `0`, not as an empty string or `null`."
  - In CSV an absent value is `""`; in JSON it is `null`.
  - The reasons Amazon lists:
    - the dimension or metric is "not applicable to the specific ad type or campaign type in that row";
    - the attribute is nullable;
    - "Data is not yet available due to processing timelines. Some metrics may take longer to finalize than others.";
    - "Access restrictions prevent the value from being included for your account."

  [official] (Helpful concepts, above)
- RULE, currency. "you cannot sum up currency related fields (e.g. `metric.sales`) to view top-level performance" across budget currencies. With `currencyOfView`, `convertedCurrency.value` and the `…Converted` metrics, Amazon converts using "daily currency rate tables". [official] (New features, above)

### G. Reporting v1: time dimensions, dates, retention, time zone

- RULE, the time dimensions replace `timeUnit`. `date.value` is the old `DAILY`, `week.value` is `WEEKLY`, `month.value` is `MONTHLY` and `hour.value` is `HOURLY`. Helpful concepts lists `day` and `year` as new; the Dimensions library also lists `dayOfWeek` and `dateRange`, the latter giving one row for the whole period. A query with no time dimension is refused with `400016`. [official] (Helpful concepts; Handling errors; Date, …/dimensions/time/date; Hour, …/dimensions/time/hour; all under https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/, read 2026-11-09)
- RULE, the period and the clock.
  - Periods are inclusive of both dates.
  - Aggregation is "based on each campaign timezone".
  - `timeZone.value` names the zone a row was aggregated in. The example table shows EST, GMT, CET and JST rows from one request.
  - "Future releases will include support for UTC time zone normalization."

  [official] (Dates and historical data retention, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dates, read 2026-11-09)
- RULE, retention and maximum range per time dimension **(for human readers only)**:

  | Dimension | Retention | Max range |
  |---|---|---|
  | `hour.value` | 14 days | 14 days |
  | `date.value` | 24 months | 120 days |
  | `week.value`, `day.value`, `dayOfWeek.value` | 24 months | 15 months |
  | `month.value` | 6 years | 25 months |
  | `year.value`, `dateRange.value` | 6 years | 6 years |

  Benchmark dimensions start on 6/1/2025. A period beyond the look-back is refused with `400025`, and a field whose data does not cover the range carries the `DATE_LIMITED` warning. [official] (Dates and historical data retention; Handling errors; New features; all above). The release-notes entry of August 26, 2026 extended `date.value`, `week.value`, `day.value` and `dayOfWeek.value` retention "from 15 months to 24 months", adding "Maximum report date ranges are unchanged." [official] (Amazon Ads API v1 release notes, above)
- [seat] Compare the v3 type table in section C (95/65/60 days for most types). Under v1, a 13-month daily history of an SP campaign can be read again from Amazon. Under v3 it must have been landed while still within the retention window.

### H. Reporting v1: fields against v3 columns

- RULE, attribution conventions.
  - v1 attributes on the traffic date, and its base metrics carry no window suffix.
  - "Sponsored Products: Base metrics ... 7-day look-back for sellers and 14-day look-back for vendors". The other sponsored products use 14 days.
  - SP and SB CPC campaigns report `0` for conversions from views.
  - Product-level attribution is split into Promoted and Halo through `productRelevance.value`.

  [official] (Overview of the Reporting v1 API, above; Product relevance, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/dimensions/product/product-relevance, read 2026-11-09)
- RULE, the v3-to-v1 map. This is from Amazon's report-type migration guide.
  - `purchases7d` and `purchases14d` both map to `metric.purchases`.
  - `acosClicks7d`, `acosClicks14d` and every `…1d` and `…30d` column have no v1 equivalent ("—").
  - `campaignStatus` maps to `campaign.deliveryStatus`.
  - `campaignRuleBasedBudgetAmount` maps to `campaign.ruleAmount`.
  - `keywordBid` maps to `adGroupTarget.bid`, and `adKeywordStatus` to `adGroupTarget.status`.
  - `campaignApplicableBudgetRuleId`, `campaignApplicableBudgetRuleName` and `campaignSite` have no equivalent.
  - Several v3 window and SKU columns map to new v1 names: `roasClicks7d` and `roasClicks14d` to `metric.roasFromClicks`; `attributedSalesSameSku7d` and `attributedSalesSameSku14d` (and DSP `sales`) to `metric.salesPromoted`; `salesOtherSku7d` and `salesOtherSku14d` to `metric.salesHalo`; `unitsSoldOtherSku7d` to `metric.unitsSoldHalo`; `unitsSoldClicks*` to `metric.unitsSoldFromClicks`; `purchasesOtherSku7d`, `purchasesOtherSku14d` and SB `purchasesBrandHalo` to `metric.purchasesHalo`. The metric pages' "Version 3 Reporting Name" agrees (e.g. `metric.salesPromoted` lists "salesPromoted, salesSameSku7d, salesSameSku14d [SP: 7d sellers / 14d vendors]"). Amazon's labels "Brand Halo" and "Other SKU" both become "Halo".
  - The guide's columns are "Amazon Ads API v3 field | Stream v2 field | New Reporting API v1 field". Where Stream v2 has no field it says why: `CALCULATED_METRIC_NOT_AVAILABLE` (e.g. `clickThroughRate`, `costPerClick`, `roasClicks*`), `DIM_ATTRIBUTE_NOT_AVAILABLE` (e.g. `keyword`, `matchType`, `campaignBudgetCurrencyCode`: "Join on the dimension ID and get the attribute from the Amazon Ads campaign management API, the Exports API, or the Selling Partner API"), or `TIME_DIM_NOT_AVAILABLE`.
  - `spGrossAndInvalids` is not in the guide.

  [official] (Reporting API v3 Report Type Migration Guide, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/report-type-migration-guide; metric pages under guides/reporting/ads-v1/metrics/; all read 2026-11-09)
- RULE, the dimension pages a sponsored-ads reader touches:
  - `searchTerm.value`: SP, SB; v3 `searchTerm`.
  - `adGroupTarget.id`: the primary key, with attributes `bid`, `targetType` and `status`.
  - `targeting.value`: "keyword, product or category".
  - `targetingMatchType.value`.
  - `placementClassification.value`: SP, SB, SD, ST.
  - `matchedTarget.value`: Sponsored Display only; v3 `matchedTargetAsin`.
  - `productRelevance.value`: promoted or halo.
  - `convertedProduct.id`: requires `convertedProductMarketplace.value`; v3 `purchasedAsin`. `parentProductId` corresponds to v3 `parentAsin`.
  - `advertisedProduct.id`: requires `advertisedProductMarketplace.value`. The SKU is its own dimension, `advertisedProductSku.value` (v3 `advertisedSku` in the migration guide); the Advertised product page defines no `.sku` field.
  - `budgetCurrency.value`: v3 `campaignBudgetCurrencyCode`.

  [official] (Dimensions library, …/dimensions/library; Advertised product SKU, …/dimensions/product/advertised-product-sku; Search term, …/dimensions/targeting/search-term; Target, …/dimensions/targeting/target; Targeting, …/dimensions/targeting/targeting; Targeting match type, …/dimensions/targeting/targeting-match-type; Placement classification, …/dimensions/supply/placement-classification; Matched target, …/dimensions/targeting/matched-target; Converted product, …/dimensions/product/converted-product; Advertised product, …/dimensions/product/advertised-product; Budget currency, …/dimensions/currency/budget-currency; all under https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/, read 2026-11-09)
- RULE, the metric pages:
  - `metric.clicks`: "Clicks = gross clicks - invalid clicks" (Clicks page). `metric.grossClicks`, `metric.invalidClicks` and `metric.invalidClickRate` sit beside it.
  - `metric.totalCost` is v3 `spend` (Sponsored Ads) and `totalCost` (DSP). It requires `budgetCurrency.value` and is incompatible with Converted product and Product relevance (Costs page). `metric.totalCostReconciled` and `metric.supplyCost` sit beside it.
  - `metric.roas`: "ROAS = sales / total cost", likewise incompatible with Converted product and Product relevance. `metric.roasReconciled` sits beside it.
  - `metric.sales` gives v3 names "sales, sales7d, sales14d [SP: 7d sellers / 14d vendors]".
  - `metric.purchases` lists Search term, Target, Targeting, Placement classification and Converted product among its compatible dimensions. Its v3 names are "purchases, orders14d, purchases7d, purchases14d [SP: 7d sellers / 14d vendors]".
  - `metric.impressionShare` and `metric.impressionShareRank` require `adProduct.value`, `advertiserAccount.id` and `searchTerm.value`. They are incompatible with campaign, ad group, ad, advertised product and placement.
  - `metric.topOfSearchImpressionShare` requires `adProduct.value` and `advertiserAccount.id`. Its compatible dimensions include Campaign; its incompatible dimensions include Ad group, Hour, Placement classification, Target, Targeting, Targeting match type, Search term and Audience segment. The migration guide nonetheless maps v3 `spTargeting` and `sbTargeting` `topOfSearchImpressionShare` to this metric (section C).

  [official] (Metrics library, …/metrics/library; Clicks, …/metrics/delivery/clicks; Costs, …/metrics/costs-and-fees/costs; Purchases, …/metrics/amazon-retail-conversions/purchases; Search impression share, …/metrics/impression-share/search; under https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/, read 2026-11-09)
- Disagreement inside Amazon's migration pages.
  - The v1 report-type examples use `target.value` and `target.matchType`. The sp-search-term, sp-targeting and sp-purchased-product examples each list `target.value` twice in one field list; listing a field twice is what `400011` refuses. The New features page's warning example flags `target.value` as `PENDING_DEPRECATION`.
  - The Target dimension page defines `adGroupTarget.id`, `.bid`, `.targetType` and `.status`; the library defines no `target.value`. The target text and match type are `targeting.value` and `targetingMatchType.value`.
  - The examples also use `campaign.currencyCode`, `portfolio.portfolioId` and `advertisedProduct.sku`; the Advertised product page has no `.sku` field (the SKU is `advertisedProductSku.value`).
  - The advertised-product example uses `advertisedProduct.id` without `advertisedProductMarketplace.value`, and the purchased-product example lacks `convertedProductMarketplace.value`, which the dimension pages require.

  [official] (pages titled "Migrating from: spCampaigns" and so on: Sponsored Products campaigns, …/report-types/sp-campaigns; Sponsored Products search term, …/report-types/sp-search-term; Sponsored Products targeting, …/report-types/sp-targeting; Sponsored Products advertised product, …/report-types/sp-advertised-product; Sponsored Products purchased product, …/report-types/sp-purchased-product; under https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/, read 2026-11-09)
- RULE, the target fields as Amazon's field map spells them. The Reporting API v3 Report Type Migration Guide, under both `spTargeting` and `spSearchTerm`, maps (v3 | Stream v2 | v1):
  - `keywordId` → `adGroupTarget.id` | `adGroupTarget.id`;
  - `keyword` and `targeting` → `DIM_ATTRIBUTE_NOT_AVAILABLE` | `targeting.value`;
  - `keywordType` and `matchType` → `DIM_ATTRIBUTE_NOT_AVAILABLE` | `targetingMatchType.value`;
  - `keywordBid` → `adGroupTarget.bid`, and `adKeywordStatus` → `adGroupTarget.status`;
  - `searchTerm` (in `spSearchTerm`) → `searchTerm.value` in both.

  This agrees with the Target, Targeting and Targeting match type dimension pages. `target.value` appears only in the "Migrating from" examples and in the New features warning example, where it is flagged `PENDING_DEPRECATION`. [official] (Reporting API v3 Report Type Migration Guide; Target; Targeting; Targeting match type; New features; all read 2026-11-09)
- RULE, placement, target, search term and hour in one v1 query. No Amazon page read on 2026-11-09 makes these dimensions incompatible with one another:
  - The Placement classification page (`placementClassification.value`, primary key, "The classification of ad placements into categories like top of search, gateway page, etc.", SP, SB, SD, ST) lists "Required fields: N/A" and "Complementary fields: N/A". The Hour page (`hour.value`, `LONG`, SP, SB, SD, ST, DSP) says the same.
  - `metric.impressions`, `metric.clicks`, `metric.totalCost`, `metric.purchases` and `metric.sales` each list Hour, Placement classification, Target, Targeting, Targeting match type and Search term among their compatible dimensions.
  - Helpful concepts gives dimension-to-dimension incompatibilities only as examples ("For example: The `convertedProduct` dimension is incompatible with the `audienceSegment` dimension; The `audienceSegment` dimension is incompatible with the `supplySource` dimension; The `metric.userReach` metric is incompatible with the `postalCode` dimension"). It directs readers to "check the compatibility and requirements for every field in our dimension library and metrics library", and an incompatible pair is refused with `400004`.
  - Stream v2 `ads-performance-v1` carries `hour.value`, `placementClassification.value`, `adGroupTarget.id` and `searchTerm.value` (SB, SP) as dimension fields, and "Dimension fields form the record key". Its subscription has "no granularity or filter parameter", and `searchTerm.value` is thresholded (section K).
  - Stream v1 `sp-traffic` and `sp-conversion` carry `keyword_id`, `keyword_text`, `match_type`, `placement` and `time_window_start` ("The start of the hour") in one row, until the 2027-06-30 shutoff (section K).
  - In v3 there is no target-by-placement type. `spTargeting` and `sbTargeting` group by `targeting` only, and placement comes from `spCampaigns` grouped by `campaignPlacement` or from `sbCampaignPlacement` (section C). The console-against-API page's column table names a Sponsored Brands console report "Keyword placement". Its list of console report types "not available using the Amazon Ads API" holds only SP Performance Over Time, SP and SB Search Term Impression Share, and SP Budget.
  - `metric.topOfSearchImpressionShare` and `metric.impressionShare` / `metric.impressionShareRank` are the exceptions. Each is incompatible with Hour, Placement classification, Target and Targeting (the share metrics are also incompatible with Campaign and Ad group, and compatible with Search term).

  [official] (Placement classification; Hour; Clicks; Impressions, …/metrics/delivery/impressions; Costs; Purchases; Search impression share; Helpful concepts; Ads performance dataset; Stream v2 FAQ; Sponsored Products performance datasets (Stream v1), https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/datasets/sp-performance; Targeting reports; Campaign reports; Reporting in the advertising console vs. API (version 2); all read 2026-11-09)

  [seat] The pages permit a v1 query with `adGroupTarget.id`, `placementClassification.value` and `hour.value` together, but do not show one. Whether the service accepts it is read from the create reply (`207` or `400004`).

### I. Reporting v1: concurrency and rate limits

- RULE, with Amazon's pages in disagreement on the scope.
  - Per client id:
    - "Reporting API v1 applies its rate and concurrency limits per client ID ... Limits are not applied per advertiser account ... A request for one advertiser account can be throttled because of other requests made with the same client ID." [official] (Limits and best practices, https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/limits, read 2026-11-09)
    - The v1 overview says the API "supports one concurrent report per client ID, not per advertiser account". [official] (Overview of the Reporting v1 API, above)
  - Per advertiser:
    - "one concurrent report per advertiser ... approximately 100 reports per day". [official] (Amazon Ads reporting overview, above; the Stream v2 overview repeats it for Reporting API v1)
    - The GA entry of September 30, 2026 says the API "supports one concurrent report per advertiser ... approximately 100 reports per day". [official] (Amazon Ads API v1 release notes, above)
  - Re-read on 2026-11-09 (gap fill), word for word:
    - The v1 overview's note: "The reporting API v1 supports one concurrent report per client ID, not per advertiser account. This allows approximately 100 reports per day based on average run times. For details, see Limits and best practices."
    - The v1 Limits page: "Reporting API v1 applies its rate and concurrency limits per client ID. The client ID is the Login with Amazon client ID you send in the `Amazon-Advertising-API-ClientId` header. Limits are not applied per advertiser account. All requests made with the same client ID share the same limits, regardless of how many advertiser accounts those requests cover."
    - The reporting overview, in a note and again under "Rate limits": "The reporting API v1 allows one concurrent report per advertiser. Only one report can be running at a time for a given advertiser account."
    - The Stream v2 overview: "The reporting API v1 is designed for ad-hoc reporting use cases and is subject to usage limits (one concurrent report per advertiser, approximately 100 reports per day)."
    - The GA release note: "The Reporting API v1 supports one concurrent report per advertiser, which allows advertisers to run approximately 100 reports per day based on average report run time."

    The two v1 pages say per client id, and the v1 overview defers to the Limits page "for details". The three general pages say per advertiser. All five give about 100 reports a day. No page is dated after another in a way that marks one as the correction. The pages disagree, and this file states the disagreement rather than one side. [official] (all five pages above, read 2026-11-09)
- RULE, what a second create meets while one report runs. The pages give two answers:
  - Limits: "When either limit is exceeded, new requests will receive an HTTP `429` (Too Many Requests) error until previous requests complete or the rate limit window resets."
  - Reporting overview: "If you submit a report request while another report is already running for the same advertiser, the request will be queued or receive a 429 response code."

  [official] (Limits and best practices; Amazon Ads reporting overview; both read 2026-11-09)
- RULE, duplicates: v1 has no `425`, and nothing documents identical asks.
  - The v1 model's answers to `AdsApiv1CreateReport` are `207`, `400`, `401`, `403`, `404`, `413`, `429`, `500`, `502`, `503` and `504`. There is no `425` or `409`.
  - `CreateReportRequest` holds only `accessRequestedAccounts` and `reports`. `ReportCreate` holds `currencyOfView`, `format`, `managerAccountDspGrouping`, `periods` and `query`. There is no client token or idempotency key.
  - Handling errors' code list has no duplicate-request code.
  - No v1 page read says whether an identical create returns the running report's id or starts a second report.
  - The v1 model has no list operation: its only paths are `/adsApi/v1/create/reports`, `/retrieve/reports` (by `reportIds`) and `/delete/reports`. A report whose id was not kept cannot be found again through the API. The v3 model likewise has only `POST /reporting/reports`, `GET` and `DELETE /reporting/reports/{reportId}`.
  - The Limits page warns that "Repeating the same request may result in repetitive failures if the report is too large to process."

  [official] (AmazonAdsAPIALLReportsContract_prod_3p.json; OfflineReport_prod_3p.json; Handling errors; Limits and best practices; all read 2026-11-09)
- RULE, levels. The limits page continues:
  - The "concurrency limit" can be "as low as 1".
  - The "rate limit" can be "as low as 1 request per second".
  - Both "may vary by client ID".
  - Backoff is exponential from 1 second, doubling.
  - A report that is too large may fail immediately or later, and "Repeating the same request may result in repetitive failures".
  - Higher concurrency is requested through a support ticket.

  [official] (Limits and best practices, above)
- RULE, the same overview's rate note: requests over the limit are "queued or receive a 429". Its recommendation is "serializing requests per advertiser". [official] (Amazon Ads reporting overview, above)

### J. Freshness, traffic validation, restatement: when a day stops moving

- RULE, v3 and v2 FAQ (the two pages carry the same text):
  - "Initial impression and click data is available using the API within 12 hours. Note that small changes to impression and click data may happen up to three days after the initial click date due to the traffic validation process. We recommend retrieving click and impression data again after three days to ensure you have the latest data."
  - "Initial conversion data is available within 24 hours, but may change as part of the restatement process. Restatements of conversion data occur 1, 7, and 28 days after the conversion event. Because conversions are reported on the date of the ad interaction, restatement includes all dates in your attribution window. For example, if your attribution window is 14 days, restatement can update attribution up to 42 days (14 plus 28) after the report date."

  [official] (Sponsored ads reporting FAQ (version 3), above; Sponsored ads reporting FAQ (version 2), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v2/faq, read 2026-11-09)
- RULE, the reporting overview, on a longer horizon:
  - "Data freshness": 12 hours.
  - Invalid traffic is monitored "up to 30 days", and "We recommend waiting at least 5 days for the most accurate click data".
  - "Conversion data ... subject to change for up to 60 days ... re-retrieving reports monthly".
  - DSP invalid traffic: 72 hours.

  [official] (Amazon Ads reporting overview, above)
- RULE, the limits table. P99 for "Impression/click invalidation" is "72h". **(for human readers only)** [official] (Limits, constraints, and quotas, above)
- RULE, Stream v2. The restatement window of `ads-performance-v1` and `ads-converted-product-v1` is 70 days. The Datasets overview says "Treat a record as final only after its window has passed." The reporting overview says Stream v2 backfills "so your data self-corrects". [official] (Ads performance dataset, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/ads-performance; Ads converted product dataset, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/ads-converted-product; Datasets overview, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/overview; Amazon Ads reporting overview; all read 2026-11-09)
- No report field marks a day as final. Neither the v3 `AsyncReport`, the v1 `Report` nor a row carries a completeness flag. The nearest signals are:
  - v1's `null` with the reason "not yet available due to processing timelines";
  - the `DATE_LIMITED` warning;
  - Stream's `streamBatch.version`.

  [official] (OfflineReport_prod_3p.json; AmazonAdsAPIALLReportsContract_prod_3p.json; Helpful concepts; all above)
- The pages disagree on the horizon: traffic 72 hours, 3 days or 30 days; conversions 42, 60 or 70 days. All three horizons are on Amazon's pages on 2026-11-09. **(for human readers only)**
- GUIDANCE, the Amazon Ads library. "After your campaign has been running for at least two weeks, review your advertising reports". [official] (How to measure and improve your campaigns, https://advertising.amazon.com/library/guides/measure-improve-campaigns, read 2026-11-09)

### K. Amazon Marketing Stream v2: datasets, delivery, limits

- RULE, delivery.
  - Stream v2 delivers Parquet files to an S3 bucket the client owns, with an SQS notification per delivery.
  - Values are totals per time window, not deltas. The record to keep for a key is the one with the highest `streamBatch.version`, which should be read as a 64-bit integer or a string, never as a float.
  - Delivery is at least once, with no ordering.
  - A batch covers a half-open UTC interval.

  [official] (Amazon Marketing Stream v2 overview, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/overview; Data delivery; both read 2026-11-09)
- RULE, datasets.
  - `ads-performance-v1`: hourly grain, one account per subscription, restatement window 70 days. The GA release note gives "Approximately 400 metrics and 50 or more dimensions" and "Delivery frequency is as often as every 15 minutes"; the dataset page's table held 377 metric rows on 2026-11-09 **(for human readers only)**.
  - `ads-converted-product-v1`: daily grain, "Global Account, Amazon DSP (ADSP) Regional Account", one account per subscription, restatement window 70 days. The GA release note gives "Approximately 170 conversion metrics at the ASIN level" and "Delivery frequency is every 4 to 6 hours".
  - On a new subscription "Stream v2 delivers your entire historical data for the dataset's restatement period, within about a day of activation." "Historical data for a dataset may arrive at a coarser grain (for example, daily) even when current deliveries for that dataset are hourly."

  [official] (Datasets overview, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/overview; Ads performance dataset; Ads converted product dataset; Create a subscription; Data delivery, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/data-delivery; Stream v2 FAQ, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/faq; Amazon Ads API v1 release notes, entry of September 30, 2026; all read 2026-11-09)
- RULE, thresholds and arithmetic.
  - "Amazon Ads applies reporting thresholds to high-cardinality dimensions, grouping values that do not meet the threshold into an `(Other)` row". In `ads-converted-product-v1`, `convertedProduct.id` is thresholded. In `ads-performance-v1`, `searchTerm.value` is thresholded.
  - Rows are disjoint: a metric that does not apply to a row is zero there, rows sharing an entity key are summed, and numerators and denominators are aggregated before dividing. Totals including `(Other)` match the coarser grain.
  - The datasets carry no calculated metrics and no names or attributes; the Stream v2 FAQ points to the campaign-management APIs for mutable attributes.

  [official] (Ads converted product dataset; Datasets overview; Stream v2 FAQ; Reporting API v3 Report Type Migration Guide; all above)
- RULE, how the threshold works, and where it is not stated (gap fill, 2026-11-09).
  - The Datasets overview: "To protect customer privacy, Amazon Ads applies reporting thresholds to high-cardinality dimensions. When activity for a dimension value does not meet the minimum threshold, that value is not reported on its own; its metrics are grouped into a row with value `(Other)` for that dimension field at that grain. Thresholds are evaluated at the exact level of detail in your data, so the same value can be reported on its own at one aggregation level and grouped into `(Other)` at a more granular level. Totals stay complete".
  - `ads-performance-v1`: "In this dataset, `searchTerm.value` is subject to reporting thresholds. If you see fewer search terms than you expect, some did not meet the threshold at the dataset's granularity." The dataset's grain is hourly.
  - The minimum threshold is not given as a number on any page read.
  - Reporting v1: none of the v1 guides (overview, quickstart, limits, dates, building queries, handling errors, helpful concepts, new features), nor the Search term dimension page, the Dimensions library, the Metrics library or the sp-search-term migration page, contains "threshold", "(Other)" or "privacy". The v3 Search term reports page, the v3 FAQ and the v3 columns page do not either; v3 states only the click rule.
  - The parity claims are general. The reporting overview says Stream v2 "Provides full reporting API v1 parity with total values". The migration guide says "Stream v2 and the new Amazon Ads Reporting API v1 share the same field conventions". The Stream v2 FAQ says "Stream v2 delivers the base metrics and dimensions the Reporting API exposes". None of them names thresholds.

  [official] (Datasets overview; Ads performance dataset; the v1 pages listed; Search term reports; Sponsored ads reporting FAQ (version 3); Reporting columns (version 3); Amazon Ads reporting overview; Reporting API v3 Report Type Migration Guide; Stream v2 FAQ; all read 2026-11-09)

  [seat] So whether a v1 `searchTerm.value` row can read `(Other)` is not settled by Amazon's pages. The Datasets overview's "evaluated at the exact level of detail" says that if the rule applies, a term reported alone in a `dateRange.value` × `searchTerm.value` query may fall into `(Other)` in an `hour.value` × `adGroupTarget.id` × `searchTerm.value` query. A reader can test this by finding a literal `(Other)` value in the rows it lands.
- RULE, identifiers in the data. `advertiserAccountAlternateProfileId.value` and `timeZone.value` are among the dimensions. [official] (Ads performance dataset, above)
- RULE, subscription and destination.
  - Subscriptions are created with `POST /adsApi/v1/create/streamSubscriptions`, with the account in `accessRequestedAccounts[].advertiserAccountId`, not in a scope header.
  - The body names the dataset, an S3 `bucketArn` and an SQS `queueArn`.
  - A subscription "becomes `ACTIVE` on creation". `SUSPENDED` is terminal (Stream v2 FAQ).
  - Manager accounts are not supported; ADSP numeric ids are accepted. A subscription for an account the caller cannot reach answers `401` "Bulk account authorization denied: DENY".
  - A destination belongs to the first application that registers it (Stream v2 FAQ).
  - AWS Regions: NA `us-east-1`; EU `eu-west-1`, `eu-west-2`, `eu-south-2`; FE `us-west-2`, `ap-southeast-1`.
  - "A subscription delivers the advertiser's global data regardless of the destination Region."
  - There is no fee beyond the client's own AWS costs.

  [official] (Create a subscription; Stream v2 overview; Stream v2 FAQ; all above)
- RULE, limits.
  - One unique subscription per dataset, destination and account.
  - "Destinations per client application | 5".
  - One account per `accessRequestedAccounts`.
  - 25 requests per second per subscription-management operation, with `429` `TOO_MANY_REQUESTS` above that.
  - Parquet files target "~256 MB", but "a file can be larger".
  - The page links the AWS Builders' Library article "Timeouts, retries, and backoff with jitter".

  [official] (Limits, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/manage-subscriptions/limits, read 2026-11-09)
- RULE, Stream v1. Stream v1 is "shut off on June 30, 2027". Its values were deltas ("pushing the delta values instead of aggregates"), and its sponsored-ads dataset names include `sp-traffic`, `sp-conversion`, `sb-traffic`, `sb-conversion`, `sd-traffic` and `sd-conversion`. [official] (Amazon Marketing Stream overview, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/overview; Dataset migration guide, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/dataset-migration-guide; both read 2026-11-09)
- RULE, Stream v1 Sponsored Products: page and dataset ids (gap fill, 2026-11-09).
  - The page at `guides/amazon-marketing-stream/datasets/sp-performance` is titled "Sponsored Products performance datasets". It describes two datasets: "To subscribe to this dataset, use the ID `sp-traffic`" and "use the ID `sp-conversion`". "sp-performance" is the page's path, not a dataset id. The Sponsored Brands and Sponsored Display pages follow the same pattern (`sb-performance`, `sd-performance` paths).
  - Subscriptions use the `/streams/subscriptions` endpoints.
  - `sp-traffic` fields: `idempotency_id` ("can be used to de-duplicate records"), `dataset_id`, `marketplace_id`, `currency`, `advertiser_id`, `campaign_id`, `ad_group_id`, `ad_id`, `keyword_id`, `keyword_text`, `match_type`, `placement` ("The page location where an ad appeared"), `time_window_start` ("The start of the hour to which the performance data is attributed ... Time zone for each advertiser is indicated on the advertiser profile"), `clicks`, `impressions` and `cost`.
  - `sp-conversion` carries `keyword_id`, `placement` and `time_window_start` with the `attributed_conversions_`, `attributed_sales_` and `attributed_units_ordered_` columns at 1, 7, 14 and 30 days, plain and `_same_sku`.
  - Freshness: traffic clicks "can be invalidated during the following 72 hours". Conversions are "reported based on the hour when the click they are attributed to occurred", with revisions "up to sixty days after the initial click". Data is delivered "in a burst every hour".
  - The page warns that "some v1 functionality may be limited before Stream v1 is shut off on June 30, 2027."

  [official] (Sponsored Products performance datasets, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/datasets/sp-performance; docs table of contents; both read 2026-11-09)

### L. Exports: the metadata beside a report

- RULE.
  - Exports cover SP, SB and SD. They are created with `POST /campaigns/export`, `POST /adGroups/export`, `POST /targets/export` and `POST /ads/export`. Each takes its own media type (`application/vnd.campaignsexport.v1+json` and so on), a required `adProductFilter` and an optional `stateFilter`.
  - Status is read with `GET /exports/{exportId}`.
  - "It is not possible to retrieve historical metadata": an export is a snapshot of now.
  - Each endpoint allows 5 in-progress jobs.
  - Download URLs are valid for 1 hour and can be regenerated for 24 hours: "Each call to GET /exports/{exportId} generates a new download URL".
  - Amazon recommends exporting 1–2 times a day.

  [official] (Exports overview, https://advertising.amazon.com/API/docs/en-us/guides/exports/overview; Get started with exports, https://advertising.amazon.com/API/docs/en-us/guides/exports/get-started; Exports FAQ, https://advertising.amazon.com/API/docs/en-us/guides/exports/faq; all read 2026-11-09)
- RULE. Exports are unaffected by the 2027 shutoff. [official] (Deprecations, above)

### M. Console reports, bulksheets, and console against API

- RULE, which reports exist only in the console. The SP Performance Over Time report, the SP and SB Search Term Impression Share reports, and the SP Budget report exist only in the console. [official] (Reporting in the advertising console vs. API (version 2), https://advertising.amazon.com/API/docs/en-us/guides/reporting/v2/advertising-console, read 2026-11-09)
- RULE, console column mapping. For SP sellers the console's sales column is "7 Day Total Sales". For vendors, and for SB and SD, it is the 14-day column. [official] (Reporting in the advertising console vs. API (version 2), above)
- GUIDANCE. "Small data discrepancies between advertising console and API reports may occur and are expected due to differences in the traffic validation and data refresh processes. If you experience a data discrepancy of greater than 5%, contact the API support team". [official] (Version 2 reporting overview, above; Reporting in the advertising console vs. API (version 2), above)
- RULE, console search terms against API search terms. The console's search term report holds every term with an impression; the API's holds terms with a click. [official] (Sponsored ads reporting FAQ (version 3), above)
- RULE, joining console and API data. "To join console and API reporting data, you can use the campaign or ad group name as an index." [official] (Sponsored ads reporting FAQ (version 2), above)
- RULE, the bulksheets search term report.
  - The seller and vendor look-back metrics are not included; the "lookback window ... always 7 days".
  - The chosen date range "does not affect the search term report metrics".
  - The report contains ASIN-like terms, and impressions only for terms with at least one click.
  - The page's CTR and CVR definitions are inverted (section D).

  [official] (Search term reports in bulksheets, above)
- RULE, what a bulksheet download includes. The download offers options for terminated campaigns, zero-impression items and placement data; by default terminated campaigns and zero-impression items are excluded and placement data is included. [official] (Understand bulksheets campaign data, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/understand-bulksheets-data, read 2026-11-09)
- The console's own report help (Reports, help GBYSPTSLR337JMLH) is a JavaScript shell to a GET. Amazon's console retention figures could not be read first-hand on 2026-11-09. Practitioners' figures are in the next part.
- RULE. Amazon's library page for the console now calls it "Amazon Ads Agent". [official] (Advertising console, https://advertising.amazon.com/library/guides/advertising-console, read 2026-11-09)

### N. Time zones across the stack

- RULE, v2 (and, by the profile, v3). The version 2 FAQ: "The time zone for a report is the time zone associated with the advertising account used to request the report, as determined by the profile ID provided in the request headers. To check the time zone for a given profile ID, use the `GET /v2/profiles/{profileId}` endpoint." [official] (Sponsored ads reporting FAQ (version 2), above)
- RULE, profiles. A profile carries `timezone`, `currencyCode`, and `accountInfo {marketplaceStringId, id, type, name}`. The model defines `timezone` as "The time zone used for all date-based campaign management and reporting", e.g. `America/Los_Angeles` for US, CA and MX, `Europe/Paris` for DE, ES, FR and IT, `Europe/London` for UK, `Asia/Tokyo` for JP. [official] (Profiles, https://advertising.amazon.com/API/docs/en-us/reference/2/profiles, read as the OpenAPI model https://d3a0d0y2hgofx6.cloudfront.net/en-us/profiles/3-0/openapi.yaml on 2026-11-09; the CDN copy of reference/2/profiles is `NoSuchKey`)
- RULE, v1. Aggregation follows each campaign's time zone, named per row in `timeZone.value`. UTC normalisation is promised in a future release (section G). [official] (Dates and historical data retention, above)
- RULE, the advertiser account's zone. A QueryAdvertiserAccount item carries `timeZoneIana` (e.g. `America/New_York` in Amazon's examples). [official] (QueryAdvertiserAccount API, read 2026-11-09). The page does not say how it relates to a campaign's `timeZone.value` or a profile's `timezone`.
- RULE, SP-API Data Kiosk Seller Analytics. Neither the schema `analytics_sellerAnalytics_2025_03_31` nor its use-case guide names the time zone of a `DAY`. The only clock words are:
  - "Data for a given day is generally available at 10 AM local time two days later";
  - promotion start and end dates "in the local time zone for a store".

  [official] (analytics_sellerAnalytics_2025_03_31.graphql; Seller Analytics Dataset Use Case Guide; both read 2026-11-09; section O)
- RULE, Stream v2. Batches are UTC intervals, and rows carry `timeZone.value`. [official] (Data delivery; Ads performance dataset; both above)
- GUIDANCE. The Well-Architected reporting component, on Stream: "When comparing Amazon Marketing Stream data with other reporting sources, consider potential time zone differences, as these can affect the interpretation and analysis of performance metrics." [official] (Reporting and analytics component, above)
- RULE, SP-API Data Kiosk Economics. Week and month boundaries are resolved "in UTC+0 timezone". [official] (analytics_economics_2024_03_15.graphql, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_economics_2024_03_15.graphql, read 2026-11-09)
- RULE, SP-API Vendor Retail Analytics are in PST. [official] (Report Type Values – Analytics, https://developer-docs.amazon/sp-api/docs/report-type-values-analytics.md, read 2026-11-09)

### O. Joining ad rows with SP-API rows

These are the keys and the grain of each side as Amazon states them. What the joined figures mean belongs to `areas/ads-organic-and-total.md` and `beyond/goals-and-economics.md`.

- RULE, Sales and Traffic (`GET_SALES_AND_TRAFFIC_REPORT`).
  - Report options: `dateGranularity` `DAY`, `WEEK` or `MONTH`; `asinGranularity` `PARENT`, `CHILD` or `SKU`.
  - A `WEEK` range expands to Sunday–Saturday weeks and a `MONTH` range to whole months.
  - The range is at most two years.
  - The report is gated by the Brand Analytics role.
  - The listed limit is "up to three times every five minutes" **(for human readers only)**.

  [official] (Report Type Values – Analytics, above)

  The document's schema has two arrays:
  - `salesAndTrafficByDate`: one entry per date, at account level;
  - `salesAndTrafficByAsin`: entries keyed by `parentAsin`, `childAsin` and `sku`, aggregated over the whole requested range, not per date.

  [official] (sellerSalesAndTrafficReport.json, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/reports/sellerSalesAndTrafficReport.json, read 2026-11-09)

  The Data Kiosk version (`analytics_salesAndTraffic_2024_04_24`) has three queries, aggregating by ASIN, by date, or by both (`asinAggregation`, `dateAggregation`). It moves a mid-week or mid-month end date to the preceding Saturday or month end, and a start date to the following Sunday or month start. The start date must be no more than two years ago. [official] (analytics_salesAndTraffic_2024_04_24.graphql, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_salesAndTraffic_2024_04_24.graphql, read 2026-11-09)
- RULE, Search Query Performance. Its periods are `WEEK`, `MONTH` and `QUARTER`. Weeks run Sunday–Saturday, and one report covers one period. [official] (Report Type Values – Analytics, above)
- RULE, Data Kiosk Economics.
  - `ads: [AdSummary]` carries `adTypeName` (e.g. "Sponsored Products charge") and `charge`.
  - It is aggregated by MSKU and day by default.
  - Its week and month boundaries are in UTC+0.
  - The start date is at most two years ago.

  [official] (analytics_economics_2024_03_15.graphql, above; last commit 2025-12-22)
- RULE, Data Kiosk Seller Analytics (`analytics_sellerAnalytics_2025_03_31`; schema last committed 2026-09-30, "SPAPI September 2026 Release"). Gap fill, 2026-11-09.
  - One view, `sellerAnalyticsView(startDate: Date!, endDate: Date!, aggregateBy: DateGranularity!, currencyCode: String, marketplaceId: [String!]!)`, for account type `MERCHANT` only ("The view is available to seller accounts only").
    - `aggregateBy` is `DAY`, `WEEK` or `MONTH`.
    - "The start date must be no more than two years ago", and the end date "Cannot be in the future".
    - `currencyCode`: "If not provided, amounts are returned in USD".
    - Marketplace identifiers "must be in the same region".
  - The reply is a list of `SellerAnalyticsView {startDate, endDate, totals, metrics: [{groupByKey, metrics}], sellerAttributes}`.
    - `groupByKey` (`GroupByAttributes`) offers `asin`, `productTitle`, `msku`, `brand`, `brandCode`, `parentAsin`, `fulfilmentChannel` (so spelt in the schema; the guide writes `fulfillmentChannel`), `productGroup`, `marketplaceId` and `encryptedMerchantCustomerId`.
    - "Every query must select at least one attribute in `groupByKey`."
    - `search.query.queryKeyword` and `defects.topics.returnDefectTopic` also group (`@domainGroupBy`).
  - Metric groups are `sales`, `traffic`, `promotion`, `accountHealth`, `lending`, `search`, `reviews`, `defects` and `returns`. The ones a join with ads uses:
    - `traffic`: `sessions` ("the sum of browserSessions and mobileAppSessions"; "All browser and mobile app activity within a 24-hour period is considered a session"), `browserSessions`, `mobileAppSessions`, `pageViews` (the sum of `browserPageViews` and `mobileAppPageViews`), `glanceViews`, `featureOfferGlanceViews` and `featureOfferPct` ("dividing the number of times your offer is the Featured Offer by the number of times customers viewed it (that is, Glance Views)").
    - `traffic` also has `conversionRatePct`: "the percentage of purchases to clicks for ASINs originated from the search results page". The misspelt `conversationRatePct` is `@deprecated(reason: "No longer supported. Use conversionRatePct instead.")`, yet the guide's traffic list still names `conversationRatePct`.
    - `sales`: `orderedProductSales`, `unitsOrdered`, `averageSellingPrice`, `orderGMS`, `unitsShipped` and `ordersShippedWithRevenue`. The B2B fields are "declared in the schema but are not yet served".
    - `promotion`: `promotionConversionRate`, `promotionGlanceViewCnt`, `promotionOrderedUnitsWithRevenue`, `promotionOrderedPrice`, `promotionDiscountPct`, `promotionDiscountAmt`, `promotionStartDate` and `promotionEndDate` ("in the local time zone for a store"), `promotionAsinStateType`, `promotionType` (e.g. "Best Deal, Deal of the Day, Lightning Deal, Sales Discount"), `promotionStatus`, `dealOurPrice`, `dealId` and `dealTitle`.
    - `search`: `query[] {queryKeyword, priceAndCountMetrics}` and `catalog {priceAndCountMetrics, clickRate, conversionRate, trafficSales}`.
  - Every numeric metric is a `…WithBenchmarking` type with `timeRangeBenchmarking {weekOverWeek, monthOverMonth, yearOverYear}`. "No benchmarking is available at `DAY` granularity."
  - Date behaviour:
    - Weekly: "The `startDate` is rolled back to the preceding Sunday and the `endDate` is rolled back to the preceding Saturday".
    - Monthly: the range is snapped to whole months.
    - "Daily: No adjustment is applied."
    - "The `endDate` is additionally capped to the most recent date for which all requested metrics have data."
    - Periods requested "within one to two business days" contain nulls.
  - Freshness: "All metrics in the seller analytics dataset are ready after 34 hours. Data for a given day is generally available at 10 AM local time two days later."
  - Nulls: "Requesting an incompatible combination is not an error"; a metric not available at the grouping "is returned as null for those rows", and the guide says to read such a null "as 'this metric is not available at this granularity' rather than as 'this metric was zero'".
  - Rights: every field carries `@paamRights` (e.g. `analytics_sales_and_traffic_view_pa`) and `@resultRetention(duration: "P30D")`. The guide names two access levels, "Sales and traffic access" and "Sales and lending access". The Data Kiosk API's operations (`createQuery`, `getQuery`, `getQueries`, `getDocument`, `cancelQuery`) list Brand Analytics as the required role.
  - The time zone of a `DAY` is not stated in the schema or the guide (section N).

  [official] (analytics_sellerAnalytics_2025_03_31.graphql, https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_sellerAnalytics_2025_03_31.graphql; Seller Analytics Dataset Use Case Guide, https://developer-docs.amazon/sp-api/docs/seller-analytics-dataset-guide (page `updatedAt: 2026-09-30`); Data Kiosk API, https://developer-docs.amazon/sp-api/docs/data-kiosk-api; all read 2026-11-09)

  The join keys against the ad side are `asin` or `msku`, with `marketplaceId`, on the day. The ad side's day is the profile's `timezone` in v3 and each campaign's `timeZone.value` in v1. The Seller Analytics day has no stated zone. The ASIN on the ad side "may differ in format and length from a standard 10-character ASIN" (below). [official] (as cited; Profiles; Dates and historical data retention; Reporting columns (version 3))
- RULE, the Finances event. `ProductAdsPaymentEvent` carries:
  - `postedDate`;
  - `transactionType` (`charge` or `refund`);
  - `invoiceId`;
  - `baseValue`, `taxValue` and `transactionValue` (= base + tax).

  Its description is "A Sponsored Products payment event." [official] (financesV0.json, https://github.com/amzn/selling-partner-api-models/blob/main/models/finances-api-model/financesV0.json, read 2026-11-09)
- RULE, the keys on the ad side.
  - v3 `advertisedAsin`, `advertisedSku` and `purchasedAsin`, with the caution that the value "may differ in format and length from a standard 10-character ASIN".
  - v1 `advertisedProduct.id` with `advertisedProductMarketplace.value`, `advertisedProductSku.value`, and `convertedProduct.id` with `convertedProductMarketplace.value`.
  - Currency from `campaignBudgetCurrencyCode` or `budgetCurrency.value`.
  - The marketplace from the profile's `accountInfo.marketplaceStringId`.

  [official] (Reporting columns (version 3); Advertised product; Advertised product SKU; Converted product; Profiles; all above). [seat] A `ProductAdsPaymentEvent` reads as an invoice posting, not a daily cost line.

### P. Amazon's MCP reporting tools

- RULE.
  - Amazon's reporting skill for its MCP server names the tools `account_management-query_advertiser_account`, `ads_accounts-list_ads_accounts`, `manager_accounts-get_manager_accounts`, `reporting-create_report` and `reporting-retrieve_report`.
  - The tool list `mcp/reporting.json` also has `create_campaign_report`, `create_product_report`, `create_inventory_report` and `delete_report`.
  - The account-context skill separates `profileId` from `advertiserAccountId` (`amzn1.ads-account.g.…`).
  - On 2026-11-09 the CDN copies of the skill pages held summaries only.

  [official] (Ads Reporting Skill, https://advertising.amazon.com/API/docs/en-us/mcp/skills/skills-library/reporting; MCP reporting tools, https://advertising.amazon.com/API/docs/en-us/mcp/reporting.json; Account Context Identifiers Skill, https://advertising.amazon.com/API/docs/en-us/mcp/skills/skills-library/account-context-identifiers; all read 2026-11-09). Using them as tools is `beyond/automation-and-amazon-tools.md`.

## What practitioners add

- [opinion] **How long the console keeps reports.** Intentwise (Michael Waters, "Explained: How long does Amazon keep your ad reports", 2023-04-23) gives these console look-backs:
  - Targeting 90 days, Search Term 60, Advertised Products 90, Purchased Products 60;
  - for the API (not the console): SP 95 days since v3, SB and SD 60.

  The advice is to save the data proactively, because it ages out. SellerApp (Ankitha Nagaraj, 2026-09-29) gives a newer console table:
  - SP: Search Term 65, Targeting 90, Advertised 90, Campaign 5 years, Budget 2 years, Placement 60, Purchased 60, Performance Over Time 90, Search Term Impression Share 90, Gross and Invalid 365;
  - SB: Keyword 90, Search Term 65, Attributed Purchases 5 years;
  - change history 90 days;
  - API look-back for SB 731 days.

  The two disagree on SP Search Term (60 against 65), which matches the v3 API's 65. Neither figure could be checked against Amazon's help page, which does not serve to a GET.
- [opinion] **Freshness and when to pull again.** emax digital's Knowledge Hub ("Data Lag and Refresh Schedules", undated) says it pulls period by period, most recent first, and that its own first backfill can take up to 7 days. In its Amazon Retail Analytics section it says "All reports accessible through the SP-API are subject to a minimum delay of 72 hours". It gives API look-backs of SP, ST and DSP 95 days, SD 65 and SB 60. It says deviations between its hub and the console "of up to 5% are anticipated per Amazon's documentation", which matches Amazon's 5% support line.

  Openbridge Support ("Amazon Advertising Attribution, Definitions, and Timing", 2024-12-13) says:
  - sales, ACOS and other data "can take up to 48 hours to populate", and "Data will be more accurate 3-5 days from the current date";
  - lock-screen ads data can take up to 14 days;
  - it re-pulls a rolling 60 days daily, at 1, 3, 7, 14, 30 and 59 days;
  - Amazon understated sales for 6/4/2020–6/8/2020 "due to manual backfill of data" (alert of June 29, 2020);
  - in Amazon Attribution, the last 48 hours are partial.
- [opinion] **Restatement as practitioners see it.** Optmyzr (Lakshmi Padmanaban, "Why Your Amazon Ads Report Is Lying to You (And What It's Not Showing)", 2026-04-08), linking Amazon's version 2 reporting FAQ and two Amazon Ads help pages, says:
  - sales are dated by the ad interaction;
  - cancellations within 72 hours are deducted, which can take up to 7 days;
  - "any report covering the last 28 days should be treated as provisional".

  Helium 10 (Vince Montero, "What Are Amazon Attribution Windows, and Why Are They Important?", published 2022-03-24, modified 2022-08-26) says:
  - sales data can take up to 12 hours to update;
  - cancellations and invalid clicks are removed within 72 hours;
  - attribution is credited to the click date;
  - the windows are SP 7 days, SB 14 and SD 14;
  - before treating a day as settled, wait 8 days for SP and 15 for SB and SD;
  - Helium 10 Ads updates its data from Amazon every 24 hours.
- [opinion] **A dissent on dating.** Ad Badger ("Attribution Window Blind Spots: How 14-Day Windows Quietly Wreck Your Decisions", by "The Badger", 2026-08-13) says:
  - SP, SB and SD use 14-day click attribution, and SD adds 14-day view-through;
  - "Amazon's standard advertising reports are built by order date, not by click date";
  - decisions should "Require both a minimum sample size AND a minimum age";
  - maturity is about 3–5, 7–10 and 14 days, depending on the category.

  The order-date claim contradicts Amazon's FAQ ("conversions are reported on the date of the ad interaction"). The 14-day claim contradicts Amazon's v1 overview for SP sellers (7-day base metric). Amazon's own wording stands; this entry records the dissent.
- [opinion] **Time zones.** Fivetran's Amazon Ads connector documentation says:
  - "Amazon Ads uses the time zone set by the profile to request the report";
  - its daily rollback syncs for SP and SD "depend on the Attribution Window setting";
  - SB is always 14 days;
  - retention is SP 95, SD 60, SB v2 60 and SB v3 95.

  Its SD figure (60) disagrees with Amazon's 65. Its SB v3 figure (95) disagrees with Amazon's 60 for most SB types (SB purchased product keeps 731 days). Openbridge ("Understanding Timezones Within Amazon Seller Central and Amazon Advertising", 2024-09-27) says Amazon's systems run on UTC while Seller Central shows Pacific time in NA. Nova (novadata.io "Time zones", "Checked against Nova's code on October 29, 2026") says:
  - ad metrics follow the profile time zone;
  - sales are counted on the marketplace's day;
  - "a UK Ads profile counts on London time, UK sales on Paris time, one hour apart".

  The three agree that ad days and sales days can sit on different clocks. They disagree on what the sales clock is.
- [opinion] **Developers on Amazon's public docs repository** (`amzn/ads-advanced-tools-docs`, issues read 2026-11-09; none has an Amazon answer):
  - #456 (bhaskardabhi-spreetail, 2026-05-04): duplicate v1 rows for the same `date.value` and `searchTerm.value`.
  - #476 (mtsanko, 2026-07-22): around 2026-07-14/15, `matchedTarget.value` stopped returning customer search terms and now returns only a product-page ASIN on Sponsored Display rows. The change was retroactive: historical dates re-requested come back blank. Together with the click-only `searchTerm.value`, this leaves no v1 view of search terms for unclicked impressions. This matches the dimension page's "Sponsored Display only". It explains why an earlier lead (listing playbook paid-keywords research, read 2026-10-14) found `matchedTarget.value` usable for search terms.
  - #453 (cn-knight, 2026-04-28): through the MCP reporting tools, no target or keyword id field is accepted (`400013`). The dimension library documents `adGroupTarget.id` (open question 10).
  - #467 (matthieuauger, 2026-07-01): a global EU account's v1 reports returned zero rows for DE and GB, while v2 and v3 per-profile reports had the data.
  - #501 (joexu-svg, 2026-09-18): persistent `429` on `POST /reporting/reports` for SB v3 in NA and EU. A second developer (2026-09-24) reports "Report generation failed due to an internal error" for most SB v3 requests.
  - #439 (wolendranh, 2026-03-26): Sponsored Television is not returned in v1, and a keyword dimension is missing from the v1 docs.
- [opinion] **A community SDK.** The `python-amazon-ad-api` library (denisneuf, GitHub, read 2026-11-09) wraps v3 with the OpenAPI wording ("Report generation can take as long as 3 hours"; DELETE "to cancel a report in a PENDING status") and offers `GZIP_JSON` only. Its `specs/` directory bundles both OpenAPI models (`OfflineReport_prod_3p.json`, `AmazonAdsAPIALLReportsContract_prod_3p.json`).

- [opinion] **Search terms below a privacy threshold** (gap fill, 2026-11-09). Nova ("How does Nova read search terms and impression share?", novadata.io, "Checked against Nova's code on 2026-10-29") says Nova reads the search term report three times a day for SP and daily for SB. It says "Amazon lists a search mostly when it got at least one click. Searches below Amazon's privacy threshold are grouped and show without the search text." It does not say which reporting version it reads, or what the grouped row is called. It also says Amazon keeps search term reports "for about 65 days", and gives top-of-search impression share as "Per target and day".
- [opinion] **Hourly keyword-by-placement rows from Stream v1.** Intentwise's Analytics Cloud data model ("Amazon Marketing Stream", docs.intentwise.com, undated) lists its SP Stream tables `ad_marketingstream_traffic` and `ad_marketingstream_conversions` with `time_window_start, placement, campaign_id, ad_group_id, keyword_id, keyword_text, match_type, ad_id` in one row. Its SD tables carry `target_id` and no placement. No table carries a search term. This matches Amazon's `sp-traffic` schema (section K). Perpetua (Tiffany Luk, "How to leverage hourly Amazon performance and Share of Voice data", 2022-06-21) recommends using Stream's hourly data for bid changes "within dayparting strategies".

Where practitioners disagree:
- the console retention of SP search terms (60 or 65);
- SD and SB API retention (Fivetran against Amazon);
- the dating of conversions (Ad Badger against Amazon and everyone else);
- the sales-day clock (UTC, Pacific or marketplace-local).

## Published research

- [research] **Delayed conversion feedback.** Ktena, Tejani et al., "Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction", arXiv:1907.06558 (2019).
  - What was measured: "5 different loss functions" for learning when positive labels arrive late (RecSys '19).
  - Data: "668 million in-house data points" offline, plus online experiments.
  - Finding: "Naive strategies which consider any data point a negative example until a positive label becomes available tend to underestimate CTR". The best methods gave a "55% gain in revenue per thousand requests (RPMq) against naive log loss" online.
  - Transfer: the bias has a sign. A recent window read as complete under-counts conversions, so ROAS reads low and ACOS high on the newest days. The magnitude is a property of the authors' in-house ads data, not Amazon's.
- [research] Yasui, Morishita, Fujita and Shibata, "A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback", arXiv:2002.02068 (2020; WWW '20).
  - What it shows: "some positive instances at the training period are labeled as negative because some conversions have not yet occurred". The authors call the resulting change in label distributions a "feedback shift". They correct it with importance weighting, prove the correction consistent, and test it in offline and online experiments.
  - Transfer: same as above. Anything learnt or judged from recent days inherits the shift unless it waits out the delay or corrects for it.
- [research] Chapelle (Criteo), "Modeling delayed feedback in display advertising", KDD 2014 (Crossref metadata for DOI 10.1145/2623330.2623634, read 2026-11-09). This is the founding paper of the line above. Only its title, venue and date were confirmed: the ACM page served a bot challenge, and the author's PDF URL answered 404. No finding of it is stated here.
- [research] **Revised data.** Croushore, "Frontiers of Real-Time Data Analysis", Journal of Economic Literature 49(1), 2011 (abstract, Crossref, read 2026-11-09). This is a survey of how data revisions affect structural modelling, forecasting and monetary policy analysis, and of the "better real-time data sets" built around the world.
  - Transfer: an ads report is a vintage. A figure read on day 2 and the same figure read on day 40 are two releases of one number. Keeping the landed copy with its read date is how a later reader tells a changed decision from a restated number. The method transfers; the economics findings do not.
- [research] **Backoff with jitter.** Marc Brooker (AWS), "Exponential Backoff And Jitter", AWS Architecture Blog, 2015-03-04, with an update note of May 2023.
  - What was measured: a simulation of contending clients.
  - Finding: "The no-jitter exponential backoff approach is the clear loser". With jitter, "In the case with 100 contending clients, we've reduced our call count by more than half."
  - Transfer: many sellers polling Amazon's report queue from one client id are contending clients. Amazon's own Stream limits page links the AWS Builders' Library article on the same topic, and its Rate limiting page links this post.

## Stable enough for a skill

1. v3 reporting, Stream v1 and SP/SB v2 reporting stop delivering data on 2027-06-30. Reporting v1 and Stream v2 have been GA since 2026-09-30, and exports are unaffected. (Deprecations; Amazon Ads API v1 release notes; Amazon Ads reporting overview)
2. A v3 report is created with `POST /reporting/reports`, read with `GET /reporting/reports/{reportId}`, and cancelled while `PENDING` with `DELETE /reporting/reports/{reportId}`. Statuses: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`. (OfflineReport_prod_3p.json; Get started with version 3 reports)
3. A `COMPLETED` v3 report carries `url`, `urlExpiresAt` and `fileSize`. The file is gzip-compressed JSON: one array of row objects keyed by the requested column names. A `FAILED` report carries `failureReason`. (OfflineReport_prod_3p.json; Get started with version 3 reports)
4. An identical v3 request while one is processing answers `425` ("a duplicate of a processing request"). Amazon's direction is to wait for the existing report, keep report ids, and remove pending reports before resubmitting. (Get started with version 3 reports; Reporting and analytics component)
5. A v3 `groupBy` is required. Filters apply only if every `groupBy` value supports them. SP has no ad-group or placement type of its own; those come from `spCampaigns` grouped by `adGroup` or `campaignPlacement`. (Get started with version 3 reports; Campaign reports; Ad group reports; Placement reports)
6. v3 report types, `groupBy` values, filters, maximum ranges and retention are per type, on each type's page. Most allow 31 days per request, and retention is 95, 65 or 60 days. (v3 type pages)
7. Search term reports from the API, in v3 and v1, hold only terms with at least one click. A product-page placement without a keyword shows `*`. The console's search term report holds terms with impressions. (Search term reports; Sponsored ads reporting FAQ (version 3))
8. v3 SP columns carry 1, 7, 14 and 30-day windows, by click. The SB `purchases` and `sales` columns are 14 days by click or view. `sales14d` includes views for vCPM campaigns. (Reporting columns (version 3))
9. A v1 report is created, retrieved and deleted with `POST /adsApi/v1/{create,retrieve,delete}/reports`. Each answers `207`, with the result at `success[0]` or `error[0]`. One report per request. The account goes in `accessRequestedAccounts`, with no scope header. (AmazonAdsAPIALLReportsContract_prod_3p.json; Getting started with the Reporting API v1)
10. A `COMPLETED` v1 report lists up to 100 `completedReportParts`, each with its own pre-signed URL and expiry. Partitioned formats split into chunks of up to 1 GB uncompressed. Amazon's guidance is to poll once a minute. (AmazonAdsAPIALLReportsContract_prod_3p.json; Getting started with the Reporting API v1; New features)
11. v1 failures come in two kinds. Synchronous `400`s carry numbered codes. Asynchronous `FAILED` carries `failureCode` `001` (internal: try again) or `002` (too large: narrow the period, the accounts or the fields). Warnings (`NO_PERMISSION`, `PENDING_DEPRECATION`, `DATE_LIMITED`, open-ended) never stop a report. (Handling errors; New features)
12. A v1 query needs at least one metric, one level-of-detail dimension and one time dimension. A dimension attribute needs its primary key, and `metric.sales` needs `budgetCurrency.value`. Rows are the group-by of all dimensions. (Handling errors; Helpful concepts; Getting started with the Reporting API v1)
13. v1 base conversion metrics carry no window suffix. For SP they are the 7-day figure for sellers and the 14-day figure for vendors. For the other products they are 14 days. Promoted and halo are split by `productRelevance.value`. v3's `acosClicks*` and every 1-day and 30-day column have no v1 equivalent. (Overview of the Reporting v1 API; Reporting API v3 Report Type Migration Guide)
14. In v1 a missing value is `null` (JSON) or `""` (CSV), and a measured zero is `0`. (Helpful concepts)
15. v1 aggregates in each campaign's time zone and names it in `timeZone.value`. v2 and v3 report in the profile's time zone, which `GET /v2/profiles/{profileId}` returns as `timezone`. (Dates and historical data retention; Sponsored ads reporting FAQ (version 2); Profiles)
16. Clicks and impressions first appear within about 12 hours and are corrected by traffic validation afterwards. Conversions first appear within about 24 hours, are dated to the ad interaction, and are restated at 1, 7 and 28 days after the conversion. Amazon's pages give 42, 60 and 70 days as the horizon of change. (Sponsored ads reporting FAQ (version 3); Amazon Ads reporting overview; Stream v2 datasets)
17. Stream v2 delivers Parquet totals to the client's own S3 bucket and SQS queue, at least once. The record to keep is the one with the highest `streamBatch.version`. `ads-performance-v1` is hourly and `ads-converted-product-v1` daily, each with a 70-day restatement window. Thresholded values fall into an `(Other)` row. (Stream v2 pages)
18. Exports give the current metadata only: no history, 5 jobs in progress per endpoint, 1-hour URLs. (Exports overview; Get started with exports; Exports FAQ)
19. Sales and Traffic by ASIN is aggregated over the requested range, while by-date entries are account-level. SQP and Sales and Traffic weeks run Sunday–Saturday. Data Kiosk Economics week and month boundaries are UTC+0. (sellerSalesAndTrafficReport.json; Report Type Values – Analytics; analytics_economics_2024_03_15.graphql)
20. Audience bid-boost performance is a v3 report: `spAudiences` and `sbAudiences`, grouped by `campaign_bid_boost_segment`, with `segmentName` and `segmentClassCode`, 31 days per request and 95 days retained. The v3 availability table and the migration guide omit both, and no v1 or Stream v2 equivalent is mapped. (Audience reports; Sponsored ads report types (version 3); Reporting API v3 Report Type Migration Guide; Release notes index, January 24, 2025)
21. In v3, `topOfSearchImpressionShare` is offered on SP and SB campaign and targeting reports, per their type pages. In v1, `metric.topOfSearchImpressionShare` is incompatible with target, targeting, search term, hour and placement dimensions. (Campaign reports; Targeting reports; Reporting columns (version 3); Search impression share)
22. Amazon's v3-to-v1 map spells the target fields `adGroupTarget.id` (key), `targeting.value` (keyword or expression text) and `targetingMatchType.value`. `target.value` is flagged `PENDING_DEPRECATION` in Amazon's warning example. (Reporting API v3 Report Type Migration Guide; Target; Targeting; Targeting match type; New features)
23. Reporting v1 and the Stream datasets document no incompatibility among `placementClassification.value`, `adGroupTarget.id`, `targeting.value`, `searchTerm.value` and `hour.value`, and the base traffic and conversion metrics list all of them as compatible. Stream v1 `sp-traffic` and `sp-conversion` carry keyword, placement and hour in one row until 2027-06-30. (Placement classification; Hour; metric pages; Helpful concepts; Ads performance dataset; Sponsored Products performance datasets)
24. Stream v2 groups low-activity values of thresholded dimensions (`searchTerm.value` in `ads-performance-v1`) into an `(Other)` row, evaluated at the exact level of detail. The v1 pages say nothing about thresholds either way. (Datasets overview; Ads performance dataset; v1 pages)
25. Reporting v1 has no `425`, no idempotency key and no list operation. Over the concurrency limit, a create answers `429` (Limits page) or is "queued or receive[s] a 429" (reporting overview). (AmazonAdsAPIALLReportsContract_prod_3p.json; Limits and best practices; Amazon Ads reporting overview)
26. The legacy `/adsAccounts*` endpoints have been deprecated since July 2026 (`Warning: 299`, new integrations blocked, `404` from July 2027). Accounts are listed with `POST /adsApi/v1/query/advertiserAccounts`, whose items carry `advertiserAccountId`, `alternateIds` (`profileId`, `countryCode`) and `timeZoneIana`. (Deprecations; QueryAdvertiserAccount API)
27. Data Kiosk Seller Analytics gives per-ASIN or per-MSKU sessions, page views, featured-offer share, conversion rate, sales and promotion fields per `DAY`, `WEEK` (Sunday–Saturday) or `MONTH`, ready about 34 hours after the day. A metric not available at the grouping returns `null`. The day's time zone is not stated. (analytics_sellerAnalytics_2025_03_31.graphql; Seller Analytics Dataset Use Case Guide)

## What cx must read at run time

The door is `cx raw amazon-ads --origin <origin> --method <m> --path <p> [--header k=v] [--body file]`. The facts about it used here:
- origins `advertising-api.amazon.com`, `-eu` and `-fe`;
- the door attaches `Authorization` and the client-id header, and refuses a request naming them;
- a `429` lands as `provider_rate_limit` with no wait added;
- a POST lands as a change, "sent, outcome unknown";
- "A report's `url` is the box's own download, outside the door".

(`cx-amazon-ads` `skills/amazon-ads/SKILL.md` and `references/door.md`, read 2026-11-09)

**Which account to report on.**
- v3: the profile, as `--header Amazon-Advertising-API-Scope=<profileId>`. The profile is read from `GET /v2/profiles`, whose items carry `profileId`, `countryCode`, `currencyCode`, `timezone` and `accountInfo.{marketplaceStringId,id,type}`.
- v1 and Stream v2: the Global Account id `amzn1.ads-account.g.*`, read from `POST /adsApi/v1/query/advertiserAccounts`. The body `{}` returns global accounts; page through `nextToken` until it is absent, including empty pages. Each item carries `advertiserAccountId`, `alternateIds[{countryCode, entityId, profileId}]` and `timeZoneIana`. The legacy `POST /adsAccounts/list` and `GET /adsAccounts/{accountId}` are deprecated (`Warning: 299`; new integrations blocked since July 2026; `404` from July 2027). Whether the client id in use is on Amazon's allowlist for the legacy calls is not stated on any page read; a legacy call's reply and its `Warning` header show it.
- Where each lives: Profiles; QueryAdvertiserAccount API; Deprecations. `method/ads-api-surface.md` owns these calls.

**v3, one report.**
- Create: `POST /reporting/reports`, `--header Content-Type=application/vnd.createasyncreportrequest.v3+json`. Body `{name?, startDate, endDate, configuration: {adProduct, reportTypeId, groupBy[], columns[], filters?, timeUnit, format: "GZIP_JSON"}}`.
  - The reply is `200` `{reportId, status, ...}`.
  - It can also be `400` or `422`, which mean the ask is wrong, read `detail`; `425`, a duplicate is processing; `429`, which may carry `Retry-After`; or `500`.
  - The type's `reportTypeId`, `groupBy` values, filters, columns, maximum range and retention are read from the type page under `guides/reporting/v3/report-types/` on the docs CDN. The `format` enum is read from `OfflineReport_prod_3p.json`.
- Read: `GET /reporting/reports/{reportId}` returns `status`, `url`, `urlExpiresAt`, `fileSize`, `failureReason`, `generatedAt` and `updatedAt`.
- Cancel while `PENDING`: `DELETE /reporting/reports/{reportId}`.
- Download: `url` (pre-signed S3, outside the door), then gunzip, then one JSON array.
- Time zone of the rows: the profile's `timezone`.

**v1, one report.**
- Create: `POST /adsApi/v1/create/reports`, `--header Content-Type=application/json`. Body `{accessRequestedAccounts: [{advertiserAccountId}], reports: [{format, periods: [{datePeriod: {startDate, endDate}}], query: {fields: [...], filter?}, currencyOfView?}]}`.
  - The reply is `207` with `success[0].report.reportId` and `status`, or `error[0]`. A synchronous `400` carries `{code, message}`.
- Read: `POST /adsApi/v1/retrieve/reports` with `{reportIds: [id]}`. It returns `status`, `completedReportParts[{url, urlExpirationDateTime, sizeInBytes}]`, `failureCode`, `failureReason`, `warnings[{field, warningCodes[]}]`, `completedDateTime` and `lastUpdatedDateTime`.
- Delete: `POST /adsApi/v1/delete/reports` with `{reportIds: [id]}`.
- Fields: dimension and metric ids, with their requirements and incompatibilities, are read from the dimension and metric pages under `guides/reporting/ads-v1/` and from the `400004` and `400006` messages. Formats, limits and enums are read from `AmazonAdsAPIALLReportsContract_prod_3p.json`. Retention and maximum range per time dimension are read from `guides/reporting/ads-v1/dates`.
- Time zone of the rows: `timeZone.value` in the row, when requested.
- Target fields: `adGroupTarget.id` (key), `targeting.value`, `targetingMatchType.value`, as in Amazon's migration guide. A `PENDING_DEPRECATION` warning in `warnings[]` names any field Amazon is retiring.
- Placement by target, or by hour: one query with `placementClassification.value`, `adGroupTarget.id` and/or `hour.value` plus base metrics. The `207` (accepted) or `400004` (with the incompatible pair named) is the service's answer. `metric.topOfSearchImpressionShare`, `metric.impressionShare` and `metric.impressionShareRank` are refused with target, placement and hour dimensions (Search impression share page).
- Thresholded rows: the literal value `(Other)` in `searchTerm.value` (or any high-cardinality dimension) in the landed rows.
- A second create while one is running: `429` (the Rate limiting page says a `429` carries `Retry-After` in seconds) or queued. The receipt's `reportId` is the only way back to a report, because there is no list operation.

**Audience bid boosting (v3 until 2027-06-30).** `POST /reporting/reports` with `adProduct` `SPONSORED_PRODUCTS` or `SPONSORED_BRANDS`, `reportTypeId` `spAudiences` or `sbAudiences`, `groupBy` `["campaign_bid_boost_segment"]`, columns from the Audience reports page (`segmentName`, `segmentClassCode`, campaign and base metrics), `timeUnit` `SUMMARY` or `DAILY`, `format` `GZIP_JSON`. Range and retention: the Audience reports page. In v1, Sponsored Products rows can carry `audienceSegment.id` with its required `audienceSegment.classCode`, `.name`, `.source`, `.type` and `audienceSegmentCountry.code`. Amazon does not map this to `spAudiences`.

**Hourly, keyword and placement until 2027-06-30.** Stream v1 datasets `sp-traffic` and `sp-conversion` (subscribed through `/streams/subscriptions`; Firehose or SQS) carry `keyword_id`, `placement` and `time_window_start`. Their time zone is the profile's. Stream v2 `ads-performance-v1` carries `hour.value`, `placementClassification.value`, `adGroupTarget.id` and thresholded `searchTerm.value` in its record key. Both need infrastructure outside the door (seat's position).

**Metadata beside a report.** `POST /campaigns/export`, `/adGroups/export`, `/targets/export` and `/ads/export`, then `GET /exports/{exportId}`, then the URL.

**Joins.**
- SP-API `GET_SALES_AND_TRAFFIC_REPORT` (`reportOptions` `dateGranularity`, `asinGranularity`); its fields are in `sellerSalesAndTrafficReport.json`.
- SQP.
- Data Kiosk `analytics_economics_2024_03_15` `ads { adTypeName charge }`.
- Data Kiosk `analytics_sellerAnalytics_2025_03_31` `sellerAnalyticsView(startDate, endDate, aggregateBy, currencyCode, marketplaceId)` → `metrics { groupByKey { asin msku marketplaceId } metrics { traffic { sessions pageViews glanceViews featureOfferPct conversionRatePct } sales { orderedProductSales unitsOrdered } promotion { … } } }`. Field names and rights come from the schema in `amzn/selling-partner-api-models`. The latest available date comes from the `endDate` cap or the error message "The latest date these metrics are available at the <granularity> granularity is <date>".
- Finances `ProductAdsPaymentEvent`.

These go through `cx raw amazon-sp-api` and the listing playbook's `report.sh`.

### The report reader: report.sh, and what v3 and v1 change

[seat] The listing playbook's `scripts/report.sh` (read 2026-11-09) makes one SP-API report run from ask to document:
- It lands each report in `<tree>/reports/<reportType>/<ask>/<n>/`, with `receipt.json` (report id, Amazon's status, createdTime), every reply under its own name, and the document as `report.<ext>`.
- It carries on the ask's unlanded report instead of creating a new one.
- It makes one wait with a ceiling, `--wait`, and polls every `--every` seconds.
- It uses the presigned link once, never prints it, and strips it from the landed reply.
- It has no limiter and no retry of its own.
- Exit codes: 0 Amazon's terminal status; 1 a call or the download failed; 2 usage; 3 still queued.

The same shape carries over to Amazon Ads. These are the facts it rests on, per version.

| Step | SP-API (`report.sh`) | Ads v3 | Ads v1 |
|---|---|---|---|
| The ask's identity | type, marketplaces, start, end, options | origin, profile id, `reportTypeId`, `adProduct`, `groupBy`, `columns`, `filters`, `timeUnit`, `startDate`, `endDate`, `format` | origin, `advertiserAccountId`(s), `fields`, `filter`, period, `format`, `currencyOfView` |
| A safe directory name | type matches `[A-Z0-9_]` | `reportTypeId` is camelCase letters (`spSearchTerm`) | no type at all; the ask's checksum names it |
| Create | `POST /reports/2021-06-30/reports` → `reportId` | `POST /reporting/reports` → `200` `reportId`; `425` when the same ask is processing | `POST /adsApi/v1/create/reports` → `207` `success[0].report.reportId` or `error[0]`; synchronous `400` codes |
| Poll | `GET` → `processingStatus` | `GET /reporting/reports/{id}` → `status` | `POST /adsApi/v1/retrieve/reports {reportIds}` → `status`; the door treats a POST as a change |
| Terminal | `DONE`, `CANCELLED`, `FATAL` | `COMPLETED`, `FAILED` | `COMPLETED`, `FAILED` |
| Still queued | `IN_QUEUE`, `IN_PROGRESS` | `PENDING`, `PROCESSING` | `PENDING`, `PROCESSING` |
| Failure detail | a FATAL explanation document | `failureReason` | `failureCode` (`001`, `002`), `failureReason`; `warnings` on success |
| Link | `getReportDocument` → `url` + `compressionAlgorithm` | `url` and `urlExpiresAt` in the report itself | one `url` and `urlExpirationDateTime` per part, up to 100 parts |
| Body | GZIP or plain; JSON, XML or TSV | gzip, then a JSON array | `CSV`, `GZIP_JSON`, or partitioned chunks of up to 1 GB each |
| Cancel | `cancelReport` | `DELETE` while `PENDING` | `POST /adsApi/v1/delete/reports` |
| Concurrency | per type and seller | report queue per region; `425` per identical ask | one concurrent report per client id or per advertiser (Amazon's pages disagree); over it, `429` or queued; no `425`, no idempotency key, no list operation |

Consequences that are facts of Amazon's API:
- A v3 `425` answers a create whose twin is processing. The model's error body is `{code, detail}`, and Amazon does not say that it names the twin's id. The receipt's `reportId` is what lets the next run carry on.
- A v3 report is read whole from one link. A v1 report may be several parts, each with its own expiry, which in Amazon's example is minutes after completion. A part counts as landed only when every part has landed.
- v1 rows carry dotted field ids (`metric.clicks`) as keys or headers. v3 rows carry column names.
- A v1 receipt keeps `warnings`, because a completed report can still carry redacted fields (`NO_PERMISSION`) or a field not covering the range (`DATE_LIMITED`).
- A day landed early is a vintage (sections J and N). Its read time sits in the receipt beside the ask, so a later run of the same ask over the same dates yields a second landed report, not an overwrite. That is what `report.sh` already does with `<n>/`.

## Pages read

All on 2026-11-09 unless noted. "CDN" means the Markdown copy at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`. A = `https://advertising.amazon.com/API/docs/en-us/`.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Docs host index | https://d3a0d0y2hgofx6.cloudfront.net/llms.txt | official | 2026-11-09 | that pages are a JS shell; the CDN Markdown |
| Docs table of contents | https://d3a0d0y2hgofx6.cloudfront.net/en-us/toc2.json | official | 2026-11-09 | exact page paths |
| Amazon Ads reporting overview | A + guides/reporting/overview | official | 2026-11-09 | surfaces, shutoffs, freshness, per-advertiser concurrency, reports against exports |
| Overview of the Reporting v1 API | A + guides/reporting/ads-v1/overview | official | 2026-11-09 | per-client-id concurrency; base metrics 7 d sellers / 14 d vendors; promoted and halo |
| Getting started with the Reporting API v1 | A + guides/reporting/ads-v1/quickstart | official | 2026-11-09 | create, retrieve, statuses, polling once a minute, parts |
| Limits and best practices (v1) | A + guides/reporting/ads-v1/limits | official | 2026-11-09 | limits per client id, as low as 1; backoff |
| Dates and historical data retention | A + guides/reporting/ads-v1/dates | official | 2026-11-09 | campaign time zone; retention and range per time dimension |
| Building queries | A + guides/reporting/ads-v1/building-queries | official | 2026-11-09 | filters; all products and campaigns by default |
| Handling errors | A + guides/reporting/ads-v1/error-handling | official | 2026-11-09 | 400 codes, failure codes 001 and 002, HTTP classes |
| Helpful concepts | A + guides/reporting/ads-v1/helpful-concepts | official | 2026-11-09 | time dimensions; primary keys; null against zero; "up to 5 accounts" |
| New features | A + guides/reporting/ads-v1/new-features | official | 2026-11-09 | partitioned formats; currency of view; warnings |
| SP campaigns (v1 report type) | A + guides/reporting/ads-v1/report-types/sp-campaigns | official | 2026-11-09 | migration example fields |
| SP search term (v1) | A + guides/reporting/ads-v1/report-types/sp-search-term | official | 2026-11-09 | migration example; duplicate `target.value` |
| SP targeting (v1) | A + guides/reporting/ads-v1/report-types/sp-targeting | official | 2026-11-09 | migration example |
| SP advertised product (v1) | A + guides/reporting/ads-v1/report-types/sp-advertised-product | official | 2026-11-09 | example lacking the marketplace field |
| SP purchased product (v1) | A + guides/reporting/ads-v1/report-types/sp-purchased-product | official | 2026-11-09 | converted product fields |
| Dimensions library | A + guides/reporting/ads-v1/dimensions/library | official | 2026-11-09 | dimension categories and ids |
| Search term dimension | A + guides/reporting/ads-v1/dimensions/targeting/search-term | official | 2026-11-09 | SP and SB; v3 `searchTerm` |
| Target dimension | A + guides/reporting/ads-v1/dimensions/targeting/target | official | 2026-11-09 | `adGroupTarget.id` primary key and attributes |
| Targeting dimension | A + guides/reporting/ads-v1/dimensions/targeting/targeting | official | 2026-11-09 | keyword, product or category |
| Targeting match type | A + guides/reporting/ads-v1/dimensions/targeting/targeting-match-type | official | 2026-11-09 | match type |
| Matched target | A + guides/reporting/ads-v1/dimensions/targeting/matched-target | official | 2026-11-09 | Sponsored Display only |
| Placement classification | A + guides/reporting/ads-v1/dimensions/supply/placement-classification | official | 2026-11-09 | SP, SB, SD, ST |
| Product relevance | A + guides/reporting/ads-v1/dimensions/product/product-relevance | official | 2026-11-09 | promoted and halo |
| Converted product | A + guides/reporting/ads-v1/dimensions/product/converted-product | official | 2026-11-09 | needs marketplace; v3 `purchasedAsin` |
| Advertised product | A + guides/reporting/ads-v1/dimensions/product/advertised-product | official | 2026-11-09 | needs marketplace |
| Budget currency | A + guides/reporting/ads-v1/dimensions/currency/budget-currency | official | 2026-11-09 | v3 `campaignBudgetCurrencyCode` |
| Date dimension | A + guides/reporting/ads-v1/dimensions/time/date | official | 2026-11-09 | daily |
| Hour dimension | A + guides/reporting/ads-v1/dimensions/time/hour | official | 2026-11-09 | hourly, LONG |
| Metrics library | A + guides/reporting/ads-v1/metrics/library | official | 2026-11-09 | metric ids |
| Purchases metric | A + guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases | official | 2026-11-09 | compatible dimensions; v3 names |
| Search impression share | A + guides/reporting/ads-v1/metrics/impression-share/search | official | 2026-11-09 | required and incompatible dimensions |
| Clicks metric | A + guides/reporting/ads-v1/metrics/delivery/clicks | official | 2026-11-09 | clicks = gross − invalid |
| Costs metric | A + guides/reporting/ads-v1/metrics/costs-and-fees/costs | official | 2026-11-09 | `metric.totalCost` needs `budgetCurrency.value`; v3 `spend` |
| Advertised product SKU | A + guides/reporting/ads-v1/dimensions/product/advertised-product-sku | official | 2026-11-09 | `advertisedProductSku.value` |
| Reports API v1 OpenAPI model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLReportsContract_prod_3p.json | official | 2026-11-09 | every v1 operation, limit and enum |
| Offline Report 3.0 OpenAPI model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/OfflineReport_prod_3p.json | official | 2026-11-09 | every v3 operation, status and enum |
| Get started with version 3 reports | A + guides/reporting/v3/get-started | official | 2026-11-09 | the call sequence; 425; 429; download |
| Sponsored ads reporting overview (v3) | A + guides/reporting/v3/overview | official | 2026-11-09 | gzip JSON; SB preview; Stream for more frequency |
| Sponsored ads report types (v3) | A + guides/reporting/v3/report-types/overview | official | 2026-11-09 | availability table |
| Campaign reports | A + guides/reporting/v3/report-types/campaign | official | 2026-11-09 | spCampaigns and others; groupBy and filters |
| Ad group reports | A + guides/reporting/v3/report-types/ad-group | official | 2026-11-09 | sbAdGroup, sdAdGroup; no SP type |
| Ad reports | A + guides/reporting/v3/report-types/ad | official | 2026-11-09 | sbAds |
| Placement reports | A + guides/reporting/v3/report-types/placement | official | 2026-11-09 | sbCampaignPlacement; no SP type |
| Targeting reports | A + guides/reporting/v3/report-types/targeting | official | 2026-11-09 | keywordType filters; columns |
| Search term reports | A + guides/reporting/v3/report-types/search-term | official | 2026-11-09 | click-only; `*` |
| Advertised product reports | A + guides/reporting/v3/report-types/advertised-product | official | 2026-11-09 | spAdvertisedProduct, sdAdvertisedProduct |
| Purchased product reports | A + guides/reporting/v3/report-types/purchased-product | official | 2026-11-09 | the "not advertised" products; SB 731 d |
| Gross and invalid traffic reports | A + guides/reporting/v3/report-types/gross-and-invalid-traffic | official | 2026-11-09 | 365 d; metrics |
| Prompt Ad Extension reports | A + guides/reporting/v3/report-types/prompt-ad-extension | official | 2026-11-09 | prompts; US; XLSX |
| Video Ad Extension reports | A + guides/reporting/v3/report-types/video-ad-extension | official | 2026-11-09 | ids match other SP reports |
| Benchmarks reports | A + guides/reporting/v3/report-types/benchmarks | official | 2026-11-09 | brand owners; from 2025-01-01; every 48 h |
| Conversion path reports | A + guides/reporting/v3/report-types/conversion-path | official | 2026-11-09 | 90 d range, 95 d retention, `SUMMARY`, `brandConversionPath`, brand owners |
| Reporting columns (v3) | A + guides/reporting/v3/columns | official | 2026-11-09 | column definitions |
| Sponsored ads reporting FAQ (v3) | A + guides/reporting/v3/faq | official | 2026-11-09 | freshness, restatement, cadence, size, console terms |
| Version 2 reporting overview | A + guides/reporting/v2/overview | official | 2026-11-09 | v2 shutoff; 60 days; 5% discrepancy |
| Sponsored ads reporting FAQ (version 2) | A + guides/reporting/v2/faq | official | 2026-11-09 | profile time zone; restatement text |
| Reporting in the advertising console vs. API (version 2) | A + guides/reporting/v2/advertising-console | official | 2026-11-09 | console-only reports; column mapping |
| Rate limiting | A + reference/concepts/rate-limiting | official | 2026-11-09 | Retry-After; queue-sized report limits; backoff |
| Limits, constraints, and quotas | A + reference/concepts/limits | official | 2026-11-09 | P99 12 h, 72 h, 15 min |
| Reporting and analytics component | A + guides/amazon-ads-well-architected-framework/reporting-and-analytics-component | official | 2026-11-09 | report-id tracking; 425; 31 days; time zones |
| Deprecations | A + release-notes/deprecations | official | 2026-11-09 | 2027-06-30; SB rank fields; benchmarks |
| Amazon Ads API v1 release notes | A + release-notes/ads-api-v1 | official | 2026-11-09 | GA 2026-09-30; warnings; retention 24 months |
| Release notes index | A + release-notes/index | official | 2026-11-09 | entry list |
| Amazon Marketing Stream v2 overview | A + guides/amazon-marketing-stream/v2/overview | official | 2026-11-09 | Parquet, S3, SQS, regions |
| Data delivery | A + guides/amazon-marketing-stream/v2/data-delivery | official | 2026-11-09 | totals; versions; at least once; UTC batches |
| Datasets overview | A + guides/amazon-marketing-stream/v2/datasets/overview | official | 2026-11-09 | thresholds; disjoint rows |
| Ads performance dataset | A + guides/amazon-marketing-stream/v2/datasets/ads-performance | official | 2026-11-09 | hourly; 70 d; dimensions |
| Ads converted product dataset | A + guides/amazon-marketing-stream/v2/datasets/ads-converted-product | official | 2026-11-09 | daily; 70 d; thresholded `convertedProduct.id` |
| Stream v2 FAQ | A + guides/amazon-marketing-stream/v2/faq | official | 2026-11-09 | backfill; fees; manager accounts |
| Reporting API v3 Report Type Migration Guide | A + guides/amazon-marketing-stream/v2/report-type-migration-guide | official | 2026-11-09 | v3-to-v1 field map |
| Dataset migration guide | A + guides/amazon-marketing-stream/v2/dataset-migration-guide | official | 2026-11-09 | v1 to v2 datasets |
| Get started (Stream v2) | A + guides/amazon-marketing-stream/v2/get-started | official | 2026-11-09 | onboarding steps |
| Create a subscription | A + guides/amazon-marketing-stream/v2/create-a-subscription | official | 2026-11-09 | account id formats; body; ACTIVE |
| Limits (Stream v2) | A + guides/amazon-marketing-stream/v2/manage-subscriptions/limits | official | 2026-11-09 | 5 destinations; 25 rps; 256 MB |
| Amazon Marketing Stream overview (v1) | A + guides/amazon-marketing-stream/overview | official | 2026-11-09 | deltas; shutoff |
| Amazon Marketing Stream FAQ (v1) | A + guides/amazon-marketing-stream/amazon-marketing-stream-faq | official | 2026-11-09 | v1 behaviour |
| Exports overview | A + guides/exports/overview | official | 2026-11-09 | metadata; no history |
| Get started with exports | A + guides/exports/get-started | official | 2026-11-09 | endpoints; media types |
| Exports FAQ | A + guides/exports/faq | official | 2026-11-09 | 5 jobs; 1 h URLs; 24 h; once or twice a day |
| Profiles (v2 reference) | A + reference/2/profiles (CDN `NoSuchKey`; read as https://d3a0d0y2hgofx6.cloudfront.net/en-us/profiles/3-0/openapi.yaml) | official | 2026-11-09 | `timezone` ("used for all date-based campaign management and reporting"), `currencyCode`, `accountInfo` |
| Profiles (account management guide) | A + guides/account-management/authorization/profiles | official | 2026-11-09 | profile per country |
| Retrieving accounts | A + guides/account-management/accounts/retrieve-accounts | official | 2026-11-09 | global account ids; statuses |
| QueryAdvertiserAccount API | A + guides/account-management/query-advertiser-accounts | official | 2026-11-09 | account query |
| Search term reports in bulksheets | A + no-code-tools/bulksheets/bulksheets-search-term-report | official | 2026-11-09 | 7-day; date range ignored; inverted CTR and CVR |
| Understand bulksheets campaign data | A + no-code-tools/bulksheets/understand-bulksheets-data | official | 2026-11-09 | download options |
| Ads Reporting Skill (MCP) | A + mcp/skills/skills-library/reporting | official | 2026-11-09 | tool names; partly readable |
| MCP reporting tools | A + mcp/reporting.json | official | 2026-11-09 | tool list |
| Account Context Identifiers Skill (MCP) | A + mcp/skills/skills-library/account-context-identifiers | official | 2026-11-09 | profileId against advertiserAccountId |
| How to measure and improve your campaigns | https://advertising.amazon.com/library/guides/measure-improve-campaigns | official | 2026-11-09 | "at least two weeks" |
| Advertising console (library) | https://advertising.amazon.com/library/guides/advertising-console | official | 2026-11-09 | "Amazon Ads Agent" |
| Report Type Values – Analytics | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics.md | official | 2026-11-09 | Sales and Traffic, SQP options; PST vendor |
| sellerSalesAndTrafficReport.json | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/reports/sellerSalesAndTrafficReport.json | official | 2026-11-09 | by date and by ASIN shapes |
| Data Kiosk economics schema | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_economics_2024_03_15.graphql | official | 2026-11-09 | ads charges; UTC+0 boundaries |
| Data Kiosk sales and traffic schema | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_salesAndTraffic_2024_04_24.graphql | official | 2026-11-09 | week and month snapping; two years |
| Finances v0 model | https://github.com/amzn/selling-partner-api-models/blob/main/models/finances-api-model/financesV0.json | official | 2026-11-09 | ProductAdsPaymentEvent |
| amzn/ads-advanced-tools-docs repository | https://github.com/amzn/ads-advanced-tools-docs | official | 2026-11-09 | repo layout; no reporting samples |
| Issue #456 | https://github.com/amzn/ads-advanced-tools-docs/issues/456 | opinion | 2026-11-09 | duplicate v1 rows |
| Issue #476 | https://github.com/amzn/ads-advanced-tools-docs/issues/476 | opinion | 2026-11-09 | matchedTarget change, retroactive |
| Issue #453 | https://github.com/amzn/ads-advanced-tools-docs/issues/453 | opinion | 2026-11-09 | no target id via MCP |
| Issue #467 | https://github.com/amzn/ads-advanced-tools-docs/issues/467 | opinion | 2026-11-09 | zero rows DE and GB |
| Issue #501 | https://github.com/amzn/ads-advanced-tools-docs/issues/501 | opinion | 2026-11-09 | SB v3 429s and failures |
| Issue #439 | https://github.com/amzn/ads-advanced-tools-docs/issues/439 | opinion | 2026-11-09 | ST absent in v1 |
| python-amazon-ad-api reports.py | https://github.com/denisneuf/python-amazon-ad-api/blob/main/ad_api/api/reports.py | opinion | 2026-11-09 | SDK wording; GZIP_JSON |
| Intentwise: how long Amazon keeps ad reports | https://www.intentwise.com/blog/explained-how-long-does-amazon-keep-your-ad-reports | opinion | 2026-11-09 | console look-backs |
| SellerApp: ad report data timing | https://www.sellerapp.com/blog/amazon-advertising-report-data-timing/ | opinion | 2026-11-09 | console retention table |
| emax digital: data lag and refresh | https://kn.emax-digital.com/customer-knowledge-base/data-lag-and-refresh-schedules | opinion | 2026-11-09 | pull order; 7 days; 5% |
| Fivetran Amazon Ads connector | https://fivetran.com/docs/connectors/applications/amazon-ads | opinion | 2026-11-09 | profile time zone; rollback; retention |
| Optmyzr: Amazon Ads reporting delays | https://www.optmyzr.com/blog/amazon-ads-reporting-delays/ | opinion | 2026-11-09 | 72 h cancellations; 28 days provisional |
| Openbridge: attribution definitions and timing | https://docs.openbridge.com/en/articles/4208366-amazon-advertising-attribution-definitions-and-timing | opinion | 2026-11-09 | 48 h; 3–5 days; rolling re-pulls |
| Openbridge: time zones | https://docs.openbridge.com/en/articles/5053618-understanding-timezones-within-amazon-seller-central-and-amazon-advertising | opinion | 2026-11-09 | UTC and Pacific |
| Ad Badger: attribution window blind spots | https://www.adbadger.com/blog/attribution-window-blind-spots-how-14-day-windows-quietly-wreck-your-decisions/ | opinion | 2026-11-09 | order-date claim; maturity |
| Helium 10: attribution windows | https://www.helium10.com/blog/amazon-attribution-windows/ | opinion | 2026-11-09 | windows; waiting days |
| Nova: time zones | https://novadata.io/docs/your-data/time-zones | opinion | 2026-10-29 (checked again 2026-11-09) | ad and sales clocks |
| Ktena et al. 2019 | https://arxiv.org/abs/1907.06558 | research | 2026-11-09 | delayed labels; abstract |
| Yasui et al. 2020 | https://arxiv.org/abs/2002.02068 | research | 2026-11-09 | feedback shift; abstract |
| Chapelle 2014 (metadata) | https://api.crossref.org/works/10.1145/2623330.2623634 | research | 2026-11-09 | title, venue, date only |
| Croushore 2011 | https://api.crossref.org/works/10.1257/jel.49.1.72 | research | 2026-11-09 | data revisions; abstract |
| Brooker: Exponential Backoff And Jitter | https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ | research | 2026-11-09 | jitter simulation |
| Audience reports (v3) | A + guides/reporting/v3/report-types/audience | official | 2026-11-09 | `spAudiences`, `sbAudiences`, `dspAudience`; `campaign_bid_boost_segment`; 31 d / 95 d; base metrics (gap fill) |
| Sponsored Products & Brands: Audience Bid Boosting | A + knowledge-hub/blogs/usage-examples/2026-01-sp-sb-bid-boosting | official | 2026-11-09 | the two report requests; console "Bid Adjustments" → "Audiences" (gap fill) |
| Release notes index (audience entries) | A + release-notes/index | official | 2026-11-09 | Jan 24, 2025 audience bid-boost reports; Mar 12, Mar 24, Aug 22, 2025 audience entries (gap fill) |
| Audience segment (v1 dimension) | A + guides/reporting/ads-v1/dimensions/audience/audience-segment | official | 2026-11-09 | `audienceSegment.*`; SP, ST, DSP; no v3 SA name (gap fill) |
| Audience segment targeting status (v1) | A + guides/reporting/ads-v1/dimensions/audience/audience-segment-targeting-status | official | 2026-11-09 | `audienceSegmentTargetingStatus.value` (gap fill) |
| Impressions metric (v1) | A + guides/reporting/ads-v1/metrics/delivery/impressions | official | 2026-11-09 | compatible with hour, placement, target, search term (gap fill) |
| Sponsored Products performance datasets (Stream v1) | A + guides/amazon-marketing-stream/datasets/sp-performance | official | 2026-11-09 | dataset ids `sp-traffic`, `sp-conversion`; keyword × placement × hour; freshness (gap fill) |
| Deprecations (legacy account management) | A + release-notes/deprecations | official | 2026-11-09 | `/adsAccounts*` deprecated July 2026, `Warning: 299`, 404 July 2027 (gap fill) |
| QueryAdvertiserAccount API (re-read) | A + guides/account-management/query-advertiser-accounts | official | 2026-11-09 | body, filters, `alternateIds`, `timeZoneIana`, pagination (gap fill) |
| Data Kiosk seller analytics schema | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_sellerAnalytics_2025_03_31.graphql | official | 2026-11-09 | view arguments, group-by, traffic, sales, promotion, rights, retention (gap fill) |
| Seller Analytics Dataset Use Case Guide | https://developer-docs.amazon/sp-api/docs/seller-analytics-dataset-guide | official | 2026-11-09 | date snapping, 34 h readiness, nulls on incompatible grouping, access levels (gap fill) |
| Data Kiosk API | https://developer-docs.amazon/sp-api/docs/data-kiosk-api | official | 2026-11-09 | Brand Analytics role on every operation (gap fill) |
| GitHub commits for the seller analytics schema | https://api.github.com/repos/amzn/selling-partner-api-models/commits?path=schemas/data-kiosk/analytics_sellerAnalytics_2025_03_31.graphql | official | 2026-11-09 | last commit 2026-09-30 (gap fill) |
| Issue #460 | https://github.com/amzn/ads-advanced-tools-docs/issues/460 | opinion | 2026-11-09 | `sbCampaignPlacement` rows without a placement key; checked, not used in a position (gap fill) |
| Nova: search terms and impression share | https://novadata.io/docs/advertising/search-terms-and-impression-share | opinion | 2026-11-09 | "below Amazon's privacy threshold are grouped" (gap fill) |
| Intentwise: Amazon Marketing Stream data model | https://docs.intentwise.com/iac-source-data/data-models/amazon-source-data/amazon-marketing-stream | opinion | 2026-11-09 | SP Stream tables with keyword, placement, hour (gap fill) |
| Perpetua: hourly performance and Share of Voice | https://perpetua.io/blog-perpetua-stream-strategies-how-to-leverage-hourly-amazon-performance-and/ | opinion | 2026-11-09 | Stream data for dayparting (gap fill) |
| cx-amazon-ads skill and door | local copy, `cx-amazon-ads/skills/amazon-ads/SKILL.md`, `references/door.md` | seat | 2026-11-09 | origins, headers, 429, POST as change |
| Listing playbook report.sh | local copy, `cx-listing-playbook/skills/listing-review/scripts/report.sh` | seat | 2026-11-09 | the reader's shape |
| Listing playbook report-lifecycle.md | local copy, `cx-listing-playbook/research/method/report-lifecycle.md` | seat | 2026-11-09 | SP-API lifecycle; form |
| Listing playbook paid-keywords.md | local copy, `cx-listing-playbook/research/angles/paid-keywords.md` | seat | 2026-11-09 | leads re-opened here |
| Listing playbook help-page-access.md | local copy, `cx-listing-playbook/research/method/help-page-access.md` | seat | 2026-11-09 | help pages are shells |

Unreachable:
- Amazon Ads help, Reports (https://advertising.amazon.com/help/GBYSPTSLR337JMLH): JavaScript shell to a GET; no public copy found.
- Amazon Ads help, column definitions (GH4CM33BLUN3XUYL): JavaScript shell.
- Amazon Ads help, traffic validation (GBYPYH79NGJJ5JPS): JavaScript shell.
- Amazon Ads help G3HEFZYWZF84NPS9: JavaScript shell.
- Seller Central help GZ8Y22NL2FSRY8M5: JavaScript shell. Its content call (`mons-api/GetHelpTopic`) is a POST that this seat may not make.
- A + concepts/reporting/advertising-console: `NoSuchKey` on the CDN. The page moved to guides/reporting/v2/advertising-console, which was read.
- A + no-code-tools/bulksheets/2-0/*: `NoSuchKey`. The pages moved to no-code-tools/bulksheets/, which was read.
- Acadia, "Understanding Amazon advertising reports: identifying data discrepancies" (https://acadia.io/understanding-amazon-advertising-reports-identifying-data-discrepancies): the body was truncated.
- Intentwise help, "Troubleshoot data discrepancy" (https://help.intentwise.com/en/articles/6007908-troubleshoot-data-discrepancy): 404.
- The ACM page for Chapelle 2014 (https://dl.acm.org/doi/10.1145/2623330.2623634): a bot challenge. The author's PDF (olivier.chapelle.cc) answered 404.
- The arXiv PDFs of 2002.02068 and 1907.06558: the local text extractor is broken, so only the abstracts were read.
- AWS Builders' Library, "Timeouts, retries, and backoff with jitter": a 301 to builder.aws.com, not followed.
- Web search: the budget was exhausted during this research. Further practitioner and academic sources were reached only by known URL. (In the gap fill, web search answered again and was used twice.)
- Intentwise help, "Amazon Marketing Stream hourly metrics data" (https://help.intentwise.com/en/articles/7181831-amazon-marketing-stream-hourly-metrics-data): 404 (gap fill). Intentwise's data-model page was read instead.

## Open questions

1. Is Reporting v1's one-report concurrency per client id (Limits and best practices; v1 overview) or per advertiser (reporting overview; Stream v2 overview; GA release note)? With one client id behind every seller, the two readings differ by the number of sellers. Re-read in the gap fill: still unsettled by Amazon's pages.
2. How many accounts may one v1 report name: 5 (Helpful concepts) or 2000 (the OpenAPI model)?
3. Does a v3 `425` body name the processing twin's `reportId`? The model gives only `{code, detail}`.
4. How long does a v3 or v1 report stay retrievable by id once completed? Does a fresh `GET` or retrieve return a fresh link after `urlExpiresAt` or `urlExpirationDateTime`? Neither model says.
5. What does a second v1 create answer while the one concurrent report is pending: queued, `429`, or something else? The overview says "queued or receive a 429".
6. Do v3 gross-and-invalid, benchmarks and extension reports accept `CSV` or `XLSX`, as their pages say, when the model's `format` enum is `GZIP_JSON` only?
7. Is v3 generation "up to three hours" (guides) or 15 minutes at P99 (limits table)?
8. How long do clicks keep changing (72 hours, 3 days, or 30 days with 5 days recommended), and conversions (42, 60 or 70 days)?
9. Which clock does SP-API Sales and Traffic use for a `DAY`: the marketplace's local day (Nova) or Pacific time in NA (Openbridge)? Amazon's pages read here do not say.
10. Is `adGroupTarget.id` usable in a v1 report through the API, when issue #453 found no target id accepted through the MCP tools?
11. Are the v1 duplicate rows for the same `date.value` and `searchTerm.value` (issue #456) a missing dimension or a defect?
12. Does Reporting v1 omit marketplaces of a global account (issue #467) in other accounts too?
13. Are the backticks in Building Queries' filter example part of the value?
14. Are `target.value` and `target.matchType` in Amazon's migration examples valid v1 ids? The Dimensions library names `adGroupTarget.*`, `targeting.value` and `targetingMatchType.value`; New features shows `target.value` flagged `PENDING_DEPRECATION`; and the Reporting API v3 Report Type Migration Guide maps `keywordId`, `keyword`/`targeting` and `matchType`/`keywordType` to `adGroupTarget.id`, `targeting.value` and `targetingMatchType.value` (gap fill). What is still open is whether the service still accepts `target.value`, with a warning, until its retirement.
15. Does SQP's impression and click data include ad traffic? The earlier paid-keywords lead says so, but it was not re-opened here.
16. Which role does Data Kiosk Economics need: Selling Partner Insights or Brand Analytics? The Data Kiosk API page lists Brand Analytics for every operation (createQuery, getQuery, getQueries, getDocument, cancelQuery), and each schema field carries its own `@paamRights` (gap fill). Which role grants the Economics fields' rights is not stated on the pages read.
17. Are the console's own report retentions what SellerApp lists? Amazon's help page does not serve to a GET.
18. Does `cx raw amazon-ads` record a v1 retrieve (a POST that changes nothing) as "sent, outcome unknown", like any other POST?
19. Does an identical v1 create, sent while its twin is still `PENDING` or `PROCESSING`, return the twin, start a second report, or answer `429`? No v1 page or model says (section I).
20. Does Reporting v1 apply Stream v2's `(Other)` threshold to `searchTerm.value`, and at what level? No v1 page says (section K).
21. Is `spGlobalAudiences` (the columns page) a separate report type or another name for `spAudiences` (the type page)? Is v1 `audienceSegment.*` on Sponsored Products rows the bid-boost segment? Sponsored Brands has no v1 audience segment id.
22. Does v1 accept `adGroupTarget.id` × `placementClassification.value` × `hour.value` in one query? Amazon's pages document no incompatibility, but they show no example (section H).
23. What time zone is a Data Kiosk Seller Analytics `DAY` in: the store's local day, Pacific, or UTC (as Economics uses for weeks and months)? How does it align with an ads profile's `timezone`, a v1 `timeZone.value`, or an account's `timeZoneIana`?
24. Why does the v3 columns page omit `spTargeting` from `topOfSearchImpressionShare`'s report types, when the Targeting reports page lists it? And why does the migration guide map that column to a v1 metric that is incompatible with Target?

## Positions

**P-reporting-1.** Reporting v3 (`POST /reporting/reports`), Amazon Marketing Stream v1 and Sponsored Ads v2 reporting stop delivering data on June 30, 2027. Reporting v1 (`/adsApi/v1/*/reports`) and Stream v2 have been generally available since September 30, 2026, and the Exports API is not affected. Sources: [official] Deprecations; Amazon Ads API v1 release notes; Amazon Ads reporting overview (all read 2026-11-09).

**P-reporting-2.** A v3 report is created with `POST /reporting/reports` (content type `application/vnd.createasyncreportrequest.v3+json`, profile in `Amazon-Advertising-API-Scope`), read with `GET /reporting/reports/{reportId}`, and cancelled while `PENDING` with `DELETE /reporting/reports/{reportId}`. Its status is one of `PENDING`, `PROCESSING`, `COMPLETED` or `FAILED`. Sources: [official] OfflineReport_prod_3p.json; Get started with version 3 reports.

**P-reporting-3.** A completed v3 report carries a pre-signed S3 `url` that expires at `urlExpiresAt`. Amazon gives 3600 seconds by default, "may vary". The file behind it is gzip-compressed JSON: one array of rows keyed by the requested columns. A failed report carries `failureReason`. Sources: [official] OfflineReport_prod_3p.json; Get started with version 3 reports.

**P-reporting-4.** A v3 create identical to a report still processing is answered `425` ("a duplicate of a processing request"). Amazon's direction is to wait for the existing report and to keep report ids to avoid duplicates. Sources: [official] Get started with version 3 reports; OfflineReport_prod_3p.json; Reporting and analytics component.

**P-reporting-5.** Throttled report calls answer `429`. A `429` carries `Retry-After` in seconds. Report rate limits are set per region by the size of the report queue and change slowly. Amazon directs longer backoff for report generation, with a maximum delay and a maximum number of retries. Sources: [official] Rate limiting; Get started with version 3 reports; [research] Brooker 2015.

**P-reporting-6.** v3 report types are per ad product. SP has campaign, targeting, search term, advertised product, purchased product, gross and invalid, prompt and video extension reports. SB adds ad, ad group and placement types, and SD has ad group but no search term. SP ad-group and placement data come from `spCampaigns` grouped by `adGroup` or `campaignPlacement`. Sources: [official] Sponsored ads report types (version 3); Campaign reports; Ad group reports; Placement reports.

**P-reporting-7.** Each v3 report type has its own `groupBy` values, filters, maximum range per request and retention, stated on its page. A filter applies only when every `groupBy` value in the request supports it. Sources: [official] v3 type pages; Get started with version 3 reports.

**P-reporting-8.** API search term reports (v3 and v1) contain only search terms with at least one click. A product-page placement without a keyword appears as `*`. The console's search term report contains terms with impressions. Sources: [official] Search term reports; Sponsored ads reporting FAQ (version 3); Search term dimension; [opinion] issue #476.

**P-reporting-9.** Amazon's Matched target dimension page limits `matchedTarget.value` to Sponsored Display, as the product page where the ad appeared (v3 `matchedTargetAsin`). One developer reports that since mid-July 2026 it carries no customer search terms, also for past dates re-requested; Amazon has not answered the report. Sources: [official] Matched target dimension; [opinion] issue #476 (mtsanko, 2026-07-22).

**P-reporting-10.** v3 Sponsored Products columns carry attribution windows of 1, 7, 14 and 30 days after a click. Sponsored Brands `purchases` and `sales` count 14 days after a click or a view. `sales14d` includes view-attributed sales for vCPM campaigns. Sources: [official] Reporting columns (version 3).

**P-reporting-11.** A v1 report is created, retrieved and deleted with `POST /adsApi/v1/create/reports`, `/retrieve/reports` and `/delete/reports`. Each answers `207`, with one result in `success[0]` or `error[0]`. The advertiser is named in the body's `accessRequestedAccounts` by its Global Account id (`amzn1.ads-account.g.*`), with no scope header, and one request holds one report with one period. Sources: [official] AmazonAdsAPIALLReportsContract_prod_3p.json; Getting started with the Reporting API v1; Retrieving accounts; QueryAdvertiserAccount API; Create a subscription.

**P-reporting-12.** A v1 report's status is `PENDING`, `PROCESSING`, `COMPLETED` or `FAILED`. Amazon's recommended polling frequency is once per minute. A completed report lists up to 100 `completedReportParts`, each with its own pre-signed URL and expiry; partitioned formats split into chunks of up to 1 GB uncompressed. Sources: [official] Getting started with the Reporting API v1; New features; AmazonAdsAPIALLReportsContract_prod_3p.json.

**P-reporting-13.** A v1 request is refused synchronously with numbered `400` codes. Among them are `400005` (unknown field), `400004` (incompatible fields), `400006` (missing required field), `400011` (duplicate field), `400014` (no metric), `400015` (no level-of-detail dimension), `400016` (no time dimension) and `400025` (past the look-back). A v1 report fails asynchronously with `failureCode` `001` (internal) or `002` (too large). Sources: [official] Handling errors.

**P-reporting-14.** A completed v1 report may carry `warnings`: `NO_PERMISSION`, `PENDING_DEPRECATION` and `DATE_LIMITED`, in a list Amazon says will grow. Warnings never stop a report from completing. Sources: [official] New features; Amazon Ads API v1 release notes.

**P-reporting-15.** Amazon's pages disagree on Reporting v1's concurrency. The Limits page and the v1 overview say one concurrent report per client id, not per advertiser; the Limits page adds that "All requests made with the same client ID share the same limits". The reporting overview, the Stream v2 overview and the GA note say one per advertiser. All give about 100 reports a day. The Limits page says concurrency and rate can be as low as 1. Sources: [official] Limits and best practices; Overview of the Reporting v1 API; Amazon Ads reporting overview; Amazon Marketing Stream v2 overview; Amazon Ads API v1 release notes (all re-read 2026-11-09).

**P-reporting-16.** In v1, rows are the group-by of every requested dimension. A dimension attribute needs its primary key, and `metric.sales` and `metric.totalCost` need `budgetCurrency.value`. Currency fields are not summed across budget currencies unless `currencyOfView` converts them. Sources: [official] Getting started with the Reporting API v1; Helpful concepts; New features; Costs metric.

**P-reporting-17.** v1 conversion metrics carry no window suffix. For Sponsored Products the base metric is the 7-day figure for sellers and the 14-day figure for vendors; for the other sponsored products it is 14 days. Promoted and halo are told apart by `productRelevance.value`. v3's `acosClicks*` and all 1-day and 30-day columns have no v1 equivalent. Sources: [official] Overview of the Reporting v1 API; Product relevance; Reporting API v3 Report Type Migration Guide.

**P-reporting-18.** In v1 a missing value is `null` in JSON and `""` in CSV, and a measured zero is `0`. A missing value can mean not applicable, not yet processed, or not permitted. Sources: [official] Helpful concepts.

**P-reporting-19.** v1 aggregates each campaign in its own time zone and names it in `timeZone.value`. v2 and v3 reports use the profile's time zone, which `GET /v2/profiles/{profileId}` returns as `timezone`. Stream v2 batches are UTC intervals. Sources: [official] Dates and historical data retention; Sponsored ads reporting FAQ (version 2); Profiles; Data delivery.

**P-reporting-20.** v1 retention and maximum range depend on the time dimension. Daily rows reach back 24 months, at most 120 days per request, and hourly rows 14 days. Under v3 most types keep 60 to 95 days. Sources: [official] Dates and historical data retention; v3 type pages (figures for human readers only).

**P-reporting-21.** Clicks and impressions first appear within about 12 hours and are corrected by traffic validation afterwards. Amazon's pages give three days, 72 hours, or up to 30 days with five days recommended. Sources: [official] Sponsored ads reporting FAQ (version 3); Limits, constraints, and quotas; Amazon Ads reporting overview.

**P-reporting-22.** Conversions first appear within about 24 hours and are reported on the date of the ad interaction. They are restated 1, 7 and 28 days after the conversion event, so a 14-day window can change up to 42 days after the report date. The reporting overview gives up to 60 days, and Stream v2 a 70-day restatement window. Sources: [official] Sponsored ads reporting FAQ (version 3); Sponsored ads reporting FAQ (version 2); Amazon Ads reporting overview; Ads performance dataset; [opinion] Optmyzr; Openbridge; Helium 10; [research] Ktena et al. 2019; Yasui et al. 2020.

**P-reporting-23.** No report or row from Amazon marks a day as final. Stream v2's Datasets overview says to treat a record as final only after its restatement window has passed. Sources: [official] OfflineReport_prod_3p.json; AmazonAdsAPIALLReportsContract_prod_3p.json; Datasets overview.

**P-reporting-24.** Amazon recommends one to two report requests per advertiser per day for each report type, spread through the day. It also recommends keeping metadata out of reports and taking it from exports joined on `campaignId`. Sources: [official] Sponsored ads reporting FAQ (version 3); Get started with version 3 reports; Reporting and analytics component.

**P-reporting-25.** Reports contain only entities with activity in the range. A campaign with no impressions in the range is absent from a campaign report. Sources: [official] Campaign reports.

**P-reporting-26.** During the v3 Sponsored Brands preview, campaigns with `isMultiAdGroupsEnabled=False` are missing from SB reports. Sources: [official] Sponsored ads reporting overview (version 3); Sponsored ads report types (version 3).

**P-reporting-27.** Stream v2 delivers Parquet totals at least once to an S3 bucket and SQS queue the client owns. The record kept for a key is the one with the highest `streamBatch.version`. Values below a reporting threshold are grouped into an `(Other)` row. A client application may register five destinations. Sources: [official] Stream v2 overview; Data delivery; Datasets overview; Limits (Stream v2); Create a subscription.

**P-reporting-28.** Exports return current campaign, ad group, target and ad metadata only, never past states. Each endpoint allows five jobs in progress, and download links last one hour. Sources: [official] Exports overview; Get started with exports; Exports FAQ.

**P-reporting-29.** Amazon's bulksheets search term report uses a fixed 7-day look-back that the chosen date range does not change. Its page defines CTR as impressions divided by clicks and conversion rate as orders divided by sales, the inverse of the v3 columns page. Sources: [official] Search term reports in bulksheets; Reporting columns (version 3).

**P-reporting-30.** The SP Performance Over Time, SP and SB Search Term Impression Share, and SP Budget reports exist only in the advertising console. Amazon treats console-against-API differences above 5% as a support matter. Sources: [official] Reporting in the advertising console vs. API (version 2); Version 2 reporting overview; [opinion] emax digital.

**P-reporting-31.** In SP-API Sales and Traffic, the by-ASIN section is aggregated over the whole requested range, and the by-date section is at account level. Weeks in Sales and Traffic and SQP run Sunday to Saturday. Data Kiosk Economics carries ad charges per MSKU per day, with week and month boundaries in UTC+0. Sources: [official] sellerSalesAndTrafficReport.json; Report Type Values – Analytics; analytics_economics_2024_03_15.graphql; analytics_salesAndTraffic_2024_04_24.graphql.

**P-reporting-32.** Ad ASIN fields may hold a retailer offer id that "may differ in format and length from a standard 10-character ASIN". v1 product ids are paired with their marketplace dimension. Sources: [official] Reporting columns (version 3); Advertised product; Converted product.

**P-reporting-33.** Sponsored Products invoice postings reach SP-API Finances as `ProductAdsPaymentEvent`, with `postedDate`, `transactionType` (`charge` or `refund`), `invoiceId` and base, tax and total values (total = base + tax). Amazon describes it as "A Sponsored Products payment event." Sources: [official] financesV0.json.

**P-reporting-34.** From November 10, 2026, Sponsored Brands v2 `searchTermImpressionRank` and `searchTermImpressionShare` return no values. In v1, `metric.impressionShare` and `metric.impressionShareRank` require `searchTerm.value`, `adProduct.value` and `advertiserAccount.id`, and do not combine with campaign, ad group, ad, advertised product or placement. Sources: [official] Deprecations; Search impression share.

**P-reporting-35.** Audience bid-boost performance has its own v3 report types, `spAudiences` and `sbAudiences`. Both group by `campaign_bid_boost_segment`, carry `segmentName` and `segmentClassCode` with campaign and base metrics, allow 31 days per request and keep 95 days, and have been supported since January 24, 2025. Amazon's v3 availability table lists the Audience type for DSP only, and the v3 columns page names the SP type `spGlobalAudiences`. Sources: [official] Audience reports; Release notes index (January 24, 2025); Sponsored Products & Brands: Audience Bid Boosting; Sponsored ads report types (version 3); Reporting columns (version 3).

**P-reporting-36.** Amazon maps no Reporting v1 or Stream v2 equivalent for `spAudiences` or `sbAudiences`. Reporting v1's `audienceSegment.id` (requiring `audienceSegment.classCode`, `.name`, `.source`, `.type` and `audienceSegmentCountry.code`) is available for Sponsored Products, Sponsored TV and DSP, not Sponsored Brands, and gives no v3 Sponsored Ads name. Sources: [official] Reporting API v3 Report Type Migration Guide; Ads performance dataset; Audience segment dimension.

**P-reporting-37.** The v3 type pages offer `topOfSearchImpressionShare` on `spCampaigns` (grouped by `campaign` or `campaignPlacement`), `sbCampaigns`, `spTargeting` and `sbTargeting`. The columns page lists `spCampaigns`, `sbCampaigns` and `sbTargeting`. Sources: [official] Campaign reports; Targeting reports; Reporting columns (version 3).

**P-reporting-38.** v1 `metric.topOfSearchImpressionShare` requires `adProduct.value` and `advertiserAccount.id`, is compatible with Campaign, and is incompatible with Ad group, Hour, Placement classification, Target, Targeting, Targeting match type, Search term and Audience segment. Amazon's migration guide still maps v3 `spTargeting` and `sbTargeting` `topOfSearchImpressionShare` to it. Sources: [official] Search impression share; Reporting API v3 Report Type Migration Guide.

**P-reporting-39.** Amazon's v3-to-v1 field map gives v3 `keywordId` as `adGroupTarget.id`, `keyword` and `targeting` as `targeting.value`, `keywordType` and `matchType` as `targetingMatchType.value`, `keywordBid` as `adGroupTarget.bid`, and `searchTerm` as `searchTerm.value`. The Dimensions library defines no `target.value`, and Amazon's warning example flags `target.value` as `PENDING_DEPRECATION`. Sources: [official] Reporting API v3 Report Type Migration Guide; Target; Targeting; Targeting match type; New features.

**P-reporting-40.** Amazon's v1 pages document no incompatibility between `placementClassification.value` and `adGroupTarget.id`, `targeting.value`, `searchTerm.value` or `hour.value`. The base traffic, cost and conversion metrics list all of these as compatible dimensions. An incompatible pair is refused with `400004`, naming both fields. Sources: [official] Placement classification; Hour; Clicks; Impressions; Costs; Purchases; Helpful concepts.

**P-reporting-41.** v3 has no report that splits a target by placement: `spTargeting` and `sbTargeting` group by `targeting` only, and placement comes at campaign level from `spCampaigns` grouped by `campaignPlacement` or from `sbCampaignPlacement`. Stream v1 `sp-traffic` and `sp-conversion` carry `keyword_id`, `placement` and the hour (`time_window_start`) in one record until June 30, 2027. Stream v2 `ads-performance-v1` keys its hourly records by all of its dimensions, including `placementClassification.value`, `adGroupTarget.id` and `searchTerm.value`. Sources: [official] Targeting reports; Campaign reports; Placement reports; Sponsored Products performance datasets; Ads performance dataset; [opinion] Intentwise data model.

**P-reporting-42.** In Stream v2, values of a thresholded dimension (`searchTerm.value` in `ads-performance-v1`, `convertedProduct.id` in `ads-converted-product-v1`) that do not meet a minimum are grouped into an `(Other)` row. The threshold is "evaluated at the exact level of detail", so a value reported alone at a coarse grain can fall into `(Other)` at a finer one, while totals stay complete. Amazon's Reporting v1 and v3 pages say nothing about such a threshold, and no page gives the minimum. Sources: [official] Datasets overview; Ads performance dataset; Ads converted product dataset; Reporting v1 guides; Search term reports; [opinion] Nova (search terms below "Amazon's privacy threshold are grouped").

**P-reporting-43.** Reporting v1's create answers `207`, `400`, `401`, `403`, `404`, `413`, `429`, `500`, `502`, `503` or `504`. It has no `425`, its request has no idempotency key, and no Amazon page says what an identical create does while its twin runs. A create over the concurrency limit answers `429` "until previous requests complete" (Limits page), or "will be queued or receive a 429" (reporting overview). Sources: [official] AmazonAdsAPIALLReportsContract_prod_3p.json; Handling errors; Limits and best practices; Amazon Ads reporting overview.

**P-reporting-44.** Neither reporting API has an operation that lists reports. v1 offers create, retrieve by `reportIds`, and delete; v3 offers create, and get or delete by `reportId`. A report is found again only through the id returned at creation. Sources: [official] AmazonAdsAPIALLReportsContract_prod_3p.json; OfflineReport_prod_3p.json.

**P-reporting-45.** The legacy account endpoints `POST /adsAccounts/list`, `GET /adsAccounts/{accountId}`, `POST /adsAccounts` and `POST /adsAccounts/batch` (with `GET /dsp/advertisers` and `GET /dsp/advertisers/{advertiserId}`) are deprecated. Since July 2026 they return `Warning: 299`, and new client integrations are blocked while existing callers continue "through an allowlist". From July 2027 they answer `404`. Account retrieval and listing moves to `POST /adsApi/v1/query/advertiserAccounts`. Sources: [official] Deprecations; QueryAdvertiserAccount API.

**P-reporting-46.** `POST /adsApi/v1/query/advertiserAccounts` with an empty body returns global accounts, each with `advertiserAccountId` (`amzn1.ads-account.g.*`), `alternateIds` holding each country's `profileId` and `countryCode`, and `timeZoneIana`. It pages by `nextToken`, and a page may be empty while a `nextToken` remains. Sources: [official] QueryAdvertiserAccount API.

**P-reporting-47.** Stream v1's Sponsored Products dataset ids are `sp-traffic` and `sp-conversion`; "Sponsored Products performance datasets" (path `sp-performance`) is the page that documents them. Their hour is `time_window_start`, in the profile's time zone. Sources: [official] Sponsored Products performance datasets; Dataset migration guide.

**P-reporting-48.** Data Kiosk `analytics_sellerAnalytics_2025_03_31` is queried through `sellerAnalyticsView(startDate, endDate, aggregateBy: DAY|WEEK|MONTH, currencyCode, marketplaceId)` for seller accounts only. It returns totals and per-`groupByKey` metrics (`asin`, `msku`, `parentAsin`, `marketplaceId` and others), including `traffic.sessions`, `pageViews`, `glanceViews`, `featureOfferPct`, `conversionRatePct`, `sales.orderedProductSales`, `unitsOrdered` and the `promotion` group. Amounts default to USD when `currencyCode` is omitted. Sources: [official] analytics_sellerAnalytics_2025_03_31.graphql; Seller Analytics Dataset Use Case Guide.

**P-reporting-49.** In Seller Analytics, weekly ranges are rolled back to Sunday–Saturday and monthly ranges to whole months. Daily ranges are not adjusted. The end date is capped at the latest date for which every requested metric has data, and "All metrics ... are ready after 34 hours", generally "at 10 AM local time two days later". A metric unavailable at the requested grouping returns `null`, not zero. Sources: [official] Seller Analytics Dataset Use Case Guide.

**P-reporting-50.** Neither the Seller Analytics schema nor its guide states the time zone of a `DAY`. Ads days are the profile's `timezone` (v3), each campaign's `timeZone.value` (v1) or UTC batches (Stream v2), and Data Kiosk Economics resolves weeks and months in UTC+0. Sources: [official] analytics_sellerAnalytics_2025_03_31.graphql; Seller Analytics Dataset Use Case Guide; Profiles; Dates and historical data retention; Data delivery; analytics_economics_2024_03_15.graphql.

**P-reporting-51.** Every Data Kiosk operation (`createQuery`, `getQuery`, `getQueries`, `getDocument`, `cancelQuery`) lists Brand Analytics as its required role, and each Seller Analytics field carries its own `@paamRights` and a 30-day result retention. Sources: [official] Data Kiosk API; analytics_sellerAnalytics_2025_03_31.graphql.

### Seat's positions (enter no skill)

- [seat] Every ComChatX seller reaches Amazon Ads through one client id. If the per-client-id reading of v1 concurrency holds (P-reporting-15), one seller's long report holds every other seller's report creation behind it. Which reading holds is a question for Amazon's support, or for a measured run, before a v1 reader is relied on.
- [seat] Stream v2 needs an S3 bucket and an SQS queue that ComChatX owns and Amazon is allowed to write to, with five destinations per application. It is infrastructure, so it needs a ruling on deployment and AWS, not a skill.
- [seat] A v3 reader written now has a life of under eight months. A v1 reader is the one that survives 2027-06-30, and it changes the ask's identity (account id, field ids), the attribution convention (7-day seller base) and the download (parts).
- [seat] The receipt carries the ask and the report id. That is what answers a `425` without a second create, and what lets the next run carry on a report still queued at the ceiling.
- [seat] A link to a report part is a credential for the seller's data for as long as it lives. It is used once, never printed, and stripped from the landed reply, as `report.sh` does.
- [seat] `ProductAdsPaymentEvent` reads as an invoice posting, not a per-day cost line; a per-day ad cost comes from the Ads reports.
- [seat] With no `425`, no idempotency key and no list operation in v1, the receipt that holds the ask's checksum and the returned `reportId` is the only record of a running report. A second create for the same ask, sent before the receipt is written, may run twice or be refused with `429`; the pages do not say which.
- [seat] If v1 shares Stream v2's threshold, a placement-by-target-by-hour query asks for the finest grain, where `(Other)` would be most likely. Harvesting from a coarse search-term query and diagnosing from a fine one would then see different term lists.
- [seat] Seller Analytics days and ad days can be joined on `asin` and `marketplaceId`, but until Amazon states the Seller Analytics clock, a one-day offset against a Pacific-profile ad day is possible and invisible in the data.
- [seat] A landed report is a vintage. Two landed copies of the same dates, read weeks apart, are how a skill sees restatement, rather than mistaking it for a change the seller made (`method/change-measurement.md`).

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** Every cited page was re-opened by a plain GET, not a sample. Amazon Ads guides were read as Markdown from `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md` (the host's `llms.txt` and `toc2.json` gave the paths), the two OpenAPI models from `https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/`, and the Profiles model from `https://d3a0d0y2hgofx6.cloudfront.net/en-us/profiles/3-0/openapi.yaml`. The SP-API page came from `developer-docs.amazon`, the SP-API schemas from `raw.githubusercontent.com/amzn/selling-partner-api-models`, the six issues from the public GitHub REST API (`api.github.com`, unauthenticated GET), the SDK from GitHub, practitioner and library pages from their own sites, the arXiv abstracts from `arxiv.org`, and the two papers' metadata from `api.crossref.org`. Each verbatim quote was searched for in the fetched text; each figure, enum, page name, author, date and tag was checked against the page; the release notes and deprecations index were re-read on 2026-11-09 for 2025–2026 entries that overturn a claim (none overturns one; the entries that refine a claim are folded in below). Positions were checked against the D233 wording rule.

**No forbidden host was called.** No Ads API host (`advertising-api*.amazon.com`), no Login with Amazon (`api.amazon.com/auth`), no Amazon Ads MCP server endpoint, no SP-API host, no Seller Central `mons-api/GetHelpTopic` call, and no page needing sign-in. No seller data was read.

**Corrections (was → now).**
1. A, naming: "v4 reporting API" "in the Sponsored Brands deprecation entry" → in the October 2026 entry deprecating SB v2 `searchTermImpressionRank`/`searchTermImpressionShare`; both SB entries are headed October 2026.
2. A, surfaces: the overview's "Amazon DSP reporting — To be shutoff after June 30, 2027" line was missing → added.
3. B, headers: guide's `Amazon-Ads-ClientId` given alone → the v3 model names `Amazon-Advertising-API-ClientId` (required).
4. B, scope and account headers: only "Required" (guide) → the model marks `Amazon-Advertising-API-Scope` `required: false` and `Amazon-Ads-AccountId` "Optional".
5. B, body: required-ness inside `configuration` unstated → all six of `adProduct`, `columns`, `format`, `groupBy`, `reportTypeId`, `timeUnit` are required in the model.
6. C, SB ad group: `groupBy` `adGroup` only → the page also has an SB "Group by `campaign`" section.
7. C, benchmarks: `timeUnit` `DAILY`, `WEEKLY`, `MONTHLY` unqualified → the model's `timeUnit` enum is `DAILY`, `SUMMARY` only.
8. C, conversion path: no configuration row → added (90 d range, 95 d retention, `SUMMARY`, `brandConversionPath`, `CSV` or `GZIP_JSON`, brand owners).
9. C, format disagreement: the v1 migration pages' v3 examples send `"format": "CSV"` → added.
10. C, SP base columns: "Every one carries … `spend`" → `spend` is listed for `spCampaigns` and `spAdvertisedProduct`, not `spTargeting` or `spSearchTerm`.
11. C, `salesOtherSku7d` … `roasClicks14d` "targeting and search-term reports" → also advertised-product reports.
12. D, `startDate`/`endDate`: paraphrase "Start/End date of summary period for a report." → the verbatim definitions, each ending "in the format YYYY-MM-DD."
13. D, SB `purchases`/`sales`: Sponsored Brands only → Sponsored Brands and Sponsored Display.
14. D, `keywordType`/`matchType`: the console's "-" note was missing → added verbatim.
15. D, inverted definitions: bulksheets page only → the console-against-API page (version 2) also gives CTR as impressions divided by clicks, and SP Total ACoS as `cost`/`attributedSales14d`.
16. E, rate limiting: added the page's own link to Brooker's post, its advice to distribute report requests and backfill in small increments, and the Well-Architected direction to honour `Retry-After`.
17. F, v1 header: the model's `Amazon-Ads-ClientId` against the quickstart's `Amazon-Advertising-API-ClientId` → named as a disagreement.
18. F, `400` body: guide's numeric codes only → the model's `code` is a word enum; `error[]` items are `{index, errors[{code, message, fieldLocation}]}` (1–20).
19. F, `warnings`: model "Absent when there are none" only → New features says `null` when none; `warningCodes` 1–100; the example flags `target.value` `PENDING_DEPRECATION`.
20. F, null reasons: "Access restrictions." (truncated) → "Access restrictions prevent the value from being included for your account."
21. G, time dimensions: "`day`, `dayOfWeek` and `year` are new" (Helpful concepts) → Helpful concepts lists `day` and `year`; `dayOfWeek` and `dateRange` are in the Dimensions library.
22. G, retention: "a later entry extending time-dimension retention to 24 months" → entry of August 26, 2026: `date`, `week`, `day`, `dayOfWeek` "from 15 months to 24 months"; "Maximum report date ranges are unchanged."
23. H, v3-to-v1 map: "v1 adds metrics with no v3 column: `metric.roasFromClicks`, `metric.salesPromoted`, `metric.salesHalo`, `metric.unitsSoldFromClicks`, `metric.unitsSoldPromoted`, `metric.unitsSoldHalo`, `metric.purchasesHalo`" was wrong → the guide maps `roasClicks*`, `attributedSalesSameSku*`, `salesOtherSku*`, `unitsSoldOtherSku*`, `unitsSoldClicks*`, `purchasesOtherSku*` and SB `purchasesBrandHalo` onto exactly these names, and the metric pages' "Version 3 Reporting Name" agrees.
24. H, the guide's shape: added its three columns (v3 | Stream v2 | v1) and the Stream labels `CALCULATED_METRIC_NOT_AVAILABLE`, `DIM_ATTRIBUTE_NOT_AVAILABLE` (with Amazon's join direction), `TIME_DIM_NOT_AVAILABLE`.
25. H, page name "Report type migration guide" → "Reporting API v3 Report Type Migration Guide" (everywhere).
26. H, metric pages: `metric.clicks` is from the Clicks page ("Clicks = gross clicks - invalid clicks"); `metric.totalCost` also requires `budgetCurrency.value` and is incompatible with Converted product and Product relevance (Costs page); `metric.roas` "ROAS = sales / total cost"; `metric.sales` v3 names added; `metric.topOfSearchImpressionShare` also incompatible with hour and placement classification.
27. H, disagreement: "list `target.value` twice in one field list" (one example) → in the sp-search-term, sp-targeting and sp-purchased-product examples; "a `target` page exists in the table of contents" → the Target page defines `adGroupTarget.id/.bid/.targetType/.status` and no `target.value`; added `campaign.currencyCode`, `portfolio.portfolioId`, `advertisedProduct.sku` in the examples and the purchased-product example's missing `convertedProductMarketplace.value`; page titles "Migrating from: spCampaigns" etc.
28. H and O, SKU field: `advertisedProduct.sku` as a v1 key → the dimension is `advertisedProductSku.value` (Advertised product SKU page); the Advertised product page has no `.sku`.
29. I, per-advertiser concurrency: the Stream v2 overview also states "one concurrent report per advertiser … approximately 100 reports per day" → added.
30. J, "Treat a record as final only after its window has passed" cited to the dataset and Data delivery pages → it is on the Datasets overview; added the reporting overview's "so your data self-corrects".
31. K, dataset figures: "about 400 metrics … every 15 minutes" and "every 4–6 hours" without a source → attributed to the GA release note (September 30, 2026: "Approximately 400 metrics", "as often as every 15 minutes", "Approximately 170 conversion metrics", "every 4 to 6 hours"), with the dataset page's 377 metric rows noted for human readers.
32. K, first delivery: paraphrase → the verbatim "within about a day of activation", plus the FAQ's "may arrive at a coarser grain".
33. K, arithmetic: "counts are summed across rows before any ratio" → non-applicable metrics are zero, rows sharing an entity key are summed, numerators and denominators are aggregated before dividing, totals including `(Other)` match the coarser grain.
34. K, subscription: `SUSPENDED` terminal and destination ownership attributed to the Stream v2 FAQ; added ADSP numeric ids accepted and the `401` "Bulk account authorization denied: DENY".
35. K, Stream v1 names: "`sp-traffic`, `sp-conversion` and the budget-usage feeds" (overview) → `sp-`, `sb-` and `sd-traffic`/`-conversion` from the Dataset migration guide; no budget-usage dataset name was found on the pages read.
36. L: exports cover SP, SB and SD; "Each call to GET /exports/{exportId} generates a new download URL" added.
37. M: page name "Understand bulksheets data" → "Understand bulksheets campaign data"; the defaults (terminated and zero-impression excluded, placement included) added.
38. N: the time-zone quote is the version 2 FAQ's → labelled so; the Profiles model's `timezone` definition and per-marketplace zones added, read from `profiles/3-0/openapi.yaml` because `reference/2/profiles` is `NoSuchKey` on the CDN.
39. N, Well-Architected: paraphrase "Stream's hourly data must be read in the right time zone" → the verbatim sentence.
40. O, Sales and Traffic limit: "up to three requests every five minutes" → "up to three times every five minutes".
41. O, Finances: "These are the invoice postings … not a daily cost line" tagged [official] → Amazon's own description quoted; the inference moved to [seat] and to the seat's positions.
42. P: "the skill body was only partly readable" → the CDN copies hold summaries only; titles "Ads Reporting Skill", "Account Context Identifiers Skill".
43. Practitioners, Intentwise: "SB and SD reports 60" as console look-backs → that 60 is the article's API figure (with SP 95 since v3), not a console figure.
44. Practitioners, emax digital: "data can take up to 7 days to fill" → its own first backfill; the 72 hours is stated for "All reports accessible through the SP-API"; the 5% is "deviations … of up to 5% are anticipated", not a line for raising a discrepancy.
45. Practitioners, titles and wording: Optmyzr's title (the URL slug had been used), and "citing Amazon help" made exact (it links the version 2 reporting FAQ and help pages G4YK9L2G4NXDD7SC and GFXUBJVCPTN75M6J); Openbridge's titles, the 48-hour and 3–5-day quotes, and the June 2020 understatement; Helium 10's full title and modified date, "sales data can take up to 12 hours", and "Helium 10 Ads" (not "Adtomic"); Ad Badger's title, author, SD view-through, and the verbatim "Amazon's standard advertising reports are built by order date"; Fivetran's "depend on the Attribution Window setting"; the SB v3 retention disagreement qualified (SB purchased product keeps 731 days); Nova's "Checked against Nova's code on October 29, 2026"; the SDK's `specs/` files named.
46. Research: Ktena et al.'s affiliation "(Twitter)" is not on the abstract page → removed, with "5 different loss functions" quoted and RecSys '19; Yasui et al. WWW '20 added; Chapelle's Criteo affiliation from Crossref; Croushore's gloss "real-time data sets that keep each vintage" → the abstract's "better real-time data sets"; Brooker's "updated 2023" → an update note of May 2023.
47. Page names: "Dimension library" → "Dimensions library"; "Version 2 reporting FAQ" → "Sponsored ads reporting FAQ (version 2)"; "Advertising console vs. API reports" → "Reporting in the advertising console vs. API (version 2)"; "Query advertiser accounts" → "QueryAdvertiserAccount API"; Pages read gained the Clicks, Costs and Advertised product SKU pages.
48. Positions: P-reporting-9 stated a developer's report as fact → Amazon's page stated as fact and the report attributed as one developer's, unanswered; P-reporting-16 adds `metric.totalCost`; P-reporting-23 cites the Datasets overview; P-reporting-33's inference moved to the seat's list; open question 14 gains the `PENDING_DEPRECATION` flag. No position was found worded as when to ask, a fixed sequence, a threshold as a rule, a ceiling, or how cx talks.

**Removed.**
1. K: "A null is not a zero" under Stream v2 thresholds and arithmetic. It is not on the Stream v2 pages; Stream's rule is that a non-applicable metric is zero (correction 33). The v1 rule stays in section F.

**Still unreachable.** Unchanged from the list above: the Amazon Ads help pages (JavaScript shells), Seller Central help (its content call is a POST this seat may not make), the ACM page and author PDF for Chapelle 2014, the arXiv PDFs (abstracts only), the Acadia body, Intentwise help (404), and the AWS Builders' Library article (301 to builder.aws.com, not followed). Also: the CDN copy of `reference/2/profiles` (`NoSuchKey`; the Profiles model was read instead).

### Gap fill 2026-11-09

Done by the research seat on 2026-11-09, after the verification above. Every page named here was re-opened by a plain GET that day: the docs CDN Markdown, the two OpenAPI models, `raw.githubusercontent.com` and the unauthenticated GitHub REST API for `amzn/*`, `developer-docs.amazon` Markdown, and practitioner sites. No forbidden host was called and no seller data was read. Only this file was written. The other research files named below are not this seat's to edit, so where they differ from the sources, the finding is recorded here for their owners.

**Gaps filled.**
1. Audience reports. Added `spAudiences` and `sbAudiences` to the section C table, with a section C note covering the availability-table omission, the `spGlobalAudiences` name on the columns page, the January 24, 2025 release note, the free-string `reportTypeId`, and the missing v1 and Stream v2 mapping (v1 `audienceSegment.*` is SP, ST and DSP only, with no v3 Sponsored Ads name). Also stable item 20, positions P-reporting-35 and 36, a run-time entry, and open question 21. The gap's facts (groupBy `campaign_bid_boost_segment`, `segmentName`, `segmentClassCode`, 2025-01-24) are confirmed.
2. Placement × target, search term and hour in v1. Added a section H bullet: no documented incompatibility, the base metrics list all of them as compatible, Helpful concepts' list is examples only, and the service answers with `207` or `400004`. Stream v1 `sp-traffic` and `sp-conversion` carry keyword × placement × hour, and Stream v2 keys by all of them. In v3, no target-by-placement type exists. The share metrics are the exceptions. Also stable item 23, positions P-reporting-40 and 41, a run-time entry, and open question 22. One correction to the gap's premise: Amazon's console-against-API page does not list a "Keyword Placement" report among console-only types. It names "Keyword placement" only as a Sponsored Brands console report in its column table.
3. `(Other)` threshold in v1. Added a section K bullet with the Datasets overview text ("evaluated at the exact level of detail"). No v1 or v3 page mentions thresholds, and the parity claims do not name them. Nova [opinion] is in the practitioners section. Also stable item 24, P-reporting-42, a seat's position, a run-time entry, and open question 20.
4. v1 duplicates. Added to section I: the model's response codes (no `425` or `409`), no idempotency key, no list operation in either API, and the two pages' answers for a create over the limit (`429` against "queued or ... 429"). Also stable item 25, P-reporting-43 and 44, a seat's position, a run-time entry, and open question 19.
5. Data Kiosk Seller Analytics. Added to section O: the view's arguments, `groupByKey`, the traffic, sales and promotion fields (including the deprecated `conversationRatePct` against `conversionRatePct`, and `fulfilmentChannel` against the guide's `fulfillmentChannel`), date snapping, 34-hour readiness, nulls on incompatible grouping, rights and the Brand Analytics role. Section N notes that no `DAY` time zone is stated. Also stable item 27, P-reporting-48 to 51, a run-time entry, open question 23, and open question 16 partly answered.

**Contradictions settled.**
1. v1 concurrency scope. Re-read all five pages; quoted verbatim in section I. Two v1 pages (v1 overview, Limits) say per client id, and three general pages (reporting overview, Stream v2 overview, GA release note) say per advertiser. Amazon's pages do not settle it, so this file keeps the disagreement (P-reporting-15, now also citing the Stream v2 overview). For other owners: `beyond/automation-and-amazon-tools.md` §J states "one concurrent report per advertiser" as a RULE, which the v1 Limits page and the v1 overview contradict. `method/ads-api-surface.md` P28 states the per-client-id side, which the reporting overview, Stream v2 overview and GA note contradict. Both should state the disagreement.
2. Account id source. `/adsAccounts*` is deprecated (Deprecations, "July 2026 - Deprecation of legacy account management APIs": `Warning: 299`, new integrations blocked, existing callers by allowlist, `404` from July 2027). The replacement is `POST /adsApi/v1/query/advertiserAccounts`. `method/ads-api-surface.md` and `areas/campaign-structure.md` are right. This file's section F, the run-time section, P-reporting-11's sources, and new positions P-reporting-45 and 46 now follow them. The Retrieving accounts guide itself still carries no deprecation notice.
3. `target.value`. Settled by Amazon's own field map. The Reporting API v3 Report Type Migration Guide maps `keywordId` → `adGroupTarget.id`, `keyword`/`targeting` → `targeting.value`, and `matchType`/`keywordType` → `targetingMatchType.value`. The Dimensions library has no `target.value`, and New features flags it `PENDING_DEPRECATION`. This file was right and now cites the map (section H, P-reporting-39). For other owners: `method/change-measurement.md`'s run-time list should use `adGroupTarget.id`, `targeting.value` and `targetingMatchType.value`. `areas/search-terms-and-negatives.md`'s "learn from the service's reply" is consistent; the warning list in a completed report is where a deprecated field shows.
4. `topOfSearchImpressionShare` report types. This file was incomplete. The v3 columns page lists `spCampaigns`, `sbCampaigns` and `sbTargeting`. The type pages list SP campaign (grouped by `campaign` and by `campaignPlacement`), SB campaign, SP targeting and SB targeting. `areas/bids-and-placements.md` (§J, P-bids-and-placements-26) and `beyond/brand-defense-and-competition.md` are right about SB. Section C now gives both pages, and P-reporting-37 states it. Section H and P-reporting-38 now give the v1 metric's full incompatibility list, which includes Target, Targeting, Search term and Audience segment as well as the three the file had.
5. Stream v1 dataset name. Settled: the page "Sponsored Products performance datasets" lives at path `sp-performance` and says "use the ID `sp-traffic`" and "use the ID `sp-conversion`". This file was right (section K, P-reporting-47). For `areas/bids-and-placements.md`: "sp-performance dataset" names the page, not a dataset a subscription takes. The hourly keyword-by-placement data is `sp-traffic` and `sp-conversion`.
6. Two parts.
   - (a) The `beyond/automation-and-amazon-tools.md` RULE is as in item 1.
   - (b) The Stream v2 overview does state the scope: "subject to usage limits (one concurrent report per advertiser, approximately 100 reports per day)". This file's section I was right. `method/change-measurement.md`'s "states neither" is not what the page says.

**Corrections to this file's earlier text.**
1. Section C, `topOfSearchImpressionShare`: given for `spCampaigns` and `spTargeting` only. Now: the type pages give SP and SB campaign and targeting, the columns page gives `spCampaigns`, `sbCampaigns` and `sbTargeting`, and the two disagree on `spTargeting`.
2. Section F and the run-time section: the account id came from `POST /adsAccounts/list` or `GET /adsAccounts/{accountId}`. Now: `POST /adsApi/v1/query/advertiserAccounts`, with the legacy calls' deprecation.
3. Section H: `metric.topOfSearchImpressionShare` was "incompatible with ad group, hour and placement classification". The list is now complete: it also includes Target, Targeting, Targeting match type, Search term and Audience segment.
4. Open questions 1, 14 and 16 updated as above. Seven open questions added (19 to 24, with 21 covering audiences).

**Declined.** None. Gap 2's premise about a console-only "Keyword Placement" report is corrected in item 2 above; the rest of that gap stands and was filled.

**Positions.** P-reporting-35 to 51 were added and P-reporting-15 was refined. They were checked against the D233 wording rule: each states a definition, an Amazon rule, a documented mechanism or a named practitioner's claim. None says when to ask the seller, sets a sequence, presents a threshold as the rule, caps what cx may change, or says how cx talks. The three new seat's positions enter no skill.

**Unreachable in the gap fill.** The Intentwise help article "Amazon Marketing Stream hourly metrics data" (404). Its data-model page was read instead.
