# The Ads API surface cx reaches

Read 2026-11-09 by the research seat.

Tags: [official] is an Amazon page, cited by page name and URL and read 2026-11-09 unless another date is given. Amazon Ads API pages are cited by their guide name. Each was read as the markdown copy Amazon's own docs site loads, at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`, or as the OpenAPI model listed in Amazon's `contracts.json`. [opinion] is a named practitioner, vendor or developer, with the person or firm given; a GitHub field report is cited by login and issue number. [research] is a paper or working paper. [seat] is this seat's own reading and is never a position. Figures (limits, batch sizes, day counts, dates) are recorded with page and date **for human readers only**. A skill reads the live figure at run time from the operation named in *What cx must read at run time*.

## What this covers

This file maps the Amazon Ads API as it stands on 2026-11-09, as far as a seller's agent can reach it through ComChatX's open door, `cx raw amazon-ads` (the package `cx-amazon-ads`, whose reference is `door.md`). The door carries any method, path, query, header and body to one of the three regional Ads API origins. It attaches the seller's access token and ComChatX's client id, and lands Amazon's reply as Amazon gave it. So the question for each API family is: what is it, what host and headers does it need, what does it accept and answer, and what in it the door cannot do.

It covers:

- the families and their hosts: profiles and accounts, portfolios, Sponsored Products v3, Sponsored Brands v4 (and the v3 paths that remain), Sponsored Display v3;
- Ads API v1, the unified create/update/query/delete surface: its release dates, which ad products it covers, and its limits at launch;
- recommendations of every kind: keywords, products, categories, bids, budgets, campaigns, tactical recommendations and the v1 Recommendations API;
- budget usage, budget rules, optimization rules, eligibility, moderation, product metadata, change history and exports;
- Brand Metrics, Stores insights and Amazon Attribution;
- Amazon Marketing Cloud (separate access) and Amazon Marketing Stream (needs an AWS destination);
- test accounts and the retired sandbox, and the Amazon Ads MCP server;
- write semantics: 207 multi-status, partial success, idempotency, and archived as a final state;
- state enums and id formats;
- rate limits and 429 handling;
- user permissions, permission scopes and manager accounts;
- seller, vendor and agency accounts;
- regional endpoints and marketplaces;
- deprecations and sunsets from 2025 to 2027;
- what the door does not name or cannot do, as follow-ups for `cx-amazon-ads`;
- added in the gap fill of 2026-11-09: the audience families (Audiences discovery, Targetable Entities, the v1 beta audiences and audience categories, audience overlap insights) that SP and SB audience bid adjustments and SD audience targets draw their ids from; the creative asset library and the SB v3 Store asset and media operations; Stores, brands and brand identifiers beyond `GET /pageAsins`; the Localization API; Sponsored Brands reserve share of voice (v1 deals, pricing and keyword-reservation validation); v1 promotion offers and rewards; the Events API; the measurement families (Brand Lift and other DSP studies, Brand Metrics, MMM, Amazon Attribution, AMC administration) with their paths; whether any experiment or holdout operation exists for sponsored ads; and the terms that bind a client application (Amazon Ads API License Agreement, Ads API policies, Partner Network Policies, and the SP-API Data Protection and Acceptable Use Policies for the sibling SP-API package).

It stays in its lane. It describes the surface, not the advertising decisions made on it. Those are owned by:

- what each campaign shape is for: `areas/campaign-structure.md`;
- keyword, product and category targets and match types as a matter of practice: `areas/keyword-and-product-targeting.md`;
- harvesting and negating search terms: `areas/search-terms-and-negatives.md`;
- bids, bid strategies and placement adjustments: `areas/bids-and-placements.md`;
- budgets, budget rules as a practice, and out-of-budget: `areas/budgets-and-pacing.md`;
- events and deal calendars: `areas/seasons-and-deals.md`;
- organic and total sales: `areas/ads-organic-and-total.md`;
- why an ad does not deliver, read from delivery reasons and eligibility: `areas/diagnosis.md`;
- launching an ASIN: `areas/launch.md`;
- which ad products a seller may run, and their eligibility rules: `beyond/ad-products-and-eligibility.md`;
- metrics and attribution windows: `beyond/metrics-and-attribution.md`;
- goals and unit economics: `beyond/goals-and-economics.md`;
- brand defense: `beyond/brand-defense-and-competition.md`;
- Amazon's own automation (rule-based bidding, budget rules, Ads Agent) as a practice: `beyond/automation-and-amazon-tools.md`;
- reports, their columns, retention and lifecycle: `method/reporting.md`;
- measuring the effect of a change: `method/change-measurement.md`.

Where this file names a reporting or Stream operation, it is for the surface (host, account id, limits, sunset). The content of reports belongs to `method/reporting.md`.

A note on method. The Amazon Ads API docs site (`advertising.amazon.com/API/docs/en-us/...`) serves a JavaScript shell. Its `server-config` meta names `d3a0d0y2hgofx6.cloudfront.net`, and every guide is served there as markdown. Every OpenAPI model is listed in `https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json`. Both were read by plain GET. No Ads API host (`advertising-api*.amazon.com`), Login with Amazon host, MCP endpoint or SP-API host was called. Web search was not available to this seat for this file (its budget was exhausted in the session), so practitioner sources come from known URLs fetched directly: GitHub, Airbyte and Fivetran connector docs.

## Amazon's own rules and guidance

Each subsection marks what Amazon states as a requirement of the API (RULE) and what it advises (GUIDANCE). A RULE here is a behaviour or constraint the API documents: an enum, a limit, a status code, a date. A GUIDANCE is a recommendation in Amazon's own words.

### A. The map: hosts, regions and marketplaces

**RULE.** The Ads API has three regional hosts. Amazon's *API overview* page (`reference/api-overview`) lists them, each with its marketplaces:

| Region | Host | Marketplaces (country codes as Amazon lists them) |
|---|---|---|
| North America | `https://advertising-api.amazon.com` | US, CA, MX, BR |
| Europe | `https://advertising-api-eu.amazon.com` | UK, FR, IT, ES, DE, NL, AE, PL, TR, EG, SA, SE, BE, IN, ZA |
| Far East | `https://advertising-api-fe.amazon.com` | JP, AU, SG |

[official] *API overview*, https://advertising.amazon.com/API/docs/en-us/reference/api-overview, read 2026-11-09.

**RULE.** Data is regional. The Well-Architected Framework defines regions this way: "The Amazon Ads API operates in three regions: North America (NA), Europe (EU), and Asia (FE), each with its own endpoint. Data for each region is exclusively accessible through its corresponding endpoint." [official] *Amazon Ads Well-Architected Framework: Fundamental component*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-ads-well-architected-framework/fundamental-component, read 2026-11-09.

**RULE.** `GET /v2/profiles` on a host returns only that region's profiles. The *Profiles* guide, under "Regions": "The Profiles resource returns *only* those profiles whose marketplace falls within the region covered by the API host to which the call is addressed." A `profileId` from another region "does *not* provide authorization for other operations on the host", and the call is answered "`4XX - Unauthorized`". [official] *Profiles*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles, read 2026-11-09. The DSP global-seat release note says the same for global manager accounts: "The Calling Profiles API returns only the Profile ID of the manager account for the regional endpoint you are calling." [official] *Release notes*, "Register once and manage ads worldwide with a global seat" (2025-04-09), https://advertising.amazon.com/API/docs/en-us/release-notes/index, read 2026-11-09.

**Ireland.** Ireland (IE) is not in the endpoint table, but it appears elsewhere in Amazon's own pages:

- The Profiles model's `countryCode` enum includes `IE`. Its region table reads "|EU|IE|Ireland|", its currency table "|EU|IE|Ireland|EUR|", and its time-zone table gives `Europe/Dublin`. [official] *Profiles* OpenAPI model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml, read 2026-11-09.
- The bid table on *Limits, constraints, and quotas* has an `IE` row: SP 0.02/1000 EUR, SD "NA". [official] *Limits, constraints, and quotas*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, read 2026-11-09.
- The portfolio unspent-budget-sharing release note lists Ireland among its European countries. [official] *Release notes*, "Automatically share unspent campaign budget with budget exhausted campaigns in a portfolio - updated" (2025-07-19), read 2026-11-09.

The endpoint table on *API overview* has no IE row, and neither does the door's origin table (see *What the door does not name or cannot do*). Nor does the URL-prefix table on *Make your first call*. The Profiles model's own table assigns IE to region `EU`, and the *Profiles* guide says each host returns the profiles of its region. [seat] Read together, an IE profile is listed by the EU host. No Amazon page read here says so in one sentence.

**Marketplace ids.** The Ads API names marketplaces in two ways:

- by country code (`US`, `UK`, `DE` …) in the Profiles model, in v1 `marketplaces` arrays and in limits tables;
- by `marketplaceStringId` (for example `ATVPDKIKX0DER` for US) in `accountInfo` and in AMC headers.

The UK is spelled two ways. The Profiles model's `countryCode` enum has `UK`. The v1 models' `Marketplace` enum (23 values in the cross-product production model) and `CountryCode` enum have `GB` and no `UK`, and so do the v1 beta audience, promotion-offer and brand-store filters. [official] *Profiles* OpenAPI model; *Amazon Ads API v1* model (`AmazonAdsAPIALL_prod_3p.json`); *Amazon Ads API v1 betas* model (`AmazonAdsAPIALLMerged_prod_3p_BETA.json`); read 2026-11-09. Stream v2's and the global account's alternate ids also carry country codes.

**Time zones.** Each profile carries a `timezone`. The Profiles model lists the zone per country (for example US, CA and MX profiles read `America/Los_Angeles`). Report dates and budget days follow the profile's zone. Fivetran's connector page states the same thing from the consumer side: "Amazon Ads uses the time zone set by the profile to request the report." [official] *Profiles* OpenAPI model, read 2026-11-09. [opinion] Fivetran, *Amazon Ads connector*, https://fivetran.com/docs/connectors/applications/amazon-ads, read 2026-11-09.

### B. Authorization: Login with Amazon, scopes, tokens and headers

**RULE.** Authorization is Login with Amazon (LwA) OAuth 2.0. There are three token hosts:

| Region | Token URL |
|---|---|
| NA | `https://api.amazon.com/auth/o2/token` |
| EU | `https://api.amazon.co.uk/auth/o2/token` |
| FE | `https://api.amazon.co.jp/auth/o2/token` |

The page states: "The resulting tokens are valid globally across all regions." [official] *Authorization grants*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/authorization-grants, read 2026-11-09.

**RULE.** Access tokens.

- "Access tokens are valid for 60 minutes."
- They begin `Atza|` and are at most 2048 bytes.
- The refresh token begins `Atzr|`.

[official] *Access tokens*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/access-tokens; *Refresh tokens*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/refresh-tokens; both read 2026-11-09.

**RULE.** Refresh-token expiry from 2026-07-30. Verbatim: "**Effective July 30, 2026**, refresh tokens issued for Amazon Ads API advertising scopes expire 365 days from the date of advertiser consent. Refresh tokens issued before July 30, 2026 are not affected by this change and continue to function as before. They remain valid indefinitely until the advertiser revokes authorization or another invalidation condition occurs." The release note "Refresh Token Expiration Policy Update" (2026-05-26) announced it. Airbyte's connector page adds that using or refreshing the token does not extend it.

- An invalid refresh token is answered `400` with `"error": "invalid_grant"`. The page lists the causes: the 365-day expiry, revocation by the advertiser, removal of the application, changed or deleted LwA application credentials, and "suspicious activity associated with the token".
- No Ads API page read here documents `invalid_client`. It is named in `door.md` as the reply to a wrong client pair, and the *Generate access and refresh tokens* page points to LwA's own error list for the rest.

[official] *Refresh tokens*, read 2026-11-09; *Release notes* (2026-05-26), read 2026-11-09; *Getting started - Generate access and refresh tokens*, read 2026-11-09. [opinion] Airbyte, *Amazon Ads source connector*, https://docs.airbyte.com/integrations/sources/amazon-ads, read 2026-11-09.

**RULE.** Scopes.

- `advertising::campaign_management` is the scope for sponsored ads and nearly every family in this file.
- `advertising::audiences` is for Data Provider.
- `advertising::test:create_account` is for creating test accounts (section U).

An Amazon docs contributor (GitHub `jerirose`, CONTRIBUTOR on `amzn/ads-advanced-tools-docs`) explained the distinction between a scope and a permission in issue #406 (2025-09-19). The **scope** belongs to the LwA application. The **permission** (for example `amazon_stores_edit`) belongs to the Amazon Ads user account. "By using the `advertising::campaign_management` scope in the auth grant URL, your client application is requesting authorization to use _any_ advertising permission that is available to the Amazon Ads user account." So a permission cannot be added to a client. [official] *Authorization grants*; *Test accounts: Authorization for test accounts*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/authorization-for-test-accounts; read 2026-11-09. [opinion] `jerirose` (Amazon Ads docs contributor), GitHub `amzn/ads-advanced-tools-docs` issue #406, https://github.com/amzn/ads-advanced-tools-docs/issues/406, read 2026-11-09.

**RULE.** Headers.

| Header | What it carries | Where it is required |
|---|---|---|
| `Authorization: Bearer <access token>` | The LwA access token | Every call |
| `Amazon-Advertising-API-ClientId` or `Amazon-Ads-ClientId` | The LwA client id | Every call. Amazon's pages use both names. `Amazon-Ads-ClientId` is the name on *Make your first call* (its header table: "Yes"), *Getting started with Amazon Ads API v1*, *QueryAdvertiserAccount API*, the v1 Recommendations *How to* and the MCP pages. `Amazon-Advertising-API-ClientId` is the name in the *Profiles* guide and model (`required: true`), the *Reporting API v1* quickstart and *Limits and best practices*. |
| `Amazon-Advertising-API-Scope` | A `profileId` | Sponsored ads campaign management and most sponsored ads calls; not `/v2/profiles` |
| `Amazon-Ads-AccountId` | An advertising account id (global, DSP, or AMC instance in MCP) | *Make your first call*: "Required for reporting and cross-product operations"; v1 getting started: "Required for ADSP and cross-product requests"; the v1 Recommendations list |
| `Amazon-Ads-Manager-AccountId` | A manager account id | Calls made through a manager account |
| `Accept`, `Content-Type` | Versioned media types such as `application/vnd.spCampaign.v3+json` | Sponsored Products v3, SB v4 and others name them per operation |

The *Profiles* guide: "If the `Amazon-Advertising-API-Scope` header is not included or is incorrect, a `401 Unauthorized` or `400 Bad Request` response is returned." The *Errors* page lists `401 - Scope header is missing`, `401 - No matching advertiser found for scope`, and `401 - Not authorized to access scope` ("Not authorized to manage this profile. Please check permissions and consent from the advertiser."), separately from `403 - Forbidden` ("user does not have access to a specified resource"), `406` (unsupported `Accept`), `415` (unsupported `Accept` or `Content-Type`) and `422`. The *Permissions* guide: "Requests will receive a `401 Unauthorized` response if the authorizing account does not have the required permissions." [official] *Make your first call*, https://advertising.amazon.com/API/docs/en-us/guides/get-started/first-call; *Getting started with Amazon Ads API v1*, https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/getting-started; *Profiles*; *Error responses and error status codes*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/errors; *Permissions*; all read 2026-11-09.

