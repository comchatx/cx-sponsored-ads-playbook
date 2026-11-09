# Campaign structure

Read 2026-11-09 by the research seat.
Tags: [official] Amazon's own words, with page and URL, read 2026-11-09 · [opinion] a named practitioner's claim, stated as theirs · [research] published research · [seat] the research seat's reasoning, never a position. A figure (a limit, a minimum, a window, a percentage, a date that may move) is recorded with its page and date for human readers only; a skill reads the figure at run time from the live surface.

## What this covers

This file covers the shape of a seller's advertising account as Amazon defines it, and what practitioners say about how to arrange that shape. It covers:

- the object model, from the account and the profile down to the target, for Sponsored Products (SP), Sponsored Brands (SB) and Sponsored Display (SD), plus the Ads API v1 unified model (`/adsApi/v1/...`)
- which settings live at which level, because that is what makes structure matter: a setting at campaign level can only differ between two things if they sit in different campaigns
- auto against manual targeting, and Amazon's own path from one to the other (target promotion groups)
- campaign goals and objectives in the console and in the API
- portfolios and their budget caps
- states (enabled, paused, archived), the irreversibility of archive, and the fields that cannot change after creation
- entity limits, Amazon's published table, and where third-party figures conflict with it
- names, tags and naming conventions
- multi-marketplace and multi-language structure, including global campaigns
- bulksheets and the Exports API, and how they relate to the API
- the structure patterns practitioners argue over (single keyword ad groups or campaigns, splitting by match type, by product, by intent, research-performance-harvest, one product per ad group, placement isolation), with who argues for and against each
- which products and which child of a variation family get ads, and catalogue tiering as a basis for campaigns and budgets
- the Sponsored Brands multi-ad group model, legacy SB campaigns and their migration
- why a restructure's effect cannot be read at campaign level, and the unit that can be compared
- what structure cx must read at run time

Topics owned by sibling files are only touched here where structure depends on them:

- match types and targeting expressions: `areas/keyword-and-product-targeting.md`
- harvesting search terms and placing negatives: `areas/search-terms-and-negatives.md`
- bid strategies and placement adjustments: `areas/bids-and-placements.md`
- budgets, pacing and budget rules: `areas/budgets-and-pacing.md`
- the first campaigns for a new product: `areas/launch.md`
- event and seasonal structure: `areas/seasons-and-deals.md`
- the ads–organic interaction: `areas/ads-organic-and-total.md`
- why a campaign does not deliver: `areas/diagnosis.md`
- which ad products a seller may use: `beyond/ad-products-and-eligibility.md`
- attribution windows and metric definitions: `beyond/metrics-and-attribution.md`
- targets such as ACOS and TACOS: `beyond/goals-and-economics.md`
- branded and competitor campaigns as a competitive question: `beyond/brand-defense-and-competition.md`
- Amazon's automation (auto-managed campaigns, rules, the Ads Agent): `beyond/automation-and-amazon-tools.md`
- the API surface in general: `method/ads-api-surface.md`
- reports: `method/reporting.md`
- measuring the effect of a structural change: `method/change-measurement.md`

The door this pack sits on is `cx raw amazon-ads --origin <regional origin> --method <M> --path <P> [--header ...] [--body ...]`, described in the `cx-amazon-ads` plugin's `skills/amazon-ads/SKILL.md` and `references/door.md`. Every endpoint named below is one a skill reaches through that door. This seat called none of them; every API fact here comes from Amazon's public documentation and its published OpenAPI files.

## Amazon's own rules and guidance

### A. Accounts, profiles and the global account — RULE

**A profile is one advertiser account in one marketplace.** The Ads API profiles guide says a profile represents an advertiser and its account in a single marketplace, and that it corresponds to an account in the advertising console. `GET /v2/profiles` lists the profiles a user's authorization reaches, but only those in the region of the host being called (North America, Europe or Far East). Each profile carries `profileId`, `countryCode`, `currencyCode`, `timezone` and `accountInfo` (`marketplaceStringId`, `id`, `type`, `name`). The `type` values are `seller`, `vendor` and `agency`. The guide gives a maximum of 5,000 profiles per response (figure for human readers only). [official] *Profiles*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles, read 2026-11-09.

**Single-marketplace calls carry the profile; global and cross-product calls carry the account.** The profile ID goes in the `Amazon-Advertising-API-Scope` header. Global calls go to the account ID in `Amazon-Ads-AccountId`. The global campaigns guide says those calls use the Global Account header and not the scope header. [official] *Global campaigns for Sponsored Products*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/global-campaigns, read 2026-11-09. The cx door states the same split: the scope header for a profile and `Amazon-Ads-AccountId` for cross-product and global calls. The door refuses a request naming `Authorization`, `Amazon-Advertising-API-ClientId` or `Amazon-Ads-ClientId`, because it supplies them itself (cx-amazon-ads `SKILL.md`, read 2026-11-09).

**The three regional origins.** The door's table lists them:

| Origin | Host | Marketplaces |
|---|---|---|
| na | `https://advertising-api.amazon.com` | US, CA, MX, BR |
| eu | `-eu` | UK, FR, IT, ES, DE, NL, AE, PL, TR, EG, SA, SE, BE, IN, ZA |
| fe | `-fe` | JP, AU, SG |

A seller with one brand selling in the US, Germany and Japan therefore has at least three profiles behind three origins. A structure decision taken in one marketplace says nothing about the others. (cx-amazon-ads `SKILL.md`, read 2026-11-09.)

**Global and non-global accounts.** `POST /adsApi/v1/query/advertiserAccounts` returns two kinds of account:

- Global accounts carry `isGlobalAccount` and an ID of the form `amzn1.ads-account.g.*`.
- Non-global accounts carry an ID of the form `amzn1.ads1.aa1.{country}.{entityId}`.

`alternateIds` map an account to its `profileId`, `entityId` and `countryCode`. "Omitting `isGlobalAccountFilter` returns only global accounts"; non-global accounts need `isGlobalAccountFilter: { include: [false] }` in a second request, and pages may come back empty with a valid `nextToken`. [official] *QueryAdvertiserAccount API developer guide*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/query-advertiser-accounts, and *Create accounts*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/accounts/create-accounts, both read 2026-11-09. The legacy account endpoints are deprecated: `POST /adsAccounts`, `POST /adsAccounts/batch`, `GET /adsAccounts/{accountId}`, `POST /adsAccounts/list`, `GET /dsp/advertisers` and `GET /dsp/advertisers/{advertiserId}`. Amazon's transition notes read: "Starting July 2026, all six legacy endpoints return `Warning: 299` response headers indicating deprecation"; "Starting July 2026, new client integrations are blocked. Existing callers continue to function through an allowlist until the shutoff date"; "Beginning July 2027, requests to these endpoints will return `HTTP 404 Not Found`." The named replacement for "Account retrieval and listing" is `POST /adsApi/v1/query/advertiserAccounts` (and for creation `POST /adsApi/v1/create/advertiserAccounts`). The release note announcing it is dated 2026-07-20 (dates for human readers only). [official] *Deprecations* ("July 2026 - Deprecation of legacy account management APIs"), https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations; *Ads API release notes*, "Deprecation of legacy account management APIs" (2026-07-20), https://advertising.amazon.com/API/docs/en-us/release-notes/index; both read 2026-11-09. A skill that needs the global account ID therefore reads it from `POST /adsApi/v1/query/advertiserAccounts`, not from `/adsAccounts*`; a new integration such as cx's is among those Amazon says are blocked from the legacy endpoints.

**The words for the three identifiers.** The Amazon Ads API v1 getting-started reference names three identifiers a caller meets:

- **Advertising Account**: "The primary account entity that contains campaigns and data across all ad products"
- **Profile ID**: "Identifier used for sponsored ads operations (`Amazon-Advertising-API-Scope` header)"
- **Account ID**: "Identifier used for cross-product operations (`Amazon-Ads-AccountId` header)"

[official] *Getting started with Amazon Ads API v1*, https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/getting-started, read 2026-11-09.

**Seller ad products need Brand Registry beyond SP.** The profiles guide notes that sellers need Brand Registry for SB and SD. Eligibility itself belongs to `beyond/ad-products-and-eligibility.md`. [official] *Profiles*, as above.

### B. The object hierarchy per ad product — RULE

**Sponsored Products.** Campaign → ad group → product ads and targets (keywords or product/category targets), with negatives at two levels:

- campaign negatives (`/sp/campaignNegativeKeywords`, `/sp/campaignNegativeTargets`)
- ad-group negatives (`/sp/negativeKeywords`, `/sp/negativeTargets`)

The SP campaign-structure guide states what each campaign kind needs before it can serve. An automatic campaign needs a campaign, an ad group and a product ad. A manual campaign also needs at least one keyword or product target in each ad group. On negatives it says: "Both manual and auto campaigns can also contain negative product targeting expressions or negative keywords at the campaign level (in addition to the ad group level)." [official] *Sponsored Products campaign structure*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/get-started/campaign-structure, read 2026-11-09 via the docs' public markdown copy at `d3a0d0y2hgofx6.cloudfront.net/en-us/...md`.

The SP v3 OpenAPI file lists these resource paths:

- `/sp/campaigns`, `/sp/adGroups` and `/sp/productAds`
- `/sp/keywords`, `/sp/negativeKeywords` and `/sp/campaignNegativeKeywords`
- `/sp/targets`, `/sp/negativeTargets` and `/sp/campaignNegativeTargets`

Each path has the same four operations:

- POST to create
- PUT to update
- POST `.../delete`, which archives
- POST `.../list`

All take the media type `application/vnd.spCampaign.v3+json` (or the matching entity name). [official] SP v3 OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json, listed in the docs' `contracts.json`, both read 2026-11-09.

**Sponsored Brands.** Campaign → several ad groups → several ads of one ad type per ad group, plus targets (the version 4 "multi-ad group" model; legacy campaigns differ, below). The SB structure guide is explicit that "you can only include a single type of ad in each ad group". An ad group targets either keywords or products, not both. Campaigns "group your ads by their advertising budgets and dates". The page now says "An ad can have different creative formats including manual collection, auto collection, video or store spotlight"; its example also shows brand video ads. [official] *Campaign structure for Sponsored Brands*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/structure, read 2026-11-09.

**The SB v4 multi-ad-group model, and legacy campaigns.** What the structure guide describes is the version 4 ("multi-ad group") campaign. Amazon's v4 features page says that in October 2022 "Sponsored Brands introduced hierarchical version 4 campaigns, featuring multiple ad groups and ads"; its feature table lists "Capability to create multiple ad groups and ads" as "Not Available" in version 3 and "Available" in version 4. [official] *Sponsored Brands version 4 features and benefits*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/v4-features, read 2026-11-09. The rules, from Amazon's pages:

- **Several ad groups per campaign, several ads per ad group.** Ad groups "let you organize and manage your ads by brands, keywords, products, categories, ad formats, landing pages, or other classifications that tie to your goals". Ads are used "to manage different variations of your creatives": "Associate multiple ads with each ad group that share the same landing page but different ASINs, headlines, life style images, product category, or videos." The structure guide's example campaign has two ad groups: one with two brand video ads, the other with "Manual and Automatic Collection ads". [official] *Campaign structure for Sponsored Brands*, as above; *Migrating to version 4 Sponsored Brands campaigns*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4, read 2026-11-09.
- **One ad type, at least one ad, one targeting kind per ad group.** "There has to be at least one ad in an ad group and an ad group cannot have more than one ad type"; the ad types listed are "collections, video, brand video and store spotlight". "An ad group can be associated to either product or keyword targeting expressions." [official] *Getting started with campaigns* (Sponsored Brands), https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns, read 2026-11-09. [seat] The guide's example of manual and automatic collection ads in one ad group fits this if "collections" counts as one ad type; no page read says so in words.
- **What sits where.** The v4 `AdGroup` schema carries only `campaignId`, `name`, `state`, `adGroupId` and `extendedData`; `UpdateAdGroup` takes `name`, `state` and `adGroupId`. There is no ad-group bid. The v4 `Campaign` carries `budget`, `budgetType`, `bidding`, `goal`, `costType`, `smartDefault`, `portfolioId`, `siteRestrictions`, `tags`, `startDate`, `endDate`, `brandEntityId`, `ruleBasedBudget` and `isMultiAdGroupsEnabled` (a boolean). Bids sit on keywords and targets: `POST /sb/keywords` takes an `adGroupId` and a `campaignId` per keyword, at most 100 per call. Create calls for campaigns and ad groups take at most 10 items. [official] SB v4 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json; SB v3 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml; both read 2026-11-09. In SB, then, two ad groups of one campaign share its budget, goal, cost type and placement bidding, and differ in their ads, their targeting and the bids on their targets.
- **Ads are moderated one by one.** "For multi ad group campaigns, only ads get moderated for the ad policy. If your ad gets rejected due to an ad policy violation, then your campaign status remains unchanged. In legacy campaigns, the creatives are linked to campaigns so if the creative gets rejected due to ad policy your campaigns status will change to rejected." And: "The new campaigns can continue to deliver impressions if there is one active ad." [official] *Migrating to version 4 Sponsored Brands campaigns*, as above.
- **Testing creatives side by side.** "Brands can test different creatives within the same ad group"; "you can test different versions of the same ad formats within the same ad group to get a better understanding of shopper behavior". [official] same page, and *Sponsored Brands version 4 features and benefits*. No page read says how impressions are divided among the ads of one ad group (see `method/change-measurement.md`).

**Limits.** No Amazon page read gives an SB-specific count of ad groups per campaign or ads per ad group. Amazon's help page *Sponsored ads campaign limits* says its one table applies to "Sponsored Products, Sponsored Brands, and Display campaigns" (section I). Perpetua's help page adds an SB table: "Keywords in a campaign 1,000" and "Ads in a campaign 100" [opinion, citing "Amazon's guidelines" by a link]; search summaries of other vendor pages give 100 ad groups per SB campaign (not read, so not recorded as a reading). Perpetua, https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit, read 2026-11-09. A skill reads the real ceiling from the refusal a write returns.

**How legacy (version 3) campaigns differ.** Amazon's migration guide: "we refer to the current campaigns without multi-ad group support as **legacy campaigns** whereas campaigns with multi-ad group support are referred to as **multi-ad group campaigns**". In a legacy campaign:

- "The current campaigns contain read-only ad groups where creatives are associated with campaigns instead of ad groups."
- "Adding new ad groups to legacy campaigns is not allowed. The ad groups for these campaigns only support `GET` operations." Trying to update a legacy ad group with v4 returns `INVALID_ARGUMENT`.
- Ads have no `adId` or `name` (the v4 model: "Ads created using version 3/non-multi ad group campaigns do not have an associated adId").
- The v4 `nameFilter` on ad groups "will not work for legacy campaigns since the ad group name is auto-generated based on campaign name".
- Campaign `state` in v4 is the user's action, and `servingStatus` in the extended data is the serving state; in v3 the two were combined.

[official] *Migrating to version 4 Sponsored Brands campaigns*, as above; SB v4 OpenAPI, as above. The legacy campaigns' feature gaps, per Amazon's table: no goals, no `VCPM`, no multiple ad groups and ads, no theme targeting, no brand video, vertical video or slideshow, no landing-page edits, no new metrics, no ad group or ad ID in the purchased-product report, and no Amazon Marketing Stream. [official] *Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4-api, read 2026-11-09 (its Q26).

**Reporting gaps for legacy campaigns.** Amazon's reporting v3 pages carry this note: "Sponsored Brands reports are currently available in preview. During the preview period, data related to Sponsored Brands campaigns with flag `isMultiAdGroupsEnabled=False` will not be available." On 2026-11-09 it is on the reporting overview, the search term report page and the FAQ. [official] *Sponsored ads reporting overview (version 3)*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/overview; *Search term reports*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term; *Sponsored ads reporting FAQ (version 3)*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/faq; all read 2026-11-09. For version 2 reporting, the migration guide says multi-ad group campaigns appear only with `"creativeType": "all"` in the request, and legacy campaigns do not return `adId` in the ad report. [official] *Migrating to version 4 Sponsored Brands campaigns*.

**Since 2023, new campaigns are multi-ad group.** As of 2023-05-22 (US) and 2023-08-10 (all regions), "all campaigns created using the version 3 Sponsored Brands `POST /sb/campaigns` endpoint are stored as multi-ad group (version 4) campaigns", created "with one ad groups and one ad". The SB multi-ad group bulksheets guide warns that "Sponsored Brands campaigns created before November 15, 2022 will not show in the multi-ad group tab of bulksheets" and are found in the legacy tab. [official] *Ads API release notes* (2023-05-22, 2023-08-10), as above; *Migrating to version 4 Sponsored Brands campaigns* ("June 2023 update"); *Overview - Sponsored Brands multi-ad group campaigns in bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sb/overview; all read 2026-11-09.

**The migration of the remaining legacy campaigns creates new campaigns.** Amazon set deadlines for moving v3 campaigns to v4. They differ between pages (dates for human readers only):

- The release note of 2025-04-17: campaigns with no impressions over 180 days were to be migrated or archived by 2025-06-30, "otherwise Amazon will archive these campaigns by July 31, 2025"; impression-generating campaigns by 2025-09-30, "or face automatic migration by Amazon by December 31, 2025".
- The release note of 2025-10-14: zero-impression campaigns created before October 2022 by 2025-10-30, active ones by 2025-12-31.
- The partner migration guide's Q3: zero-impression campaigns by 2025-10-19, active ones by 2025-12-31, then "Amazon will archive the zero impression campaigns and automatically migrate the all Version 3 (V3) campaigns to Version 4 (V4) campaigns starting January 1st, 2026".

[official] *Ads API release notes* (2025-04-17, 2025-10-14); *Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API*; read 2026-11-09. What a migration does to a campaign's identity, from that guide and the v4 model:

- A migrated campaign is a new campaign with a new ID (`legacyCampaignId` → `newCampaignId` in `CampaignMigrationFinalStatus`). `MIGRATION_COMPLETE` means "Migration is complete and new V4 campaigns are ready to serve. The V3 campaigns are archived."
- "The **start date of the migrated campaign** will be updated to the **date the migration begins**, while the campaign name will remain the same with a **`migrated` suffix** appended."
- "The **legacy** **campaign ID** can be retrieved from the **tags of the migrated version 4 campaign**. It is stored under the `legacyCampaignId` key."
- On performance history (Q5): the process ensures "a clean transfer of campaign settings and structures while preventing unintended performance data carryover"; advertisers can "manually link and track performance metrics across version transitions".
- Migrated campaigns default to "Drive Page Visits" with `CPC` (Q18); "Migrated campaigns may require re-moderation", up to 72 hours; archived campaigns cannot be migrated (Q19).
- Endpoints: `POST /sb/v4/legacyCampaigns/migrationJob` (up to 1,000 `campaignIds`, `isStagedMigration`, `newCampaignState`), `.../migrationJob/status`, `.../migrationJob/results` and `/sb/v4/legacyCampaigns/overallMigrationResults`; "An advertiser can run only **one ongoing migration job** at a time".

[official] *Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API*; SB v4 OpenAPI; both read 2026-11-09. [seat] For structure history this matters: an SB campaign's performance before and after migration sits under two campaign IDs, joined only through the `legacyCampaignId` tag. No page read says whether any legacy SB campaign still exists after the automatic migration announced for 2026; a skill reads `isMultiAdGroupsEnabled` on each campaign rather than assuming.

**Product Collection: two end dates for two different things.** The Product Collection ad type is deprecated. The *Deprecations* entry ("June 2026 - Deprecation of Sponsored Brands Product Collection Ad Type") gives, for both the V0 and the V1 APIs, "**Shutoff Date:** January 2027": "Starting August 2026, requests to create new Product Collection ads will succeed but create a Manual Collection ad instead" (v1: `productCollectionSettings` "will be automatically mapped to `manualCollectionSettings`"); manual collections need at least 3 ASINs and titles of at most 32 characters; "Post January 2027, requests to create new Product Collection ads will return an error." [official] *Deprecations*, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations, read 2026-11-09. The API migration guide calls January 2027 the "**Final shutoff**. All API requests to create Product Collection ads will be rejected with an error", and answers "Will my existing Product Collection ads stop serving impressions?" with "No. Existing Product Collection ads will continue to serve impressions and can be read, queried, paused, or deleted via the current API endpoints." [official] *Product Collection Migration Guide*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-product-collection, read 2026-11-09. The release note of 2026-09-18 introducing `POST /sb/v4/migrations/list` says "Beginning February 2027, product collections will no longer be supported". [official] *Ads API release notes*, https://advertising.amazon.com/API/docs/en-us/release-notes/index, read 2026-11-09. Amazon's help page on the migration (last modified 2026-10-05) gives the February date its content: "Migrating ensures your campaigns continue running after product collections are deprecated in February 2027"; "Beginning February 2027, product collections will no longer be supported. Eligible (see common questions) product collection ads with 3 ASINs that have not been migrated will be automatically transitioned to manual collections featuring the same 3 ASINs. Product collections with fewer than 3 ASINs will not auto-migrate." [official] *Migrate from Product collections to Sponsored Brands collections*, https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P, read 2026-11-09. Read together: January 2027 is the end of creating Product Collection ads through the API; February 2027 is the end of support for existing Product Collection ads, with an automatic move to manual collections for eligible 3-ASIN ads. The bulksheet release note of 2026-07-06 ("Existing Product collection campaigns will continue to function and can be edited") describes the time before February 2027. All dates are for human readers only.

**Sponsored Display.** The SD overview gives the hierarchy campaign → ad group → product ad → targeting clauses. A campaign's tactic decides what its targeting can be:

- T00020: contextual (product and category targeting)
- T00030: audiences

`costType` is `cpc` or `vcpm`, and `bidOptimization` is `clicks`, `conversions` or `reach`. In the SD v3 API `DELETE` archives. [official] *Amazon Ads API for Sponsored Display overview*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/overview, read 2026-11-09.

**The Ads API v1 unified model.** Amazon's campaign management overview describes one model for every ad product. It has five entity types:

- campaigns
- ad groups
- ads
- targets
- ad associations (DSP only)

It covers SP, SB, SD, Sponsored TV and DSP. The campaign management overview's "Current limitations" say that "At launch, calls will be bound to one ad product at a time" and "API rate limits (TPS) will be per each ad product". [official] *Campaign management in the Amazon Ads API*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview, and *Campaign management entities*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/overview, both read 2026-11-09. The v1 overview states the intent plainly: "They will eventually fully replace the ad product-specific APIs." [official] *Amazon Ads API v1 overview*, https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview, read 2026-11-09.

The v1 paths are all POST: `/adsApi/v1/{create|query|update|delete}/{campaigns|adGroups|ads|targets|adAssociations}`, plus create, query and update (no delete) for `adExtensions`.

- **Create, update and delete** answer HTTP 207 with `success`, `error` and `partialSuccess` arrays, each keyed by the request `index`. One request can half-succeed, and the caller must read which items failed.
- **Query** answers 200, with a `nextToken` for paging. `QueryCampaignRequest` requires `adProductFilter` and takes `maxResults` 1–1,000. Its optional filters are `campaignIdFilter`, `goalFilter`, `marketplaceScopeFilter`, `nameFilter`, `portfolioIdFilter`, `retailerScopeFilter` and `stateFilter`.
- **Batch size:** the request schemas for create, update and delete allow up to 1,000 items, and each operation notes that "Batch size limits are specific to each ad product" (figure for human readers only).

[official] Ads API merged OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json, read 2026-11-09.

Release history (dates for human readers only):

- beta from 2025-05-29 ("over 190 separate variations" of CRUD endpoints, "reduced to 16")
- general availability for SP, SB and DSP announced 2025-08-01 and re-announced 2025-12-01, with SD and Sponsored TV "later in 2025"
- the v1 example-payloads page already carries SD and Sponsored TV payloads

The 2025-08-01 and 2025-12-01 announcements put the reduction as "nearly 200 separate variations … reduced to 16". [official] *Ads API v1 release notes*, https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v1, and *Example payloads*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/example-payloads, both read 2026-11-09.

The v1 `AdProduct` enum reads `AMAZON_DSP`, `FULL_FUNNEL`, `RMS`, `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS` and `SPONSORED_TELEVISION`. The enum describes `FULL_FUNNEL` as "Full funnel ad product combining multiple ad types." [official] merged OpenAPI, as above. [seat] It is probably the API side of the Full-Funnel Campaigns Amazon announced at unBoxed 2026 (section G); no page read links the two in words.

**Ads and targets in v1.** An ad carries:

- `adType`: AUDIO, COMPONENT, DISPLAY, PRODUCT_AD, THIRD_PARTY or VIDEO
- for SP, `creative.productCreative.productCreativeSettings.advertisedProduct`, with `productIdType` ASIN, SKU or RETAILER_OFFER. The global campaigns guide says sellers identify products by SKU and vendors by ASIN.

A target carries:

- `negative` (required)
- `targetType`: KEYWORD, PRODUCT, PRODUCT_CATEGORY, THEME and others
- `targetDetails`, holding exactly one of `keywordTarget`, `productTarget`, `productCategoryTarget`, `themeTarget` and so on
- `targetLevel`, AD_GROUP or CAMPAIGN, which is read-only and follows from where the target was created
- `bid.bid`

- `tags` (up to 50, per the merged OpenAPI)

The target guide notes: "Campaign-level targeting is supported only for a subset of sponsored ads targeting types." The v1 `TargetUpdate` schema carries only `bid`, `state`, `tags`, `campaignId`, `targetId` and the marketplace fields, so a v1 target's keyword or product cannot be changed by update. [official] *Target*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/target, and *Ad*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad, both read 2026-11-09.

The match-type enums:

| Enum | Values |
|---|---|
| `KeywordMatchType` | BROAD, PHRASE, EXACT |
| `ThemeMatchType` (SP auto groups) | KEYWORDS_CLOSE_MATCH, KEYWORDS_LOOSE_MATCH, PRODUCT_SUBSTITUTES, PRODUCT_COMPLEMENTS; also KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES and others for SB |
| `ProductMatchType` | PRODUCT_EXACT, PRODUCT_SIMILAR, PRODUCT_COMPLEMENTS, PRODUCT_REMARKETING |

What each match type does is `areas/keyword-and-product-targeting.md`'s. [official] merged OpenAPI, as above.

### C. What lives at each level — RULE

Structure matters because Amazon puts some settings on the campaign and others on the ad group or target. Two things can differ in a campaign-level setting only if they sit in different campaigns. This section records where each setting lives, from the SP v3 and v1 schemas and their guides.

