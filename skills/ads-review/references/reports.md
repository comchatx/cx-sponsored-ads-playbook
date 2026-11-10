# Reports: types, windows, limits, the v3 sunset and Stream

- How a v3 report is asked for, polled and landed: the amazon-ads skill's references/door.md.

## The sunset

- Reporting v3, Sponsored Ads v2 reporting and Marketing Stream v1 stop delivering data on 2027-06-30; Reporting v1 and Stream v2 have been generally available since 2026-09-30 (R1).

## Reporting v3

- A pending v3 report can be cancelled with `DELETE` on its id; a completed one carries a pre-signed S3 `url` expiring at `urlExpiresAt`, 3600 seconds by default, which Amazon says "may vary", and a failed one carries a `failureReason` (R2).
- For a create identical to a report still processing, which answers `425`, Amazon's direction is to wait for the existing report and keep report ids (R3).
- v3 report types are per ad product, each with its own `groupBy`, filters, maximum range and retention, and a filter applies only when every `groupBy` supports it (R5).
- SP has campaign, targeting, search term, advertised product, purchased product, gross and invalid, prompt and video extension types, with ad-group and placement data from `spCampaigns` grouped by `adGroup` or `campaignPlacement` (R5).
- SB adds ad, ad group and placement types; SD has ad group but no search term (R5).
- Audience boosts have `spAudiences` and `sbAudiences`, 31 days per request and 95 days kept, though the v3 columns page names the SP type `spGlobalAudiences` and the availability table lists Audience for DSP only (R5).
- Amazon maps no v1 or Stream v2 equivalent for the audience types, and v1's `audienceSegment.id` covers SP but not SB (R5).
- Amazon recommends one or two report requests per advertiser per day per type, spread through the day, and taking metadata from exports joined on `campaignId` rather than from reports (R13).
- Reports hold only entities with activity in the range, and during the v3 Sponsored Brands preview, campaigns with `isMultiAdGroupsEnabled=False` are missing from SB reports (R14).

## Reporting v1

- A v1 report is created, retrieved and deleted with `POST /adsApi/v1/create/reports`, `/retrieve/reports` and `/delete/reports`, each answering 207 with one result (R6).
- A v1 request names the advertiser by global account id in `accessRequestedAccounts`, with no scope header, and holds one report and one period (R6).
- A v1 report's status is `PENDING`, `PROCESSING`, `COMPLETED` or `FAILED`, polled about once a minute (R6).
- A completed v1 report lists up to 100 parts, each with its own pre-signed URL and expiry, partitioned formats splitting into chunks of up to 1 GB uncompressed (R6).
- A v1 create has no `425` and no idempotency key, and no Amazon page says what an identical create does while its twin runs (R6).
- Neither API lists reports, so a report is found again only by the id returned at creation (R6).
- A v1 request is refused synchronously with numbered 400 codes, among them `400004` incompatible fields, `400005` unknown field, `400006` missing field and `400025` past the look-back, and a failed report carries a failure code (R7).
- A completed v1 report may carry warnings (`NO_PERMISSION`, `PENDING_DEPRECATION`, `DATE_LIMITED`) in a list Amazon says will grow, and warnings never stop it completing (R8).
- In v1 rows are the group-by of every requested dimension, an attribute needs its primary key, money metrics need `budgetCurrency.value`, and currencies are not summed across budget currencies unless `currencyOfView` converts them (R10).
- In v1 a missing value is `null` in JSON and `""` in CSV and "does not imply zero"; a measured zero is `0` (R11).
- v1 keeps daily rows longer than hourly rows, with a cap on the days one request spans, and most v3 types keep their own retention; the figures are read at run time from Amazon's *Dates and historical data retention* page and the v3 type pages (R12).
- Amazon's v3-to-v1 field map gives `keywordId` as `adGroupTarget.id`, `keyword` and `targeting` as `targeting.value`, `keywordType` and `matchType` as `targetingMatchType.value`, `keywordBid` as `adGroupTarget.bid` and `searchTerm` as `searchTerm.value` (R20).
- The Dimensions library defines no `target.value`, though Amazon's own v1 examples write it and the New features warning example flags it `PENDING_DEPRECATION` (R20).
- v1 pages document no incompatibility between placement and target, term or hour dimensions, an incompatible pair being refused with `400004`, while v3 has no target-by-placement report (R20).
- Ad ASIN fields may hold a retailer offer id of another format and length, and v1 product ids pair with their marketplace (R18).