**RULE.** API access is applied for. A developer applies through the onboarding flow, and an approved LwA client is the precondition for every family. The onboarding pages state the review time ("up to 1 business day" is the figure in Amazon's page as read). GitHub field reports in 2026 describe approvals pending for weeks; one quotes a "Registration Request Pending" email promising a reply "within three business days" (see *What practitioners add*). [official] *Onboarding: Apply for access*, https://advertising.amazon.com/API/docs/en-us/guides/onboarding/apply-for-access; *Onboarding overview*, https://advertising.amazon.com/API/docs/en-us/guides/onboarding/overview; read 2026-11-09.

### C. Profiles, advertiser accounts and account identifiers

**RULE.** A profile is one advertising account in one marketplace.

- `GET /v2/profiles` takes no Scope header and returns at most 5000 items.
- Each item has `profileId`, `countryCode`, `currencyCode`, `dailyBudget`, `timezone` and `accountInfo`.
- `accountInfo` holds:
  - `marketplaceStringId`;
  - `id` (the model warns it is "not unique and may be the same across marketplace");
  - `type`: `seller`, `vendor` or `agency`;
  - `name`;
  - `subType`: `KDP_AUTHOR` or `AMAZON_ATTRIBUTION`;
  - `validPaymentMethod`, for vendors only.

[official] *Profiles* OpenAPI model, read 2026-11-09; *Profiles*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles, read 2026-11-09.

**RULE.** The profiles list's query parameters (Profiles model):

- `apiProgram`: one of `billing`, `campaign`, `paymentMethod`, `store`, `report`, `account`, `posts`; default `campaign`.
- `accessLevel`: `edit` or `view`; default `edit`. The default hides profiles the user can only view.
- `profileTypeFilter`: `seller`, `vendor`, `agency`.
- `validPaymentMethodFilter`.

Airbyte's connector changelog (8.1.3) records switching to `accessLevel=view` so that view-only accounts appear. [official] *Profiles* OpenAPI model, read 2026-11-09. [opinion] Airbyte, *Amazon Ads source connector*, read 2026-11-09.

**RULE.** An account with no campaign returns no profile. The Profiles model's description of the list says it "does not return a response unless the current account has created at least one campaign using the advertising console". [official] *Profiles* OpenAPI model, read 2026-11-09.

**RULE.** `PUT /v2/profiles` updates a profile's `dailyBudget`, for sellers, for Sponsored Products only. [official] *Profiles* OpenAPI model, read 2026-11-09.

**RULE.** Account types and what they serve (*Profiles* guide and model):

- **Seller** and **vendor** accounts run Sponsored Products, Sponsored Brands and Sponsored Display. Sponsored Brands and Sponsored Display need Brand Registry. (Eligibility in detail belongs to `beyond/ad-products-and-eligibility.md`.)
- **Agency** profiles serve Amazon DSP and Data Provider only ("Agency accounts are used with the DSP and Data Provider APIs only").
- A profile can carry `accountInfo.subType` `KDP_AUTHOR` or `AMAZON_ATTRIBUTION`. The model gives the enum without saying which `type` goes with each.

Airbyte's wording: the connector "supports only profiles with seller and vendor type, profiles with agency type will be ignored."

[official] *Profiles*; *Profiles* OpenAPI model; read 2026-11-09. [opinion] Airbyte, read 2026-11-09.

**RULE.** Global accounts and v1 account ids. Ads API v1 names an advertiser by an account id, not by a profile. The formats in Amazon's guides:

| Identifier | Format | Where |
|---|---|---|
| Global account | `amzn1.ads-account.g.<id>` | v1 reporting, v1 recommendations, Stream v2, AMC for global accounts |
| Non-global (regional) advertiser account | `amzn1.ads1.aa1.<country>.<entityId>` | Advertiser accounts API |
| Entity id | `ENTITY…` | `alternateIds`; Brand Metrics and Stores `brandEntityId` contexts |
| Manager account | `amzn1.ads1.ma1.<id>` | Manager accounts; not accepted by Stream v2 |
| Profile id | Numeric string | `Amazon-Advertising-API-Scope`; the v3 product APIs |
| DSP advertiser | Numeric | DSP, Stream v2, v1 reporting |

`POST /adsApi/v1/query/advertiserAccounts` returns, per account, `alternateIds` that tie the global id to each marketplace's `profileId`, `entityId`, `countryCode`, `dspAdvertiserId` and `region`. A release note of 2026-07-10 says `businessDetails` is returned only when a single account is queried. The Advertiser Account Management APIs (create, query, update) became generally available on 2026-06-18, "open to all Amazon Ads API customers with an approved LwA client". [official] *Query advertiser accounts*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/query-advertiser-accounts; *Account registration*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/registration; *Release notes* (2026-06-18, 2026-07-10); *Amazon Ads API v1 merged (prod and beta)* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json, which holds `/adsApi/v1/{create,query,update}/advertiserAccounts`; read 2026-11-09. (The *Advertising accounts* model at `dtrnk0o2zy01c.cloudfront.net/.../AdvertisingAccounts_prod_3p.json` is the legacy `/adsAccounts` surface, not the v1 one.) The 2025-07-15 closed-beta note also lists `POST /adsApi/v1/query/sellingAccounts`, which returns the Seller, Vendor, Author or KDP selling accounts a user can reach, as an encrypted token for registering an advertiser account. [official] *Release notes*, "Account registration API now available in closed beta" (2025-07-15), read 2026-11-09.

**RULE.** A Seller Central id is not an advertiser id. Stream v2's *Create a subscription* page: "Other identifiers are **not** accepted — including a **manager account** ID (`amzn1.ads1.ma1.*`) and selling-partner IDs such as a **Seller Central account ID** (MCID, e.g. `A6DEQ9LYHIBE8`) or a **Vendor Group** ID … A selling-partner ID identifies a Seller or Vendor account, not an advertiser account; use the advertiser's Global Account ID (`amzn1.ads-account.g.*`) instead." [official] *Stream v2: Create a subscription*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/create-a-subscription, read 2026-11-09.

**RULE.** Legacy account APIs are deprecated. The release note "Deprecation of legacy account management APIs" (2026-07-20) and the *Deprecations* page set the dates:

- `/adsAccounts*` and `/dsp/advertisers*` are deprecated from July 2026. Responses carry `Warning: 299` headers, and new integrations are blocked ("Existing callers continue to function through an allowlist until the shutoff date").
- They answer 404 from July 2027.
- The replacement is the v1 advertiser accounts surface.

The *Deprecations* entry "July 2026 - Deprecation of legacy account management APIs", re-read 2026-11-09, names the six endpoints exactly: `GET /dsp/advertisers`, `GET /dsp/advertisers/{advertiserId}`, `POST /adsAccounts`, `POST /adsAccounts/batch`, `GET /adsAccounts/{accountId}`, `POST /adsAccounts/list`. It names the replacements: account creation `POST /adsApi/v1/create/advertiserAccounts`, and "Account retrieval and listing: `POST /adsApi/v1/query/advertiserAccounts`". The notes read verbatim: "Starting July 2026, all six legacy endpoints return `Warning: 299` response headers indicating deprecation." "Starting July 2026, new client integrations are blocked. Existing callers continue to function through an allowlist until the shutoff date." "Beginning July 2027, requests to these endpoints will return `HTTP 404 Not Found`." [seat] A file that reads the global account id from `POST /adsAccounts/list` or `GET /adsAccounts/{accountId}` names a path that a client new since July 2026 is blocked from. The operation Amazon names for retrieval is `POST /adsApi/v1/query/advertiserAccounts`.

[official] *Release notes* (2026-07-20); *Deprecations*, https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations; read 2026-11-09.

**RULE.** Average daily budget at account level. The account-budget settings are `GET /accountBudgets/featureFlags` and `POST /accountBudgets/featureFlags`. The guide: "The default average daily budget setting is 100% of the daily budget"; an account can "revert to 25%" with the `POST`. [official] *Average daily budget*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/average-daily-budget, read 2026-11-09. (What the setting does to pacing belongs to `areas/budgets-and-pacing.md`.)

### D. Permissions, user roles and manager accounts

**RULE.** The console grants each user a tier of **Viewer**, **Editor** or **Admin** on an advertising account, and finer permissions under it. The *Permissions* guide maps console permissions to API permission names:

- Campaign manager: `advertiser_campaign_view` and `advertiser_campaign_edit`;
- Advertising reports: `nemo_report_view` and `nemo_report_edit`;
- Stores builder: `amazon_stores_edit` only (the page's View column reads "N/A");
- Billing history: `nemo_transactions_view` and `nemo_transactions_edit`.

(The *Stores* model's operations nevertheless list `amazon_stores_view` among their accepted permissions, section Q.)

Payment-settings and user-management permissions do not affect the API. Sellers manage these permissions in Seller Central, where they are named for the console's sections:

- Campaign manager;
- Product Ads Performance Reports;
- Product Ads Invoice History;
- Stores builder.

[official] *Permissions*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/permissions, read 2026-11-09.

**RULE.** Every operation states the permissions it needs. Operation descriptions in the OpenAPI models read "Requires one of these permissions" followed by a list. The permission strings seen across the models include:

- `advertiser_campaign_edit` and `advertiser_campaign_view`;
- `campaign_edit` and `campaign_view`;
- `dsp_campaign_*` and `campaign_proposed`;
- `MasterAccount_Manager` and `MasterAccount_Viewer`;
- `amc_edit` and `amc_view`;
- `reports_edit` and `reports_view`;
- `account_edit` and `account_view`;
- `user_edit` and `manage_users`.

In the Sponsored Products model, most reads list `advertiser_campaign_edit` and `advertiser_campaign_view`. Writes list `advertiser_campaign_edit`, often with `campaign_proposed`. A few list operations list edit and `campaign_proposed` rather than view. [official] *Sponsored Products* OpenAPI model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json; *Amazon Ads API v1* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALL_prod_3p.json; read 2026-11-09.

**RULE.** Manager accounts (*Manager accounts* guide; *Manager account* model):

- A manager account links advertising accounts with Editor or Viewer access per link.
- A Viewer link answers 401 on edits.
- `GET /managerAccounts` returns up to 50 linked accounts per manager account.
- Associating requires that "the user account associated with the access token must have admin access to both the advertiser account and the manager account."
- "Manager accounts can accept linked accounts in any marketplace", but "In the API, the manager account will only have access to a given linked account when calling the API host in the region of the linked account."
- `GET /profiles` also returns the accounts that gave **Editor** permission to a manager account owned by the authorized user.

[official] *Manager accounts*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/manager-accounts; *Manager account* model, https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json; read 2026-11-09.

**RULE.** A v1 Manager Account API went generally available on 2026-08-12: `POST /adsApi/v1/create/managerAccounts`, `/adsApi/v1/update/managerAccounts` and `/adsApi/v1/query/managerAccounts`, "open to all Amazon Ads API customers with an approved LwA client". [official] *Release notes*, "Manager Account API now generally available" (2026-08-12); *Amazon Ads API v1 merged* model; read 2026-11-09.

**RULE.** The API can do only what the authorizing user can. The `advertising::campaign_management` scope reaches whatever the authorizing user's permissions allow (section B). A grant from a Viewer user lists profiles only under `accessLevel=view`, and that user's writes are answered 401. [official] *Permissions*; *Profiles* OpenAPI model; read 2026-11-09. [opinion] `jerirose`, issue #406, read 2026-11-09.

### E. Ads API v1: unified campaign management

**RULE.** What it is. *Amazon Ads API v1 overview*: v1 standardizes "API behavior across Sponsored Products, Sponsored Brands, Sponsored Display, Sponsored Television, and Amazon DSP. If you are just starting out using Amazon Ads APIs, we highly recommend using these v1 APIs. They will eventually fully replace the ad product-specific APIs." [official] *Amazon Ads API v1 overview*, https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview, read 2026-11-09.

**RULE.** Release dates, from Amazon's release notes:

| Date | Event |
|---|---|
| 2025-05-29 | "Amazon Ads Campaign Management API (beta) is now available" |
| 2025-08-01 | "Campaign management API now available for Sponsored Products, Sponsored Brands, and Amazon DSP"; its body already announces "worldwide general availability" for the three |
| 2025-11-11 | "New reporting API now in open beta" |
| 2025-12-01 | "Unified APIs: Campaign Management API now generally available" |
| 2026-09-30 | Reporting v1 and Marketing Stream v2 generally available; v3 reporting, Sponsored Ads v2 reporting and Stream v1 set to stop 2027-06-30 |

- The 2025-08-01 note: "Previously, there were nearly 200 separate variations of create, read, update, and delete endpoints that will be reduced to 16 with this launch. … Today, we announce the completion of Sponsored Products, Sponsored Brands, and Amazon DSP for worldwide general availability. All of our ad products will be available through the Amazon Ads Campaign Management API, including Sponsored Display and Sponsored TV later in 2025." The 2025-12-01 note repeats the first two sentences and ends "and we will have Sponsored Display and Sponsored TV later this year."
- The current campaign-management overview and example payloads include `SPONSORED_DISPLAY` and `SPONSORED_TELEVISION` entities, and Amazon publishes per-product v1 specifications for SP, SB, SD and STV.
- No release note read here announces SD or STV general availability on v1 by name. Both the *Campaign management overview* and the description of the v1 contract in Amazon's `contracts.json` read: "The Amazon Ads API currently supports campaign management operations for:" followed by a list of Amazon DSP, Sponsored Brands, Sponsored Products, Sponsored Display and Sponsored Television.

[official] *Release notes: Ads API v1*, https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v1; *Release notes* index; *contracts.json*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json; *Campaign management overview*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview; read 2026-11-09.

**RULE.** Entities and paths. Every v1 campaign-management operation is a `POST`:

- `/adsApi/v1/create/{campaigns|adGroups|ads|targets|adAssociations}`
- `/adsApi/v1/update/{…}`
- `/adsApi/v1/query/{…}`
- `/adsApi/v1/delete/{…}`
- `adExtensions` as well, for SP prompt and video extensions.

A keyword is a target (`targetType: KEYWORD`). Queries take a required `adProductFilter` (the only `required` field of `QueryCampaignRequest`) and page with `nextToken`. The cross-product production model has 23 paths; there is no `delete/adExtensions`. [official] *Campaign management: Entities overview*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/overview; *Campaign*, *Ad group*, *Ad*, *Target*, *Ad association* entity pages under `guides/campaign-management/entities/`; *Amazon Ads API v1* model; read 2026-11-09.

**RULE.** One ad product per call at launch. Verbatim from *Campaign management overview*, "Current limitations":

- "At launch, calls will be bound to one ad product at a time."
- "At launch, API rate limits (TPS) will be per each ad product."

After launch, Amazon says, it will "Enable support for multi-ad product operations in the same payload and move rate limiting to payload level". [official] *Campaign management overview*, read 2026-11-09.

**RULE.** Batch sizes differ by ad product. They are in the per-product v1 specifications (`maxItems` on request arrays and `maxResults` on queries), read 2026-11-09 and **for human readers only**:

| Ad product | create / update / delete per call | query `maxResults` |
|---|---|---|
| Sponsored Products | 1000 for campaigns, ad groups, ads and targets; ad extensions 50 | 1000 |
| Sponsored Brands | 10 for campaigns, ad groups and ads; 1000 for targets | 100 for campaigns, ad groups and ads; 5000 for targets |
| Sponsored Display | 100 for campaigns, ad groups and ads; 1000 for targets | 100; 5000 for targets |

[official] *Amazon Ads API v1, Sponsored Products* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISP_prod_3p.json; *…SB* (`AmazonAdsAPISB_prod_3p.json`) and *…SD* (`AmazonAdsAPISD_prod_3p.json`) at the same path; read 2026-11-09. The STV specification (`AmazonAdsAPISTV_prod_3p.json`) answered 403 and was not read.

**RULE.** Budgets in v1. A campaign's budget is a list: `budgets: [{ budgetType: "MONETARY", budgetValue: { monetaryBudgetValue: { monetaryBudget: { value } } }, recurrenceTimePeriod: "DAILY" }]`, in the profile's currency. [official] *Campaign*; *Example payloads*, https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/example-payloads; read 2026-11-09.

**RULE.** Example shapes from *Example payloads*:

- A campaign create carries `adProduct`, `name`, `state`, `marketplaceScope`, `marketplaces`, `startDateTime`, `budgets` and, for an auto campaign, `autoCreationSettings.autoCreateTargets`.
- A target bid update is `{"targets":[{"targetId":"…","bid":{"bid":10}}]}`.
- A delete is `{"campaignIds":[…]}`.

[official] *Example payloads*, read 2026-11-09.

**RULE.** Ids are strings in v1. Sponsored Products v1 ids read as the same numeric strings the SP v3 API uses. [official] *Amazon Ads API v1* model; *Campaign* entity page; read 2026-11-09. A field report (issue #379) found an older spec typing an id as integer while the API returned a string (see *What practitioners add*).

**GUIDANCE.** Migration. An "AI migration skill", `ads-api-migration` (2026-11-02), is offered to coding agents through the MCP skills library (section V). [official] *MCP: AI migration skills*, https://advertising.amazon.com/API/docs/en-us/mcp/ai-migration-skills, read 2026-11-09.

### F. Write semantics: 207, partial success, idempotency, and archived as final

**RULE.** A batch write answers 207 Multi-Status. The Well-Architected Framework: "When using Amazon Ads APIs that support bulk operations (multiple objects in a single request), expect HTTP `207` Multi-Status responses. These responses indicate that some operations may have succeeded while others failed within the same request. Applications must parse the response body to determine the status of each individual operation and handle successes and failures accordingly." [official] *Well-Architected Framework: Fundamental component*, read 2026-11-09.

**RULE.** The v1 multi-status shape. The cross-product v1 model (`AmazonAdsAPIALL_prod_3p.json`) answers every create, update and delete on campaigns, ad groups, ads, targets and ad extensions with a `…MultiStatusResponseWithPartialErrors`:

- `success[]`: `{ index, <entity> }`, the entity as Amazon stored it.
- `partialSuccess[]`: `{ index, <entity>, errors[1..20] }`, an item Amazon wrote with some of its fields refused.
- `error[]`: `{ index, errors[1..20] }`, an item that was not written.
- `index` is the item's position in the request (bounded 0–999 in `CampaignPartialIndex`, 0–4999 in the shared `ErrorsIndex`).
- Each error is `{ code, message, fieldLocation }`.

The per-product Sponsored Products v1 model (`AmazonAdsAPISP_prod_3p.json`) shows only `success` and `error` for the same operation. [official] *Amazon Ads API v1* model; *Amazon Ads API v1, Sponsored Products* model; read 2026-11-09. [seat] A reader of the reply meets `partialSuccess` on the cross-product surface and may not see it named in the per-product spec.

**RULE.** v1 error codes, from the `ErrorCode` enum with Amazon's descriptions:

- `ARCHIVED_RESOURCE_CANNOT_EDIT`: "Archived resources cannot be edited."
- `ARCHIVED_PARENT_CANNOT_EDIT` and `ARCHIVED_PARENT_CANNOT_CREATE`.
- `RESOURCE_IS_IN_TERMINAL_STATE`: "Resource is in terminal state."
- `AUTOCREATED_ENTITY_CANNOT_EDIT`: "Autocreated entities cannot be edited. To complete this action, create the resource manually."
- `CONFLICT`: "Operation could not be completed due to a conflict. Please retry your request."
- `TOO_MANY_REQUESTS`: "There have been too many requests, please slow down your call rate."
- `FIELD_VALUE_NOT_UNIQUE`: "Resource field value conflicts with existing resource. Try again with an unique field value."
- `DUPLICATE_FIELD_VALUE_FOUND`: several items in one request share a value that must be unique.
- `DUPLICATE_RESOURCE_ID_FOUND`.
- `ACTIVE_RESOURCE_LIMIT_EXCEEDED` and `TOTAL_RESOURCE_LIMIT_EXCEEDED`.
- `PRODUCT_INELIGIBLE`.
- `PAYMENT_ISSUE`.
- `UNSUPPORTED_MARKETPLACE`.
- `FEATURE_DISCONTINUED`.
- `GLOBAL_CAMPAIGN_SINGLE_ADGROUP_LIMIT`, `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_STATE`, `GLOBAL_ATTRIBUTE_UPDATE_RESTRICTED_PORTFOLIO`.
- the `FIELD_VALUE_*` and `FIELD_SIZE_*` validation family.
- `UNAUTHORIZED`, `FORBIDDEN`, `NOT_FOUND`, `INTERNAL_ERROR`.

Every v1 operation also lists HTTP 400, 401, 403, 404, 413, 429, 500, 502, 503 and 504 responses. [official] *Amazon Ads API v1, Sponsored Products* model; *Amazon Ads API v1* model; read 2026-11-09.

**RULE.** The Sponsored Products v3 multi-status shape.

- A v3 write answers 207 with the result under the entity's plural name: `{ "campaigns": { "success": [ { index, campaignId, campaign? } ], "error": [ { index, errors: [ { errorType, errorValue } ] } ] } }`.
- Up to 1000 items per call.
- Sending `Prefer: return=representation` returns the full entity in each success item, not only its id.
- `errorType` names a family. Each family's `errorValue` carries a `reason` and, for bids and budgets, `lowerLimit` and `upperLimit`. The families and some of their reasons:

| Family | Example reasons |
|---|---|
| entity state | `ARCHIVED_ENTITY_CANNOT_BE_MODIFIED`, `AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY`, `INVALID_STATE_TRANSITION`, `PARENT_ARCHIVED_FORBIDS_UPDATES` |
| duplicate value | `DUPLICATE_VALUE`, `NAME_NOT_UNIQUE` |
| bidding | `BID_OUT_OF_MARKET_PLACE_RANGE`, `BID_GT_BUDGET` |
| budget | `BUDGET_TOO_LOW`, `BUDGET_LT_KEYWORD_BIDS` |
| billing | `ADVERTISER_BILLING_SETUP_INCOMPLETE`, `EXPIRED_PAYMENT_METHOD` |
| quota | a `quotaScope` of `ACCOUNT` or `PARENT_ENTITY` |
| throttled | `THROTTLED` |

[official] *Sponsored Products* OpenAPI model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json, read 2026-11-09.

**RULE.** There is no idempotency key on sponsored ads writes. No `Idempotency-Key` header and no client token field appears on any create, update or delete operation in these models:

- the SP v3, SB v3, SB v4 and SD v3 models;
- the v1 campaign-management models;
- the Portfolios model.

Idempotency keys appear in Amazon's models only for DSP audiences, AMC custom models and billing. [official] the models named, as listed in `contracts.json`, read 2026-11-09. [seat] So a create whose reply is lost has an unknown outcome at Amazon: the call may have created the entity. Only a later read of the entities (by name, by query, or through change history, section O) tells whether it did.

**RULE.** Names are the closest thing to a natural key, and only for sellers. The SP v2 and SB v3 models read: "Note that idempotency for this field works different for sellers and vendors. Sellers aren't allowed to have duplicate campaign names, but vendors can have duplicate campaign names." The same SB v3 field description opens with "This name must be unique to the Amazon Ads account to which the campaign is associated", so the model states both. A seller's repeated create with the same campaign name is refused with a duplicate-name error, `NAME_NOT_UNIQUE` (SP v3) or `FIELD_VALUE_NOT_UNIQUE` (v1). A vendor's is not. The Stream campaigns dataset describes `name` as "Name of the campaign (must be unique for an account)". [official] *Sponsored Products v2* model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-products/2-0/openapi.yaml; *Sponsored Brands v3* model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml; *Stream: Sponsored ads campaign management datasets*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/datasets/sponsored-ads-campaign-management; read 2026-11-09.

**RULE.** Archived is final. In Amazon's own words, on four surfaces:

- v1 `State` enum: "`ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state." [official] *Amazon Ads API v1* model, read 2026-11-09.
- Sponsored Display v3, `DELETE /sd/campaigns/{campaignId}`: "Sets the campaign status to archived." and "This operation is equivalent to an update operation that sets the status field to 'archived'. Note that setting the status field to 'archived' is permanent and can't be undone." The ad group and product ad deletes read the same. [official] *Sponsored Display v3* model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml, read 2026-11-09.
- Sponsored Brands v3 keywords, negative keywords and targets: "Archives a keyword specified by identifier." … "setting the status field to 'archived' is permanent and can't be undone"; for targets, "archiving is permanent, and once a target has been archived it can't be made active again." [official] *Sponsored Brands v3* model, read 2026-11-09.
- Sponsored Products v3: the error reason `ARCHIVED_ENTITY_CANNOT_BE_MODIFIED`. [official] *Sponsored Products* model, read 2026-11-09.

**RULE.** In SP v1, create and update accept only `ENABLED` and `PAUSED`. The SP v1 model's `SPCreateState` and `SPUpdateState` enums are `ENABLED` and `PAUSED`. `SPState`, the state an entity can be read in, is `ARCHIVED`, `ENABLED` or `PAUSED`. [official] *Amazon Ads API v1, Sponsored Products* model, read 2026-11-09. [seat] So in SP v1 an entity reaches `ARCHIVED` through the delete operation, not through an update. No v1 page read here says in a sentence that delete archives.

**RULE.** Auto-created entities cannot be edited by these calls. Two errors cover them:

- `AUTOCREATED_ENTITY_CANNOT_EDIT` (v1).
- `AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY` (SP v3). An auto campaign's built-in targeting clauses (close match, loose match, substitutes, complements) are paused or bid on, not archived.

[official] *Amazon Ads API v1* model; *Sponsored Products* model; read 2026-11-09.

**RULE.** Latency and consistency. The *Limits* page's "P99 Guarantee" for "Synchronous CRUD operations" is 30s; that is a response-time figure, not a visibility window. A DSP note of 2026-06-03 states, for the DSP Bid Adjustments API, that "mutating operations are not strongly consistent within a 5-minute window — a subsequent `GET` for the same rule or association may not reflect the change for up to 5 minutes". No sponsored ads page read here gives a consistency window. [seat] Whether a sponsored ads write is visible to an immediate read is therefore undocumented. [official] *Limits, constraints, and quotas*; *Release notes*, "DSP Bid Adjustments API now returns 423 ConcurrentModificationException for racing writes" (2026-06-03); read 2026-11-09.

### G. State enums, serving status and id formats

These enums are recorded for human readers. A skill reads the live model.

**v1, cross-product** (*Amazon Ads API v1* model, read 2026-11-09):

- `State`: `ARCHIVED`, `ENABLED`, `PAUSED` in the production cross-product model. For DSP, "campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery".
- `DeliveryStatus`: `DELIVERING`, `LIMITED`, `NOT_DELIVERING`, `UNAVAILABLE`. The SP model's `SPDeliveryStatus` omits `LIMITED`.
- `status.deliveryReasons` carries the reasons. Examples: `NOT_IN_BUYBOX`, `OUT_OF_STOCK`, `CAMPAIGN_OUT_OF_BUDGET`, `ADVERTISER_OUT_OF_BUDGET`, `AD_GROUP_LOW_BID`, the `MODERATION_*` and `PORTFOLIO_*` families. How these read in a diagnosis belongs to `areas/diagnosis.md`.
- `AdProduct`: `AMAZON_DSP`, `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS`, `SPONSORED_TELEVISION` in the production model; the merged prod-and-beta model (`AmazonAdsAPIALLMerged_prod_3p.json`) adds `FULL_FUNNEL` and `RMS`.
- `CostType`: `CPC`, `CPM`, `FIXED_PRICE`, `VCPM`.
- `MarketplaceScope`: `GLOBAL`, `SINGLE_MARKETPLACE`. SP's `SPMarketplaceScope` reads `SINGLE_MARKETPLACE`.

**v1, Sponsored Products** (*Amazon Ads API v1, Sponsored Products* model `AmazonAdsAPISP_prod_3p.json`, and its merged prod-and-beta copy `AmazonAdsAPISPMerged_prod_3p.json`, read 2026-11-09):

- `SPBidStrategy`: `MANUAL`, `RULE_BASED`, `SALES_DOWN_ONLY`, `SALES_UP_AND_DOWN`. The enum's own description: `SALES_UP_AND_DOWN` "Increases or decreases your bids in real time by a maximum of 100%".
- `SPPlacement`: `PRODUCT_PAGE`, `REST_OF_SEARCH`, `SITE_AMAZON_BUSINESS`, `TOP_OF_SEARCH` in the production model; the merged model adds `REST_OF_BROWSE` and `TOP_OF_BROWSE`.
- `SPTargetType`: `KEYWORD`, `LOCATION`, `PRODUCT`, `PRODUCT_CATEGORY`, `THEME` ("formerly known as Auto Targets for Sponsored Products").
- `SPMatchType`: `BROAD`, `EXACT`, `PHRASE`; `PRODUCT_EXACT`, `PRODUCT_SIMILAR`; `KEYWORDS_CLOSE_MATCH`, `KEYWORDS_LOOSE_MATCH`, `PRODUCT_SUBSTITUTES`, `PRODUCT_COMPLEMENTS`; the `KEYWORDS_RELATED_TO_*` theme family (`GIFTS`, `PEER_BRANDS_PRODUCT_CATEGORY`, `PRIME_DAY`, `YOUR_BRAND`, `YOUR_PRODUCT_CATEGORY`). The merged model adds `INTERESTED_AUDIENCE`.
- `SPSiteRestriction`: `AMAZON_BUSINESS`, `AMAZON_HAUL`.
- `SPCustomerActionType`: `REVIEW_REQUEST`, in the merged model only (the Review Requests beta, section Y).

**Sponsored Products v3** (*Sponsored Products* model, read 2026-11-09):

- Entity state on read: `ENABLED`, `PAUSED`, `ARCHIVED`, `ENABLING`, `PROPOSED`, `USER_DELETED`, `OTHER`.
- State on create and update: `ENABLED`, `PAUSED`, `PROPOSED`.
- Serving status, returned under `includeExtendedDataFields`: per-level enums (`SponsoredProductsCampaignServingStatus`, `…AdGroupServingStatus`, `…AdServingStatus`), each with a `…Reason` detail enum. Examples: `CAMPAIGN_OUT_OF_BUDGET`, `AD_NOT_IN_BUYBOX`, `AD_OUT_OF_STOCK`, `AD_POLICING_SUSPENDED`, `ASIN_QUARANTINED`, `VARIATION_PARENT`, `PIR_RULE_EXCLUDED`.

**Sponsored Brands and Sponsored Display.**

- SB and SD entity states on the Stream campaigns dataset are `ENABLED`, `PAUSED`, `ARCHIVED`. SP adds `USER_DELETED`, `ENABLING` and `OTHER`.
- SD v3 list filters take lowercase values: `stateFilter=enabled,paused,archived`.
- An SB ad can be set to `ENABLED` or `PAUSED`; an SD ad to `ENABLED`, `PAUSED` or `ARCHIVED`. `anandile` stated this in issue #378 (2025-05-21), citing the SB and SD specifications; GitHub shows no repository association for that login, and the Amazon contributor `jerirose` closed the issue on that answer (2025-06-03).

[official] *Stream: Sponsored ads campaign management datasets*; *Sponsored Display v3* model; read 2026-11-09. [opinion] `anandile`, `jerirose` (CONTRIBUTOR), GitHub issue #378, https://github.com/amzn/ads-advanced-tools-docs/issues/378, read 2026-11-09.

**Id formats.**

| Id | Format as documented | Source |
|---|---|---|
| `profileId` | 64-bit integer, sent as a string in the Scope header | *Profiles* model |
| SP v3 entity ids | Numeric strings | *Sponsored Products* model |
| SB v4 entity ids | Strings | *Sponsored Brands v4* model |
| SD v3 entity ids | `int64` | *Sponsored Display v3* model |
| v1 entity ids | Strings; SP v1 ids match SP v3 | *Amazon Ads API v1* model |
| Global account | `amzn1.ads-account.g.*` | *Query advertiser accounts* |
| Manager account | `amzn1.ads1.ma1.*` | *Stream v2: Create a subscription* |
| Portfolio id | Numeric string (v3) | *Portfolios* model |
| Stream batch | `streamBatch.version`, a LONG; "the highest value is the most recent" | *Stream v2: ads-performance-v1* |

Change history (section O) accepts alphanumeric or numeric ids. [official] *Change history* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json, read 2026-11-09. The same campaign id can surface as a string in one API and an integer in another. Airbyte's connector page: "Amazon types adId as a string on the ads entity API but as an integer in reporting v3 … The same applies to adGroupId and campaignId." [opinion] Airbyte, read 2026-11-09.

### H. Sponsored Products v3

**RULE.** Shape (*Sponsored Products* model, read 2026-11-09):

- Each resource has a versioned media type, for example `application/vnd.spCampaign.v3+json`, `application/vnd.spAdGroup.v3+json`, `application/vnd.spKeyword.v3+json`, `application/vnd.spTargetingClause.v3+json`, `application/vnd.spProductAd.v3+json`, and the negative and campaign-negative variants.
- Verbs:
  - `POST /sp/{resource}` creates;
  - `PUT /sp/{resource}` updates;
  - `POST /sp/{resource}/delete` deletes;
  - `POST /sp/{resource}/list` lists, with a filter body and `nextToken`.
- Up to 1000 items per write.
- `includeExtendedDataFields: true` on a list adds an `extendedData` object to each entity. The request field's own description reads "Whether to get entity with extended data fields such as creationDate, lastUpdateDate, servingStatus". The response schemas (`SponsoredProductsCampaignExtendedData`, `…AdGroupExtendedData`, `…ProductAdExtendedData`, `…KeywordExtendedData`, `…TargetingClauseExtendedData` and the negative variants) name the fields `extendedData.creationDateTime`, `extendedData.lastUpdateDateTime`, `extendedData.servingStatus` and `extendedData.servingStatusDetails`. Both dates are "in ISO 8601". The response names are the ones a reply carries. *Rate limiting* says of "list extended data operations" in general: "These calls hold 5x the weight of standard calls towards throttling limits", and "Avoid calling extended data operations unless you specifically need to know the status of the entities." [seat] The page names no product; the SD v3 `…/extended` lists and SP v3's `includeExtendedDataFields` are the extended variants in the models read, so the 5x is read as applying to both.

**RULE.** Other SP v3 operations, by family (*Sponsored Products* model, read 2026-11-09):

- **Budget usage:** `POST /sp/campaigns/budget/usage`, up to 100 `campaignIds`. Answers 207 with `budgetUsagePercent` and `usageUpdatedTimestamp` per campaign.
- **Budget recommendations:**
  - `POST /sp/campaigns/budgetRecommendations`;
  - `POST /sp/campaigns/initialBudgetRecommendation`, for a campaign not yet created.
- **Budget rules:**
  - `/sp/budgetRules` (create, update, get);
  - `/sp/campaigns/{campaignId}/budgetRules` (associate and list);
  - `POST /sp/campaigns/budgetRules/recommendations` (event-based rule recommendations).
- **Optimization rules:**
  - `/sp/rules/optimization` (+ `/search`);
  - `/sp/rules/campaignOptimization` (+ `/eligibility`, `/state`);
  - `/sp/campaigns/{campaignId}/optimizationRules`.
- **Events:** `/sp/v1/events`, the events a budget rule can be keyed to.
- **Keyword recommendations:**
  - `POST /sp/targets/keywords/recommendations`, under `application/vnd.spkeywordsrecommendation.v3+json`, `.v4+json` and `.v5+json`;
  - a global variant, `POST /sp/global/targets/keywords/recommendations/list`.
- **Bid recommendations:**
  - `POST /sp/targets/bid/recommendations` under `application/vnd.spthemebasedbidrecommendation.v3+json`, `.v4+json` and `.v5+json`; the model still lists v3, which *Deprecations* records as shut off 2025-05-15;
  - a global variant, `POST /sp/global/targets/bid/recommendations`.
- **Product and category targeting:**
  - `POST /sp/targets/products/recommendations`;
  - `POST /sp/targets/categories/recommendations`;
  - `GET /sp/targets/categories`;
  - `GET /sp/targets/category/{categoryId}/refinements`;
  - `POST /sp/targets/products/count`.
- **Negative brand targets:**
  - `GET /sp/negativeTargets/brands/recommendations`;
  - `POST /sp/negativeTargets/brands/search`.
- **Keyword groups:** `POST /sp/targeting/recommendations/keywordGroups`.
- **Campaign recommendations:** `GET` and `POST /sp/campaign/recommendations`.
- **Target promotion groups:** `POST /sp/targetPromotionGroups`, `…/list`, `…/recommendations`, `…/targets` and `…/targets/list`.

How these recommendations enter a keyword or bid decision belongs to `areas/keyword-and-product-targeting.md` and `areas/bids-and-placements.md`. Budget rules as a practice belong to `areas/budgets-and-pacing.md` and `beyond/automation-and-amazon-tools.md`.

**RULE.** Rule-based bidding and rules guides. These figures are for human readers only; the practice belongs to `beyond/automation-and-amazon-tools.md`.

- *Bidding rules overview* sets rule-based bidding's preconditions: the campaign has run "for at least 10 days prior to setting a rule and have a minimum of 10 conversions in the last 30 days". It names a ROAS guardrail "based on the previous 21 days" and a minimum daily budget per marketplace (for example US 10, IN 300, JP 600, MX 50).
- *Scheduled bid rules*: "A maximum of 20 schedule bid rules can be specified for a campaign"; changes "take effect within 24 hours".
- *Performance-based rules*: "For sellers, the time period used for metric calculation is within 7 days of an ad click. For vendors, metrics are calculated within 14 days of an ad click." The metrics are `ACOS`, `CTR`, `CVR` (SP, SD), `ROAS` (SP, SB, SD), and `IS` and `NTB` (SB).
- *Schedule-based rules*: "`intraDaySchedule` is currently only available for campaigns in the following marketplaces: US, CA, UK, IN, JP."

[official] *Bidding rules overview*, https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview; *Scheduled bid rules*, …/guides/rules/bidding-rules/scheduled-bid-rules; *Budget rules overview*, …/guides/rules/budget-rules/overview; *Performance-based budget rules*, …/guides/rules/budget-rules/performance-based; *Schedule-based budget rules*, …/guides/rules/budget-rules/schedule-based; all read 2026-11-09.

### I. Sponsored Brands v4, and the v3 paths that remain

**RULE.** Campaigns, ad groups and ads are on v4.

- Paths: `/sb/v4/campaigns`, `/sb/v4/adGroups`, `/sb/v4/ads`, each with `POST …/list` and `POST …/delete`.
- Media types such as `application/vnd.sbcampaignresource.v4+json`, `application/vnd.sbadgroupresource.v4+json` and `application/vnd.sbadresource.v4+json`.
- Ads are created at type-specific paths: `/sb/v4/ads/autoCollection`, `…/manualCollection`, `…/brandVideo`, `…/video`, `…/storeSpotlight`, and the deprecated `…/productCollection` and `…/productCollectionExtended`.
- `productCollection` and `productCollectionExtended` are deprecated (*Deprecations*, "June 2026 - Deprecation of Sponsored Brands Product Collection Ad Type"). "Starting August 2026" a product-collection create "will succeed but create a Manual Collection ad instead" (in v1, `productCollectionSettings` "will be automatically mapped to `manualCollectionSettings`"); manual collections need at least 3 ASINs and titles of at most 32 characters; "Post January 2027" such creates "will return an error".
- Sponsored Brands Collections became available in all marketplaces on 2026-09-23, through `POST /adsApi/v1/create/ads` and `/adsApi/v1/update/ads` and SB v4 ("Sponsored Brands Collections Now Available Worldwide").
- The ListMigrations note (2026-09-18) adds: "Beginning February 2027, product collections will no longer be supported." It also offers `POST /sb/v4/migrations/list` to fetch recommended `MANUAL_COLLECTION` and `AUTO_COLLECTION` replacements.

[official] *Sponsored Brands v4* model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json; *Release notes*, "Introducing the ListMigrations API for Sponsored Brands Product Collection migration" (2026-09-18); *Deprecations*; read 2026-11-09. [seat] The deprecation entries read here give January 2027, and the ListMigrations note gives February 2027. Both are recorded.

**RULE. The product-collection dates, page by page** (re-read 2026-11-09 to settle the date the sibling files disagree on):

| Amazon page | What it says | Date it gives |
|---|---|---|
| *Deprecations*, "June 2026 - Deprecation of Sponsored Brands Product Collection Ad Type", V0 APIs | "**Shutoff Date:** January 2027"; "Post January 2027, requests to create new Product Collection ads will return an error." | January 2027 |
| Same entry, V1 APIs (`productCollectionSettings` in `/adsApi/v1/create/ads`) | "**Shutoff Date:** January 2027"; "Post January 2027, create ad requests using `productCollectionSettings` will return an error." | January 2027 |
| *Deprecations*, table "Amazon Ads API deprecations", row "Sponsored Brands Product Collection V1 API" | shutoff column | January 2027 |
| *Product Collection Migration Guide* (`reference/migration-guides/sb-product-collection`) | "January 2027 \| **Final shutoff**. All API requests to create Product Collection ads will be rejected with an error."; "The Product Collection endpoints will continue to function until **January 2027**." | January 2027 |
| *Release notes*, ListMigrations (2026-09-18) | "Beginning February 2027, product collections will no longer be supported." | February 2027 |
| *Sponsored Brands v4* model, `POST /sb/v4/ads/productCollection` and `…/productCollectionExtended` | `deprecated: true`, "[DEPRECATED - Do not use]", pointing to the *Deprecations* entry; no date | — |

All of these agree on August 2026: from then a product-collection create "will succeed but create a Manual Collection ad instead", and in v1 `productCollectionSettings` is "automatically mapped to `manualCollectionSettings`". Custom images on such a create "will be accepted but will not render". `ListMigrations` adds that collections "feature up to 10 products per ad (compared to 3 with Product Collection)". [official] the pages named, read 2026-11-09. [seat] Four Amazon statements give January 2027 for the error on create, and one later release note gives February 2027 for "no longer supported". The pages do not reconcile the two, so both dates stand as Amazon gave them.

**RULE.** Keywords and targets are on v3.

- SB keywords, negative keywords, targets, negative targets and themes are on the SB v3 specification: `/sb/keywords`, `/sb/negativeKeywords`, `/sb/targets`, `/sb/negativeTargets`, `/sb/themes`.
- v3 keyword lists are `GET` with query parameters.
- `DELETE` archives, permanently (section F).

[official] *Sponsored Brands v3* model, read 2026-11-09.

**RULE. Which SB specification carries which path** (re-read 2026-11-09 to settle what sibling files disagree on). Amazon publishes the SB surface in three files. `contracts.json` lists two of them:

| File | Where listed | `info` title | What it holds |
|---|---|---|---|
| `https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml` | `contracts.json`, "Sponsored Brands campaign management (version 3)" | — | `GET /brands`; `GET`/`POST`/`PUT /sb/keywords` and `GET`/`DELETE /sb/keywords/{keywordId}`; `GET`/`POST`/`PUT /sb/negativeKeywords` (media types `application/vnd.sbnegativekeyword.v3+json` and `.v3.2+json` on the list) and `GET`/`DELETE /sb/negativeKeywords/{keywordId}`; `/sb/targets` and `POST /sb/targets/list`; `/sb/negativeTargets` and `POST /sb/negativeTargets/list`; `/sb/themes` and `POST /sb/themes/list`; `GET /pageAsins`; `GET /media/describe`; `GET`/`POST /stores/assets`; `POST /sb/recommendations/bids`, `/sb/recommendations/keyword`, `/sb/recommendations/targets/product/list`, `/sb/recommendations/targets/category`, `/sb/recommendations/targets/brand`; `POST /sb/campaigns/budgetRules/recommendations`; the deprecated `/sb/moderation/campaigns/{campaignId}` and the v2 `/v2/hsa/{recordType}/report` |
| `https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json` | `contracts.json`, "Sponsored Brands campaign management", version 4 | — | `/sb/v4/campaigns`, `/sb/v4/adGroups`, `/sb/v4/ads*`, `/sb/ads/creatives/*`, `GET /sb/negativeTargets/brands/recommendations` (media type `application/vnd.sbtargeting.v4+json`), `/sb/targets/categories*`, `/sb/targets/products/count`, budget rules, budget usage, forecasts, insights, optimization rules, headline and budget recommendations, the migration operations |
| `https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json` | Not in `contracts.json` (fetched by plain GET) | "Sponsored Brands 3.0" | 50 paths, the same `/sb/v4/*` surface as the v4 file, including `GET /sb/negativeTargets/brands/recommendations`; no `/sb/negativeKeywords`, no `/sb/keywords`, no `/brands` |

So `/sb/negativeKeywords` is on the SB v3 specification, and `/sb/negativeTargets/brands/recommendations` is on the v4 surface. The `SponsoredBrands_prod_3p.json` file is titled 3.0 but holds the v4 paths. A reader of that file finds no `/sb/negativeKeywords` and does find the negative-brand recommendation, and both observations are correct about that file. [official] the three files, read 2026-11-09.

**RULE. SB v3 paths outside keywords and targets** (*Sponsored Brands v3* model, read 2026-11-09):

- `GET /brands` (`application/vnd.brand.v3+json`): "Gets an array of Brand data objects for the Brand associated with the profile ID passed in the header". Each item has `brandId`, `brandEntityId` ("The Brand entity identifier available exclusively for seller advertisers") and `brandRegistryName`. A `brandTypeFilter` query narrows the list.
- `GET /pageAsins?pageUrl=…` (`application/vnd.pageasins.v3+json`): "for sellers, the addresss must be a Store page. Vendors may also specify a custom landing page address. Only the `ASINs` that are directly associated on creation with a Store landing page are returned by this API … This includes `ASINs` that are on Dynamic widgets, product selections, and featured deals widgets." (The last sentence lists what is *not* returned.)
- `GET /stores/assets?brandEntityId=…&mediaType=brandLogo` (`application/vnd.mediaasset.v3+json`): the brand's Store-library assets. "For sellers, this field is required"; only `brandLogo` is supported as `mediaType`.
- `POST /stores/assets`: "Creates a new image asset", `multipart/form-data`, with required `Content-Disposition` (the file name) and `Content-Type` (the image type) headers. "Image assets are stored in the Store Assets Library. Note that there may be a delay before the image is displayed in the console."
- `GET /media/describe?mediaId=…`: "API to poll for media status. In order to attach media to campaign, media should be in either `PendingDeepValidation` or `Available` status." No `/media/upload` or `/media/complete` operation appears in any SB model read on 2026-11-09. Video for SB is uploaded through the creative asset library (section AA).

**RULE.** The v3-to-v4 migration.

- The note "Sponsored Brands campaigns v3 to v4 migration" (2025-10-14) required advertisers to migrate:
  - zero-impression campaigns created before October 2022, by 2025-10-30;
  - campaigns with impressions, by 2025-12-31.
- Endpoints: `/sb/v4/legacyCampaigns/migrationJob*`, and `/sb/v4/migrations/list` for product collections.
- The *SB v3 to v4 migration guide* maps fields.

[official] *Release notes* (2025-10-14); *Sponsored Brands v3 to v4 migration guide*, https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4; read 2026-11-09.

**RULE.** SB other families: budget usage, forecasts, insights, budget rules, optimization rules, and headline and keyword recommendations. The legacy SB moderation endpoint shut off 2025-12-15. Negative bid adjustments for SB placement groups:

- the deprecation was first announced for 2026-02-02;
- the note of 2026-01-27 moved it to 2026-06-15: "existing campaigns with negative bid adjustments will continue to run with their current settings, no new negative adjustments will be accepted after this date."

[official] *Sponsored Brands v4* model; *Release notes* (2025-12-01, 2026-01-27); *Deprecations*; read 2026-11-09.

### J. Sponsored Display v3

**RULE.** Shape (*Sponsored Display v3* model, read 2026-11-09):

- `/sd/campaigns`, `/sd/adGroups`, `/sd/productAds`, `/sd/targets`, `/sd/negativeTargets`, `/sd/creatives`.
- Lists are `GET` with query parameters (`stateFilter`, `campaignIdFilter`, `startIndex`, `count` and others). `…/extended` variants add serving status.
- Creates (`POST`) and updates (`PUT`) take arrays. `DELETE /sd/{resource}/{id}` archives, permanently.
- Ids are `int64`.

Other families:

- `POST /sd/targets/recommendations`;
- `POST /sd/targets/bid/recommendations`;
- budget usage;
- `/sd/optimizationRules`;
- budget rules;
- `/sd/locations`;
- creatives and `/sd/moderation/creatives`;
- `/sd/brandSafety`;
- `/sd/forecasts`.

**RULE.** Deprecated SD paths: `/sd/{recordType}/report` (v2 reports, whose download answers a 307 redirect) and SD snapshots. SD reports are on reporting v3, and reporting v1 from 2026-09-30. [official] *Deprecations*, read 2026-11-09. Report detail belongs to `method/reporting.md`.

**RULE.** Sponsored Display on v1. Amazon publishes an SD v1 specification (`AmazonAdsAPISD_prod_3p.json`), with batch limits of 100 for campaigns, ad groups and ads and 1000 for targets. [official] *Amazon Ads API v1, Sponsored Display* model, read 2026-11-09. Field reports on SD v1 (issues #475, #481) are under *What practitioners add*.

**RULE. Whether SD v1 campaign management is usable** (re-read 2026-11-09 to settle a disagreement with `areas/bids-and-placements.md`). Four facts, each from its page:

1. The SD v1 specification (`info.title` "Amazon Ads API SD") holds 16 paths: `POST /adsApi/v1/{create,update,query,delete}/{campaigns,adGroups,ads,targets}`. It has no ad associations and no ad extensions. [official] *Amazon Ads API v1, Sponsored Display* model.
2. The `contracts.json` description of the v1 contract and the *Campaign management overview* both read "The Amazon Ads API currently supports campaign management operations for:" Amazon DSP, Sponsored Brands, Sponsored Products, Sponsored Display, Sponsored Television. [official] *contracts.json*; *Campaign management overview*.
3. No release note dates SD or STV general availability on v1. The v1 release notes name SD only in the 2025-08-01 and 2025 roadmap sentences ("including Sponsored Display and Sponsored TV later in 2025"; "Throughout 2025, all of our ad products will become available … including Sponsored Display and Sponsored TV"). [official] *Release notes: Ads API v1*.
4. Developers report calling SD v1 and getting answers. In #475 a budget update was accepted and ignored. In #481 the API's own validation refused a `kpi` value and listed the accepted enum. [opinion] `zhangwg4apollo`, issue #475; `iYetaimei`, issue #481.

[seat] "SD is not in the unified v1 campaign API" does not match items 1, 2 and 4. "No note announces SD" matches item 3. Amazon's specification and overview list SD v1 as supported, the field reports show it answering, and no dated GA note exists.

### K. Portfolios and account budgets

**RULE.** Portfolios v3.

- `POST /portfolios` (create), `PUT /portfolios` (update), `POST /portfolios/list`.
- `POST /portfolios/budget/usage`.
- Media type `application/vnd.spPortfolio.v3+json`.
- `/v2/portfolios` shut off 2025-03-01.

[official] *Portfolios* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json; *Deprecations*; read 2026-11-09.

**RULE.** Unspent budget sharing. The release note of 2025-07-19 introduced `budgetControls.campaignUnspentBudgetSharing.featureState` (`ENABLED` / `DISABLED`) on a portfolio, set with `PUT /portfolios`. In its words, campaigns that "consistently reach their daily spending limits" can "spend up to twice their daily budget by tapping into unspent campaign budget from previous days in the month", "while staying within your total monthly portfolio budget". The release note lists the countries, among them US, CA, MX, BR, the EU five, IE, JP, AU, IN and SG. The guide adds: "By default, all portfolios created after 6/20/2025 have unspent campaign budget sharing turned on." [official] *Release notes* (2025-07-19); *Portfolios: Sharing leftover budget*, https://advertising.amazon.com/API/docs/en-us/guides/portfolios/sharing-leftover; read 2026-11-09. Its pacing meaning belongs to `areas/budgets-and-pacing.md`.

**RULE.** Account-level budget settings are read and written with `GET` and `POST /accountBudgets/featureFlags` (section C).

### L. Recommendations: three surfaces

Amazon offers recommendations on three surfaces that do not share a shape.

**RULE.** 1. Product-specific targeting, bid and budget recommendations (SP v3, SB, SD; section H). Each is a synchronous `POST` or `GET` that returns suggestions for one request:

- keywords for ASINs or an ad group;
- product and category targets;
- bids for targets in an ad group or for a new ad group;
- a daily budget for an existing or a not-yet-created campaign;
- brands to exclude;
- event-based budget-rule suggestions.

The keyword and bid recommendation operations each carry several versioned media types (v3, v4, v5). Each version answers a different shape. [official] *Sponsored Products* model, read 2026-11-09. The deprecated predecessors and their shut-off dates:

- The v2 suggested keywords were deprecated 2026-01-27 and shut off June 2026.
- `/v2/sp/targets/bidRecommendations` and the `spthemebasedbidrecommendation.v3+json` content type shut off 2025-05-15; the other v2 bid recommendations (`/v2/sp/adGroups/{adGroupId}/bidRecommendations`, `/v2/sp/keywords/…/bidRecommendations`) shut off 2024-03-27.

[official] *Deprecations*; *Release notes*, "Deprecation of V2 Legacy APIs" (2026-01-27); read 2026-11-09. Airbyte's changelog 9.0.0 records the move of its suggested-keywords stream from v2 to the keyword recommendations API. [opinion] Airbyte, read 2026-11-09.

**RULE.** 2. Tactical recommendations (`/recommendations`). The *Recommendations* model (https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json, read 2026-11-09) holds three operations:

- `POST /recommendations/list`;
- `POST /recommendations/apply`, up to 100 recommendation ids;
- `PUT /recommendations/{recommendationId}`, to edit a recommendation before applying it.

Recommendation types include `CAMPAIGN_BUDGET`, `KEYWORD_BID` and `NEW_NEGATIVE_KEYWORD`, among others. Statuses:

- `PUBLISHED`;
- `APPLY_IN_PROGRESS`;
- `APPLY_SUCCESS`;
- `APPLY_FAILED`;
- `REJECTED`.

Applying a `NEW_CAMPAIGN` recommendation answers `ACCEPTED`: the campaign is created asynchronously. [seat] Applying a recommendation is a write to the seller's campaigns made by Amazon on the caller's request. Its effect is read afterwards from the entity, not from the apply reply.

**RULE.** 3. The v1 Recommendations API, launched 2026-08-31 ("Amazon Ads Recommendations API now available"), per that note, *Recommendations API overview*, *How to* and *Recommendation types*:

- `POST /adsApi/v1/query/recommendations`:
  - takes a required `accessRequestedAccounts` (exactly one entry, `advertiserAccountId` as a global account id or a DSP account id) and a required `marketplacesFilter`;
  - optional filters: `languageFilter`, `adProductFilter`, `recommendationTypeFilter`, `recommendationTypeDetailsFilter`;
  - `maxResults` defaults to 300 and is capped at 300.
- The list operation is documented as `GET /adsApi/v1/list/recommendations` in the guide.
  - It takes no body.
  - It needs the `Amazon-Ads-AccountId` header. "A request that omits the `Amazon-Ads-AccountId` header is rejected at the gateway before reaching the service and returns `401 Unauthorized`."
- Recommendation types:
  - `REMOTE_CAMPAIGN_PAUSED` (Sponsored Products);
  - `AUTOMATIC_GLOBAL_ADS_ENROLLMENT`;
  - `BRAND_PRODUCT_SEGMENT` and `BRAND_PRODUCT_KEYWORD` (Sponsored Brands, scoped by type details).
  - Other types are refused with `400` `INVALID_RECOMMENDATION_TYPE`.

[official] *Recommendations API overview*, https://advertising.amazon.com/API/docs/en-us/guides/recommendations/recommendations-api/overview; *Recommendations API: How to*, …/guides/recommendations/recommendations-api/how-to; *Recommendation types*, …/guides/recommendations/recommendations-api/recommendation-types; read 2026-11-09. The guides and the 2026-08-31 release note name `GET /adsApi/v1/list/recommendations`; the merged v1 model (`AmazonAdsAPIALLMerged_prod_3p.json`, read 2026-11-09) lists `GET /adsApi/v1/recommendations` and `POST /adsApi/v1/query/recommendations`, and also `POST /adsApi/v1/create/recommendations/sb` and `POST /adsApi/v1/query/recommendationTypes/sb`. [seat] The guide and the model disagree on the list path; the live reference decides.

The Stream v1 deprecation entry says recommendation data comes from the Recommendations API, not Stream: "For recommendation data, use the Recommendations API. These features are not carried forward in Stream v2." [official] *Deprecations*, "September 2026 - Deprecation of Amazon Marketing Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting", read 2026-11-09.

### M. Budget usage, budget rules and optimization rules

**RULE.** Budget usage.

- Endpoints:
  - `POST /sp/campaigns/budget/usage`;
  - `POST /sb/campaigns/budget/usage`;
  - `POST /sd/campaigns/budget/usage`;
  - `POST /portfolios/budget/usage`.
- Each takes up to 100 ids and answers 207.
- Each item gives:
  - `budgetUsagePercent`;
  - `budget`;
  - `usageUpdatedTimestamp`;
  - on error, an `index` and a message.

[official] *Sponsored Products* model; *Sponsored Display v3* model; *Sponsored Brands v4* model; *Portfolios* model; read 2026-11-09. How fresh the figure is: the models give only the timestamp. A developer asked about it in issue #413 and got no answer from Amazon by 2026-11-09. [opinion] GitHub issue #413, https://github.com/amzn/ads-advanced-tools-docs/issues/413, read 2026-11-09.

**RULE.** Budget rules. Budget rules raise a campaign's budget by a percentage under one of two triggers:

- a schedule, or an Amazon event from `/sp/v1/events`;
- a performance condition (`ACOS`, `CTR`, `CVR`, `ROAS`, and for SB `IS` and `NTB`).

SP, SB and SD each have them. The guides' figures, for human readers only: performance metrics are calculated "within 7 days of an ad click" for sellers and "within 14 days of an ad click" for vendors; `intraDaySchedule` exists only in US, CA, UK, IN and JP. [official] *Budget rules overview*; *Schedule-based budget rules*; *Performance-based budget rules*; read 2026-11-09.

**RULE.** Optimization rules. These are campaign-level automation that Amazon runs:

- `/sp/rules/optimization` and `/sp/rules/campaignOptimization` (with `/eligibility` and `/state`);
- `/sd/optimizationRules`;
- the SB optimization rules.

Rule-based bidding (`RULE_BASED` bid strategy in v1) has preconditions on a campaign's history, which *Bidding rules overview* states. [official] *Sponsored Products* model; *Bidding rules overview*; read 2026-11-09. As a practice, see `beyond/automation-and-amazon-tools.md`.

### N. Eligibility, product metadata and moderation

**RULE.** Product eligibility.

- `POST /eligibility/product/list` takes:
  - `adType`: `sp`, `sb`, `sd` or `dsp`;
  - up to 50 `productDetailsList` entries (`asin`, `sku`);
  - optional `locale`.
- It answers per product:
  - `overallStatus`: `ELIGIBLE`, `ELIGIBLE_WITH_WARNING` or `INELIGIBLE`;
  - an `eligibilityStatusList` of `{ name, message, severity, helpUrl }`.
- `POST /eligibility/programs` answers whether the account may run programs.

[official] *Eligibility* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json, read 2026-11-09. A request logged in issue #380 shows the call made with the Scope header and an SD `adType`. [opinion] `Tristin-C`, GitHub issue #380, https://github.com/amzn/ads-advanced-tools-docs/issues/380, read 2026-11-09. Which reasons make a product ineligible belongs to `beyond/ad-products-and-eligibility.md` and `areas/diagnosis.md`.

**RULE.** Product metadata.

- `POST /product/metadata` under `application/vnd.productmetadatarequest.v1+json`.
- Input: one of `asins` (up to 300), `skus` (up to 300; "Currently only support SP program type for sellers") or `searchStr` (a title search of up to 200 characters), with `pageIndex` and `pageSize` (up to 300); for sellers and vendors "results are capped at 10k ((pageIndex + 1) * pageSize)".
- Options: `adType` (`SP`, `SB`, `SD`; required for an eligibility check), `checkEligibility`, `checkItemDetails`, `isGlobalStoreSelection`, `locale`, and `sortBy` (`SUGGESTED` or `CREATED_DATE`, SP sellers only).
- It returns, per product:
  - `asin` and `sku`;
  - `title`;
  - `availability`;
  - `bestSellerRank`;
  - `eligibilityStatus` and `ineligibilityCodes`;
  - `priceToPay` and `basisPrice`;
  - image and other item details.

This is the advertising console's product picker as an API. [official] *Product selector* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json, read 2026-11-09.

**RULE.** Moderation.

- `POST /moderation/results` (media type v4.1) returns the moderation status of SB and SD creatives and their rejection reasons.
- `POST /preModeration` checks creative components before submission.
- The legacy SB moderation endpoint shut off 2025-12-15.

[official] *Moderation* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Moderation_prod_3p.json; *Pre-moderation*, https://advertising.amazon.com/API/docs/en-us/guides/moderation/pre-moderation; *Deprecations*; read 2026-11-09. Ad policy as such belongs to `beyond/ad-products-and-eligibility.md`.

### O. Change history

**RULE.** `POST /history` (*Change history* model, read 2026-11-09).

- Scope, verbatim: "This API only returns change history for Sponsored Products and Sponsored Brands campaigns. Changes for Sponsored Display campaigns are not returned. Also, it doesn't return information about who made the change."
- Window: `fromDate` is "Max 90 days of history". "All times will be in UTC Epoch format"; the event `timestamp` is described as "unix time".
- Paging:
  - `count`: "Default 100. Minimum 50. Maximum 200."
  - `pageOffset` is "Mutually exclusive with 'nextToken'. Max results with pageOffset is 10000. Use nextToken instead for more results."
  - `totalResults` is "Only provided for pageOffset queries and capped at 10000."
- Filters:
  - `eventTypes`: `AD`, `AD_GROUP`, `CAMPAIGN`, `KEYWORD`, `NEGATIVE_KEYWORD`, `PRODUCT_TARGETING`, `THEME`;
  - up to 10 `eventTypeIds` and up to 10 `parents` per type.
- `THEME` events need `Accept: application/vnd.historyresponse.v1.1+json`.
- Each event gives `changeType`, for example `BID_AMOUNT`, `BUDGET_AMOUNT`, `STATUS`, `PLACEMENT_GROUP`, `SMART_BIDDING_STRATEGY` and others. It also gives `previousValue`, `newValue`, `timestamp` and `metadata`.
- Ids: if numeric ids are supplied, numeric ids are returned; otherwise alphanumeric ids are.

A field report (issue #422) describes persistent 429 on this call for one seller (see *What practitioners add*). How a change's effect is measured belongs to `method/change-measurement.md`.

### P. Exports

**RULE.** Exports are snapshots of current entity metadata, produced asynchronously.

- Request: `POST /campaigns/export`, `/adGroups/export`, `/targets/export`, `/ads/export`. Each answers `202` with an `exportId`.
- Poll: `GET /exports/{exportId}` until `COMPLETED`, which carries a download `url`.
- Exports cover SP, SB and SD.

From *Exports FAQ*:

- Throttling is a queue: "The default cap for all customers is 5 jobs per endpoint."
- URLs: "Export download URLs are valid for one hour. Each call to `GET /exports/{exportId}` generates a new download URL. You can generate new download URLs for up to 24 hours after the export completes."
- History: "Exports contain information about campaigns at the time of the request. It is not possible to retrieve historical metadata via exports."
- Cadence (GUIDANCE): "We recommend requesting exports one to two times per day to synchronize your advertising data. The exports API is not designed for continuous real-time data retrieval."

*Rate limiting* (GUIDANCE): "A better alternative to making thousands of list operations is to request an export and parse the results." The Well-Architected Framework: "use Exports (async) for bulk campaigns, use `GET` (sync) for single or subset of campaigns."

[official] *Exports* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json; *Exports overview*, https://advertising.amazon.com/API/docs/en-us/guides/exports/overview; *Exports: Get started*, …/guides/exports/get-started; *Exports FAQ*, …/guides/exports/faq; *Rate limiting*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/rate-limiting; read 2026-11-09.

### Q. Brand Metrics, Stores insights and Amazon Attribution

**RULE.** Brand Metrics.

- Operations: `POST /insights/brandMetrics/report` creates a report; `GET /insights/brandMetrics/report/{reportId}` polls it.
- The guide calls Brand Metrics an open beta for "professional sellers enrolled in Amazon Brand Registry and vendors" in US, CA, MX, UK, DE, FR, IN, IT, ES, JP and AU.
- Test accounts can request reports, which carry no data.

[official] *Brand Metrics* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json; *Brand Metrics overview*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview; *Test accounts overview*; read 2026-11-09. What the metrics mean belongs to `beyond/metrics-and-attribution.md`.

**RULE.** Stores insights.

- Operations: `POST /stores/{brandEntityId}/insights` and `POST /stores/{brandEntityId}/asinMetrics`.
- Permissions, as the model lists them: `advertiser_campaign_edit`, `amazon_stores_view` or `amazon_stores_edit`.
- `/v2/stores` was replaced by `/brand/stores/v1/storePages/list` and shut off 2026-06-01. The *Deprecations* table row reads "V2 Stores | `/v2/stores` | /brand/stores/v1/storePages/list | January 2026 | June 1, 2026", and the link goes to a `brand-home` reference whose model this seat could not read (section AB). [seat] A read of `brandEntityId` from `GET /v2/stores` now meets a shut-off path. The `brandEntityId` is returned today by SB v3 `GET /brands` (section I), which the *Creating assets* guide names for sellers: "Amazon sellers must include their brand entity ID. You can find this using the `GET /brands` endpoint."
- v1 Brand Store, Store Edition, Store Page and Publish Version contracts are also published at Amazon's contract host; `denisneuf/python-amazon-ad-api`'s README links them.

A field report on `denisneuf/python-amazon-ad-api` (issue #253, 2026-02-19) is titled "Add Content-Type header to the Get Store Insights API request". [official] *Stores* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json; *Deprecations*; read 2026-11-09. [opinion] `denisneuf/python-amazon-ad-api` README and issue list, https://github.com/denisneuf/python-amazon-ad-api, read 2026-11-09.

**RULE.** Amazon Attribution.

- Operations:
  - `GET /attribution/advertisers` and `GET /attribution/publishers`;
  - `POST /attribution/report`;
  - `GET /attribution/tags/macroTag` and `GET /attribution/tags/nonMacroTemplateTag`.
- The guide gives it as a beta for brand-registered professional sellers and vendors in US, CA, MX, UK, DE, FR, IT, ES and NL.
- An Attribution profile shows `accountInfo.subType` `AMAZON_ATTRIBUTION`.

Airbyte skips profiles that answer "This profileID is not authorized to use Amazon Attribution" or 401. [official] *Amazon Attribution* model, https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json; *Amazon Attribution overview*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-attribution/overview; *Profiles* model; read 2026-11-09. [opinion] Airbyte, read 2026-11-09.

### R. Reporting, as a surface

The content of reports (types, columns, windows, retention, lifecycle) belongs to `method/reporting.md`. The surface facts, for human readers only:

- **Reporting v3.**
  - Operations: `POST /reporting/reports`, `GET /reporting/reports/{reportId}`, `DELETE /reporting/reports/{reportId}`.
  - It uses the profile Scope header.
  - It stops 2027-06-30, as do "Sponsored Ads v2 reporting endpoints and their associated report types" (among them `/v2/hsa/…`) and Stream v1. The *Deprecations* page and the GA note of 2026-09-30 say so. The same entry: "The Exports API for campaign metadata is not affected."
- **Reporting v1.**
  - Operations: `POST /adsApi/v1/create/reports`, `/adsApi/v1/retrieve/reports`, `/adsApi/v1/delete/reports`.
  - The account goes in `accessRequestedAccounts[].advertiserAccountId`, not in a header.
  - Limits, from *Limits and best practices*: "Reporting API v1 applies its rate and concurrency limits per client ID … Limits are not applied per advertiser account. All requests made with the same client ID share the same limits, regardless of how many advertiser accounts those requests cover. A request for one advertiser account can be throttled because of other requests made with the same client ID." Concurrency can be "as low as 1" and rate "as low as 1 request per second", "per client ID and may vary by client ID".
  - The *Reporting API v1 overview*: "The reporting API v1 supports one concurrent report per client ID, not per advertiser account. This allows approximately 100 reports per day based on average run times."
  - Two other Amazon pages say the opposite. The *Amazon Ads reporting overview*: "The reporting API v1 allows one concurrent report per advertiser. Only one report can be running at a time for a given advertiser account", and a request made while another runs "will be queued or receive a 429 response code". The GA note of 2026-09-30: "The Reporting API v1 supports one concurrent report per advertiser, which allows advertisers to run approximately 100 reports per day". [seat] The two newer-looking reference pages (v1 overview, *Limits*) say per client id; the general reporting overview and the GA note say per advertiser. Which applies is not settled by the pages.
  - A higher concurrency limit can be requested by support ticket; "approval is not guaranteed" (*Limits*).
  - A completed v1 report may carry a `warnings` array (2026-10-05), for example for "values redacted because you are not permissioned to see the field". Amazon says to treat `warningCodes` "as an open-ended list".
- **Other dates.**
  - SB category benchmark APIs stop 2026-12-17.
  - SB v2 `searchTermImpressionShare` and `searchTermImpressionRank` return null from 2026-11-10.

[official] *Amazon Ads reporting overview*, https://advertising.amazon.com/API/docs/en-us/guides/reporting/overview; *Reporting API v1 overview*, …/guides/reporting/ads-v1/overview; *Reporting v1: Limits and best practices*, …/guides/reporting/ads-v1/limits; *Reporting v1 quickstart*, …/guides/reporting/ads-v1/quickstart; *Release notes* (2026-09-30, 2026-10-05); *Deprecations*; read 2026-11-09.

**GUIDANCE.** Amazon points volume to Stream: "Amazon Marketing Stream is the only reporting surface that scales for automated and recurring reporting." Also: "It is recommended that most use cases shift to Amazon Marketing Stream." [official] *Reporting API v1 overview*; *Reporting v1: Limits and best practices*; read 2026-11-09.

### S. Amazon Marketing Stream (needs an AWS destination)

**RULE.** Stream v1 is being retired. It delivered JSON deltas through Amazon Data Firehose or SQS to the customer's AWS account, hourly; subscriptions were made with `/streams/subscriptions` (and `/dsp/streams/subscriptions`). The campaigns datasets page carries the warning: "Amazon Marketing Stream v1 is on a deprecation path. Existing subscriptions will keep delivering data during this period, and some v1 functionality may be limited before Stream v1 is shut off on June 30, 2027." [official] *Amazon Marketing Stream* model, https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonMarketingStream_prod_3p.json; *Stream: Sponsored ads campaign management datasets*; *Stream overview*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/overview; read 2026-11-09.

**RULE.** How Stream v2 delivers. From *Data delivery*: "Once your subscription is `ACTIVE`, Stream v2 writes Apache Parquet files to your S3 bucket and sends a notification to your SQS queue for each delivery."

- Each notification names the dataset, the batch (`streamBatchId`, `startDateTime`, `endDateTime`, `version`) and the S3 URIs.
- "Read notifications to process each delivery rather than listing the S3 bucket."
- Values are totals, not deltas.
- When a batch is restated, the newest copy carries the highest `streamBatch.version`.

[official] *Stream v2: Data delivery*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/data-delivery; *Stream v2 overview*; *Stream v2: Migrate from v1*, …/v2/migrate-from-v1; read 2026-11-09.

**RULE.** Stream v2 subscriptions.

- Operations:
  - `POST /adsApi/v1/create/streamSubscriptions`;
  - `POST /adsApi/v1/query/streamSubscriptions`;
  - `POST /adsApi/v1/retrieve/streamSubscriptions`;
  - `POST /adsApi/v1/delete/streamSubscriptions`.
- Request fields:
  - `accessRequestedAccounts[].advertiserAccountId`: a global account (`amzn1.ads-account.g.*`) or a numeric DSP advertiser. "The advertiser account is supplied in the request body through `accessRequestedAccounts`, not through a scope header."
  - `destination.s3Destination.bucketArn`;
  - `destination.s3Destination.notification.queueArn`.
- "A subscription delivers the advertiser's global data regardless of the destination Region."
- An unsupported or unauthorized account is refused at the gateway with `401` and "Unauthorized exception while handling 3P Multi-Accounts Request: Bulk account authorization denied: DENY".

[official] *Stream v2: Create a subscription*, read 2026-11-09.

**RULE.** Stream v2 limits (*Stream v2: Limits*), for human readers only:

- One subscription per dataset, destination and account.
- 5 destinations per client application.
- One subscription per create, retrieve or delete request; one account per `accessRequestedAccounts`.
- Query `maxResults` 1–5000.
- Each subscription operation is limited to 25 requests per second per client application, with `429 TOO_MANY_REQUESTS`.
- Parquet files target about 256 MB but can be larger.
- On 429: "retry with exponential backoff and jitter".

[official] *Stream v2: Limits*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/manage-subscriptions/limits, read 2026-11-09.

**RULE.** Stream v2 datasets.

- `ads-performance-v1`:
  - hourly grain; supported accounts are Global Account and DSP Regional Account;
  - "Restatement window | 70 days";
  - "The dataset does not include calculated metrics such as ROAS or CTR."
- `ads-converted-product-v1`: daily grain.

[official] *Stream v2: ads-performance-v1*, …/v2/datasets/ads-performance; *Stream v2: Datasets overview*, …/v2/datasets/overview; read 2026-11-09.

**RULE.** The destination is the integrator's AWS account. *Set up your destination* and *Get started* require an S3 bucket and an SQS queue in the integrator's own AWS account, in a supported Region:

- NA: `us-east-1`;
- EU: `eu-west-1`, `eu-west-2`, `eu-south-2`;
- FE: `us-west-2`, `ap-southeast-1`.

The bucket and queue carry policies that admit Stream's roles in Amazon's AWS account `926844853897` (`PublisherRole`, `ReviewerRole`). Amazon supplies a CloudFormation template. "A destination belongs to the application that first uses it." [official] *Stream v2: Set up your destination*, …/v2/set-up-your-destination; *Stream v2: Get started*, …/v2/get-started; read 2026-11-09. [seat] With the door, "the application" is ComChatX's LwA client. A Stream v2 destination is therefore registered to ComChatX's application, not to the seller. The data lands in an AWS account, not in a reply the door returns.

**RULE.** How often Stream v2 delivers. The GA note and the *Stream v2 overview* give "As frequently as every 15 minutes" (v1: hourly); the GA note gives `ads-converted-product-v1` "every 4 to 6 hours". The *Amazon Ads reporting overview* adds "automated backfill up to 70 days on subscription creation". [official] *Release notes* (2026-09-30); *Stream v2 overview*; *Amazon Ads reporting overview*; read 2026-11-09.

**RULE.** What Stream does not carry. The Stream v1 deprecation entry: "For messaging data (entity state changes and budget consumption notifications), use the Campaign Management API. For recommendation data, use the Recommendations API. These features are not carried forward in Stream v2." [official] *Deprecations*, read 2026-11-09. The campaign datasets of v1 went GA on 2025-12-01; their records mimic the v1 campaign-management read operations, and they carry a `version` that "is incremented when changes are made to the object". [official] *Release notes*, "Amazon Marketing Stream campaign datasets GA" (2025-12-01); *Stream: Sponsored ads campaign management datasets*; read 2026-11-09.

### T. Amazon Marketing Cloud (separate access)

**RULE.** AMC is a clean room with its own instances.

- Since 2025-09-16, "Amazon Marketing Cloud now available to all advertisers running sponsored ads campaigns", with instant self-service access.
- Creating an instance takes up to 300 seconds.
- "AMC terms and conditions must be accepted once in each region (NA, EU, and FE) where the AMC instance is going to be created and accessed", by logging into the AMC UI.
- Instance-level APIs were retired 2024-08-01 (the AMC overview: their use "may result in `410` errors"; *Deprecations*: "will return a `404` error").
- "raw event information cannot be exported"; results are "aggregated to generate anonymous reports that you can export".
- Automated approvals for instance creation and advertiser inclusion have run since 2025-02-10 ("AMC announces automated approvals for AMC instance requests").

[official] *Overview - Amazon Marketing Cloud*, https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/overview; *How does Amazon Marketing Cloud work*, …/guides/amazon-marketing-cloud/how-amc-works; *Get access to AMC using self-service APIs*, …/guides/amazon-marketing-cloud/get-started/instant-access-to-amc; *Instance management*, …/guides/amazon-marketing-cloud/admin/instance-management; *Release notes* (2025-02-10, 2025-09-16); *Deprecations*; read 2026-11-09.

**RULE.** AMC calls use their own headers:

- `Amazon-Advertising-API-AdvertiserId`: on the self-service page, "the sponsored ads entity ID for a sponsored ads account, or the global advertising account ID (beginning with `amzn1.ads-account.g.`)"; on *Instance management*, "The AMC account identifier";
- `Amazon-Advertising-API-MarketplaceId`: "For global advertising accounts, always use US (`ATVPDKIKX0DER`)."

`GET /amc/instances` lists instances. The MCP server's `amc` group has 10 tools (`execute_query`, `create_workflow`, `get_workflow_execution_download_url` and others). [official] *AMC instance management*; *MCP amc tools*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/amc.json; read 2026-11-09. [seat] A query result downloads from a URL, and the terms step is a UI step. Neither is a reply the door returns.

### U. Test accounts and the retired sandbox

**RULE.** Test accounts.

- "Advertising test accounts are a type of advertising account dedicated to testing. Test accounts do not serve ads or have active billing."
- They are created with `POST /testAccounts` and read with `GET /testAccounts`. The scope is `advertising::test:create_account`, in addition to `advertising::campaign_management` for use.
- `accountType` is `VENDOR` or `AUTHOR`. There is no seller type.
- The country enum lists AE, AU, BE, BR, CA, DE, EG, ES, FR, IT, JP, MX, NL, PL, SA, SE, SG, TR, UK, US; `AUTHOR` test accounts are offered only in US, UK, IT, ES, FR and DE (*Creating test accounts*).
- Creation status: `IN_PROGRESS`, `COMPLETED`, `FAILED`.

[official] *Test accounts overview*, https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/overview; *Create test accounts*, …/test-accounts/create-test-accounts; *Advertising test account* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json; read 2026-11-09.

**RULE.** What a test account does not do (*Test accounts overview*; *Using test accounts*):

- "Sponsored ads created in test accounts will not be served to shoppers," so there are no clicks, impressions, sales, ACOS or spend.
- Reports and brand metrics can be requested but "will not contain data".
- Budget rules and rule-based bidding "can be used to configure … but the rules will not take effect as the ads are not served."
- "Amazon Ads test accounts are enabled with auto-moderation", so every SB campaign is approved. The page warns that "Campaign approval with a test account does not necessarily mean that the same campaign created in a real advertiser account" will be.
- `IMAGE` assets only; no `VIDEO`.
- "**Lock Screen Ads**, **Posts**, and **Stores** are currently not supported."

[official] *Test accounts overview*; *Using test accounts*, …/test-accounts/use-test-accounts; read 2026-11-09.

**RULE.** The sandbox host is gone. `advertising-api-test.amazon.com` shut off 2022-06-28. Test accounts replace it. [official] *Deprecations*, read 2026-11-09.

### V. The Amazon Ads MCP server and skills

**RULE.** Release history (*Release notes*, read 2026-11-09):

- Open beta: the release note is dated 2026-02-18; Amazon's newsroom post "Introducing the Amazon Ads MCP Server" (Paula Despins, VP of Ads Measurement) is dated 2026-02-02 and says the server and tools "are available globally in open beta to Amazon Ads partners with active API credentials" ([official] https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta, read 2026-11-09).
- OAuth 2.1 since 2026-07-06; Claude Code is among the clients named in the OAuth guide.
- A Lite version at `/mcp/lite` since 2026-09-29, "a compact three-tool interface (`search_tools`, `describe_tools`, and `invoke_tool`)"; Amazon's unBoxed 2026 news page lists it among the event's announcements.
- Audience Discovery tools added 2026-10-30.

**RULE.** Endpoints and context.

- Regional endpoints: `https://advertising-ai.amazon.com/mcp`, `https://advertising-ai-eu.amazon.com/mcp`, `https://advertising-ai-fe.amazon.com/mcp`, and the `/mcp/lite` variants. "These URLs are not region agnostic."
- Authentication uses the same LwA access token and client id as the API.
- Account context:
  - Dynamic is the default; the model asks for the account identifiers per tool.
  - Fixed context needs `Amazon-Ads-AI-Account-Selection-Mode: FIXED` plus at least one account identifier header: `Amazon-Advertising-API-Scope` (a profile), `Amazon-Ads-AccountID` ("a DSP advertiser account, global account ID, or AMC instance ID") or `Amazon-Ads-Manager-AccountID`. "Please note that not all three account identifier headers need to be included, but at least one is required." "Please note that not all tools work on manager account scope."

[official] *MCP overview*, https://advertising.amazon.com/API/docs/en-us/mcp/mcp-overview; *MCP: Get started*, …/mcp/get-started; *MCP: Get started with Lite*, …/mcp/get-started-lite; *MCP: OAuth*, …/mcp/oauth; read 2026-11-09.

**RULE.** Tools, as published in the MCP tool specifications at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/<group>.json` (read 2026-11-09):

| Group | Tools | Examples |
|---|---|---|
| `campaign_management` | 32 | `create_singleshot_sp_campaign`, `add_country_campaign`, `update_target_bid`, `update_campaign_budget`, `update_campaign_state`, `check_product_eligibility`, `query_portfolio`, `create_singleshot_portfolio`, `create_bid_adjustment_rule` |
| `reporting` | 6 | `create_report`, `retrieve_report`, `delete_report`, `create_campaign_report`, `create_inventory_report`, `create_product_report` |
| `account_management` | 7 | `query_advertiser_account`, `create_advertiser_account`, `update_account_timezone`, `update_account_currency` |
| `amc` | 10 | `execute_query`, `create_workflow`, `get_workflow_execution_download_url` |
| `audience_discovery` | 3 | `list_audiences`, `get_audience`, `list_audience_categories` |
| `billing` | 4 | `list_invoices`, `list_invoice_summaries` |
| `inventory_management` | 10 | DSP deals and seats |
| `eligibility` | 2 | `product_list`, `programs` |

The spec files for `recommendations`, `insights`, `brand_stores`, `audiences`, `user_management` and `amc_workflow` answered `NoSuchKey` at those names.

The overview divides tools into two kinds:

- "Standard tools": "Deterministic actions to achieve an outcome", for example "end-to-end campaign creation (multiple API calls performed by a single tool)".
- "Expert tools": "Inference behind the" tool. The first is the AMC SQL Generator, in closed beta.

A "Skill" is "a pre-defined prompt definition provided by Amazon Ads that guides AI applications through Amazon Ads workflows and tool usage". [official] *MCP overview*; *MCP skills: Get started*, …/mcp/skills/get-started; read 2026-11-09.

**RULE.** The skills library is served from the Ads API hosts: `GET https://advertising-api{,-eu,-fe}.amazon.com/skills`, with "the same `Amazon-Ads-ClientId` and `Authorization` headers as the MCP server". The `ads-api-migration` skill (2026-11-02) helps coding agents move integrations to v1. [official] *MCP skills: Get started*; *MCP: AI migration skills*; read 2026-11-09. This seat did not call it (an Ads API host). [seat] It sits on the origins the door reaches.

### W. Rate limits and 429

**RULE.** The 429 contract. Verbatim from *Rate limiting*: "When this happens, you will receive a response with the code `429`. Contained within that response is a `Retry-After` header. The `Retry-After` value is the number of seconds that you should wait before submitting another API call. Rate limiting will occur dynamically based on the overall system load." [official] *Rate limiting*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/rate-limiting, read 2026-11-09. (The older copy at `guides/get-started/rate-limiting` answered 404 on the markdown host on 2026-11-09.)

**RULE.** Limits are dynamic and mostly unpublished.

- "Rate limits in the Amazon Ads API are dynamic and based on system load."
- The Well-Architected Framework defines a TPS limit as "set at the regional level for each API endpoint".
- For v1 campaign management at launch, "API rate limits (TPS) will be per each ad product."
- For reporting v1, limits are per client id on two pages and per advertiser on two others (section R).
- Where Amazon does publish numbers, they are for single surfaces: Stream v2 subscription operations at 25 per second; exports at 5 in-progress jobs per endpoint.
- Report limits follow the regional report queue: "Rate limits in the Sponsored Products, Sponsored Display, and Sponsored Brands reporting endpoints change with usage levels. We decrease during high usage times and increase them during low usage time."

[official] *Rate limiting*; *Well-Architected Framework: Fundamental component*; *Campaign management overview*; *Reporting v1: Limits and best practices*; *Stream v2: Limits*; *Exports FAQ*; read 2026-11-09.

**GUIDANCE.** Which errors to retry, and how (*Rate limiting*):

- Three error classes: server (5xx), throttling (429), and client (other 4xx), the last to be investigated "before retrying".
- "In general, you should retry requests that receive server or throttling errors. When retrying your requests, use an exponential backoff algorithm." Its example: back off 2 seconds, then 4, then 8; "You should implement a maximum delay interval, as well as a maximum number of retries".
- For reports: "Dynamic rate limits are unlikely to change over short time periods. Therefore, choose longer backoff periods for report generation."
- Other GUIDANCE on the page:
  - prefer exports to thousands of list calls;
  - avoid extended list calls (5x weight);
  - avoid reporting during high-usage times.

**GUIDANCE.** The Well-Architected Framework's backoff example, quoted as Amazon's illustration and not as a rule:

- an initial delay "for example, 1 second";
- "double the delay";
- "add a random jitter value … between 0 and the current delay amount";
- optionally a "maximum delay … for example, 60 seconds";
- "a limit on the number of retry attempts, for example, 5 or 10 attempts".

It adds: "Implement similar logic in your workload when calling services that are idempotent and where retries improve your client availability." [official] *Well-Architected Framework: Fundamental component*, read 2026-11-09. [seat] Section F shows sponsored ads creates carry no idempotency key; the *Rate limiting* page's retry advice names no such condition, while this sentence of the framework does.

**RULE.** Throttling in a 207 body. SP v3 can report throttling per item (`THROTTLED` in the error family), and v1 carries `TOO_MANY_REQUESTS` as an error code inside the body as well as a 429 status. [official] *Sponsored Products* model; *Amazon Ads API v1* model; read 2026-11-09.

### X. Figures from *Limits, constraints, and quotas* (for human readers only)

*Limits, constraints, and quotas*, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, read 2026-11-09. A skill reads the live page or the per-operation error bounds (`lowerLimit`/`upperLimit` in SP v3 errors).

- **Service P99s:**
  - synchronous CRUD: 30 s;
  - impression or click event to availability via API: 12 h;
  - impression or click invalidation: 72 h;
  - async report generation: 15 min;
  - async snapshot generation: 15 min.
- **Bids**, per marketplace and ad product, min/max in local currency. Examples: US SP 0.02/1000 USD; JP SP 2/100000 JPY; IN SP 1/5000 INR; IE SP 0.02/1000 EUR. The page notes: "The min/max amounts in the UI for non-US countries differ from those in the API (typically, the API max is lower than the UI max)." [seat] The EG SP row reads 0.15/5.50 EGP, out of line with its SD column (0.15/7400), and the SB columns' header and rows do not line up. The table is hand-kept.
- **Budgets:** SP daily min/max per marketplace, for example US 1/1000000 for seller and vendor. There are separate SB and SD tables, and SD default budgets.
- **Keywords:**
  - "The maximum length of characters in a keyword is **80**."
  - Up to 10 parts for a positive keyword, 4 for a negative, and 10 for `negativeExact`.
  - "The reserved phrase `Automatically Selected Keywords` is not accepted as a keyword."
  - Rules for `.`, `-`, `+` and paired `"`.
- **Names:** "The maximum length of a campaign name is 128 characters for sellers and 116 characters for vendors. The maximum length of an ad group is 255 characters." The page lists the valid character ranges.

### Y. Deprecations and sunsets, 2025–2027

From *Deprecations* (https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations) and the release notes, read 2026-11-09. Dates are as Amazon gives them. Past dates are recorded because old code and old guides still name the paths.

| Date | What | Replacement |
|---|---|---|
| 2025-03-01 | `/v2/portfolios` shut off | Portfolios v3 |
| 2024-03-27 / 2025-05-15 | SP v2 ad-group and keyword bid recommendations (2024-03-27); `/v2/sp/targets/bidRecommendations` and the v3 theme-based bid recommendation content type (2025-05-15) | `/sp/targets/bid/recommendations` current versions |
| 2025-09-30 | DSP legacy campaign, creative and reporting APIs shut off | As listed on *Deprecations* (DSP, outside this file) |
| 2025-10-30 / 2025-12-31 | SB v3 campaigns to be migrated to v4 (zero-impression pre-Oct-2022 / active) | SB v4 |
| 2025-12-01 | Campaign Diagnostics API (`POST /diagnostics/campaigns/issues`) shut off; new users refused from June 20 | None named in the entry read; [seat] v1 delivery reasons and v3 serving status carry the same kind of signal |
| 2025-12-15 | Legacy SB moderation endpoint shut off | `/moderation/results` |
| 2025-06-03 → 2025-06-16 / 2025-07-31 | Brand Posts (`/bp/v2/posts`) deprecated, then shut off | None |
| 2026-01-27 → June 2026 | SP v2 legacy APIs including suggested keywords deprecated, then shut off | Keyword recommendations; v3 |
| 2026-06-01 | `/v2/stores` shut off | `/brand/stores/v1/storePages/list` |
| 2026-06-15 | No new negative bid adjustments for SB placement groups (moved from 2026-02-02) | Positive adjustments only |
| July 2026 | Legacy `/adsAccounts*` and `/dsp/advertisers*` deprecated (`Warning: 299`) | v1 advertiser accounts |
| 2026-07-30 | Refresh tokens issued from this date expire 365 days after consent | Re-consent |
| August 2026 | SB `productCollection` ads map to manual collections | SB collections |
| 2026-11-10 | SB v2 `searchTermImpressionShare` and `searchTermImpressionRank` return null | — |
| 2026-12-17 | SB category benchmark APIs (`GET /benchmarks/brands`, `POST /benchmarks/brandsAndCategories`, …) stop | "Migrate to Unified Reporting for benchmarks metrics" (benchmarks reporting GA 2026-05-18) |
| January / February 2027 | SB product collections error / "no longer supported" (two notes) | SB collections |
| 2027-06-30 | Reporting v3, Sponsored Ads v2 reporting, Stream v1 stop | Reporting v1, Stream v2 |
| July 2027 | Legacy account APIs answer 404 | v1 advertiser accounts |

The Well-Architected Framework tells integrators to "Adhere to version changes, manage compatibility updates, and follow the Amazon Ads deprecation policy", linking the *Deprecations* page. [official] *Deprecations*; *Well-Architected Framework: Fundamental component*; read 2026-11-09.

**Dates to treat with care.**

- The release notes index carries an entry "Review Requests API (beta)" dated November 16, 2026, a week after this reading, in the United States. It is "Available for products with fewer than 1,000 total reviews", and "the advertiser pays only when a shopper leaves a rating or review". [seat] It is recorded as Amazon dated it. Its subject (`SPCustomerActionType: REVIEW_REQUEST` in the merged SP v1 model) belongs to `areas/launch.md`.
- Other 2026 notes that touch this surface: "Events API now generally available" (2026-10-15, `POST /adsApi/v1/create/events`, off-Amazon conversion events); "Choose whether to include performance data in Sponsored Ads exports" (2026-09-09) concerns bulk-operations exports in the console, not the Exports API.
- The SB placement-group deprecation appears under two dates in two notes; the later one stands.

### Z. Audiences: where audience ids come from (gap fill 2026-11-09)

Three places in the sponsored ads surface take an audience id:

- Sponsored Products audience bid adjustments: SP v3 `dynamicBidding.shopperCohortBidding[]` and v1 `bidAdjustments.audienceBidAdjustments[]`.
- Sponsored Brands audience bid adjustments: SB v4 `bidding.shopperCohortBidAdjustments[]` and the same v1 field.
- Sponsored Display audience targets: `audience(audienceSameAs=<id>)` in SD v3 targeting expressions.

Amazon documents four families of operations that list audiences. Each names its own ad products, and no page read here says whether their ids are interchangeable.

**RULE. Audiences discovery** (*Audiences discovery* model, `https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json`, listed in `contracts.json`; read 2026-11-09):

| Operation | Media type | Headers in the model | Body | Paging |
|---|---|---|---|---|
| `POST /audiences/list` (`listAudiences`) | `application/json` | `Amazon-Advertising-API-ClientId` (required), `Amazon-Advertising-API-Scope`, `Amazon-Ads-AccountId` ("Send either this header or `Amazon-Advertising-AccountId` (legacy) — not both") | `adType`: `DSP`, `SD` or `ST`; `countries` (exactly one ISO code, "must be specified if the advertiser does not have an associated country"); `filters[]` of `{ field, operator: EQ \| NOT_EQ, values[] }` with `field` one of `audienceName` ("a broad match filter"), `category`, `categoryPath`, `audienceId`, `status` | query `nextToken`, `maxResults` 1–250, default 10; query `canTarget=true` returns "only targetable audience segments"; query `advertiserId` "required for the DSP adType, but optional for the SD adType" |
| `POST /audiences/taxonomy/list` (`fetchTaxonomy`) | `application/json` | as above | `adType`, `categoryPath[]`, `countries` | `maxResults` default and maximum 250 |

- Each audience returns `audienceId`, `audienceName`, `category`, `subCategory`, `description`, `status` (`Active`, `Deactivated`, `Deprecated`, `Failed`, `Pending`, `Processing`), `createDate`, `updateDate` and `forecasts.inventoryForecasts`. For SD the forecast is `dailyReach`, "The forecasted unique devices reachable daily for the inventory type."
- Each taxonomy node returns `category` and `audienceCount`.
- Permissions: `advertiser_campaign_edit`, `advertiser_campaign_view`, `campaign_edit`, `ads_planner_internal_edit`, `ads_planner_edit`.
- `adType` has no `SP` and no `SB` value.

The *Sponsored Display audience targeting* guide describes the pair in order: "This API does not return the audience segments; instead, you use the category path from this API to call the audience discovery API to discover audiences". Its examples send the profile in `Amazon-Advertising-API-Scope` with `Content-Type: application/json` and `"adType": "SD"`. The guide also documents audience overlap: `GET /insights/audiences/{audienceId}/overlappingAudiences?adType=SD`, which "will return the top 30 audiences that overlap with the selected audience" (*Audience insights* model `Insights_prod_3p.json`, response `application/vnd.insightsaudiencesoverlap.v2+json`). [official] *Audiences discovery* model; *Audience insights* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json; *Sponsored Display audience targeting*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/audience-targeting; read 2026-11-09.

**RULE. Targetable Entities** (`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/TargetableEntities_prod_3p.json`, `info.title` "Targetable Entities", version 3.0; **not listed in `contracts.json`**, fetched by plain GET; read 2026-11-09):

- `POST /targetableEntities/list` (`ListTargetableEntities`) and `POST /targetableEntities/paths/list` (`ListTargetableEntityPaths`).
- Request and response media type: `application/vnd.Mindreader.TargetableEntitiesResource.v1+json`.
- Headers in the model: `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope`, `Amazon-Advertising-AccountId`.
- Permissions: `advertiser_campaign_edit`, `advertiser_campaign_view`.
- Body:
  - `adProduct` is the only required field: `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS` or `SPONSORED_TELEVISION`;
  - `targetTypeFilter[]`: `AUDIENCE`, `CONTENT_CATEGORY`, `PRODUCT_CATEGORY`, `PRODUCT_CATEGORY_AUDIENCE` (empty means all);
  - `pathsFilter` (up to 10 paths of up to 10 strings each);
  - `searchQueryFilter`;
  - `productCategoryIdFilter[]` and `parentBrowseNodeIdFilter[]` (browse node ids, up to 1000);
  - `locale`;
  - `maxResults` up to 250, and `nextToken`.
- Each `TargetableEntity` carries `audienceId`, `audienceResolved` (the name), `audienceTooltip`, `path` and `targetType`; the reply carries `totalResults`.

The SP v3 and SB v4 models name this operation as the source of audience ids for bid adjustments. The SB v4 `AudienceSegmentType` enum, verbatim: `SPONSORED_ADS_AMC` audiences "can be retrieved using the Discovery API ListTargetableEntities with parameters; `adProduct`=`SPONSORED_BRANDS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "AMC"]]`", and `BEHAVIOR_DYNAMIC` (Amazon-built) audiences with `pathsFilter` `[["Audience Category", "Custom-built", "Product"]]`. "Only the audiences retrieved using these filters are usable." The SP v3 model gives the same with `adProduct`=`SPONSORED_PRODUCTS`. It marks `audienceSegmentType` "DEPRECATED: This field is no longer used and any provided value will be ignored. The audience type is automatically determined … Audience IDs are guaranteed to be unique across all audience types". The *Sponsored Brands shopper cohort bidding* guide calls this operation "the Audience Discovery API" and shows `POST targetableEntities/list` with `{"adProduct": "SPONSORED_BRANDS"}`. [official] *Targetable Entities* model; *Sponsored Products* model; *Sponsored Brands v4* model; *Shopper cohort bidding* (SB), https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/bidding/shopper-cohort; read 2026-11-09.

**RULE. The bid-adjustment fields that take the id** (models read 2026-11-09):

| Surface | Field | Shape and bounds |
|---|---|---|
| SP v3 campaign | `dynamicBidding.shopperCohortBidding[]` (up to 10 items) | each `{ shopperCohortType: AUDIENCE_SEGMENT, percentage: 0–900, audienceSegments: [ { audienceId, audienceSegmentType } ] }`, `audienceSegments` exactly one item. Model text: "The percentage value set is the percentage of the original bid including any other bid adjustments such as `placementBidding`. For example, a `placementBidding` with 50% adjustment on a $1.00 bid would increase the bid to $1.50, and a `shopperCohortBidding` with 100% adjustment would further increase the bid to $3.00." `siteRestrictions` "don't support shopperCohortBidding setting". |
| SB v4 campaign | `bidding.shopperCohortBidAdjustments[]` | `{ shopperCohortType: AUDIENCE_SEGMENT, percentage: 0–900, audienceSegments: [1 item] }`. The SB guide: "We only allow one audience group per one campaign." |
| v1 campaign (cross-product) | `bidAdjustments.audienceBidAdjustments[]` (at most 1) | `{ audienceId, percentage }`, beside `placementBidAdjustments` (up to 4) and `creativeBidAdjustments` (up to 2, "Range of bid adjustment value would be 0:900"); `shopperSegmentBidAdjustments` is a "Legacy SB field (marked for deprecation)". |
| SP v3 recommendations | `ShopperCohortBiddingRecommendation` | `action` `ADD`/`REMOVE`/`UPDATE`, `percentage` "basis points, e.g., 900 = 9%", maximum 900. [seat] This recommendation's `percentage` is described in basis points, while the campaign field of the same name is a percentage up to 900. The two descriptions do not match. |

[official] *Sponsored Products* model; *Sponsored Brands v4* model; *Amazon Ads API v1* model; *Shopper cohort bidding* (SB); read 2026-11-09.

**RULE. Release notes on the audiences** (*Release notes*, read 2026-11-09):

- 2024-10-14, "Help increase engagement with advertiser-defined audiences through sponsored ads bidding controls": SP and SB bid controls for AMC-built audiences, retrieved through the Targetable Entities API.
- 2025-02-28 and 2025-03-24: the Amazon-built "New-to-brand shoppers" audience for SB bid boosting, preview and then worldwide ("shoppers who have not purchased from the brand in the last 12 months").
- 2025-03-12, "Preview: Introducing Amazon-built audiences for bid boosting in Sponsored Products": "Purchased brand products", "Clicked or added brand product to cart" and "Affinity for similar products". It is marked "This capability is in preview only."
- 2025-08-22: SB adds "Purchased brand product" and "Clicked or Added brand product to cart".

**RULE. v1 audiences (beta).** The *Amazon Ads API v1 betas* model (`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p_BETA.json`, listed in `contracts.json`) has three audience operations:

- `POST /adsApi/v1/query/audiences`: "Search and list audiences for an advertiser". Its filters:
  - `adProductsFilter.include` (exactly one of `AMAZON_DSP`, `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS`, `SPONSORED_TELEVISION`);
  - `audienceIdFilter` (up to 100);
  - `audienceCategoryIdFilter`;
  - `nameFilter` (`BROAD_MATCH`);
  - `countryCodesFilter` (one country, `GB` not `UK`).

  `maxResults` is 1–250 (default 10). Permissions: `advertiser_campaign_edit`, `audiences_view`, `advertiser_campaign_view`.
- `POST /adsApi/v1/retrieve/audiences`: "Retrieve a single audience by ID".
- `POST /adsApi/v1/query/audienceCategories`: "Browse the audience taxonomy. Returns the child category nodes beneath a given categoryPath, each with the count of available audiences for the requested adProduct". `adProductFilter` is required.

The MCP `audience_discovery` tool group (`list_audiences`, `get_audience`, `list_audience_categories`, added 2026-10-30, section V) has the same three-part shape. [seat] The MCP tool names line up one-to-one with these beta operations, but no page read here says the tools call them.

### AA. Creative assets and media upload (gap fill 2026-11-09)

**RULE. The asset library** (*Asset library* model, `https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml`, `info.title` "Creative assets", version 3.0, listed in `contracts.json`; read 2026-11-09). Its *Asset library overview* guide: it "currently supports video and image for Sponsored Brands, Sponsored Display, Amazon DSP, and Stores."

| Operation | Request media type | Response media type | Headers in the model |
|---|---|---|---|
| `POST /assets/upload` (`getUploadLocation`) | `application/json` | `application/vnd.creativeassetsuploadresponse.v3+json` | ClientId (required); `Amazon-Advertising-API-Scope`; `Amazon-Ads-AccountId` ("Use Amazon-Ads-AccountId to get resources at advertiser level. Use Amazon-Advertising-API-Scope and leave Amazon-Ads-AccountId empty to get resources at manager …") |
| `POST /assets/register` (`registerAsset`) | `application/json` | `application/vnd.creativeassetsregisterresponse.v3+json` | as above |
| `POST /assets/batchRegister` | `application/vnd.assetsbatchregisterrequest.v1+json` | `application/vnd.assetsbatchregisterresponse.v1+json` | ClientId, Scope (required) |
| `GET /assets/batchRegister/{requestId}` | — | `…assetsbatchregisterresponse.v1+json` or `…creativeassetsgetbatchregisterresponse.v3+json` | ClientId, Scope |
| `GET /assets?assetId=…[&version=…]` (`getAsset`) | — | `application/vnd.creativeassetsgetresponse.v3+json` | ClientId, Scope (required) |
| `POST /assets/search` (`searchAssets`) | `application/json` | `application/vnd.creativeassetssearchassetsresponse.v3+json` | ClientId, Scope (required) |

- `assetType`: `IMAGE` or `VIDEO`.
- `assetSubTypeList` (1–10): for `IMAGE`, `LOGO`, `PRODUCT_IMAGE`, `AUTHOR_IMAGE`, `LIFESTYLE_IMAGE`, `OTHER_IMAGE`; for `VIDEO`, `BACKGROUND_VIDEO`.
- Search takes `text`, `filterCriteria`, `sortCriteria` and `pageCriteria`. `filterCriteria` has `valueFilters` on `TAG`, `ASIN`, `CAMPAIGN_NAME`, `CAMPAIGN_ID`, `PROGRAM`, `ASSET_TYPE`, `ASSET_SUB_TYPE`, `APPROVED_AD_POLICY`, `ASSET_EXTENSION`, and `rangeFilters` on `SIZE` and `DATE_UPLOADED` ("timestamp in milliseconds").
- The model's operations list no "Requires one of these permissions" line.

**RULE. The upload sequence** (*Creating assets*, https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/creating-assets, read 2026-11-09): "Regardless of the type of creative, you need to make three calls":

1. `POST /assets/upload` with `{"filename": "logo.png"}`. The reply is `{"url": "https://al-na-184b9306-7f8a.s3.amazonaws.com/xxxxxxxxxxxxxx"}`. The model: "The upload location is short lived and expires in 15 minutes. The upload location only supports PUT HTTP Method to upload the asset content. If the upload location expires, API user will get `403` Forbidden response." The guide: "Using an unsupported extension will not result in error in this step, but you will encounter errors later."
2. "To upload your asset, use `PUT` on the URL returned in step 1", with the file's own `Content-Type` (`image/png`, `video/quicktime`) and the binary as the body. "If the asset uploads correctly, you receive a 200 response."
3. `POST /assets/register` with:
   - `url`, `name`, `assetType` and `assetSubTypeList` (all required);
   - optional `asinList`, `tags`, `versionInfo` (to version an existing `assetId`) and `skipAssetSubTypesDetection`;
   - `registrationContext`, required only for DSP;
   - `associatedSubEntityList`: "Amazon sellers must include their brand entity ID. You can find this using the `GET /brands` endpoint."

   The reply is `{ "assetId": "amzn1.assetlibrary.asset1.…", "versionId": "version_v1", "failedSpecChecks": [...], "programPolicyValidationsList": … }`.

After registration: "the asset is set to a `PROCESSING` status. Once the asset is in `ACTIVE` status, it can be used in a campaign", and the asset "can be in `PROCESSING` status up to 30 minutes". Amazon suggests "polling the `GET /assets` endpoint", and "If the transcoding process fails, the asset status moves to `INACTIVE`." Two notes on what the library does not check: "Asset library does not perform checks on eligibility for images", and "Creative asset library processing is not part of the moderation process." The guide's curl examples send `Content-Type: text/plain` on the JSON calls, while the model names `application/json`. [official] *Asset library overview*, https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/asset-library-overview; *Creating assets*; *Managing assets*, https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/managing-assets; *Asset library* model; read 2026-11-09.

**RULE. Where asset ids are used.**

- **SB v4 creatives:**
  - `videoAssetIds` (exactly one), with `originalVideoAssetIds` when `consentToTranslate` produced a translated video;
  - `brandLogoAssetID`/`brandLogoAssetId`, "The identifier of the brand logo image from the brand store's asset library";
  - `customImageAssetId`, "The identifier of image/video asset from the store's asset library", with up to 5 `customImages`;
  - `productImageAssetId`.

  These are created at `POST /sb/v4/ads/{video,brandVideo,manualCollection,autoCollection,storeSpotlight}` or as new creatives at `POST /sb/ads/creatives/{video,brandVideo,…}` (`application/vnd.sbAdCreativeResource.v4+json`).
- **SD v3 creatives** (`/sd/creatives`): *Sponsored Display creatives* builds a creative from "a headline, logo or custom image, where the logo and custom image are referenced using the `assetId`" and the `versionId` from the register step, and notes "Asset image height should not be smaller than 100px, width should not be smaller than 600px".
- **SB v3 Store library:** `GET /stores/assets` lists brand-logo assets and `POST /stores/assets` creates an image by `multipart/form-data` (section I).
- `GET /media/describe` polls SB media until `PendingDeepValidation` or `Available` (section I).

[official] *Sponsored Brands v4* model; *Sponsored Display creatives*, https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/creatives; *Sponsored Brands v3* model; read 2026-11-09. Test accounts accept `IMAGE` assets only (section U).

[seat] Step 2 is a `PUT` of a binary body to an S3 host (`al-na-….s3.amazonaws.com` in Amazon's examples), not to an Ads API origin. The door reaches only the three Ads API origins, so it cannot perform step 2. Through the door, a creative that needs a new image or video cannot be made end to end. A creative that reuses an asset already in the library can be made, because steps 1 and 3 and the creative create are calls on the Ads API origin. `POST /stores/assets` is on the Ads API origin but takes a `multipart/form-data` binary body. Whether the door's `--body` can carry a binary multipart body is not stated in `door.md`.

### AB. Stores, brands and brand identifiers beyond `GET /pageAsins` (gap fill 2026-11-09)

**RULE.** The families that touch a seller's Store and brand (models read 2026-11-09):

| Family | Operations | Model | Permissions in the model |
|---|---|---|---|
| Store insights | `POST /stores/{brandEntityId}/insights` (`application/vnd.GetInsightsForStoreRequest.v1+json`), `POST /stores/{brandEntityId}/asinMetrics` (`application/vnd.GetAsinEngagementForStoreRequest.v1+json`) | `Stores_prod_3p.json`, "Store insights" | `advertiser_campaign_edit`, `amazon_stores_view`, `amazon_stores_edit` |
| v1 brand stores (production) | `POST /adsApi/v1/query/brandStores` (required `storeNameFilter`, `maxResults` ≤ 30; returns `storeId`, `storeName`, `pageInfos`); `POST /adsApi/v1/query/brandStorePages` (required `storeIdFilter`, `editionIdFilter`, `pageIdFilter`; returns `content`, `editionId`, `pageId`, `pageType`, `storeEditionPublishId`); `GET /adsApi/v1/brandStoreEditions`; `POST /adsApi/v1/query/brandStoreEditionPublishVersions`; `POST /adsApi/v1/update/brandStoreEditionPublishVersions` | `AmazonAdsAPIALLMerged_prod_3p.json` | reads `amazon_stores_edit`/`amazon_stores_view` (`query/brandStores` also accepts campaign, creative and account permissions); the update `amazon_stores_edit` |
| v1 brand stores (beta) | `POST /adsApi/v1/update/brandStorePages` ("Update brand store page content") | `AmazonAdsAPIALLMerged_prod_3p_BETA.json` | `amazon_stores_edit` |
| Brand Home | `/brand/stores/v1/storePages/list`, named on *Deprecations* as the `/v2/stores` replacement | `brand-home` reference; model not read (section *Unreachable*) | — |
| SB v3 brands and pages | `GET /brands` (`brandEntityId` for sellers), `GET /pageAsins`, `GET`/`POST /stores/assets` | `sponsored-brands/3-0/openapi.yaml` | none listed |
| Brand associations (v1) | `POST /adsApi/v1/retrieve/brands` (`brandIds` 1–100), `POST /adsApi/v1/query/brandAdvertiserAssociations` | `BrandAidV2_prod_3p.json`, "Brand associations" | `account_view` on the association query |

The *Brand associations* contract describes "advertiser global brand identifiers. Global Brand IDs streamline brand identification by reducing multiple marketplace-specific IDs into a single identifier … a company can go from having 38 brand IDs to having a single global brand ID." A `Brand` carries `brandId`, `brandLogos` and `brandAlternateIds[]`. The only `alternateBrandIdType` is `LINEAR_TV_ID`. [seat] The global `brandId` here is a different identifier from the SB v3 `brandEntityId` (`ENTITY…`) that Store insights, the asset library and the SB v3 Store asset operations take. No page read here maps one to the other.

[official] *Store insights* model; *Amazon Ads API v1* merged and betas models; *Sponsored Brands v3* model; *Brand associations* model, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandAidV2_prod_3p.json; *contracts.json*; *Deprecations*; read 2026-11-09.

### AC. Localization (gap fill 2026-11-09)

**RULE.** The *Localization* model (`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json`, listed in `contracts.json`) "provides operations to localize data used when creating advertising campaigns. Depending on the type of data, localization may entail translating text, converting monetary amounts, or mapping an entity in a source marketplace to an analogous entity in one or more target marketplaces." Its operations:

| Operation | Media types (request and response) | What it does, in the model's words |
|---|---|---|
| `POST /keywords/localize` | `application/vnd.keywordlocalization.v1+json`, `.v2+json` | "Returns localized keywords within specified marketplaces or locales." |
| `POST /products/localize` | `application/vnd.productlocalization.v1+json`, `.v2+json` | "Localizes (maps) products from a source marketplace to one or more target marketplaces. The localization process succeeds for a given target marketplace if a product matching the source product can be found there and the advertiser is eligible to advertise it. Seller requests have an additional condition: the SKU of a localized product must match the SKU of the source product." |
| `POST /targetingExpression/localize` | `application/vnd.targetingexpressionlocalization.v1+json`, `.v2+json` | "Localizes (maps) targeting expressions from a source marketplace to one or more target marketplaces." Locales in the request return translations as well. |
| `POST /currencies/localize` | `application/vnd.currencylocalization.v1+json`, `.v2+json` | "Localizes currencies within specified marketplaces." |

Every operation marks three headers as required: `Amazon-Advertising-API-ClientId`, `Amazon-Advertising-API-Scope` and `Amazon-Ads-AccountId`. The "Authorized resource type" is "Global Ad Account ID, Profile ID". Permissions are `advertiser_campaign_edit` or `advertiser_campaign_view`. [official] *Localization* model, read 2026-11-09. [seat] All four are `POST`s that change nothing at Amazon. The door's gate reads them as changes (follow-up 9).

### AD. Sponsored Brands reserve share of voice (gap fill 2026-11-09)

**RULE.** Launched 2025-10-15 ("Drive top-of-search visibility and engagement by reserving branded share of voice through Sponsored Brands"). The feature "enables advertisers to secure top-of-search (TOS) Sponsored Brands placements for branded keywords at a fixed, upfront price … their ad will appear on Sponsored Brands top of search placement for those branded queries most of the time." The release note says the solution covers keyword recommendations, keyword validation, "real-time pricing", launch through console or API, and "automated invoices". [official] *Release notes* (2025-10-15), read 2026-11-09.

**RULE. Operations**, all `POST`, `application/json`, in the production merged v1 model, each with permissions `advertiser_campaign_edit` or `advertiser_campaign_view`:

- `/adsApi/v1/create/recommendations/sb` with `recommendationType: BRANDED_KEYWORD`;
- `/adsApi/v1/create/keywordReservationValidations/sb`: returns `isReservable` and, when false, `reservationRejectedReason`;
- `/adsApi/v1/create/brandedKeywordsPricings/sb`: `keywords` 1–1000, `startDateTime`, `endDateTime`, optional `advertisingDealId`; returns `keywordsPricing` and `rejectedKeywords`;
- `/adsApi/v1/create/reservedTargetPricings/sb`: up to 10 per request;
- `/adsApi/v1/{create,update,query,delete}/advertisingDeals/sb`: a deal has `name`, `startDateTime`, `endDateTime`, `price { priceType: FIXED_PRICE, value, currencyCode }`, `state`, `status` (`DRAFT`, `PROPOSED`, `MODERATION_APPROVED`) and `replacingDealId`; the query `maxResults` is ≤ 50;
- `/adsApi/v1/{create,query,delete}/advertisingDealTargets/sb`: a target is `BRANDED_KEYWORD`, "an exact match to the shoppers' search term"; the query requires `advertisingDealIdFilter`, with `maxResults` 100–1000.

[official] *Amazon Ads API v1* merged model, read 2026-11-09.

**RULE. Sequence and constraints**, from the *Reserve share of voice* guide (https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/reserve-share-of-voice, read 2026-11-09). The guide lists its steps: optional recommendation, validation and pricing; "Create a deal"; "Create at least five deal targets"; "Set `deal.state` to `PROPOSED`. This step triggers the internal pricing engine to calculate the price and assign it to the deal"; then "Create a campaign with `targetPGDealId`", through SB v4 `POST /sb/v4/campaigns`. The model and the guide's own sample request spell the campaign field `targetedPGDealId`. Its sample reply shows `costType: FIXED_PRICE`, `budgetType: LIFETIME`, `goal: BRAND_IMPRESSION_SHARE` and `kpi: TOP_OF_SEARCH_IMPRESSION_SHARE`. Other rules in the guide:

- "only the day portion (before "T") is used by the API and is interpreted as marketplace default time zone".
- "A deal in `PROPOSED` state cannot be modified."
- A `PROPOSED` deal can be deleted only "if `currentTime` is less than `deal.startDateTime - 12 hours`".
- "If you delete a deal, it also deletes associated deal targets and archives the associated campaigns."

[official] *Reserve share of voice*; *Sponsored Brands v4* model (`targetedPGDealId`); read 2026-11-09. [seat] The guide's step 7 says `targetPGDealId` and its sample says `targetedPGDealId`. The model has only the latter.

### AE. Promotion offers and rewards; the Events API (gap fill 2026-11-09)

**RULE. Promotion offers and rewards are billing promotions, not shopper deals.** The v1 betas model lists:

- `POST /adsApi/v1/query/promotionOffers`: "API to list the promotion offers for a global account". Filters: `marketplaceFilter` up to 30 countries and `statusFilter` (`AVAILABLE`, `IN_PROGRESS`, `MISSED`, `REWARDED`). `maxResults` ≤ 100.
- `POST /adsApi/v1/query/promotionRewards`: "Query promotion rewards for an advertiser account. Returns reward details including type, amounts, consumption tracking, and linked account information."
- `POST /adsApi/v1/create/promotionCodeRedemptions`: "API to create promotion code redemptions for affiliate codes".

All three need billing permissions: `nemo_transactions_view` or `nemo_transactions_edit` on the queries, `nemo_transactions_edit` on the create. [official] *Amazon Ads API v1 betas* model, read 2026-11-09. [seat] By their descriptions and permissions these are offers made to the advertiser's account, such as ad credits. They are not the Prime Day or coupon promotions a seller runs for shoppers, which are SP-API and Seller Central objects.

**RULE. Events API.** `POST /adsApi/v1/create/events` is in the production merged v1 model, with permissions `event_manager_view`, `event_manager_edit` or `MasterAccount_Manager`. The release notes:

- Open beta (2025-09-26): "send conversion events that occur outside of the Amazon ecosystem … via Server to Server integration". It was announced as "available to self-serve Amazon DSP advertisers world-wide", with conversions managed in "the Amazon DSP console Events Manager page".
- 2026-09-28: added `AREF_TOKEN` and `FIP` `matchKeys` and `deviceInfo.userAgent`.
- GA (2026-10-15): "the endpoint and request format are unchanged".

The event schema carries `consent` (`amazonConsent`, `geo.ipAddress`, `tcf`, `gpp`; "For EU advertisers, it is required to provide one of geo, amazonConsent, tcf, or gpp"), `countryCode` and `amazonAdEventKey` ("Amazon Traffic identifier for post attributed events"). [official] *Amazon Ads API v1* merged model; *Release notes* (2025-09-26, 2026-09-28, 2026-10-15); read 2026-11-09. [seat] The release notes describe Events as a DSP and Events Manager feature. No page read here ties it to sponsored ads attribution.

### AF. Measurement families and their paths (gap fill 2026-11-09)

Paths from the OpenAPI models, read 2026-11-09. "In contracts.json" means listed in Amazon's contract index.

| Family | Model (in contracts.json?) | Operations | Scope |
|---|---|---|---|
| Brand Metrics | `BrandMetrics_prod_3p.json` (yes) | `POST /insights/brandMetrics/report` (`application/vnd.insightsbrandmetrics.v1+json`, `.v1.1+json`); `GET /insights/brandMetrics/report/{reportId}` | Profile Scope header; open beta for brand-registered sellers and vendors in listed marketplaces (section Q) |
| Amazon Attribution | `AmazonAttribution_prod_3p.json` (yes) | `GET /attribution/advertisers`, `GET /attribution/publishers`, `POST /attribution/report`, `GET /attribution/tags/macroTag`, `GET /attribution/tags/nonMacroTemplateTag` | Profile Scope header (section Q) |
| Marketing Mix Modeling | `MarketingMixModeling_prod_3p.json` (yes) | `POST /mmm/v1/brandGroups/list`; `GET /mmm/v1/brandGroups/{brandGroupId}/products`; `GET /mmm/v1/brandGroups/{brandGroupId}/campaigns`; `POST /mmm/v1/brandGroupOverrides`, `…/list`, `…/delete`; `POST /mmm/v1/reports`; `POST /mmm/v1/reports/list`; `GET`/`DELETE /mmm/v1/reports/{reportId}` | Permissions `MasterAccount_Manager`, `MasterAccount_Viewer`, `ManagerAccount_Dev`, `MA_ReadOnly`. MMM API GA with 14 countries; 21 marketplaces since a later note ("expands to 21 marketplaces") |
| Brand Lift and other DSP studies | `Measurement_prod_3p.json`, "Amazon DSP measurement" (yes) | `POST /dsp/measurement/eligibility/{brandLift,audienceResearch,creativeTesting,omnichannelMetrics}`; `GET`/`POST`/`PUT /dsp/measurement/studies/brandLift`; `GET /measurement/studies/brandLift/{studyId}/result`; `…/studies/{audienceResearch,creativeTesting}` with `/{studyId}/result`; `…/studies/omnichannelMetrics`; `GET`/`DELETE /measurement/studies`; `GET`/`POST`/`PUT /measurement/studies/surveys`; `POST /measurement/planning/eligibility`; `/measurement/vendorProducts/*` | DSP only; no `SPONSORED_*` value anywhere in the model; brand-lift results carry `controlGroupRate` and `controlGroupResponseRate` |
| AMC administration | `AMCAdministration_prod_3p.json`, "AMC Administration" 3.0 (**no**, fetched by plain GET) | `GET /amc/accounts`; `GET`/`POST /amc/instances`; `GET`/`PUT`/`DELETE /amc/instances/{instanceId}`; `GET /amc/instances/{instanceId}/advertisers`; `GET`/`POST /amc/instances/{instanceId}/advertisers/updates`, `GET …/updates/{updateId}`; the `…/collaboration*` and `…/collaborations*` (AWS Clean Rooms) operations; `POST /amc/instances/{instanceId}/updateCustomerAwsAccount` | Headers include `Amazon-Advertising-API-AdvertiserId` (section T) |
| AMC on v1 (beta) | `AmazonAdsAPIALLMerged_prod_3p_BETA.json` (yes) | `POST /adsApi/v1/{create,query,retrieve,update,delete}/cleanRooms`; `POST /adsApi/v1/{create,query,retrieve,delete}/queries` | `amc_edit`, `amc_view`, `MasterAccount_*` |
| Events (off-Amazon conversions) | merged v1 (yes) | `POST /adsApi/v1/create/events` | section AE |
| Multi-touch attribution | No operation of its own | Fields in Reporting v1 (`POST /adsApi/v1/create/reports`, section R): the *Purchases (Amazon retail conversions)* field page lists 56 distinct `metric.multiTouch*` ids, for example `metric.multiTouchPurchases`, `metric.multiTouchPurchasesFromClicks`, `metric.multiTouchPurchasesHalo` and `metric.multiTouchCostPerPurchase` | Field meaning and eligibility belong to `beyond/metrics-and-attribution.md` |

The Brand Lift release note of 2023-10-09 names the same three DSP paths: "Create study: `POST /dsp/measurement/studies/brandLift`", "Update study details: `PUT /measurement/studies/brandLift`", "Get results: `GET /measurement/studies/brandLift/{studyId}/result`". [official] the models named; *Release notes* ("French advertisers can now measure brand marketing impact using Amazon Brand Lift", 2023-10-09; "Request Amazon Marketing Mix Modeling (MMM) feed via API"; "Marketing Mix Modeling (MMM) API now generally available"; "Marketing Mix Modeling (MMM) API expands to 21 marketplaces"); read 2026-11-09.

**RULE. No experiment, A/B, split-test or holdout operation exists for sponsored ads in the models read.** This seat searched every model downloaded on 2026-11-09 for `experiment`, `holdout`, `A/B test`, `split test`, `control group` and `incrementality`:

- the v1 production, merged and betas models;
- SP v3, SB v3, SB v4 and the `SponsoredBrands_prod_3p.json` copy, SD v3 and SD v1;
- Audiences, Targetable Entities, the creative asset library, Localization, Stores, Brand Metrics, Attribution, MMM, Measurement, AMC Administration and Brand associations.

The only hits are in the DSP *Measurement* model: brand-lift control-group rates, and DSP `CREATIVE_TESTING` and `AUDIENCE_RESEARCH` studies. The release notes index, the v1 release notes and *Deprecations* have no entry announcing a sponsored ads experiment or A/B operation. [official] the models and pages named, read 2026-11-09. [seat] An absence in the files read is not a statement by Amazon that none exists. Console features that no API model carries would not appear in this search.

### AG. Terms that bind a client application (gap fill 2026-11-09)

These are contract terms. They are recorded verbatim because an integrator that lands one seller's reports and exports under a single ComChatX client id is bound by them next to rate limits. They are not advice on how cx acts.

**RULE. Who may hold Ads API access.** *Amazon Ads API Policies*, Overview: "The Amazon Ads API is made available only to companies that do not operate a significant ecommerce business (e.g., an online shopping business or online comparison shopping service), a demand-side ad platform, or an ad network." [official] *Amazon Ads API Policies*, https://advertising.amazon.com/resources/ad-policy/api, read 2026-11-09.

**RULE. The Amazon Advertising API License Agreement** (https://advertising.amazon.com/API/docs/oas, "Last Updated: June 1, 2024", read 2026-11-09):

- Licence scope (§1): "solely for the purpose of sending and receiving information in connection with Amazon Advertising by or on behalf of the particular Amazon Advertising Participant that has expressly authorized you to do so."
- Policies (§2): "You must comply with all instructions and requirements related to the Program Materials in the Program Policies, including the Data Protection Policy and Acceptable Use Policy." The linked policy page (`https://advertising.amazon.com/API/docs/policy/en_US`) is a JavaScript shell and was not read (see *Unreachable*).
- Restrictions (§2), among them:
  - "(i) send multiple listings of identical products in the same feed or sending multiple feeds under different accounts";
  - "(j) generate fraudulent, repetitive or otherwise invalid clicks, impressions, queries or other interactions, whether through the use of automated applications or otherwise";
  - "(n) use information received in connection with the Program Materials to conduct any marketing efforts targeted at our existing advertisers or Amazon Advertising Participants";
  - "(o) use the Program Materials to contribute to, offer or promote external (non-Amazon) data services that vend data about Amazon".
- Quotas (§2): "We may, in our sole discretion, set a quota on your usage of Program Materials, and you will not attempt to exceed any such use-quota restrictions of which we have informed you. All licenses granted to you in this License Agreement will immediately and automatically terminate if you do not comply with any term or condition of this License Agreement."
- Confidentiality (§5.A): data "relating to us, the Program Materials or Amazon Advertising Participants that is not known to the general public" is Confidential Information. The licensee agrees "(b) you will not disclose any Confidential Information to any person or entity other than to the Amazon Advertising Participant to which such data or information relates", "(d) you will not collect any user information from any Amazon Sites or retrieve, extract, index or cache any portion of any Amazon Sites", and "(e) you will not use any Confidential Information for any purpose other than creating, managing, and reporting Amazon Advertising ad campaigns by or on behalf of the particular Amazon Advertising Participant that has expressly authorized you to do so."
- Personal data (§9, Compliance): "Other than as expressly permitted in any applicable Program-Specific Terms (such as the Amazon Attribution Agreement, or the Advertiser Audiences Agreement), you may not provide us any data which, alone, or when combined with other personal or identifying information … can be used to identify, contact, or precisely locate a natural person".
- Amendment (§10): "We may amend any of the terms and conditions contained in this License Agreement (including any Program Policies) at any time and in our sole discretion. Any changes will be effective upon the posting".

**RULE. The Amazon Ads Partner Network Policies** (https://advertising.amazon.com/resources/ad-policy/partner-network-policies, read 2026-11-09). These are "binding on all partners, developers, vendors, agencies, and other entities … approved to access and interface products, services, tools and APIs". The glossary defines "Amazon Data" as "Any data, reports, analysis, content or other materials relating to or derived from Amazon Ads." The policies:

- 3.1: "comprehensive administrative, physical, and technical safeguards conforming to industry data security standards such as encryption, access controls".
- 3.2: "a documented and publicly accessible process for prompt submission, tracking, response and resolution of data privacy, security vulnerability notifications, and incidents".
- 4.3: "You may not place Amazon Data on public websites, search engines, or environments, aggregate it commercially, or monetize Amazon Data in any way beyond the approved product/service integration".
- 4.5: "You may not cache, store, retain or maintain any Amazon Data beyond its intended use for providing the approved product/service functionality interfacing with Amazon Ads, unless expressly permitted by Amazon."
- 4.7: no sharing with third parties "except to approved Service Providers operating under confidentiality agreements".
- 4.8: access limited to personnel "having a strict need-to-know".
- 4.9: "Sharing or combining Amazon Data with any other third-party data sources is strictly prohibited without express prior written approval from Amazon."
- Usage Guidelines: "You shall only access the minimal Amazon Data required … Upon termination of your agreement with Amazon Ads, or upon request, you must promptly delete and discontinue all use of Amazon Data. You must delete Amazon Data when no longer required for a Permitted Use".
- 4.14: "clear and conspicuous notice to users regarding the specific Amazon Data accessed or used by your product or service, as well as the purposes".
- 4.18: "You are required to respect and conform to all Throttling Limits specified by Amazon".
- 4.19: "robust data validation and error-handling mechanisms … for any products, services, or applications that impact the integrity of user advertising campaigns".
- 5.1: "You shall not solicit, collect, store, proxy, buy, sell or transfer Amazon login credentials or other authentication credentials of End Users".
- 5.3: "You may only take actions or operate products/services on behalf of End Users who have granted you express and verifiable authorization and permissions to do so."
- 5.4: "Amazon Ads reserves the right to rotate or expire previously issued Credentials".
- 7.1: updates are published "at least 30 days prior to taking effect".

**RULE. The SP-API Data Protection Policy and Acceptable Use Policy** bind the sibling package `cx-amazon-sp-api`, not the Ads door. They are recorded because ads analysis in this pack joins SP-API sales and traffic data.

- *Data Protection Policy* (https://sellercentral.amazon.com/solution-provider/policy?policyType=DPP&locale=en_US, read 2026-11-09). It "is applicable to all systems that store, process, or otherwise handle data vended and retrieved from the Amazon Services API":
  - MFA "for all user accounts";
  - programmatic credentials "encrypted at rest … and rotated at least once every twelve (12) months";
  - encryption in transit "such as TLS 1.2 or higher";
  - notify "security@amazon.com within twenty four (24) hours of detecting a Security Incident";
  - "permanently and securely delete all Information … within thirty (30) days of the earliest of" Amazon's notice, the customer's revocation of authorization, the provider's own finding that it is no longer authorized, or termination, by "industry-standard sanitization processes such as NIST 800-88";
  - "retain Information only for so long as, and to the extent, such retention is strictly necessary";
  - "Data Attribution: Solution Provider must store Information in a separate database or implement a mechanism to tag and identify the origin of all data in any database that contains Information";
  - PII retained "no longer than 30 days after order delivery", and encrypted at rest with "at least AES-128 or RSA with 2048-bit key size";
  - logs retained "at least twelve (12) months".
- *Acceptable Use Policy* (https://sellercentral.amazon.com/solution-provider/policy?policyType=AUP&locale=en_US, read 2026-11-09):
  - 2.4: "Be explicit about any calculations and the use of models such as artificial intelligence in the service you provide, their accuracy and data freshness."
  - 2.9: "Design your Application to respect per-Authorized User throttling quotas".
  - 2.10: "Implement data integrity and validation checks within your Application for any analytical processing (e.g. AI models for insights, automated decision-making) that has material impact on an Authorized User's business."
  - 3.5: "Access keys that do not make a successful call in 90 days will be deleted".
  - 3.8: "Do not request access to or retrieve Information that is not necessary for your Application's functionality."
  - 3.10: "Do not attempt to circumvent throttling quotas through the creation of multiple Solution Provider accounts or applications."
  - 4.4: "Do not aggregate data across Authorized Users' businesses or customers obtained through the Amazon Services API to provide or sell to any parties, including competing Authorized Users."
  - 4.6: "Do not disclose Information, individually labelled or aggregated, to other Application users, affiliated entities or any outside parties, unless required to perform acceptable Authorized User activities for Authorized Users that authorized your Application."
- *SP-API changelog*, "Updates to the Data Protection Policy and Acceptable Use Policy" (https://developer-docs.amazon/sp-api/changelog/updates-to-the-data-protection-policy-and-acceptable-use-policy, read 2026-11-09), effective 2025-11-25: "Added that non-PII data must not be stored for longer than with 18 months, unless longer retention is legally required" (Amazon's wording). [seat] The DPP text served on 2026-11-09 has no 18-month figure. Its retention sentence is "strictly necessary". The changelog and the live policy differ on this point, and the live policy is the binding text.

[official] the pages named. [seat] None of the Ads pages read on 2026-11-09 states a fixed retention period for Ads data, an encryption standard, or a breach-notification window. Those figures appear only in the SP-API DPP. The Ads Data Protection Policy that the License Agreement names could not be read (*Unreachable*).

## What practitioners add

Web search was not available to this seat for this file, so the practitioner layer is narrower than in sibling files. It comes from three kinds of source, each fetched by known URL:

- developer field reports on Amazon's own public documentation repository, `amzn/ads-advanced-tools-docs` on GitHub, where Amazon staff answer as CONTRIBUTOR;
- the documentation of two data-pipeline vendors that run Ads API connectors at scale (Airbyte, Fivetran);
- the open-source client `denisneuf/python-amazon-ad-api`.

A field report is one developer's observation on their own accounts. It is stated as theirs, with login and date. It is not Amazon's rule unless an Amazon contributor confirms it in the thread.

### Throttling as integrators meet it

- **Per-seller 429 that does not clear.** `RianKoja` (issue #422, 2025-12-04, first noticed mid-September 2025) reports that every change-history request for one seller account (marketplace `A1F83G8C2ARO7P`) returned an immediate 429 "even after 24+ hours without any calls", while other sellers on the same application were not throttled. The response carried `x-amzn-ErrorType: AccessDeniedException` and `amazon-advertising-api-throttled: true`. The excerpt shows no `Retry-After`. No Amazon reply by 2026-11-09. [opinion] `RianKoja`, https://github.com/amzn/ads-advanced-tools-docs/issues/422, read 2026-11-09.
- **Report-creation 429 across regions.** `joexu-svg` (issue #501, 2026-09-18) reports persistent 429 on `POST /reporting/reports` for SB v3 in both NA and EU. `fredrickdave` adds (2026-09-24) that "Most requests fail with 'Report generation failed due to an internal error'" and that email to Amazon's API support had no answer after a week. [opinion] `joexu-svg`, `fredrickdave`, https://github.com/amzn/ads-advanced-tools-docs/issues/501, read 2026-11-09.
- **MCP gateway 429 with no Retry-After.** `ciocca-dev` (issue #436, 2026-03-07) reports that the MCP tool `reporting-create_campaign_report` on `advertising-ai-eu.amazon.com/mcp` returned an HTML 429 page from "openresty" about 23 seconds after a first call, and again after about 80 seconds, with "No Retry-After header". The same report request succeeded on the REST API directly, "which suggests the rate limit is enforced at the MCP proxy layer". Closed without a comment. [opinion] `ciocca-dev`, https://github.com/amzn/ads-advanced-tools-docs/issues/436, read 2026-11-09.
- **Connector defaults.** Airbyte's connector:
  - waits the `Retry-After` seconds on 429;
  - retries 500, 502, 503 and 504;
  - stops a stream if Amazon asks for a wait of 15 minutes or more;
  - runs 14 concurrent threads by default (range 2–20), to be reduced if throttled.

  The page states that Amazon publishes no specific numbers, and that report generation can take up to three hours. [opinion] Airbyte, *Amazon Ads source connector*, read 2026-11-09.

### Specification against behaviour

- **Id types.** `Lafetz` (issue #379, 2025-05-13): a target id was documented as an integer while the API returned a string. The Amazon contributor `kdwivedi13` confirmed on 2025-05-21 that "the target_id field is a string", and `jerirose` reported the document updated on 2025-06-03. Airbyte notes the same id fields are typed string in some streams and integer in others. [opinion] `Lafetz`, https://github.com/amzn/ads-advanced-tools-docs/issues/379; Airbyte; read 2026-11-09.
- **A required field that is not returned.** `vudathayajushi` (issue #525, 2026-11-05): `AdvertiserAccountStatus.statusMessage` is marked required in the v1 advertiser-accounts spec, but `query/advertiserAccounts` returns `status` with `statusCode` only. "Clients generated from the spec reject that payload because the required field is missing." [opinion] `vudathayajushi`, https://github.com/amzn/ads-advanced-tools-docs/issues/525, read 2026-11-09.
- **A budget update silently ignored (SD).** `zhangwg4apollo` (issue #475, 2026-07-21): the SD `SDCreateBudget` schema lacks `recurrenceTimePeriod`. Because `SDCampaignUpdate.budgets` references it, "The server silently ignores the entire budget object without returning an error, causing budget changes (e.g., updating `value` from 5.0 to 1.0) to never take effect." [opinion] `zhangwg4apollo`, https://github.com/amzn/ads-advanced-tools-docs/issues/475, read 2026-11-09. [seat] If this holds, a 207 success on an SD v1 budget update does not show that the budget changed. Only a read-back of the campaign does.
- **A pause that reverts (SP prompt extensions).** `AlexUnitix` (issue #524, 2026-11-03): setting `state = PAUSED` on a PROMPTS ad extension via `POST /adsApi/v1/update/adExtensions` succeeds with no errors, and an immediate query returns `PAUSED / NOT_DELIVERING / AD_EXTENSION_PAUSED`. "By the next day, the prompt is back to `ENABLED / DELIVERING`." Prompts paused in the console are returned as `ENABLED / DELIVERING`. [opinion] `AlexUnitix`, https://github.com/amzn/ads-advanced-tools-docs/issues/524, read 2026-11-09.
- **v1 payloads.** `CoderWeiAden` (issue #430, 2026-02-13) asked how to build a v1 SP campaign create. Amazon contributor `kdwivedi13` answered on 2026-07-24 with a sample that includes `autoCreationSettings.autoCreateTargets`, `budgets`, `optimizations` and `marketplaces`. [opinion] `kdwivedi13` (Amazon Ads docs contributor), https://github.com/amzn/ads-advanced-tools-docs/issues/430, read 2026-11-09.
- **SD v1 optimization goals.** In issue #481 (2026-08-05), `kdwivedi13` suggested `goal: CONVERSIONS` with `kpi: RETURN_ON_AD_SPEND` for an SD ad group with THEME targeting. `iYetaimei` reported that the API refused it: `kpi` must be one of `ADD_TO_CART`, `APPLICATIONS`, `CHECKOUTS`, `CLICKS`, `CONTACTS`, `LEADS`, `OTHER`, `PAGE_VIEWS`, `PURCHASES`, `REACH`, `SEARCH`, `SIGN_UP`, `SUBSCRIBE`. [opinion] `kdwivedi13`, `iYetaimei`, https://github.com/amzn/ads-advanced-tools-docs/issues/481, read 2026-11-09. [seat] An Amazon contributor's answer in the issues is not the spec. Here the API's own validation message was the authority.
- **No targeting-type field on ad groups.** `neyugn-yuh` (issue #499, 2026-09-11): v1 has no ad-group field that says whether an ad group uses product or keyword targeting. "The only available workaround is to inspect the first target in the ad group." [opinion] `neyugn-yuh`, https://github.com/amzn/ads-advanced-tools-docs/issues/499, read 2026-11-09.

### Reporting v1 as integrators meet it (detail in `method/reporting.md`)

- `mtsanko` (issue #476, 2026-07-22): around 2026-07-14/15, `matchedTarget.value` stopped returning customer search terms, retroactively, "on every advertiser account we manage". `searchTerm.value` "only returns rows that received **clicks**". So v1 "now has **no way to see search terms for un-clicked impressions**". [opinion] `mtsanko`, https://github.com/amzn/ads-advanced-tools-docs/issues/476, read 2026-11-09.
- `matthieuauger` (issue #467, 2026-07-01): for an EU global account, v1 reporting returned no rows for DE and GB, while FR, IT, ES and NL returned data and the classic per-profile reports had the DE and UK data. [opinion] `matthieuauger`, https://github.com/amzn/ads-advanced-tools-docs/issues/467, read 2026-11-09.
- Three more v1 reporting reports:
  - `bhaskardabhi-spreetail` (issue #456): duplicate rows for the same date and search term.
  - `cn-knight` (issue #453): no target or keyword id among v1 report fields; `targetId` is refused with "400013: field targetId has invalid format".
  - `wolendranh` (issue #439): Sponsored Television missing from v1 reporting.

  [opinion] GitHub issues #456, #453, #439, read 2026-11-09.

### The MCP server as integrators meet it

- `cn-knight` (issue #450, 2026-04-21): the tool `campaign_management-create_campaign_harvest_targets` "consistently returns a 504 Gateway Timeout error after approximately 30 seconds, regardless of the source campaign used". The request body named an `accessRequestedAccount` by `profileId` and `harvestRequests` with a `sourceCampaignId` and conditions such as `SALES >= 10`. [opinion] `cn-knight`, https://github.com/amzn/ads-advanced-tools-docs/issues/450, read 2026-11-09. [seat] The tool's name does not appear among the 32 tools of the published `campaign_management` specification read on 2026-11-09.

### Access, onboarding and permissions

- **Onboarding.** `Circadianrest` (issue #519, 2026-10-28) reports a Direct Advertiser application pending 29 days across four submissions (29 September, 6, 19 and 26 October), each answered by a "Registration Request Pending" email "promising a reply within three business days". `hrocks` (issue #523, 2026-11-02) reports a Partner Network request pending since 2026-09-29. Amazon's onboarding pages say "Review of your application may take up to 1 business day." [opinion] `Circadianrest`, https://github.com/amzn/ads-advanced-tools-docs/issues/519; `hrocks`, https://github.com/amzn/ads-advanced-tools-docs/issues/523; read 2026-11-09. [official] *Onboarding: Apply for access*, read 2026-11-09.
- **Scopes against permissions.** `jerirose` (Amazon contributor, issue #406): `amazon_stores_edit` "is actually not a scope -- it _can't_ be added to a client application. Rather, it is a user permission". [opinion] `jerirose`, issue #406, read 2026-11-09.
- **Ireland.** In issue #391 (2025-06-24), `salton4` wrote that IE "began being exposed in the profiles API towards the end of May" 2025, before its limits were documented. In issue #383, `jerirose` answered `xieyifeng-pacvue` (Pacvue) that IE bid and budget constraints would publish on 2025-06-25. She posted them on 2025-06-26 and confirmed them published. [opinion] `salton4`, https://github.com/amzn/ads-advanced-tools-docs/issues/391; `xieyifeng-pacvue`, `jerirose`, https://github.com/amzn/ads-advanced-tools-docs/issues/383; read 2026-11-09.

### Data pipelines

- **Fivetran** states report retention by product: "Sponsored Products 95 days, Sponsored Display 60 days, Sponsored Brands Version 2 60 days, Sponsored Brands Version 3 95 days", and 90 days for the SB benchmark report. Its daily rollback syncs re-read the attribution window. It quotes Amazon's documentation: "Only 14-day data is available for Sponsored Brands." It captures deletes for tables including SB keywords, SB product targets, SD targeting expressions and budget rules. [opinion] Fivetran, *Amazon Ads connector*, read 2026-11-09. Retention as such belongs to `method/reporting.md`.
- **Airbyte** caps start dates at 60 days back, uses a 3-day lookback for late-arriving data, and reads dates in the profile's time zone. It treats `invalid_grant` and `invalid_permissions` as configuration errors (9.2.11). It handles duplicate report requests answered 425 by reusing the named report or waiting (9.2.9). [opinion] Airbyte, read 2026-11-09.
- **`denisneuf/python-amazon-ad-api`** (205 stars; pushed 2026-11-09) runs automated "[Auto] Amazon Ads API contract updates" pull requests, two in the week of 2026-11-02 (#308 on 2026-11-05, #309 on 2026-11-06). Its README describes v1 as follows: it "is **not** split by product: every call targets the same resource and the product is selected in the request body with `adProductFilter`. It supersedes the per-product v3 endpoints." [opinion] `denisneuf/python-amazon-ad-api`, https://github.com/denisneuf/python-amazon-ad-api, read 2026-11-09. [seat] The contracts change weekly. A cached copy of a model goes stale within days, so the live contract is the reference.

## Published research

No academic paper read for this file addresses the Amazon Ads API surface itself: its write semantics, throttling or account model. [research] none read. The general literature this file's topics touch is engineering guidance rather than peer-reviewed research. Two examples are AWS's "Timeouts, retries, and backoff with jitter" (Amazon Builders' Library), which Amazon's Stream v2 limits page links, and RFC 9110's definition of idempotent methods. Neither was read in this session, and neither is cited as support for any position. Papers on sponsored-search auctions and attribution belong to `areas/bids-and-placements.md` and `beyond/metrics-and-attribution.md`.

## Stable enough for a skill

Each item is a mechanism or rule Amazon documents, unlikely to change within a skill's life. Figures stay at run time.

1. **Three regional hosts; data does not cross them.** Profiles are listed per host. A token from any LwA token host works on every host. (*API overview*; *Well-Architected Framework: Fundamental component*; *Authorization grants*.)
2. **A profile is one advertiser in one marketplace.** Sponsored ads calls name it with `Amazon-Advertising-API-Scope`. v1 reporting, v1 recommendations and Stream v2 name a global account (`amzn1.ads-account.g.*`) or a DSP advertiser in the body or in `Amazon-Ads-AccountId`. A Seller Central id is not an advertiser id. (*Profiles*; *Query advertiser accounts*; *Stream v2: Create a subscription*; *Recommendations API: How to*.)
3. **The API can do only what the authorizing user can.** The scope delegates the user's permissions. A view-only user's profiles appear only under `accessLevel=view`, and that user's writes are answered 401. (*Permissions*; *Profiles* model; issue #406.)
4. **Batch writes answer 207, item by item, by request index.** v1 adds `partialSuccess`. A 207 is not a success of every item. (*Well-Architected Framework*; *Amazon Ads API v1* model; *Sponsored Products* model.)
5. **Sponsored ads writes carry no idempotency key.** A repeated create can make a second entity. Only a seller's campaign names are unique per account. (Models read; *Sponsored Products v2* and *Sponsored Brands v3* models.)
6. **Archived is terminal.** In v1, SD v3 and SB v3, an archived entity cannot be re-enabled or edited. In SD v3 and SB v3 keyword/target paths, delete is archive. (*Amazon Ads API v1* model; *Sponsored Display v3* model; *Sponsored Brands v3* model; *Sponsored Products* model.)
7. **v1 is one ad product per call at launch, with per-product batch limits and per-product TPS.** (*Campaign management overview*; per-product v1 models.)
8. **429 carries `Retry-After` in seconds; limits are dynamic.** Amazon's guidance is to retry 5xx and 429 with exponential backoff and to investigate other 4xx before retrying. Report backoff is longer. (*Rate limiting*.)
9. **Bulk reads belong to exports, recurring metrics to Stream.** Exports are current-state snapshots with short-lived URLs. Stream v2 delivers Parquet to an S3 bucket and SQS queue in the integrator's AWS account. (*Exports FAQ*; *Rate limiting*; *Stream v2: Data delivery*; *Stream v2: Set up your destination*.)
10. **Change history covers SP and SB, 90 days, without the actor.** (*Change history* model.)
11. **Test accounts serve no ads and are vendor or author only.** Rules configure but do not act. SB auto-moderation passes everything. (*Test accounts overview*; *Using test accounts*; *Advertising test account* model.)
12. **Refresh tokens issued from 2026-07-30 expire 365 days after consent, fixed at consent.** (*Refresh tokens*.)
13. **The surface is being replaced by v1 on a published calendar.** Reporting v3, Sponsored Ads v2 reporting and Stream v1 stop 2027-06-30. Legacy account APIs answer 404 from July 2027. (*Deprecations*; *Release notes*.)
14. **Audience ids come from discovery operations, not from the campaign APIs.** SP and SB audience bid adjustments take ids that the SP v3 and SB v4 models say to read from Targetable Entities (`POST /targetableEntities/list`). SD audience targets take ids from `POST /audiences/list` with `adType: SD`. (*Targetable Entities* model; *Sponsored Products* model; *Sponsored Brands v4* model; *Audiences discovery* model; *Sponsored Display audience targeting*.)
15. **A new image or video enters the ads surface in three calls, and the middle one is a binary `PUT` to a pre-signed S3 URL** that expires in 15 minutes. The asset is usable only once it is `ACTIVE`. (*Creating assets*; *Asset library* model.)
16. **No sponsored ads experiment or holdout operation appears in Amazon's published models.** Control groups and creative-testing studies appear only in the DSP measurement model. (Models listed in section AF.)
17. **The Ads API licence ties every use of Ads data to the advertiser that authorized it.** The licence limits Confidential Information to "creating, managing, and reporting Amazon Advertising ad campaigns by or on behalf of the particular Amazon Advertising Participant that has expressly authorized you". The Partner Network Policies forbid combining Amazon Data with third-party data without written approval and require deletion when the data is no longer needed. (*Amazon Advertising API License Agreement*; *Amazon Ads Partner Network Policies*.)

## What cx must read at run time

Every figure in this file is for human readers. These are the operations and pages that carry the live values. Paths are relative to the region's origin unless a full URL is given.

| What | Where it lives | Operation or page | Fields |
|---|---|---|---|
| Which advertisers and marketplaces the grant reaches | Ads API, per region | `GET /v2/profiles` (no Scope header); `?accessLevel=view` for view-only; `?profileTypeFilter=seller` etc. | `profileId`, `countryCode`, `currencyCode`, `timezone`, `dailyBudget`, `accountInfo.{type,subType,marketplaceStringId,id,name,validPaymentMethod}` |
| The global account behind a profile | Ads API | `POST /adsApi/v1/query/advertiserAccounts` | `advertiserAccountId`, `alternateIds[].{profileId,entityId,countryCode,region}`, `status.statusCode`, `businessDetails` (single-account queries) |
| What the user may do | Ads API | The operation's own reply (401 on too little permission); the operation description's "Requires one of these permissions" in the live model | — |
| Linked accounts of a manager account | Ads API | `GET /managerAccounts` | linked accounts with access level |
| Entities, current state | Ads API | v1 `POST /adsApi/v1/query/{campaigns,adGroups,ads,targets,adAssociations,adExtensions}` with `adProductFilter`; SP v3 `POST /sp/{resource}/list`; SB v4 `POST /sb/v4/{resource}/list`; SB v3 and SD v3 `GET` lists | `state`, `status.deliveryStatus`, `status.deliveryReasons` (v1); `extendedData.{servingStatus,servingStatusDetails,creationDateTime,lastUpdateDateTime}` with `includeExtendedDataFields` (SP v3) |
| Entities in bulk | Ads API, then a download URL | `POST /{campaigns,adGroups,targets,ads}/export` → `GET /exports/{exportId}` | `status`, `url` (valid one hour) |
| The result of a write | The write's own 207 body | v1 create/update/delete; SP v3 `POST`/`PUT`/`…/delete` | `success[].index`, `partialSuccess[].errors[]`, `error[].errors[].{code,message,fieldLocation}` (v1); `…errors[].errorType`, `errorValue.*.reason`, `lowerLimit`, `upperLimit` (SP v3) |
| Whether a write took effect | Ads API | A read of the same entity after the write; `POST /history` for SP and SB | entity fields; `changeType`, `previousValue`, `newValue`, `timestamp` |
| Batch sizes and enums | Amazon's live models | `https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json` → per-product v1 models | `maxItems`, `maxResults`, enum values |
| Bid and budget bounds | The write's error, or the limits page | SP v3 error `lowerLimit`/`upperLimit`; *Limits, constraints, and quotas* | per marketplace and ad product |
| Budget spent so far today | Ads API | `POST /sp/campaigns/budget/usage`, `/sb/campaigns/budget/usage`, `/sd/campaigns/budget/usage`, `/portfolios/budget/usage` | `budgetUsagePercent`, `usageUpdatedTimestamp` |
| Amazon's suggestions | Ads API | section L operations; `POST /recommendations/list`; `POST /adsApi/v1/query/recommendations` | per operation |
| Whether a product can be advertised | Ads API | `POST /eligibility/product/list`; `POST /product/metadata` with `checkEligibility` | `overallStatus`, `eligibilityStatusList[]`; `eligibilityStatus`, `ineligibilityCodes`, `availability` |
| Creative moderation | Ads API | `POST /moderation/results` | per creative status and reasons |
| How long to wait after a 429 | The 429 reply | `Retry-After` header | seconds |
| What is being deprecated | Docs | *Deprecations* page and *Release notes*, markdown at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md` and `…/release-notes/index.md`; `Warning: 299` headers on deprecated legacy account calls | dates |
| Report status and rows | See `method/reporting.md` | v3 `/reporting/reports`; v1 `/adsApi/v1/{create,retrieve}/reports` | — |
| Audiences for SP/SB bid adjustments | Ads API | `POST /targetableEntities/list` (`application/vnd.Mindreader.TargetableEntitiesResource.v1+json`) with `adProduct`, `targetTypeFilter: [AUDIENCE]`, `pathsFilter` `[["Audience Category","Custom-built","Product"]]` (Amazon-built) or `…,"AMC"]]`; `POST /targetableEntities/paths/list` for the tree | `audienceId`, `audienceResolved`, `audienceTooltip`, `path`, `targetType`, `nextToken` |
| Audiences for SD targets | Ads API | `POST /audiences/taxonomy/list` then `POST /audiences/list` (`adType: SD`, one `countries` entry, `filters[]`, `?canTarget=true`); `GET /insights/audiences/{audienceId}/overlappingAudiences?adType=SD` | `audienceId`, `audienceName`, `category`, `status`, `forecasts.inventoryForecasts.all.dailyReach`; taxonomy `category`, `audienceCount` |
| Audiences, v1 beta | Ads API | `POST /adsApi/v1/query/audiences`, `/retrieve/audiences`, `/query/audienceCategories` (betas model) | per operation |
| A brand's `brandEntityId` | Ads API | SB v3 `GET /brands` | `brandId`, `brandEntityId` (sellers), `brandRegistryName` |
| Global brand ids | Ads API | `POST /adsApi/v1/retrieve/brands`; `POST /adsApi/v1/query/brandAdvertiserAssociations` | `brandId`, `brandAlternateIds[]`, `associationStatus` |
| Store structure and Store ASINs | Ads API | v1 `POST /adsApi/v1/query/brandStores`, `/query/brandStorePages`; SB v3 `GET /pageAsins?pageUrl=`; Store insights `POST /stores/{brandEntityId}/insights`, `…/asinMetrics` | `storeId`, `pageInfos`, `pageId`, `content`; ASIN list |
| Asset library | Ads API, then an S3 URL | `POST /assets/upload` → `PUT <url>` (outside the door) → `POST /assets/register` → `GET /assets?assetId=` until `ACTIVE`; `POST /assets/search` for existing assets | `url`; `assetId`, `versionId`, `failedSpecChecks`; asset status |
| SB media status | Ads API | SB v3 `GET /media/describe?mediaId=` | status (`PendingDeepValidation`, `Available`, `Failed` …) |
| Cross-marketplace mapping | Ads API | `POST /keywords/localize`, `/products/localize`, `/targetingExpression/localize`, `/currencies/localize` (each needs Scope and `Amazon-Ads-AccountId`) | per operation, versioned media types v1/v2 |
| Reserve share of voice | Ads API | `POST /adsApi/v1/create/{keywordReservationValidations,brandedKeywordsPricings,reservedTargetPricings,advertisingDeals,advertisingDealTargets}/sb`; `query`/`update`/`delete` variants; then SB v4 `POST /sb/v4/campaigns` with `targetedPGDealId` | `isReservable`, `reservationRejectedReason`, `keywordsPricing`, deal `status` |
| Advertiser promotion credits (beta) | Ads API | `POST /adsApi/v1/query/promotionOffers`, `/query/promotionRewards` | offer `status`; reward amounts and consumption |
| Measurement families | Ads API | section AF table | per operation |
| Binding terms for the client | Amazon pages | *Amazon Advertising API License Agreement*; *Amazon Ads API Policies*; *Amazon Ads Partner Network Policies*; for SP-API, the DPP and AUP at `sellercentral.amazon.com/solution-provider/policy?policyType=…` | "Last Updated" line; policy text |

### What the door does not name or cannot do (follow-ups for `cx-amazon-ads`)

Read against `door.md` and `SKILL.md` of `cx-amazon-ads` (door.md's own date: Amazon's guides read 2026-11-03). Each item is a fact about the door's current text set against an Amazon page. It is offered to that package's owners and is not a change made here.

1. **Ireland is not in the origin table.** The door's table lists the EU marketplaces as UK, FR, IT, ES, DE, NL, AE, PL, TR, EG, SA, SE, BE, IN, ZA, the same list as Amazon's *API overview*. The Profiles model (which tables IE under region `EU`), the limits page and a field report (#391) show IE profiles since late May 2025. [official] *Profiles* model; *Limits, constraints, and quotas*. [seat] By the model's region table and the *Profiles* guide's per-region rule, an IE profile is listed by the EU origin; no Amazon page read here says so in one sentence.
2. **Reporting v1 is not named.** `door.md` documents reporting v3 only and records its 2027-06-30 stop. v1 reporting names the advertiser by global account id in `accessRequestedAccounts`, not by Scope header. Its limits are per client id on *Limits and best practices* and the *Reporting API v1 overview*, and per advertiser on the *Amazon Ads reporting overview* and the 2026-09-30 GA note. [official] those pages. [seat] If the per-client reading holds, one seller's v1 reports can throttle another's under ComChatX's single client id; if the per-advertiser reading holds, they cannot.
3. **The global account id is not named.** The door documents `GET /v2/profiles` but not `POST /adsApi/v1/query/advertiserAccounts`, which ties a profile to the `amzn1.ads-account.g.*` id that v1 reporting, v1 recommendations and Stream v2 require.
4. **Families the door does not name:** manager accounts, exports, change history, budget usage, eligibility, product metadata, moderation, portfolios, budget and optimization rules, tactical recommendations, the v1 Recommendations API, Brand Metrics, Stores insights and Attribution. The door carries them, since it carries any method and path. It does not name their media types or account headers.
5. **Downloads are outside the door.** Report URLs (v3 S3 links; the SD v2 report download's 307), export URLs (valid one hour), AMC workflow download URLs and Stream v2 files in S3 are not replies the door returns. `door.md` says this for reports. [official] *Exports FAQ*; *Deprecations*; *AMC* tools spec.
6. **Stream v2 needs an AWS account the door does not have.** It needs an S3 bucket and an SQS queue with Amazon's policies, and "A destination belongs to the application that first uses it", which for the door is ComChatX's application. Each client application may have at most 5 destinations. [official] *Stream v2: Set up your destination*; *Stream v2: Limits*.
7. **A fresh token per call.** The door trades the refresh token at LwA on every call and keeps no access token, whose life is 60 minutes. [official] *Access tokens*. [seat] Each call therefore makes two requests, one to LwA and one to the Ads API, and LwA's own limits are not documented on the Ads API pages read here.
8. **No wait on 429.** The door "adds no wait and retries nothing"; Amazon's guidance is backoff with `Retry-After`. [official] *Rate limiting*. Field reports show 429 bodies without `Retry-After` (#422, #436).
9. **A list sent as `POST` reads as a change.** The gate reads every `POST` as a change, and v1 query, SP v3 list, SB v4 list, exports, budget usage, eligibility, product metadata, change history and recommendations are all `POST`s that change nothing at Amazon. A lost reply to any of them reads "sent, outcome unknown". The opposite case also holds: `POST /recommendations/apply` and the v1 creates are real changes, and they have no idempotency key (section F).
10. **Header names.** The door refuses a request naming either client-id header and attaches `Amazon-Advertising-API-ClientId`. *Make your first call*, *Getting started with Amazon Ads API v1*, *QueryAdvertiserAccount API*, the v1 recommendations examples and the MCP and skills pages use `Amazon-Ads-ClientId`; the *Profiles* model and guide and the Reporting v1 pages use `Amazon-Advertising-API-ClientId`. [seat] Whether every v1 family accepts the older header name is not stated on a page read here.
11. **The refresh-token expiry.** `door.md` records the 365-day expiry for tokens issued on or after 2026-07-30. [seat] A connection saved from that date fails with `invalid_grant` 365 days after consent, whatever its use.
12. **Test accounts need another scope and have no seller type.** `advertising::test:create_account` is a separate scope, and test accounts are `VENDOR` or `AUTHOR`. [official] *Test accounts* pages.
13. **AMC needs a UI step and its own headers.** Terms are accepted once per region in the AMC UI. Calls carry `Amazon-Advertising-API-AdvertiserId` and `Amazon-Advertising-API-MarketplaceId`. [official] *AMC instance management*.
14. **The MCP server is not reachable through the door.** Its hosts are `advertising-ai*.amazon.com`, not the door's origins. Amazon's skills library (`GET /skills`) is on the Ads API origins and is reachable.
15. **`Content-Type` per operation.** The door composes no content type. SP v3, SB v4, product metadata, moderation and change history name versioned media types, and change history's `THEME` events need the v1.1 `Accept`. [official] models named.
16. **A new creative image or video cannot be uploaded through the door.** The asset library's step 2 is a `PUT` of the file's bytes to a pre-signed S3 URL (`al-na-….s3.amazonaws.com` in Amazon's examples) that expires in 15 minutes. That host is not one of the door's three origins. So an SB video ad, an SB creative with a new logo or custom image, or an SD creative with a new image cannot be made end to end through the door. Creatives that reuse an asset already `ACTIVE` in the library can be, since `POST /assets/upload`, `POST /assets/register`, `GET /assets`, `POST /assets/search` and the creative creates are on the Ads API origin. [official] *Creating assets*; *Asset library* model. [seat] SB v3 `POST /stores/assets` is on the origin but takes a `multipart/form-data` binary body with `Content-Disposition` and `Content-Type` headers. Whether `--body` carries binary multipart is not stated in `door.md`.
17. **The audience families are not named.** `POST /audiences/list` and `/audiences/taxonomy/list` (SD), `POST /targetableEntities/list` and `/paths/list` (SP, SB, SD, STV; versioned media type `application/vnd.Mindreader.TargetableEntitiesResource.v1+json`; model not in `contracts.json`), the v1 beta `query/audiences`, `retrieve/audiences` and `query/audienceCategories`, and `GET /insights/audiences/{audienceId}/overlappingAudiences`. The Audiences model names the account header `Amazon-Ads-AccountId` ("or `Amazon-Advertising-AccountId` (legacy) — not both"). Targetable Entities names `Amazon-Advertising-AccountId`. [official] the models.
18. **Brand and Store identifiers.** `door.md` does not name SB v3 `GET /brands`, the source of the seller's `brandEntityId`, which Store insights, `GET /stores/assets` and asset registration need. It does not name the v1 brand-store operations or the v1 brand associations either. `/v2/stores` has been shut off since 2026-06-01. [official] *Sponsored Brands v3* model; *Deprecations*; *Creating assets*.
19. **Localization, reserve share of voice, promotion offers and rewards, Events and the measurement families are not named.** Their paths, media types and permissions are in sections AC to AF. Localization's four operations mark `Amazon-Ads-AccountId` and the Scope header as both required. [official] *Localization* model.
20. **Two models the door's users may need are not in `contracts.json`.** These are Targetable Entities (`TargetableEntities_prod_3p.json`) and AMC Administration (`AMCAdministration_prod_3p.json`). `SponsoredBrands_prod_3p.json`, titled 3.0 but holding the `/sb/v4/*` surface, is not in it either. [seat] A reader that maps the surface from `contracts.json` alone misses them.
21. **Binding terms under one client id.** The Ads API licence, the Ads API policies and the Partner Network Policies bind the client application that the door's calls are made under, which is ComChatX's. The terms that read most directly on a multi-seller box: Confidential Information is disclosed only "to the Amazon Advertising Participant to which such data or information relates" and used only "by or on behalf of the particular Amazon Advertising Participant that has expressly authorized you"; "Sharing or combining Amazon Data with any other third-party data sources is strictly prohibited without express prior written approval from Amazon"; Amazon Data is not kept "beyond its intended use"; and, in policy 5.1, "You shall not solicit, collect, store, proxy, buy, sell or transfer Amazon login credentials or other authentication credentials of End Users for any purpose whatsoever." [official] section AG. [seat] `door.md` has the seller save a refresh token on the plugin's Settings, and the door trades it at Login with Amazon on every call. Whether a refresh token issued to the application through the seller's own consent counts as an "authentication credential of End Users" under 5.1 is not stated on any page read here. The other terms concern what is done with landed data afterwards, which `door.md` does not address.

## Pages read

Every Amazon docs page was read as the markdown copy named beside it, by plain GET. The docs site URL is given as the page's canonical address. Models were read as JSON or YAML. "Read" means fetched and searched for this file. "context" in the last column means the page was read for orientation and no claim in this file rests on it alone.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Betas overview | https://advertising.amazon.com/API/docs/en-us/developer/betas (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/developer/betas.md) | Guide | 2026-11-09 | Which APIs are in beta |
| Access Tokens in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/access-tokens (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/access-tokens.md) | Guide | 2026-11-09 | 60-minute access tokens; Atza prefix; 2048 bytes |
| Amazon Ads API Authorization Grants | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/authorization-grants (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/authorization-grants.md) | Guide | 2026-11-09 | LwA token hosts per region; tokens valid across regions |
| Manager accounts in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/manager-accounts (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/manager-accounts.md) | Guide | 2026-11-09 | Manager account links, Editor/Viewer, 50 accounts, admin on both sides |
| Amazon Ads API Authorization Overview | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/overview.md) | Guide | 2026-11-09 | Authorization flow overview |
| Profiles | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/profiles (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/profiles.md) | Guide | 2026-11-09 | Profiles; account types; what each serves |
| Refresh tokens | https://advertising.amazon.com/API/docs/en-us/guides/account-management/authorization/refresh-tokens (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/authorization/refresh-tokens.md) | Guide | 2026-11-09 | 365-day expiry from 2026-07-30; invalidation |
| Average daily budget user guide | https://advertising.amazon.com/API/docs/en-us/guides/account-management/average-daily-budget (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/average-daily-budget.md) | Guide | 2026-11-09 | `/accountBudgets/featureFlags` |
| Permissions | https://advertising.amazon.com/API/docs/en-us/guides/account-management/permissions (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/permissions.md) | Guide | 2026-11-09 | Console permissions mapped to API permission names; Seller Central names |
| QueryAdvertiserAccount API | https://advertising.amazon.com/API/docs/en-us/guides/account-management/query-advertiser-accounts (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/query-advertiser-accounts.md) | Guide | 2026-11-09 | Global account ids and `alternateIds` |
| Account registration | https://advertising.amazon.com/API/docs/en-us/guides/account-management/registration (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/registration.md) | Guide | 2026-11-09 | Advertiser account registration (v1) |
| Authorization for test accounts | https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/authorization-for-test-accounts (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/test-accounts/authorization-for-test-accounts.md) | Guide | 2026-11-09 | `advertising::test:create_account` scope |
| Creating test accounts | https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/create-test-accounts (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/test-accounts/create-test-accounts.md) | Guide | 2026-11-09 | `POST /testAccounts` |
| Test accounts overview | https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/test-accounts/overview.md) | Guide | 2026-11-09 | No serving, no billing; unsupported features |
| Using test accounts in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/account-management/test-accounts/use-test-accounts (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/account-management/test-accounts/use-test-accounts.md) | Guide | 2026-11-09 | Rules configure but do not act; SB auto-moderation; image assets only |
| fundamental component | https://advertising.amazon.com/API/docs/en-us/guides/amazon-ads-well-architected-framework/fundamental-component (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-ads-well-architected-framework/fundamental-component.md) | Guide | 2026-11-09 | Regions; TPS; 207 handling; backoff example; idempotent retries; exports vs GET |
| Amazon Attribution API overview | https://advertising.amazon.com/API/docs/en-us/guides/amazon-attribution/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-attribution/overview.md) | Guide | 2026-11-09 | Attribution beta, eligible marketplaces |
| Instance management | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/admin/instance-management (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/admin/instance-management.md) | Guide | 2026-11-09 | Instances; headers; terms per region |
| Get access to AMC using self-service APIs | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/get-started/instant-access-to-amc (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/get-started/instant-access-to-amc.md) | Guide | 2026-11-09 | Self-service instant access |
| How does Amazon Marketing Cloud work | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/how-amc-works (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/how-amc-works.md) | Guide | 2026-11-09 | Aggregated outputs only |
| Overview - Amazon Marketing Cloud | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/overview.md) | Guide | 2026-11-09 | AMC overview |
| Sponsored ads campaign management | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/datasets/sponsored-ads-campaign-management (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/datasets/sponsored-ads-campaign-management.md) | Guide | 2026-11-09 | Stream v1 sunset warning; campaigns dataset states, `version`, unique names |
| Overview - Amazon Marketing Stream | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/overview.md) | Guide | 2026-11-09 | Stream v1 overview |
| Create a subscription | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/create-a-subscription (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/create-a-subscription.md) | Guide | 2026-11-09 | Accepted account ids; body-scoped account; 401 DENY |
| Data delivery | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/data-delivery (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/data-delivery.md) | Guide | 2026-11-09 | Parquet to S3, SQS notifications, batch versions |
| Ads performance | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/ads-performance (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/datasets/ads-performance.md) | Guide | 2026-11-09 | Hourly grain; 70-day restatement; no calculated metrics |
| Overview | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/datasets/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/datasets/overview.md) | Guide | 2026-11-09 | Dataset list |
| Get started | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/get-started (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/get-started.md) | Guide | 2026-11-09 | AWS prerequisites; Regions |
| Limits | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/manage-subscriptions/limits (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/manage-subscriptions/limits.md) | Guide | 2026-11-09 | Subscription, destination and rate limits |
| Migrate from Version 1 | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/migrate-from-v1 (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/migrate-from-v1.md) | Guide | 2026-11-09 | v1 to v2 differences |
| Overview | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/overview.md) | Guide | 2026-11-09 | Totals not deltas; delivery as often as every 15 minutes; Region table (the "what Stream does not carry" pointer is on *Deprecations*) |
| Set up your destination | https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-stream/v2/set-up-your-destination (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-stream/v2/set-up-your-destination.md) | Guide | 2026-11-09 | Bucket and queue policies; Amazon's AWS account; destination ownership |
| The adassociation entity in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad-association (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/ad-association.md) | Guide | 2026-11-09 | v1 ad association entity |
| The adgroup entity in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad-group (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/ad-group.md) | Guide | 2026-11-09 | v1 ad group entity |
| The ad entity in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/ad (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/ad.md) | Guide | 2026-11-09 | v1 ad entity |
| The campaign entity in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/campaign (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/campaign.md) | Guide | 2026-11-09 | v1 campaign entity; budgets list |
| Campaign entities in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/overview.md) | Guide | 2026-11-09 | v1 entities and operations |
| The target entity in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/entities/target (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/entities/target.md) | Guide | 2026-11-09 | v1 target entity; keywords as targets |
| Example request payloads for campaign management in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/example-payloads (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/example-payloads.md) | Guide | 2026-11-09 | v1 create, update and delete payloads |
| Campaign management in the Amazon Ads API | https://advertising.amazon.com/API/docs/en-us/guides/campaign-management/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/campaign-management/overview.md) | Guide | 2026-11-09 | One ad product per call; per-product TPS at launch |
| Exports FAQ | https://advertising.amazon.com/API/docs/en-us/guides/exports/faq (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/exports/faq.md) | Guide | 2026-11-09 | 5 jobs per endpoint; URL life; no history; cadence |
| Get started with exports | https://advertising.amazon.com/API/docs/en-us/guides/exports/get-started (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/exports/get-started.md) | Guide | 2026-11-09 | Export request and poll |
| Exports overview | https://advertising.amazon.com/API/docs/en-us/guides/exports/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/exports/overview.md) | Guide | 2026-11-09 | Exports scope |
| Getting started - Create an authorization grant | https://advertising.amazon.com/API/docs/en-us/guides/get-started/create-authorization-grant (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/get-started/create-authorization-grant.md) | Guide | 2026-11-09 | Grant URL and scopes |
| Make your first call | https://advertising.amazon.com/API/docs/en-us/guides/get-started/first-call (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/get-started/first-call.md) | Guide | 2026-11-09 | Headers; first calls |
| Amazon Ads API Getting Started Overview | https://advertising.amazon.com/API/docs/en-us/guides/get-started/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/get-started/overview.md) | Guide | 2026-11-09 | Getting-started path |
| Rate limiting (getting started copy) | https://advertising.amazon.com/API/docs/en-us/guides/get-started/rate-limiting (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/get-started/rate-limiting.md) | Guide | 2026-11-09 | Answered 404 at re-read by the verifier; no claim rests on it |
| Getting started - Generate access and refresh tokens | https://advertising.amazon.com/API/docs/en-us/guides/get-started/retrieve-access-token (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/get-started/retrieve-access-token.md) | Guide | 2026-11-09 | Token trade |
| Get started with unified pre-moderation | https://advertising.amazon.com/API/docs/en-us/guides/moderation/pre-moderation (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/moderation/pre-moderation.md) | Guide | 2026-11-09 | Pre-moderation |
| Apply for Amazon Ads API access | https://advertising.amazon.com/API/docs/en-us/guides/onboarding/apply-for-access (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/onboarding/apply-for-access.md) | Guide | 2026-11-09 | Application; review "up to 1 business day" |
| Amazon Ads API Onboarding Overview | https://advertising.amazon.com/API/docs/en-us/guides/onboarding/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/onboarding/overview.md) | Guide | 2026-11-09 | Onboarding steps |
| Sharing leftover budget in a portfolio | https://advertising.amazon.com/API/docs/en-us/guides/portfolios/sharing-leftover (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/portfolios/sharing-leftover.md) | Guide | 2026-11-09 | Unspent budget sharing |
| How to call the API | https://advertising.amazon.com/API/docs/en-us/guides/recommendations/recommendations-api/how-to (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/how-to.md) | Guide | 2026-11-09 | v1 query and list; headers; 300 cap; 401 without account header |
| Recommendations API overview | https://advertising.amazon.com/API/docs/en-us/guides/recommendations/recommendations-api/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/overview.md) | Guide | 2026-11-09 | v1 Recommendations API |
| Recommendation types | https://advertising.amazon.com/API/docs/en-us/guides/recommendations/recommendations-api/recommendation-types (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/recommendation-types.md) | Guide | 2026-11-09 | Supported recommendation types |
| Limits and best practices | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/limits (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/limits.md) | Guide | 2026-11-09 | Limits per client id; concurrency as low as 1 |
| Overview of the Reporting v1 API | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/overview.md) | Guide | 2026-11-09 | One concurrent report per client id; Stream as the scaling surface |
| Getting started with the Reporting API v1 | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/quickstart (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/quickstart.md) | Guide | 2026-11-09 | v1 report calls |
| Brand Metrics API Overview | https://advertising.amazon.com/API/docs/en-us/guides/reporting/brand-metrics/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/brand-metrics/overview.md) | Guide | 2026-11-09 | Brand Metrics beta and marketplaces |
| Amazon Ads reporting overview | https://advertising.amazon.com/API/docs/en-us/guides/reporting/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/overview.md) | Guide | 2026-11-09 | Reporting surfaces; "one concurrent report per advertiser"; Stream v2 70-day backfill |
| Sponsored Products Rule-based bidding overview | https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/overview.md) | Guide | 2026-11-09 | Rule-based bidding preconditions |
| Scheduled bid rules | https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/scheduled-bid-rules (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/scheduled-bid-rules.md) | Guide | 2026-11-09 | Scheduled bid rules |
| Budget Rules overview | https://advertising.amazon.com/API/docs/en-us/guides/rules/budget-rules/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/overview.md) | Guide | 2026-11-09 | Budget rules |
| Performance-based rules | https://advertising.amazon.com/API/docs/en-us/guides/rules/budget-rules/performance-based (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/performance-based.md) | Guide | 2026-11-09 | Lookbacks 7 / 14 days |
| Schedule-based rules | https://advertising.amazon.com/API/docs/en-us/guides/rules/budget-rules/schedule-based (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/schedule-based.md) | Guide | 2026-11-09 | `intraDaySchedule` marketplaces |
| Sponsored Products overview | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-products/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/overview.md) | Guide | 2026-11-09 | SP API overview |
| AI Migration Skills | https://advertising.amazon.com/API/docs/en-us/mcp/ai-migration-skills (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/ai-migration-skills.md) | MCP guide | 2026-11-09 | `ads-api-migration` skill |
| Connecting to the Amazon Ads MCP Server (Lite) | https://advertising.amazon.com/API/docs/en-us/mcp/get-started-lite (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/get-started-lite.md) | MCP guide | 2026-11-09 | Lite endpoints; account context modes |
| Connecting to the Amazon Ads MCP Server | https://advertising.amazon.com/API/docs/en-us/mcp/get-started (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/get-started.md) | MCP guide | 2026-11-09 | MCP endpoints; Fixed and Dynamic context |
| Overview | https://advertising.amazon.com/API/docs/en-us/mcp/mcp-overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/mcp-overview.md) | MCP guide | 2026-11-09 | Tools, expert tools, skills |
| Connecting to the Ads MCP Server using OAuth 2.1 | https://advertising.amazon.com/API/docs/en-us/mcp/oauth (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/oauth.md) | MCP guide | 2026-11-09 | OAuth 2.1; named clients |
| Download Skills from the Amazon Ads MCP Server | https://advertising.amazon.com/API/docs/en-us/mcp/skills/get-started (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/skills/get-started.md) | MCP guide | 2026-11-09 | Skills library on the Ads API hosts |
| Getting started with Amazon Ads API v1 | https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/getting-started (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/amazon-ads/getting-started.md) | Reference | 2026-11-09 | v1 prerequisites and headers |
| Amazon Ads API v1 overview | https://advertising.amazon.com/API/docs/en-us/reference/amazon-ads/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/amazon-ads/overview.md) | Reference | 2026-11-09 | v1 scope; "will eventually fully replace" |
| Overview | https://advertising.amazon.com/API/docs/en-us/reference/api-overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/api-overview.md) | Reference | 2026-11-09 | Regional hosts and marketplaces |
| Error responses and error status codes | https://advertising.amazon.com/API/docs/en-us/reference/concepts/errors (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/errors.md) | Reference | 2026-11-09 | Error responses and status codes |
| Limits, constraints, and quotas | https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md) | Reference | 2026-11-09 | P99s; bid, budget, keyword and name limits |
| Amazon Ads API Concepts Overview | https://advertising.amazon.com/API/docs/en-us/reference/concepts/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/overview.md) | Reference | 2026-11-09 | Concepts index |
| Rate limiting | https://advertising.amazon.com/API/docs/en-us/reference/concepts/rate-limiting (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/rate-limiting.md) | Reference | 2026-11-09 | 429, `Retry-After`, dynamic limits, retry classes, 5x extended lists |
| Migrating to version 4 Sponsored Brands campaigns | https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-v3-v4 (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-v3-v4.md) | Reference | 2026-11-09 | SB v3 to v4 field mapping |
| Amazon Ads advanced tools release notes | https://advertising.amazon.com/API/docs/en-us/release-notes/index (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md) | Release notes | 2026-11-09 | Dated release notes 2025-2026 |
| Amazon Ads API v0 release notes | https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v0 (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v0.md) | Release notes | 2026-11-09 | Non-v1 release notes |
| Amazon Ads API v1 release notes | https://advertising.amazon.com/API/docs/en-us/release-notes/ads-api-v1 (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v1.md) | Release notes | 2026-11-09 | v1 release dates; "reduced to 16" |
| Deprecations | https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md) | Release notes | 2026-11-09 | Planned and past deprecations |
| contracts.json (OpenAPI contract index) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json | Contract index | 2026-11-09 | Every model's URL; v1 supported products |
| Amazon Ads API v1 (cross-product) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALL_prod_3p.json | OpenAPI model | 2026-11-09 | v1 paths; State, DeliveryStatus, AdProduct enums; ErrorCode; partialSuccess |
| Amazon Ads API v1 merged (prod and beta) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | OpenAPI model | 2026-11-09 | Merged v1 schemas: advertiser accounts, manager accounts, reports, stream subscriptions, recommendations (`GET /adsApi/v1/recommendations`), events; `FULL_FUNNEL`, `RMS` |
| Amazon Ads API v1, Sponsored Products | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISP_prod_3p.json (and `AmazonAdsAPISPMerged_prod_3p.json`) | OpenAPI model | 2026-11-09 | SP batch limits; SP enums; create and update states; browse placements, `INTERESTED_AUDIENCE` and `REVIEW_REQUEST` in the merged copy only |
| Amazon Ads API v1, Sponsored Brands | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISB_prod_3p.json (and SBMerged) | OpenAPI model | 2026-11-09 | SB batch limits |
| Amazon Ads API v1, Sponsored Display | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISD_prod_3p.json (and SDMerged) | OpenAPI model | 2026-11-09 | SD batch limits |
| Sponsored Products (v3) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | OpenAPI model | 2026-11-09 | SP v3 paths, media types, 207 shape, error families, permissions, serving status |
| Sponsored Products v2 | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-products/2-0/openapi.yaml | OpenAPI model | 2026-11-09 | Duplicate campaign names: sellers no, vendors yes |
| Sponsored Brands v3 | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | OpenAPI model | 2026-11-09 | Keyword and target paths; delete archives permanently |
| Sponsored Brands v4 | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | OpenAPI model | 2026-11-09 | v4 paths; ad-type paths; migration endpoints; budget usage |
| Sponsored Display v3 | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml | OpenAPI model | 2026-11-09 | SD paths; delete archives permanently; int64 ids |
| Profiles v3 | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml | OpenAPI model | 2026-11-09 | Query parameters; accountInfo; IE in countryCode; no profile without a campaign |
| Portfolios | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Portfolios_prod_3p.json | OpenAPI model | 2026-11-09 | Portfolio v3 paths; budget usage |
| Change history | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json | OpenAPI model | 2026-11-09 | SP and SB only; no actor; 90 days; paging limits |
| Eligibility | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json | OpenAPI model | 2026-11-09 | Product eligibility shape |
| Product selector (product metadata) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ProductSelector_prod_3p.json | OpenAPI model | 2026-11-09 | `/product/metadata` inputs and fields |
| Moderation | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Moderation_prod_3p.json | OpenAPI model | 2026-11-09 | `/moderation/results`, media types |
| Pre-moderation | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/PreModeration_prod_3p.json | OpenAPI model | 2026-11-09 | `/preModeration` |
| Brand Metrics | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json | OpenAPI model | 2026-11-09 | Report create and poll |
| Stores | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json | OpenAPI model | 2026-11-09 | Stores insights paths |
| Amazon Attribution | https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json | OpenAPI model | 2026-11-09 | Attribution paths |
| Amazon Marketing Stream (v1) | https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonMarketingStream_prod_3p.json | OpenAPI model | 2026-11-09 | v1 subscription paths |
| Manager account | https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json | OpenAPI model | 2026-11-09 | Manager account paths |
| Recommendations (tactical) | https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json | OpenAPI model | 2026-11-09 | list, apply, update |
| Advertising accounts | https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AdvertisingAccounts_prod_3p.json | OpenAPI model | 2026-11-09 | Legacy account APIs |
| Advertising test account | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json | OpenAPI model | 2026-11-09 | VENDOR / AUTHOR; countries; statuses |
| Exports | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json | OpenAPI model | 2026-11-09 | Export paths |
| Offline report (reporting v3) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/OfflineReport_prod_3p.json | OpenAPI model | 2026-11-09 | v3 report paths |
| Sponsored TV (product API) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredTV_prod_3p.json | OpenAPI model | 2026-11-09 | Downloaded; no claim rests on it |
| SB category benchmark | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrandsCategoryBenchmark_prod_3p.json | OpenAPI model | 2026-11-09 | Downloaded; the retirement is from *Deprecations* |
| Remaining models in contracts.json (DSP, audiences, AMC custom models, billing and others) | URLs as listed in contracts.json | OpenAPI models | 2026-11-09 | Where idempotency keys appear (DSP audiences, AMC custom models, billing) |
| MCP tools: campaign_management | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/campaign_management.json | MCP tool spec | 2026-11-09 | 32 tools |
| MCP tools: reporting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/reporting.json | MCP tool spec | 2026-11-09 | 6 tools |
| MCP tools: account_management | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/account_management.json | MCP tool spec | 2026-11-09 | 7 tools |
| MCP tools: amc | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/amc.json | MCP tool spec | 2026-11-09 | 10 tools |
| MCP tools: audience_discovery | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/audience_discovery.json | MCP tool spec | 2026-11-09 | 3 tools |
| MCP tools: billing | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/billing.json | MCP tool spec | 2026-11-09 | 4 tools |
| MCP tools: inventory_management | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/inventory_management.json | MCP tool spec | 2026-11-09 | 10 tools |
| MCP tools: eligibility | https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/eligibility.json | MCP tool spec | 2026-11-09 | 2 tools |
| Introducing Amazon Ads Agent, your AI-powered ad platform | https://advertising.amazon.com/library/news/amazon-ads-agent | News (Amazon Ads) | 2026-11-09 | Ads Agent naming (2026-09-29); no API or MCP statement |
| Introducing the Amazon Ads MCP Server | https://advertising.amazon.com/library/news/amazon-ads-mcp-server-open-beta | News (Amazon Ads) | 2026-11-09 (verifier) | Open beta dated 2026-02-02; "available globally in open beta to Amazon Ads partners with active API credentials" |
| unBoxed 2026 news: Explore the latest advertising announcements | https://advertising.amazon.com/library/news/unboxed-2026-news-announcements | News (Amazon Ads) | 2026-11-09 (verifier) | MCP Server (Lite) and the AMC expert tool among unBoxed 2026 announcements |
| `amzn/ads-advanced-tools-docs` issue list (100 most recent) | https://api.github.com/repos/amzn/ads-advanced-tools-docs/issues | GitHub (Amazon's docs repo) | 2026-11-09 | Field reports below |
| Issue #378 | https://github.com/amzn/ads-advanced-tools-docs/issues/378 | GitHub issue | 2026-11-09 | SB / SD ad states (Amazon contributor) |
| Issue #379 | https://github.com/amzn/ads-advanced-tools-docs/issues/379 | GitHub issue | 2026-11-09 | Id typed integer, returned string |
| Issue #380 | https://github.com/amzn/ads-advanced-tools-docs/issues/380 | GitHub issue | 2026-11-09 | Eligibility request shape |
| Issue #383 | https://github.com/amzn/ads-advanced-tools-docs/issues/383 | GitHub issue | 2026-11-09 | IE limits published 2025-06-26 |
| Issue #391 | https://github.com/amzn/ads-advanced-tools-docs/issues/391 | GitHub issue | 2026-11-09 | IE profiles from late May 2025 |
| Issue #406 | https://github.com/amzn/ads-advanced-tools-docs/issues/406 | GitHub issue | 2026-11-09 | Scope vs permission (Amazon contributor) |
| Issue #413 | https://github.com/amzn/ads-advanced-tools-docs/issues/413 | GitHub issue | 2026-11-09 | Budget usage freshness unanswered |
| Issue #422 | https://github.com/amzn/ads-advanced-tools-docs/issues/422 | GitHub issue | 2026-11-09 | Per-seller 429 on change history |
| Issue #430 | https://github.com/amzn/ads-advanced-tools-docs/issues/430 | GitHub issue | 2026-11-09 | v1 campaign create sample |
| Issue #436 | https://github.com/amzn/ads-advanced-tools-docs/issues/436 | GitHub issue | 2026-11-09 | MCP 429 without Retry-After |
| Issue #439 | https://github.com/amzn/ads-advanced-tools-docs/issues/439 | GitHub issue | 2026-11-09 | STV absent from v1 reporting |
| Issue #450 | https://github.com/amzn/ads-advanced-tools-docs/issues/450 | GitHub issue | 2026-11-09 | Harvest tool 504 |
| Issue #453 | https://github.com/amzn/ads-advanced-tools-docs/issues/453 | GitHub issue | 2026-11-09 | No target id in v1 report fields |
| Issue #456 | https://github.com/amzn/ads-advanced-tools-docs/issues/456 | GitHub issue | 2026-11-09 | Duplicate v1 report rows |
| Issue #467 | https://github.com/amzn/ads-advanced-tools-docs/issues/467 | GitHub issue | 2026-11-09 | v1 global report missing DE and GB |
| Issue #475 | https://github.com/amzn/ads-advanced-tools-docs/issues/475 | GitHub issue | 2026-11-09 | SD budget update ignored |
| Issue #476 | https://github.com/amzn/ads-advanced-tools-docs/issues/476 | GitHub issue | 2026-11-09 | v1 search terms only on clicked rows |
| Issue #481 | https://github.com/amzn/ads-advanced-tools-docs/issues/481 | GitHub issue | 2026-11-09 | SD v1 KPI enum |
| Issue #499 | https://github.com/amzn/ads-advanced-tools-docs/issues/499 | GitHub issue | 2026-11-09 | No targeting-type field on ad groups |
| Issue #501 | https://github.com/amzn/ads-advanced-tools-docs/issues/501 | GitHub issue | 2026-11-09 | SB v3 report 429 in NA and EU |
| Issue #519 | https://github.com/amzn/ads-advanced-tools-docs/issues/519 | GitHub issue | 2026-11-09 | Onboarding pending 29 days |
| Issue #523 | https://github.com/amzn/ads-advanced-tools-docs/issues/523 | GitHub issue | 2026-11-09 | Partner onboarding pending |
| Issue #524 | https://github.com/amzn/ads-advanced-tools-docs/issues/524 | GitHub issue | 2026-11-09 | Prompt extension pause reverts |
| Issue #525 | https://github.com/amzn/ads-advanced-tools-docs/issues/525 | GitHub issue | 2026-11-09 | Required `statusMessage` absent |
| Airbyte, Amazon Ads source connector | https://docs.airbyte.com/integrations/sources/amazon-ads | Vendor doc | 2026-11-09 | 429 handling, concurrency, lookback, agency profiles ignored, changelog |
| Fivetran, Amazon Ads connector | https://fivetran.com/docs/connectors/applications/amazon-ads | Vendor doc | 2026-11-09 | Retention by product; profile time zone; SB 14-day data |
| `denisneuf/python-amazon-ad-api` README, repo and issues | https://github.com/denisneuf/python-amazon-ad-api | Open-source client | 2026-11-09 | v1 description; weekly contract updates; v1 contract URLs |
| `cx-amazon-ads` SKILL.md and references/door.md | package files (read-only copy) | ComChatX package | 2026-11-09 | What the door names and does |
| Audiences discovery (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json | OpenAPI model | 2026-11-09 | `/audiences/list`, `/audiences/taxonomy/list`; `adType` DSP/SD/ST; headers; status enum |
| Targetable Entities (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/TargetableEntities_prod_3p.json | OpenAPI model (not in contracts.json) | 2026-11-09 | `/targetableEntities/list`, `/paths/list`; media type; filters; entity fields |
| Audience insights (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Insights_prod_3p.json | OpenAPI model | 2026-11-09 | Overlapping audiences operation |
| Amazon Ads API v1 betas (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p_BETA.json | OpenAPI model | 2026-11-09 | v1 beta audiences, audience categories, promotion offers/rewards, brand store page update, clean rooms, queries; `GB` marketplace value |
| Asset library (creative assets) (gap fill) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml | OpenAPI model | 2026-11-09 | Six asset operations, media types, headers, subtype and filter enums, 15-minute upload URL |
| Asset library overview (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/asset-library-overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/creative-asset/asset-library-overview.md) | Guide | 2026-11-09 | Programs the library serves |
| Creating assets (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/creating-assets (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/creative-asset/creating-assets.md) | Guide | 2026-11-09 | Three-call sequence; S3 `PUT`; register fields; `GET /brands` for sellers; `PROCESSING` → `ACTIVE` |
| Managing assets (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/creative-asset/managing-assets (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/creative-asset/managing-assets.md) | Guide | 2026-11-09 | context (asset versions) |
| Sponsored Display audience targeting (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/audience-targeting (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/audience-targeting.md) | Guide | 2026-11-09 | Taxonomy then discovery; Scope header; overlap insights |
| Sponsored Display creatives (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/creatives (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/creatives.md) | Guide | 2026-11-09 | Creatives built from asset ids; image minimums |
| Sponsored Display overview (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-display/overview (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/overview.md) | Guide | 2026-11-09 | context |
| Shopper cohort bidding (SB) (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/bidding/shopper-cohort (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/bidding/shopper-cohort.md) | Guide | 2026-11-09 | `POST targetableEntities/list`; one audience group per campaign; stacking with placement bids |
| Sponsored Brands overview; Get started with SB campaigns (gap fill) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/overview.md; https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns.md | Guide | 2026-11-09 | context |
| Reserve share of voice (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/sponsored-brands/reserve-share-of-voice (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/reserve-share-of-voice.md) | Guide | 2026-11-09 | Seven steps; five deal targets; `PROPOSED` rules; deletion window |
| Product Collection Migration Guide (gap fill) | https://advertising.amazon.com/API/docs/en-us/reference/migration-guides/sb-product-collection (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-product-collection.md) | Reference | 2026-11-09 | "January 2027 \| Final shutoff" |
| Sponsored Brands (SponsoredBrands_prod_3p.json) (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | OpenAPI model (not in contracts.json) | 2026-11-09 | Titled 3.0, holds `/sb/v4/*`; has negative-brand recommendations, no `/sb/negativeKeywords` |
| Sponsored Brands v3 and v4, re-read (gap fill) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml; …/4-0/openapi.json | OpenAPI models | 2026-11-09 | Path-to-spec mapping; `/brands`, `/pageAsins`, `/stores/assets`, `/media/describe`; asset id fields; `targetedPGDealId`; `shopperCohortBidAdjustments`; product-collection `deprecated: true` |
| Sponsored Products v3, re-read (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | OpenAPI model | 2026-11-09 | `extendedData` field names; `shopperCohortBidding`; deprecated `audienceSegmentType` |
| Amazon Ads API v1 (cross-product and merged), re-read (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALL_prod_3p.json; https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | OpenAPI models | 2026-11-09 | `audienceBidAdjustments`; SB deal operations; brand stores; Events; `Marketplace` enum with `GB` |
| Amazon Ads API v1, Sponsored Display, re-read (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISD_prod_3p.json; https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISDMerged_prod_3p.json | OpenAPI models | 2026-11-09 | 16 SD v1 CRUD paths |
| Localization (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json | OpenAPI model | 2026-11-09 | Four localize operations; media types; required headers |
| Store insights, re-read (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Stores_prod_3p.json | OpenAPI model | 2026-11-09 | Store insights media types and permissions |
| Brand associations (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandAidV2_prod_3p.json | OpenAPI model | 2026-11-09 | Global brand ids; retrieve/brands; brand–advertiser associations |
| Amazon DSP measurement (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Measurement_prod_3p.json | OpenAPI model | 2026-11-09 | Brand Lift and other DSP study paths; control-group fields |
| Marketing Mix Modeling (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/MarketingMixModeling_prod_3p.json | OpenAPI model | 2026-11-09 | MMM paths and permissions |
| Brand Metrics and Amazon Attribution, re-read (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/BrandMetrics_prod_3p.json; https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AmazonAttribution_prod_3p.json | OpenAPI models | 2026-11-09 | Paths and media types |
| AMC Administration (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AMCAdministration_prod_3p.json | OpenAPI model (not in contracts.json) | 2026-11-09 | AMC instance and collaboration paths |
| Conversions API; Ad library API; Validation configurations; Partner opportunities; Advertising accounts (gap fill) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ConversionsAPI_prod_3p.json; https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdLibraryAPI_prod_3p.json; https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ValidationConfigurationsAPI_prod_3p.json; https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/PartnerOpportunities_prod_3p.json; https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/AdvertisingAccounts_prod_3p.json | OpenAPI models | 2026-11-09 | Searched for experiment/holdout terms; context only |
| Release notes index, Ads API v1, v0 and Deprecations, re-read (gap fill) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md; https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v1.md; https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v0.md; https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md | Release notes | 2026-11-09 | Audience notes 2024–2025; RSoV (2025-10-15); Events (2025-09-26, 2026-09-28, 2026-10-15); MMM; Brand Lift (2023-10-09); ListMigrations; legacy accounts entry verbatim; product-collection entries; `/v2/stores` table row; no experiment notes |
| Amazon Advertising API License Agreement (gap fill) | https://advertising.amazon.com/API/docs/oas | Legal (Amazon Ads) | 2026-11-09 | Licence scope; restrictions (i), (j), (n), (o); quota; confidentiality; personal data; "Last Updated: June 1, 2024" |
| Amazon Ads API Policies (gap fill) | https://advertising.amazon.com/resources/ad-policy/api | Policy (Amazon Ads) | 2026-11-09 | Eligibility to hold API access |
| Amazon Ads Partner Network Policies (gap fill) | https://advertising.amazon.com/resources/ad-policy/partner-network-policies | Policy (Amazon Ads) | 2026-11-09 | Data security, use, retention, combination, credentials, throttling |
| SP-API Data Protection Policy (gap fill) | https://sellercentral.amazon.com/solution-provider/policy?policyType=DPP&locale=en_US (redirect from …/mws/static/policy?documentType=DPP) | Policy (SP-API) | 2026-11-09 | MFA, TLS, 24-hour incident notice, 30-day deletion, data attribution, PII rules |
| SP-API Acceptable Use Policy (gap fill) | https://sellercentral.amazon.com/solution-provider/policy?policyType=AUP&locale=en_US | Policy (SP-API) | 2026-11-09 | AI transparency, throttling, no cross-user aggregation or disclosure |
| SP-API changelog: Updates to the DPP and AUP (gap fill) | https://developer-docs.amazon/sp-api/changelog/updates-to-the-data-protection-policy-and-acceptable-use-policy | Changelog (SP-API) | 2026-11-09 | Effective 2025-11-25; 18-month non-PII line |
| Purchases (Amazon retail conversions), Reporting v1 field page (gap fill) | https://advertising.amazon.com/API/docs/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases (markdown: https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md) | Guide | 2026-11-09 | 56 `metric.multiTouch*` field ids |
| Protect Amazon API Applications with Data Retention and Recovery (gap fill) | https://developer-docs.amazon/sp-api/docs/protecting-amazon-api-applications-data-encryption-and-recovery | Guide (SP-API) | 2026-11-09 | "for informational purposes only"; PII 30 days; non-PII "strictly necessary" |

### Unreachable

- **The Ads API docs site as HTML** (`https://advertising.amazon.com/API/docs/en-us/...`): a JavaScript shell whose `server-config` meta names the cloudfront host. Every page cited was read from the markdown copy instead. `https://advertising.amazon.com/API/docs/llms.txt` serves the same shell. On the cloudfront host, `llms.txt`, a sitemap and a navigation JSON answered 404.
- **Guessed doc paths that answered 404 on the markdown host:**
  - `guides/get-started/sandbox`;
  - `mcp/lite`;
  - `guides/developer_notes`;
  - `guides/change-history/overview`;
  - `guides/stores/insights`;
  - `guides/eligibility/overview`;
  - `guides/product-metadata/overview`;
  - `guides/recommendations/tactical-recommendations/overview`;
  - `reference/portfolios`;
  - `guides/account-management/user-permissions`;
  - `guides/reporting/ads-v1/faq`;
  - `guides/reporting/ads-v1/accounts`;
  - `guides/amazon-ads-well-architected-framework/account-management`;
  - `guides/amazon-ads-well-architected-framework/overview`.

  These were guesses. The families they would cover were read from their OpenAPI models instead.
- **Amazon Ads API v1, Sponsored Television** (`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISTV_prod_3p.json` and its merged copy): 403. STV batch limits are not recorded here.
- **MCP tool specifications** `recommendations.json`, `insights.json`, `brand_stores.json`, `audiences.json`, `user_management.json` and `amc_workflow.json` under `https://d3a0d0y2hgofx6.cloudfront.net/en-us/mcp/`: S3 `NoSuchKey`. Those group names were guesses.
- **Amazon news pages:**
  - `advertising.amazon.com/library/news/amazon-ads-mcp-server`, `…/unboxed-2025-announcements` and `…/unboxed-2026-announcements`: 404;
  - `…/library/news/unboxed-2026`: 301, then 404;
  - `aboutamazon.com/news/innovation-at-amazon/amazon-ads-unboxed-2025` and `…-2026`: 404.

  These were guessed URLs. The verifier found the real pages by search (`…/library/news/amazon-ads-mcp-server-open-beta` and `…/library/news/unboxed-2026-news-announcements`) and read them; they are in the table above.
- **Amazon Ads console help page `GR9KP77YZUD3UEZD`** (user permissions to API permissions), linked by an Amazon contributor in issue #406: not fetched in this session. The API *Permissions* guide was read instead.
- **Fivetran connector page, first 100,000 characters:** site navigation only. The connector content was in the remainder, which was read.
- **Practitioner blogs and agency write-ups:** not reached, because web search was unavailable to this seat for this file. No URL was known in advance.
- **Gap fill 2026-11-09, unreachable:**
  - *Amazon Ads API program policies* (`https://advertising.amazon.com/API/docs/policy/en_US`, linked from the License Agreement as the home of the Ads "Data Protection Policy and Acceptable Use Policy"): a JavaScript shell ("Amazon Ads Advanced Tools Center"). Markdown guesses on the cloudfront host (`policy`, `policy/en_US`, `policy/data-protection-policy`, `policy/acceptable-use-policy`, `developer/policies`) answered 404, and web search found no public copy. The Ads-specific DPP and AUP text is therefore **not** in this file.
  - *Brand Home* model (the `brand-home` reference behind `/brand/stores/v1/storePages/list`): `BrandHome_prod_3p.json` answered S3 `AccessDenied`, and other guessed names answered 403.
  - AMC reporting and audience models: guessed names (`AMCReporting_prod_3p.json`, `AMCAudiences_prod_3p.json` and others) answered 403. AMC reporting paths are recorded from the MCP `amc` tools and the v1 beta `queries` operations only.
  - Amazon Ads help page `GV7N6KZTH4HF4T2P` ("Migrate from Product collections to Sponsored Brands collections", linked from the ListMigrations note): a JavaScript shell with no text.
  - Guessed guide paths that answered 404 on the markdown host: `targetable-entities`, `guides/sponsored-products/bidding/shopper-cohort`, `guides/creative-asset/search-assets`, `guides/creative-asset/overview`, `guides/sponsored-brands/creatives/video`, `guides/sponsored-brands/video`, `guides/sponsored-brands/stores`, `guides/localization/overview`, `guides/sponsored-brands/reserved-share-of-voice`, `guides/events/overview`.
- **Not called, by rule:**
  - any Ads API host (`advertising-api.amazon.com`, `-eu`, `-fe`), including the skills library at `/skills`;
  - Login with Amazon (`api.amazon.com/auth/...`);
  - the MCP endpoints (`advertising-ai*.amazon.com/mcp`);
  - any SP-API host;
  - the Seller Central help hub's content call;
  - any page behind sign-in, including the AMC UI and the advertising console.

## Open questions

1. **Ireland's host.** Amazon's endpoint tables (*API overview*, *Make your first call*) list no IE, while the Profiles model tables IE under region `EU`, and the limits page and the 2025-07-19 portfolio note include it. Will Amazon add IE to the endpoint tables? (*API overview*; *Profiles* model; issue #391.)
2. **SD and STV on v1.** The 2025-12-01 note promised SD and STV "later in 2025". The current overview and `contracts.json` list both as supported. No release note read here dates their general availability.
3. **The v1 recommendations list path.** The guides and the 2026-08-31 release note give `GET /adsApi/v1/list/recommendations`, while the merged v1 model (`AmazonAdsAPIALLMerged_prod_3p.json`) gives `GET /adsApi/v1/recommendations`.
4. **How SP v1 archives.** SP v1 create and update accept only `ENABLED` and `PAUSED`. No v1 page read here says in a sentence that the v1 delete operation archives, as SD v3 and SB v3 say of theirs.
5. **`partialSuccess` on per-product specs.** The cross-product v1 model answers writes with `partialSuccess`, and the SP per-product model does not name it. Which shape does the live endpoint return for an SP write?
6. **Client-id header name on v1.** Amazon's examples use both `Amazon-Advertising-API-ClientId` and `Amazon-Ads-ClientId`. Do all v1 families accept both?
7. **Consistency after a write.** Amazon gives a 30-second P99 for synchronous CRUD and, for one DSP API, a 5-minute window. No sponsored ads page read here states when a write becomes visible to a list or query.
8. **Budget-usage freshness.** `usageUpdatedTimestamp` is returned, but no page read here states the refresh cadence (issue #413 is unanswered).
9. **Throttling scope.** Amazon describes TPS limits as regional per endpoint, per ad product for v1, and per client id for reporting v1. Field report #422 describes one seller throttled while others on the same client were not. Is there also a per-advertiser limit?
10. **LwA limits.** The Ads API pages read here do not state limits on the Login with Amazon token endpoint, which the door calls before every request.
11. **Product collections end date.** The deprecation entries read say January 2027; the ListMigrations note says February 2027.
12. **"Review Requests API (beta)".** It is dated 2026-11-16 in the release notes index, after this reading's date.
13. **Harvest tool.** Field report #450 names `create_campaign_harvest_targets`, which the published `campaign_management` spec of 2026-11-09 does not list. Was it withdrawn, renamed, or never published?
14. **EG Sponsored Products max bid.** The limits page row reads 0.15/5.50 EGP, out of line with its SD column (7400). Is it a typo?
15. **SD v1 budgets.** Does the SD v1 campaign update still ignore a budget without `recurrenceTimePeriod` (issue #475)?
16. **Reporting v1 concurrency scope.** One concurrent report per client id (*Reporting API v1 overview*; *Limits and best practices*) or per advertiser (*Amazon Ads reporting overview*; GA note 2026-09-30)?
17. **MCP open-beta date.** The newsroom post is dated 2026-02-02 and the release note 2026-02-18.
18. **Stores view permission.** The *Permissions* guide gives Stores builder no View permission ("N/A"), while the *Stores* model accepts `amazon_stores_view`.
19. **The Ads API Data Protection Policy.** The License Agreement binds licensees to an Ads "Data Protection Policy and Acceptable Use Policy" whose page is a JavaScript shell. Does it set retention, encryption or incident-notice figures like the SP-API DPP's?
20. **Audience id spaces.** `POST /audiences/list` (SD), `POST /targetableEntities/list` (SP, SB, SD, STV) and v1 beta `query/audiences` each return an `audienceId`. Are they the same ids? The SP v3 model says only "Audience IDs are guaranteed to be unique across all audience types".
21. **SP Amazon-built audiences.** The 2025-03-12 note on Amazon-built SP audiences was "in preview only" and promised an update "once this functionality is made available". No later SP note read here makes that announcement.
22. **The shopper-cohort recommendation's units.** SP v3 `ShopperCohortBiddingRecommendation.percentage` is described as "basis points, e.g., 900 = 9%", while the campaign field of the same name is a percentage of up to 900.
23. **`targetPGDealId` or `targetedPGDealId`.** The RSoV guide's step list and its sample use different names. The SB v4 model has only `targetedPGDealId`.
24. **Product collections: January or February 2027.** This repeats open question 11 with the page-by-page table in section I. Four statements say January and one later note says February.
25. **The SP-API 18-month non-PII limit.** The changelog effective 2025-11-25 says it was added, but the DPP text served on 2026-11-09 does not contain it.
26. **Unlisted models.** Targetable Entities, AMC Administration and `SponsoredBrands_prod_3p.json` are served but not listed in `contracts.json`. Are they current?

## Positions

**P-ads-api-surface-1.** The Ads API is served from three regional hosts: `advertising-api.amazon.com` (US, CA, MX, BR), `advertising-api-eu.amazon.com` (UK, FR, IT, ES, DE, NL, AE, PL, TR, EG, SA, SE, BE, IN, ZA) and `advertising-api-fe.amazon.com` (JP, AU, SG). A region's data is reachable only through its own host. [official] *API overview*; *Well-Architected Framework: Fundamental component*.

**P-ads-api-surface-2.** Ireland (IE, EUR, `Europe/Dublin`) is a country code in the Profiles model, which tables it under region `EU`, and it has a row in Amazon's bid-limits table; a developer reports IE profiles returned since late May 2025. Amazon's endpoint tables do not list it. [official] *Profiles* model; *Limits, constraints, and quotas*; *API overview*. [opinion] `salton4`, issue #391.

**P-ads-api-surface-3.** Login with Amazon issues tokens from regional token hosts, and "the resulting tokens are valid globally across all regions"; an access token is valid for 60 minutes. [official] *Authorization grants*; *Access tokens*.

**P-ads-api-surface-4.** Refresh tokens for Amazon Ads advertising scopes issued on or after 2026-07-30 expire 365 days from the advertiser's consent. Tokens issued before then have no fixed expiry, and an invalid refresh token is answered `400 invalid_grant`. [official] *Refresh tokens*; *Release notes* (2026-05-26). [opinion] Airbyte.

**P-ads-api-surface-5.** The `advertising::campaign_management` scope lets a client application act with whatever advertising permissions the authorizing user holds. A permission such as `amazon_stores_edit` belongs to the user and cannot be added to a client. [official] *Permissions*; *Authorization grants*. [opinion] `jerirose` (Amazon Ads docs contributor), issue #406.

**P-ads-api-surface-6.** Every OpenAPI operation states the permissions it requires ("Requires one of these permissions"). In the Sponsored Products model, most reads accept `advertiser_campaign_view`, and writes require `advertiser_campaign_edit` or `campaign_proposed`. "Requests will receive a `401 Unauthorized` response if the authorizing account does not have the required permissions." [official] *Sponsored Products* model; *Permissions*; *Manager accounts*.

**P-ads-api-surface-7.** A profile is one advertising account in one marketplace. `GET /v2/profiles` takes no Scope header, returns only the calling region's profiles, defaults to `accessLevel=edit`, and returns at most 5000 items. [official] *Profiles* model; *Profiles*.

**P-ads-api-surface-8.** The Profiles model states that the profiles call "does not return a response unless the current account has created at least one campaign using the advertising console". [official] *Profiles* model.

**P-ads-api-surface-9.** A profile's `accountInfo.type` is `seller`, `vendor` or `agency`. Seller and vendor profiles run sponsored ads, with Sponsored Brands and Sponsored Display requiring Brand Registry. Agency profiles serve Amazon DSP and Data Provider. [official] *Profiles*; *Profiles* model.

**P-ads-api-surface-10.** Ads API v1 reporting, v1 recommendations and Stream v2 identify the advertiser by a global account id (`amzn1.ads-account.g.*`) or a DSP advertiser id, in the request body or the `Amazon-Ads-AccountId` header, not by profile. `POST /adsApi/v1/query/advertiserAccounts` maps a global account to its per-marketplace `profileId`s. [official] *Query advertiser accounts*; *Stream v2: Create a subscription*; *Recommendations API: How to*; *Reporting v1 quickstart*.

**P-ads-api-surface-11.** Stream v2 does not accept a manager account id or a Seller Central account id (MCID) as an advertiser id. In Amazon's words, "A selling-partner ID identifies a Seller or Vendor account, not an advertiser account". [official] *Stream v2: Create a subscription*.

**P-ads-api-surface-12.** Ads API v1 is a single set of `POST` create, update, query and delete operations on campaigns, ad groups, ads, targets and ad associations, with a keyword expressed as a target. Amazon says the v1 APIs "will eventually fully replace the ad product-specific APIs". [official] *Amazon Ads API v1 overview*; *Campaign management: Entities overview*.

**P-ads-api-surface-13.** Amazon announced worldwide general availability of Ads API v1 campaign management for Sponsored Products, Sponsored Brands and Amazon DSP in its 2025-08-01 note and again under the title "Campaign Management API now generally available" on 2025-12-01, replacing "nearly 200 separate variations" of CRUD endpoints with 16. Amazon's current v1 contract and campaign-management overview list Sponsored Display and Sponsored Television as supported as well. [official] *Release notes: Ads API v1*; *contracts.json*; *Campaign management overview*.

**P-ads-api-surface-14.** At launch, a v1 campaign-management call is bound to one ad product, and its rate limit applies per ad product. [official] *Campaign management overview*.

**P-ads-api-surface-15.** v1 batch sizes differ by ad product and are published as `maxItems` and `maxResults` in each product's v1 specification. Sponsored Brands campaign, ad-group and ad writes take far fewer items per call than Sponsored Products'. [official] *Amazon Ads API v1, Sponsored Products / Sponsored Brands / Sponsored Display* models.

**P-ads-api-surface-16.** Amazon's bulk writes answer HTTP 207 Multi-Status, and "Applications must parse the response body to determine the status of each individual operation". Each result carries the item's `index` in the request. [official] *Well-Architected Framework: Fundamental component*; *Amazon Ads API v1* model; *Sponsored Products* model.

**P-ads-api-surface-17.** The cross-product v1 model's writes return three lists: `success`, `partialSuccess` (an item written with some fields refused, with its errors) and `error`. [official] *Amazon Ads API v1* model.

**P-ads-api-surface-18.** No sponsored ads create, update or delete operation in Amazon's v1, SP v3, SB v3, SB v4, SD v3 or Portfolios models takes an idempotency key. Amazon's models carry idempotency keys only for DSP audiences, AMC custom models and billing. [official] the named models in *contracts.json*.

**P-ads-api-surface-19.** Amazon's SP v2 and SB v3 models state that "Sellers aren't allowed to have duplicate campaign names, but vendors can have duplicate campaign names." [official] *Sponsored Products v2* model; *Sponsored Brands v3* model.

**P-ads-api-surface-20.** `ARCHIVED` is a terminal state. v1 defines it as "permanently stopped and cannot be reactivated. Terminal end state". In Sponsored Display v3 and in Sponsored Brands v3 keyword and target paths, `DELETE` sets the entity to archived, which "is permanent and can't be undone". [official] *Amazon Ads API v1* model; *Sponsored Display v3* model; *Sponsored Brands v3* model.

**P-ads-api-surface-21.** In Sponsored Products v1, the create and update states are `ENABLED` and `PAUSED` only, while an entity can be read as `ARCHIVED`. [official] *Amazon Ads API v1, Sponsored Products* model.

**P-ads-api-surface-22.** Entities Amazon created automatically, such as an auto campaign's targeting clauses, are refused for some edits. The refusals are `AUTOCREATED_ENTITY_CANNOT_EDIT` (v1) and `AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY` (SP v3). [official] *Amazon Ads API v1* model; *Sponsored Products* model.

**P-ads-api-surface-23.** v1 entities report a user-set `state` and a separate delivery status (`DELIVERING`, `LIMITED`, `NOT_DELIVERING`, `UNAVAILABLE`), with reasons such as `NOT_IN_BUYBOX`, `OUT_OF_STOCK` and `CAMPAIGN_OUT_OF_BUDGET`. SP v3 reports the same kind of signal as `extendedData.servingStatus` and `extendedData.servingStatusDetails` under `includeExtendedDataFields`. [official] *Amazon Ads API v1* model; *Sponsored Products* model.

**P-ads-api-surface-24.** Amazon's *Rate limiting* page says list extended data operations, which add entity status, "hold 5x the weight of standard calls towards throttling limits". [official] *Rate limiting*.

**P-ads-api-surface-25.** A throttled call is answered 429 with a `Retry-After` header giving seconds to wait, and "Rate limiting will occur dynamically based on the overall system load". Amazon publishes no fixed TPS for the campaign-management APIs. [official] *Rate limiting*. [opinion] Airbyte.

**P-ads-api-surface-26.** Amazon's guidance is to retry server (5xx) and throttling (429) errors with exponential backoff, to investigate other 4xx errors before retrying, and to use longer backoff for report generation. Its Well-Architected Framework says to implement retry logic "when calling services that are idempotent and where retries improve your client availability". [official] *Rate limiting*; *Well-Architected Framework: Fundamental component*.

**P-ads-api-surface-27.** Field reports describe 429 responses without a `Retry-After` header: on change history for a single seller, persisting for over 24 hours (#422), and from the MCP gateway as an HTML page (#436). [opinion] `RianKoja`, issue #422; `ciocca-dev`, issue #436.

**P-ads-api-surface-28.** Amazon's *Reporting v1: Limits and best practices* and *Reporting API v1 overview* state that Reporting v1's rate and concurrency limits apply per client id, shared across every advertiser account the client calls for, with concurrency "as low as 1"; Amazon's *Amazon Ads reporting overview* and its 2026-09-30 GA note state "one concurrent report per advertiser". [official] those four pages.

**P-ads-api-surface-29.** Exports return a snapshot of current campaign, ad group, ad or target metadata through `POST /{entity}/export` and `GET /exports/{exportId}`. The default cap is 5 in-progress jobs per endpoint, and download URLs are valid for one hour and regenerable for 24 hours. Amazon recommends exports "one to two times per day" and in place of "thousands of list operations". [official] *Exports FAQ*; *Rate limiting*.

**P-ads-api-surface-30.** Change history (`POST /history`) returns changes for Sponsored Products and Sponsored Brands only, up to 90 days back, and "doesn't return information about who made the change". [official] *Change history* model.

**P-ads-api-surface-31.** Budget usage is read with `POST /{sp,sb,sd}/campaigns/budget/usage` and `/portfolios/budget/usage`, up to 100 ids per call. Each result gives `budgetUsagePercent` and `usageUpdatedTimestamp`. [official] *Sponsored Products* model; *Sponsored Display v3* model; *Sponsored Brands v4* model; *Portfolios* model.

**P-ads-api-surface-32.** Product eligibility for an ad type is read with `POST /eligibility/product/list` (up to 50 products), which answers `ELIGIBLE`, `ELIGIBLE_WITH_WARNING` or `INELIGIBLE` with reasons. `POST /product/metadata` returns availability, price, best seller rank and eligibility for up to 300 ASINs or SKUs. [official] *Eligibility* model; *Product selector* model.

**P-ads-api-surface-33.** Amazon's recommendations come on three surfaces with different shapes: product-specific keyword, target, bid and budget recommendations; tactical recommendations at `/recommendations/list` and `/recommendations/apply`; and the v1 Recommendations API at `/adsApi/v1/query/recommendations`. [official] *Sponsored Products* model; *Recommendations* model; *Recommendations API overview*.

**P-ads-api-surface-34.** Amazon Marketing Stream v2 writes Parquet files to an S3 bucket and sends notifications to an SQS queue in the subscriber's own AWS account. A destination "belongs to the application that first uses it", and a client application may register at most 5 destinations. [official] *Stream v2: Data delivery*; *Stream v2: Set up your destination*; *Stream v2: Limits*.

**P-ads-api-surface-35.** Reporting v3, Sponsored Ads v2 reporting and Marketing Stream v1 stop on 2027-06-30; Reporting v1 and Stream v2 have been generally available since 2026-09-30. [official] *Deprecations*; *Release notes* (2026-09-30); *Stream: Sponsored ads campaign management datasets*.

**P-ads-api-surface-36.** Amazon Marketing Cloud has been open to every advertiser running sponsored ads since 2025-09-16. It uses its own `Amazon-Advertising-API-AdvertiserId` and `Amazon-Advertising-API-MarketplaceId` headers and requires terms to be accepted "once in each region (NA, EU, and FE)" in the AMC UI. Raw event information "cannot be exported"; aggregated results can. [official] *Release notes* (2025-09-16); *Get access to AMC using self-service APIs*; *Instance management*; *How does Amazon Marketing Cloud work*.

**P-ads-api-surface-37.** Advertising test accounts do not serve ads or bill. They are created with the separate `advertising::test:create_account` scope as `VENDOR` or `AUTHOR` accounts only. Rules can be configured in them but do not take effect, and Sponsored Brands campaigns in them are auto-approved. The sandbox host `advertising-api-test.amazon.com` shut off on 2022-06-28. [official] *Test accounts overview*; *Using test accounts*; *Advertising test account* model; *Deprecations*.

**P-ads-api-surface-38.** The Amazon Ads MCP server is served from `advertising-ai.amazon.com`, `-eu` and `-fe` (`/mcp` and `/mcp/lite`), not from the Ads API hosts. It authenticates with the same LwA token and client id, and takes account context either per tool (Dynamic) or fixed by header. [official] *MCP: Get started*; *MCP: Get started with Lite*; *MCP: OAuth*.

**P-ads-api-surface-39.** Amazon's published MCP `campaign_management` tool group holds 32 tools, including single-call Sponsored Products campaign creation, target-bid and campaign-budget updates, and product eligibility. Amazon distinguishes deterministic "standard tools" from "expert tools" with inference behind them. [official] *MCP tools: campaign_management*; *MCP overview*.

**P-ads-api-surface-40.** Amazon's skills library for AI clients is served by `GET /skills` on the Ads API hosts, and an `ads-api-migration` skill for moving integrations to v1 was published on 2026-11-02. [official] *MCP skills: Get started*; *MCP: AI migration skills*.

**P-ads-api-surface-41.** Legacy account APIs (`/adsAccounts*`, `/dsp/advertisers*`) have been deprecated since July 2026, with `Warning: 299` response headers, and answer 404 from July 2027. [official] *Release notes* (2026-07-20); *Deprecations*.

**P-ads-api-surface-42.** Sponsored Brands product collection ads are being retired. From August 2026 a product-collection create makes a manual collection instead. Amazon's *Deprecations* entries (V0 and V1) and its *Product Collection Migration Guide* say creates return an error after January 2027, and the ListMigrations release note of 2026-09-18 says "Beginning February 2027, product collections will no longer be supported." `POST /sb/v4/migrations/list` returns recommended replacements. [official] *Deprecations*; *Product Collection Migration Guide*; *Release notes* (2026-09-18).

**P-ads-api-surface-43.** Developers report v1 behaviour that departs from the specification: an SD budget update without `recurrenceTimePeriod` silently ignored (#475), an SP prompt-extension pause that reverts by the next day (#524), and a required `statusMessage` absent from `query/advertiserAccounts` (#525). [opinion] `zhangwg4apollo`, issue #475; `AlexUnitix`, issue #524; `vudathayajushi`, issue #525.

**P-ads-api-surface-44.** Amazon's API P99 targets are 30 seconds for synchronous CRUD, 12 hours from an impression or click to its availability in the API, and 72 hours for invalidation. [official] *Limits, constraints, and quotas*.

**P-ads-api-surface-45.** Audience ids for Sponsored Products and Sponsored Brands audience bid adjustments are read from `POST /targetableEntities/list` (media type `application/vnd.Mindreader.TargetableEntitiesResource.v1+json`, required `adProduct`). Amazon-built audiences are under `pathsFilter` `[["Audience Category","Custom-built","Product"]]` and AMC audiences under `[["Audience Category","Custom-built","AMC"]]`, and "Only the audiences retrieved using these filters are usable." [official] *Targetable Entities* model; *Sponsored Products* model; *Sponsored Brands v4* model; *Shopper cohort bidding* (SB).

**P-ads-api-surface-46.** Sponsored Display audience ids for `audience(audienceSameAs=…)` targets are read from `POST /audiences/list` with `adType: SD` and one country, after browsing `POST /audiences/taxonomy/list`. The Audiences discovery model's `adType` takes `DSP`, `SD` or `ST`, with no SP or SB value. [official] *Audiences discovery* model; *Sponsored Display audience targeting*; *Sponsored Display v3* model.

**P-ads-api-surface-47.** An SP v3 audience bid adjustment is a `dynamicBidding.shopperCohortBidding[]` entry of 0–900 percent with one audience segment. Amazon's model states it applies on top of placement adjustments: a 50% placement adjustment on a $1.00 bid gives $1.50, and a 100% shopper-cohort adjustment then gives $3.00. In v1 the field is `bidAdjustments.audienceBidAdjustments[]`, at most one per campaign. [official] *Sponsored Products* model; *Amazon Ads API v1* model.

**P-ads-api-surface-48.** Amazon's SB shopper-cohort guide states "We only allow one audience group per one campaign" for Sponsored Brands audience bid adjustments. [official] *Shopper cohort bidding* (SB).

**P-ads-api-surface-49.** New images and videos for Sponsored Brands, Sponsored Display, Stores and DSP enter the asset library in three calls: `POST /assets/upload` returns a URL that "expires in 15 minutes" and "only supports PUT"; the file is `PUT` to that URL, an S3 host in Amazon's examples; `POST /assets/register` returns an `assetId`. The asset is usable in a campaign once its status is `ACTIVE`, which "can be … up to 30 minutes". [official] *Creating assets*; *Asset library* model.

**P-ads-api-surface-50.** Amazon's *Creating assets* guide requires sellers to include their brand entity id when registering an asset, "You can find this using the `GET /brands` endpoint" (SB v3, which returns `brandEntityId` "available exclusively for seller advertisers"). `/v2/stores` has been shut off since 2026-06-01. [official] *Creating assets*; *Sponsored Brands v3* model; *Deprecations*.

**P-ads-api-surface-51.** Amazon's asset library "does not perform checks on eligibility for images", and its processing "is not part of the moderation process". Moderation of the creative happens separately (section N). [official] *Creating assets*.

**P-ads-api-surface-52.** The Localization API maps keywords, products, targeting expressions and currencies from a source marketplace to target marketplaces (`POST /keywords/localize`, `/products/localize`, `/targetingExpression/localize`, `/currencies/localize`). For sellers, a localized product's SKU "must match the SKU of the source product". [official] *Localization* model.

**P-ads-api-surface-53.** Sponsored Brands reserve share of voice sells top-of-search placement for branded keywords at a fixed price through v1 `/advertisingDeals/sb`, `/advertisingDealTargets/sb`, `/brandedKeywordsPricings/sb` and `/keywordReservationValidations/sb`. Amazon's guide requires at least five deal targets and a `PROPOSED` deal before the SB v4 campaign is created, and a `PROPOSED` deal "cannot be modified". [official] *Release notes* (2025-10-15); *Reserve share of voice*; *Amazon Ads API v1* merged model.

**P-ads-api-surface-54.** The v1 beta `promotionOffers` and `promotionRewards` operations list promotion offers and rewards on the advertiser's account and need billing permissions (`nemo_transactions_view` or `_edit`). [official] *Amazon Ads API v1 betas* model.

**P-ads-api-surface-55.** The Events API (`POST /adsApi/v1/create/events`, GA 2026-10-15) takes off-Amazon conversion events server to server. Amazon announced it for "self-serve Amazon DSP advertisers" with conversions managed in the DSP console's Events Manager. [official] *Release notes* (2025-09-26, 2026-10-15); *Amazon Ads API v1* merged model.

**P-ads-api-surface-56.** Amazon's published measurement operations are Brand Metrics (`/insights/brandMetrics/report`), Amazon Attribution (`/attribution/*`), Marketing Mix Modeling (`/mmm/v1/*`), DSP Brand Lift, creative-testing, audience-research and omnichannel studies (`/dsp/measurement/*`, `/measurement/*`), AMC administration (`/amc/*`) and the v1 beta clean rooms and queries. The control groups and creative tests are in the DSP measurement model only. [official] the models in section AF.

**P-ads-api-surface-57.** No operation for a sponsored ads experiment, A/B test, split test or holdout appears in any Amazon Ads OpenAPI model or release note read on 2026-11-09. [official] the models and release notes in section AF.

**P-ads-api-surface-58.** The Amazon Advertising API License Agreement limits Confidential Information to disclosure "to the Amazon Advertising Participant to which such data or information relates" and to use "for creating, managing, and reporting Amazon Advertising ad campaigns by or on behalf of the particular Amazon Advertising Participant that has expressly authorized you". It forbids generating "repetitive or otherwise invalid clicks, impressions, queries or other interactions". [official] *Amazon Advertising API License Agreement*.

**P-ads-api-surface-59.** Amazon's Partner Network Policies forbid "Sharing or combining Amazon Data with any other third-party data sources … without express prior written approval from Amazon" and keeping Amazon Data "beyond its intended use". They require deletion "when no longer required for a Permitted Use", and conformity with Amazon's throttling limits. [official] *Amazon Ads Partner Network Policies*.

**P-ads-api-surface-60.** Amazon states that "The Amazon Ads API is made available only to companies that do not operate a significant ecommerce business …, a demand-side ad platform, or an ad network." [official] *Amazon Ads API Policies*.

**P-ads-api-surface-61.** For SP-API data, Amazon's Data Protection Policy requires notifying Amazon within 24 hours of a security incident, and deleting Information within 30 days of the earliest of Amazon's notice, the customer's revocation, the provider's own finding that it is no longer authorized, or termination. It requires stored Information to be in a separate database or tagged by origin. The Acceptable Use Policy forbids aggregating data "across Authorized Users' businesses" to provide to others, and disclosing Information "individually labelled or aggregated, to other Application users". [official] *SP-API Data Protection Policy*; *SP-API Acceptable Use Policy*.

**P-ads-api-surface-62.** Amazon's SP-API Acceptable Use Policy requires solution providers to "Be explicit about any calculations and the use of models such as artificial intelligence in the service you provide, their accuracy and data freshness". It also requires "data integrity and validation checks" for AI-driven analytical processing that has material impact on an Authorized User's business. [official] *SP-API Acceptable Use Policy*.

**P-ads-api-surface-63.** The Sponsored Products v3 `includeExtendedDataFields` option returns an `extendedData` object with `creationDateTime`, `lastUpdateDateTime`, `servingStatus` and `servingStatusDetails`. The request parameter's own description calls them "creationDate, lastUpdateDate, servingStatus". [official] *Sponsored Products* model.

**P-ads-api-surface-64.** In Amazon's Sponsored Brands specifications, `/sb/negativeKeywords` is on the SB v3 file (`sponsored-brands/3-0/openapi.yaml`), and `GET /sb/negativeTargets/brands/recommendations` is on the v4 surface (`sponsored-brands/4-0/openapi.json`, and `SponsoredBrands_prod_3p.json`, which is titled 3.0). [official] the three SB files.

**P-ads-api-surface-65.** Amazon publishes a Sponsored Display v1 specification with create, update, query and delete for campaigns, ad groups, ads and targets, and its v1 contract and campaign-management overview list Sponsored Display as supported. No release note dates its general availability. [official] *Amazon Ads API v1, Sponsored Display* model; *contracts.json*; *Campaign management overview*; *Release notes: Ads API v1*. [opinion] `zhangwg4apollo`, issue #475; `iYetaimei`, issue #481.

**P-ads-api-surface-66.** Amazon names `POST /adsApi/v1/query/advertiserAccounts` as the replacement for "Account retrieval and listing" by `POST /adsAccounts/list` and `GET /adsAccounts/{accountId}`. Since July 2026 "new client integrations are blocked" from the legacy endpoints, and from July 2027 they "return `HTTP 404 Not Found`". [official] *Deprecations*.

**P-ads-api-surface-67.** The UK is `UK` in the Profiles model and `GB` in the v1 `Marketplace` and `CountryCode` enums. [official] *Profiles* model; *Amazon Ads API v1* model.

### Seat's positions (enter no skill)

- [seat] Taken together, Amazon's pages make a write's reply evidence of what Amazon accepted, not of what now serves. The 207 shape, `partialSuccess`, terminal archiving, no idempotency key, and the field reports of silent no-ops and reverting states all point the same way. The entity read afterwards is the evidence of its state.
- [seat] The surface the door reaches is being moved, between 2025 and mid-2027, from per-product, profile-scoped APIs to v1 APIs scoped by global account. The parts that move first (reporting, Stream, recommendations) are the parts that need the global account id the door's text does not yet name.
- [seat] Two of the families Amazon steers volume toward (exports and Stream) deliver their data outside an HTTP reply: as a short-lived download URL or as files in an AWS account. Those are the places where the door's "lands Amazon's reply as Amazon gave it" stops being the whole delivery.
- [seat] Under one ComChatX client id, every limit Amazon applies per client (Stream v2 destinations and subscription rates, and reporting v1 if its per-client reading holds) is shared by every seller using the door. Limits applied per ad product or per region are shared the same way across sellers in that region.
- [seat] (gap fill) The asset library splits creative work across two hosts: the Ads API origin for the request, registration and creative, and an S3 URL for the bytes. Through a door bound to the Ads API origins, a seller's ad work with existing imagery is fully reachable and work that needs new imagery is not.
- [seat] (gap fill) The binding terms recorded in section AG speak of the licensee and its "Amazon Advertising Participant". Under one ComChatX client id, every seller is a separate Participant, and the licence's confidentiality clause reads per Participant.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** I re-opened every Amazon guide cited, by plain GET of its markdown copy at `https://d3a0d0y2hgofx6.cloudfront.net/en-us/<path>.md`, and grepped each one for the quoted words. I also re-opened every OpenAPI model cited (`contracts.json`, the per-product and merged v1 models, SP v3, SP v2, SB v3, SB v4, SD v3, Profiles, Portfolios, Change history, Eligibility, Product selector, Moderation, Brand Metrics, Stores, Test account, Exports, Recommendations, Manager account, Attribution, Advertising accounts, Stream v1). From those models I parsed paths, enums, `maxItems`/`maxResults`, `required` fields, multi-status schemas and permission strings. The MCP tool specifications were counted as OpenAPI operations. Of the release notes, I read the index and the v1 page whole for titles and dates, and the cited notes in full. I read the *Deprecations* page whole. I read the GitHub issues and comments through the public GitHub API, checking author, date, author association and the quoted text; the denisneuf repository was checked by its API and its README. I read the Airbyte and Fivetran pages as text. Web search was used to look for 2025–2026 announcements that could overturn a claim. That turned up the MCP open-beta newsroom post and the unBoxed 2026 news page, both read; nothing found there overturns a claim beyond the corrections below. Claims checked: about 230. Positions were checked against the wording rule. None prescribes behaviour (when to ask, a sequence, a threshold as a rule, a ceiling, or how cx talks). Four were reworded because they stated as Amazon's flat fact something that Amazon's pages state differently or contradict.

**Corrections (was → now).**

1. §A, profiles per region: was sourced to the DSP global-seat note (about manager accounts) → now sourced to the *Profiles* guide's "Regions" sentence, with the global-seat note kept as a DSP-specific parallel.
2. §A and the door follow-up on Ireland: was "No Amazon page read here says [IE is EU]" with IE's region inferred → now the Profiles model's own region table reads "|EU|IE|Ireland|" (also `Europe/Dublin`); only the endpoint tables omit IE. P-2 and open question 1 were updated to match.
3. §B, `invalid_client`: was an [official] rule → now noted as not documented on any Ads API page read; the invalidation causes from *Refresh tokens* were added.
4. §B, client-id header: was "`Amazon-Advertising-API-ClientId` on every call; the v1 page and MCP pages also name `Amazon-Ads-ClientId`" → now *Make your first call* itself names only `Amazon-Ads-ClientId`. Each name is listed with the pages that use it. Door follow-up 10 was updated to match.
5. §B, Scope errors: was cited to *Make your first call*, v1 getting started and *Errors* for "400 or 401" → now the "401 … or 400" sentence is cited to the *Profiles* guide, and the *Errors* page's own 401/403/406/415/422 rows are quoted. P-6 now quotes *Permissions* for the 401.
6. §C, KDP: was "a seller-type profile with `subType` `KDP_AUTHOR`" → now the subType enum only; no page ties it to `seller`.
7. §C, Airbyte quote: was "Only seller and vendor profiles are supported." (not on the page) → now the verbatim "supports only profiles with seller and vendor type, profiles with agency type will be ignored."
8. §C, v1 advertiser-accounts model: was cited to `dtrnk0o2zy01c…/AdvertisingAccounts_prod_3p.json` → that model is the legacy `/adsAccounts` surface; now cited to `AmazonAdsAPIALLMerged_prod_3p.json`. Also added `query/sellingAccounts` (2025-07-15 note).
9. §D, Stores permission: was "`amazon_stores_edit` and `amazon_stores_view`" → now *Permissions* gives Stores builder View "N/A". The model's contrary list is recorded (open question 18), and §Q now gives the model's full list, including `advertiser_campaign_edit`.
10. §D, manager accounts: was "A manager account is bound to its region" → now Amazon's words: links in any marketplace, but API access only "when calling the API host in the region of the linked account". The v1 Manager Account API GA (2026-08-12) was added.
11. §E, release table: was "2025-08-01 available / 2025-12-01 worldwide GA", with the "later in 2025" quote attributed to 2025-12-01 → now the quote is the 2025-08-01 note's, which already announces worldwide GA; the 2025-12-01 note ends "later this year". P-13 was reworded.
12. §E, "currently supports … for" quote: was attributed to `contracts.json` alone → now to the *Campaign management overview* as well.
13. §F, `index` range: was 0–999 → now 0–999 on partial-success items and 0–4999 on `ErrorsIndex`.
14. §F, duplicate-name quote: was truncated inside quotation marks ("but vendors can.") → now verbatim ("but vendors can have duplicate campaign names."). The SB v3 model's contradictory "must be unique to the Amazon Ads account" was added, and P-19 now quotes the models rather than stating the rule flat.
15. §F, consistency: was headed "Writes are eventually visible" with the 30s P99 as support → now the P99 is a response-time guarantee and the visibility gap is marked [seat].
16. §G, enums: was `AdProduct` with `FULL_FUNNEL`, `RMS`, and `SPPlacement` with browse placements, `INTERESTED_AUDIENCE` and `SPCustomerActionType: REVIEW_REQUEST` in "the SP v1 model" → these appear only in the merged prod-and-beta models; the production model lacks them.
17. §G, issue #378: was "Amazon contributor `anandile`" → now GitHub shows no association for that login, and the Amazon contributor `jerirose` closed the issue on his answer.
18. §G, Airbyte id-type quote: was not on the page → now the verbatim "Amazon types adId as a string on the ads entity API but as an integer in reporting v3 … The same applies to adGroupId and campaignId."
19. §H and P-24, 5x weight: was attributed to SP v3 `includeExtendedDataFields` → *Rate limiting* says "list extended data operations" without naming a product, and the attribution is now marked [seat].
20. §H and §M, performance-based budget rules: was "a 7-day lookback for sellers and 14 for vendors" → the page says metrics are calculated "within 7 days of an ad click" (sellers) and 14 (vendors), an attribution window, not a lookback. The metric list now includes `IS` and `NTB` (SB).
21. §I, product collections: added the deprecation entry's exact terms (3-ASIN minimum, 32-character titles, "Post January 2027" error) and the 2026-09-23 worldwide Collections note.
22. §K, unspent budget sharing: was "The page lists the countries" → now the release note lists them. Added `featureState` and the guide's "on by default for portfolios created after 6/20/2025".
23. §L, v2 bid recommendations: was all "shut off 2025-05-15" → now `/v2/sp/targets/bidRecommendations` and the v3 content type shut off 2025-05-15, and the other v2 bid recommendations 2024-03-27. Also noted that the SP v3 model still lists the v3 content type.
24. §L, v1 recommendations path conflict: was "the model read earlier in this session" → now named: the merged v1 model has `GET /adsApi/v1/recommendations`, while the guides and the 2026-08-31 launch note have `/list/recommendations`.
25. §L and §S, "recommendation data / messaging data not in Stream": was cited to the *Stream v2 overview* (which does not say it) → now cited to the *Deprecations* entry, quoted.
26. §N, product metadata: was "`searchStr` (up to 300)" → now `searchStr` is a title search of up to 200 characters, and `asins`/`skus` take up to 300 each (`skus` SP sellers only). Added `adType`, and the 10k cap formula verbatim.
27. §O, change history: was "UTC epoch milliseconds" → now "UTC Epoch format" / "unix time" (milliseconds is not stated).
28. §R, P-28, door follow-up 2 and the seat position: was reporting v1 concurrency "per client id" as settled → now Amazon contradicts itself. Per client id: *Reporting API v1 overview*, *Limits*. Per advertiser: *Amazon Ads reporting overview*, the GA note of 2026-09-30. Both are recorded, with open question 16.
29. §R, §Y, P-35 and stable item 13: was "SB v2 reports" stopping 2027-06-30 → now "Sponsored Ads v2 reporting" (all v2 report endpoints), as *Deprecations* has it.
30. §T, AMC: was "once per region" and an unsourced 2025-02-10 date → now verbatim "once in each region (NA, EU, and FE)", and the 2025-02-10 release note is cited. Also added: the 410 vs 404 wording for retired instance APIs, and that `AdvertiserId` is described differently on two pages.
31. §V, MCP open beta: was 2026-02-18 only → now the newsroom post is dated 2026-02-02 and the release note 2026-02-18 (open question 17). The fixed-mode manager header is spelled `Amazon-Ads-Manager-AccountID` as the MCP pages spell it.
32. §W, the old rate-limiting copy: was "also read" → it answers 404 today, and the row is marked.
33. §Y, Brand Posts: was "June 2025 deprecated" → now deprecated 2025-06-03, shut off 2025-06-16 / 2025-07-31.
34. §B, onboarding: added the "three business days" email reported in #519, and the dates of its four submissions.
35. §G, issue #379: was "Closed with two comments" → now the Amazon contributor confirmed the string type and reported the document fixed.

**Removals.** No claim was removed outright. The unsupported parts were cut from items 3, 6, 7, 18, 27 and 32, or replaced with what the page says. No position needed to move to the seat's list: each kept position has an Amazon or named-practitioner source, and items 13, 19, 24 and 28 were reworded as attributed statements.

**Pages that stayed unreachable.**

- *Amazon Ads API v1, Sponsored Television* model (`AmazonAdsAPISTV_prod_3p.json`): still 403.
- MCP spec files `recommendations.json` and the other guessed group names: still `NoSuchKey`.
- `guides/get-started/rate-limiting.md`: 404.
- The console help page `GR9KP77YZUD3UEZD`: not fetched (a console help page; the API *Permissions* guide covers the mapping).
- Some of the GitHub REST API: rate-limited after the issue checks. The denisneuf issue #253 and PRs #308/#309 were confirmed through GitHub search instead.

**Hosts.** This verifier called no Ads API host (`advertising-api*.amazon.com`, including `/skills`), no Login with Amazon host, no MCP endpoint (`advertising-ai*.amazon.com`), no SP-API host and no Seller Central content call. Every Amazon read was of the cloudfront docs and model hosts or a public `advertising.amazon.com/library/news` page.

### Gap fill 2026-11-09

Done by the research seat that owns this file, against three completeness critics' lists. Every page and model was read by plain GET on 2026-11-09. No Ads API host, Login with Amazon host, MCP endpoint, SP-API host or Seller Central content call was made. The new material is unverified by an adversarial seat: **Pending verification** for everything below.

**Gaps filled.**

1. *API families missing from the map (lead gap 1, API gap 3).* Added the following, with paths, media types, headers and permissions from the models:
   - section Z, audiences: Audiences discovery; Targetable Entities, a model served but not listed in `contracts.json`; the v1 beta audiences and audience categories; audience overlap insights; and the SP v3, SB v4 and v1 fields that take audience ids;
   - section AA, the creative asset library;
   - section AB, Stores, brands and brand identifiers beyond `GET /pageAsins`: Store insights, v1 brand stores, Brand Home (unreadable), SB v3 `/brands`, `/pageAsins` and `/stores/assets`, and v1 brand associations;
   - section AC, Localization;
   - section AD, the SB reserve-share-of-voice deal, pricing and keyword-reservation-validation operations;
   - section AE, v1 promotion offers and rewards (beta) and the Events API.

   Run-time rows, door follow-ups 17–20, stable item 14 and positions 45–48 and 52–55 cover them.
2. *Creative Assets API and the door (API gap 2).* Section AA records the three-call sequence, the 15-minute S3 upload URL that takes only a `PUT`, and the `PROCESSING` → `ACTIVE` lifecycle. It also records where SB, SD and Store asset ids are used. Door follow-up 16 states that the binary upload goes to a host outside the door's origins, so a creative with new imagery or video cannot be made end to end through the door. Positions 49–51 and stable item 15 cover it.
3. *Binding terms (API gap 4).* Section AG adds the Amazon Advertising API License Agreement, the Amazon Ads API Policies eligibility line, the Partner Network Policies, and, for the sibling SP-API package, the SP-API Data Protection and Acceptable Use Policies and their 2025-11-25 changelog. The Ads-specific DPP and AUP page is a JavaScript shell and is listed as unreachable. Positions 58–62, stable item 17, door follow-up 21 and open questions 19 and 25 cover it.
4. *Measurement paths and experiments (measure gap 5).* Section AF tables the exact paths of Brand Metrics, Attribution, MMM, the DSP measurement studies, AMC Administration (a model not in `contracts.json`), the v1 beta clean rooms and queries, and Events. It also records the result of searching the models, the release notes and *Deprecations*: no sponsored ads experiment, A/B, split-test or holdout operation was found, and control groups and creative tests appear only in the DSP measurement model. Positions 56–57 and stable item 16 cover it. On "multi-touch fields": no OpenAPI model or release note read here has a multi-touch operation or field. The fields live in the Reporting v1 field library. The *Purchases (Amazon retail conversions)* page (`https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md`, re-read 2026-11-09) lists 56 distinct `metric.multiTouch*` ids. Section AF records that multi-touch attribution has no operation of its own and is requested through `POST /adsApi/v1/create/reports`.

**Contradictions settled.**

1. *SB Product Collection shutoff date (contradictions 1 and 8; this file is the owner).* Re-read. Four Amazon statements give **January 2027** for creates returning an error: the *Deprecations* V0 and V1 entries, the *Deprecations* table row, and the *Product Collection Migration Guide*, which says "January 2027 | **Final shutoff**". One statement, the ListMigrations release note of 2026-09-18, gives **February 2027** ("no longer supported"). All agree on August 2026 for the mapping to manual collections. Section I now has a page-by-page table, and P-42 names the pages. The single-date sibling files (`areas/seasons-and-deals.md`, `areas/diagnosis.md`, `areas/keyword-and-product-targeting.md`) should carry both dates with their pages. This file does not edit them.
2. *Reporting v1 concurrency scope (contradiction 2; owner `method/reporting.md`).* Re-read 2026-11-09. Pages that say **per client id**: *Reporting API v1 overview* ("one concurrent report per client ID, not per advertiser account") and *Limits and best practices* ("applies its rate and concurrency limits per client ID"). Pages that say **per advertiser**: *Amazon Ads reporting overview*, in two sentences ("one concurrent report per advertiser, which allows approximately 100 reports per day", and "allows one concurrent report per advertiser"), and the 2026-09-30 GA note. This file's P-28 already records both, so no change was needed. A file that states either side as Amazon's single rule (`beyond/automation-and-amazon-tools.md` §J) is contradicted by the other pair.
3. *Sponsored Display on v1 (contradiction 3; owner).* Section J now records the 16-path SD v1 specification, the overview and `contracts.json` support list, the absence of any dated GA note, and the field reports of SD v1 answering. "Not yet in the unified v1 campaign API" is contradicted by Amazon's specification and overview. "No note announces SD" is correct. P-65 was added.
4. *`brandEntityId` from `/v2/stores` (contradiction 4; owner).* Re-read *Deprecations*: `/v2/stores` was shut off 2026-06-01, replaced by `/brand/stores/v1/storePages/list`, whose `brand-home` model could not be read. The `brandEntityId` source Amazon names today is SB v3 `GET /brands` (*Creating assets*). Sections Q and AB and P-50 record it.
5. *Global account id from `/adsAccounts*` (contradiction 5; owner).* The *Deprecations* entry was re-read verbatim (six endpoints, `Warning: 299`, new integrations blocked since July 2026, 404 from July 2027). Its named replacement for "Account retrieval and listing" is `POST /adsApi/v1/query/advertiserAccounts`. Section C and P-66 record it. `method/reporting.md`'s run-time read of `/adsAccounts*` names a path new clients are blocked from.
6. *`includeExtendedDataFields` field names (contradiction 6; owner).* Re-read the SP v3 model. The response object is `extendedData` with `creationDateTime`, `lastUpdateDateTime`, `servingStatus` and `servingStatusDetails`. The request parameter's description says "creationDate, lastUpdateDate, servingStatus". **Correction to this file (was → now):** §H said the option "adds `servingStatus`, `creationDate` and `lastUpdateDate`", and it now gives the response field names under `extendedData` and quotes the parameter's description. P-23 and the run-time row were aligned, and P-63 was added. `areas/diagnosis.md` and `method/change-measurement.md` have the response names right.
7. *Which SB spec carries which negative path (contradiction 7; owner).* `/sb/negativeKeywords` is on `sponsored-brands/3-0/openapi.yaml`, so this file's §I stands. `GET /sb/negativeTargets/brands/recommendations` is on the v4 surface: `sponsored-brands/4-0/openapi.json`, and `SponsoredBrands_prod_3p.json`, which is titled "Sponsored Brands 3.0" but holds the `/sb/v4/*` paths and is not in `contracts.json`. `areas/search-terms-and-negatives.md` read that file, so its two observations are correct about the file and its "SB 3.0 model" label follows the file's title. `areas/keyword-and-product-targeting.md` and `beyond/brand-defense-and-competition.md` are right to place the recommendation in v4. Section I now tables the three files, and P-64 was added.

**Correction found while filling (own file).** §A said "The UK is `UK` in the Ads API country enum". The v1 models' `Marketplace` and `CountryCode` enums have `GB` and no `UK`, while the Profiles model has `UK`. §A was corrected and P-67 added.

**Declined.** None. No gap item was wrong on the facts. Measure gap 5's "multi-touch fields" were traced to the Reporting v1 field library rather than to a measurement API path (item 4 above).