**At campaign level (SP v3, `SponsoredProductsCreateCampaign`):**

- `name` and `targetingType` (AUTO or MANUAL)
- `state`
- `budget` (`budget`, `budgetType`)
- `dynamicBidding`, which holds the bidding strategy and the placement bid adjustments
- `startDate` and `endDate` (YYYY-MM-DD)
- `portfolioId`
- `siteRestrictions`
- `offAmazonSettings` (MAXIMIZE_REACH or MINIMIZE_SPEND)
- `tags` (a map, up to 50 properties)
- `autoManageCampaign`

The SP v3 campaign read object (`SponsoredProductsCampaign`) also carries, for global campaigns, `marketplaceBudgetAllocation` and `globalCampaignId`; these are not in the create schema. The update schema (`SponsoredProductsUpdateCampaign`) lists `targetingType`, but the update request's description says "Note: targetingType cannot be updated" (section D).

The bidding strategies are LEGACY_FOR_SALES (down only), AUTO_FOR_SALES (up and down, described with a "maximum of 100%" raise), MANUAL and RULE_BASED. [official] SP v3 OpenAPI, as above.

**At campaign level (v1 `Campaign`):**

- `adProduct`, `name`, `state`, `startDateTime`, `endDateTime`
- `autoCreationSettings.autoCreateTargets`, which is required for SP; `true` makes it an auto campaign
- `budgets[]`: up to two entries, each with `budgetType` (MONETARY), `budgetValue` and `recurrenceTimePeriod` (the `Recurrence` enum is DAILY, LIFETIME or MONTHLY), a single value or `marketplaceSettings[]`
- `optimizations.bidSettings`: `bidStrategy`, `bidAdjustments.placementBidAdjustments[]`, `audienceBidAdjustments`, `shopperSegmentBidAdjustments`
- `optimizations.goalSettings`: `goal`, `kpi`, `kpiValue`
- `optimizations.budgetSettings.offAmazonBudgetControlStrategy`
- `portfolioId`, `siteRestrictions` and `tags[]` (up to 50 key/value pairs)
- `marketplaceScope` (GLOBAL or SINGLE_MARKETPLACE, required for SP and SB), `marketplaces`, `marketplaceConfigurations`, `autoScaleGlobalCampaign` and `globalCampaignId`
- `costType` (required for SB), `brandId`, `retailerScope` and `eligibleAutomatedTargetingTactics`

The v1 `BidStrategy` values are MANUAL, NEW_TO_BRAND, PRIORITIZE_KPI_TARGET, RULE_BASED, SALES_DOWN_ONLY, SALES_UP_AND_DOWN, SPEND_BUDGET_IN_FULL and USE_CAMPAIGN_STRATEGY. [official] *Campaign*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/campaign, and merged OpenAPI, both read 2026-11-09.

The v1 `Placement` enum, which placement adjustments are keyed on:

| Placement | Amazon's description |
|---|---|
| TOP_OF_SEARCH | "Placements on the top row of the first-page search results." |
| REST_OF_SEARCH | "Placements on the middle or the bottom of the first-page search results. Also refers to ads on the second page of search results and beyond." |
| PRODUCT_PAGE | "Placements on the product detail page, and all nonsearch placements such as the add-to-cart page." |
| HOME_PAGE | Home page placements |
| SITE_AMAZON_BUSINESS | Amazon Business site placements |
| TOP_OF_BROWSE, REST_OF_BROWSE | Only for the OTHER_RETAILERS retailer scope |

[official] merged OpenAPI, as above. What the adjustments are worth is `areas/bids-and-placements.md`'s. The structural fact here is that they are a property of the campaign, so a keyword that should be pushed to the top of search harder than its neighbours needs a campaign of its own. That is the mechanism practitioners cite for single keyword campaigns (section 2 of *What practitioners add*).

**At ad-group level.** The SP ad group guide says "Products placed together in an ad group share the same bids and targeting (keyword or product)". The ad group's default bid applies to every target in it without a bid of its own, and "Ad group names must be unique within a campaign". [official] *Creating Sponsored Products ad groups*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/ad-groups, read 2026-11-09. The v1 ad group carries `bid.defaultBid` (required for SP), optional `bid.marketplaceSettings[]` for global campaigns, `name`, `state` and `tags`. For SP and SB, `marketplaceScope` and `marketplaces` are read-only on the ad group because they come from the campaign. [official] *Ad group*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad-group, read 2026-11-09.

**At target level.** A target has its own bid, which overrides the ad group's default bid, and its own state. In SP v3, `SponsoredProductsUpdateKeyword` takes only `keywordId`, `bid` and `state`. [official] SP v3 OpenAPI, as above.

**One kind of targeting per SP ad group.** The SP bulksheets guide states that "you cannot have both keyword and product targeting in a single ad group". [official] *Get started with bulksheets for Sponsored Products*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/get-started, read 2026-11-09. In an auto campaign the ad group holds the four auto targeting groups instead (section E).

**The budget is the campaign's, not the ad group's.** Mina Elias (Helium 10, 2020, modified 2022) states that "Amazon distributes the budget at their own discretion" between the ad groups of one campaign [opinion]. Vince Montero (Helium 10) gives the same mechanism as his reason for separate campaigns: "budget control is housed on the campaign level" [opinion]. The schemas agree that there is no ad-group budget field in SP v3, and the v1 ad group guide marks `budgets` as a DSP-only ad-group field [official]. A seller who wants a fixed share of spend for one set of products or keywords can get it only with a campaign or a portfolio. Budget behaviour itself is `areas/budgets-and-pacing.md`'s.

### D. States, archive and what cannot change — RULE

**The state values.**

| API | States |
|---|---|
| SP v3 `SponsoredProductsEntityState` | ENABLED, PAUSED, ARCHIVED, ENABLING, PROPOSED, USER_DELETED, OTHER |
| SP v3 create/update state | ENABLED, PAUSED, PROPOSED |
| v1 `State` | DRAFT, ENABLED, PAUSED, PROPOSED, ARCHIVED |

v1 describes ARCHIVED as: "The object is permanently stopped and cannot be reactivated. Terminal end state." v1's `CreateState` and `UpdateState` exclude ARCHIVED, so a v1 caller archives through `POST /adsApi/v1/delete/...`, not through an update. The v1 update-campaign notes add that DSP does not accept ARCHIVED. [official] SP v3 OpenAPI and merged OpenAPI, both read 2026-11-09.

**Archive is a delete in every API.**

- SP v3: archiving is `POST /sp/<entity>/delete`.
- SD v3: `DELETE` archives (SD overview).
- v1: archiving is `/delete/...`.
- Bulksheets: archiving is the Operation value "Archive" on the entity's row.

[official] the pages above, and *Get started with bulksheets for Sponsored Products*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/get-started, read 2026-11-09.

**Archive cannot be undone.** The v1 `State` enum calls ARCHIVED a "Terminal end state" (above), and the global campaigns guide calls it "terminal". On the Seller Forums an Amazon staff account (Tatiana_Amazon, about three years before the read date) answered a seller asking how to revive archived campaigns:

> "Archived campaigns cannot be enabled or copied once they have been archived. They remain available in the ads console if needed for future reference, but if you are looking to duplicate the archived campaign, you will need to create a new campaign or copy an active or paused campaign. We suggest setting campaigns to Paused instead of Archived if you are planning to utilize the campaign again."

[official, forum staff reply] *Revive campaign from archive*, https://sellercentral.amazon.com/seller-forums/discussions/t/de6fac84-a3a2-44df-9074-c62cf980ec76, read 2026-11-09.

The bulksheets release notes of 2026-08-31 add that "Archived campaigns are not available in the campaign filter" of the filtered export. [official] *Ads API release notes*, https://advertising.amazon.com/API/docs/en-us/release-notes/index, read 2026-11-09.

**The archive error reasons.** SP v3's `EntityStateErrorReason` enum names the refusals a caller meets around archive:

- ARCHIVED_ENTITY_CANNOT_BE_MODIFIED
- PARENT_ARCHIVED_FORBIDS_UPDATES
- PARENT_ENTITY_FORBIDS_CREATION
- PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES
- INVALID_STATE_TRANSITION
- AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY
- MARKETPLACE_STATE_CANNOT_BE_ARCHIVED

[official] SP v3 OpenAPI, as above. Three facts follow from Amazon's own enum:

- An archived campaign freezes its children, since updates and creates under it are refused.
- An auto campaign's four targeting groups cannot be archived on their own; they can be paused.
- In a global campaign a single marketplace's state cannot be set to archived.

**Archive cascades.** The global campaigns guide says that `delete` archives and that "Archiving a campaign cascades its ad groups, ads, and targets to `ARCHIVED`." [official] *Global campaigns for Sponsored Products*, as above. For SP in bulksheets, Amazon's update guide says: "When you archive a parent entity, all child entities will also be archived. You should avoid archiving both a parent and its child entity, or you will get an error indicating that the child entity failed to archive." [official] *How to update Sponsored Products campaigns with bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/update-sp-campaigns, read 2026-11-09. The seat found no page stating the cascade in words for a single-marketplace SP v3 or v1 `delete` call; the error reason PARENT_ARCHIVED_FORBIDS_UPDATES at least freezes the children (Open questions).

**Fields that cannot change after creation.** A change to any of these is, in Amazon's model, a new entity plus a paused or archived old one. Amazon's bulksheet page on editable fields states the general route: "For fields that cannot be edited (for example, keyword text or `ASIN`/`SKU`), a typical workaround is to archive its associated entity, then create a new one with the updated information." [official] *Understand which fields can be updated*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/editable-non-editable-bulksheets-fields, read 2026-11-09.

- **Keyword text and match type.** The SP v3 keyword update takes only `keywordId`, `bid` and `state`. In bulksheets, Keyword Text and Match Type are "No" under "Can update?": "You cannot update keywords by changing the keyword text." [official] SP v3 OpenAPI and *Understand which fields can be updated*.
- **Product targeting expression.** In bulksheets, "Product Targeting Expression" cannot be updated: "Targeting can only be archived or paused." The v1 `TargetUpdate` schema has no `targetDetails`. Note that the SP v3 `SponsoredProductsUpdateTargetingClause` schema does list `expression` and `expressionType`; the seat found no SP v3 text saying whether an expression update is accepted. [official] *Understand which fields can be updated*; merged OpenAPI; SP v3 OpenAPI.
- **Ad group.** `SponsoredProductsUpdateAdGroup` takes only `adGroupId`, `defaultBid`, `name` and `state`. [official] SP v3 OpenAPI.
- **Product ad.** `SponsoredProductsUpdateProductAd` takes `adId` and `state`. In bulksheets: "You cannot update a `SKU` or `ASIN`, but you can pause or archive the associated product ad entity and then create a new one". [official] SP v3 OpenAPI; *Understand which fields can be updated*.
- **Targeting type.** The SP v3 update request says "Note: targetingType cannot be updated" (the field is listed in the update schema all the same); the v1 `CampaignUpdate` schema has no `autoCreationSettings`; in bulksheets "You cannot update an auto campaign to be manual, and vice versa." [official] SP v3 OpenAPI; merged OpenAPI; *Understand which fields can be updated*.
- **Site restriction.** The SP v3 `siteRestrictions` description: "siteRestrictions cannot be changed post campaign creation". [official] SP v3 OpenAPI.
- **Start date (bulksheets).** "When updating a campaign, you cannot change the start date." [official] *Understand which fields can be updated*. The SP v3 update schema does list `startDate`; the seat did not find a statement on whether the API accepts a start-date change.
- **SB goal-based campaigns.** "Once a goal-based campaign is created, the `goal`, `costType`, and `smartDefault` values are not editable." [official] *Getting started with campaigns* (Sponsored Brands), https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns, read 2026-11-09.

**Delivery status is separate from state.** v1 `Status` is read-only. It holds `deliveryStatus` (DELIVERING, LIMITED, NOT_DELIVERING, UNAVAILABLE), up to 50 `deliveryReasons` and up to 30 per-marketplace settings. Many delivery reasons are structural:

- CAMPAIGN_PAUSED, CAMPAIGN_ARCHIVED and CAMPAIGN_INCOMPLETE (a manual ad group with no target, for example)
- CAMPAIGN_OUT_OF_BUDGET
- PORTFOLIO_OUT_OF_BUDGET, PORTFOLIO_PAUSED, PORTFOLIO_ARCHIVED, PORTFOLIO_END_DATE_REACHED and PORTFOLIO_PENDING_START_DATE
- AD_GROUP_INCOMPLETE and AD_GROUP_LOW_BID
- TARGET_PAUSED and TARGET_BLOCKED
- ADVERTISER_OUT_OF_BUDGET and SPEND_LIMIT_EXCEEDED
- OUT_OF_STOCK, NOT_IN_BUYBOX and NO_PURCHASABLE_OFFER

[official] merged OpenAPI, as above. The SP v3 serving-status enums carry the same family, with different spellings (for example PORTFOLIO_ENDED where v1 says PORTFOLIO_END_DATE_REACHED, and PORTFOLIO_STATUS_ENABLED), when `includeExtendedDataFields` is requested on a list call. Reading these is `areas/diagnosis.md`'s. The structural fact is that a portfolio's state and cap appear in each of its campaigns' delivery reasons.

### E. Auto and manual targeting — RULE and GUIDANCE

**RULE: auto or manual is fixed when the campaign is created.** It is SP v3's `targetingType` (AUTO or MANUAL) and v1's `autoCreationSettings.autoCreateTargets`, which is required for SP. The SP v3 update request says "Note: targetingType cannot be updated"; the v1 `CampaignUpdate` schema has no `autoCreationSettings`; bulksheets say "You cannot update an auto campaign to be manual, and vice versa." [official] SP v3 OpenAPI; merged OpenAPI; *Understand which fields can be updated*; as above.

**RULE: an auto campaign's targets are four theme groups.**

| Group | v1 theme | Bulksheet entity |
|---|---|---|
| close match | KEYWORDS_CLOSE_MATCH | close-match |
| loose match | KEYWORDS_LOOSE_MATCH | loose-match |
| substitutes | PRODUCT_SUBSTITUTES | substitutes |
| complements | PRODUCT_COMPLEMENTS | complements |

In a global auto campaign, Amazon creates the four THEME targets for each marketplace. [official] *Global campaigns for Sponsored Products*. In bulksheets a seller can write the four groups on create: "If you do not create all four entities, Amazon will automatically create them, and the ad group default bid will apply." [official] *How to create Sponsored Products campaigns with bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/create-sp-campaign, read 2026-11-09. Each of the four groups has its own bid and state. None can be archived by hand (AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY). [official] SP v3 OpenAPI. The auto campaign also takes negative keywords and negative product targets at both levels. What the four groups match is `areas/keyword-and-product-targeting.md`'s.

**GUIDANCE: Amazon suggests starting with auto.** The Ads API's own SP campaign-structure guide carries a tip box:

> "We suggest new advertisers start with auto campaigns. You can then analyze the performance of suggested keyword and targeting expressions, and create a manual campaign using the highest performers."

[official] *Sponsored Products campaign structure*, as above.

The Amazon Ads new-advertiser success guide gives the same order to a console reader. It also says "Just $10 a day can help you get clicks and sales" and recommends no end date, and two eligibility checks before advertising: the featured offer at 90% or more, and at least five reviews and a 3.5-star rating (figures for human readers only). [official] *New advertiser success guide*, https://advertising.amazon.com/library/guides/new-advertiser-success-guide, read 2026-11-09.

The library best-practices guide says to "Create manual campaigns to supplement your automated campaign". It adds that manual targeting "allows you to split campaigns based on objectives". [official] *Best practices for your Sponsored Products ads*, https://advertising.amazon.com/library/guides/sponsored-products-best-practices, read 2026-11-09.

**GUIDANCE: running both, for a new country.** Amazon's international checklist sets the sequence for a new marketplace: "Once you've mastered automatic targeting, launch a manual product targeting campaign". It recommends "multiple match types to help you discover what performs well for your ads in a new country". It also tells the reader to read the auto campaign's search term report, "Select top-performing ones and add these to a campaign with manual keyword targeting". [official] *Checklist for new international ad campaigns*, https://advertising.amazon.com/library/guides/checklist-for-new-international-ad-campaigns, read 2026-11-09.

### F. Target promotion groups: Amazon's own harvest structure — RULE

SP v3 has a resource for the auto-to-manual path that practitioners build by hand: `/sp/targetPromotionGroups`. Its operations are create, list, recommendations, targets and targets/list. Create, list, targets and targets/list take v1 and v2 media types (`application/vnd.sptargetpromotiongroup.v1+json` / `.v2+json`, `application/vnd.sptargetpromotiongrouptarget.v1+json` / `.v2+json`); recommendations takes only `application/vnd.spTargetPromotionGroupsRecommendations.v1+json`.

**What a group is.**

- In the v1 form, a group ties an auto ad group ("The adGroupId of the Ad Group of an Auto-Targeting campaign") to manual keyword and product ad groups that take its winners.
- In the v2 form it is a "source Ad Group" with destination manual ad groups, existing or new (`existingCampaignDetails`, `newCampaignDetails`, at most two entries each), and a `targetPromotionGroupName`.

**The recommendations call.** The OpenAPI description of `/sp/targetPromotionGroups/recommendations` reads:

> "Retrieves keyword and product targets of an auto-targeting campaign as recommendations for promoting to a manual-targeting campaign. The recommendations are based on performance heuristics of the targets."

The targets call takes up to 1,000 items (figure for human readers only). [official] SP v3 OpenAPI, as above. The seat found no guide page for this resource; four guessed paths returned 404 (Unreachable).

The heuristics are not published. What a promoted term is (which search terms, how many clicks, how many orders) is therefore Amazon's model, read through its recommendations, and harvesting rules belong to `areas/search-terms-and-negatives.md`. The structural fact is that Amazon models the auto → manual promotion as a named link between ad groups. A skill reading a seller's structure can find that link instead of inferring it from names.

### G. Campaign goals and objectives — RULE

**Sponsored Products.** The v1 campaign carries `optimizations.goalSettings` (`goal`, `kpi`, `kpiValue`), and `QueryCampaignRequest` takes a `goalFilter`. The v1 campaign guide marks goal settings per ad product. For SB the goal is read-only and the KPI is required; for SP the seat found no goal value the guide says SP accepts. The v1 `Goal` enum is AWARENESS, CONSIDERATION, CONVERSIONS and ENGAGEMENT. The KPI enum includes CLICKS, ROAS, TOP_OF_SEARCH_IMPRESSION_SHARE and NEW_TO_BRAND_PURCHASES, among others. [official] *Campaign* and merged OpenAPI, as above.

What an SP campaign is for is expressed through its settings, not through a goal field:

- targeting type
- bid strategy (including RULE_BASED with a rule, and v1's PRIORITIZE_KPI_TARGET)
- placement adjustments
- budget

A practitioner's "ranking", "defend" or "harvest" campaign has no Amazon field. It exists only in the seller's names, tags and settings (sections J and *What practitioners add*).

**Sponsored Brands goal-based campaigns.** SB campaigns take a `goal` of BRAND_IMPRESSION_SHARE, for which "only `costType` `VCPM` is available", or PAGE_VISIT; with neither `goal` nor `costType` in the request, the default is PAGE_VISIT with CPC. Both `goal` and `costType` must be sent to create a goal-based campaign. They also take a `smartDefault` of MANUAL or TARGETING. All three are fixed at creation (section D). Goal-based campaigns are not supported in the Ireland marketplace; there both fields must be omitted, and sending them returns GOAL_BASED_CAMPAIGNS_DISABLED. [official] *Getting started with campaigns* (Sponsored Brands), as above.

Amazon's announcement page names the two goals as "Drive page visits" (success metric "clicks", served "across search pages, detail pages, and the home page") and "Grow brand impression share" (success metric "top-of-search impression share", paid "by cost per 1,000" impressions). It says "All previously created Sponsored Brands campaigns will be tagged as 'Drive page visits.'" It frames the pair as a structure:

> "Combining these two campaign goals in the campaign portfolio, brands can structure campaigns…"

The same page cites an Amazon statistic: 60% of shoppers who searched a brand bought from a competitor within 30 days (6,000 advertisers, June 2023; figure for human readers only). [official] *Sponsored Brands goal-based campaigns*, https://advertising.amazon.com/resources/whats-new/sponsored-brands-goal-based-campaigns, read 2026-11-09. The international checklist recommends the drive page visits goal first and grow brand impression share once established. [official] *Checklist for new international ad campaigns*, as above.

**Sponsored Display** expresses its objective as `bidOptimization` (`clicks`, `conversions`, `reach`) together with the tactic (contextual T00020 or audiences T00030) and `costType`. [official] *Amazon Ads API for Sponsored Display overview*, as above.

**Full-Funnel Campaigns and the Amazon Ads Agent.** Amazon's unBoxed 2026 news page (2026-09-30) describes:

- Full-Funnel Campaigns, in which the advertiser sets a goal and "AI handles the channel mix"
- Amazon's beta figures for them: +67% long-term ROAS and −29% new-to-brand cost (figures for human readers only)
- an Amazon Ads Agent that "brings together what was formerly the DSP and Ads Console" for sponsored ads, Full-Funnel Campaigns and DVA+, with the conversational part in expanded closed beta

[official] *unBoxed 2026 news: Explore the latest advertising announcements*, https://advertising.amazon.com/library/news/unboxed-2026-news-announcements, read 2026-11-09. [seat] The `FULL_FUNNEL` value of v1 `AdProduct` is likely the API trace of this. A goal-led campaign in which Amazon picks the channels is a structure in which the seller no longer chooses ad product, campaign or ad group for each slice. How far that reaches into sponsored ads is not documented on the pages read (Open questions). The unBoxed 2025 page described the revamped Campaign Manager beta: an "All View", smart search, multi-account management and a universal "+" button. That page said the beta was "currently available to a select group of advertisers and partners" with a broader rollout planned. [official] *Campaign Manager beta: One command center for every campaign*, https://advertising.amazon.com/resources/whats-new/unboxed-2025-campaign-manager, read 2026-11-09.

**Auto-managed campaigns.** The v1 `autoCreationSettings.autoManageCampaign` is documented as a "Flag that allows Amazon to manage the lifecycle of your Campaign"; SP v3's `autoManageCampaign` boolean carries no description. [official] merged OpenAPI (`AutoCreationSettings`) and SP v3 OpenAPI, as above. The v1 *Campaign* entity guide does not list the field. What Amazon then does is `beyond/automation-and-amazon-tools.md`'s. For structure, a campaign carrying the flag has a lifecycle that is not only the seller's.

### H. Portfolios and their budget caps — RULE

**What a portfolio is.** The portfolios guide says a portfolio groups campaigns and that portfolios "do not compete against each other". It lists the uses:

- managing several brands
- budget caps
- sharing unspent budget
- performance tracking
- billing

"A campaign can only belong to one portfolio at a time." [official] *Get started with Portfolios*, https://advertising.amazon.com/API/docs/en-us/guides/portfolios/get-started, read 2026-11-09. The Amazon Ads help page on portfolios gives the same uses and adds that billing "will reflect the portfolio mapping at the time the invoice is issued", and that the console now labels spend "Cost (formerly known as Spend on sponsored ads)". [official] *Understand portfolios*, https://advertising.amazon.com/help/GPEJN2E6R52G7C2T (content embedded in the page's HTML, last modified 2026-02-24), read 2026-11-09. A campaign joins a portfolio through its own `portfolioId`, which the update schemas of SP v3 and v1 include. "The `portfolioId` metric in reporting returns all campaigns associated with a specific `portfolioId`." [official] SP v3 OpenAPI and *Get started with Portfolios*.

**The API.** The v3 operations are POST `/portfolios` to create and PUT `/portfolios` to update (each up to 100 per call) and POST `/portfolios/list`, all in `application/vnd.spPortfolio.v3+json`. Budget usage is POST `/portfolios/budget/usage` in `application/vnd.portfoliobudgetusage.v1+json`. It takes up to 100 IDs and returns `budgetUsagePercent` and `usageUpdatedTimestamp`. The v2 `/v2/portfolios` was shut off on 2025-03-01 (date for human readers only). [official] Portfolios OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json, and *Deprecations*, both read 2026-11-09.

**The cap.** A portfolio's `budget` object is `{amount, currencyCode, startDate, endDate, policy}`. The policy is one of:

- DATE_RANGE
- MONTHLY_RECURRING
- NO_CAP
- OTHER

To remove a cap, the caller nulls the fields and sets NO_CAP. Budget errors include BUDGET_TOO_LOW and BUDGET_LT_DEFAULT_BIDS, a cap below the default bids of its campaigns. A QUOTA_EXCEEDED error exists with ACCOUNT scope, so the number of portfolios has a limit Amazon enforces. The seat found no page that states it, and the Amazon help page *Sponsored ads campaign limits* (section I) lists no portfolio count. Capconvert also says Amazon "does not publish a hard maximum number of portfolios per account" [opinion]. The serving statuses are:

- PORTFOLIO_STATUS_ENABLED
- PORTFOLIO_OUT_OF_BUDGET
- PORTFOLIO_ENDED
- PORTFOLIO_PENDING_START_DATE
- ADVERTISER_* values, among them ADVERTISER_OUT_OF_BUDGET, ADVERTISER_ACCOUNT_OUT_OF_BUDGET and ADVERTISER_EXCEED_SPENDS_LIMIT

Each also carries a boolean `inBudget`. [official] Portfolios OpenAPI, as above.

**State.** The v3 Portfolio `EntityState` enum has a single value, ENABLED. The v1 campaign delivery reasons still include PORTFOLIO_PAUSED and PORTFOLIO_ARCHIVED. [official] Portfolios OpenAPI and merged OpenAPI. The seat reads this as an API that cannot pause or archive a portfolio, while the system still reports portfolios in those states, perhaps set in the console or left from v2. No page read explains the gap (Open questions).

**Unspent budget sharing.** Portfolios carry `budgetControls.campaignUnspentBudgetSharing.featureState`, ENABLED or DISABLED. The sharing guide states the default and the mechanism:

- **Default:** on by default for portfolios created after 2025-06-20.
- **Mechanism:** campaigns that have spent their full daily budget may use siblings' unspent budget "from previous days in the month", "allowing them to spend up to 100% more than their average daily budget on any given day".
- **Ceiling:** the month's total stays at or below the sum of the daily budgets times the days in the month.
- **Billing:** the invoice is adjusted for any over-delivery.

Release notes of 2025-07-07 (launch) and 2025-07-19 (an update listing the geographies and the eligible advertiser types: vendors, registered sellers, managed-service and self-service customers, authors) record it (dates and percentages for human readers only). [official] *Sharing leftover budget*, https://advertising.amazon.com/API/docs/en-us/guides/portfolios/sharing-leftover, and *Ads API release notes*, both read 2026-11-09. A portfolio is therefore a structural lever on spend in two ways: it can stop a set of campaigns at a cap, and it can let them move budget between themselves.

**GUIDANCE on what to group.** Amazon's library suggests "creating portfolios to organize your campaigns by brand, category, season, or any way you choose". [official] *Best practices for your Sponsored Products ads*, as above. An Ad Intel article hosted on Amazon's site is written by a partner, Brent Zahradnik of AMZ Pathfinder, an Amazon Ads Verified Partner. It advises:

- "use logical grouping with portfolios to organize campaigns by brand, product line, or seasonality"
- setting budgets in order: "Start with setting your daily account-level budget, then portfolio-level, and finally campaign-level"
- when a keyword's "velocity of spend exceeds what is available in the campaign it's in", moving it "to a different campaign"

[opinion, on an Amazon page] *Ad Intel: 5 common sponsored ads campaign mistakes*, https://advertising.amazon.com/library/expert-advice/common-sponsored-ads-mistakes-and-solutions, read 2026-11-09. The account-level budget that article refers to matches the ADVERTISER_OUT_OF_BUDGET delivery reason. That makes Capconvert's sentence "a portfolio is the only mechanism Amazon gives you to cap total monthly spend" [opinion] doubtful as stated; the seat did not read an Amazon page describing the account-level budget (Open questions).

### I. Entity limits — RULE

**Amazon's limits reference.** The Ads API limits page was read in full. It gives:

- a per-marketplace table of minimum and maximum bids, for example US SP 0.02 to 1,000
- daily budget minimums and maximums, for example US SP 1 to 1,000,000
- keyword constraints: at most 80 characters and 10 words for a positive keyword, and 4 words for a negative phrase (10 for negative exact)
- that "Automatically Selected Keywords" is reserved
- the allowed script ranges per marketplace
- entity name constraints (section J)
- P99 latencies: 30 seconds for synchronous CRUD, 12 hours from an impression or click to the API, and 72 hours for traffic invalidation

All these figures are for human readers only. [official] *Limits, constraints, and quotas*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, read 2026-11-09.

**Entity counts: Amazon's help page.** For counts the SP campaign-structure guide links to the Amazon Ads help page G86H2227323T8T4Q. A plain GET of that page returns a script shell, but the article itself is embedded in the HTML (`window.__scV2Content`), titled *Sponsored ads campaign limits*, status "Live", last modified 2026-07-29. It says the limits "apply to Sponsored Products, Sponsored Brands, and Display campaigns across all advertiser types (sellers, vendors, and authors)" and gives:

| Type | Amazon's limit |
|---|---|
| Campaigns in your account (active and paused) | 10,000 |
| Ad groups in a campaign | 20,000 |
| Ad groups in an account | 200,000 |
| Ads in an ad group | 10,000 for manual targeting |
| Ads in an account | 2,000,000 |
| Keywords in an ad group (excluding negative keywords) | 1,000 for manual targeting |
| Keywords in an account (including negative keywords) | 2,000,000 |
| Category and product targets in an ad group | 10,000 |
| Campaign negative keywords | 10,000 |
| Ad group negative keywords | 10,000 |
| Negative products in an ad group (product targeting) | 10,000 |
| Negative phrase | 4 words or 80 characters |
| Negative exact | 10 words or 80 characters |

Its note is load-bearing: "Advertisers can archive campaigns, ad groups, ads, or targets to free up space. Amazon now increases customer limits as they approach a limit beyond the limits listed below. Customers can contact us to request ad hoc increases, if they are planning large account changes or restructures." [official] *Sponsored ads campaign limits*, https://advertising.amazon.com/help/G86H2227323T8T4Q, read 2026-11-09. Every count is for human readers only; by Amazon's own note, an account's real ceiling can sit above the table.

**Third-party tables, now superseded where they differ.** The counts that circulate from third parties partly match Amazon's page and partly do not:

| Limit (SP) | Perpetua help, 2026-02-12, citing Amazon help | Karooya, 2019-02-21, no source | Amalyze, undated, no source |
|---|---|---|---|
| Campaigns per account | 10,000 (active and paused) | 10,000 | "up to 1 million" |
| Ad groups per campaign | 20,000 | 20,000 | 10,000 |
| Ad groups per account | 200,000 | 200,000 | — |
| Product ads per ad group | 10,000 manual; 500,000 auto | same | 1,000 ASINs |
| Product ads per account | 2,000,000 | same | — |
| Keywords per ad group | 1,000 | 1,000 | 1,000 |
| Keywords per account (incl. negatives) | 2,000,000 | same | — |
| Category and product targets per ad group | 10,000 | 10,000 | 1,000 |
| Campaign negative keywords | 1,000 | 1,000 | — |
| Ad-group negative keywords | 1,000 | 1,000 | 1,000 |
| Negative products per ad group | 10,000 | 10,000 | 1,000 |

Against Amazon's page of 2026-07-29: the negative-keyword counts (1,000) in Perpetua and Karooya are lower than Amazon's 10,000; the "500,000 auto" ads figure is not on Amazon's page; Amalyze's figures (1 million campaigns, 10,000 ad groups per campaign, 1,000 product targets) do not match Amazon's. Capconvert (updated 2026-05-30) gives Perpetua's counts and calls them ceilings "none of which can be raised", which Amazon's note ("Amazon now increases customer limits as they approach a limit") contradicts. Perpetua adds, for SB, 1,000 keywords and 100 ads per campaign. Amalyze adds 100 ad groups per campaign for SB. [opinion] Perpetua, https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit; Karooya, https://www.karooya.com/blog/amazon-ads-campaign-limits-you-must-know/; Amalyze, https://amalyze.com/resources/guides/advertising/amazon-ppc-bid-and-keyword-limits; Capconvert, https://www.capconvert.com/learn/blog/amazon-ads-account-structure; all read 2026-11-09. The library best-practices page says "You can add 1,000 products to an ad group at a time", which is a per-action figure and not a cap. [official] *Best practices for your Sponsored Products ads*.

**What the API returns: the refusal.** SP v3 has a `QuotaErrorReason` of QUOTA_EXCEEDED or NON_ARCHIVED_QUOTA_EXCEEDED, with a `quotaScope` of ACCOUNT or PARENT_ENTITY. [official] SP v3 OpenAPI. NON_ARCHIVED_QUOTA_EXCEEDED shows that at least some quotas count only non-archived entities, which matches the help page's "active and paused" wording and its note that archiving frees up space. Whatever the true counts, a write that would cross one is refused with a reason that names the scope.

### J. Names, tags and naming guidance — RULE and GUIDANCE

**RULE: name constraints.**

- Campaign names: at most 128 characters for sellers, 116 for vendors.
- Ad group names: at most 255 characters.
- Allowed symbols: Amazon lists them, including `- $ " ' & ( ) * + , . / : ; = ? @ \ [ ] _ ` ~ { }` and the pipe `|`.
- No leading or trailing spaces.

These lengths are figures for human readers only. [official] *Limits, constraints, and quotas*, as above. Ad group names must be unique within a campaign. [official] *Creating Sponsored Products ad groups*. The v1 `nameFilter` and SP v3 `nameFilter` let a list call select by name. [official] SP v3 OpenAPI and merged OpenAPI.

**RULE: tags.** Campaigns carry up to 50 tags:

- in SP v3, a map with `maxProperties` 50
- in v1, `tags[{key, value}]` with `maxItems` 50, on campaigns, ad groups and targets

[official] SP v3 OpenAPI and merged OpenAPI. Tags are a structured place for what practitioners otherwise encode in names: the ASIN, the intent, the stage, the owner. The seat found no Amazon page that says how tags show in the console or in reports (Open questions).

**GUIDANCE: names should be plain.** The new-advertiser guide says "Give your campaign a name: Keep it straightforward". [official] *New advertiser success guide*. The Ad Intel partner article names "Campaigns that are built without clear naming conventions, mixed targeting types, unclear objectives, overlapping targeting, and scattered ASINs" as "The most visible problem we see when doing campaign audits". It advises "a consistent naming convention across all portfolios, campaigns, and ad groups". [opinion, on an Amazon page] Brent Zahradnik, *Ad Intel*, as above.

### K. Multi-marketplace and multi-language structure — RULE and GUIDANCE

**RULE: the default unit is one campaign per marketplace.** Every profile is one marketplace (section A). A seller in five marketplaces with no global campaigns has five separate campaign trees. Their names, currencies, keyword languages and budgets do not relate to each other in Amazon's model.

**RULE: global SP campaigns are one campaign with marketplace children.** Amazon's Global Campaign Management for SP uses `marketplaceScope` GLOBAL under the account ID header. The guide gives these rules:

- **Subsets.** "a child's list must be a subset of its parent's" marketplaces.
- **Single-marketplace children.** Ads and targets each carry a single marketplace. An ad is created per marketplace with that marketplace's ASIN or SKU. A keyword is created per marketplace in that marketplace's language. The guide's example is a Spanish keyword for ES, with optional `nativeLanguageKeyword` and `nativeLanguageLocale` holding the advertiser's own wording.
- **Overrides.** `marketplaceConfigurations` overrides `state`, `name`, `startDateTime`, `endDateTime`, `optimizations` and `tags` per marketplace.
- **One bid strategy.** `bidStrategy` is set once for the campaign, and only bid values differ per marketplace (`bid.marketplaceSettings[]`).
- **Expanding.** Adding a marketplace requires its budget in the same call; otherwise the call fails with FIELD_VALUE_IS_NULL.
- **Auto.** A global auto campaign gets the four THEME targets per marketplace.
- **Scaling.** `autoScaleGlobalCampaign` is AUTO ("Auto scale global campaign to new marketplaces") or MANUAL.
- **Archive.** Archiving cascades.
- **Reports.** Only the `spCampaigns` report surfaces global campaigns.
- **Status IDs.** `status.marketplaceSettings[]` returns Amazon marketplace IDs, for example A1F83G8C2ARO7P, not country codes.
- **Mixing.** SP and global SP campaigns can be mixed in one account.

The supported marketplaces listed are AE, AU, BE, BR, CA, DE, EG, ES, FR, GB, IN, IT, JP, MX, NL, PL, SA, SE, SG, TR and US (list for human readers only). Release notes of 2025-07-29 add Global Store support (`globalStoreSetting`, `catalogSourceCountryCode`) and `/sp/global/targets/keywords/recommendations`. [official] *Global campaigns for Sponsored Products* and *Ads API release notes*, as above. Each child marketplace campaign has its own ID; v1's `MarketplaceCampaignConfigurations` describes `campaignId` as "marketplace campaign id (Ex: campaignId-US) associated to global campaign (Ex: campaignId-Global)". [official] merged OpenAPI.

**RULE: Amazon localizes for the caller.** The Localization API offers four calls:

- `POST /keywords/localize`: "Returns localized keywords within specified marketplaces or locales."
- `POST /products/localize`: maps a product from a source marketplace to target marketplaces. "The localization process succeeds for a given target marketplace if a product matching the source product can be found there and the advertiser is eligible to advertise it. Seller requests have an additional condition: the SKU of a localized product must match the SKU of the source product."
- `POST /targetingExpression/localize`
- `POST /currencies/localize`

All four take the account ID or a profile ID, with campaign edit or view permission. [official] Localization OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json, read 2026-11-09. For a seller, a product carries over to another marketplace only under the same SKU.

**GUIDANCE: Amazon's international structure.** The checklist says to "Launch a global Sponsored Products campaign for all the countries you want to advertise in". It warns that "Even if you run the same campaign in multiple countries, the results can be different". It tells the reader to define benchmarks per country and to "Reallocate budgets and bids across countries based on actual results". For keywords, it says the console shows translations of suggested keywords and offers a "Translate to [foreign language] and add" button. Its footnotes say this "may not be available in all languages" and that "The feature does not currently support all possible combinations of secondary languages and countries". Product targeting is offered as the tactic that needs no localization ("There's no need to localize anything"). The checklist also recommends Dynamic bids – down only "at least for your first campaign" in a new country, and a $10 minimum daily budget (figure for human readers only). [official] *Checklist for new international ad campaigns*, as above.

### L. Bulksheets and their relation to the API — RULE

**Columns and entities.** A bulksheet is a spreadsheet of entity rows. Each row carries Product, Entity and Operation (Create, Update or Archive). The SP entities are:

- Campaign
- Ad group
- Product ad
- Keyword
- Negative keyword
- Campaign negative keyword
- Product targeting
- Negative product targeting
- Bidding adjustment

The legacy bulksheet format was deprecated on 2023-09-28. [official] *Overview - About bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/overview-about-bulksheets, and *Get started with bulksheets for Sponsored Products*, both read 2026-11-09. The entity list matches the SP v3 resources one-to-one, which is why practitioners such as Capconvert advise designing "backward from the bulksheet entity model" [opinion].

**Downloads.** A custom download covers a range of at most 60 days (figure for human readers only). It has options to include:

- terminated campaigns
- zero-impression items
- placement data
- brand assets data
- SP input guidance and SP search term data
- a Portfolios tab

[official] *Get started with bulksheets: Part 1*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/get-started-with-bulksheets-part1, read 2026-11-09.

**Recent changes (dates for human readers only).** The bulksheet release notes record:

- 2026-06-08: an "Off-Amazon ad serving" column (US)
- 2026-07-06: SB Manual and Auto Collection in bulksheets
- 2026-08-31: export filtered by campaign
- 2026-09-09: export without performance data

[official] *Ads API release notes*, as above.

**Same rules, different door.** The bulksheet rules are the API's rules in a spreadsheet:

- Keyword text, match type, the product ad's SKU or ASIN, the product targeting expression, a campaign's targeting type, start date and (for bidding adjustments) placement cannot be updated; the work-around is to pause or archive and create a new entity. [official] *Understand which fields can be updated*, as above; *Overview - how to update campaigns with bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/campaign-update-overview, read 2026-11-09 ("Start Date and Targeting Type fields cannot be modified after the campaign is created").
- On create, fields marked with an asterisk "cannot be edited or updated after the campaign is created". The Sites column takes blank "for default (Amazon and Beyond)" or "Amazon Business". [official] *How to create Sponsored Products campaigns with bulksheets*, as above.
- Archiving a parent archives its children. [official] *How to update Sponsored Products campaigns with bulksheets*, as above.
- "'Archive' is not an option for portfolios", and a portfolio's Budget End Date "cannot be changed or updated once you set it". [official] *Bulksheets for portfolios*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-portfolios, read 2026-11-09.
- Keyword and product targeting cannot share an ad group. [official] *Get started with bulksheets for Sponsored Products*.

Amalyze gives a 32 MB and 500,000-row limit per upload [opinion, unverified on an Amazon page].

The seat found no Amazon page saying bulksheets and the API share one quota or one validation path. They use the same entity model and the same refusals.

### M. The Exports API: a snapshot of structure — RULE

Amazon offers an asynchronous snapshot of structure:

- **Requests:** POST `/campaigns/export`, `/adGroups/export`, `/targets/export` and `/ads/export`, with media types `application/vnd.{campaigns|adgroups|targets|ads}export.v1+json`.
- **Status:** GET `/exports/{exportId}`, from IN_PROGRESS to COMPLETED.
- **Download URL:** valid for one hour, and can be regenerated for 24 hours.
- **Snapshot:** the export reflects the moment of the request and keeps no history.
- **Limits and pace:** five in-progress jobs per endpoint by default; Amazon recommends exporting once or twice a day.
- **Coverage:** SP, SB and SD, with `adProductFilter` and a `stateFilter` of ENABLED, PAUSED or ARCHIVED.
- **Deprecation:** the September 2026 reporting notice says "The Exports API for campaign metadata is not affected". [official] *Deprecations*, as above.

Figures for human readers only. [official] *Exports overview*, https://advertising.amazon.com/API/docs/en-us/guides/exports/overview; *Get started with exports*, https://advertising.amazon.com/API/docs/en-us/guides/exports/get-started; *Exports FAQ*, https://advertising.amazon.com/API/docs/en-us/guides/exports/faq; all read 2026-11-09. A snapshot cannot say what the structure was last week. Comparing structure over time means keeping one's own snapshots, which is `method/change-measurement.md`'s.

### N. Amazon's guidance on grouping products and campaigns — GUIDANCE

**Group similar products.** Amazon's product strategy guide says:

> "Group similar products into the same campaign… Ad groups containing similar products saw 6% more units sold on average when advertising with Sponsored Products, compared to those with less similar products."

The footnote is "Amazon internal data, WW, 1/1/23-12/31/23" (figure for human readers only). The same guide reports a "67% uplift in ordered units, four weeks after being added" for excess inventory advertised with product labels. [official] *Product strategy*, https://advertising.amazon.com/library/guides/product-strategy, read 2026-11-09.

**The best-practices page.** Amazon's best-practices page adds:

- "Use separate campaigns or ad groups for each product group"
- "Only include ASINs from the same category in one campaign"
- "Group ASINs based on price range and conversions within the same category"
- "we recommend you add as many similar products to the ad group as you can"
- "Start creating portfolios to organize your campaigns by brand, category, season, or any way you choose"
- "Keyword or product targeting, and bids apply to all products within an ad group"

The "as many similar products" line is given "When creating an ad group with manual targeting". The page also reports that suggested products are "321 times more likely to generate ad-attributed sales when advertised, compared to products that are not suggested" (figure for human readers only), and notes that a campaign can be saved as a draft. [official] *Best practices for your Sponsored Products ads*, as above. "As many similar products as you can" in one ad group runs against the one-product-per-ad-group school (*What practitioners add*, section 3). Amazon's measured line compares ad groups of similar products with ad groups of less similar products; it does not compare a grouped ad group with a single-product one.

**Know your goal first.** The new-advertiser guide says "Establishing your goals up front will help you … decide how to structure your campaigns". [official] *New advertiser success guide*.

**Which products to advertise at all — RULE and GUIDANCE.** For a catalogue of hundreds of ASINs the first structural decision is which products get ads. Amazon's pages state the gates and offer three kinds of guidance.

- **RULE: only children of a variation family, and only offers that can be the Featured Offer.** "Where a product has multiple variations (parent-child relationship), only the variation (child product) is eligible for advertising." The account must have "product listings that are eligible to be the Featured Offer"; suppressed listings and virtual bundles cannot be advertised. [official] *Sponsored Products eligibility requirements*, https://advertising.amazon.com/help/GMJYF5GN8RNYB6HD (last modified 2026-10-20), read 2026-11-09. "In order to advertise, your product must be eligible to be the featured offer. We recommend choosing products that regularly display the featured offer"; "Your products need to be in-stock in order to be the featured offer and be eligible for inclusion in a Sponsored Products campaign. If a product you are advertising goes out of stock, it will be automatically paused within your campaign." The same guide recommends advertising products with a Prime badge, positive reviews and a reasonable price. [official] *How to improve your products for advertising*, https://advertising.amazon.com/library/guides/improve-your-products-for-advertising, read 2026-11-09. The v1 delivery reasons NOT_IN_BUYBOX, OUT_OF_STOCK and NO_PURCHASABLE_OFFER (section D) are these gates as the API reports them.
- **GUIDANCE: Amazon's product labels.** Amazon's product strategy guide describes labels on the campaign creation page: grey "suggested" labels for "products that are most likely to generate impressions and clicks when advertised", and green labels giving the reason: "New product", "Brand building", "Benchmarking" (a product whose "sales trend or conversion rate is low compared to similar products in the same category"), "Forecasted demand" and "Trending". It also suggests a campaign for products with upcoming deals and for products with excess inventory (found in "FBA Inventory" by "estimated excess units"), and advertising in additional countries. Its figures (Amazon internal data, worldwide, 2023; for human readers only): new products "36 times more clicks when advertised"; "Brand building" products "11x more repurchases when advertised, compared to the brand's other advertised products"; deal or coupon products "an average 65% increase in sales and 75% increase in units sold" when advertised; "Suggested products observed 321 times more sales when advertised, compared to products that are not suggested"; products in high-engagement weeks for their product type "32% more sales"; trending "22% more sales"; excess-inventory products "67% uplift in ordered units". [official] *Product strategy*, https://advertising.amazon.com/library/guides/product-strategy, read 2026-11-09. [seat] Each figure compares advertised products with a label against other products or periods; none is a controlled test of advertising one product instead of another.
- **RULE: the same "suggested" ranking is in the API.** `POST /product/metadata` (media type `application/vnd.productmetadatarequest.v1+json`) takes `sortBy` `SUGGESTED` ("Suggested products are those most likely to engage customers, and have a higher chance of generating clicks if advertised"; "Currently only support SP program type for sellers") or `CREATED_DATE`, `checkEligibility` with `adType` SP, SB or SD, `checkItemDetails`, and up to 300 items per page. Each product returns `asin`, `sku`, `availability` (IN_STOCK, IN_STOCK_SCARCE, OUT_OF_STOCK, PREORDER, LEADTIME, AVAILABLE_DATE), `bestSellerRank`, `eligibilityStatus` (ELIGIBLE or INELIGIBLE), `ineligibilityCodes`, `ineligibilityReasons`, `priceToPay`, `basisPrice` and `variationList` ("List of ASIN variations of the current item", up to 1,500). [official] Product selector OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json, read 2026-11-09. The Eligibility API (`POST /eligibility/product/list`) answers per product and ad type with an `overallStatus` and reasons. [official] Eligibility OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json, read 2026-11-09.
- **GUIDANCE: Amazon's four-quadrant ASIN matrix.** An Amazon Ads library guide classifies ASINs by life cycle (days since the listing's "Open Date") and sales against the catalogue's averages into "emerging" ("new and rising sales"), "flagship" ("Mainstay products with stable sales over a longer period"), "potential" ("Newer products with lower sales that have the potential to improve") and "longtail" ("Low-cost and hard-to-find products with stable, long-term demand"). It says: "Flagship and emerging ASINs are the main ones that help you increase impressions and sales, so we tend to carry out multiple sponsored ads campaigns on these products. Potential ASINs can rely on the flagship and emerging ASINs to drive higher exposure and sales … If you still have the resources to spare and have good longtail ASINs, you can also try using Sponsored Products for longtail ASINs." Its table pairs emerging with SP and SB, flagship with SP, SB and display ("Focus on category and product keywords"), potential with SB and SP ("Focus on branded keywords"), and longtail with SP ("Increase impressions through Sponsored Products"). [official] *Amazon Ads ASIN selection and promotion strategies*, https://advertising.amazon.com/library/guides/asin-matrix, read 2026-11-09.
- **GUIDANCE: standard and non-standard ASINs.** Another library guide separates "standard ASINs" (clear specifications, clear purchase intent, "Sales are concentrated on a limited number of keywords", "relatively high CPC") from non-standard ones, and suggests for standard ASINs either a heavier strategy ("approximately 80% of your budget to manual campaigns", about 20% to automatic) or a limited-budget one (figures for human readers only). [official] *Operations and advertising strategies for standard ASINs*, https://advertising.amazon.com/library/guides/standard-asin-strategy, read 2026-11-09.
- **GUIDANCE: variations in Sponsored Brands collections.** "For the best results, choose distinct products that complement each other, not variations of a single product or unrelated items (such as different sizes, colors, etc)." [official] *Migrate from Product collections to Sponsored Brands collections*, help GV7N6KZTH4HF4T2P, read 2026-11-09.

No Amazon page read says which child of a variation family to advertise, or how the ad and the page it opens present the family when one child is advertised (Open questions). The sibling `areas/launch.md` records, through the listing playbook's capture of Seller Central *Becoming the Featured Offer* (G201687550, not re-read by this seat), that "the Featured Offer is determined separately for each variation".

**Segment by funnel.** The Ad Intel partner article on Amazon's site describes the funnel split:

> "Top-of-funnel campaigns focus on brand awareness and product discovery, using higher volume, broader keywords, auto-targeting, or display campaigns… Middle-of-funnel campaigns narrow the focus… Lastly, bottom-of-funnel campaigns reach high-intent shoppers with exact match keywords and competitor ASIN targeting"

[opinion, on an Amazon page] Brent Zahradnik, AMZ Pathfinder, *Ad Intel*, as above.

### O. The surface is moving — RULE

These dates are for human readers only, from *Deprecations* and the release notes, read 2026-11-09:

- **SP campaign management:** v1 and v2 shut off 2023-06-30. No shutoff of v3 SP campaign management is announced, and v1 `/adsApi/v1` is said to "eventually fully replace" it.
- **SB:** v2/v3 SB campaign management shut off 2024-01-31 for most calls; the v3 → v4 migration of remaining campaigns had deadlines of 2025-10-30 (zero-impression campaigns created before October 2022) and 2025-12-31 (active ones), per the release note of 2025-10-14, which revised the 2025-04-17 schedule. Product Collection ads: creation mapped to Manual Collection from August 2026, API create requests rejected after January 2027 (*Deprecations*, the API migration guide's "Final shutoff"), and existing Product Collection ads no longer supported from February 2027, with eligible 3-ASIN ads moved automatically to manual collections (release note of 2026-09-18; help GV7N6KZTH4HF4T2P) (section B). Legacy (v3) SB campaigns: automatic migration to v4 announced from 2026-01-01 in the partner migration guide (section B). Negative SB placement adjustments are not accepted from 2026-06-15. SB top-of-search and rest-of-search adjustments are allowed up to 900% (2025-06-19). Amazon Business-only SB campaigns through `siteRestrictions` arrived 2025-06-12.
- **Portfolios:** v2 shut off 2025-03-01.
- **Diagnostics:** the Campaign Diagnostics API shut off 2025-12-01.
- **Stream:** Amazon Marketing Stream campaign datasets mirroring the v1 model became generally available 2025-12-01.
- **Reporting:** reporting v3, Stream v1 and SA v2 reporting shut off hard on 2027-06-30. Stream v2 and Reporting v1 became generally available 2026-09-30; the Exports API is not affected.
- **Accounts:** the six legacy account endpoints (`/adsAccounts*`, `/dsp/advertisers*`) are deprecated from July 2026, answer with `Warning: 299` headers, are closed to new integrations (existing callers only through an allowlist) and return 404 from July 2027; the replacement for listing is `POST /adsApi/v1/query/advertiserAccounts` (section A).

A seller's tree may hold entities created through the console, bulksheets, SP v3, SB v4 or v1, and by third-party tools. [seat] The pages read do not say in words whether every entity created through one generation is returned by the other's list or query call; the v1 overview presents v1 as a replacement over the same campaigns, which suggests they are, but this is not verified (Open questions).

## What practitioners add

Every claim in this section is [opinion], attributed to the person or firm that made it. Most come from firms that sell PPC software or agency services, and several of those products are built around the structure their authors advise. No practitioner page read reports a controlled comparison of one structure against another on Amazon.

### 1. The common skeleton: auto plus manual, split by targeting kind

Nearly every practitioner read starts from auto plus manual. Where they differ is how far to split the manual side.

- **Perpetua Marketing Team (2021-03-02)** proposes this unit for each ASIN or ASIN set:
  - "1 automatic campaign with 1 automatic ad group"
  - "1 manual campaign with 3 ad groups for broad, exact match keywords, and ASIN targeting"
  - "1 manual campaign with 1 ad group for category targeting"

  It leaves phrase match out, calling it "a bit too narrow for research and too broad for a super-refined performance campaign". It sets initial negatives to keep the lanes apart: the broad ad group's targets go into the auto ad group as negative phrase, the ASIN ad group's targets go into auto as negative ASINs, and the broad group's own targets are negated as negative exact in broad. Its graduation thresholds are "IF orders > 1" from auto to broad, and "IF orders > 2" after X clicks from broad to exact and from auto to ASIN, with X "between 10 and 20 is a good rule of thumb". Perpetua, https://perpetua.io/blog-amazon-ppc-ad-strategy/, read 2026-11-09. The thresholds are Perpetua's, recorded here as claims. The harvesting itself is `areas/search-terms-and-negatives.md`'s.

- **Perpetua help, *Search Term Isolation* (2026-02-27)** describes a setting that "allows you to funnel spend towards Exact match keywords using ad-group Negative matches". It works like this:
  - "a Negative Exact match will be added to the Phrase ad group"
  - "a Negative Phrase match will be added to the Broad ad group"
  - a search term then matches only its own exact keyword

  The page describes turning it on in Advanced Settings and does not state a default. https://help.perpetua.io/en/articles/4172431-search-term-isolation, read 2026-11-09.

- **Vince Montero (Helium 10, 2021-05-12, modified 2022-06-10)** gives four SP campaigns as a minimum:
  - "An Auto campaign for search term research purposes"
  - "A Manual Research campaign to bolster keyword harvest (finding new keywords) with Broad match keywords"
  - "A Manual Performance campaign with Exact match keywords"
  - "A Manual Product Targeting campaign using ASIN targets and categories"

  He adds SB with Brand Registry, and says "Sponsored Display product targeting campaigns are another way to ensure full coverage of all the Amazon placements available to sellers". He prefers "separate campaigns rather than separate ad groups because budget control is housed on the campaign level". He ties the structure to three lifecycle stages:
  - **Launch:** optimizes for impressions, with an ACoS goal after about 2–4 weeks.
  - **Scale:** uploaded campaigns default to "Target ACos" at 30%.
  - **Liquidate:** "focused solely on optimizing towards conversions".

  https://www.helium10.com/blog/helium10-life-cycle-template-strategy/, read 2026-11-09. This is the "research–performance" pattern named in the brief. In Montero's version harvesting is a movement of winning terms into the Performance campaign during Scale.

- **Helium 10 Adtomic (knowledge base, not read).** Search results summarized the Adtomic "SP Super Wizard" Standard as creating five campaigns:
  - "[YourPrefix]-SP-Auto"
  - "-SP-Keyword-Brand"
  - "-SP-Keyword-Competitor"
  - "-SP-Keyword-Category"
  - "-SP-PAT"

  The page itself returned 403 to this seat (Unreachable), so the list is recorded as a search summary, not a reading. It is the intent split (brand, competitor, category) built into a tool.

- **Seller Labs knowledge base (last updated 2026-05-13; no author)** recommends, for each ASIN or tight product family:
  1. an auto campaign for discovery
  2. a manual broad/phrase campaign for testing
  3. a manual exact campaign for scaling winners
  4. optionally, a product targeting campaign

  When scaling, it adds splits for branded vs non-branded, seasonal vs evergreen, high vs low margin, and launch vs mature. It gives signs of each failure:
  - **Too many:** "5–10+ campaigns per ASIN without a clear strategic reason", "Duplicated keywords across campaigns", "Many campaigns spending $2–$5 daily".
  - **Too few:** "One single campaign controlling all keywords", "Auto and manual targeting mixed together", "No separation between branded and non-branded traffic".

  Its FAQ says "3–5 campaigns per ASIN is scalable and manageable", and to separate match types into different campaigns "Only if you need budget-level control". It also claims "Internal bidding wars increase CPC" and that "One search term should have one strategic 'home'" [opinion; no Amazon source given]. https://www.sellerlabs.com/knowledge-base/campaign-structure-diagnostics-too-many-vs-too-few-campaigns/, read 2026-11-09. These counts are Seller Labs' and are thresholds, so they enter no skill as a rule.

- **Shazib Haseen (Ad Badger, 2019-11-18)** says:
  - for a single-ASIN account, use an automatic and a manual campaign, with the manual split by keyword, product and category targeting
  - "segment each of your campaigns by targeting type and then segment each ad group by product"
  - three separate campaigns instead of three ad groups "if you want more control over their ad placement settings"
  - portfolios are for large accounts (he names sellers with 5,000+ products)

  https://www.adbadger.com/blog/amazon-ppc-education/amazon-ppc-campaign-structure/, read 2026-11-09.

- **Capconvert ("Cortex", reviewed by Jacque, updated 2026-05-30)** advises "one auto plus one manual campaign per parent ASIN", each campaign built around "a single, tightly related product theme":
  - run auto for 7 to 14 days
  - "move converting search terms into the manual exact campaign"
  - negate the promoted terms in auto
  - add a manual broad or phrase campaign around proven roots
  - use single keyword ad groups selectively
  - give child ASINs their own ad groups

  It says to choose one segmentation axis (brand, category or product line, season or promotion, or goal such as launch, defend, harvest) and hold to it, matching "how you allocate budget". https://www.capconvert.com/learn/blog/amazon-ads-account-structure, read 2026-11-09. The page credits an author named "Cortex"; the seat cannot tell whether that is a person.

**Where they disagree on the skeleton:**

- **Phrase match.** Perpetua drops it. Seller Labs pairs it with broad. Capconvert uses broad or phrase. Amazon's checklist says to use all three match types.
- **Campaigns or ad groups.** Perpetua puts broad, exact and ASIN in one campaign as three ad groups. Montero and Seller Labs give each its own campaign. Section C's rule decides what that choice costs: separate campaigns get separate budgets, bid strategies and placement adjustments, while ad groups in one campaign share them.

### 2. Single keyword ad groups and single keyword campaigns (SKAG / SKC)

**For:**

- **Scale Insights (help centre, *Part 3: Build SKC campaigns for performers*)** builds a "Single Keyword Campaign" for each proven search term not yet in an exact SKC:
  - one keyword per ad group, exact match
  - Dynamic bids – down
  - an initial bid of 110% of the term's CPC
  - optionally created paused for review
  - selection by the report filters "Check Exact = Unique" and "SKC Yet? = Unique"
  - naming "SP_ASIN_ProductName_SKC_Exact_KT_{Keyword}", where "The Ad Group Name should match the Campaign Name"

  https://help.scaleinsights.com/en/knowledge-base/part-3-build-skc-campaigns-for-performers, read 2026-11-09.

- **Quartile (blog, 2024-05-15, no named author)** pairs one ASIN with one keyword in one match type per campaign. It tracks performance hourly and contrasts "one campaign with 100 keywords covering two products" with 200 campaigns. Its claims ("100% certainty on which keywords perform well") are marketing claims. Its one figure, 30% higher ROAS, is about importing campaigns into Quartile, not about SKCs. https://www.quartile.com/blog/achieving-adaptability-and-efficiency-with-single-keyword-campaigns, read 2026-11-09.

- **Reilly McDonnell (JumpFly, 2022-09-28)** gives the mechanism: placement bid adjustments are campaign-level, so a single keyword campaign lets a seller favour the placement where that keyword performs. He also names brand defence and lower-cost category visibility.

**Against:**

- **McDonnell, in the same post:**
  - "the optimization process does take much longer than optimizing one campaign"
  - "there will be much less search volume to examine the data"
  - "It can be challenging to make decisions with only a few clicks"
  - his advice: "start with a small number of single keyword campaigns and build from there"

  https://www.jumpfly.com/blog/single-keyword-ad-groups-and-campaigns-on-amazon/, read 2026-11-09.

- **Capconvert** uses SKAGs "selectively" for high-value terms, because applying them everywhere inflates campaign count.

- **Seller Labs** names many small campaigns ($2–$5 a day) as a sign of over-fragmentation.

- Search results surfaced vendor posts arguing that fragmentation starves Amazon's own bidding of data. They were not read, so no claim from them is recorded.

**Somewhere between: Mina Elias (Helium 10 blog, 2020-08-15, modified 2022-12-20).**

- He advises "only create one ad group per campaign".
- He says "a good number of keywords to have in a campaign is up to 10 keywords" and that "all keywords should have similar search volume".
- His reason, which he calls "keyword bullying", is that high-volume keywords take most of the budget.
- He adds that "Amazon distributes the budget at their own discretion".

https://www.helium10.com/blog/amazon-ppc-campaign-structure/, read 2026-11-09.

The argument is about where the trade-off sits, not about Amazon's rules. Section C gives the mechanism both sides use: a campaign's budget, bid strategy and placement adjustments are shared by everything in it. Section 1 of *Published research* gives the cost the "against" side names: sparse per-keyword data.

### 3. One product per ad group

**For:**

- **Shazib Haseen (Ad Badger, 2019)** calls single-product ad groups "still a winning strategy" for catalogues of 400,000+ SKUs. He notes "there's a 20,000 ad group limit per campaign", and says products at different price points or competing for different terms get "its own ad group or campaign".
- **Capconvert** gives child ASINs separate ad groups.
- A search summary of other vendor posts gives two further reasons for keeping ASINs apart. First, when variations share an ad group, "Amazon could potentially show your 3 ft cable ad for a search term like '6ft iPhone cable'". Second, one ASIN going out of stock skews the whole group's data. Those posts were not read, so this is recorded as a search summary only.

**Against, or in tension:**

- Amazon's guidance, section N: "we recommend you add as many similar products to the ad group as you can", with the measured "6% more units sold on average" for ad groups of similar products [official].
- **Capconvert's** hierarchy has "a single, tightly related product theme" per ad group, which is not one product.

The structural fact behind the dispute is section C: products in an ad group share bids and targeting [official]. So a single-product ad group buys per-product bids at the price of more ad groups.

### 4. Splitting by intent: branded, competitor, category, discovery

**The Badger (Ad Badger, *How to Segment Branded Keywords*, 2019-08-28)** gives the reasons for a branded split:

- budget control, because "you can set unique budgets and control your spending for each one individually"
- "easier reporting for 'true non-branded performance'"

His method:

1. Add the brand as negative exact in product targeting campaigns.
2. Put the branded keywords in their own campaign.
3. Optionally, run a third campaign on competitor brands.
4. Keep the lanes apart: "None of your keywords should overlap between the campaigns".

His verdict is mixed. He calls it "more of a reporting strategy than a performance strategy" and concludes "in general a hardline separation of your keywords probably isn't worth it". The drawbacks he names are more campaigns, diluted search-term data and unclear brand boundaries. https://www.adbadger.com/blog/how-to-segment-branded-keywords-in-amazon-ads/, read 2026-11-09.

Others take the split for granted:

- Seller Labs counts "No separation between branded and non-branded traffic" as a failure.
- The Helium 10 Adtomic wizard (search summary only) builds Brand, Competitor and Category campaigns by default.
- The Ad Intel partner article on Amazon's site builds the funnel split (section N).
- Amazon's SB goal page frames "Grow brand impression share" against "Drive page visits" as a structure (section G) [official].

Whether defending one's own brand terms pays is `beyond/brand-defense-and-competition.md`'s. The research there (Simonov, Nosko and Rao; Blake, Nosko and Tadelis) is noted in *Published research*.

### 5. Do a seller's own campaigns compete with each other?

This question decides whether overlap between campaigns matters. Amazon answers one case of it; the rest is open.

- **What Amazon states [official].** The help page on match types: "If you set multiple match types with different bids for the same keyword, then the match type with the highest bid will be used for any matching shopping query." [official] *Understand keyword match types*, https://advertising.amazon.com/help/GHTRFDZRJPW6764R (last modified 2026-07-29), read 2026-11-09. Amazon's targeting guide: "you won't be bidding against yourself by adding different match types on the same keyword." [official] *A guide to targeting with Sponsored Products*, https://advertising.amazon.com/library/guides/targeting-with-sponsored-products, read 2026-11-09. Both sentences cover one keyword text held in several match types. Neither says whether the rule holds when those match types sit in different ad groups or different campaigns, nor how Amazon chooses between the same keyword in the same match type in two campaigns, between a keyword and an auto or product target that both match a query, or between two different advertised products. Whether "the highest bid" is the bid before or after placement adjustments and dynamic bidding is not stated either. The owner of the match-type rule is `areas/keyword-and-product-targeting.md`.
- [seat] The rule explains the logic behind several practitioner structures: if the highest-bid match type is the one used, a broad keyword bid above its own exact twin takes the query the exact keyword was built for, which is what Perpetua's initial negatives and its Search Term Isolation setting (section 1) are built to prevent.

Non-Amazon statements:

- **Seller Forums thread (about eight years old).** A seller wrote: "I know Amazon explicitly states that if you are bidding on the same keyword in two campaigns in the same account, you will not compete against yourself". The only reply was "In my experience, it does". Neither post is from Amazon staff, and the original statement has no link. https://sellercentral.amazon.com/seller-forums/discussions/t/bbf265413c73f5100c256da33acf7438, read 2026-11-09.
- **Seller Forums thread (about five years old).** A non-staff reply warns against "pushing the bid rate up upon yourself (your ads completing against each other)". It advises against the same keywords in two campaigns. https://sellercentral.amazon.com/seller-forums/discussions/t/31a06264fe517de180891126092b5e60, read 2026-11-09.
- **Seller Labs** lists "Duplicated keywords across campaigns" as a symptom. Perpetua's negatives and Search Term Isolation, and The Badger's "None of your keywords should overlap", are all built to stop overlap.
- **The Badger (Ad Badger, *Keyword Cannibalization in Amazon PPC*, 2024-09-12)** writes: "Whenever two of your products are shown in Sponsored Product placements for a particular SERP, you will not be bidding against yourself. However, because of the stock Amazon gives to proven products, your CPC for each product may be different." No Amazon source is given. https://adbadger.com/blog/keyword-cannibalization-and-placement-in-amazon-ppc/, read 2026-11-09. [opinion]

The other Amazon statement near this is about portfolios: they "do not compete against each other" [official], which concerns portfolios, not campaigns or ad groups. How the auction treats one advertiser's several eligible ads beyond the match-type case is listed in Open questions.

### 6. Naming conventions

- **The Badger (Ad Badger, *Amazon Campaign Naming Convention: 3-Level Structure Guide*, 2024-05-16)** builds names in three levels:
  1. "Searchability and Ability To Scan": product name, SKU or ASIN, and the ad type
  2. "Targeting Types"
  3. "Integrate Business Objectives": ACOS, ranking, impression share, bid adjustment

  The template is "Product name ASIN | Ad Type | Targeting | Strategy Objective | Bid Adjustment", for example "Red Sock B0XXXXXXXX | SP | Keywords Exact | Ranking | TOS +50". It uses the abbreviations "ASP" (auto SP), "MSP" (manual SP), "SB" and "KW" to stay under the length limit. https://www.adbadger.com/blog/amazon-campaign-name-guide/, read 2026-11-09.
- **Capconvert:** "SP | Auto | Brand | Category | MatchType | Goal".
- **Scale Insights:** "SP_ASIN_ProductName_SKC_Exact_KT_{Keyword}", with the ad group named as the campaign.
- **Helium 10 Adtomic** (search summary): "[YourPrefix]-SP-Auto" and similar.

The conventions share one idea: the name carries the ad product, the product, the targeting kind or match type, and the purpose. Amazon's only rules on names are length, allowed characters and uniqueness within a campaign (section J). The pipe the conventions use is an allowed character on Amazon's list.

### 7. Portfolios

- **Shazib Haseen (Ad Badger):** use portfolios for large accounts, for example a cat portfolio holding cat food, cat toy and cat tower campaigns.
- **Capconvert:**
  - "a portfolio is the only mechanism Amazon gives you to cap total monthly spend"; section H casts doubt on "only"
  - Amazon "does not publish a hard maximum number of portfolios per account"
  - nested manager accounts arrived 2024-04-15
- **Brent Zahradnik (Ad Intel, on Amazon's site):** "Start with setting your daily account-level budget, then portfolio-level, and finally campaign-level". The seat found no Amazon help page describing an account-level daily budget setting for sponsored ads (Open questions).

### 8. Placement isolation: "top of search" campaigns beside product-page campaigns

**The mechanism Amazon documents [official].** Placement adjustments are a campaign setting (section C). Amazon's help page states how they apply: "Enter a percentage amount to increase your bid when your ad is eligible to compete for one or all of these placements", namely top of search ("Up to the first 5 positions in the top row of the first page search results on desktop, and up to the first 4 positions on mobile"), rest of search, product pages and Amazon Business. "The specified increase works in addition to your selected bidding strategy (dynamic or fixed)." Its example: a $1 bid with a 50% top-of-search adjustment becomes $1.5 "When your ad is eligible to appear in the top of search", and "Dynamic bidding (up and down) can further increase the bid up to $3." [official] *Adjust Sponsored Products bids*, https://advertising.amazon.com/help/GYYZVM7LGSRYGWV5 (last modified 2026-09-28), read 2026-11-09. Since 2024-01-09 rest of search has its own adjustment: "advertisers can adjust their bid for rest of search by up to 900% same as the other two placements", for "all targeting types (auto and manual) and bidding strategies (fixed and dynamic bidding)". [official] *Improve your campaign performance on rest of search placements using Sponsored Products rest of search bid adjustment control*, https://advertising.amazon.com/resources/whats-new/improve-campaign-performance, read 2026-11-09. Figures for human readers only. So a keyword's effective bid per placement is its base bid times its campaign's adjustment for that placement (times the dynamic factor); placement isolation uses that arithmetic by holding the same keyword in two campaigns with different base bids and adjustments.

**For:**

- **Helium 10 Team (blog *Dynamic Bidding*, published 2019-01-25, a Prestozon-era article).** Under "Low Bid + Aggressive Adjustment": "consider starting a new campaign with your most important exact match keywords, setting the bid somewhat low, and then turning on Dynamic Up and Down as well as Top of Search Adjustment to 900%". Its example sets the bid at $0.20 against a $1.00 average CPC so that "Amazon could bid up to $3.60 for a Top of Search placement". On running it beside the existing exact campaign: "Because the bid for other placements won't be increased by as much, this keyword will primarily get impressions for Top of Search which allows you to run it in parallel with the standard Performance campaign in your Search Term Isolation structure without competing against it for the rest of the placements. You can think about the standard Performance campaign as the 'rest of search' performance campaign and this new campaign as the 'top of search' performance campaign." It adds: "don't do any bid management or automation on this campaign." https://www.helium10.com/blog/amazon-dynamic-bidding/, read 2026-11-09. [opinion] [seat] The arithmetic under Amazon's current help page gives $0.20 × 10 = $2.00 with a +900% adjustment and up to $4.00 with dynamic up and down; the article's $3.60 and "up to 1,800%" do not match that page. The article predates the rest-of-search adjustment.
- **Feedvisor (*Optimizing your Amazon ad placement*, no author or date shown on the page read).** "If your goal is to maximize exposure of your products by winning impressions on the top of search results placement on the first page, set a low bid for your keyword or ad group, and a high top of search adjustment. Doing so will make your ad more competitive for top of search opportunities, while limiting impressions on other placements, as your base bid is low." It pairs this with "the 'fixed bids' bidding strategy". https://feedvisor.com/resources/amazon-marketing-advertising-strategies/optimizing-your-amazon-ad-placement/, read 2026-11-09. [opinion] The seat searched for an Amazon page with the same sentence and found none.
- **Perpetua (*Maximizing the impact of top-of-search Amazon ad placements*, undated on the page read).** "Isolate keywords for targeting with top-of-search bid multipliers so you have maximum control of your expenditure—you can do this with Perpetua's Keyword Boost feature", and "Back your top-of-search campaigns with increased budget", because "Higher bids compounded with superior click-through rates mean that you'll use up the same budget in a much shorter space of time." https://perpetua.io/blog-maximizing-the-impact-of-top-of-search-amazon-ad-placements/, read 2026-11-09. [opinion]
- **The Badger (Ad Badger, *How to Combine "Adjust Bids by Placement" and Your Keyword Bid*, 2020-03-18).** "A single keyword campaign gives us the ability to customize placement settings for an individual keyword"; for a campaign whose rest-of-search placement performs worst, "the base bid would be lower than your target CPC to cover our low-performing Rest of Search placements. We then use bid modifiers to boost Top of Search and Product Pages bids." He warns that top-of-search figures in multi-keyword campaigns may be "tainted by branded keywords" ("If you have a lot of keywords in your campaign, it's possible that the only Top of Search placements you are getting are from branded keywords"), and that a single keyword campaign for every keyword is impractical ("don't. Just don't."). https://www.adbadger.com/blog/amazon-ppc-education/placement-bid-adjustment-with-keyword-bid-campaign-settings-amazon-ppc/, read 2026-11-09. [opinion] Its statements "Rest of Search doesn't have a bid modifier" and "Sellers cannot set negative adjustments" predate the 2024 rest-of-search control.
- **The Badger (Ad Badger, *How to Use Adjust Bids by Placement on Amazon PPC (2023 Update)*, published 2023-11-20, modified 2026-10-29).** Under "Should I Segment Campaigns Based on Placements?": "Mixing placement modifiers isn't a smart play because the three placements behave differently. You can have three campaigns, each targeting a specific placement." https://www.adbadger.com/blog/amazon-ppc-education/adjust-bids-by-placement-amazon-ppc/, read 2026-11-09. [opinion]

**Against, or limits:**

- **The same Ad Badger 2023 article** limits the low-base-bid version: "you'd think it'd be possible to set your keyword bid to the lowest-performing placement and then boost the top two. It wouldn't work. You might not even enter the auction if you were to set the keyword bid to the lowest — say, ten cents"; "Amazon doesn't quite play along with that idea. Even if you're bidding on a niche keyword, there's a minimum bid requirement to enter the auction." [opinion; no Amazon page read describes such an entry threshold beyond the published minimum bid in *Limits, constraints, and quotas*]
- **m19 (*Top of Search on Amazon: Why Bidding High Isn't Enough*, datePublished 2026-10-27 on the page read).** Under "Only One Exact Match Keyword Campaign for Top-of-Search Ads": "Even if you consider having a campaign structure with only one Exact match keyword per campaign to push those keywords to top, which would limit the impact of placement modifiers on other keywords, this approach is not recommended due to several drawbacks": "Each campaign must have a minimum budget", "the Top of Search placement often tends to be much more expensive than the Rest of Search placement", and "Managing numerous campaigns with such a structure becomes complicated". It also argues that top-of-search figures look best partly because high-performing keywords already carry high bids. https://www.m19.com/blog/stop-bidding-on-top-of-search-on-amazon, read 2026-11-09. [opinion] The page says of rest of search "It is not possible to set a bid modifier for this placement", which Amazon's 2024 launch contradicts.
- **Pacvue** ("Three Reasons Winning Top of Search Doesn't Matter") is cited in `areas/bids-and-placements.md`, through a search summary, for the view that a moderate base bid with a moderate multiplier tends to serve more often than a very low bid with a high multiplier. The page answered HTTP 403 to this seat as well, and the public archive copy could not be fetched from this environment (Unreachable). A search summary read 2026-11-09 adds that the post says a granular placement strategy works best for "the top 15-25% of keywords" by search volume. Both are search summaries, not readings.

[seat] Placement isolation puts the same keyword, usually in the same match type, in two campaigns. Amazon's documented tie-break covers only different match types of one keyword ("the match type with the highest bid will be used", section 5); no page read says which of two same-match-type copies enters an auction, or whether the comparison uses the base bid or the placement-adjusted bid. Helium 10's "without competing against it" is that article's claim, not an Amazon statement. A skill reading such a structure sees two targets with the same `keywordText` and `matchType` in campaigns whose `placementBidAdjustments` differ, and reads which one took a query from the search term report's `campaignId` and the placement report.

### 9. Which ASINs, and which child, get ads

- **m19 (*How to Select the Right ASINs for Amazon Advertising?*, datePublished 2026-10-08).** "You can't directly advertise a parent ASIN"; "If you choose a low-performing child ASIN just because it's part of a popular parent ASIN, you're setting yourself up for poor results … Analyze metrics like sales, conversions, and reviews for each variation. Then choose only the top-performing children to include in your campaigns." It reuses Amazon's four-quadrant matrix under its own names ("Rising Stars", "Flagship Products", "High-Potential ASINs", "Long-Tail Products") and adds margin, reviews and inventory as selection criteria. https://www.m19.com/blog/amazon-asins-selection, read 2026-11-09. [opinion]
- **Amita (Karooya, *Using Amazon Product Variations And PPC Together To Maximize Sales*, 2021-09-14).** "While creating an Ad Campaign, you can only create an ad for a child ASIN. When this ad appears on Amazon, it will display images and details of the selected ASIN. Once customers click on the Ad, they will reach to the product page of the Grouped listing and have that particular variation selected." She suggests one ad group per child with the other children's attribute words ("Red", "Yellow") as negatives, then "If you have enough data, you can run ads only for the most popular variation". https://www.karooya.com/blog/using-amazon-product-variations-and-ppc-together-to-maximize-sales/, read 2026-11-09. [opinion; the description of what the ad shows is hers, not Amazon's]
- **Chuck Kessler (Canopy Management, *Amazon Advertising Budgets: How to Allocate Spend Across Campaign Types in 2026*, 2026-01-13).** "Your top performers (the 20% of products driving 80% of revenue) deserve defensive budget allocation"; new products get "80-85% of that product's budget" in Sponsored Products for the first 30–60 days; the page says its figures reflect "patterns we see in our own data and client base" and "should not be read as official statements from Amazon". https://canopymanagement.com/amazon-advertising-budgets-how-to-allocate-spend-across-campaigns/, read 2026-11-09. [opinion; thresholds and shares are Canopy's]
- **Capconvert** (section 1) chooses one segmentation axis (brand, category or product line, season, or goal) and matches it to "how you allocate budget"; **Shazib Haseen (Ad Badger)** gives single-product ad groups to products "at different price points" (section 3). [opinion]
- **Scale Insights (*Amazon PPC for Variations*, undated)** says sellers "can create an ad campaign for each child ASIN separately" and also that "By grouping variations together under a parent ASIN, sellers can create a single ad campaign that promotes all variations"; the second sentence conflicts with Amazon's rule that only children are eligible, and the page names no mechanism. https://scaleinsights.com/learn/amazon-ppc-for-variations-ad-campaigns-for-multiple-product-options, read 2026-11-09. [opinion, low weight]

The tiering vocabulary practitioners use (hero, core, long-tail) appears on the pages read only as Amazon's own quadrant names and m19's restatement; no page read reports a measured comparison of tiered against untiered budget splits.

### 10. Measuring a restructure

Practitioners credit restructures with gains; the pages read give claims about what a restructure does to Amazon's systems, not measurements.

- **The Badger (Ad Badger, *You're Optimizing Too Much*, 2026-06-02, a write-up of a PPC Den episode with Clément Hynaux).** "every change you make resets Amazon's learning loop. When you adjust a bid, Amazon's system needs to recalibrate. When you pause a keyword, the data history for that keyword starts fragmenting." https://www.adbadger.com/blog/amazon-ppc-optimization-mistakes/, read 2026-11-09. [opinion] The claim is about every change, not restructures in particular, and the post gives no data.
- **George Meressa (Clear Ads, *Your Amazon Ad Structure Is Starving the Algorithm*, 2026-04-29).** "Any campaign generating fewer than 30 conversions in 30 days is in data starvation", which he calls "the threshold Amazon itself requires before activating rule-based ROAS bidding"; "Pausing campaigns and restarting them to fix performance typically makes the problem worse by triggering a learning reset and spiking CPCs", with "CPCs spike 15 to 30% during active hours after a campaign restart" from Clear Ads' audits; he argues for consolidating "by intent layer, not match type". https://clearadsagency.com/your-amazon-ad-structure-is-starving-the-algorithm-heres-the-fix/, read 2026-11-09. [opinion] Amazon's rule-based bidding guide gives a different threshold: "Your campaign must be running for at least 10 days prior to setting a rule and have a minimum of 10 conversions in the last 30 days" [official] *Sponsored Products Rule-based bidding overview*, https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview, read 2026-11-09.
- **Seller Forums (EU), *Split product ads up into different ad groups retrospectively*, about two years old.** A seller feared that new ad groups would be "like starting the product ads from scratch". A reply from another seller account (not Amazon staff) says: "the specific historical data in the current ad group won't transfer (e.g., historical reporting data can't be split up or transferred to new ad groups)", but "The sales and interactions your ads have already generated contribute to Amazon's understanding of which customers find your product relevant." https://sellercentral-europe.amazon.com/seller-forums/discussions/t/46150e60-9be2-42dc-b0ce-1981c873c720, read 2026-11-09. [opinion]

**What Amazon documents about per-campaign state [official].** No Amazon page read documents a learning state of a campaign, ad group or target for relevance or bidding, nor a reset of one when a target moves. What Amazon does document as tied to a campaign's own history:

- Rule-based bidding eligibility: at least 10 days running and at least 10 conversions in the last 30 days; "the ROAS guardrail is based on the previous 21 days"; the rule is switched off if "the return on ad spend (ROAS) of the campaign for the last 20 days drops to less than 30% of your ROAS over a 20-to-40-day period". *Sponsored Products Rule-based bidding overview*, as above. A target moved into a new campaign therefore sits in a campaign that is not eligible until it has its own 10 days and 10 conversions.
- Reports, budgets and placement figures are keyed by `campaignId`; an SB legacy migration creates a new campaign ID with the old one kept in a `legacyCampaignId` tag and "preventing unintended performance data carryover" (section B).

**What Amazon's published modelling says [research].** Xue, Liu, Du, Korlimarla and Men (arXiv:2304.09107, 2023) describe click and conversion models whose position de-biasing uses "history-based features on the batch level - that is - we calculate the historical views/clicks/CTR of each ad item on each batch"; the word "campaign" does not occur in the HTML full text read. The paper does not name the shop and says nothing about advertiser structure. https://arxiv.org/abs/2304.09107 and https://arxiv.org/html/2304.09107, read 2026-11-09. [seat] If features are kept per ad item, a restructure that keeps the same advertised ASIN and query would not by itself erase them; the paper does not say so, and it is not documented as Amazon's production system.

**The measurement problem [seat; method from published research].** Moving converting terms out of a broad or auto campaign into an isolated exact campaign changes which campaign receives which queries. A campaign-level before/after comparison then mixes two things: a composition change (the source campaign loses its best queries, the new campaign holds only them) and a rate change (CTR, CVR or CPC on the same query). This is the aggregation reversal described by Simpson (1951) and shown on admissions data by Bickel, Hammel and O'Connell (1975) (*Published research*). Typical signatures: the source campaign's ACOS rises and the new campaign's ACOS is low, while nothing changed for any query; or every campaign improves while the account does not. The comparison that separates them:

1. Hold the unit fixed at advertised ASIN × search term (× match type or placement where needed), across all campaigns. The Ads API's `spSearchTerm` report carries `searchTerm`, `campaignId`, `adGroupId`, `keywordId`, `matchType`, `keywordType` and `targeting`, but no advertised-ASIN column; the ASIN is joined through the ad group's product ads, which is exact only where an ad group advertises one ASIN. The report holds "only … impressions that resulted in at least one ad click". [official] *Search term reports*, as above.
2. Add the query's totals beyond ads where the seller is brand-registered: SP-API `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` gives, per ASIN and query and per `reportPeriod` WEEK, MONTH or QUARTER, `searchQueryVolume`, `searchQueryScore`, `totalQueryImpressionCount`, `asinImpressionCount`, `asinImpressionShare`, `asinClickCount`, `asinPurchaseCount`, `asinPurchaseShare`, `totalPurchaseCount` and related fields; the page lists `asins` as optional and `reportPeriod` as required, with week boundaries Sunday to Saturday. [official] *Analytics reports* (SP-API report type values), https://developer-docs.amazon/sp-api/docs/report-type-values-analytics, read 2026-11-09.
3. Split the account-level change into a mix part and a rate part with the log-mean Divisia index (Ang 2005), as `areas/diagnosis.md` sets out: over the ASIN × query cells, ΔV = Σ L(V₁, V₀) · ln(x₁/x₀) per factor, with no residual.
4. Read the same windows before and after, with the attribution lag and the time zone handled as `method/change-measurement.md` and `areas/diagnosis.md` describe.

The owner of change measurement is `method/change-measurement.md`; this section records why the default campaign-level read of a restructure is confounded by construction.

The seat looked for published research on how campaign or keyword granularity affects performance in sponsored search. It found none that studies Amazon campaign structure directly. The items below bear on the mechanisms structure arguments rely on. None is a position about Amazon structure.

1. **Sparse keyword data.** Rutz, Bucklin and Sonnier, "A Latent Instrumental Variables Approach to Modeling Keyword Conversion in Paid Search Advertising", *Journal of Marketing Research* 49(3), 2012, pp. 306–319. As summarized in search results, the abstract notes that keyword-level conversion data are often zero: "A problem occurs when the observed conversion rate (number of sales divided by number of clicks) for a given keyword is zero". It also notes that search engines withhold competitors' bids and report position only as a daily average. The author's PDF (https://faculty.washington.edu/orutz/docs/Keywords_JMR_2012.pdf) was fetched but could not be turned into text in this session (Unreachable). The abstract wording is from search snippets, not from reading the paper. [research]

2. **Aggregation bias.** Abhishek, Hosanagar and Fader, "Aggregation Bias in Sponsored Search Data: The Curse and the Cure", *Marketing Science* 34(1), 2015, pp. 59–77. Per the abstract as summarized in search results, models fit to daily aggregates "attenuate the impact of ad position on click-through rate", and search-engine revenue loss from that bias "can be as high as 11%". The INFORMS page returned 403 (Unreachable), so this is from search snippets of the abstract only. It is about data aggregation over time, not campaign grouping. [research]

3. **Generic-to-branded spillover.** Rutz and Bucklin, "From Generic to Branded: A Model of Spillover in Paid Search Advertising", *Journal of Marketing Research* 48(1), 2011, pp. 87–102. Per the abstract as summarized in search results, generic search ads raise later branded searches, and the reverse does not hold. The data were one lodging chain's paid search campaign. The author's PDF was fetched but not converted (Unreachable). This bears on judging a generic-keyword campaign only by its own attributed sales when a branded campaign sits beside it. Attribution itself is `beyond/metrics-and-attribution.md`'s. [research]

4. **Brand keywords.** Simonov, Nosko and Rao, "Competition and Crowd-Out for Brand Keywords in Sponsored Search", *Marketing Science* 37(2), 2018, pp. 200–215, Bing field experiments. Per the abstract (IDEAS/RePEc page, read 2026-11-09):
   - With no competitors bidding, a brand's own ad adds a small effect of about 1–4%.
   - Competitors in positions 2–4 take about 1–5% of the focal brand's clicks.
   - Where the brand does not advertise on its own term, competitors take 18–42% of clicks.
   - The authors conclude defensive brand advertising has a strongly positive return.

   Chris Nosko is listed with Amazon, Inc. https://ideas.repec.org/a/inm/ormksc/v37y2018i2p200-215.html. The setting is Bing, not Amazon's store. [research]

5. **Paid search effectiveness at eBay.** Blake, Nosko and Tadelis, "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment", *Econometrica* 83, 2015, pp. 155–174 (NBER w20171, 2014). Per the NBER abstract page, read 2026-11-09:
   - Returns from paid search are "a fraction of conventional non-experimental estimates".
   - Brand-keyword ads showed no measurable short-term benefit at eBay.
   - Non-brand ads worked for new and infrequent users.
   https://www.nber.org/papers/w20171. The setting is Google/Bing ads for eBay, not ads inside Amazon. [research]

6. **Amazon's own sponsored products modelling.** Xue, Liu, Du, Korlimarla and Men, "Practical Lessons on Optimizing Sponsored Products in eCommerce", arXiv:2304.09107, 2023-04-05. It covers position de-biasing, joint click and conversion learning and CTR calibration in a sponsored products ad system, evaluated on an online shop's traffic logs. https://arxiv.org/abs/2304.09107, read 2026-11-09. The abstract page does not name the company and says nothing about advertiser campaign structure. It is recorded because Rel.ai (blog, https://rel.ai/blog/how-amazons-ad-auction-works, read 2026-11-09) cites it, with arXiv:2307.16060 (not read), as describing Amazon's ad ranking: "Ad Rank = Bid × Relevance Score", relevance "computed per query, per auction". Rel.ai's article does not address how one advertiser's several ads for one query are handled. [research] for the paper; [opinion] for Rel.ai's reading of it. Re-read for the gap fill (HTML full text, 2026-11-09): its de-biasing features are "the historical views/clicks/CTR of each ad item on each batch", and the text never uses the word "campaign" (section 10 of *What practitioners add*). The heading's "Amazon's own" is the reading of Rel.ai and of the authors' affiliations; the paper does not name the shop.

7. **Aggregation reversal (Simpson's paradox).** Simpson, "The Interpretation of Interaction in Contingency Tables", *Journal of the Royal Statistical Society Series B* 13(2), 1951, pp. 238–241, shows "by an example that the vanishing of this second order interaction does not necessarily justify the mechanical procedure of forming the three component 2 × 2 tables". Bickel, Hammel and O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", *Science* 187(4175), 1975, pp. 398–404: "Examination of aggregate data on graduate admissions … shows a clear but misleading pattern of bias against female applicants. Examination of the disaggregated data reveals few decision-making units that show statistically significant departures"; the pattern came from "the tendency of women to apply to graduate departments that are more difficult to enter". Both from Crossref metadata and abstracts (https://doi.org/10.1111/j.2517-6161.1951.tb00088.x; https://doi.org/10.1126/science.187.4175.398), read 2026-11-09. *Transfer:* campaigns are the "departments" and queries the applicants; moving queries between campaigns changes each campaign's mix, so campaign-level rates can move in a direction no query moved. [research]

8. **Decomposing a change into mix and rate.** Ang, "The LMDI approach to decomposition analysis: a practical guide", *Energy Policy* 33(7), 2005, pp. 867–871 (Crossref metadata, https://doi.org/10.1016/j.enpol.2003.10.010, read 2026-11-09; the method as set out in `areas/diagnosis.md`). The log-mean Divisia index splits a change in a product of factors exactly into per-factor parts with no residual. *Transfer:* over ASIN × query cells, an account's change in sales or spend splits into a share-of-queries (mix) part and per-query rate parts (CTR, CVR, CPC). [research]

## Stable enough for a skill

These are facts that held across every page read and that Amazon states as rules of its system. A skill can carry them as knowledge. It still reads figures and current values at run time.

1. A profile is one advertiser account in one marketplace. Single-marketplace calls carry its ID in `Amazon-Advertising-API-Scope`; global calls carry the account ID in `Amazon-Ads-AccountId`. Sources: *Profiles*; *Global campaigns for Sponsored Products*; cx-amazon-ads `door.md`.
2. SP's hierarchy is campaign → ad group → product ads and targets. Negatives sit at campaign level and at ad-group level. An auto campaign serves with a product ad alone; a manual ad group needs at least one target. Source: *Sponsored Products campaign structure*.
3. Products in one ad group share its bids and targeting. Ad group names are unique within a campaign. Source: *Creating Sponsored Products ad groups*.
4. An SP ad group carries keyword targeting or product targeting, never both. An SB ad group carries one ad type and one targeting kind. Sources: *Get started with bulksheets for Sponsored Products*; *Campaign structure for Sponsored Brands*.
5. These live on the campaign: the budget, the bid strategy, the placement adjustments, the start and end dates, the portfolio, the site restriction, the off-Amazon setting and the tags. Neither SP v3 nor v1 SP has an ad-group budget. Sources: SP v3 OpenAPI; *Campaign* (v1).
6. Auto or manual is set at creation and cannot be updated (SP v3: "targetingType cannot be updated"; v1 `CampaignUpdate` has no `autoCreationSettings`; bulksheets: "You cannot update an auto campaign to be manual, and vice versa"). An auto campaign's targets are the four theme groups: close match, loose match, substitutes and complements. They can be paused and given bids, but not archived on their own. Sources: SP v3 OpenAPI; merged OpenAPI; *Global campaigns for Sponsored Products*; *Understand which fields can be updated*; *How to create Sponsored Products campaigns with bulksheets*.
7. ARCHIVED is terminal. It is reached through delete (or a bulksheet Archive row) and cannot be re-enabled or copied. Pausing is reversible. Archiving a parent archives its children in global campaigns and in SP bulksheets; children of an archived parent can no longer be updated or created. Portfolios cannot be archived in bulksheets. Sources: merged OpenAPI (`State`); *Global campaigns for Sponsored Products*; *How to update Sponsored Products campaigns with bulksheets*; *Bulksheets for portfolios*; SP v3 `EntityStateErrorReason`; Seller Forums staff reply.
8. Several things cannot change after creation: keyword text and match type, a product ad's product, a product target's ASIN, a campaign's targeting type and its site restriction, and an SB goal-based campaign's goal, cost type and smart default. Changing one means creating anew. Sources: SP v3 OpenAPI; merged OpenAPI; *Understand which fields can be updated*; *Getting started with campaigns* (SB).
9. A campaign belongs to at most one portfolio. A portfolio's cap is a DATE_RANGE, MONTHLY_RECURRING or NO_CAP budget. Unspent budget sharing exists and is on by default for portfolios created after a 2025 date. A portfolio's state and cap appear in its campaigns' delivery reasons. Sources: *Get started with Portfolios*; Portfolios OpenAPI; *Sharing leftover budget*; merged OpenAPI.
10. A write that crosses an entity quota is refused with QUOTA_EXCEEDED or NON_ARCHIVED_QUOTA_EXCEEDED and a scope of ACCOUNT or PARENT_ENTITY. Some quotas count non-archived entities only. Source: SP v3 OpenAPI.
11. Ads API v1 creates, updates and deletes answer 207 with per-index success, error and partial success. A batch may half-succeed. Source: merged OpenAPI.
12. A global SP campaign is one campaign whose children each hold a subset of its marketplaces. Ads and targets each carry one marketplace; keywords are written in that marketplace's language. The bid strategy is shared, and bids, budgets and some fields can differ per marketplace. Source: *Global campaigns for Sponsored Products*.
13. For a seller, a product localizes to another marketplace only under the same SKU. Source: Localization OpenAPI.
14. SB goal-based campaigns have two goals, drive page visits (the default, with CPC when neither goal nor cost type is sent) and grow brand impression share (vCPM only). SD expresses its objective as `bidOptimization` with a tactic. Sources: *Getting started with campaigns* (SB); *Sponsored Brands goal-based campaigns*; *Amazon Ads API for Sponsored Display overview*.
15. Amazon's own guidance:
    - start new advertisers on auto, then build manual campaigns from its best performers
    - group similar products
    - keep one category per campaign
    - organize portfolios by brand, category or season

    It reports +6% units for ad groups of similar products against ad groups of less similar products (Amazon internal data, 2023). Sources: *Sponsored Products campaign structure*; *Product strategy*; *Best practices for your Sponsored Products ads*.
16. An export is a snapshot at request time with no history. Source: *Exports overview*.
17. A Sponsored Brands version 4 ("multi-ad group") campaign holds several ad groups, each with at least one ad and only one ad type, and one targeting kind. The SB ad group carries no bid; budget, goal, cost type and placement bidding sit on the campaign, and bids on keywords and targets. Ads are moderated one by one, and a campaign keeps serving while one ad is active. `isMultiAdGroupsEnabled` marks the model on each campaign. Sources: *Campaign structure for Sponsored Brands*; *Getting started with campaigns* (SB); *Migrating to version 4 Sponsored Brands campaigns*; SB v4 OpenAPI.
18. Legacy SB campaigns have read-only ad groups, ads without `adId`, and no ad-group creation; v3 reporting previews exclude campaigns with `isMultiAdGroupsEnabled=False`. Migrating a legacy campaign creates a new campaign ID, archives the old one, keeps the old ID in the `legacyCampaignId` tag, resets the start date and appends a `migrated` suffix, without carrying performance data over. Sources: *Migrating to version 4 Sponsored Brands campaigns*; *Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API*; SB v4 OpenAPI; *Sponsored ads reporting overview (version 3)*.
19. Only child variations, eligible to be the Featured Offer and in stock, can be advertised in SP; an advertised product that goes out of stock is paused within its campaign. `POST /product/metadata` with `sortBy` `SUGGESTED` ranks a seller's SP products by Amazon's "suggested" model and returns availability, eligibility, best seller rank and variation lists. Sources: *Sponsored Products eligibility requirements*; *How to improve your products for advertising*; Product selector OpenAPI.
20. A placement adjustment raises a bid only when the ad is eligible for that placement, adds to the bidding strategy, and is a campaign setting; top of search, rest of search and product pages each take an adjustment. Sources: *Adjust Sponsored Products bids*; *Improve your campaign performance on rest of search placements…*; SP v3 OpenAPI.
21. For one keyword set in several match types with different bids, "the match type with the highest bid will be used for any matching shopping query". Amazon states nothing on the pages read about two copies of the same keyword and match type in different campaigns. Sources: *Understand keyword match types*; *A guide to targeting with Sponsored Products*.
22. Rule-based bidding eligibility and its ROAS guardrail are computed from a campaign's own history (10 days running, 10 conversions in 30 days, a 21-day guardrail basis). Source: *Sponsored Products Rule-based bidding overview*.
23. The SP search term report has no advertised-ASIN column and holds only impressions with at least one click; Search Query Performance gives per-ASIN, per-query totals by week, month or quarter for brand-registered sellers. Sources: *Search term reports*; *Analytics reports* (SP-API).
24. Product Collection ads: API creates end after January 2027; existing ads are unsupported from February 2027, with eligible 3-ASIN ads moved automatically to manual collections. Sources: *Deprecations*; *Product Collection Migration Guide*; release note of 2026-09-18; help GV7N6KZTH4HF4T2P.

## What cx must read at run time

Every call below goes through the door: `cx raw amazon-ads --origin <na|eu|fe> --method <M> --path <P> [--header ...] [--body ...]`. The door's own rule matters here. Many structure reads are a `POST` list, and "the gate reads a `POST` as a change, so one whose reply was lost reads `sent, outcome unknown`" (cx-amazon-ads `SKILL.md`). Paths and media types below are from Amazon's published references as read on 2026-11-09. A skill checks them against the reference it reads on the day.

**Who and where:**

- `GET /v2/profiles` on each origin the seller authorized. This gives the profiles and, for each, the marketplace, currency, timezone and seller/vendor type.
- `POST /adsApi/v1/query/advertiserAccounts`, to learn whether a global account exists, its ID, and which profiles it maps to. Not `/adsAccounts*`: those endpoints are deprecated, answer with `Warning: 299`, are closed to new integrations and return 404 from July 2027 (section A).

**The tree, per profile (or per global account):**

- Portfolios: `POST /portfolios/list` (`application/vnd.spPortfolio.v3+json`). This returns caps, policy, dates, `inBudget`, serving status and the unspent-sharing state.
- Campaigns: `POST /adsApi/v1/query/campaigns` with `adProductFilter` once per ad product, paged by `nextToken`. Alternatively `POST /sp/campaigns/list` with `includeExtendedDataFields` for serving status, and `POST /sb/v4/campaigns/list` (`application/vnd.sbcampaignresource.v4+json`) for SB.
- From each campaign: targeting type or `autoCreateTargets`, state, delivery status and reasons, budget, bid strategy and placement adjustments, dates, `portfolioId`, `siteRestrictions`, `tags`, `autoManageCampaign`, goal settings, `marketplaceScope`, and for global campaigns `marketplaces` and `marketplaceConfigurations`.
- Below the campaign: ad groups, ads and targets through the v1 query calls or their SP v3 list calls (`/sp/adGroups/list`, `/sp/productAds/list`, `/sp/keywords/list`, `/sp/targets/list`).
- Negatives: `/sp/negativeKeywords/list`, `/sp/campaignNegativeKeywords/list`, `/sp/negativeTargets/list` and `/sp/campaignNegativeTargets/list`, or v1 targets with `negative: true`. From these the skill sees which campaigns are fenced off from which.
- Target promotion groups: `POST /sp/targetPromotionGroups/list` and `.../targets/list`. These are Amazon's recorded auto → manual links, where the seller or a tool made them.
- For a large account: the Exports API (`POST /campaigns/export` and its siblings, then `GET /exports/{exportId}`). This gives one snapshot instead of many paged lists. Its download link expires.
- Sponsored Brands model per campaign: `isMultiAdGroupsEnabled` on `POST /sb/v4/campaigns/list`; ad groups through `POST /sb/v4/adGroups/list` (`application/vnd.sbadgroupresource.v4+json`); ads through `POST /sb/v4/ads/list` (`application/vnd.sbadresource.v4+json`), which "returns ads created using both version 3 and version 4" (legacy ads without `adId` or `name`); keywords through the SB keyword calls (`/sb/keywords`). Migrated campaigns carry the old ID in the `legacyCampaignId` tag; `POST /sb/v4/legacyCampaigns/overallMigrationResults` lists an advertiser's migration results (media type `application/vnd.SponsoredBrands.SponsoredBrandsMigrationApi.v4+json`). Product Collection ads still running: `POST /sb/v4/migrations/list`, which returns recommended `MANUAL_COLLECTION` and `AUTO_COLLECTION` replacements and a `MigrationStatus` of ACCEPTED, ELIGIBLE, MIGRATED or MIGRATION_FAILED.

**Which products can and could be advertised:**

- `POST /product/metadata` (`application/vnd.productmetadatarequest.v1+json`) with `checkEligibility`, `adType` and, for SP sellers, `sortBy` `SUGGESTED`: per product `availability`, `eligibilityStatus`, `ineligibilityCodes`, `bestSellerRank`, `priceToPay`, `basisPrice` and `variationList`. The header and permission the model names are read from the Product selector OpenAPI on the day.
- `POST /eligibility/product/list`: per product and ad type, `overallStatus` and reasons.
- The advertised products already in campaigns: `/sp/productAds/list` (or v1 ads with `productIdType` ASIN or SKU), against the catalogue.
- Outside the Ads API, by their own doors: the Featured Offer percentage, sessions and conversion by child ASIN from `cx-amazon-sp-api` (sales and traffic report); price and rank history per child from `cx-keepa`; the variation family from `cx-amazon-sp-api` listings or catalog reads.

**For a restructure's before/after (method owned by `method/change-measurement.md`):**

- `spSearchTerm` (Ads API reporting) across every campaign of the profile for the same windows, with `searchTerm`, `campaignId`, `adGroupId`, `keywordId`, `matchType`, `keywordType`, `targeting` and the cost and sales columns; the advertised ASIN joined through each ad group's product ads.
- The campaign report grouped by placement for top-of-search isolation structures (the reporting owner is `method/reporting.md`).
- `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` through `cx-amazon-sp-api`, per ASIN and `reportPeriod` WEEK, MONTH or QUARTER, for brand-registered sellers.
- Change history for when each structural write happened (`method/change-measurement.md`).
- `POST /sp/rules/campaignOptimization/eligibility` (path as `areas/bids-and-placements.md` records it from Amazon's rule-based bidding API guide) for whether a newly created campaign is eligible for rule-based bidding.

**Live figures, never from this file:**

- Bid and budget minimums and maximums for the marketplace: *Limits, constraints, and quotas*, a public documentation page, or the refusal a write returns.
- Name lengths and allowed characters: the same page, or the refusal.
- Entity count caps: the Amazon help page *Sponsored ads campaign limits* gives a table, but Amazon also says it raises an account's limits as the account approaches them, so the account's own ceiling is read from the refusal (QUOTA_EXCEEDED or NON_ARCHIVED_QUOTA_EXCEEDED, with its scope).
- Portfolio budget usage: `POST /portfolios/budget/usage`. Campaign budget usage: `/sp/campaigns/budget/usage`.
- Which marketplaces global campaigns support, and whether goal-based SB campaigns exist in the marketplace. Read these from the reply or the error (for example GOAL_BASED_CAMPAIGNS_DISABLED).

**Structure as the seller has encoded it:** campaign and ad group names and tags. These are the seller's (or their tool's) words for purpose, product and stage. Amazon gives them no meaning.

**Before a change that cannot be undone:** the entity's current state and its children. An archive is terminal and freezes the subtree (section D). A change to a fixed field is a create plus an archive (section D).

## Pages read

All read 2026-11-09. API documentation pages were read through their public markdown copies at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`; the URL given is the canonical page.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| cx-amazon-ads skill | (plugin file) `skills/amazon-ads/SKILL.md` | ComChatX | 2026-11-09 | the door, origins, refused headers, the gate's reading of a POST |
| cx-amazon-ads door reference | (plugin file) `skills/amazon-ads/references/door.md` | ComChatX | 2026-11-09 | headers, profile fields, list paths |
| API docs contracts list | https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json | official | 2026-11-09 | index of published OpenAPI files |
| Campaign management in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview | official | 2026-11-09 | v1 scope; one ad product per call and TPS per ad product "at launch" |
| Campaign management entities | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/overview | official | 2026-11-09 | five entities |
| Campaign (v1 entity) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/campaign | official | 2026-11-09 | campaign fields per ad product |
| Ad group (v1 entity) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad-group | official | 2026-11-09 | ad group fields; read-only scope |
| Ad (v1 entity) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad | official | 2026-11-09 | ad types; advertised product |
| Target (v1 entity) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/target | official | 2026-11-09 | target types; target level; negatives |
| Ad association (v1 entity) | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad-association | official | 2026-11-09 | DSP only |
| Ads API merged OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official | 2026-11-09 | v1 enums: State, Goal, KPI, BidStrategy, Placement, DeliveryReason; batch sizes |
| Amazon Ads API v1 overview | https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview | official | 2026-11-09 | the unified API's framing; "eventually fully replace" |
| Getting started with Amazon Ads API v1 | https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/getting-started | official | 2026-11-09 | account, profile and account ID words |
| Sponsored Products overview | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/overview | official | 2026-11-09 | SP API orientation |
| Sponsored Products campaign structure | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/get-started/campaign-structure | official | 2026-11-09 | hierarchy; auto-first tip; negatives at two levels |
| Sponsored Products campaigns | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/campaigns | official | 2026-11-09 | v1 SP campaign example; placement adjustment example |
| Creating Sponsored Products ad groups | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/ad-groups | official | 2026-11-09 | shared bids and targeting; unique names |
| Global campaigns for Sponsored Products | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/global-campaigns | official | 2026-11-09 | GLOBAL scope; subsets; per-marketplace children; cascade |
| Common models: targets | https://advertising.amazon.com/API/docs/en-us/reference/common-models/targets | official | 2026-11-09 | target model shared across products |
| Example payloads | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/example-payloads | official | 2026-11-09 | v1 payloads incl. SD and Sponsored TV |
| Ads API v1 release notes | https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v1 | official | 2026-11-09 | beta and GA dates; "nearly 200 … 16" |
| Ads API release notes | https://advertising.amazon.com/API/docs/en-us/release-notes/index | official | 2026-11-09 | portfolio sharing, Global Store, bulksheet changes, SB changes |
| Deprecations | https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations | official | 2026-11-09 | shutoff dates; legacy account endpoints; Product Collection; Exports unaffected |
| SP v3 OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official | 2026-11-09 | SP paths, states, error reasons, quotas, update fields, target promotion groups |
| Portfolios OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json | official | 2026-11-09 | portfolio paths, policies, states, errors |
| Get started with Portfolios | https://advertising.amazon.com/API/docs/en-us/guides/portfolios/get-started | official | 2026-11-09 | one portfolio per campaign; uses |
| Sharing leftover budget | https://advertising.amazon.com/API/docs/en-us/guides/portfolios/sharing-leftover | official | 2026-11-09 | unspent budget sharing |
| Sponsored Brands overview | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/overview | official | 2026-11-09 | SB serving status to console status |
| Campaign structure for Sponsored Brands | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/structure | official | 2026-11-09 | one ad type per ad group; creative formats |
| Getting started with campaigns (Sponsored Brands) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns | official | 2026-11-09 | goals; fixed fields; IE exclusion |
| Amazon Ads API for Sponsored Display overview | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/overview | official | 2026-11-09 | SD hierarchy; tactics; DELETE archives |
| Limits, constraints, and quotas | https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits | official | 2026-11-09 | bids, budgets, keyword and name constraints, latencies |
| Get started with bulksheets: Part 1 | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/get-started-with-bulksheets-part1 | official | 2026-11-09 | columns; operations; download options |
| Get started with bulksheets for Sponsored Products | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/get-started | official | 2026-11-09 | SP entities; no keyword and product targeting together |
| Overview - About bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/overview-about-bulksheets | official | 2026-11-09 | what bulksheets are; legacy format deprecated 2023-09-28 |
| Understand which fields can be updated | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/editable-non-editable-bulksheets-fields | official | 2026-11-09 | fields that cannot be updated; archive-and-recreate route |
| Overview - how to update campaigns with bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/campaign-update-overview | official | 2026-11-09 | start date and targeting type fixed |
| How to create Sponsored Products campaigns with bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/create-sp-campaign | official | 2026-11-09 | four auto groups created with the default bid; Sites column |
| How to update Sponsored Products campaigns with bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/update-sp-campaigns | official | 2026-11-09 | archiving a parent archives its children |
| Bulksheets for portfolios | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/bulksheets-portfolios | official | 2026-11-09 | no Archive for portfolios; budget end date fixed |
| Sponsored ads campaign limits (Amazon Ads help) | https://advertising.amazon.com/help/G86H2227323T8T4Q | official | 2026-11-09 | entity count limits; limits raised as accounts approach them (content embedded in the page HTML) |
| Understand portfolios (Amazon Ads help) | https://advertising.amazon.com/help/GPEJN2E6R52G7C2T | official | 2026-11-09 | portfolio uses; billing by portfolio (content embedded in the page HTML) |
| Exports overview | https://advertising.amazon.com/API/docs/en-us/guides/exports/overview | official | 2026-11-09 | snapshot; coverage |
| Get started with exports | https://advertising.amazon.com/API/docs/en-us/guides/exports/get-started | official | 2026-11-09 | paths; URL lifetime |
| Exports FAQ | https://advertising.amazon.com/API/docs/en-us/guides/exports/faq | official | 2026-11-09 | job cap; cadence |
| Profiles | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles | official | 2026-11-09 | profile = account in a marketplace |
| QueryAdvertiserAccount API developer guide | https://advertising.amazon.com/API/docs/en-us/guides/account-management/query-advertiser-accounts | official | 2026-11-09 | global and non-global accounts |
| Create accounts | https://advertising.amazon.com/API/docs/en-us/guides/account-management/accounts/create-accounts | official | 2026-11-09 | account IDs |
| Advertisers OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Advertisers_prod_3p.json | official | 2026-11-09 | advertiser resource (little on structure) |
| Localization OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json | official | 2026-11-09 | keyword, product, expression, currency localization |
| Product strategy | https://advertising.amazon.com/library/guides/product-strategy | official | 2026-11-09 | group similar products; +6% against less similar products |
| New advertiser success guide | https://advertising.amazon.com/library/guides/new-advertiser-success-guide | official | 2026-11-09 | goals first; simple names; auto first |
| Best practices for your Sponsored Products ads | https://advertising.amazon.com/library/guides/sponsored-products-best-practices | official | 2026-11-09 | grouping by product group, category, price; portfolios |
| Checklist for new international ad campaigns | https://advertising.amazon.com/library/guides/checklist-for-new-international-ad-campaigns | official | 2026-11-09 | global SP; translation; sequence |
| unBoxed 2026 news: Explore the latest advertising announcements | https://advertising.amazon.com/library/news/unboxed-2026-news-announcements | official | 2026-11-09 | Ads Agent; Full-Funnel Campaigns |
| Campaign Manager beta: One command center for every campaign | https://advertising.amazon.com/resources/whats-new/unboxed-2025-campaign-manager | official | 2026-11-09 | revamped Campaign Manager (beta) |
| Sponsored Brands goal-based campaigns | https://advertising.amazon.com/resources/whats-new/sponsored-brands-goal-based-campaigns | official | 2026-11-09 | two goals; old campaigns tagged |
| Ad Intel: 5 common sponsored ads campaign mistakes | https://advertising.amazon.com/library/expert-advice/common-sponsored-ads-mistakes-and-solutions | opinion (partner, on Amazon's site) | 2026-11-09 | naming, portfolios, funnel split, budget order |
| Seller Forums: Revive campaign from archive | https://sellercentral.amazon.com/seller-forums/discussions/t/de6fac84-a3a2-44df-9074-c62cf980ec76 | official (staff reply) | 2026-11-09 | archived cannot be enabled or copied |
| Seller Forums: same keywords in different ad groups | https://sellercentral.amazon.com/seller-forums/discussions/t/bbf265413c73f5100c256da33acf7438 | opinion (sellers) | 2026-11-09 | unsourced "will not compete" claim |
| Seller Forums: same product in two campaigns | https://sellercentral.amazon.com/seller-forums/discussions/t/31a06264fe517de180891126092b5e60 | opinion (seller) | 2026-11-09 | overlap warning |
| Perpetua: campaign, ad group and target limits | https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit | opinion | 2026-11-09 | entity counts citing Amazon help |
| Karooya: Amazon Ads campaign limits | https://www.karooya.com/blog/amazon-ads-campaign-limits-you-must-know/ | opinion | 2026-11-09 | same counts, 2019 |
| Amalyze: bid and keyword limits | https://amalyze.com/resources/guides/advertising/amazon-ppc-bid-and-keyword-limits | opinion | 2026-11-09 | conflicting counts; bulksheet size |
| Capconvert: Amazon Ads account structure | https://www.capconvert.com/learn/blog/amazon-ads-account-structure | opinion | 2026-11-09 | hierarchy, naming, portfolios |
| Ad Badger: Amazon PPC campaign structure | https://www.adbadger.com/blog/amazon-ppc-education/amazon-ppc-campaign-structure/ | opinion | 2026-11-09 | segment by targeting type and product |
| Ad Badger: campaign naming guide | https://www.adbadger.com/blog/amazon-campaign-name-guide/ | opinion | 2026-11-09 | three-level naming |
| Ad Badger: segment branded keywords | https://www.adbadger.com/blog/how-to-segment-branded-keywords-in-amazon-ads/ | opinion | 2026-11-09 | branded split for and against |
| Scale Insights: build SKC campaigns | https://help.scaleinsights.com/en/knowledge-base/part-3-build-skc-campaigns-for-performers | opinion | 2026-11-09 | SKC build and naming |
| Quartile: single keyword campaigns | https://www.quartile.com/blog/achieving-adaptability-and-efficiency-with-single-keyword-campaigns | opinion | 2026-11-09 | SKC for |
| JumpFly: single keyword ad groups and campaigns | https://www.jumpfly.com/blog/single-keyword-ad-groups-and-campaigns-on-amazon/ | opinion | 2026-11-09 | SKC for and against |
| Helium 10: Amazon PPC campaign structure (Mina Elias) | https://www.helium10.com/blog/amazon-ppc-campaign-structure/ | opinion | 2026-11-09 | one ad group per campaign; keyword bullying |
| Helium 10: life cycle template strategy (Vince Montero) | https://www.helium10.com/blog/helium10-life-cycle-template-strategy/ | opinion | 2026-11-09 | four-campaign minimum; stages |
| Perpetua: Search Term Isolation | https://help.perpetua.io/en/articles/4172431-search-term-isolation | opinion | 2026-11-09 | cross-negatives between match lanes |
| Perpetua: 2021 Amazon ads strategy guide | https://perpetua.io/blog-amazon-ppc-ad-strategy/ | opinion | 2026-11-09 | auto + manual skeleton; thresholds |
| Seller Labs: too many vs too few campaigns | https://www.sellerlabs.com/knowledge-base/campaign-structure-diagnostics-too-many-vs-too-few-campaigns/ | opinion | 2026-11-09 | fragmentation signs |
| Rel.ai: how Amazon's ad auction works | https://rel.ai/blog/how-amazons-ad-auction-works | opinion | 2026-11-09 | relevance × bid reading; nothing on self-competition |
| Practical Lessons on Optimizing Sponsored Products | https://arxiv.org/abs/2304.09107 | research | 2026-11-09 | sponsored products modelling abstract |
| Competition and Crowd-Out for Brand Keywords | https://ideas.repec.org/a/inm/ormksc/v37y2018i2p200-215.html | research | 2026-11-09 | brand keyword field experiment abstract |
| Consumer Heterogeneity and Paid Search Effectiveness | https://www.nber.org/papers/w20171 | research | 2026-11-09 | eBay paid search experiment abstract |
| Sponsored Brands version 4 features and benefits | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/v4-features | official | 2026-11-09 | multiple ad groups and ads in v4 only; feature table; testing ads in one ad group (gap fill) |
| Migrating to version 4 Sponsored Brands campaigns | https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4 | official | 2026-11-09 | legacy vs multi-ad group; read-only legacy ad groups; `isMultiAdGroupsEnabled`; per-ad moderation; `creativeType: all`; 2023 storage change (gap fill) |
| Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API | https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4-api | official | 2026-11-09 | migration creates a new campaign; `legacyCampaignId` tag; start date reset; no performance carryover; deadlines; Q26 feature table (gap fill) |
| Managing Sponsored Brands campaigns (multi-ad group) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/managing-multi-ad-group-campaigns | official | 2026-11-09 | v4 list calls; ads list returns v3 and v4 ads (gap fill) |
| Overview - Sponsored Brands multi-ad group campaigns in bulksheets | https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sb/overview | official | 2026-11-09 | multi-ad group tab; pre-2022-11-15 campaigns in legacy tab; collection entities (gap fill) |
| SB v4 OpenAPI | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | official | 2026-11-09 | `AdGroup` and `Campaign` fields; `isMultiAdGroupsEnabled`; migration and ListMigrations schemas; batch sizes (gap fill) |
| SB v3 OpenAPI | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | official | 2026-11-09 | `/sb/keywords` create carries `adGroupId`, `campaignId`; 100 per call (gap fill) |
| Sponsored ads reporting overview (version 3) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/overview | official | 2026-11-09 | SB preview excludes `isMultiAdGroupsEnabled=False` (gap fill) |
| Search term reports (version 3) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term | official | 2026-11-09 | `spSearchTerm` columns (no advertised ASIN); clicked impressions only; SB preview note (gap fill) |
| Sponsored ads reporting FAQ (version 3) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/faq | official | 2026-11-09 | SB preview note (gap fill) |
| Product Collection Migration Guide | https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-product-collection | official | 2026-11-09 | January 2027 "Final shutoff" of creates; existing ads keep serving (gap fill) |
| Migrate from Product collections to Sponsored Brands collections (help) | https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P | official | 2026-11-09 | February 2027 end of support; auto-transition of 3-ASIN ads; "not variations of a single product" (gap fill; content embedded in page HTML, last modified 2026-10-05) |
| Adjust Sponsored Products bids (help) | https://advertising.amazon.com/help/GYYZVM7LGSRYGWV5 | official | 2026-11-09 | placement adjustments apply when eligible; stacking; $1 → $1.5 → $3 example (gap fill; last modified 2026-09-28) |
| Rest of search bid adjustment launch (2024-01-09) | https://advertising.amazon.com/resources/whats-new/improve-campaign-performance | official | 2026-11-09 | rest-of-search adjustment up to 900% (gap fill) |
| Understand keyword match types (help) | https://advertising.amazon.com/help/GHTRFDZRJPW6764R | official | 2026-11-09 | "the match type with the highest bid will be used" (contradiction 4; last modified 2026-07-29) |
| A guide to targeting with Sponsored Products | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official | 2026-11-09 | "you won't be bidding against yourself by adding different match types" (contradiction 4) |
| Sponsored Products eligibility requirements (help) | https://advertising.amazon.com/help/GMJYF5GN8RNYB6HD | official | 2026-11-09 | only child variations eligible; Featured Offer eligibility (gap fill; last modified 2026-10-20) |
| How to improve your products for advertising | https://advertising.amazon.com/library/guides/improve-your-products-for-advertising | official | 2026-11-09 | Featured Offer, in-stock, auto-pause when out of stock, Prime, reviews (gap fill) |
| Amazon Ads ASIN selection and promotion strategies (ASIN matrix) | https://advertising.amazon.com/library/guides/asin-matrix | official | 2026-11-09 | emerging/flagship/potential/longtail quadrants and ad types (gap fill) |
| Operations and advertising strategies for standard ASINs | https://advertising.amazon.com/library/guides/standard-asin-strategy | official | 2026-11-09 | standard vs non-standard ASINs; budget split guidance (gap fill) |
| Product strategy (re-read whole) | https://advertising.amazon.com/library/guides/product-strategy | official | 2026-11-09 | product labels and their figures (gap fill) |
| Product selector OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json | official | 2026-11-09 | `POST /product/metadata`; `SUGGESTED` sort; availability; variation list (gap fill) |
| Eligibility OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json | official | 2026-11-09 | `/eligibility/product/list` (gap fill) |
| Sponsored Products Rule-based bidding overview | https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview | official | 2026-11-09 | 10 days and 10 conversions in 30 days; 21-day guardrail (gap fill) |
| Analytics reports (SP-API report type values) | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics | official | 2026-11-09 | SQP report options, periods and fields (gap fill) |
| Deprecations (re-read for the account and Product Collection entries) | https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations | official | 2026-11-09 | `Warning: 299`; allowlist; 404 July 2027; Product Collection January 2027 (contradictions 1–3) |
| Ads API release notes (re-read: 2023-05-22, 2023-08-10, 2025-04-17, 2025-10-14, 2026-07-20, 2026-09-18) | https://advertising.amazon.com/API/docs/en-us/release-notes/index | official | 2026-11-09 | SB storage change; migration deadlines; account deprecation; ListMigrations (gap fill and contradictions) |
| Seller Forums (EU): Split product ads up into different ad groups retrospectively | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/46150e60-9be2-42dc-b0ce-1981c873c720 | opinion (sellers) | 2026-11-09 | history does not transfer between ad groups (non-staff reply) (gap fill) |
| Helium 10: Dynamic Bidding (2019) | https://www.helium10.com/blog/amazon-dynamic-bidding/ | opinion | 2026-11-09 | low bid + 900% top-of-search campaign beside the exact campaign (gap fill) |
| Feedvisor: Optimizing your Amazon ad placement | https://feedvisor.com/resources/amazon-marketing-advertising-strategies/optimizing-your-amazon-ad-placement/ | opinion | 2026-11-09 | low bid with high top-of-search adjustment (gap fill) |
| Perpetua: Maximizing the impact of top-of-search placements | https://perpetua.io/blog-maximizing-the-impact-of-top-of-search-amazon-ad-placements/ | opinion | 2026-11-09 | isolate keywords for top-of-search multipliers (gap fill) |
| Ad Badger: How to Combine "Adjust Bids by Placement" and Your Keyword Bid (2020) | https://www.adbadger.com/blog/amazon-ppc-education/placement-bid-adjustment-with-keyword-bid-campaign-settings-amazon-ppc/ | opinion | 2026-11-09 | single keyword campaigns for placement control; branded TOS distortion (gap fill) |
| Ad Badger: How to Use Adjust Bids by Placement (2023 Update) | https://www.adbadger.com/blog/amazon-ppc-education/adjust-bids-by-placement-amazon-ppc/ | opinion | 2026-11-09 | three placement campaigns; low-base-bid limit (gap fill) |
| m19: Top of Search on Amazon: Why Bidding High Isn't Enough | https://www.m19.com/blog/stop-bidding-on-top-of-search-on-amazon | opinion | 2026-11-09 | against one-keyword TOS campaigns (gap fill) |
| m19: How to Select the Right ASINs for Amazon Advertising? | https://www.m19.com/blog/amazon-asins-selection | opinion | 2026-11-09 | choose top-performing children; quadrant restatement (gap fill) |
| Karooya: Using Amazon Product Variations And PPC Together | https://www.karooya.com/blog/using-amazon-product-variations-and-ppc-together-to-maximize-sales/ | opinion | 2026-11-09 | child-only ads; one ad group per child (gap fill) |
| Canopy Management: Amazon Advertising Budgets 2026 (Chuck Kessler) | https://canopymanagement.com/amazon-advertising-budgets-how-to-allocate-spend-across-campaigns/ | opinion | 2026-11-09 | defensive budget for top 20% of products (gap fill) |
| Scale Insights: Amazon PPC for Variations | https://scaleinsights.com/learn/amazon-ppc-for-variations-ad-campaigns-for-multiple-product-options | opinion | 2026-11-09 | per-child campaigns; conflicting parent claim (gap fill) |
| Ad Badger: Keyword Cannibalization in Amazon PPC (2024) | https://adbadger.com/blog/keyword-cannibalization-and-placement-in-amazon-ppc/ | opinion | 2026-11-09 | two products on one SERP "not bidding against yourself" (gap fill) |
| Ad Badger: You're Optimizing Too Much (2026) | https://www.adbadger.com/blog/amazon-ppc-optimization-mistakes/ | opinion | 2026-11-09 | "resets Amazon's learning loop" (gap fill) |
| Clear Ads: Your Amazon Ad Structure Is Starving the Algorithm (George Meressa) | https://clearadsagency.com/your-amazon-ad-structure-is-starving-the-algorithm-heres-the-fix/ | opinion | 2026-11-09 | consolidation; "30 conversions" claim; restart CPC spike (gap fill) |
| Practical Lessons on Optimizing Sponsored Products (HTML full text) | https://arxiv.org/html/2304.09107 | research | 2026-11-09 | per-ad-item history features; no campaign concept (gap fill) |
| The Interpretation of Interaction in Contingency Tables (Simpson 1951) | https://doi.org/10.1111/j.2517-6161.1951.tb00088.x (Crossref) | research | 2026-11-09 | aggregation reversal (gap fill) |
| Sex Bias in Graduate Admissions: Data from Berkeley (Bickel et al. 1975) | https://doi.org/10.1126/science.187.4175.398 (Crossref) | research | 2026-11-09 | aggregate vs disaggregated reversal (gap fill) |
| The LMDI approach to decomposition analysis (Ang 2005) | https://doi.org/10.1016/j.enpol.2003.10.010 (Crossref) | research | 2026-11-09 | mix-against-rate decomposition (gap fill) |

The gap fill of 2026-11-09 added 45 rows (marked "gap fill" or by contradiction number): 27 on Amazon's hosts or Amazon's published models (one SP-API documentation page among them), 1 Seller Forums thread, 13 practitioner pages and 4 research pages; three of the Amazon rows (Deprecations, the release notes, Product strategy) re-read pages already listed above for the passages the gap fill used. Before the gap fill: 80 rows, 2 ComChatX plugin files and 78 public pages — 59 on Amazon's own hosts (one a partner article on Amazon's site, three Seller Forums threads, two help pages), 16 practitioner and vendor pages, and 3 research pages. Seven rows were added by the verifier (five bulksheet pages and two help pages). Search-result summaries that were not followed by a reading are not counted. Where one is used above, it is marked as such: Helium 10 Adtomic, the multi-ASIN vendor posts, and the Rutz and Abhishek abstracts.