## Limits

- A throttled call answers `429` with `Retry-After` in seconds; limits move with system load and, for reports, with the region's queue (R4).
- Amazon's guidance is exponential backoff on `429` and 5xx answers, longer for report generation, and investigating other 4xx answers first (R4).
- Field reports show `429`s without `Retry-After`, one persisting over 24 hours on change history and one from the MCP gateway as HTML (R4).
- Amazon's pages disagree on Reporting v1 concurrency: its limits page and v1 overview say limits apply per client id, shared across every advertiser the client calls for, with concurrency "as low as 1", while the reporting overview, the Stream v2 overview and the GA note say per advertiser (R9).

## Marketing Stream

- Stream v2 delivers Parquet totals at least once to an S3 bucket and SQS queue in the subscriber's AWS account, and the record to keep for a key is the one with the highest `streamBatch.version` (R15).
- Stream v2's thresholded values fall into an `(Other)` row evaluated at the exact level of detail (R15).
- A Stream v2 destination belongs to the application that first uses it, at most five per application (R15).
- Stream v1 carries `keyword_id`, `placement` and the hour in one record until 2027-06-30, and Stream v2's `ads-performance-v1` keys hourly records by placement, target and search term (R20).
- Stream v1's Sponsored Products datasets are `sp-traffic` and `sp-conversion`, documented on the page whose path is `sp-performance`, with the hour in the profile's time zone (R21).

## Console and seller-side data

- The SP Performance Over Time, SP and SB search term impression share and SP Budget reports exist only in the console, and Amazon treats console-to-API differences above 5% as a support matter (R16).
- On the seller side, Sales and Traffic aggregates its by-ASIN section over the whole range, and its weeks run Sunday to Saturday (R17).
- Data Kiosk Economics carries ad charges per MSKU per day, with weeks and months in UTC (R17).
- Seller Analytics rolls weeks back to Sunday–Saturday, has all metrics ready after about 34 hours, states no time zone for a day, needs the Brand Analytics role and keeps results 30 days (R17).
- SP invoice postings reach SP-API Finances as `ProductAdsPaymentEvent`, with posted date, charge or refund, invoice id, and base, tax and total (R19).

## Ads API v1, the MCP server and test accounts

- Ads API v1 is one set of `POST` create, update, query and delete operations over campaigns, ad groups, ads, targets and associations, which Amazon says will eventually replace the per-product APIs (R22).
- SP, SB and DSP campaign management on v1 have been GA since 2025; at launch each call is bound to one ad product, with a per-product rate limit and batch sizes (`maxItems`, `maxResults`), SB writes taking far fewer items per call than SP's (R22).
- The v1 contract and overview also list Sponsored Display and Sponsored Television as supported, and SD has a published v1 specification with no dated GA note (R22).
- The Amazon Ads MCP server is served from `advertising-ai.amazon.com`, `-eu` and `-fe`, not the Ads API hosts, with the same token and client id, and the `cx-amazon-ads` door, whose origins are the `advertising-api*` hosts, does not reach it (R23).
- The MCP server's `campaign_management` group holds 32 tools, among them a single-call SP campaign create whose specification states no response and no behaviour on a failure part-way (R23).
- None of those tools is named for harvesting or negatives, although the MCP server's 2026-02-18 release note describes workflows that "automate keyword harvesting from automatic to manual campaigns" (R23).
- Amazon's skills library is served by `GET /skills` on the Ads API hosts, with an `ads-api-migration` skill published on 2026-11-02 (R23).
- Test accounts serve and bill nothing, are created under a separate `advertising::test:create_account` scope as vendor or author accounts only, and do not run rules (R24).