### Unreachable

- **Amazon Ads help pages G86H2227323T8T4Q and GPEJN2E6R52G7C2T** were recorded here as JavaScript shells by the research seat. The verifier found that a plain GET carries the article text inside the HTML (`window.__scV2Content`), and read both (*Sponsored ads campaign limits*, *Understand portfolios*); they moved to *Pages read*.
- **Helium 10 knowledge base, *Creating Amazon Ads PPC Campaigns within Adtomic*** (https://kb.helium10.com/hc/en-us/articles/360046281853-Creating-Amazon-Ads-PPC-Campaigns-within-Adtomic): HTTP 403 to a plain GET (again 403 to the verifier, 2026-11-09).
- **Rutz, Bucklin and Sonnier (2012) PDF** (https://faculty.washington.edu/orutz/docs/Keywords_JMR_2012.pdf) and **Rutz and Bucklin (2011) PDF** (https://faculty.washington.edu/orutz/docs/Spillover_JMR_2011.pdf): fetched, but the local PDF tool failed on a missing library, so no text could be read (the verifier's attempts failed the same way).
- **JMR record on IDEAS** (https://ideas.repec.org/a/sae/jmarkr/v49y2012i3p306-319.html): HTTP 404.
- **EconBiz record** for the 2012 paper: blocked by a bot-protection page.
- **INFORMS page for Abhishek, Hosanagar and Fader** (https://pubsonline.informs.org/doi/10.1287/mksc.2014.0884): HTTP 403.
- **Guide paths that returned 404 on the docs' markdown host:** guides/portfolios/overview, guides/sponsored-brands/campaigns, guides/sponsored-products/target-promotion-groups (and three variants), no-code-tools/bulksheets/sd/overview, several bulksheet FAQ variants, and concepts/limits (the page lives at reference/concepts/limits). The seat was guessing these paths, so the 404s say only that the guesses were wrong. No guide page for target promotion groups was found.
- **SP OpenAPI under a guessed name** (SponsoredProductsProd_3p.json): HTTP 403. The real file is SponsoredProducts_prod_3p.json, which was read.
- **Gap fill, 2026-11-09:**
  - **Pacvue, *Three Reasons Winning Top of Search Doesn't Matter*** (https://pacvue.com/blog/three-reasons-why-winning-top-of-search-doesnt-matter/) and **Pacvue, *Using bid placement modifier rules to succeed on Amazon*** (https://pacvue.com/blog/using-bid-placement-modifier-rules-to-succeed-on-amazon/): HTTP 403 to a plain GET with browser headers. The Wayback Machine lists copies (2026-07-11 and 2026-08-21), but neither curl nor the fetch tool could retrieve web.archive.org from this environment. Only search summaries were used, marked as such.
  - **Amazon Ads what's-new page *Sponsored Brands ad groups*** (https://advertising.amazon.com/resources/whats-new/sponsored-brands-ad-groups): 301 to the what's-new index; the launch announcement is no longer served at that address. Its content is carried by the v4 features page and the migration guide, which were read.
  - **adbrew help, *Are my bids competing against each other?*** (https://help.adbrew.io/en/articles/11431690-are-my-bids-competing-against-each-other): HTTP 401, "you may need to sign in first"; not read.

## Open questions

1. **Entity counts.** Amazon's help page *Sponsored ads campaign limits* (last modified 2026-07-29) now gives the table (section I) and says Amazon raises limits as accounts approach them. Still open: whether the one table holds for SB and SD as it says (it lists no SB- or SD-specific counts, while third parties give SB its own), how high an account's raised limit can go, and which quotas count non-archived entities only.
2. **Self-competition.** Partly answered: for one keyword in several match types with different bids, "the match type with the highest bid will be used for any matching shopping query" (help GHTRFDZRJPW6764R), and the targeting guide says "you won't be bidding against yourself by adding different match types on the same keyword". Still open: whether that holds across ad groups and campaigns; which of two copies of the same keyword and match type in two campaigns (the placement-isolation structure, *What practitioners add* section 8) enters an auction, and whether the comparison uses the base bid or the placement-adjusted bid; how a keyword competes with an auto or product target matching the same query; and whether two of one advertiser's products can fill two sponsored slots of one results page (Ad Badger says they can).
3. **Cascade in single-marketplace SP.** Partly answered: Amazon's SP bulksheet update guide says "When you archive a parent entity, all child entities will also be archived." Still open: whether a single-marketplace SP v3 or v1 `delete` call cascades the same way (no API page read says so in words).
4. **Portfolio state.** The v3 API offers only ENABLED, and the bulksheet page says "'Archive' is not an option for portfolios", yet delivery reasons include PORTFOLIO_PAUSED and PORTFOLIO_ARCHIVED. Where are those states set, and can they be reversed?
5. **Portfolio count.** Is there a maximum number of portfolios per account? A QUOTA_EXCEEDED with ACCOUNT scope exists, but no figure was found; Amazon's *Sponsored ads campaign limits* page lists none.
6. **Account-level budget.** Is there an account-level budget or spend limit, as ADVERTISER_OUT_OF_BUDGET, SPEND_LIMIT_EXCEEDED and the Ad Intel article suggest? On which page and through which API is it set?
7. **SP goals.** Does SP accept any v1 `goalSettings` value? Does the console offer goal-based SP campaigns in any marketplace?
8. **Full-Funnel and the Ads Agent.** How do Full-Funnel Campaigns and the Amazon Ads Agent relate to a seller's existing SP, SB and SD campaigns? Do they create entities visible through the v1 query?
9. **Tags.** Are tags shown in the console and in reports, and can a report be grouped by tag?
10. **Generations.** Are entities created through SP v3, SB v4, bulksheets and the console all returned by the v1 query calls, and the reverse?
11. **Target promotion groups.** What heuristics drive the recommendations, and does the console create these groups (for example when a seller builds a manual campaign from an auto campaign's suggestions)?
12. **Bulksheets and the API.** Are bulksheet uploads subject to the same entity quotas and validation as API writes? What are the current file-size and row limits on an Amazon page?
13. **Variations in the ad.** When one child of a variation family is advertised, what does the ad show, and does the click open the family's page with that child selected (as Karooya writes)? Does Amazon ever serve a different child than the advertised one? No Amazon page read says.
14. **SB limits.** How many ad groups per SB campaign and ads per SB ad group does Amazon allow? Only Perpetua's SB table (1,000 keywords and 100 ads per campaign) and search summaries (100 ad groups) were found.
15. **Ads in one SB ad group.** How does Amazon divide impressions among several ads of one SB ad group (also `method/change-measurement.md`'s Open question)?
16. **Remaining legacy SB campaigns.** After the automatic migration announced from 2026-01-01, do any `isMultiAdGroupsEnabled=false` campaigns remain, and is the 2025-10-19 or the 2025-10-30 zero-impression deadline the one that applied?
17. **February 2027 for Product Collection.** Do non-migrated Product Collection ads with fewer than 3 ASINs stop serving in February 2027, and are they archived or left paused?
18. **Learning state.** Does Amazon keep any per-campaign or per-ad-group model state for bidding or relevance that a restructure resets? No Amazon page read documents one; the only campaign-history-dependent features found are rule-based bidding's eligibility and guardrail.

## Positions

Amazon's sources first. Each position is a fact with its source. A figure inside a position is for human readers only and is read at run time.

**P-campaign-structure-1.** A profile is one advertiser account in one marketplace and corresponds to an account in the advertising console. `GET /v2/profiles` returns only the profiles in the region of the host called. [official] *Profiles*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles, read 2026-11-09.

**P-campaign-structure-2.** Global and cross-product calls are scoped by the account ID in `Amazon-Ads-AccountId`. Single-marketplace calls are scoped by the profile ID in `Amazon-Advertising-API-Scope`. Global accounts have IDs of the form `amzn1.ads-account.g.*`. [official] *Global campaigns for Sponsored Products*; *QueryAdvertiserAccount API developer guide*; read 2026-11-09.

**P-campaign-structure-3.** In Sponsored Products the hierarchy is campaign → ad group → product ads and targets. "Both manual and auto campaigns can also contain negative product targeting expressions or negative keywords at the campaign level (in addition to the ad group level)." An auto campaign needs a campaign, an ad group and a product ad; a manual campaign also needs at least one keyword or product target per ad group. [official] *Sponsored Products campaign structure*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/get-started/campaign-structure, read 2026-11-09.

**P-campaign-structure-4.** "Products placed together in an ad group share the same bids and targeting", and "Ad group names must be unique within a campaign". [official] *Creating Sponsored Products ad groups*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/ad-groups, read 2026-11-09.

**P-campaign-structure-5.** In Sponsored Products "you cannot have both keyword and product targeting in a single ad group". [official] *Get started with bulksheets for Sponsored Products*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/get-started, read 2026-11-09.

**P-campaign-structure-6.** In Sponsored Brands "you can only include a single type of ad in each ad group". An SB ad group targets either keywords or products. [official] *Campaign structure for Sponsored Brands*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/structure, read 2026-11-09.

**P-campaign-structure-7.** In SP the budget, the bidding strategy with its placement bid adjustments, the start and end dates, the portfolio, the site restriction, the off-Amazon setting and the tags are fields of the campaign. Neither the SP v3 ad group nor the v1 SP ad group has a budget field. Two sets of targets can differ in any of these only by sitting in different campaigns. [official] SP v3 OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json; *Campaign*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/campaign; read 2026-11-09.

**P-campaign-structure-8.** Whether an SP campaign is auto or manual is set at creation (`targetingType`; v1 `autoCreationSettings.autoCreateTargets`). The SP v3 update request says "Note: targetingType cannot be updated", the v1 `CampaignUpdate` schema has no `autoCreationSettings`, and bulksheets say "You cannot update an auto campaign to be manual, and vice versa." [official] SP v3 OpenAPI; merged OpenAPI; *Understand which fields can be updated*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/editable-non-editable-bulksheets-fields; read 2026-11-09.

**P-campaign-structure-9.** An SP auto campaign's targets are four theme groups: close match, loose match, substitutes and complements. In bulksheets, "If you do not create all four entities, Amazon will automatically create them, and the ad group default bid will apply." They take their own bids and states, and cannot be archived by hand (AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY). [official] *How to create Sponsored Products campaigns with bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/create-sp-campaign; SP v3 OpenAPI; *Global campaigns for Sponsored Products*; read 2026-11-09.

**P-campaign-structure-10.** Amazon's SP guide suggests: "We suggest new advertisers start with auto campaigns. You can then analyze the performance of suggested keyword and targeting expressions, and create a manual campaign using the highest performers." [official] *Sponsored Products campaign structure*, read 2026-11-09.

**P-campaign-structure-11.** SP v3 offers target promotion groups (`/sp/targetPromotionGroups`), which link an auto ad group to manual destination ad groups. It also has a recommendations call that "Retrieves keyword and product targets of an auto-targeting campaign as recommendations for promoting to a manual-targeting campaign… based on performance heuristics of the targets." [official] SP v3 OpenAPI, read 2026-11-09.

**P-campaign-structure-12.** ARCHIVED is "permanently stopped and cannot be reactivated. Terminal end state." Every API reaches it through a delete call, and bulksheets through an Archive row. An Amazon staff reply adds that archived campaigns "cannot be enabled or copied" and suggests pausing instead when the campaign may be used again. [official] merged OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json; Seller Forums staff reply, https://sellercentral.amazon.com/seller-forums/discussions/t/de6fac84-a3a2-44df-9074-c62cf980ec76; read 2026-11-09.

**P-campaign-structure-13.** Under an archived parent, Amazon refuses updates and creations of children (PARENT_ARCHIVED_FORBIDS_UPDATES, PARENT_ENTITY_FORBIDS_CREATION). In global campaigns, archiving cascades to the children. In SP bulksheets, "When you archive a parent entity, all child entities will also be archived." [official] SP v3 OpenAPI; *Global campaigns for Sponsored Products*; *How to update Sponsored Products campaigns with bulksheets*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/sp/sp-examples/update-sp-campaigns; read 2026-11-09.

**P-campaign-structure-14.** Several things are fixed at creation:

- keyword text and match type: the SP v3 keyword update takes only bid and state
- a product ad's product
- a product target's expression (bulksheets: "Targeting can only be archived or paused")
- a campaign's site restriction ("cannot be changed post campaign creation")
- a campaign's start date and targeting type, in bulksheets
- an SB goal-based campaign's goal, costType and smartDefault

To change one, Amazon's documented route is a new entity, with the old one paused or archived: "For fields that cannot be edited (for example, keyword text or ASIN/SKU), a typical workaround is to archive its associated entity, then create a new one with the updated information." [official] SP v3 OpenAPI; *Understand which fields can be updated*; *Getting started with campaigns* (SB), https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns; read 2026-11-09.

**P-campaign-structure-15.** "A campaign can only belong to one portfolio at a time", and portfolios "do not compete against each other". [official] *Get started with Portfolios*, https://advertising.amazon.com/API/docs/en-us/guides/portfolios/get-started, read 2026-11-09.

**P-campaign-structure-16.** A portfolio's budget cap has a policy of DATE_RANGE, MONTHLY_RECURRING, NO_CAP or OTHER, with an amount and dates. Unspent budget sharing lets campaigns that have spent their daily budget use the portfolio's unspent budget from previous days in the month, "up to 100% more than their average daily budget on any given day". The month's total stays within the sum of daily budgets times days. The feature is on by default for portfolios created after 2025-06-20. [official] Portfolios OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json; *Sharing leftover budget*, https://advertising.amazon.com/API/docs/en-us/guides/portfolios/sharing-leftover; read 2026-11-09.

**P-campaign-structure-17.** A portfolio's condition shows in its campaigns' delivery reasons (v1: PORTFOLIO_OUT_OF_BUDGET, PORTFOLIO_END_DATE_REACHED, PORTFOLIO_PENDING_START_DATE, PORTFOLIO_PAUSED, PORTFOLIO_ARCHIVED; SP v3 spells the end-date status PORTFOLIO_ENDED), next to campaign, ad group, target, advertiser and offer reasons. [official] merged OpenAPI, read 2026-11-09.

**P-campaign-structure-18.** A write that would exceed an entity quota is refused with QUOTA_EXCEEDED or NON_ARCHIVED_QUOTA_EXCEEDED, scoped to ACCOUNT or PARENT_ENTITY. Some quotas therefore count only non-archived entities. [official] SP v3 OpenAPI, read 2026-11-09.

**P-campaign-structure-19.** Campaign names are limited to 128 characters for sellers and 116 for vendors, and ad group names to 255. Amazon lists the allowed symbols, which include the pipe `|`, and forbids leading and trailing spaces. Campaigns (and v1 ad groups and targets) carry up to 50 tags. [official] *Limits, constraints, and quotas*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits; SP v3 OpenAPI; merged OpenAPI; read 2026-11-09.

**P-campaign-structure-20.** Ads API v1 models campaigns, ad groups, ads, targets and ad associations across SP, SB, SD, Sponsored TV and DSP; "At launch, calls will be bound to one ad product at a time". Amazon says these APIs "will eventually fully replace the ad product-specific APIs". Its create, update and delete calls answer 207 with per-index success, error and partial success. [official] *Campaign management in the Amazon Ads API*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview; *Amazon Ads API v1 overview*, https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview; merged OpenAPI; read 2026-11-09.

**P-campaign-structure-21.** A global SP campaign has `marketplaceScope` GLOBAL, and "a child's list must be a subset of its parent's" marketplaces. Ads and targets each carry one marketplace, with keywords in that marketplace's language. The bid strategy is set once for the campaign, while bids, budgets and listed fields can differ per marketplace through `marketplaceConfigurations`. Only the `spCampaigns` report surfaces global campaigns. [official] *Global campaigns for Sponsored Products*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/global-campaigns, read 2026-11-09.

**P-campaign-structure-22.** Amazon's Localization API maps keywords, products, targeting expressions and currencies between marketplaces. For a seller, a product localizes only if a product with the same SKU exists in the target marketplace and the seller is eligible to advertise it. [official] Localization OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json, read 2026-11-09.

**P-campaign-structure-23.** Amazon's international checklist:

- says "Launch a global Sponsored Products campaign for all the countries you want to advertise in"
- notes that "Even if you run the same campaign in multiple countries, the results can be different"
- offers in-console keyword translation that does not support every language combination

[official] *Checklist for new international ad campaigns*, https://advertising.amazon.com/library/guides/checklist-for-new-international-ad-campaigns, read 2026-11-09.

**P-campaign-structure-24.** Sponsored Brands goal-based campaigns have two goals: drive page visits (the default, with CPC, when neither goal nor cost type is sent) and grow brand impression share (vCPM only). Earlier SB campaigns are tagged "Drive page visits". Goal-based campaigns are not supported in Ireland. Sponsored Display expresses its objective through `bidOptimization` (clicks, conversions, reach) with a contextual or audience tactic. [official] *Getting started with campaigns* (SB); *Sponsored Brands goal-based campaigns*, https://advertising.amazon.com/resources/whats-new/sponsored-brands-goal-based-campaigns; *Amazon Ads API for Sponsored Display overview*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/overview; read 2026-11-09.

**P-campaign-structure-25.** Amazon reports that "Ad groups containing similar products saw 6% more units sold on average when advertising with Sponsored Products, compared to those with less similar products" (Amazon internal data, worldwide, 2023). It advises grouping similar products, using "separate campaigns or ad groups for each product group", including "ASINs from the same category in one campaign" and adding "as many similar products to the ad group as you can". [official] *Product strategy*, https://advertising.amazon.com/library/guides/product-strategy; *Best practices for your Sponsored Products ads*, https://advertising.amazon.com/library/guides/sponsored-products-best-practices; read 2026-11-09.

**P-campaign-structure-26.** Amazon suggests portfolios "to organize your campaigns by brand, category, season, or any way you choose". It says that "Establishing your goals up front will help you … decide how to structure your campaigns". [official] *Best practices for your Sponsored Products ads*; *New advertiser success guide*, https://advertising.amazon.com/library/guides/new-advertiser-success-guide; read 2026-11-09.

**P-campaign-structure-27.** A bulksheet row carries Product, Entity and Operation (Create, Update, Archive) over the same entities as the SP API. Amazon's bulksheet pages state the same fixed fields and the same archive-and-recreate route as the API's schemas imply, and add that archiving a parent archives its children. [official] *Get started with bulksheets: Part 1*, https://advertising.amazon.com/API/docs/en-us/no-code-tools/bulksheets/get-started-with-bulksheets-part1; *Understand which fields can be updated*; *How to update Sponsored Products campaigns with bulksheets*; read 2026-11-09.

**P-campaign-structure-28.** An export from the Exports API is a snapshot of campaigns, ad groups, ads or targets at request time, with no history. Its download URL is short-lived. [official] *Exports overview*, https://advertising.amazon.com/API/docs/en-us/guides/exports/overview; *Get started with exports*; read 2026-11-09.

**P-campaign-structure-29.** Amazon marks a campaign that it manages through the flag `autoManageCampaign`, which v1's `autoCreationSettings` describes as "Flag that allows Amazon to manage the lifecycle of your Campaign" (SP v3 carries the same boolean without a description). [official] merged OpenAPI; SP v3 OpenAPI; read 2026-11-09.

**P-campaign-structure-30.** The Perpetua Marketing Team (2021) structures each ASIN as one auto campaign, one manual campaign with broad, exact and ASIN ad groups, and one category campaign. It leaves phrase match out and fences the lanes with initial negatives. Its Search Term Isolation feature (2026) adds negative exact to the phrase ad group and negative phrase to the broad ad group, so a search term matches only its exact keyword. [opinion] Perpetua, https://perpetua.io/blog-amazon-ppc-ad-strategy/ and https://help.perpetua.io/en/articles/4172431-search-term-isolation, read 2026-11-09.

**P-campaign-structure-31.** Vince Montero (Helium 10, 2021/2022) names a minimum of four SP campaigns: Auto (research), Manual Research (broad), Manual Performance (exact) and Manual Product Targeting. He moves winning search terms into exact in the Performance campaign during a Scale stage. [opinion] https://www.helium10.com/blog/helium10-life-cycle-template-strategy/, read 2026-11-09.

**P-campaign-structure-32.** Seller Labs (knowledge base, 2026) recommends auto, broad/phrase, exact and an optional product targeting campaign per ASIN or tight family. It names as signs of over-fragmentation "5–10+ campaigns per ASIN without a clear strategic reason", "Duplicated keywords across campaigns" and "Many campaigns spending $2–$5 daily". As signs of under-structure it names mixed auto and manual and no branded/non-branded split. [opinion] https://www.sellerlabs.com/knowledge-base/campaign-structure-diagnostics-too-many-vs-too-few-campaigns/, read 2026-11-09.

**P-campaign-structure-33.** Single keyword campaigns are argued for by:

- Scale Insights: one exact keyword per campaign, with a naming pattern
- Quartile: one ASIN, one keyword and one match type, tracked hourly
- Reilly McDonnell (JumpFly, 2022): campaign-level placement control and brand defence

They are argued against by McDonnell himself ("much less search volume to examine", "challenging to make decisions with only a few clicks", more time) and by Capconvert ("selectively"). [opinion] Scale Insights, https://help.scaleinsights.com/en/knowledge-base/part-3-build-skc-campaigns-for-performers; Quartile, https://www.quartile.com/blog/achieving-adaptability-and-efficiency-with-single-keyword-campaigns; JumpFly, https://www.jumpfly.com/blog/single-keyword-ad-groups-and-campaigns-on-amazon/; Capconvert, https://www.capconvert.com/learn/blog/amazon-ads-account-structure; read 2026-11-09.

**P-campaign-structure-34.** Mina Elias (Helium 10, 2020/2022) advises "only create one ad group per campaign" with up to about ten keywords of similar search volume, because high-volume keywords take the budget ("keyword bullying"). He says "Amazon distributes the budget at their own discretion" across a campaign's ad groups. [opinion] https://www.helium10.com/blog/amazon-ppc-campaign-structure/, read 2026-11-09.

**P-campaign-structure-35.** Shazib Haseen (Ad Badger, 2019) advises "segment each of your campaigns by targeting type and then segment each ad group by product". He calls single-product ad groups "still a winning strategy" for very large catalogues, and uses portfolios for large accounts. Capconvert puts child ASINs in separate ad groups. [opinion] https://www.adbadger.com/blog/amazon-ppc-education/amazon-ppc-campaign-structure/; Capconvert, as above; read 2026-11-09.

**P-campaign-structure-36.** The Badger (Ad Badger, 2019) describes branded segmentation:

- the brand as a negative exact in product targeting campaigns
- branded keywords in their own campaign
- an optional competitor campaign
- no overlap between them

He calls it "more of a reporting strategy than a performance strategy" and concludes that "in general a hardline separation of your keywords probably isn't worth it". [opinion] https://www.adbadger.com/blog/how-to-segment-branded-keywords-in-amazon-ads/, read 2026-11-09.

**P-campaign-structure-37.** Naming conventions in print put the ad product, product identifier, targeting kind or match type, and objective into the name, separated by pipes or underscores:

- Ad Badger (2024): "Product name ASIN | Ad Type | Targeting | Strategy Objective | Bid Adjustment"
- Capconvert: "SP | Auto | Brand | Category | MatchType | Goal"
- Scale Insights: "SP_ASIN_ProductName_SKC_Exact_KT_{Keyword}"

[opinion] https://www.adbadger.com/blog/amazon-campaign-name-guide/; Capconvert; Scale Insights; read 2026-11-09.

**P-campaign-structure-38.** Third-party tables of SP entity limits disagree with each other and, in places, with Amazon's own help page (P-campaign-structure-42):

- Perpetua (2026, citing Amazon help) and Karooya (2019): 10,000 campaigns per account, 20,000 ad groups per campaign and 10,000 product targets per ad group
- Amalyze (undated, uncited): "up to 1 million" campaigns, 10,000 ad groups per campaign and 1,000 product targets per ad group

[opinion] https://help.perpetua.io/en/articles/5138146-the-campaigns-ad-groups-target-limits-for-each-ad-unit; https://www.karooya.com/blog/amazon-ads-campaign-limits-you-must-know/; https://amalyze.com/resources/guides/advertising/amazon-ppc-bid-and-keyword-limits; read 2026-11-09.

**P-campaign-structure-39.** Brent Zahradnik (AMZ Pathfinder, an Amazon Ads Verified Partner, in Amazon's Ad Intel series) names "Campaigns that are built without clear naming conventions, mixed targeting types, unclear objectives, overlapping targeting, and scattered ASINs" as the most visible audit problem. He advises portfolios by brand, product line or season, and a top-, middle- and bottom-of-funnel campaign split. [opinion, on an Amazon page] https://advertising.amazon.com/library/expert-advice/common-sponsored-ads-mistakes-and-solutions, read 2026-11-09.

**P-campaign-structure-40.** In Bing field experiments across many brands, a brand's own ad on its brand keyword added about 1–4% clicks when no competitor bid. Where the brand did not advertise and competitors did, competitors took 18–42% of clicks. The authors conclude defensive brand advertising has strongly positive returns. The setting is a general search engine, not Amazon's store. [research] Simonov, Nosko and Rao, *Marketing Science* 37(2), 2018, abstract at https://ideas.repec.org/a/inm/ormksc/v37y2018i2p200-215.html, read 2026-11-09.

**P-campaign-structure-41.** In eBay's field experiments on search-engine ads, brand-keyword ads showed no measurable short-term benefit. Non-brand ads worked mainly for new and infrequent users. Returns were "a fraction of conventional non-experimental estimates". The setting is search-engine advertising for eBay, not Amazon's store. [research] Blake, Nosko and Tadelis, *Econometrica* 83, 2015 (NBER w20171), https://www.nber.org/papers/w20171, read 2026-11-09.

**P-campaign-structure-42.** Amazon's help page *Sponsored ads campaign limits* (last modified 2026-07-29) lists, for SP, SB and Display "across all advertiser types", 10,000 campaigns per account (active and paused), 20,000 ad groups per campaign, 200,000 ad groups per account, 2,000,000 ads and 2,000,000 keywords per account, and 10,000 campaign and ad-group negative keywords. It says "Advertisers can archive campaigns, ad groups, ads, or targets to free up space. Amazon now increases customer limits as they approach a limit beyond the limits listed below." Figures for human readers only. [official] https://advertising.amazon.com/help/G86H2227323T8T4Q, read 2026-11-09.

**P-campaign-structure-43.** Product Collection Sponsored Brands ads are deprecated: from August 2026 a create request is mapped to Manual Collection, after January 2027 it returns an error, and Amazon's release note of 2026-09-18 says "Beginning February 2027, product collections will no longer be supported". Existing Product Collection campaigns "will continue to function and can be edited" (release note of 2026-07-06) until then. The two dates name different ends: January 2027 is the API create shutoff (the migration guide's "Final shutoff. All API requests to create Product Collection ads will be rejected with an error"), and February 2027 is the end of support for existing ads, when "Eligible … product collection ads with 3 ASINs that have not been migrated will be automatically transitioned to manual collections featuring the same 3 ASINs. Product collections with fewer than 3 ASINs will not auto-migrate" (help GV7N6KZTH4HF4T2P). Dates for human readers only. [official] *Deprecations*, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations; *Ads API release notes*, https://advertising.amazon.com/API/docs/en-us/release-notes/index; *Product Collection Migration Guide*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-product-collection; *Migrate from Product collections to Sponsored Brands collections*, https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P; read 2026-11-09.

**P-campaign-structure-44.** A Sponsored Brands version 4 ("multi-ad group") campaign can hold several ad groups, and each ad group several ads; "There has to be at least one ad in an ad group and an ad group cannot have more than one ad type", and an ad group uses "either product or keyword targeting expressions". Ads in one ad group "share the same landing page but different ASINs, headlines, life style images, product category, or videos", and Amazon says advertisers "can test different versions of the same ad formats within the same ad group". [official] *Getting started with campaigns* (SB), https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns; *Migrating to version 4 Sponsored Brands campaigns*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4; *Sponsored Brands version 4 features and benefits*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/v4-features; read 2026-11-09.

**P-campaign-structure-45.** The SB v4 ad group schema has no bid field (`campaignId`, `name`, `state`, `adGroupId`, `extendedData`); the SB campaign carries the budget, `bidding`, `goal`, `costType`, `smartDefault`, `portfolioId`, `siteRestrictions`, `tags` and the boolean `isMultiAdGroupsEnabled`, and bids sit on keywords and targets. [official] SB v4 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json; SB v3 OpenAPI (`/sb/keywords`), https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml; read 2026-11-09.

**P-campaign-structure-46.** In SB multi-ad group campaigns "only ads get moderated for the ad policy. If your ad gets rejected … your campaign status remains unchanged", and "The new campaigns can continue to deliver impressions if there is one active ad"; in legacy campaigns a rejected creative changes the campaign's status to rejected. [official] *Migrating to version 4 Sponsored Brands campaigns*, read 2026-11-09.

**P-campaign-structure-47.** Legacy (version 3) SB campaigns "contain read-only ad groups where creatives are associated with campaigns instead of ad groups"; "Adding new ad groups to legacy campaigns is not allowed", a v4 update of a legacy ad group returns `INVALID_ARGUMENT`, and their ads have no `adId` or `name`. During the v3 reporting preview, "data related to Sponsored Brands campaigns with flag `isMultiAdGroupsEnabled=False` will not be available". [official] *Migrating to version 4 Sponsored Brands campaigns*; SB v4 OpenAPI; *Sponsored ads reporting overview (version 3)*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/overview; read 2026-11-09.

**P-campaign-structure-48.** A legacy SB campaign migrated to version 4 becomes a new campaign with a new ID; on `MIGRATION_COMPLETE` "The V3 campaigns are archived"; the migrated campaign's start date becomes "the date the migration begins", its name gets a `migrated` suffix, the old ID is kept under the `legacyCampaignId` tag, and the process prevents "unintended performance data carryover". Migrated campaigns default to "Drive Page Visits" with `CPC`. Amazon's pages gave migration deadlines in 2025 and an automatic migration "starting January 1st, 2026" (dates for human readers only). [official] *Migrating to version 4 Sponsored Brands campaigns using the legacy campaigns migration API*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4-api; SB v4 OpenAPI; *Ads API release notes* (2025-04-17, 2025-10-14); read 2026-11-09.

**P-campaign-structure-49.** The legacy account endpoints (`POST /adsAccounts`, `POST /adsAccounts/batch`, `GET /adsAccounts/{accountId}`, `POST /adsAccounts/list`, `GET /dsp/advertisers`, `GET /dsp/advertisers/{advertiserId}`) return `Warning: 299` from July 2026; "new client integrations are blocked. Existing callers continue to function through an allowlist until the shutoff date"; from July 2027 they return `HTTP 404 Not Found`. The replacement for account retrieval and listing is `POST /adsApi/v1/query/advertiserAccounts` (dates for human readers only). [official] *Deprecations*, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations; *Ads API release notes* (2026-07-20); read 2026-11-09.

**P-campaign-structure-50.** In Sponsored Products, "only the variation (child product) is eligible for advertising"; "In order to advertise, your product must be eligible to be the featured offer"; and "If a product you are advertising goes out of stock, it will be automatically paused within your campaign." [official] *Sponsored Products eligibility requirements*, https://advertising.amazon.com/help/GMJYF5GN8RNYB6HD; *How to improve your products for advertising*, https://advertising.amazon.com/library/guides/improve-your-products-for-advertising; read 2026-11-09.

**P-campaign-structure-51.** Amazon labels products on the campaign creation page as "suggested" ("most likely to generate impressions and clicks when advertised") and by reason (New product, Brand building, Benchmarking, Forecasted demand, Trending), and reports, from internal 2023 data, that "Suggested products observed 321 times more sales when advertised, compared to products that are not suggested" and that excess-inventory products saw "an average 67% uplift in ordered units" after being added to a campaign (figures for human readers only). The API's `POST /product/metadata` sorts a seller's SP products by `SUGGESTED` and returns `availability`, `eligibilityStatus`, `bestSellerRank` and `variationList`. [official] *Product strategy*, https://advertising.amazon.com/library/guides/product-strategy; Product selector OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json; read 2026-11-09.

**P-campaign-structure-52.** Amazon's ASIN matrix guide sorts ASINs by life cycle and sales against catalogue averages into emerging, flagship, potential and longtail, and says "Flagship and emerging ASINs are the main ones that help you increase impressions and sales, so we tend to carry out multiple sponsored ads campaigns on these products", while "If you still have the resources to spare and have good longtail ASINs, you can also try using Sponsored Products for longtail ASINs". [official] *Amazon Ads ASIN selection and promotion strategies*, https://advertising.amazon.com/library/guides/asin-matrix, read 2026-11-09. m19 (2026) restates the matrix and advises advertising "only the top-performing children" of a family; Canopy's Chuck Kessler (2026) gives "the 20% of products driving 80% of revenue" a defensive budget. [opinion] https://www.m19.com/blog/amazon-asins-selection; https://canopymanagement.com/amazon-advertising-budgets-how-to-allocate-spend-across-campaigns/; read 2026-11-09.

**P-campaign-structure-53.** For Sponsored Brands collections Amazon advises choosing "distinct products that complement each other, not variations of a single product or unrelated items (such as different sizes, colors, etc)". [official] *Migrate from Product collections to Sponsored Brands collections*, https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P, read 2026-11-09.

**P-campaign-structure-54.** A Sponsored Products placement adjustment increases a bid "when your ad is eligible to compete for" that placement, "works in addition to your selected bidding strategy (dynamic or fixed)", and is set per campaign for top of search, rest of search (since 2024-01-09, "up to 900% same as the other two placements") and product pages; Amazon's example takes a $1 bid with +50% top of search to $1.5, and up to $3 with dynamic bids up and down. [official] *Adjust Sponsored Products bids*, https://advertising.amazon.com/help/GYYZVM7LGSRYGWV5; *Improve your campaign performance on rest of search placements…*, https://advertising.amazon.com/resources/whats-new/improve-campaign-performance; read 2026-11-09.

**P-campaign-structure-55.** Placement isolation, holding the same exact keyword in a campaign with a low base bid and a high top-of-search adjustment beside a campaign for the other placements, is argued for by the Helium 10 Team (2019: "run it in parallel with the standard Performance campaign … without competing against it for the rest of the placements"), Feedvisor ("set a low bid … and a high top of search adjustment") and Perpetua ("Isolate keywords for targeting with top-of-search bid multipliers"), and by Ad Badger (2020, 2023) as single keyword or per-placement campaigns. Ad Badger (2023) says a very low base bid may not enter the auction ("Amazon doesn't quite play along with that idea"), m19 (2026) advises against one-keyword top-of-search campaigns (minimum budgets, cost, management load), and Pacvue's moderate-base-bid argument is known only from search summaries. [opinion] https://www.helium10.com/blog/amazon-dynamic-bidding/; https://feedvisor.com/resources/amazon-marketing-advertising-strategies/optimizing-your-amazon-ad-placement/; https://perpetua.io/blog-maximizing-the-impact-of-top-of-search-amazon-ad-placements/; https://www.adbadger.com/blog/amazon-ppc-education/placement-bid-adjustment-with-keyword-bid-campaign-settings-amazon-ppc/; https://www.adbadger.com/blog/amazon-ppc-education/adjust-bids-by-placement-amazon-ppc/; https://www.m19.com/blog/stop-bidding-on-top-of-search-on-amazon; read 2026-11-09.

**P-campaign-structure-56.** Amazon states that "If you set multiple match types with different bids for the same keyword, then the match type with the highest bid will be used for any matching shopping query", and that "you won't be bidding against yourself by adding different match types on the same keyword"; the pages read do not say how this extends across ad groups or campaigns, or to two copies of one keyword in the same match type. [official] *Understand keyword match types*, https://advertising.amazon.com/help/GHTRFDZRJPW6764R; *A guide to targeting with Sponsored Products*, https://advertising.amazon.com/library/guides/targeting-with-sponsored-products; read 2026-11-09.

**P-campaign-structure-57.** Rule-based bidding requires a campaign "running for at least 10 days prior to setting a rule" with "a minimum of 10 conversions in the last 30 days", bases the ROAS guardrail on "the previous 21 days", and is switched off when the last 20 days' ROAS falls below 30% of the 20-to-40-day ROAS; these are the campaign-history-dependent states Amazon documents. No Amazon page read documents a per-campaign learning state for bids or relevance. Ad Badger (2026) says "every change you make resets Amazon's learning loop", and George Meressa (Clear Ads, 2026) puts a "data starvation" line at 30 conversions in 30 days, which he attributes to Amazon. [official] *Sponsored Products Rule-based bidding overview*, https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview; [opinion] https://www.adbadger.com/blog/amazon-ppc-optimization-mistakes/; https://clearadsagency.com/your-amazon-ad-structure-is-starving-the-algorithm-heres-the-fix/; read 2026-11-09.

**P-campaign-structure-58.** The Sponsored Products search term report (`spSearchTerm`) carries `searchTerm`, `campaignId`, `adGroupId`, `keywordId`, `matchType`, `keywordType` and `targeting` but no advertised-ASIN column, and "only include[s] impressions that resulted in at least one ad click"; the SP-API Search Query Performance report gives per-ASIN, per-query `searchQueryVolume`, `totalQueryImpressionCount`, `asinImpressionCount`, `asinClickCount`, `asinPurchaseCount` and shares by WEEK, MONTH or QUARTER to brand-registered sellers. [official] *Search term reports*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term; *Analytics reports*, https://developer-docs.amazon/sp-api/docs/report-type-values-analytics; read 2026-11-09.

**P-campaign-structure-59.** Aggregated rates can show a pattern the disaggregated units do not: Bickel, Hammel and O'Connell found Berkeley's aggregate admissions "a clear but misleading pattern of bias" that the department-level data did not show, because applicants' distribution across departments differed; Simpson (1951) gives the contingency-table form. The log-mean Divisia index (Ang 2005) splits a change in a product of factors into per-factor parts with no residual. [research] *Science* 187(4175), 1975, https://doi.org/10.1126/science.187.4175.398; *JRSS B* 13(2), 1951, https://doi.org/10.1111/j.2517-6161.1951.tb00088.x; *Energy Policy* 33(7), 2005, https://doi.org/10.1016/j.enpol.2003.10.010; read 2026-11-09.

### Seat's positions (enter no skill)

- [seat] Most of the structure arguments reduce to the rule in P-campaign-structure-7. Separating things into campaigns buys separate budgets, bid strategies and placement adjustments. Putting them together pools their data and budget, and Amazon then allocates between them. The practitioner positions are different prices put on that trade. None of the pages read measures the trade on Amazon.
- [seat] Amazon's +6% for similar-product ad groups (P-campaign-structure-25) is the only measured structural effect found from Amazon. Amazon states the comparison: ad groups of similar products against ad groups of less similar products. It does not compare grouped against single-product ad groups, so it does not settle the one-product-per-ad-group dispute.
- [seat] Archive is the one structural write that cannot be taken back. Several fixed-at-creation fields turn a "change" into a create plus an archive. A skill that understands this can tell the seller what a structural change actually does at Amazon. How it says so is the skill's and the model's own.
- [seat] Because Amazon gives names no meaning, the purpose of a campaign ("ranking", "harvest", "defend") is readable only from the seller's names and tags and from its settings. A seller's naming convention is therefore part of the data cx reads, and a convention the seller already uses is evidence of how they think about their account.
- [seat] The research found bears on branded keywords and keyword-level data sparsity in general search engines. Its transfer to Amazon's store, where the organic result is the same product listing, is unproven. `beyond/brand-defense-and-competition.md` is the place to weigh it.
- [seat] A restructure moves queries between campaigns, so every campaign-level rate after it describes a different query mix than before. The comparison that holds the mix fixed is per advertised ASIN and per query, summed over all campaigns (section 10 of *What practitioners add*); without it, a "better" exact campaign and a "worse" source campaign may both be artefacts of the move.
- [seat] Placement isolation and the self-competition question meet in one gap: Amazon's tie-break is documented only for different match types of one keyword. Whether a top-of-search copy and a product-page copy of the same exact keyword split the auction the way their builders intend is something the seller's own placement and search term reports show, campaign by campaign, not something any page read guarantees.
- [seat] For SB, the multi-ad group model makes the ad group the unit of theme and the ad the unit of creative; a legacy campaign can do neither, and its history after migration lives under a new ID. A skill reading SB history across 2025–2026 meets both.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** The file was read whole. Every cited page was re-opened by plain GET as a browser would: Amazon Ads API documentation through its public markdown copies (`https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`); the published OpenAPI files (merged v1, SP v3, Portfolios, Localization, Advertisers) on the public CloudFront host, parsed locally to check schemas, enums, descriptions and `maxItems`; Amazon's library, what's-new and unBoxed pages; the three Seller Forums threads; the two Amazon Ads help pages (whose article text is embedded in the public HTML); every practitioner page; and the research abstracts. Each verbatim quote was matched against the page text, each page name against the page's own title, each tag against who wrote the words, and each figure against the current page and the release notes and *Deprecations* page for later changes. Web searches looked for 2025–2026 Amazon announcements that overturn a claim (entity limits, archive behaviour, Product Collection, SB migration, v1 general availability, unBoxed 2026, self-competition). Positions were checked for behaviour wording (when to ask, fixed sequences, thresholds as rules, ceilings, how cx talks); none was found among P-campaign-structure-1 to 41, whose thresholds are all attributed practitioner claims, so no position moved; two positions were added (42, 43) from pages the verifier read. No Ads API host (advertising-api*.amazon.com), Login with Amazon (api.amazon.com/auth), Amazon Ads MCP endpoint, SP-API host, Seller Central help-hub content call, or page needing sign-in was called. No seller data was touched.

**Corrections (was → now).**

1. Section B: "eventually fully replace" cited to *Campaign management overview* → it is on *Amazon Ads API v1 overview*; the one-ad-product-per-call and per-product TPS limits are on *Campaign management in the Amazon Ads API* and are stated "At launch", not on the entities overview. Page names fixed (*Campaign management in the Amazon Ads API*, *Campaign management entities*); P-20 and the Pages read table follow.
2. Section B: v1 paths `{create|query|update|delete}` for all six resources → `adExtensions` has no delete; batch "up to 1,000 items" → the schema maximum, with Amazon's note that "Batch size limits are specific to each ad product".
3. Section A: legacy `/adsAccounts*` deprecation cited to the account guides → it is on *Deprecations*; non-global ID `amzn1.ads1.aa1.{country}.{entity}` → `{entityId}`; added that omitting `isGlobalAccountFilter` returns only global accounts. Page name *Query advertiser accounts* → *QueryAdvertiserAccount API developer guide*.
4. Section A: the three identifiers paraphrased under *Getting started* → Amazon's own definitions quoted, page name *Getting started with Amazon Ads API v1*.
5. Section A: door refusal attributed to `door.md` → it is in `SKILL.md`, and names `Authorization`, `Amazon-Advertising-API-ClientId` and `Amazon-Ads-ClientId`.
6. Section B: SP negatives quote "can be set at campaign level and at ad-group level" (not on the page) → the page's own sentence quoted; P-3 follows.
7. Section B: SB ad types "product collection (manual and auto), video, brand video and store spotlight" → the page's current list "manual collection, auto collection, video or store spotlight"; page name *Campaign structure for Sponsored Brands*.
8. Section B: Product Collection "shut off in January 2027" and "a structure that is being moved under them" → create requests mapped from August 2026, create errors after January 2027, support ending February 2027 (release note 2026-09-18), existing campaigns still run and can be edited (release note 2026-07-06). P-43 added.
9. Section B: v1 beta "nearly 200" → the 2025-05-29 note says "over 190"; "nearly 200" is the GA notes' wording; example payloads include Sponsored TV as well as SD.
10. Section B and G: `FULL_FUNNEL` stated as the API side of unBoxed Full-Funnel Campaigns → tagged [seat]; no page links the two.
11. Section C: `marketplaceBudgetAllocation` and `globalCampaignId` listed as SP v3 create fields → they are on the read object `SponsoredProductsCampaign`.
12. Section C: v1 budget "recurrence DAILY" → `recurrenceTimePeriod`, whose enum is DAILY, LIFETIME, MONTHLY.
13. Section C/H: v1 ad group "has no budget field" for SP → the v1 guide marks ad-group `budgets` as DSP-only.
14. Sections D, E, P-8, stable 6: "targetingType is not in the SP v3 update schema" → it is listed there; the rule is the update request's "Note: targetingType cannot be updated", v1 `CampaignUpdate` lacking `autoCreationSettings`, and the bulksheet rule.
15. Section D: product target's ASIN "cannot be swapped" sourced to SP v3 → SP v3 `SponsoredProductsUpdateTargetingClause` does list `expression`; the rule is from bulksheets ("Targeting can only be archived or paused") and v1 `TargetUpdate`, which has no `targetDetails`.
16. Section D, L, P-14, P-27, stable 8: immutability and work-around cited to *Overview about bulksheets* (not on that page) → *Understand which fields can be updated* and *Overview - how to update campaigns with bulksheets*; start date added as fixed in bulksheets.
17. Section E, P-9: auto groups' default bid cited to *Overview about bulksheets*, quote not verbatim → *How to create Sponsored Products campaigns with bulksheets*, quoted.
18. Section L: download options cited to *Overview about bulksheets* → *Get started with bulksheets: Part 1*, with the page's own list (brand assets, SP input guidance added); legacy deprecation date confirmed on *Overview - About bulksheets*.
19. Section D, P-17: v1 delivery reason PORTFOLIO_ENDED → PORTFOLIO_END_DATE_REACHED (PORTFOLIO_ENDED is SP v3's and the Portfolios API's spelling).
20. Section F: target promotion groups "each in v1 and v2 media types" → recommendations has only v1; v2 detail fields described.
21. Section G, P-24, stable 14: PAGE_VISIT "which is CPC" → PAGE_VISIT is the default, with CPC when neither field is sent; BRAND_IMPRESSION_SHARE is VCPM only; page name *Getting started with campaigns* (SB).
22. Section G, P-29: `autoManageCampaign` description attributed to SP v3 and the v1 *Campaign* guide → it is on v1 `AutoCreationSettings` in the merged OpenAPI; SP v3's field has no description; the guide does not list it.
23. Section G: page names *unBoxed 2025: Campaign Manager* → *Campaign Manager beta: One command center for every campaign* (a beta for select advertisers); *unBoxed 2026 news and announcements* → *unBoxed 2026 news: Explore the latest advertising announcements*.
24. Section H, P-16: sharing "up to 100% over their own daily budget from the month's leftovers" → Amazon's words "up to 100% more than their average daily budget on any given day"; PUT `/portfolios` also capped at 100; serving-status list extended.
25. Section H, practitioners 7: Capconvert "Amazon does not publish a maximum number of portfolios" → "does not publish a hard maximum number of portfolios per account".
26. Section I, P-38, Open question 1, run-time list: "no Amazon page was reachable" for entity counts → Amazon's help page *Sponsored ads campaign limits* (G86H2227323T8T4Q, last modified 2026-07-29) was read: 10,000 campaigns, 20,000 ad groups per campaign, 10,000 campaign and ad-group negative keywords (third parties say 1,000), no 500,000-auto-ads figure, and limits raised as accounts approach them. P-42 added; the third-party tables marked superseded where they differ.
27. Section I/J and elsewhere: page name *Limits and constraints* → *Limits, constraints, and quotas*.
28. Section J, P-19: v1 tags "on campaigns and ad groups" → also on targets.
29. Section M: "Exports API is not affected by the reporting deprecation" cited to the exports pages → it is on *Deprecations* (September 2026 notice).
30. Section N, P-25, stable 15, seat position 2: "the comparison behind it … is not given on the page" → the page gives it: "compared to those with less similar products"; full footnote and the 67% wording quoted.
31. Section N: "associated with 321× more sales" → "321 times more likely to generate ad-attributed sales when advertised, compared to products that are not suggested"; the "as many similar products" line is for manual-targeting ad groups; portfolios quote completed ("or any way you choose"), P-26 follows.
32. Section O: SB v3 → v4 dates given without source → attributed to the release note of 2025-10-14 (which revised 2025-04-17), with the 2024-01-31 SB v2/v3 shutoff and the Product Collection dates added.
33. Practitioners: Montero's SD quote "for full placement coverage" (not verbatim) → his sentence quoted; Liquidate "maximizes orders" → "focused solely on optimizing towards conversions"; his campaign-level budget reason added.
34. Practitioners: Capconvert "one tightly related product theme" → "a single, tightly related product theme"; Ad Badger's placement reason quoted; Seller Labs' FAQ on match-type campaigns and its CPC claim added as [opinion].
35. Section D, P-13, stable 7, Open question 3: no page states the cascade outside global campaigns → *How to update Sponsored Products campaigns with bulksheets* states it for SP bulksheets; the API `delete` cascade stays open.
36. Several page names corrected to the pages' own titles: *Creating Sponsored Products ad groups*, *Global campaigns for Sponsored Products*, *Get started with Portfolios*, *Get started with bulksheets for Sponsored Products*, *Amazon Ads API for Sponsored Display overview*.

**Removals.**

1. The quote "Archiving is a permanent action that cannot be undone, while pausing is less permanent", attributed to *Overview about bulksheets* (sections D, L, P-12): not on that page or on any linked bulksheet page, and a web search found it on no Amazon page. Archive's terminality stays sourced by the v1 `State` enum and the Seller Forums staff reply.
2. The bulksheets FAQ on the Sites field with its archive-and-copy recipe (sections D, L): not found on any bulksheet page read. The Sites column's values from the create guide replace it; `siteRestrictions`' immutability stays sourced by SP v3.
3. The claim that Amazon's +6% comparison "is not given on the page" (section N, seat position 2): the page gives it.

**Pages that stayed unreachable.** Helium 10 knowledge base Adtomic article (HTTP 403 again); the Rutz, Bucklin and Sonnier (2012) and Rutz and Bucklin (2011) PDFs (fetched; no local tool could extract text); the IDEAS JMR record, the EconBiz record and the INFORMS Abhishek page (not re-tried: no claim depends on them beyond search-summary abstracts already marked as such). The two Amazon Ads help pages the research seat listed as unreachable were read (see Corrections 26). An adbrew help page searched for self-competition returned HTTP 401 and is not cited. Self-competition (Open question 2) found only vendor claims of an Amazon statement, with no Amazon page.

### Gap fill 2026-11-09

The research seat re-opened every page used below by plain GET (Amazon API guides through their markdown copies on `d3a0d0y2hgofx6.cloudfront.net`, OpenAPI models on the public CloudFront hosts, Amazon Ads help pages through the article text embedded in their HTML, practitioner pages and Crossref metadata) and called no Ads API, Login with Amazon, MCP, SP-API or Seller Central help-hub host. No seller data was touched. 45 pages-read rows were added.

**Gaps added.**

1. **SB v4 multi-ad group model** (gap 1) — added to section B: several ad groups and ads, one ad type and one targeting kind per ad group, no ad-group bid, per-ad moderation, side-by-side creative testing; limits (no Amazon SB-specific count found; Perpetua's SB table recorded as [opinion]); how legacy campaigns differ (read-only ad groups, no `adId`, `INVALID_ARGUMENT`, feature table); the `isMultiAdGroupsEnabled` reporting gap; the 2023 storage change; and the legacy migration (new campaign ID, `legacyCampaignId` tag, start-date reset, no performance carryover, three different published deadlines). Stable 17–18; run-time SB reads; P-44 to P-48; Open questions 14–16.
2. **Placement isolation** (gap 2) — added as *What practitioners add* section 8, with Amazon's documented mechanism (help GYYZVM7LGSRYGWV5; the 2024 rest-of-search control) and authors for (Helium 10 Team 2019, Feedvisor, Perpetua, Ad Badger 2020 and 2023) and against or limiting (Ad Badger 2023 on very low base bids, m19 2026). Pacvue's moderate-base-bid argument stays a search summary: its pages answered 403 and the archive copy could not be fetched (Unreachable). Stable 20; P-54, P-55.
3. **Which ASIN to advertise** (gap 3) — added to section N (Amazon's gates, product labels and figures, `POST /product/metadata` with `SUGGESTED`, the ASIN matrix, standard-ASIN guide, SB collections "not variations") and *What practitioners add* section 9 (m19, Karooya, Canopy, Scale Insights). What the ad shows for one advertised child is not stated on any Amazon page read and is Open question 13; the gap's description stands. Stable 19; run-time product reads; P-50 to P-53.
4. **Measuring a restructure** (gap 4) — added as *What practitioners add* section 10 and *Published research* items 7–8: Ad Badger's "learning loop" claim recorded as a claim about every change, with the explicit note that no Amazon page read documents a per-campaign learning state; Meressa's "30 conversions" claim set against Amazon's documented 10-conversion rule-based bidding eligibility; Xue et al. re-read in full text (per-ad-item history features; the word "campaign" absent); the Simpson/Bickel aggregation reversal and Ang's LMDI. One correction to the gap's wording: `spSearchTerm` has no advertised-ASIN column, so the ASIN × query unit is built by joining each ad group's product ads, exact only for single-ASIN ad groups; SQP supplies the per-ASIN query totals. Stable 22–23; run-time restructure reads; P-57 to P-59; Open question 18.

**Contradictions settled.**

1. **Product Collection dates** (contradictions 1 and 3) — re-opened *Deprecations*, the 2026-09-18 release note, and two pages not read before: the API *Product Collection Migration Guide* and Amazon help GV7N6KZTH4HF4T2P (last modified 2026-10-05). Both dates are Amazon's and name different ends: January 2027 is the API create shutoff ("Final shutoff. All API requests to create Product Collection ads will be rejected with an error"); February 2027 is the end of support for existing Product Collection ads, with eligible 3-ASIN ads moved automatically to manual collections and ads with fewer than 3 ASINs not auto-migrated. Creates have been mapped to Manual Collection since August 2026. This file now states both with their meanings (section B, section O, P-43, stable 24). Files that give one date only (`areas/seasons-and-deals.md`, `areas/diagnosis.md`, `areas/keyword-and-product-targeting.md`) should carry both with these meanings; the owner is `method/ads-api-surface.md`, which records both dates but not yet which end each names.
2. **Global account ID source** (contradiction 2) — re-opened *Deprecations* and the 2026-07-20 release note: all six legacy account endpoints, including `POST /adsAccounts/list` and `GET /adsAccounts/{accountId}`, return `Warning: 299` since July 2026, are blocked for new client integrations (existing callers only through an allowlist), and return 404 from July 2027; the named replacement for retrieval and listing is `POST /adsApi/v1/query/advertiserAccounts`. This file's section A, section O, run-time list and P-49 now say so in full. `method/reporting.md`'s run-time reads of `/adsAccounts*` conflict with these sources; the owner is `method/ads-api-surface.md`.
3. **Self-competition** (contradiction 4) — re-opened help GHTRFDZRJPW6764R and the targeting guide: the match-type case is answered ("the match type with the highest bid will be used for any matching shopping query"; "you won't be bidding against yourself by adding different match types on the same keyword"). Neither page says whether that holds across ad groups or campaigns, nor covers two copies of one keyword in the same match type, keyword against auto or product targets, or the bid stage compared. *What practitioners add* section 5 and Open question 2 now record the answered part and the open remainder; stable 21; P-56. `method/change-measurement.md`'s Open question 3 is right for same-match-type duplicates and should cite the match-type rule for the rest; the owner is `areas/keyword-and-product-targeting.md`.

**Declined.** None of the four gaps was wrong on the facts. Two of their premises were narrowed: gap 3's "how Amazon shows the family when one child is advertised" has no Amazon answer on any page read (only Karooya's description), and gap 4's "account-wide `spSearchTerm`" cannot alone give the ASIN-and-query unit (no ASIN column).

**Corrections made in passing.** Section B's SB line "one ad type per ad group" kept, with the structure guide's mixed manual and automatic collection example noted as a [seat] reading; the Helium 10 2019 arithmetic ($3.60, "up to 1,800%") and the Ad Badger 2020 and m19 2026 statements that rest of search has no adjustment are flagged against Amazon's current pages; Published research item 6's heading "Amazon's own" is qualified (the paper does not name the shop).

