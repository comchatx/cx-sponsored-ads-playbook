# Keywords and products to target

Read 2026-11-09 by the research seat.

Tags: [official] is an Amazon page, cited by page name and URL and read 2026-11-09 unless another date is given. Help-center pages also carry the `lastModified` date their content reports. [opinion] is a named practitioner or vendor, with the person or firm given. [research] is a published paper or working paper. [seat] is this seat's own reading. It may appear in the file but is never a position. Figures (bid floors, counts, day windows, percentages) are recorded with page and date **for human readers only**. A skill reads the live figure at run time from the operation or page named in *What cx must read at run time*.

## What this covers

This file covers **what an advertiser can point an Amazon sponsored ad at**, and what Amazon says each kind of target matches. That means:

- keywords in Sponsored Products (SP) and Sponsored Brands (SB): broad, phrase and exact, and exactly how Amazon describes each one's matching of plurals, misspellings, synonyms, word order, acronyms, translations and "close variants";
- negative keyword match types;
- SP automatic targeting: the four targeting groups and what Amazon says automatic targeting reads;
- product targeting in SP, SB and Sponsored Display (SD):
  - single ASIN;
  - category, with its refinements (brand, price, star rating, Prime shipping, age range, genre);
  - expanded ASIN targeting ("similar to");
- theme targeting:
  - SB's "keywords related to your brand" and "keywords related to your landing pages";
  - the v1 `THEME` target type and its match types;
  - SP keyword groups (beta);
- Amazon's recommendation surfaces for keywords, products, categories, brands and keyword groups, and what Amazon says their ranking means;
- SD contextual targeting and audiences: views and purchases remarketing, in-market, lifestyle and interests, and the multi-signal targeting that is replacing standalone contextual targeting on the unified console;
- keyword idea sources:
  - the search term report;
  - the Search Term Impression Share report;
  - Brand Analytics Top Search Terms;
  - Search Query Performance;
  - Product Opportunity Explorer and its Customer Review Insights;
  - third-party estimate and reverse-ASIN tools, as opinion;
- where audience ids for SD audience targets and SP/SB audience boosts are listed;
- language and per-marketplace rules: keyword translation, locales, scripts and global campaigns, and what Amazon says (and does not say) about unspaced Japanese and German compounds;
- minimum and maximum bids per marketplace (recorded here; read live at run time);
- keyword policy: relevance, restricted targets, trademarks in keywords versus trademarks in creative, branded-keyword rules for reserve share of voice;
- what published research says about query-to-product matching at Amazon, about broad match as a mechanism, about whether retargeting is incremental, and about how conversion moves with ad position.

**What this file does not own.** It names these topics and points to their homes:

| Topic | Home |
|---|---|
| How targets are grouped into campaigns and ad groups, and how many match types sit in one ad group | `areas/campaign-structure.md` |
| Reading the search term report for harvesting and negation, and the negative-keyword workflow | `areas/search-terms-and-negatives.md` |
| What to bid on a target once chosen, bid suggestions as a bid, placement adjustments | `areas/bids-and-placements.md` |
| Budget sizing | `areas/budgets-and-pacing.md` |
| Event themes (Prime Day, holiday keyword themes) in their seasonal context | `areas/seasons-and-deals.md` |
| How paid targets relate to organic rank | `areas/ads-organic-and-total.md` |
| Why a target does not serve, as a diagnosis | `areas/diagnosis.md` |
| The first targets of a new ASIN | `areas/launch.md` |
| Which ad products a seller may use at all | `beyond/ad-products-and-eligibility.md` |
| What the metrics on a target mean and how they are attributed | `beyond/metrics-and-attribution.md` |
| What a target is worth | `beyond/goals-and-economics.md` |
| Targeting one's own brand and competitors' brands as a strategy | `beyond/brand-defense-and-competition.md` |
| Amazon's own automation over targets: rules, Ads Agent, target promotion as an automation | `beyond/automation-and-amazon-tools.md` |
| The full API operation list and hosts | `method/ads-api-surface.md` |
| Report types, columns and windows | `method/reporting.md` |
| How a targeting change is measured | `method/change-measurement.md` |

## Amazon's own rules and guidance

Each item is marked:

- RULE: Amazon states it as a requirement, or the API schema enforces it.
- GUIDANCE: Amazon recommends it, describes it loosely, or gives it as an example.

Amazon's targeting text is spread over four places, which do not always agree:

1. The Ads help center (advertising.amazon.com/help). A plain GET of a help page serves the article text in the page's `window.__scV2Content` object, with a `lastModified` stamp.
2. The library guides and blog (advertising.amazon.com/library, /blog, /resources).
3. The Ads API guides, read as markdown on the cloudfront host d3a0d0y2hgofx6.cloudfront.net.
4. The OpenAPI models: SP 3.0, the v1 "Amazon Ads API (all)" merged model, SB v3/v4, and SD v3.

Where they disagree, both texts are quoted and the conflict is carried into *Open questions*. On recency, the help center is the most recently edited of the four: most targeting pages read today carry a `lastModified` in 2026. The library guides carry no date.

### A. The kinds of target, by ad product

- RULE: the v1 API's `TargetType` enum names the kinds of target:
  - `KEYWORD`: "customer search terms";
  - `PRODUCT`;
  - `PRODUCT_CATEGORY`;
  - `PRODUCT_AUDIENCE`: "customers who interacted with a specific product";
  - `AUDIENCE`;
  - `THEME`: "Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products".

  The enum also carries DSP-only kinds. A `TargetCreate` requires `adProduct`, `negative`, `state`, `targetDetails` and `targetType`. `TargetLevel` is `AD_GROUP` or `CAMPAIGN`. [official] OpenAPI model *Amazon Ads API (all), merged*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json
- RULE: "Targeting is assigned at the ad group level and all products in the ad group share the keyword targeting". [official] Ads API guide *Keyword targeting overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/overview.md
- RULE: in the console, an SP campaign is created with **automatic** or **manual** targeting. Manual targeting is either:
  - "Keyword targeting: Choose specific keywords to help your products appear in shopper searches", or
  - "Product targeting: Choose specific products, categories, brands, or other product features to target your ads."

  For automatic: "We'll select the keywords and products to target for you with either automatic targeting option." [official] Help *Create a Sponsored Products campaign* (GKLSYGFS2YD33FER, lastModified 2026-09-28), https://advertising.amazon.com/help/GKLSYGFS2YD33FER
- RULE: "Once the campaign is live, you will not be able to change the campaign targeting". [official] Library guide *A guide to targeting with Sponsored Products*, https://advertising.amazon.com/library/guides/targeting-with-sponsored-products
- RULE: "Once the campaign is created, you won't be able to change the match types you initially selected for your campaign. However, you can add keywords with different match types while your campaign is running." [official] Help *Understand keyword match types* (GHTRFDZRJPW6764R, lastModified 2026-07-29), https://advertising.amazon.com/help/GHTRFDZRJPW6764R
  - [seat] The two rules together say a campaign's targeting *type* (auto versus manual) is fixed, and so is a created keyword's match type. The API carries match type on each keyword target. A keyword in another match type is a new target, and its history starts at zero.
- RULE: SB targets keywords and products: "Select between Keyword and Product to choose how you want to target your ads." [official] Help *Create a Sponsored Brands campaign* (GF86HBCNDJUAC5WN, lastModified 2026-09-30), https://advertising.amazon.com/help/GF86HBCNDJUAC5WN. SB also takes theme targets, launched in the US on 2023-08-17 and worldwide on 2023-12-11 ("Regions: All"). [official] Ads API *Release notes* (cited in item I). The console page above does not mention themes.
- RULE: SD's targeting tactics in the v3 model:
  - `T00020`: contextual (product and category);
  - `T00030`: "Audiences or Contextual Targeting".

  [official] OpenAPI model *Sponsored Display v3* (sd3.yaml, from https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml). Section L carries the detail.
- GUIDANCE: Amazon's strategy names for targeting, in the library guide's own words:
  - **Expand**: "focus on high-traffic category keywords and products";
  - **Promote**: "create a specific campaign to drive sales of products with coupons";
  - **Protect**: "focus on branded keywords and targeting";
  - **Conquest**: "target competitors' products";
  - **Upsell**: "use keywords geared towards higher-priced items, such as larger sizes of the product you're advertising";
  - **Cross-sell**: "target products in adjacent categories".

  The same guide: "avoid mixing different targeting strategies within the same campaign and ad group". [official] *A guide to targeting with Sponsored Products* (as above). How campaigns are cut is `areas/campaign-structure.md`'s.

### B. Sponsored Products keyword match types: what Amazon says each matches

The help page *Understand keyword match types* is the most recently edited statement (lastModified 2026-07-29). Its words are quoted first; the library guides follow, and their conflicts are marked.

- RULE (all match types): "They all account for plurals, misspellings, and translations. If you set multiple match types with different bids for the same keyword, then the match type with the highest bid will be used". [official] Help GHTRFDZRJPW6764R (as above)
- RULE (inferred search term): "When a customer search term is not available, Amazon will infer a search term from the context that best matches your keywords and show your ads in relevant placements." [official] Help GHTRFDZRJPW6764R (as above)
  - [seat] This sentence is how a keyword can serve where there is no typed query: on browse or detail-page context, and off Amazon (see item R). It is also why a search term report can carry rows that no shopper typed.
- RULE (broad): "A shopping query can contain the keyword terms in any order. It may include singulars, plurals, variations, synonyms, and related terms as determined by the meaning of the keyword and the context of the advertised products. The keyword itself may not be contained in the customer shopping query." Amazon's example: the broad keyword "sneakers" "may match customer shopping queries such as "canvas sneakers," "sneakers," "basketball shoes," "athletic shoes," "cleats," "trainers," or "foam runners."" [official] Help GHTRFDZRJPW6764R (as above)
  - [seat] "the context of the advertised products" means broad match reads the ad group's products as well as the keyword. The same broad keyword can therefore match different queries in two ad groups that advertise different products.
- RULE (broad, API): the v1 enum `KeywordMatchType` defines:
  - `BROAD`: "expands matching on user intent beyond PHRASE";
  - `PHRASE`: "expands matching on user intent beyond EXACT".

  [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
- RULE (phrase): "your ad is shown when your keyword phrase or sequence of words, as well as their close variations like misspellings, plural forms, acronyms, translations appear in shopper queries." Example: "a phrase match keyword "curtain rod" can trigger your ad for searches such as "extra long curtain rods" or "curtain rods for bedroom."" [official] Help GHTRFDZRJPW6764R (as above)
- RULE (exact): "your ad is shown when your keyword or sequence of words exactly match shopper queries as well as their close variations like misspellings, plural forms, acronyms, translations." Example: "if your exact match keyword is "outside lights," your ad can still appear when a customer searches for "outdoor lights"". [official] Help GHTRFDZRJPW6764R (as above)
  - [seat] "outside lights" serving "outdoor lights" under exact match is a synonym-grade variant, not a spelling variant. Amazon's own example shows that exact match in SP is not a literal string match.
- GUIDANCE (phrase and exact, older text): the library targeting guide's wording is narrower than the help page's:
  - phrase: "contain all components… in the same order. Phrase match also includes the plural form";
  - exact: "word for word (same words and in the same order)… also includes the plural form".

  [official] *A guide to targeting with Sponsored Products* (as above)
- GUIDANCE (exact, word order, conflicting text): the library guide *What is keyword targeting?* says exact match "white running shoes" matches "extremely close variants like "running shoes white"". The same guide says phrase match "running shoes" does not match "shoes for running". [official] Library guide *What is keyword targeting?*, https://advertising.amazon.com/library/guides/keyword-targeting
  - The first sentence reorders words under exact match. The targeting guide says exact means "same words and in the same order". Amazon's pages disagree on whether exact match tolerates word reordering. See *Open questions*.
- GUIDANCE (case): "Keywords aren't case-sensitive". [official] *A guide to targeting with Sponsored Products* (as above)
- GUIDANCE (start broad): the help page's tip is "Start with a broad match". [official] Help GHTRFDZRJPW6764R (as above)
- GUIDANCE (keyword count): Amazon's figures differ from page to page:
  - "Add at least 25 keywords" [official] Help *Set up keyword targeting* (GK3MNACNTXG659J9), https://advertising.amazon.com/help/GK3MNACNTXG659J9;
  - "25–50 relevant keywords per ad group" [official] *What is keyword targeting?* (as above);
  - "minimum of 25 terms" [official] Blog *3 steps to help start or improve your keyword strategy*, https://advertising.amazon.com/blog/how-to-start-and-improve-your-keyword-strategy.

  These are Amazon guidance figures, for human readers only.
- GUIDANCE (bids by match type): Amazon's pages give opposite advice:
  - The targeting guide advises "setting the highest bid on the exact match, a lower on the phrase match, and the lowest bid on the broad match". It adds that if the same keyword is in several match types "you won't be bidding against yourself". [official] *A guide to targeting with Sponsored Products* (as above)
  - The blog says of broad "you can expect to bid higher" and of exact "You might bid lower". [official] Blog *3 steps to help start or improve your keyword strategy* (as above)

  The bid itself is `areas/bids-and-placements.md`'s. The conflict is recorded in *Open questions*.
- RULE (per-match-type bids): for an individual keyword, the console lets an advertiser "bid only on a specific match type", "bid the same amount for all match types", or "bid different amounts for each match type". [official] Help *Set bids in a Sponsored Products campaign* (GTMXQWASBRZTHLF2, lastModified 2026-10-16), https://advertising.amazon.com/help/GTMXQWASBRZTHLF2
- GUIDANCE (keyword kinds): Amazon's pages name these kinds:
  - the keyword-targeting guide: generic keywords, branded keywords ("brand names, product lines, or trademark terms"), and non-branded keywords [official] *What is keyword targeting?* (as above);
  - the targeting guide: branded keywords and category keywords, which "can be short-tail (i.e., 1-3 words such as "women's running shoes") or long-tail (word combinations, usually three or more words…)". It adds: "Consider bidding on your branded keyword as a brand defense strategy since your competitors may be bidding on your branded keywords, too." [official] *A guide to targeting with Sponsored Products* (as above);
  - complementary keywords: "Include complementary keywords, like "digital camera" for memory cards." [official] Help GK3MNACNTXG659J9 (as above).
- GUIDANCE (organic source): "Go organic. Use keywords that you've added to your product detail page". [official] Blog *3 steps to help start or improve your keyword strategy* (as above)
- GUIDANCE (test length): Amazon's waiting periods:
  - "let your automatic campaign run for about two weeks";
  - test match types for "at least 1-2 weeks" [official] *A guide to targeting with Sponsored Products* (as above);
  - check the Search Term Impression Share report after 2 weeks [official] Help GK3MNACNTXG659J9 (as above).

  These are guidance figures, for human readers only.
- GUIDANCE (Amazon figure): "12 months continuously saw on average 11.2% higher return on ad spend (ROAS), compared to … first month". This is Amazon's own aggregate and is for human readers only. [official] Blog *3 steps to help start or improve your keyword strategy* (as above)

### C. Sponsored Brands keyword matching: semantic matching and the broad match modifier

- RULE: SB keyword matching includes semantic matching. The help page *Understand targeting* carries a table of what each SB match type matches "generally" and what it matches by "semantic match". [official] Help *Understand targeting* (G3XAU5G7C2JTNQTM, lastModified 2026-07-29), https://advertising.amazon.com/help/G3XAU5G7C2JTNQTM
- RULE: "In Sponsored Brands campaigns, phrase match also allows your ad to show on searches that have similar meaning…". Amazon's example: phrase "curtain rods" can match "pole for curtains for bedroom". [official] Help *Set up keyword targeting* (GK3MNACNTXG659J9, as above)
- GUIDANCE: an SB example of semantic matching is "running shoes" matching "jogging shoes". [official] *What is keyword targeting?* (as above)
- RULE (broad match modifier, SB): "In Sponsored Brands, you can add broad match modifiers to indicate words that must appear in the customers' shopping queries for your ad." With "+kids shoes", "the ad will match only the searches that contain the word "kids."" It "may match to "kids sneakers" or "running shoes for kids"" but not to "sneakers" or "running shoes". [official] Help GHTRFDZRJPW6764R (as above). The help page places the modifier under the heading "Broad match modifiers (Sponsored Brands)" and says nothing of it for SP. The impressions-troubleshooting page: "You can also use broad match modifiers to expand your campaign match terms. This isn't applicable to Sponsored Display ads." [official] Help *Troubleshoot your campaign for impressions* (G8WCYU3FQKFVSMR4, lastModified 2026-07-16), https://advertising.amazon.com/help/G8WCYU3FQKFVSMR4
- RULE (SB API): `MatchType` takes `broad`, `exact` or `phrase`. `NegativeMatchType` takes `negativeExact` or `negativePhrase` only: SB has no negative broad. Keyword text has a maximum of 10 words. Negative text has a maximum of 10 words for `negativeExact` and 4 for `negativePhrase`. [official] OpenAPI model *Sponsored Brands v3*, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml

### D. Keyword text: characters, length, scripts

- RULE: the API limits page sets these rules for keyword text:
  - no leading or trailing spaces;
  - a period only inside a keyword;
  - `-` and `+` only inside a keyword, with no spaces around them;
  - `"` must be paired;
  - a maximum of 80 characters;
  - a maximum of 10 words ("parts") for a positive keyword;
  - a maximum of 4 parts for a negative keyword, but 10 for negative exact;
  - the reserved phrase "Automatically Selected Keywords" is not accepted.

  The valid symbols are `-`, `&`, `+`, `[`, `]`, tab, newline, carriage return, `'` and `"`. `%` is valid only in AE, SA and EG. Arabic script is valid only in AE, SA and EG. Devanagari and Tamil are valid everywhere except AE, SA and EG. [official] Ads API *Limits*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md (web: https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits)
- GUIDANCE (conflicting text): the library guide says keywords have a "maximum limit of 10 words per keyword and 80 characters". It also says special characters "question mark, slash, double quote, ampersand or backlash are not permitted". The API limits page lists `&` and `"` as valid. [official] *A guide to targeting with Sponsored Products* (as above). The API page is the one the endpoint enforces. See *Open questions*.
- RULE: the negative limits in the help center agree with the API: "Negative phrase: 4 words or 80 characters"; "Negative exact: 10 words or 80 characters". [official] Help *Sponsored ads campaign limits* (G86H2227323T8T4Q, lastModified 2026-07-29), https://advertising.amazon.com/help/G86H2227323T8T4Q; Help GHTRFDZRJPW6764R (as above)
- RULE: an ASIN as a search term in a report is "always 10 characters". [official] *A guide to targeting with Sponsored Products* (as above). The same guide says this is how a product-page match shows in the search term column.

### E. Negative keywords

- RULE (SP API): SP negatives are created as `NEGATIVE_EXACT`, `NEGATIVE_PHRASE` or `NEGATIVE_BROAD`, through the `SponsoredProductsCreateOrUpdateNegativeMatchType` enum. They are created at the ad-group level (`/sp/negativeKeywords`) or the campaign level (`/sp/campaignNegativeKeywords`), and campaign-level negatives use the same enum. [official] OpenAPI model *Sponsored Products 3.0*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json
- RULE (what a negative blocks): "Negative phrase: Ads don't show on shopping queries that contain the complete phrase or close variations." "Negative exact: Ads don't show on shopping queries that contain the exact phrase or close variation." [official] Help GHTRFDZRJPW6764R (as above)
  - [seat] Negatives, like positives, are said to cover "close variations". A negative exact keyword therefore blocks more than one literal string, and what it blocks is Amazon's call, not the advertiser's.
- RULE (console, help): "Negative keywords can be used with phrase and exact match types". "You can't change the match type of an existing negative keyword". [official] Help *Add negative keywords or negative products targeting* (GTEHPEG5BXY9UX5W), https://advertising.amazon.com/help/GTEHPEG5BXY9UX5W
- GUIDANCE (conflicting text): the keyword-targeting library guide describes negatives "with options for exact, phrase, or broad match types". [official] *What is keyword targeting?* (as above). The help center says phrase and exact; the SP model carries an enum value for negative broad. Whether a negative broad keyword can be created for a seller's SP campaign today is unconfirmed without a live write. See *Open questions*.
- RULE (v1): a negative keyword in the v1 API is a target with `negative: true`, `targetType: KEYWORD` and a `keywordTarget`; `targetLevel` reads `CAMPAIGN` or `AD_GROUP`. The guide's examples all use `matchType: EXACT`, and the guide does not say which match types a negative accepts. The v1 `KeywordMatchType` enum the field points to carries `BROAD`, `EXACT` and `PHRASE`. [official] Ads API guide *Negative keyword targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/keywords.md; OpenAPI model *Amazon Ads API (all), merged* (as above)
- RULE (effect delay): "Negative keywords: 72 hours; Negative products/ASINs: 96 hours". [official] Help GTEHPEG5BXY9UX5W (as above). These are figures for human readers only; `method/change-measurement.md` owns how a change's window is set.
- GUIDANCE: "We recommend using phrase or exact match with negative keywords". Negate low performers after "at least 20 clicks" over "two weeks or more". [official] *A guide to targeting with Sponsored Products* (as above). These are guidance figures for human readers only; the workflow is `areas/search-terms-and-negatives.md`'s.
- RULE (limits): campaign negative keywords: 10,000. Ad group negative keywords: 10,000. Keywords in an account, including negatives: 2,000,000. [official] Help G86H2227323T8T4Q (as above). These are figures for human readers only; the help page adds that "Amazon now increases customer limits as they approach a limit".

### F. Automatic targeting: the four groups and what auto targeting reads

- RULE: "Automatic targeting is available only for Sponsored Products." An advertiser can "increase your bid for a single strategy, or turn on or off a strategy all together." "In Sponsored Products automatic targeting campaigns, you'll use targeting groups instead of match types". [official] Help GHTRFDZRJPW6764R (as above)
- RULE (the four groups), in the help page's words, with its "Doppler 400-count Cotton Sheets" example:
  - **Close match**: "We'll show your ad to customers who use search terms closely related to your products". Examples: "cotton sheets", "400-count sheets", "soft cotton sheets", "400TC bedsheets", "100% cotton sheets 400 thread count".
  - **Loose match**: "customers who use search terms loosely related to your products". Examples: "bed sheets", "bath sheets", "bath towels".
  - **Substitutes**: "customers who view detail pages of products similar to yours". Examples: "300-count Cotton sheets", "queen 400-count Sheets".
  - **Complements**: "customers who view the detail pages of products that complement your product". Examples: "queen quilt", "feather pillows".

  [official] Help GHTRFDZRJPW6764R (as above). (Help *Understand targeting*, G3XAU5G7C2JTNQTM, describes automatic versus manual targeting but does not list the four groups.)
  - [seat] By the help page's definitions, Close and Loose are query (search) targets, and Substitutes and Complements are detail-page (product) targets. That split is the difference between keyword-like and product-like reach inside one auto ad group.
- RULE (API names): in SP 3.0 the four groups are targeting predicates:
  - `QUERY_HIGH_REL_MATCHES` = Close match;
  - `QUERY_BROAD_REL_MATCHES` = Loose match;
  - `ASIN_SUBSTITUTE_RELATED` = Substitutes;
  - `ASIN_ACCESSORY_RELATED` = Complements.

  All four "cannot be manually created": they exist only in an auto ad group. [official] OpenAPI model *Sponsored Products 3.0* (as above). In v1 they are `THEME` targets, with `ThemeMatchType` values `KEYWORDS_CLOSE_MATCH`, `KEYWORDS_LOOSE_MATCH`, `PRODUCT_SUBSTITUTES` and `PRODUCT_COMPLEMENTS`. [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
- RULE (creation): "four auto targeting expressions are automatically created" when an auto ad group is made. A bid set on an expression replaces the ad group's default bid for that expression. [official] Ads API guide *Auto targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/auto-targeting.md. In the console: "Choose to set 1 default bid, or unique bids for each targeting group". [official] Help GTMXQWASBRZTHLF2 (as above)
- GUIDANCE (what auto reads, library text): "The system analyzes your product details, including titles and descriptions, to help display your ads for relevant shopping queries." [official] *What is keyword targeting?* (as above). This is an undated library guide's description, not a rule the API enforces.
- GUIDANCE (what auto reads, other texts):
  - Auto targeting works "based on previous shopping queries and your product information" [official] *A guide to targeting with Sponsored Products* (as above);
  - "Amazon chooses products and keywords for you based on similar products and ads" [official] Help G3XAU5G7C2JTNQTM (as above).

  No Amazon page read today names bullets, backend search terms or A+ content as inputs to auto targeting. The prior paid-keywords research (read 2026-10-14) said Amazon names no listing field. That is now corrected: Amazon names titles and descriptions.
- GUIDANCE (example error on Amazon's page): the targeting guide's examples for an espresso maker list "ground coffee" and "espresso mugs" under **Substitutes**, and "queen comforter" and "feather pillows" under **Complements**. These do not fit Amazon's own definitions of those groups. [official] *A guide to targeting with Sponsored Products* (as above). [seat] The page's examples are unreliable; the help center's definitions are the ones to read.
- GUIDANCE (start auto): "If you are new … we recommend starting with an auto campaign". [official] Ads API guide *Get started with automatic campaigns*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/auto-campaigns.md. In v1 an auto campaign is made with `autoCreateTargets` set to `true` in the campaign's `autoCreationSettings` (same guide).
- RULE (auto to manual): the Target Promotion API (`/sp/targetPromotionGroups`, with `/list`, `/recommendations` and `/targets`) promotes well-performing auto-campaign search terms and ASINs into manual keyword and product targets. Its recommendations are "based on performance heuristics". [official] OpenAPI model *Sponsored Products 3.0* (as above); Ads API guide *Target promotion*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/target-promotion.md; release note 2023-10-23, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md. As an automation, this is `beyond/automation-and-amazon-tools.md`'s.
- RULE (negatives in auto): "Negative product targets created at the ad group level affect product attribute targets or automatic targets configured in the same ad group." [official] Help GTEHPEG5BXY9UX5W (as above). Negative keywords on auto campaigns: "You can add negative keywords to Sponsored Products automatic, product, and keyword targeting, and to Sponsored Brands keyword targeting campaigns." [official] *What is keyword targeting?* (as above). The 2025-05-22 US release note says negatives "can now be saved on campaigns and ad group regardless of targeting type" (item H).

### G. Product targeting: single ASIN, category with refinements, expanded

- RULE (what product targeting is): "Product targeting allows you to choose specific products, categories, brands, or other product features that are relevant to the product in your ad. You can target categories and products individually or target a combination of categories and brands in the same campaign." [official] Help *Set up product targeting* (GB2JECV9CJK6R6AL), https://advertising.amazon.com/help/GB2JECV9CJK6R6AL
- GUIDANCE (when): Amazon's two named uses:
  - "You're looking for broad reach (rather than targeting specific keywords)";
  - "You're launching a campaign in a foreign marketplace and don't want to rely on translations to do keyword research."

  [official] Help GB2JECV9CJK6R6AL (as above); Help G3XAU5G7C2JTNQTM (as above)
- RULE (where a product target serves): a product target appears on "its product detail page, as well as search result pages where the targeted product appears among the top search results". [official] *A guide to targeting with Sponsored Products* (as above)
  - [seat] Product targets therefore also buy some search-results inventory. The Perpetua placement shares in *What practitioners add* put the top-of-search share at 2–7% for one seller's product targets.
- RULE (one ASIN per clause): "You can only add one `ASIN` per targeting clause. If you want to target multiple `ASIN`s, you should create two targeting clauses." [official] Ads API guide *Sponsored Products product targeting overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/overview.md
- RULE (exact versus similar): "When you target individual products, you can choose to target a specific `ASIN` exactly, or target a specific `ASIN` and other similar `ASIN`s, including substitutes, complements, and other related products." The v1 examples use `matchType: PRODUCT_EXACT` and `PRODUCT_SIMILAR` under `targetType: PRODUCT`. [official] Ads API guide *Sponsored Products product targeting overview* (as above). The v1 `ProductMatchType` enum is `PRODUCT_COMPLEMENTS`, `PRODUCT_EXACT`, `PRODUCT_REMARKETING` and `PRODUCT_SIMILAR`. [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
- RULE (expanded product targeting), in the help page's words:
  - "It is the default setting for campaigns. The Expanded box next to the targeted product will be automatically selected during campaign set-up."
  - It works by "Choosing closely related products based on past interactions and views".
  - It works by "Only expanding each product to a limited number of additional products with the highest performance potential".
  - It works by "Automatically updating the underlying products targeted daily".
  - Expanded targets "appear in available reports with a "Product-expanded" prefix in the targeting column".
  - "you can use negative targeting to exclude individual products or brands from the expanded list."

  [official] Help GB2JECV9CJK6R6AL (as above)
- RULE (expanded, the launch note and the model): Amazon's launch note says the expanded products "are updated dynamically and are chosen to provide performance similar to the individual product target". [official] What's new *Sponsored Products launches expanded product targeting* (dated 2022-10-26), https://advertising.amazon.com/resources/whats-new/expanded-product-targeting-sponsored-products. The SP 3.0 predicate `ASIN_EXPANDED_FROM` reads "Target products similar in performance to the ASIN expressed". [official] OpenAPI model *Sponsored Products 3.0* (as above). Bulksheets take `asin-expanded="<ASIN>"` (release note 2022-10-01). [official] Ads API *Release notes*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md
  - [seat] Because expanded is the console default, an ASIN target that a seller created in the console is likely an expanded one unless the box was cleared. Reading the target's expression (`ASIN_SAME_AS` versus `ASIN_EXPANDED_FROM`, or `PRODUCT_EXACT` versus `PRODUCT_SIMILAR`) is the only way to know.
- RULE (category and refinements): "Categories: you can target suggested categories that are based on relevance to your product. You can refine categories by brand, price range, and review star ratings." "Sponsored Products and Display: you can also refine categories by Prime shipping eligibility. In addition, in the Toys & Games category, you can refine by the product's age range. For the Books and eBooks, you can refine by genre." [official] Help GB2JECV9CJK6R6AL (as above)
- RULE (category first): "When using refinements, you must first define the category." [official] Ads API guide *Sponsored Products product targeting overview* (as above). The guide's v1 examples show `targetType: "PRODUCT"` for a bare category (`productCategoryId` only) and `targetType: "PRODUCT_CATEGORY"` for a category with refinements (`productBrandId` plus `productCategoryId`).
  - [seat] Both shapes appear in Amazon's own examples, so a category target can come back under either target type.
- RULE (SP 3.0 predicates): an SP product or category expression is built from these predicates:
  - `ASIN_SAME_AS`;
  - `ASIN_CATEGORY_SAME_AS`;
  - `ASIN_BRAND_SAME_AS`;
  - `ASIN_PRICE_LESS_THAN`, `ASIN_PRICE_BETWEEN`, `ASIN_PRICE_GREATER_THAN`;
  - `ASIN_REVIEW_RATING_LESS_THAN`, `ASIN_REVIEW_RATING_BETWEEN`, `ASIN_REVIEW_RATING_GREATER_THAN`;
  - `ASIN_IS_PRIME_SHIPPING_ELIGIBLE` ("category or brand level only");
  - `ASIN_AGE_RANGE_SAME_AS` (toys and games);
  - `ASIN_GENRE_SAME_AS` (books and eBooks);
  - `ASIN_EXPANDED_FROM`;
  - `KEYWORD_GROUP_SAME_AS` ("Beta coming soon").

  [official] OpenAPI model *Sponsored Products 3.0* (as above)
- RULE (v1 refinement fields): the v1 `ProductCategoryRefinement` fields are:
  - `productCategoryId`;
  - `productBrandId`;
  - `productPriceGreaterThan`, `productPriceLessThan`;
  - `productRatingGreaterThan`, `productRatingLessThan`;
  - `productPrimeShippingEligible`;
  - `productAgeRangeId`;
  - `productGenreId`.

  The four id fields (category, brand, age range, genre) each have a `…Resolved` read-back field; the price, rating and Prime fields do not. `ProductCategoryMatchType` has one value, `MULTISIGNAL_BROAD`: "This expands matching on user intent beyond BROAD by taking multiple behavioral and contextual signals." `ProductIdType` is `ASIN`, `SKU` or `RETAILER_OFFER`. [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
- RULE (category tree and counts):
  - `GET /sp/targets/categories` returns "a tree of all categories currently available on Amazon.com".
  - `POST /sp/targets/categories/recommendations` returns categories for a list of ASINs, "as well as the minimum and maximum number of products in that category". "Note that all inputted `ASIN`s should be similar, as the recommendations are for **all** `ASIN`s in the request."
  - `GET /sp/targets/category/{categoryId}/refinements` returns brands, age ranges and genres.
  - `POST /sp/targets/products/count` returns how many products a category expression would reach.

  [official] Ads API guide *Sponsored Products product category targeting suggestions and refinements*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/category-suggestions-refinements.md; OpenAPI model *Sponsored Products 3.0* (as above)
  - [seat] "currently available on Amazon.com" is the guide's wording. Whether the tree is per marketplace when called on an EU or FE profile is not stated on the pages read. The operation's own description says only "Returns all targetable categories… a tree of category nodes".
- RULE (limit): "Category and product targets in an ad group: 10,000"; "Keywords in an ad group (excluding negative keywords): 1,000 for manual targeting". [official] Help G86H2227323T8T4Q (as above). For human readers only.
- GUIDANCE (what to target), from Amazon's guides:
  - "Target your own product pages to showcase your product range" [official] Library guide *Best practices for your Sponsored Products ads*, https://advertising.amazon.com/library/guides/sponsored-products-best-practices;
  - for consideration, "focus more on ASIN targeting for items with high star ratings" [official] *A guide to targeting with Sponsored Products* (as above);
  - "Only include ASINs from the same category in one campaign" [official] *Best practices for your Sponsored Products ads* (as above).
- GUIDANCE (impressions): "If a campaign targeting products or product categories isn't delivering impressions, this could be related to low traffic for the category or product targets, or that these targets aren't showing up in organic search results. In this case, you can expand targeting to similar popular products or categories that show up on search results, or get more traffic in their corresponding detail pages." [official] Help G8WCYU3FQKFVSMR4 (as above). The diagnosis is `areas/diagnosis.md`'s.
- RULE (a placement change Amazon announced): "Starting July 1, 2026, recommendations on US mobile product detail pages in the fashion and apparel categories have been organized into clearer sections for similar and complementary products. As a result, Sponsored Products ads now appear in fewer but more relevant placements, and your total impressions may be lower than in previous periods." [official] Help G8WCYU3FQKFVSMR4 (as above)
  - [seat] This bears on product targets and the Substitutes and Complements auto groups in US fashion: an impression drop from July 2026 there has a named Amazon cause.

### H. Negative product and brand targeting

- RULE (what it blocks): "To keep your Sponsored Products ads off specific product detail pages, whether your own or a competitor, use negative product targeting." The help page explains: "These product targets prevent your product targeted or automatically targeted ads from displaying when the ASIN of a product page matches the negative product target. Negative product targets created at the ad group level affect product attribute targets or automatic targets configured in the same ad group. Negative product targets created at the campaign level affect product attribute targets or automatic targets in any ad group within the campaign." Brands are excluded under "Exclude brands", ASINs under "Exclude products". [official] Help GTEHPEG5BXY9UX5W (lastModified 2026-10-20, as above)
- RULE (predicates): SP negative targeting expressions use `ASIN_SAME_AS` and `ASIN_BRAND_SAME_AS` only. [official] OpenAPI model *Sponsored Products 3.0* (as above). In v1, a brand negative is a `productCategoryTarget` with `productBrandId` (the guide's example is at the campaign level). [official] Ads API guide *Sponsored Products negative product and brand targeting overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/product-brand.md
- RULE (brand search and recommendations):
  - `GET /sp/negativeTargets/brands/recommendations` recommends brands to negate. Its description: "These recommendations include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands".
  - `/sp/negativeTargets/brands/search` finds brand ids (up to 100 brands).

  [official] OpenAPI model *Sponsored Products 3.0* (as above)
  - [seat] The sentence describes Amazon's recommender, not a finding about every seller. It is Amazon's stated reason the list contains the seller's own brand. Own-brand defence is `beyond/brand-defense-and-competition.md`'s.
- RULE (which campaigns, conflicting texts):
  - The API guide: "Both auto and manual Sponsored Products campaigns can use negative product targeting." It also carries a warning: "Campaign-level negative product targeting for manual campaigns is only available for vendors. Sellers can add campaign-level negative targeting to auto campaigns, but not manual." [official] Ads API guide *Sponsored Products negative product and brand targeting overview* (as above)
  - The release note of 2025-05-22, "Negative targets can now be saved on campaigns and ad group regardless of targeting type in US marketplace": "Now you can negatively target a keyword, `ASIN`, or brand during campaign creation or on any existing campaign or ad group." It continues: "Negatively targeting a keyword prevents your ad from showing on search results pages for that keyword, while `ASIN` and brand negative targeting prevents your ad from showing on the product detail page for that `ASIN` or `ASIN`s with that brand." The API line: "Now you can succeed saving negative keywords, products, and brands on campaigns and ad groups regardless of targeting type." [official] Ads API *Release notes* (as above)
  - The release note is later than the guide's warning and names the US marketplace only. Whether the vendor-only warning still holds for sellers outside the US is open. See *Open questions*.
- RULE (delay): "Negative products/ASINs: 96 hours". [official] Help GTEHPEG5BXY9UX5W (as above). For human readers only.
- RULE (limit): "Negative products in an ad group (product targeting): 10,000". [official] Help G86H2227323T8T4Q (as above). For human readers only.

### I. Theme targeting: SB themes, v1 themes, SP keyword groups

**Sponsored Brands theme targeting**

- RULE: SB theme targets come in two types:
  - `KEYWORDS_RELATED_TO_YOUR_BRAND`;
  - `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES`.

  The model adds: "Note: Additional theme types may be added in the future." The create call "supports a maximum list size of 100 theme targets and only one target can be created for each themeType per adGroup." Themes are created with `POST /sb/themes`. [official] OpenAPI model *Sponsored Brands v3* (as above)
- RULE (default on goal-based SB campaigns): "`TARGETING` - Theme targeting is automatically created when creating an ad group." "If no goal is present in request, `MANUAL` is set by default. If a goal is present, `TARGETING` is set by default." "Once a goal-based campaign is created, the `goal`, `costType`, and `smartDefault` values are not editable." [official] Ads API guide *Get started with Sponsored Brands campaigns*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns.md
- RULE (what themes read): theme targeting launched for SB in the US on 2023-08-17 using "advanced machine learning algorithms that take into account historical performance targets and brand interactions". It went worldwide from 2023-12-11. The SB v3-to-v4 migration note of 2025-04-17 says: "the theme targeting feature automatically generates and categorizes keywords based on historical performance and brand interactions, offering two pre-configured targeting groups (keywords related to landing pages and brand)". [official] Ads API *Release notes* (as above)
- RULE (goals): SB goals in the API are:
  - `BRAND_IMPRESSION_SHARE`: "This goal will show your ads to shoppers searching for your brand";
  - `PAGE_VISIT`: "drives traffic to your landing and detail pages through all placements".

  [official] Ads API guide *Get started with Sponsored Brands campaigns* (as above). The SB v4 model also lists `ACQUIRE_NEW_CUSTOMERS` and `AD_VIEWS`, each marked "This property is a PREVIEW ONLY and cannot be used as part of a request or response". The same model: "Goal-based campaigns are not supported in the Ireland (IE) marketplace." [official] OpenAPI model *Sponsored Brands v4* (from https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json)
- RULE (target groups in the console): "You can either target individual keywords or create target groups, which consists of a set of keywords. We recommend you use targeting groups to start a campaign quickly." Bid recommendations for goals "are built from historical winning bids for each specific target (keyword or product) and the impression opportunity for each specific goal." [official] Help *Campaign goals for Sponsored Brands* (GXXPFXLSVX9VD3U9, lastModified 2026-08-11), https://advertising.amazon.com/help/GXXPFXLSVX9VD3U9

**v1 `THEME` targets (all ad products)**

- RULE: the v1 `ThemeMatchType` enum lists these values:
  - `KEYWORDS_CLOSE_MATCH`, `KEYWORDS_LOOSE_MATCH`;
  - `PRODUCT_SUBSTITUTES`, `PRODUCT_COMPLEMENTS`;
  - `PRODUCTS_SIMILAR_TO_ADVERTISED_PRODUCTS`;
  - `KEYWORDS_RELATED_TO_YOUR_BRAND`, `KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES`;
  - `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY`;
  - `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` ("peer brands are selected automatically");
  - `KEYWORDS_RELATED_TO_GIFTS`;
  - `KEYWORDS_RELATED_TO_PRIME_DAY` ("will only match queries through the end of Prime Day");
  - `INTERESTED_AUDIENCE`.

  [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
  - [seat] The model lists these values but does not say which ad product accepts which in which marketplace. No guide read today documents the category, peer-brand, gift or Prime Day themes. Their availability is a run-time read (create returns a per-item error), not a fact here. Seasonal themes are `areas/seasons-and-deals.md`'s.

**SP keyword groups (beta)**

- RULE: "Keyword Groups targeting automatically identifies and targets highly relevant keyword targets for ads. Keyword Groups targeting is based on specified product `ASIN`s and continuously refreshes them over time to maximize ad performance." "Keyword Groups is currently in beta and only available for US marketplace." "You can adopt both keyword and Keyword Groups targets for a given ad group. However, you cannot mix keyword group targets with product targets." Recommendations come from `POST /sp/targeting/recommendations/keywordGroups` with a list of ASINs (and an optional `locale`). The sample response is a group with id "branded" and text "Keywords related to your brand", with sample keywords. [official] Ads API guide *Sponsored Product keyword groups targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keyword-group-targeting.md
- RULE: in the SP model:
  - a `KeywordGroup` is described with the example "the keyword group "gift" can target relevant search queries containing the word gift";
  - its fields are `id`, `text`, `description`, `impactSummary` and `sampleKeywords` (max 10);
  - the request takes up to 1,000 ASINs and a `countryCode`;
  - the content type is `application/vnd.spkeywordgroupsrecommendations.v1.0+json`;
  - the create predicate `KEYWORD_GROUP_SAME_AS` is marked "Beta coming soon".

  [official] OpenAPI model *Sponsored Products 3.0* (as above)
- RULE: the beta launched on 2024-04-23 in the US. "Once a Keyword Group specification is created, the performance of Keyword Groups will be available in the search terms report. Keyword Groups improves campaign performance by dynamically updating the keywords within a group through the campaign lifecycle and eliminates the need for advertisers to constantly curate new keywords." [official] Ads API *Release notes* (as above). The words "improves campaign performance" are Amazon's own claim, not a measured effect published with data.
- RULE (bids on groups): theme-based bid recommendations v4 accept `KEYWORD_GROUP` targets (US only). `MultiCountryTargetingExpressionType` includes `KEYWORD_GROUP`. [official] OpenAPI model *Sponsored Products 3.0* (as above)

### J. Amazon's recommendation surfaces, and what their ranking means

**SP keyword recommendations (`POST /sp/targets/keywords/recommendations`, `getRankedKeywordRecommendation`)**

- RULE (request): the request can take two forms:
  - `recommendationType` `KEYWORDS_FOR_ASINS`, with up to 50 ASINs, for keywords before an ad group exists;
  - `KEYWORDS_FOR_ADGROUP`, with a campaign and ad group id, "to retrieve recommended keyword targets for an existing ad group".

  Further parameters:
  - `maxRecommendations` defaults to 200, with a maximum of 200. "Set it to 0 if you only want to rank user-defined keywords."
  - `targets` takes up to 100 of the advertiser's own keywords, "to be ranked alongside the keyword recommendations".
  - `biddingStrategy` takes `AUTO_FOR_SALES`, `LEGACY_FOR_SALES` (default), `MANUAL` or `RULE_BASED`: "The bid recommendations returned will depend on the bidding strategy."
  - `locale` takes one of 21 values.

  Content types v3, v4 and v5 exist; the guide says "If you have currently integrated with either version 3 or version 4, integrate with version 5 as soon as possible." v5 adds bid themes `CONVERSION_OPPORTUNITIES` ("The default theme which aims to maximize number of conversions") and `SPECIAL_DAYS` ("A theme available during high sales events such as Prime Day, to anticipate an increase in sales and competition"), with impact metrics that "are based on historic performance of similar products to provide guidance on choosing a bid, and are not estimates of expected performance". [official] OpenAPI model *Sponsored Products 3.0* (as above); Ads API guide *Sponsored Products keyword recommendations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/suggestions.md
- RULE (ranking): the model's text conflicts with itself:
  - The operation description: "The keyword recommendations will be ranked in descending order of clicks or impressions, depending on the **sortDimension** field provided by the user."
  - The field itself: "`sortDimension`: The ranking metric value. Supported values: CLICKS, CONVERSIONS, DEFAULT. DEFAULT will be applied if no value passed in."

  - The v4 section of the same operation text: "The default sort dimension, if not specified, ranks recommendations by our interal [sic] ranking mechanism." The guide calls it "the default ranking heuristic".

  The enum has no `IMPRESSIONS`. [official] OpenAPI model *Sponsored Products 3.0* (as above); Ads API guide *Sponsored Products keyword recommendations* (as above)
  - [seat] A keyword's `rank` in the response is an order by a metric Amazon names (clicks or conversions) or by an unnamed default. It is not a relevance score, a search volume or a forecast for the advertiser's product. The response carries no volume figure. See *Open questions* for "impressions" versus "conversions".
- RULE (response): each recommendation carries:
  - `keyword`;
  - `bidInfo`: in the v3/v4 shape (`KeywordBidInfo`), up to three entries, one per match type, each with `matchType`, `rank`, `bid`, and `suggestedBid` {`rangeStart`, `suggested`, `rangeEnd`, `bidRecId`}; in the v5 shape (`ThemedBid`), up to 15 entries;
  - `recId`;
  - `userSelectedKeyword`;
  - `translation`;
  - `searchTermImpressionShare` and `searchTermImpressionRank`.

  `searchTermImpressionShare` is "The account-level ad-attributed impression share for the search-term/keyword. Provides percentage share of all ad impressions the advertiser has for the keyword in the last 30 days." `searchTermImpressionRank` "Provides [1:N] place the advertiser ranks among all advertisers for the keyword by ad impressions in a marketplace in the last 30 days." Both: "This information is only available for keywords the advertiser targeted with ad impressions." [official] OpenAPI model *Sponsored Products 3.0* (as above)
- RULE (currency units, conflicting text):
  - `KeywordBidInfo.bid` is "in minor currency units (example: cents). The default value will be the suggested bid." Its `matchType` default is "BROAD".
  - `BidSuggestion` is "Suggested bid range in major and minor currency units (example: dollars and cents)".

  [official] OpenAPI model *Sponsored Products 3.0* (as above). See *Open questions*. The bid side is `areas/bids-and-placements.md`'s.
- RULE (translation): "Translations are for readability and do not affect the targeting of ads." [official] OpenAPI model *Sponsored Products 3.0* (as above)
- GUIDANCE (what the recommender reads): "we assess which keywords performed well for you in the past, as well as those which performed well across Amazon more broadly… what customers are searching for on Amazon, and how often these searches translate into sales". [official] *A guide to targeting with Sponsored Products* (as above)
- RULE (deprecation): the v2 suggested-keyword endpoints were deprecated on 2026-01-27 and "will be shutoff on June 2026". They are:
  - `/v2/asins/{asin}/suggested/keywords`;
  - `/v2/adGroups/{adGroupId}/suggested/keywords/extended`;
  - `/v2/adGroups/{adGroupId}/suggested/keywords`;
  - `/v2/asins/suggested/keywords`.

  "Please use the /sp/targets/keywords/recommendations API instead." [official] Ads API *Release notes* (as above)
- RULE (multi-country): `POST /sp/global/targets/keywords/recommendations/list` returns keyword recommendations for several countries at once. The v5 content type lists the 21 marketplaces where v5 is available. [official] OpenAPI model *Sponsored Products 3.0* (as above)

**SP product, category and brand recommendations**

- RULE (product recommendations, `POST /sp/targets/products/recommendations`): "Given an advertised ASIN as input, this API returns suggested ASINs to target in a product targeting campaign. We use various methods to generate these suggestions. These include using historical performance of your ad, items that shoppers they frequently view and purchase together, etc." Results come either as a list of ASINs, or grouped by theme, "an accompanying context for why we recommend the items". The themes are:
  - "Top converting targets": "These ASINs generated conversions for the input ASIN in the past 30 days… The suggested ASINs under this theme are sorted in decreasing order of sales generated for your promoted item";
  - "Similar items (frequently viewed together)": "Items that shoppers frequently view and click along with your advertised item during a shopping session";
  - "Complements": "Items that are frequently purchased together as complements. For example, if you are promoting a tennis racquet, you may see tennis balls recommended under this theme";
  - "Similar items with low ratings and reviews": "Subset of the 'similar items' theme containing items that are rated lower than 3 stars and/or with fewer than 5 reviews";
  - "Other books read by your readers".

  "Availability of themes differs by input ASIN". The themes format returns a default of 5 and a maximum of 10. The ASINs format returns a default of 100 and a maximum of 1,000 per page, with cursors. [official] OpenAPI model *Sponsored Products 3.0* (as above)
- GUIDANCE: "If you are including multiple `ASIN`s in the request, make sure they are similar products. The response includes suggested products for **all** `ASIN`s included in the request." [official] Ads API guide *Sponsored Products product targeting recommendations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/suggestions.md
  - [seat] Only one theme states an order ("decreasing order of sales generated for your promoted item"). That order uses the advertiser's own past ad data. The other themes are retail co-view and co-purchase sets with no stated ordering.
- RULE (category recommendations): see item G. Categories come with min and max product counts. The help page says suggested categories are "based on relevance to your product". [official] Help GB2JECV9CJK6R6AL (as above)
- RULE (brand negatives recommendations): see item H.

**Theme-based bid recommendations**

- RULE: `POST /sp/targets/bid/recommendations` "supports keyword, auto and product targets". "The API will return a 422 response when an unsupported marketplace or target is provided." v4 "allows users to get theme-based bid recommendations for product targeting expressions, including PAT_ASIN, PAT_CATEGORY and PAT_CATEGORY_REFINEMENT" and "supports keyword, auto and product targets in all marketplaces". v5 adds estimated impressions for the suggested bid and for "a range of bids (8 bids)". "New features are currently available only for existing ad group requests in US marketplace." [official] OpenAPI model *Sponsored Products 3.0* (as above). The bid is `areas/bids-and-placements.md`'s; it is named here because the endpoint is also a check on whether a target is supported in a marketplace.

**SB recommendations**

- RULE (keywords): `POST /sb/recommendations/keyword` "Gets an array of keyword recommendation objects for a set of ASINs included either on a landing page or a Stores page. Vendors may also specify a custom landing page." Each suggestion carries:
  - `value`, `matchType`, `type`, `translation` and `recommendationId`;
  - `searchTermImpressionShare`: "Provides percentage share of all ad impressions the advertiser has for the keyword in the last 7 days";
  - `searchTermImpressionRank`.

  [official] OpenAPI model *Sponsored Brands v3* (as above). The release note of 2023-05-25: "Search term impression share and rank are only available if your account has generated impressions for search terms matching the recommended keywords." [official] Ads API *Release notes* (as above)
- RULE (products, categories, brands):
  - `POST /sb/recommendations/targets/product/list`: "Recommendations are based on the ASINs that are passed in the request";
  - `/sb/recommendations/targets/category`;
  - `/sb/recommendations/targets/brand`;
  - `/sb/targets/categories` and `/sb/targets/products/count` in SB v4;
  - `/sb/negativeTargets/brands/recommendations` in SB v4.

  [official] OpenAPI models *Sponsored Brands v3* and *v4* (as above)
- RULE (which SB spec carries which targeting path; re-read 2026-11-09 to settle a disagreement between files). Amazon publishes three SB models, and they carry different path sets:
  - The cloudfront YAML *Amazon Ads API - Sponsored Brands*, `version: "3.0"` (https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml), 26 paths. It carries the keyword and target entities: `/sb/keywords`, `/sb/negativeKeywords` (tag "Negative keywords"), `/sb/targets`, `/sb/targets/list`, `/sb/negativeTargets`, `/sb/negativeTargets/list`, `/sb/themes`, `/sb/themes/list`, `/sb/recommendations/keyword` and `/sb/recommendations/targets/{product/list,category,brand}`. It does **not** carry `/sb/negativeTargets/brands/recommendations`, `/sb/targets/categories` or `/sb/targets/products/count`.
  - The JSON titled *Sponsored Brands 3.0* (`SponsoredBrands_prod_3p.json`, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json), 50 paths. It carries the `/sb/v4/…` campaign, ad group, ad and migration paths, budget rules, `/sb/recommendations/keyword`, `/sb/targets/categories`, `/sb/targets/categories/{categoryRefinementId}/refinements`, `/sb/targets/products/count` and `/sb/negativeTargets/brands/recommendations`. It does **not** carry `/sb/keywords`, `/sb/negativeKeywords`, `/sb/targets` or `/sb/themes`.
  - The cloudfront JSON *Sponsored Brands campaign management 4.0* (https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json), 48 paths: the same set as the *Sponsored Brands 3.0* JSON less `/sb/campaigns/budgetRules/recommendations` and `/sb/recommendations/keyword`.

  `GET /sb/negativeTargets/brands/recommendations` (`SBTargetingGetNegativeBrands`) answers under `application/vnd.sbtargeting.v4+json` in both JSON models, with the description "Only available in the following marketplaces: US, CA, MX, UK, DE, FR, ES, IT, IN, JP". The *Deprecations* page links SB v4 ad paths to the docs location `sponsored-brands/3-0/openapi/prod`, which is the *Sponsored Brands 3.0* JSON. [official] the three models as named, read 2026-11-09; *Deprecations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md
  - [seat] So both statements in the sibling files are true of the file each read: `/sb/negativeKeywords` is in the SB v3 YAML and not in the *Sponsored Brands 3.0* JSON; the brand-negative recommendations operation is in the *Sponsored Brands 3.0* JSON and the SB v4 JSON (v4 media type) and not in the v3 YAML.

**SD recommendations**

- RULE: `POST /sd/targets/recommendations` "provides product, category and standard audience recommendations to target based on the list of input ASINs. Allow 1 week for our systems to process data for any new ASINs listed on Amazon before using this service." "For API v3.1, the API returns up to 100 recommendations for both product and category targeting." [official] OpenAPI model *Sponsored Display v3* (as above). The release note of 2023-11-06 added `themes`: "Target products under each theme are curated specific to the use case, with high-quality suggestions based on Amazon first-party signals. Each theme will have up to 50 individually recommended products". [official] Ads API *Release notes* (as above)

**The v1 Recommendations API (launched August 2026)**

- RULE: "The Recommendations API provides a single interface for retrieving recommendations across Amazon advertiser campaigns." It has two endpoints:
  - `GET /adsApi/v1/list/recommendations`, which returns "only recommendation types that do not require type-specific input fields";
  - `POST /adsApi/v1/query/recommendations`, which runs in discovery mode or scoped mode. Scoped mode "is required for recommendation types that need additional inputs, such as branded keyword recommendations, bid recommendations, or cross-format extension recommendations".

  "Launch date: August 2026"; "Locales: Worldwide". "Design your application to tolerate `recommendationType` values it does not recognize". [official] Ads API guide *Recommendations API overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/overview.md; release note 2026-08-31 (as above)
- RULE (types live on 2026-11-09): the types page lists four:
  - `REMOTE_CAMPAIGN_PAUSED` (SP);
  - `AUTOMATIC_GLOBAL_ADS_ENROLLMENT`;
  - `BRAND_PRODUCT_SEGMENT` (SB): "Recommends product groups within a brand that shoppers search for as a distinct need";
  - `BRAND_PRODUCT_KEYWORD` (SB): "Recommends keywords and bids for brand product segments".

  `BRAND_PRODUCT_KEYWORD` returns a `keywordTarget`, a `recommendedBid`, and a `keywordTheme` ("for example `Generic`, `Branded`, or `Seasonal`"). `recommendedObjectType` values include `BRANDED_KEYWORD`, `UNBRANDED_KEYWORD`, `BRAND_PRODUCT_SEGMENT` and `BRAND_PRODUCT_KEYWORD`. [official] Ads API guide *Recommendation types*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/recommendation-types.md; Ads API guide *How to call the Recommendations API*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/how-to.md
  - The same page: "Recommendation types beyond the table above are not currently available through these endpoints; requesting them returns `400 BadRequest` with the error code `INVALID_RECOMMENDATION_TYPE`."
  - [seat] The types list "is updated as new recommendation types launch". Which targeting recommendations exist on this surface is therefore a run-time read, and today's four are a snapshot, not a rule.

**The tactical recommendations API (sponsored ads, 2023)**

- RULE: a separate, older surface: `POST /recommendations/list`, `POST /recommendations/update` and `POST /recommendations/apply` ("to automatically apply recommendations to your account"), announced in beta on 2023-05-25 for "Sponsored Products, Sponsored Brands, and Sponsored Display campaigns", "Regions: All". "Recommendations are made by Amazon Ads machine learning algorithms or account management teams". [official] Ads API *Release notes* (as above). Its model ("Sponsored Ad recommendations for Amazon Advertiser accounts", version 3.0) lists targeting types among others: `NEW_KEYWORD` ("Create new keywords to increase visibility"), `KEYWORD_BID`, `KEYWORD_STATE`, `NEW_NEGATIVE_KEYWORD` ("Create new negative keywords to reduce unwanted traffic"), `NEW_PRODUCT_TARGETING`, `PRODUCT_TARGETING_BID`, `PRODUCT_TARGETING_STATE`, `NEW_NEGATIVE_PRODUCT_TARGETING`, `NEW_AUDIENCE_TARGETING` and `NEW_NEGATIVE_AUDIENCE_TARGETING`. [official] OpenAPI model *Recommendations*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json. The overview and get-started guides linked from the release note return 404 on the cloudfront host.
  - [seat] An earlier reading of this model as DSP-only was wrong; it is the sponsored-ads tactical surface. Whether it still returns recommendations after the v1 Recommendations API launched is not stated on the pages read.

**Console surfaces**

- RULE (Ads Agent targeting): "AI targeting: Describe the audience you want to reach in plain language and receive targeting recommendations across products, categories, keywords, and Amazon audiences". [official] Library news *Introducing Amazon Ads Agent, your AI-powered ad platform* (unBoxed 2026, dated 2026-09-29), https://advertising.amazon.com/library/news/amazon-ads-agent. On the help center: "To use Ads Agent to generate policy-compliant Amazon audience, keyword, and category suggestions: Click Add targeting with AI." "Ads Agent is not available for advertisers in CL, CO, AR, MENA, NZ, IN, KR, CN, TW, TH." [official] Help *Set up targeting* (G7A36P2ZEMPT7N73, lastModified 2026-07-27), https://advertising.amazon.com/help/G7A36P2ZEMPT7N73. Ads Agent as a tool is `beyond/automation-and-amazon-tools.md`'s.
- RULE (suggested products, which ASINs to advertise rather than target): "We use machine-learning models to identify products with a high likelihood of being clicked if advertised. Suggested products are 46 times more likely to generate ad-attributed clicks compared to nonsuggested products (Amazon internal data, WW, 03/26/2023-04/01/2023)." [official] Help *Suggested products* (G9DL6CTTHZ56GU38, lastModified 2026-02-24), https://advertising.amazon.com/help/G9DL6CTTHZ56GU38. The figure is Amazon's own and is for human readers only. Which ASINs to launch is `areas/launch.md`'s.

### K. Sponsored Brands keyword and product targeting

- RULE: "An ad group can be associated to either product or keyword targeting expressions." Endpoints:
  - "For keyword targeting, use the POST /sb/keywords endpoint";
  - "For product targeting, use the POST /sb/targets endpoint";
  - "For theme targeting, use the POST /sb/themes endpoint".

  [official] Ads API guide *Get started with Sponsored Brands campaigns* (as above)
- RULE (keyword matching): broad, phrase and exact, with semantic matching and the broad match modifier (item C). Negatives are `negativeExact` and `negativePhrase` (item C).
- RULE (product predicates): SB product expressions use:
  - `asinCategorySameAs`;
  - `asinBrandSameAs`;
  - `asinPriceLessThan`, `asinPriceBetween`, `asinPriceGreaterThan`;
  - `asinReviewRatingLessThan`, `asinReviewRatingBetween`, `asinReviewRatingGreaterThan`;
  - `asinSameAs`.

  SB has no expanded-ASIN predicate and no Prime, age-range or genre refinement. SB negative targets use `asinBrandSameAs` and `asinSameAs`. [official] OpenAPI model *Sponsored Brands v3* (as above); Help GB2JECV9CJK6R6AL ("Sponsored Products and Display: you can also refine categories by Prime shipping eligibility").
- RULE (formats): "you can choose between manual collection, automatic collection, store spotlight, or video" [official] Ads API guide *Sponsored Brands overview* (cited below). Sponsored Brands Collections went worldwide in the Unified Ads API and SB v4 API on 2026-09-23. [official] Ads API *Release notes* (as above).
- RULE (the legacy Product Collection end date: Amazon's pages give two months). Re-read 2026-11-09:
  - *Deprecations*, entry "June 2026 - Deprecation of Sponsored Brands Product Collection Ad Type": "Starting August 2026, requests to create new Product Collection ads will succeed but create a Manual Collection ad instead" (in v1, `productCollectionSettings` "will be automatically mapped to `manualCollectionSettings`"); manual collections need at least 3 ASINs and titles of at most 32 characters; "Post January 2027, requests to create new Product Collection ads will return an error." The page's table gives shutoff "January 2027" for both the V0 paths (`/sb/v4/ads/productCollection`, `/sb/v4/ads/productCollectionExtended`, `/sb/ads/creatives/productCollectionExtended`) and the V1 `productCollectionSettings`. [official] *Deprecations*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md
  - The API migration guide says the same: "January 2027 | **Final shutoff**. All API requests to create Product Collection ads will be rejected with an error." [official] Ads API guide *Product Collection Migration Guide*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-product-collection.md
  - The release note of 2026-09-18 ("Introducing the ListMigrations API…"): "Sponsored Brands collections replace the legacy Product Collection format… Beginning February 2027, product collections will no longer be supported." `POST /sb/v4/migrations/list` returns recommended `MANUAL_COLLECTION` and `AUTO_COLLECTION` replacements. [official] Ads API *Release notes* (as above)
  - The console help page (lastModified 2026-10-05) says "before the February 2027 deprecation", "Beginning February 2027, product collections will no longer be supported", and "Eligible … product collection ads with 3 ASINs that have not been migrated will be automatically transitioned to manual collections featuring the same 3 ASINs. Product collections with fewer than 3 ASINs will not auto-migrate." A launched replacement runs beside the legacy ad "for 4 weeks", after which "we'll archive the legacy ad. Archived legacy ads cannot be relaunched." [official] Help *Migrate from Product collections to Sponsored Brands collections* (GV7N6KZTH4HF4T2P, lastModified 2026-10-05), https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P
  - [seat] Read together: the API pages give January 2027 for creates to fail, and the console help and the ListMigrations note give February 2027 for the format to stop being supported. Both dates are Amazon's; `method/ads-api-surface.md` owns the deprecation calendar.
- RULE (targeting by collection format): the same help page's comparison table gives "Targeting: Keyword or product" for product collections and manual collections, and "Keyword only" for auto collections, whose products are "3–10 (automatically selected from your catalog by Amazon AI)". [official] Help GV7N6KZTH4HF4T2P (as above)
  - [seat] An SB ad group that holds product targets cannot carry an auto collection ad on this table's terms. A product-collection ad group with product targets migrates to a manual collection, not an auto one. "Automatic collections highlight to shoppers the best combination of products based on your keyword targets and shopper queries… Our AI engine dynamically groups the most relevant products from your catalog into collections based on your keyword targets and shopper search queries." "Product exclusions (optional): To exclude certain products related to your keywords that you don't want to advertise, enter up to 1,000 ASINs". [official] Help GF86HBCNDJUAC5WN (as above); Ads API guide *Sponsored Brands overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/overview.md
  - [seat] With automatic collections, the keyword picks the query and Amazon picks which of the brand's products show. The target-to-product mapping is no longer the advertiser's.
- RULE (reserve share of voice): reserve SOV takes:
  - "Reserve 5 to 1,000 keywords associated with any of your brands";
  - "We will validate keywords for reservation and reject any non-branded keywords";
  - "Suggested keywords are related to your brands and listed in order of keyword search volume";
  - "the campaign duration must be between 15 and 92 days";
  - "A minimum budget of $3,000 is required";
  - "You must add all reserved keywords to an ad group within 14 days of your campaign start date";
  - "once the campaign starts, you can't change your keywords, campaign duration, or budget".

  "Reserve share of voice is not available in Spain." It gives "a fixed, upfront price to display your ads in the top of search placement". [official] Help *Reserve keywords in a Sponsored Brands campaign* (G86SD7HK6NHHRB9B, lastModified 2026-07-07), https://advertising.amazon.com/help/G86SD7HK6NHHRB9B
  - The SB create page words the 14-day rule as "You must map keywords to a relevant ad within 14 days of your campaign start. Keywords not associated with a relevant ad within 14 days will be removed from your campaign", and adds "The same keyword can't be reserved in multiple campaigns or ad groups." [official] Help GF86HBCNDJUAC5WN (as above)
  - API (launched 2025-10-15): branded keyword recommendations come from `POST /adsApi/v1/create/recommendations/sb` with `recommendationType: BRANDED_KEYWORD`; keywords outside that list are checked with `POST /adsApi/v1/create/keywordReservationValidations/sb`; reserved keywords are attached with `POST /adsApi/v1/create/advertisingDealTargets/sb` (`targetType: BRANDED_KEYWORD`). [official] Ads API guide *Reserve share of voice*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/reserve-share-of-voice.md; release note 2025-10-15 (as above). The guide gives no duration or budget figures.
  - The goals page gives "Your pricing is for the duration of your campaign, which must be between 30 to 92 days." [official] Help GXXPFXLSVX9VD3U9 (as above). This is a conflict; see *Open questions*.
  - The library guide (dateModified 2026-10-09) gives a third duration and a different minimum: "Select the campaign flight (e.g., 14–90 days)", and eligibility "provided they can reserve a minimum of five branded keywords, with a minimum spend of $6K per campaign for the U.S. marketplace". Its marketplace answer: "Reserve share of voice is available across 20 Sponsored Brands-enabled marketplaces: United States, Canada, Mexico, Brazil, Germany, France, Italy, United Kingdom, Belgium, Poland, Netherlands, Sweden, Turkey, Ireland, Australia, Japan, India, Singapore, United Arab Emirates, and Saudi Arabia." [official] Library guide *How to set up Amazon Sponsored Brands reserve share of voice*, https://advertising.amazon.com/library/guides/sponsored-brands-reserve-share-of-voice
  - The what's-new page (dateModified 2026-10-09) lists "Middle East : Egypt, Saudi Arabia, United Arab Emirates" and Europe without Ireland or Spain. [official] What's new *Drive top-of-search visibility and engagement*, https://advertising.amazon.com/resources/whats-new/sponsored-brands-reserve-share-of-voice
  - The SB v4 model: "Goal-based campaigns are not supported in the Ireland (IE) marketplace." [official] OpenAPI model *Sponsored Brands v4* (as above)
  - [seat] On 2026-11-09 Amazon's pages give three flight ranges (15–92, 30–92, "e.g., 14–90" days), two US minimums ($3,000 budget; $6K spend), and marketplace lists that differ on Ireland and Egypt; all agree Spain is absent. `beyond/brand-defense-and-competition.md` owns reserve SOV and records the same spread.
  - It also says: "We strive to deliver 95% SOV at the campaign level when campaigns are properly set up with relevant creative assets that align with the selected keywords." [official] Help GXXPFXLSVX9VD3U9 (as above)
  - Every figure in this item is for human readers only.
- RULE (branded keyword rejection): "Keywords must be branded and related to any of your brands. For example, if you are advertising a skincare brand named Glow, you can include branded keywords like Glow moisturizer and Glow skincare. You cannot include generic terms like moisturizer or face wash." The page lists these "possible reasons why your keyword was rejected":
  - "Your brand or trademark is not yet registered with Amazon Registry."
  - "Your keywords with your brand name or trademark are too broad."
  - "Your keywords contain common misspellings and variations of brand name or trademarks."
  - "You used non-branded keywords (shoes, lipstick)."
  - "A keyword contains both your and another company's brand name or trademark or your keyword has a brand name or trademark shared by more than 2 brands."
  - "You used keywords that contain another company's brand name or trademark."
  - "Your brand isn't mapped to the advertiser account where you are reserving the keyword."

  "Once your keyword is removed, you cannot add it back to the same campaign."

  [official] Help *Branded keyword guidelines and keyword suspension* (G2QZJUGUT4RGLJ6N, lastModified 2025-11-05), https://advertising.amazon.com/help/G2QZJUGUT4RGLJ6N. This is the one place in Amazon's text where another company's trademark in a keyword is grounds for rejection, and it is scoped to reserve SOV. See item P.
- RULE (top-of-search impression share, SB): "This shows the amount of impressions the advertiser received for the reserved keyword divided by the total amount of impressions across all ads for the reserved keyword." [official] Help GXXPFXLSVX9VD3U9 (as above). The SB goal enum: "Brand Impression Share (BIS) is Top of search (ToS) impression shares for branded search terms." [official] OpenAPI model *Sponsored Brands v3* (as above)

### L. Sponsored Display targeting: contextual and audiences

**Who and where**

- RULE: "If you sell on the Amazon store, you can use remarketing, in-market, lifestyle, and custom audiences and/or contextual targeting. If you don't sell on the Amazon Store, you can target interest/ lifestyle, and in-market audiences." Display targeting "uses first-party shopping, streaming, and browsing signals and insights from Amazon, Prime Video, Twitch, and IMDb". [official] Help *Understand targeting in Display campaigns* (GPKPWTLW6B8T683N, lastModified 2026-03-19), https://advertising.amazon.com/help/GPKPWTLW6B8T683N
- RULE (past-purchaser exclusion): "Display campaigns that use Audiences will always exclude past customers who purchased your advertised products or similar products in the past 30-day window." [official] Help GPKPWTLW6B8T683N (as above)
  - [seat] A views-remarketing audience in SD therefore cannot reach a shopper who bought the advertised product in the last 30 days, whatever lookback is chosen.

**Contextual targeting**

- RULE (where contextual targets serve):
  - "If you add the "similar to advertised products" category, or a suggested category with no refinements your ad will: Reach audiences on Amazon… Reach audiences off Amazon".
  - "If you add individual products, or categories with refinements your ad will: Serve ads on Amazon only."
  - "Display doesn't restrict the categories where you're able to advertise. You can advertise on product detail pages even when they're outside of your category to reach incremental audiences "outside the aisle." We use relevancy guardrails to make sure that ads are shown on appropriate detail pages."
  - "Tip: Add at least 10 well performing products when you use contextual targeting."
  - "Contextual targeting is available only to advertisers that sell products and services on Amazon."

  [official] Help *Understand contextual targeting in Display* (GNTK7LTYZS3KSTAN, lastModified 2026-05-01), https://advertising.amazon.com/help/GNTK7LTYZS3KSTAN
- RULE (SD v3 contextual predicates, usable under tactic `T00030` and, for contextual campaigns, `T00020`):
  - `asinSameAs`;
  - `asinCategorySameAs`;
  - `asinBrandSameAs`;
  - price and review predicates;
  - `asinIsPrimeShippingEligible`;
  - `asinAgeRangeSameAs`;
  - `asinGenreSameAs`;
  - `similarProduct`.

  "Brand, price, and review predicates are optional and may only be specified if category is also specified." "Review predicates accept numbers between 0 and 5 and are inclusive." "Prices are not inclusive." "'similarProduct' has no expression value or refinements." [official] OpenAPI model *Sponsored Display v3* (as above)
- RULE (dynamic segment): ""Similar to advertised products" product targeting for Sponsored Display is a dynamic segment option that allows advertisers to leverage machine learning to help reach relevant audiences on popular detail pages of other similar and complementary products." "When advertisers create new campaigns in the Amazon Ads console, "Similar to advertised products" targeting is added automatically." "For advertisers creating campaigns through the Amazon Ads API, a targeting clause of type "similarProduct" must be explicitly created". [official] Ads API guide *Sponsored Display dynamic segments overview*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/dynamic-segments.md
  - [seat] The console adds this target and the API does not. An SD campaign built through the API lacks it unless the caller creates it.
- GUIDANCE: the SD contextual guide recommends `similarProduct`, describing it as "dynamically generated using machine learning models that are built on retail data". SD negative targets are made through `/sd/negativeTargets`. [official] Ads API guide *Sponsored Display contextual targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/contextual-targeting.md

**Audiences (tactic `T00030`)**

- RULE (clauses, SD v3), in the model's words:
  - `views(exactProduct lookback=…)`: "Target an audience that has viewed the advertised asins in the past 7,14,30,60, or 90 days";
  - `views(similarProduct …)`: viewed "similar products to the advertised asins";
  - `views(asinCategorySameAs=… [brand, price refinements] lookback=…)`;
  - `purchases(relatedProduct …)` and `purchases(exactProduct …)`: "in the past 7,14,30,60,90,180 or 365 days";
  - `purchases(asinCategorySameAs=… …)`;
  - `audiencesLikelyInterestedInAd`: "Dynamic segment to target audiences that are likely to consider and buy from your business… only supported when using landingPageType of OFF_AMAZON_LINK";
  - `audience(audienceSameAs=…)`: "Target the given Amazon Audience";
  - content clause `contentCategorySameAs=amzn1.iab-content.…`: "Target an audience that has engaged with or shown interest in the given entertainment category".

  [official] OpenAPI model *Sponsored Display v3* (as above)
- RULE (lookback, conflicting text in the model): `TargetingPredicateNested` says that for manual ASIN-grain and category-grain targeting "The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'". The clause table caps views at 90. [official] OpenAPI model *Sponsored Display v3* (as above). The help center settles the console side: "Purchases remarketing supports lookback windows up to 365 days; views remarketing supports up to 90 days." "All lookback windows include consumers currently browsing content related to the specified categories." [official] Help *Understand remarketing audience segments* (G82GQS569JWSVNRB, lastModified 2026-10-23), https://advertising.amazon.com/help/G82GQS569JWSVNRB
- RULE (remarketing segments): category audiences can be refined "based on brand, price band, Prime eligibility, or star rating". Dynamic segments "use machine learning and don't support product attribute refinements":
  - "Advertised products" (purchases and views);
  - "Related to advertised products" (purchases): "audiences who bought products related or complementary to your advertised products";
  - "Similar to advertised products" (views): "audiences who viewed products highly similar to your advertised products".

  "You must sell products or services on Amazon to use remarketing audiences in Display campaigns." [official] Help G82GQS569JWSVNRB (as above)
- RULE (in-market, interest and lifestyle):
  - "In-market audiences allow advertisers to engage consumers that are "in-the-aisle" and recently shopped for products in a given category."
  - Interest and lifestyle audiences are "groups of consumers who share a common interest or lifestyle based on Amazon streaming, browse, and purchase signals".
  - Custom audiences come from AMC, "rule-based or lookalike".

  [official] Help GPKPWTLW6B8T683N (as above). Discovery of audience ids is through the Audiences API (taxonomy, discovery, overlapping audiences). [official] Ads API guide *Sponsored Display audience targeting*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/audience-targeting.md; OpenAPI model *Audiences*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json

**Where audience ids come from (two discovery surfaces)**

Only one SD clause takes an Amazon audience id: `audience(audienceSameAs=…)`. The `views(…)` and `purchases(…)` clauses take ASINs, categories and a lookback, not an audience id. SP audience bid boosts (`shopperCohortBidding`) and SB audience boosts also take an `audienceId`. Amazon documents two listing surfaces for these ids.

- RULE (SD and DSP: the Audiences API, *Audiences* 3.0, "Audience Discovery API"):
  - `POST /audiences/taxonomy/list` (`fetchTaxonomy`), "Browse the taxonomy of audience categories". The body takes `adType` (`DSP`, `SD` or `ST`), `categoryPath` (an array of node names) and `countries` (one ISO code per request). "main categories will be returned if no path is specified." Each node returns `category` and `audienceCount`. The guide: "This API does not return the audience segments; instead, you use the category path from this API to call the audience discovery API". Its sample top level for SD is "In-market" (6,236 audiences), "Interest" (968), "Lifestyle" (672) and "Life event" (8); the counts are a sample, for human readers only.
  - `POST /audiences/list` (`listAudiences`), "Gets audience segments based on filters". Query parameters `advertiserId` ("required for the DSP adType, but optional for the SD adType"), `canTarget` ("When set to true, only targetable audience segments will be returned"), `nextToken`, `maxResults`. Body: `adType`, `countries`, and `filters`, each a `field` with `operator` (`EQ` or `NOT_EQ`) and `values`. Filter fields: "'audienceName', 'category', 'categoryPath', 'audienceId' and 'status'. The 'audienceName' is a broad match filter but not an exact match. The 'category' enum returns all audiences under a high-level category, whereas the 'categoryPath' enum expects a path of nodes in the taxonomy tree and returns audiences attached directly to the node at the specified path." Several values in one filter are OR'd. Each audience returns `audienceId`, `audienceName`, `category`, `subCategory`, `description`, `status` (`Active`, `Deactivated`, `Deprecated`, `Failed`, `Pending`, `Processing`), dates, and a `forecasts.inventoryForecasts` daily-reach band.
  - `GET /insights/audiences/{audienceId}/overlappingAudiences?adType=SD` returns "the top 30 audiences that overlap with the selected audience".
  - The guide's create example puts the returned id into an SD target: `"expression": [{"type": "audience", "value": [{"type": "audienceSameAs", "value": 365445316056904705}]}]` under `POST /sd/targets` with `expressionType: manual`.

  [official] OpenAPI model *Audiences* (as above); Ads API guide *Sponsored Display audience targeting* (as above)
- RULE (SP, SB and SD: the Targetable Entities API, *Targetable Entities* 3.0, "Discover targetable entities"):
  - `POST /targetableEntities/list` (`ListTargetableEntities`), media type `application/vnd.Mindreader.TargetableEntitiesResource.v1+json`. Body: `adProduct` (required: `SPONSORED_BRANDS`, `SPONSORED_DISPLAY`, `SPONSORED_PRODUCTS` or `SPONSORED_TELEVISION`), `targetTypeFilter` (up to 4 of `AUDIENCE`, `CONTENT_CATEGORY`, `PRODUCT_CATEGORY`, `PRODUCT_CATEGORY_AUDIENCE`; empty means all), `pathsFilter` (paths as lists of strings), `searchQueryFilter` ("Search for terms or phrases that are relevant to your advertising goals… "Runners", "Athletic Apparel", or "Fitness Enthusiasts""), `productCategoryIdFilter`, `parentBrowseNodeIdFilter`, `locale` (27 values, among them `ja_JP` and `de_DE`), `maxResults` (1–250) and `nextToken`. Each entity returns `targetType`, `path`, and per type `audienceId`/`audienceResolved`/`audienceTooltip`, `contentCategoryId`/`contentCategoryResolved` or `productCategoryId`/`productCategoryResolved`, plus `behaviouralTargetingEligibility` ("All" or "None") and `childCount`.
  - `POST /targetableEntities/paths/list` (`ListTargetableEntityPaths`) returns "The direct descendants of the paths specified in the request's pathsFilter field".

  [official] OpenAPI model *Targetable Entities*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/TargetableEntities_prod_3p.json
- RULE (which path holds which audiences, for SP and SB boosts): the SP 3.0 model's `SponsoredProductsAudienceSegmentType` says Amazon-built audiences are listed with "`adProduct`=`SPONSORED_PRODUCTS`, `targetTypeFilter`=`AUDIENCE` and `pathsFilter` = `[["Audience Category", "Custom-built", "Product"]]`", and AMC audiences with `pathsFilter` `[["Audience Category", "Custom-built", "AMC"]]`; "Only the audiences retrieved using these filters are usable." The field itself is "DEPRECATED… The audience type is automatically determined… by examining the Audience path. Audience IDs are guaranteed to be unique across all audience types". `SponsoredProductsShopperCohortBidding.audienceSegments` takes exactly one segment (`maxItems` 1) with an `audienceId` of 1 to 20 characters. [official] OpenAPI model *Sponsored Products 3.0* (as above). For SB the release notes give the same call with `adProduct=SPONSORED_BRANDS` and the `Product` path, the id then used "with `AudienceSegmentType` of `BEHAVIOR_DYNAMIC`", and the SB guide's sample `POST targetableEntities/list` with `{"adProduct": "SPONSORED_BRANDS"}` returns AMC audiences under `["Audience Category","Custom-built","AMC"]`. [official] Ads API *Release notes* (2025-03-12, 2025-03-24, 2025-08-22); Ads API guide *Shopper cohort bidding* (Sponsored Brands), https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/bidding/shopper-cohort.md
- RULE (v1): the v1 merged model's `AudienceTarget` ("Target based on a specified audience ID") takes `audienceId`, a `groupId` ("You may specify up to 10 include groups and 1 exclude group") and group operators; `AudienceBidAdjustment` takes `audienceId` and `percentage` ("Null removes audience"). [official] OpenAPI model *Amazon Ads API (all), merged* (as above)
  - [seat] The Audiences API's `adType` enum has no SP or SB value, so SP and SB boost ids come from the Targetable Entities API only. How bids on these boosts behave is `areas/bids-and-placements.md`'s.
- RULE (audience policy): "Advertisers may not use audience segments that aren't relevant to the product or service being promoted." "Ad lines must have a forecasted reach across their flight time of at least 1,000 unique users or have first delivered contextually to at least 1,000 unique users, to deliver impressions by behavioral targeting, otherwise only contextual targeting can be used." "Modeled targeting solutions that are based upon a seed customer set, such as lookalikes and performalikes, must have a minimum seed set size of 100 distinct customers." The page also lists prohibited targeting characteristics. [official] Help *Targeting* policy (GD6SPCK5RJZL73PU, lastModified 2026-08-03), https://advertising.amazon.com/help/GD6SPCK5RJZL73PU

**Multi-signal targeting replacing standalone contextual (unified console)**

- RULE: "If you're looking for contextual targeting, it's no longer a standalone feature. It has been incorporated into multi-signal targeting." Multi-signal targeting combines:
  - "Contextual signals: Match ads to content semantically related to a keyword, product, or category";
  - "Behavioral signals: Target shoppers based on view, purchase, search activity and more. For example, shoppers who have searched for products related to your keywords in the past 7 days."

  Further rules:
  - "Policy-restricted items: Products, keywords, and categories required to be contextual-only for policy compliance remain that way."
  - "Exclusions: When you exclude a product, keyword, or category, it's applied contextually".
  - Products: "We recommend including 10-20+ ASINs to start"; "You can include 500 ASINs maximum for inclusion and exclusion lists per ad group".
  - Keywords: "Include at least 25 keywords (500 maximum)".

  [official] Help *Set up multi-signal targeting* (GDTFJ44CQ2QUKX9X, lastModified 2026-07-01), https://advertising.amazon.com/help/GDTFJ44CQ2QUKX9X
  - [seat] This page describes ad groups ("formerly known as Line Item on Amazon DSP") in the unified Display/DSP buying flow. It is not the SD v3 API, which still takes `T00020` and `T00030`. Display campaign types under DVA+ are `beyond/ad-products-and-eligibility.md`'s. The v1 `ProductCategoryMatchType` value `MULTISIGNAL_BROAD` is this feature's name in the v1 model.
- RULE (DVA+): "DVA+ offers a single, simplified buying experience and optimization solution, combining what was previously managed through separate campaign types—including Sponsored Display, Sponsored TV, and programmatic campaigns." "DVA+ will begin rolling out to advertisers beginning in late October." [official] *Introducing Amazon Ads Agent, your AI-powered ad platform* (dated 2026-09-29, as above)

### M. Where keyword and product ideas come from: Amazon's own sources

This item records what each source *is*, as Amazon defines it. How the search term report is worked into harvests and negatives is `areas/search-terms-and-negatives.md`'s. Its columns and windows are `method/reporting.md`'s.

**The search term report (Ads)**

- RULE: "Search term reports contain search term performance metrics broken down by targeting expressions and keywords. Note that search term reports only include impressions that resulted in at least one ad click." The `keywordType` filter takes `BROAD`, `PHRASE`, `EXACT`, `TARGETING_EXPRESSION` or `TARGETING_EXPRESSION_PREDEFINED`. The predefined value covers the auto groups. Report types are `spSearchTerm` and `sbSearchTerm`, grouped by `searchTerm`. [official] Ads API guide *Search term reports* (v3), https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/report-types/search-term.md. The targeting report (`spTargeting`, `sbTargeting`, `sdTargeting`) takes the same `keywordType` values; on SB it adds `THEME`. [official] Ads API guide *Targeting reports* (v3), https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/report-types/targeting.md
- RULE (v1 names):
  - `searchTerm.value` is "The search term used by the customer", available for SP and SB only.
  - `matchedTarget.value` is "The product page where the ad appeared", available for Sponsored Display only (v3 name `matchedTargetAsin`).
  - `productRelevance.value` "Indicates whether the product was directly promoted in the campaign or attributed based on relevance to promoted products (halo)."

  [official] Ads API guides *Search term (Targeting)*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/targeting/search-term.md; *Matched target (Targeting)*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/targeting/matched-target.md; *Product relevance (Product)*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/product/product-relevance.md
  - This corrects the prior paid-keywords research (read 2026-10-14), which had `matchedTarget.value` usable for SP. The v1 dimension page today lists Sponsored Display only.
  - [seat] On SP, the ASIN pages where a product target or a Substitutes/Complements group served show up in the search-term column as 10-character ASINs. They do not show up in a matched-target dimension.
- GUIDANCE: "Replace low-performing keywords and increase bids on high-performing keywords using insights from the search terms report." [official] Help GK3MNACNTXG659J9 (as above). The best-practices guide describes the search term report as the shopping terms "that resulted in at least one click on your ad", and the targeting report as covering keywords and products "with at least one impression". [official] *Best practices for your Sponsored Products ads* (as above)

**The Search Term Impression Share report**

- RULE: "The search term impression share report shows, for each search term, the numeric rank of your account-wide impression share relative to all the other advertisers generating impressions on the same term." It is "Available for: sellers, vendors, authors, and book vendors running Sponsored Brands and Sponsored Products campaigns." "Use this report to review the overall percentage of ad impressions that you've received compared to other advertisers over last 30 days." "The search term impression share report has 2 time units available: summary or daily. The lookback window for this report is 90 days." Amazon's example: "you have a Sponsored Products ad-attributed impression share of 50% on the search term "mobile" on January 1. It means that you won 50% of all the Sponsored Products impressions the search term "mobile" got on that date". [official] Help *Search Term Impression Share (SIS) report for Sponsored Products* (G7AQQUSFVZPAAXEU, lastModified 2026-02-24), https://advertising.amazon.com/help/G7AQQUSFVZPAAXEU
  - [seat] The same page names both a 30-day share and a 90-day report lookback. Read together: the report can be pulled for dates up to 90 days back, and the share is per day or per summary period. The keyword recommendation's share field is fixed at "the last 30 days" (SP) or "the last 7 days" (SB). These are three windows for one idea, and a share figure means nothing without the window it was read over.
- RULE (definitions): "Impression share (IS) is the percentage of impressions that you're getting on this term relative to all the impressions it's generating. An IS of 0% means that you haven't received any impressions on the term." "Impression rank (IR) is where your IS stands relative to other advertisers' share of impressions for the same term." [official] Help GK3MNACNTXG659J9 (as above)
- RULE (v1): `metric.impressionShare` ("The percentage share of all your impressions compared to all other advertisers") and `metric.impressionShareRank` require `adProduct.value`, `advertiserAccount.id` and `searchTerm.value`. Campaign and ad group are among their incompatible dimensions. Their v3 name is `Search Term Impression Rank`/share. [official] Ads API guide *Search (Impression share)*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/impression-share/search.md
  - [seat] Impression share in Amazon's definition is account-wide per search term and cannot be split by campaign. It measures the share of *ad* impressions of one ad type, not of organic results.

**Brand Analytics: Top Search Terms and Search Query Performance (Seller Central and SP-API, not the Ads API)**

- RULE (who): "Amazon Brand Analytics is available to brands enrolled in Amazon Brand Registry." [official] sell.amazon.com blog *What is Amazon Brand Analytics?*, https://sell.amazon.com/blog/brand-analytics
- RULE (Top Search Terms): the dashboard "shows: Search frequency rank for top search terms; Top-clicked brands; Top-clicked categories", plus "the product titles for the three top-clicked products for each search term, along with click shares and conversion shares". [official] *What is Amazon Brand Analytics?* (as above). The SP-API report `GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT`:
  - "Contains data on the most-clicked ASINs by search keyword and department for an Amazon store";
  - takes periods DAY, WEEK, MONTH and QUARTER, which a request cannot span;
  - "is limited to approximately 12 million items… This limit may cause this report to differ from other reporting";
  - requires the Brand Analytics role, Brand Registry and being a brand representative.

  Fields: `departmentName`, `searchTerm`, `searchFrequencyRank`, `clickedAsin`, `clickShareRank`, `clickShare`, `conversionShare`. [official] SP-API docs *Analytics Reports*, https://developer-docs.amazon/sp-api/docs/report-type-values-analytics; schema *sellingPartnerSearchTermsReport*, https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchTermsReport.json
  - [seat] Top Search Terms gives a search frequency *rank*, not a volume. It is marketplace-wide, not limited to the brand's catalog, so it is the one Amazon source of query demand beyond the advertiser's own impressions.
- RULE (Search Query Performance): "This dashboard lists the top queries that led customers to your products." It shows "search query score (which indicates how individual keywords are performing) and search query volume (which tells you how many times customers used a given keyword in Amazon search within a certain time frame)". [official] *What is Amazon Brand Analytics?* (as above). The SP-API report `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT`:
  - is available to sellers only, with the Brand Analytics role and Brand Registry;
  - covers 18 stores: US, CA, MX, BR, ES, UK, FR, NL, DE, IT, SE, TR, SA, AE, IN, SG, AU, JP;
  - takes periods WEEK, MONTH and QUARTER, with a maximum of 17 months for MONTH;
  - takes `asin` as "A space-separated list of ASINs… There is a 200 character limit".

  Fields include `searchQuery`, `searchQueryScore`, `searchQueryVolume`, and query-total and ASIN-level impression, click, cart-add and purchase counts and shares, with shipping-speed splits. [official] SP-API docs *Analytics Reports* (as above). The schema defines the search query as one "relevant to your branded catalog", and impressions as those that "originate from the search results page". [official] schema *sellingPartnerSearchQueryPerformanceReport*, https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchQueryPerformanceReport.json
  - [seat] SQP is the only Amazon source that gives a query **volume** with the brand's share of impressions, clicks, adds and purchases, organic and paid together. It covers only queries where the brand's catalog already appeared.

**Product Opportunity Explorer (Seller Central, not the Ads API or SP-API)**

- RULE (what it is): "Product Opportunity Explorer is a tool that helps Amazon sellers generate new product or offer ideas by better understanding customer demand." "A niche is a collection of customer search terms and products that represent a specific customer need… we create niches by grouping search terms based on the products customers view or purchase after searching." "Keep in mind that search terms and products can exist in multiple niches. Niche metrics are refreshed at the beginning of each week, and new niches are created at the start of each month." Access: "opening the Seller Central main menu, hovering over Growth, and selecting Product Opportunity Explorer." Search results: "We determine relevancy based on text matching between your search terms and the search terms related to niches." [official] Seller guide PDF *Product Opportunity Explorer overview* (undated), https://m.media-amazon.com/images/G/01/sell/guides/Product_Opportunity_Explorer_Overview.pdf
- RULE (what a niche shows, in the same guide):
  - Products: "the products within a niche that cumulatively receive 80% of clicks after customer searches", with brand, average selling price, launch date, reviews and rating;
  - Search Terms: "the top Amazon customer search terms for a niche, along with search volume, click share, search conversion rate, and top-three clicked products", with "Year-over-year and quarter-over-quarter metrics"; "Non-branded search terms with high search volume may indicate customers are open to new solutions. Additionally, you can use this section to plan Sponsored Campaigns when entering a niche";
  - Insights: among others "Average Out of Stock Rate", "% of Prime products", "% of Products Using Sponsored Products", "Top 5 Products Click Share", "Top 20 Products Click Share", "# of Successful Launches";
  - Trends: two metrics at a time over time, among them search volume and search conversion rate.

  [official] *Product Opportunity Explorer overview* (as above)
- RULE (reviews and returns): "The Customer Review Insights tool (found within Product Opportunity Explorer) provides a snapshot of customer sentiment for a particular product or niche." "It buckets themes into positive and negative review snippets and shows you how the review topic impacts the star rating." "The Returns tab within the tool shares the most common reasons why customers return products in the specified niche." ASIN search shows "the niches that the ASIN belongs to", and "not all ASINs belong in niches because niches include the top products receiving clicks for those search terms." [official] sell.amazon.com blog *Get product ideas with Product Opportunity Explorer*, https://sell.amazon.com/blog/product-opportunity-explorer
- RULE (who): the tools page says "Sign up* for a selling account or log in to Seller Central if you already have one", with "*A Professional selling account is $39.99/month + selling fees" (the blog: "*A Professional selling plan is $39.99 a month + selling fees"). No Amazon page read names Brand Registry as a requirement. It also carries Amazon's figure "New products launched using insights from Product Opportunity Explorer have 2.5x higher sales potential in their first three months" (footnote: "2025 Amazon internal data based on a study of sellers in the US, EU, and Japan"), for human readers only. [official] sell.amazon.com *Product Opportunity Explorer*, https://sell.amazon.com/tools/product-opportunity-explorer
- RULE (API): the SP-API Customer Feedback API v2024-06-01 "provides the same information as the Product Opportunity Explorer (OX) on Seller Central and Vendor Central", in the US, UK, FR, IT, DE, ES and JP, "refreshed weekly", "only available in English". Its operations are review topics and trends per ASIN and per browse node, return topics and trends per browse node, and an ASIN's browse node: `getItemReviewTopics`, `getItemReviewTrends`, `getItemBrowseNode`, `getBrowseNodeReviewTopics`, `getBrowseNodeReviewTrends`, `getBrowseNodeReturnTopics`, `getBrowseNodeReturnTrends` under `/customerFeedback/2024-06-01/…`. None returns a niche, a search term or a search volume. [official] SP-API *Customer Feedback v2024-06-01* reference, https://developer-docs.amazon/sp-api/reference/customer-feedback-v2024-06-01; changelog *New: Introducing the Customer Feedback API v2024-06-01*, https://developer-docs.amazon.com/sp-api/changelog/new-introducing-the-customer-feedback-api-v2024-06-01; model `customerFeedback_2024-06-01.json`, https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/models/customer-feedback-api-model/customerFeedback_2024-06-01.json
  - [seat] So POE's niche search-term volume, click share and search conversion rate are a Seller Central screen with no API on 2026-11-09; its review and return insights are readable through `cx-amazon-sp-api`. Unlike SQP, POE's search terms are not limited to queries where the seller's own brand appeared, and no Amazon page read ties it to Brand Registry. Amazon's guide does not define the window behind "search volume" or "click share"; practitioners give different windows (*What practitioners add*).

**Amazon Marketing Cloud keyword clustering**

- GUIDANCE: AMC's keyword clustering playbook "groups similar search terms together based on the products (`ASIN`s) they drive traffic and sales to". It does so with an AMC query on `customer_search_term` and `tracked_item`, then K-means-style clustering in SageMaker. Its stated method: "Utilize scatter plots to visually analyze clusters, apply the 80-20 rule; filter out less relevant clusters." [official] Ads API guide *Amazon Marketing Cloud - Keyword clustering*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/playbooks/keyword-clustering.md (launched 2025-03-20 per the release notes). AMC access is `beyond/automation-and-amazon-tools.md`'s.

### N. Language and per-marketplace rules

- RULE (keyword translation in the console): "The keyword translation feature allows you to enter your preferred keywords in your language, and we'll translate them into the local language of the country where you're launching your campaign." It is "available when creating Sponsored Products and Sponsored Brands campaigns". "We'll use a combination of machine-generated translations, translations by professional linguists, and closest matching terms from the local marketplace". "There's a limit of 1,000 keywords that can be translated at once". "You can't edit a translated keyword". The original keywords are saved, "While they won't be used to target the campaign". [official] Help *Keyword translation* (GHPTCVTGNFZ2KTSP, lastModified 2022-09-20), https://advertising.amazon.com/help/GHPTCVTGNFZ2KTSP
- RULE (languages per country), from the same page:

  | Country | Supported languages |
  |---|---|
  | United States, Canada | Simplified Chinese, Spanish, German, French, Italian, Japanese |
  | Mexico, Brazil, Saudi Arabia, United Arab Emirates | English |
  | United Kingdom | Simplified Chinese, German, French, Dutch, Italian, Spanish |
  | Germany | English, French, Italian, Spanish, Dutch, Simplified Chinese |
  | Italy | English, German, French, Spanish, Dutch, Simplified Chinese |
  | France | English, German, Italian, Spanish, Dutch, Simplified Chinese |
  | Spain | English, French, Italian, German, Dutch, Simplified Chinese |
  | Netherlands | English, German, French, Italian, Spanish, Simplified Chinese |
  | Japan | English, Simplified Chinese |
  | Singapore, Australia, India | Simplified Chinese |

  [official] Help GHPTCVTGNFZ2KTSP (as above). The page was last edited in 2022 and is for human readers only. The live mapping is the Localization API's.
- RULE (API): SP keyword create accepts `nativeLanguageKeyword` ("The unlocalized keyword text in the preferred locale of the advertiser") and `nativeLanguageLocale`. The model says: "Supported locales include: Simplified Chinese (locale: zh_CN) for US, UK and CA. English (locale: en_GB) for DE, FR, IT and ES." [official] OpenAPI model *Sponsored Products 3.0* (as above). The guide: "Most advertisers should not use `nativeLanguageLocale`". "Advertisers who are advertising in other regions can use the `nativeLanguageLocale` and `nativeLanguageKeyword` parameters to specify the equivalent `keyword` in their preferred language for reporting purposes." [official] Ads API guide *Keyword targeting overview* (as above)
  - [seat] The text that targets is `keyword`/`keywordText` in the marketplace's language. The native-language field is a label for the advertiser and does not target.
- RULE (bulksheets): "you can now add keywords in your preferred or native language… your "native language" keyword will be automatically translated into English or the default language of your locale" (2024-06-04; Egypt, Saudi Arabia and the UAE). [official] Ads API *Release notes* (as above)
- RULE (Localization API): the Localization API has these endpoints:
  - `POST /keywords/localize` "Returns localized keywords within specified marketplaces or locales";
  - `POST /products/localize` "Localizes (maps) products from a source marketplace to one or more target marketplaces… Seller requests have an additional condition: the SKU of a localized product must match the SKU of the source product";
  - `POST /targetingExpression/localize` "Localizes (maps) targeting expressions from a source marketplace to one or more target marketplaces";
  - `POST /currencies/localize`.

  [official] OpenAPI model *Localization*, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json
- RULE (global SP campaigns): "Global campaigns enable you to create and launch one Sponsored Products campaign across multiple countries." "Products must be available for sale in all the countries you select for advertising." "Amazon uses generative AI to generate high-performing localized targets and corresponding keywords recommendations based on local search trends and ads for the same or similar products in the target country." "The bids and budgets aren't converted and are only for viewing." [official] Help GKLSYGFS2YD33FER (as above). The multi-country SP model carries `MultiCountryTargetingExpressionType`:
  - `CLOSE_MATCH`, `LOOSE_MATCH`, `SUBSTITUTES`, `COMPLEMENTS`;
  - `KEYWORD_BROAD_MATCH`, `KEYWORD_PHRASE_MATCH`, `KEYWORD_EXACT_MATCH`;
  - `KEYWORD_GROUP`;
  - `PAT_ASIN`, `PAT_CATEGORY`, `PAT_CATEGORY_REFINEMENT`.

  [official] OpenAPI model *Sponsored Products 3.0* (as above)
- RULE (scripts and symbols): per item D, Arabic script only in AE, SA and EG; Devanagari and Tamil everywhere except AE, SA and EG; `%` only in AE, SA and EG. [official] Ads API *Limits* (as above)
- RULE (locale for recommendations): the keyword recommendation `locale` returns translations "for readability" only (item J). The keyword-groups `locale` header "should conform to the IETF BCP 47 standard". [official] OpenAPI model *Sponsored Products 3.0*; Ads API guide *Sponsored Product keyword groups targeting* (as above)
- RULE (feature availability by marketplace), each on its own page:
  - keyword groups: US only, beta (item I);
  - theme-based bid v5 features: US, existing ad groups (item J);
  - category tree: "Amazon.com" (item G);
  - reserve SOV: not in Spain (item K);
  - Ads Agent: not in CL, CO, AR, MENA, NZ, IN, KR, CN, TW, TH (item J);
  - 2025-05-22 negative targeting change: US (item H);
  - SP off-Amazon: a named list of 19 countries (item R).

  [official] pages as cited in each item.
  - goal-based SB campaigns: not in IE (item I).
  - [seat] Availability changes often and is marketplace-specific. It shows in the API's per-item error or on the page on the day; a list like the one above is a dated snapshot.

**Unspaced Japanese and German compounds: what Amazon says, and where it is silent**

No Amazon ads page read on 2026-11-09 states whether broad, phrase, exact or negative matching normalises Japanese script variants (hiragana, katakana, kanji), full-width against half-width characters, or a German compound against the same words written apart. The localized help-center articles could not be read (*Unreachable*). What Amazon's pages do say:

- RULE (characters accepted): the limits page accepts in **all** marketplaces "Hiragana (`　`-`ゟ`)", "Katakana (`゠`-`ヿ`)", "Kanji (`一`-`鿿`)" and "Halfwidth and Fullwidth Forms (`＀`-`￯`)". Its word limits are counted in "parts": "The maximum number of parts for a positive keyword is **10**", "for a negative keyword is **4**", and "For `negativeExact` match type… up to **10** parts". "You can use a blank space in a keyword, but leading or trailing spaces are not allowed." "When using the hyphen (`-`)… they can only be used in the middle of keywords and cannot have blank spaces around them." [official] Ads API *Limits* (as above)
  - [seat] The page does not define a "part". If parts are split on blank spaces, an unspaced Japanese string such as 子供マスク不織布 is one part, and the 4-part negative phrase limit binds on spaced queries only. The hiragana range as written starts at `　`, the ideographic (full-width) space; whether that space separates parts is not stated. Both readings are the seat's.
- GUIDANCE (Japanese phrase match on unspaced text, Amazon's own JP examples): the Japanese keyword-targeting guide's phrase example is "フレーズ一致キーワード「ランニングシューズ」の場合、「女性用ランニングシューズ」や「男性用ランニングシューズ」には広告が表示される可能性がありますが、「ランニング用シューズ」には表示されません" (phrase "running shoes" can show for "women's running shoes" and "men's running shoes", written without spaces, but not for "running-use shoes"). Its exact example: "完全一致キーワード「白いランニングシューズ」は、そのフレーズと完全に一致するか、「ランニングシューズ白」のような非常に近いバリエーションでのみ表示されます". [official] Library guide (ja-jp) *キーワードターゲティングとは何ですか？* (dateModified 2026-10-09), https://advertising.amazon.com/ja-jp/library/guides/keyword-targeting. The Japanese targeting guide's phrase example matches "「Dopplerコットンシーツセット」" to "「キングDopplerコットンシーツセット」", again with no space before the phrase; it says "キーワードに含めることができるのは、文字、数字、スペースです" and that keywords "は大文字と小文字が区別されない". [official] Library guide (ja-jp) *スポンサープロダクト広告のターゲティングに関するガイド* (dateModified 2026-10-20), https://advertising.amazon.com/ja-jp/library/guides/targeting-with-sponsored-products
  - [seat] These are translations of the English examples, but as written they show phrase match finding a keyword inside an unspaced Japanese query, not only at space boundaries. The pages say nothing of hiragana/katakana/kanji or width variants.
- GUIDANCE (German compound against separate words, Amazon's own DE examples): the German keyword-targeting guide: "Mit dem Keyword „Laufschuhe" als Wortgruppen-Übereinstimmung wird Ihre Werbeanzeige beispielsweise für „Laufschuhe für Damen" oder „Laufschuhe für Herren" geschaltet, jedoch nicht für „Schuhe zum Laufen"." For SB: "Wenn Kunden beispielsweise nach „Laufschuhen" suchen, können Kampagnen, die auf semantisch äquivalente Keywords wie „Joggingschuhe" und „Schuhe zum Laufen" ausgerichtet sind, für diese Suche berechtigt sein". Exact: "„weiße Laufschuhe" würde … nur für genau diese Wortgruppe oder sehr ähnliche Varianten wie „Laufschuhe weiß" angezeigt werden." [official] Library guide (de-de) *Was ist Keyword-Targeting?* (dateModified 2026-10-08), https://advertising.amazon.com/de-de/library/guides/keyword-targeting. The German targeting guide's own examples use hyphenated compounds ("Doppler-Baumwollbettlaken-Set"; exact "Bettwäsche-Set aus Doppler-Baumwolle" matching "Bettwäsche-Sets aus Doppler-Baumwolle"). [official] Library guide (de-de) *Ein Leitfaden zum Targeting mit Sponsored Products* (dateModified 2026-10-13), https://advertising.amazon.com/de-de/library/guides/targeting-with-sponsored-products
  - [seat] In Amazon's DE text an SP phrase keyword written as one compound does not reach the same idea written as separate words, while SB's semantic matching can. Whether SP broad or exact bridges compound and split forms (Laufschuhe / Lauf Schuhe / Lauf-Schuhe) is not stated.
- [research] Amazon's own published work shows the retail search stack normalising these cases for **Ads matching** in Japan. Zhang, Huang, Deng, Xiao, Mittal & Deng (Amazon), *Towards Scalability and Extensibility of Query Reformulation Modeling in E-commerce Search* (CIKM 2024; arXiv 2402.11202), describe "script type normalization (e.g., translation between different spellings of the same word, as illustrated by "こども" to "子供" in the Japanese case), tokenization (e.g., converting "子供マスク不織布" to "子供_マスク_不織布"), and token sorting". Queries "only differ in terms of tokenization (i.e., the presence or absence of space) and token order" in their example. In a two-week Japanese A/B test, "we included the Ads matched for" the reformulated queries "directly into the match set" of the original query, with "+0.36%" Ads revenue. The paper does not say which advertiser match types this applies to, and it excludes "identified named entities, such as brands". (See *Published research*.)

### O. Minimum and maximum bids per marketplace (figures for human readers only)

- RULE: the Ads API *Limits* page gives "the maximum allowable bid (in local currency) for keywords or targets by marketplace". The table gives min/max per ad type. Selected columns, read 2026-11-09:

  | Marketplace | Currency | SP min/max | SD CPC min/max | SD vCPM min/max | SB CPC image min/max | SB video CPC min/max |
  |---|---|---|---|---|---|---|
  | US | USD | 0.02/1000 | 0.02/1000 | 1/1000 | 0.10/49 | 0.25/49 |
  | CA | CAD | 0.02/1000 | 0.02/1000 | 1/1000 | 0.10/49 | 0.15/49 |
  | MX | MXN | 0.1/20000 | 0.1/20000 | 5/20000 | 0.10/20000 | 0.15/20000 |
  | BR | BRL | 0.07/3700 | 0.07/3700 | 2/3700 | 0.53/200 | 0.8/25000 |
  | UK | GBP | 0.02/1000 | 0.02/1000 | 1/1000 | 0.10/31 | 0.15/31 |
  | DE, FR, ES, IT, NL, BE | EUR | 0.02/1000 | 0.02/1000 | 1/1000 | 0.10/39 | 0.15/39 |
  | IE | EUR | 0.02/1000 | NA | NA | 0.10/39 | 0.15/39 |
  | SE | SEK | 0.18/9300 | 0.18/1000 | 1/1000 | 0.90/500 | 1.30/500 |
  | PL | PLN | 0.04/2000 | 0.02/1000 | 1/1000 | 0.2/200 | 0.3/200 |
  | TR | TRY | 0.05/2500 | 0.05/2500 | 1.85/2500 | 0.2/200 | 0.3/200 |
  | AE | AED | 0.24/184 | 0.2/3670 | 1/3670 | 0.40/184 | 0.6/184 |
  | SA | SAR | 0.10/3670 | 0.10/3670 | 4/3670 | 0.40/184 | 0.60/184 |
  | EG | EGP | 0.15/5.50 | 0.15/7400 | 5/7400 | 0.7/400 | 1/400 |
  | IN | INR | 1/5000 | 1/5000 | 4/5000 | 1/500 | 1.5/500 |
  | JP | JPY | 2/100000 | 2/100000 | 100/100000 | 10.0/7760 | 15.0/7760 |
  | AU | AUD | 0.02/1410 | 0.2/1000 | 1/1000 | 0.10/70 | 0.15/70 |
  | SG | SGD | 0.02/1100 | .14/1410 | 4/1410 | 0.14/100 | 0.2/1400 |
  | ZA | ZAR | 1/7000 | 0.7/1000 | 1.5/1000 | 0.7/350 | 1.1/350 |

  The page has further SB vCPM columns (BIS, NTB). [official] Ads API *Limits*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md
  - [seat] The EG SP maximum of 5.50 is three orders of magnitude below EG's SD CPC maximum (7400) and below its SB image maximum (400). It reads as a typo on Amazon's page. The bound the endpoint enforces shows in the API's per-item reply to a write.
  - [seat] The SP 3.0 keyword `bid` is described "in minor currency units (example: cents)" in some schemas, while this table and the v1 guide's example bid (0.02) are in major units. See *Open questions*.
- RULE (vCPM floors in the console): "There is a minimum bid requirement for vCPM (it varies by ad type and country). Using the minimum bids may not lead to viewable impressions." [official] Help *Understand bidding on Sponsored ads* (GDS2E64R9GQ35768, lastModified 2026-11-02), https://advertising.amazon.com/help/GDS2E64R9GQ35768
- RULE (reserve prices): "Some reserves help allocate ad space by setting a bid threshold. Your bid must meet this amount to be allocated, and you'll be charged at least this amount if your ad wins." [official] Help *Understand Amazon Ads auctions* (GEXGZNBBWPZZK7P8, lastModified 2026-04-27), https://advertising.amazon.com/help/GEXGZNBBWPZZK7P8
  - [seat] The table's minimum is the lowest bid the API accepts. It is not the lowest bid that wins. Reserve prices per placement are not published. What to bid is `areas/bids-and-placements.md`'s.

### P. Keyword and targeting policy: relevance, restricted targets, trademarks

- RULE (relevance): "The keywords or products targeted in your campaigns must be relevant to the product being promoted. Ads must not target keywords or products that could result in an offensive, insensitive, or undesirable shopper experience. On that account, some product categories aren't permitted as advertising targets." The page's examples:
  - "Prescription drug keyword or products, such as "Lipitor" or "prednisone.""
  - "Offensive, profane, or vulgar keywords or products."
  - "Products, and keywords of products that we don't advertise per our creative acceptance policy, such as e-cigarettes, or sexually explicit and adult products."

  [official] Help G3XAU5G7C2JTNQTM (as above). The same rule appears in the moderation guide: "The keywords or products targeted in your ads must be relevant to the product being promoted." [official] Library guide *A complete guide to Sponsored Brands and display ads moderation*, https://advertising.amazon.com/library/guides/sponsored-brands-display-ads-moderation
- RULE (restricted targets are accepted but do not serve): "If some of your existing targets aren't receiving impressions or clicks, it may be due to keyword and product targeting restrictions. In such cases, you may be able to add a restricted keyword or product when creating your campaign, but ads won't run against those targets." [official] Help G3XAU5G7C2JTNQTM (as above)
  - [seat] A successful create (207 with the item in `success`) is not proof that a target can serve. A restricted target is created and then gets no delivery. `areas/diagnosis.md` owns reading that.
- RULE (policy-restricted items are contextual-only in multi-signal targeting): "Products, keywords, and categories required to be contextual-only for policy compliance remain that way." [official] Help GDTFJ44CQ2QUKX9X (as above)
- RULE (competitors in creative): "Ads on Amazon cannot explicitly call out your competitors by name. You may include references to a "leading brand" or other generic phrasing." The guide's checklist adds: "Don't use superiority claims (the best, the biggest, better than) or mention competitors by name." [official] *A complete guide to Sponsored Brands and display ads moderation* (as above). The O&O prohibited list includes "Disparaging or criticizing a named competitor". [official] Help *Prohibited content and products for Amazon O&O supply* (GTEEH3E3J2BDELBA, lastModified 2026-04-10), https://advertising.amazon.com/help/GTEEH3E3J2BDELBA
- RULE (rights in creative): advertisers must "Obtain and maintain all necessary rights and permissions for all content in ads, such as logos, music, images, and others", and "Comply with Brand Usage Guidelines if referencing Amazon, its products, or programs". [official] Help *General requirements* (G4U9JBZH3664JWX2, lastModified 2026-07-22), https://advertising.amazon.com/help/G4U9JBZH3664JWX2
- RULE (trademarks in keywords, reserve SOV only): "You used keywords that contain another company's brand name or trademark" is a rejection reason for reserved keywords. [official] Help G2QZJUGUT4RGLJ6N (as above)
- Trademarks as auction keywords: **no Amazon page read today forbids, permits or restricts bidding on another company's brand name or trademark as an SP or SB auction keyword, or targeting a competitor's ASINs or brand.** These pages were searched:
  - *General requirements*;
  - *Prohibited content across all supply* (GRW23T7LB4MFMBXQ, lastModified 2026-06-19);
  - *Prohibited content and products for Amazon O&O supply*;
  - *Targeting* policy (GD6SPCK5RJZL73PU);
  - the moderation guide;
  - *Branded keyword guidelines*;
  - the policy tree from *Policies and guidelines* (G26M9XTK78AMR8TP).

  Amazon's own guidance instead names competitor targeting as a strategy:
  - "Conquest" [official] *A guide to targeting with Sponsored Products* (as above);
  - the same guide's line "your competitors may be bidding on your branded keywords, too", and branded keywords defined as including "trademark terms" [official] *A guide to targeting with Sponsored Products*; *What is keyword targeting?* (as above);
  - the brand-negative recommender's sentence comparing "your own brands" and "competitors' brands" (item H).

  [seat] What Amazon's text separates is the **creative** (no naming competitors; rights to all content) from the **target** (must be relevant; restricted categories). Its only trademark-in-keyword rule is the reserve SOV one. Trademark law outside Amazon's policies is not covered by this file. See *Open questions*.
- RULE (policy home and change log): the policy tree starts at *Policies and guidelines* (G26M9XTK78AMR8TP). Changes are logged in *Ad policy change log* (G8X8M375UPCN4UUC, lastModified 2026-04-27). [official] https://advertising.amazon.com/help/G26M9XTK78AMR8TP; https://advertising.amazon.com/help/G8X8M375UPCN4UUC. The older URL https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies now redirects to the help center.

### Q. How a target becomes an impression: auctions and relevance

- RULE: "Our auctions evaluate a variety of factors in determining what ads to show, placing particular value on the ad's expected relevance to the customer." The variables named are:
  - "The content surrounding where the ad will go";
  - "The customer's search query (if applicable)";
  - "The likelihood a customer will engage with the advertised product or service";
  - "The customer's shopping interests".

  "As a result, ads with lower bid amounts, but higher relevance to the customer, can and do win our auctions." "We run billions of auctions each day with multiple auctions often running simultaneously on a single page". [official] Help *Understand Amazon Ads auctions* (GEXGZNBBWPZZK7P8, as above)
- RULE: "Amazon and partners match your keywords to a customer's search term and interests to display ads for the products you advertise." [official] Help G3XAU5G7C2JTNQTM (as above)
  - [seat] A keyword is the advertiser's *eligibility* statement. Which eligible ad shows is decided by the auction, using relevance predictions the advertiser does not see. The match type widens or narrows eligibility; it does not buy position.
- RULE (highest-bid match type wins inside one advertiser): "If you set multiple match types with different bids for the same keyword, then the match type with the highest bid will be used for any matching shopping query." [official] Help GHTRFDZRJPW6764R (as above)
- GUIDANCE (the same case, the library guide, re-read 2026-11-09 with its context): "Test all three match types, with different bids… When setting manual bids, we recommend setting the highest bid on the exact match, a lower on the phrase match, and the lowest bid on the broad match… And don't worry, you won't be bidding against yourself by adding different match types on the same keyword." [official] *A guide to targeting with Sponsored Products* (dateModified 2026-10-09, as above)
  - What is answered, and how far (this file owns the question; `method/change-measurement.md` and `areas/campaign-structure.md` carry it as open): Amazon answers **one keyword text in several match types**. Its words are "the match type with the highest bid will be used for any matching shopping query", and "you won't be bidding against yourself" in the guide. Neither page says whether "the same keyword" means within one ad group or across ad groups and campaigns. Neither says what happens when *different* keyword texts, a keyword and a product target, an auto group and a manual keyword, or two campaigns of one advertiser all match one query. No other Amazon page read on 2026-11-09 (*Understand Amazon Ads auctions*, *Understand keyword match types*, *Set bids*, the targeting guides in English, German and Japanese) states that rule. [official] Help GHTRFDZRJPW6764R; Help GEXGZNBBWPZZK7P8; *A guide to targeting with Sponsored Products*
  - [opinion] Practitioners differ on the cross-campaign case (see *What practitioners add*): AMALYZE says Amazon chooses among duplicates "based on the highest expected bid and expected click-through rate (CTR)" and that duplicates "compete against themselves"; Ad Badger says two of a seller's products in different ad groups can both serve on one results page and "you will not be bidding against yourself".
  - [seat] The highest-bid rule as Amazon words it compares bids only. Amazon's auction page says ranking values "expected relevance" and that lower bids "can and do win". How the two combine for one advertiser's own duplicates is not published.

### R. Where targets serve beyond Amazon search: off-Amazon, prompts, Alexa for Shopping, Alexa+

- RULE (SP off-Amazon): "Your Sponsored Products campaigns can reach shoppers beyond Amazon, on premium sites, apps, and in creator content". The page's terms:
  - "Your ads run on the targeting, bid, and budget you already set — no extra setup required."
  - Availability: "Belgium, Brazil, Canada, Egypt, France, Germany, India, Ireland, Italy, Mexico, Netherlands, Poland, Saudi Arabia, Spain, Sweden, Türkiye, United Arab Emirates, United Kingdom, and the United States".
  - Settings: "Increase reach off-Amazon (default)" and "Limit reach to Amazon".
  - "Bid adjustments for Top of Search, Rest of Search, and Product Pages do not apply to off-Amazon placements."
  - "You can continue to optimize your campaigns with keywords and bids, just as you do on Amazon."

  [official] Help *Understand Sponsored Products off-Amazon advertising* (GYTD2Z3SYMAAMVXA, lastModified 2026-10-31), https://advertising.amazon.com/help/GYTD2Z3SYMAAMVXA. The overview page: "By default, Amazon extends your Sponsored Products cost-per-click campaigns to premium sites, apps, and creators using your existing campaign targeting, bid, and budget parameters." [official] Help *Understand Sponsored Products* (GJUCNANNV3GQVXJZ, lastModified 2026-10-20), https://advertising.amazon.com/help/GJUCNANNV3GQVXJZ
  - Bulksheets carry the setting as the column `Off-Amazon ad serving` for SP campaigns ("Availability: US", release note 2026-06-08). [official] Ads API *Release notes* (as above)
  - [seat] An SP keyword now buys more than search. Off Amazon there is often no typed query, so the "infer a search term from the context" rule (item B) is what applies. A keyword list's spend can include clicks the search term report shows under inferred terms. Placement reporting (`method/reporting.md`) separates "Off Amazon".
- RULE (prompts): "Prompts are an AI-powered extension to Sponsored Products and Sponsored Brands campaigns that help shoppers discover products through conversational experiences on Amazon." "Prompts are generated from brand-provided inputs (such as detail page, Brand Store, and campaign data)". "All existing and new Sponsored Products and Sponsored Brands campaigns in the US are automatically enrolled in prompts". "You can pause individual prompts at any time." [official] Help *Understand prompts on Sponsored Products and Sponsored Brands* (GLWNW26EWQZW46WZ, lastModified 2026-03-26), https://advertising.amazon.com/help/GLWNW26EWQZW46WZ
- RULE (Alexa+, 2025): "Sponsored products campaigns will now be automatically integrated into shopping conversations when customers chat with Alexa+ about products." (release note, 2025-07-15). [official] Ads API *Release notes* (as above)
- RULE (Rufus and Alexa+ merged into Alexa for Shopping, May 2026; re-read 2026-11-09 to settle a disagreement between files): "Amazon brings together Rufus and Alexa+ to create 'Alexa for Shopping' on the Amazon Shopping app and website", "available to U.S. customers on the Amazon Shopping app and website, and Echo Show devices" (2026-05-13). [official] aboutamazon *Meet Alexa for Shopping, your personalized, agentic AI assistant on Amazon*, https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant. The Ads page (2026-06-11, dateModified 2026-10-09): "Last month, Amazon brought together two powerful AI experiences—Rufus… and Alexa+… into a single, unified experience: Alexa for Shopping." "Existing sponsored ads campaigns are automatically eligible to serve in Alexa for Shopping… without additional campaign setup." Prompts "appear in shopping results and product pages, opening product-related conversations with Alexa for Shopping", and "Existing sponsored ads campaigns are automatically eligible to be optimized as a prompt." Separately, "On Alexa+… we have introduced Alexa+ Conversational Ads and Prime Video Sponsored Tiles"; for Alexa+ Conversational Ads, "Advertisers with sponsored ads campaigns are automatically enrolled." [official] Library news *What agentic shopping means for advertising*, https://advertising.amazon.com/library/news/agentic-shopping-advertising
  - [seat] On Amazon's own pages, since May 2026 Rufus is no longer a separate surface: the shopping assistant on the app and website is Alexa for Shopping. Alexa+ remains the name of the device assistant, where Alexa+ Conversational Ads run. The 2024 "Rufus-related placements" and 2025 Alexa+ release notes are dated history. `beyond/ad-products-and-eligibility.md` owns these surfaces.
  - [seat] Prompts, Alexa for Shopping and Alexa+ placements are reached by existing targets with no target of their own. How they match a target is not documented on the pages read.

## What practitioners add

Every item here is [opinion]: the named firm's or person's claim, stated as theirs. None was tested by this seat. Sample sizes are given where the source gives them.

**Match types and close variants**

- AMALYZE, *Broad, phrase, exact — match types, with the gotchas Amazon doesn't print* (undated), https://amalyze.com/resources/guides/advertising/amazon-ppc-keyword-match-types. AMALYZE says:
  - "Amazon applies close-variant matching at all three match types";
  - "You cannot turn close-variant matching off";
  - "even exact-match negatives sometimes do not fully block a search term";
  - "There is no negative broad".

  The last claim matches the help center and SB model, and not the SP 3.0 enum (item E).
- AMALYZE, *Close Variant — AMALYZE Glossary* (undated), https://amalyze.com/resources/glossary/close-variant. For an exact-match "running shoes", AMALYZE lists close variants as plural/singular, misspelling, **reordering** ("shoes running, shoes for running"), function word, stem/accent and hyphenation. It says "Amazon does not treat synonyms (sneakers, trainers) or category siblings (hiking shoes) as close variants under exact match" and "Amazon does not expose a switch. Negatives are the only lever."
  - AMALYZE's reordering claim sides with the keyword-targeting guide ("running shoes white") against the targeting guide ("same order").
  - AMALYZE's synonym claim conflicts with Amazon's own exact-match example, "outside lights" → "outdoor lights" (item B).
- Intentwise, *Unpacked: Sponsored Brands Search Term Report* (undated), https://www.intentwise.com/analytics-cloud/data-source/amazon-ads/sponsored-brands-search-term-report. Intentwise says that in SP "the only difference between broad match and phrase match terms is the word order". It says the search terms "always contain the same words". It says SB broad uses synonyms, and that adding "+" makes SB broad behave like SP broad.
  - This conflicts with Amazon's help page, which says SP broad "may include… synonyms, and related terms" and that "The keyword itself may not be contained in the customer shopping query" (item B).
  - [seat] The undated page may predate Amazon's 2026 wording.
- Parker-Lambert, *Amazon's Sponsored Products Are Behaving Differently* (2026-06-22, no author named), https://parker-lambert.com/news/amazons-sponsored-products-are-behaving-differently-heres-what-changed/. The firm says "Broad match is now prioritizing root category relevance over specific search term intent". Its evidence is one forum case ("5080 pc" matched to "desktop computer"). It recommends moving spend to phrase match.
  - [seat] One case is not a measured effect. It is consistent with Amazon's own text that broad match reads "the context of the advertised products".

**Automatic targeting**

- Ad Badger, Paul Haberlien, *Should You Segment Your 4 Auto-Targets in Amazon Ads?* (2021-07-09), https://www.adbadger.com/blog/amazon-ppc-education/should-you-segment-your-4-auto-targets-in-amazon-ads/. Haberlien says that in an unsegmented auto campaign "CM is getting all the traffic" (Close match), and that "all four ad types are blended in placement stats together". He recommends one auto campaign per targeting group, tested on the top 3–5 products, and warns of spreading budget thin.
- ClearAds Agency, *Amazon's Automatic Targeting Search Term Report* (2025-05-31), https://clearadsagency.com/amazon-reports/amazons-automatic-targeting-search-term-report/. ClearAds says "Amazon evaluates product title, bullet points, backend keywords, and sales data" for auto targeting, and that "Product titles, bullet points, and backend keywords should be optimised".
  - Amazon's own text names "titles and descriptions" (item F). Bullets and backend search terms are ClearAds' addition, not Amazon's statement.
  - The page also uses "quality score", a term no Amazon targeting page read today uses.

**Product targeting**

- Perpetua (originally Sellics), Angela Yuan, *How to Run Effective Amazon Product Targeting Campaigns* (2020-11-18), https://perpetua.io/blog-amazon-ppc-ads-product-targeting-campaigns. Placement shares for **one seller's account**, by targeting type:

  | Targeting type | Detail page | Other on Amazon | Top of search |
  |---|---|---|---|
  | Category | 91.7% | 6.1% | 2.1% |
  | ASIN | 84.9% | 7.7% | 7.4% |
  | Brand | 91.6% | 3.8% | 4.6% |
  | Auto | 88% | 11.5% | 0.5% |
  | Manual | 84.7% | 15% | 0.3% |

  No conversion data is given. Yuan recommends targeting competitors with lower ratings, fewer reviews or higher prices, using category targeting for new products, and running at least two weeks. The figures are for human readers only: one account, 2020, before expanded targeting and off-Amazon placements.
  - [seat] Amazon's own product recommendation theme "Similar items with low ratings and reviews" (<3 stars and/or <5 reviews; item J) builds the same idea into Amazon's recommender.
- JumpFly, Jennifer Gebhart, *Expanded Brand, Keyword, and Product Targeting on Amazon Ads* (2024-07-09), https://www.jumpfly.com/blog/expanded-brand-keyword-and-product-targeting-on-amazon-ads/. Gebhart says expanded product targets are updated daily, the "Expanded" box is checked by default, and both SB themes are added by default. She recommends SB broad modifiers such as "+pink+eraser". Her first two claims match Amazon's help (items G, I).

**Sponsored Brands themes**

- Perpetua help centre, Andrea Mamone, *Sponsored Brands Theme Targeting keywords* (2026-04-02), https://help.perpetua.io/en/articles/9202814-sponsored-brands-theme-targeting-keywords. Mamone says themes are added "by default to all new SBv4 campaigns" and "A bid is set at the theme-target level". She recommends pausing themes if their ACoS is poor.

**Keyword volume tools (third-party estimates)**

- Helium 10, Bradley Sutton, *Helium 10 vs. Jungle Scout Accuracy: Amazon Search Volume* (2024-08-23, modified 2024-10-01), https://www.helium10.com/blog/helium-10-vs-jungle-scout-search-volume-accuracy/. Sutton says Helium 10 used Amazon's internal search volume from 2018 and has estimated it from historical data since. He says Helium 10's volume is based on "normalized searches" (as Brand Analytics is) while SQP and Jungle Scout use "denormalized" searches, and "We show our monthly search volume as a "velocity" based on the most recent week's searches." On 31 keywords from one brand he sold, he scores Helium 10's keyword order against Brand Analytics' order at 93.5%, and Jungle Scout's order against SQP's at 41.9% ("13 out of the 31 in the correct order"); he also reports Jungle Scout's volumes 34.5% off SQP on average.
- Jungle Scout, Brian Connolly, *Jungle Scout vs. Helium 10* (2024-03-21), https://www.junglescout.com/resources/articles/jungle-scout-vs-helium-10/. Connolly compares against SQP search query volume. He reports Keyword Scout at a 10.93% difference and Helium 10 at −58.38%, on about 22 keywords from Jungle Scout's own dog pee pad brand.
  - [seat] Each vendor's test favours the vendor and uses one brand's keywords. Sutton benchmarks his own tool against Brand Analytics order and the rival against SQP; Connolly benchmarks both against SQP volume. The two results cannot both describe one tool. Third-party search volume is an estimate. Amazon publishes query volume in two places: SQP's `searchQueryVolume` (SP-API, Brand Registry, only queries where the brand already appeared) and Product Opportunity Explorer's niche search terms (Seller Central screen, no API, no Brand Registry named; item M). (Corrected in the gap fill of 2026-11-09: the earlier text named SQP as the only one.)

**Reverse-ASIN keyword tools (how a list of a competitor's keywords is built)**

- Helium 10, *Cerebro* tool page (dateModified 2026-03-09), https://www.helium10.com/tools/cerebro/. Helium 10 says: "Paste in your own or a competitor's ASIN to get a list of every keyword that product ranks for, both organic and paid"; "Analyze up to 10 ASINs side by side"; "Separate organic ranking keywords from sponsored ones"; filters by "organic rank, search volume, and title density". The page does not say how ranks are collected. How Helium 10 estimates volume is Sutton's article above.
- Jungle Scout, *Keyword Scout* feature page (dateModified 2025-01-24), https://www.junglescout.com/features/keyword-scout/. Jungle Scout says: "reverse-search competing ASINs for organic and sponsored keyword ranking data"; "Keyword Scout pulls millions of data points to show you exact and broad keyword search volumes"; "Analyze past keyword performance for up to two years"; "Reverse-search up to 10 ASINs"; and it shows "the cost-per-click for keywords in exact, broad, and headline search ads".
- DataDive's *Master Keyword List* (its support pages answered a Cloudflare 403; see *Unreachable*), as described by others:
  - EcomCrew, *DataDive Review and Case Study* (2024-10-30, modified 2025-01-21), https://www.ecomcrew.com/datadive-review-and-case-study/: "DataDive works by pulling data from the following sources…: Helium 10 Keepa Google Trends Amazon Seller Central"; "you really have to pay for Helium 10 to use all of DataDive's features because… it pulls data out of this tool"; the Master Keyword List shows "the keywords used by your competitors as well as the relevancy and search volume".
  - SellerSprite, *SellerSprite vs DataDive 2026* (2026-08-05; a rival vendor's page), https://www.sellersprite.com/en/blog/sellersprite-vs-datadive-2026: the MKL is "built from a 90-second "Dive" that auto-selects top competitor ASINs via Niche Dive" and "optimises itself by excluding non-relevant terms and eliminating duplicates". Of its own tool, SellerSprite says its "Reverse ASIN tool captures all keywords that drove a product into the top 3 pages of search results in the past 30 days", "Up to 20 ASINs can be reversed simultaneously", and its "ABA Reverse ASIN function adds Brand Analytics data… when Brand Registry is in place".
  - [seat] On these vendors' own descriptions, a reverse-ASIN list is the set of queries for which the tool observed the ASIN ranking (organically or in a sponsored slot) in a window, with the tool's own volume estimate attached. DataDive builds on Helium 10's data rather than its own, on EcomCrew's account. None of these is an Amazon figure. Amazon's nearest first-party equivalents are the advertiser's own search term report (queries that drew a click on its ads), SQP (queries where its brand appeared) and POE (a niche's top queries).

**Product Opportunity Explorer as practitioners read it**

- AMALYTIX, Trutz Fries, *Product Opportunity Explorer: Find and Validate Niches* (2022-01-06, modified 2026-10-26), https://www.amalytix.com/en/knowledge/controlling/amazon-product-opportunity-explorer/. Fries says: "Amazon does not list Brand Registry as a requirement, only the Professional selling plan"; the niche page has "five tabs below: Insights and trends, Products, Search terms, Customer Review Insights and Returns (as of October 2026)"; Insights "sums up the niche in 20 data points, each for today, the last 90 and the last 360 days"; "The Search Terms tab of a niche has a download button"; and "Find opportunities in" also includes "the Netherlands, Poland, Sweden, Belgium and Ireland (as of October 2026)".
- Intentwise, *Amazon Product Opportunity Explorer* data-source page (undated), https://www.intentwise.com/analytics-cloud/data-source/amazon-seller/product-opportunity-explorer. Intentwise gives "search volume (over the past 360 days)…, search conversion rate (over the past 360 days), click share (over the past 360 days)", and says the report "is available to Professional Sellers on Amazon US, Germany, France, Spain, and Italy" and "not available for sellers with the Basic or Individual selling plans".
- Goat Consulting, Eric Sutton, *Tips Using Amazon's Product Opportunity Explorer* (2022-01-13, modified 2026-04-01), https://www.goatconsulting.com/blog/product-opportunity-explorer-keyword-and-market-research-for-selling-on-amazon. Sutton lists "Search Volume in the past 90 days" and "Click Share (Past 90 Days)" and says "There currently is no excel format export option".
- AMALYZE glossary *Product Opportunity Explorer (POE)* (undated), https://amalyze.com/resources/glossary/product-opportunity-explorer, says POE is "available to Brand Registry sellers and vendors".
  - Where they disagree: AMALYTIX says Brand Registry is not required, AMALYZE says it is for Brand Registry sellers, and Amazon's pages name only a Professional selling account. Intentwise gives 360-day windows and Goat 90-day windows, and AMALYTIX says the screen shows today, 90 and 360 days. AMALYTIX (October 2026) lists more marketplaces than Intentwise, and AMALYTIX reports a download button where Goat's older text said there was no export. [seat] The windows and the marketplace list are screen facts that change; Amazon's guide states neither.

**Self-competition between one advertiser's own targets**

- AMALYZE, *Duplicate Keywords in Amazon PPC: Why They Bleed Budget and How to Clean Them Up* (undated), https://amalyze.com/blog/duplicate-keywords-ppc. AMALYZE says: "Amazon's internal auction logic must choose which of your identical targets to serve. This choice is based on the highest expected bid and expected click-through rate (CTR)"; "The instance with the highest bid is likely winning the auction, while the lower-bid duplicates sit idle or occasionally "steal" an impression when the primary campaign runs out of budget"; and for match types, "the match type with the highest expected bid (adjusted for CVR and CTR) will generally be used". The CTR and CVR adjustment is AMALYZE's addition; Amazon's help sentence names the highest bid only.
- Ad Badger ("The Badger"), *Amazon PPC Keyword Cannibalization: When It Hurts & How to Fix It* (2024-09-12, modified 2026-06-24), https://adbadger.com/blog/keyword-cannibalization-and-placement-in-amazon-ppc/. Ad Badger says: "Whenever two of your products are shown in Sponsored Product placements for a particular SERP, you will not be bidding against yourself"; "In order to have two products appear as Sponsored Products for a search, these products have to be in different ad groups"; and "because of the stock Amazon gives to proven products, your CPC for each product may be different".
  - Where they disagree: AMALYZE describes Amazon choosing one of a seller's identical targets; Ad Badger describes several of a seller's products serving on one results page from different ad groups. The two can both hold if Amazon picks one target per advertised product and ad group, but no Amazon page read states that.

**Japanese and German matching, from practitioners**

- ECのミカタ (an agency column), *【広告】Amazon広告を最適化！キーワードマッチタイプの基本ガイド！* (2023-07-18, modified 2024-12-17), https://ecnomikata.com/column/39736/. Its examples write Japanese keywords with a space between words ("「スニーカー メンズ」"): under broad it says the keyword also shows for "「スニーカー」「メンズ」のような単体キーワード" and any word order; under phrase "「ナイキ スニーカー メンズ 」" and similar, "２つの連続したキーワードが一致していた場合は前後に別のキーワードがある状態で検索されたとしても表示されます". It says phrase match has no "類義語や関連用語まで補完する機能". It does not address hiragana/katakana, width variants, or unspaced queries.
- AMALYZE's *Close Variant* glossary (above) lists "Hyphenation running-shoes" and "Stem / accent" among close variants. AMALYZE does not mention German compounds.
- No reachable JP or DE practitioner page read on 2026-11-09 reports a test of how negative phrase or negative exact treat hiragana/katakana/kanji spellings, full-width against half-width characters, unspaced against spaced Japanese, or a German compound against its split form. The SellerSprite Japanese negative-keyword guide served only its title to a plain GET and to a fetch tool, and MarkeZine's article answered a bot check (*Unreachable*). [seat] Amazon's own search research (item N) says its Japanese query stack normalises these cases for search Ads matching. Whether an advertiser's negative exact keyword is applied before or after that normalisation is not stated anywhere read.

**Pages not reachable or not opened, from practitioners**

- Search Engine Land's match-type article, the Helium 10 match-type page, Teikametrics' product-targeting page and Pacvue's match-type page could not be read (see *Pages read*, Unreachable).
- Karooya and BidX were cited in the prior paid-keywords research and were not re-opened today, so their claims are not carried here.

## Published research

- [research] Nigam, Song, Mohan, Lakshman, Ding et al., *Semantic Product Search*, KDD 2019 (arXiv 1907.00937, 2019-07-01), https://arxiv.org/abs/1907.00937. The authors are Amazon researchers.
  - "Pure lexical matching via an inverted index falls short… due to several factors: a) lack of understanding of hypernyms, synonyms, and antonyms, b) fragility to morphological variants (e.g. "woman" vs. "women"), and c) sensitivity to spelling errors."
  - The model is trained "using customer behavior data". Its loss function separates "random negative examples, impressed but not purchased examples, and positive examples (purchased items)".
  - Offline it reports "at least 4.7% improvement in Recall@100 and 14.5% improvement in mean average precision (MAP)" over baseline semantic search methods. The paper also reports online tests.
  - [seat] The three failure modes it names (synonyms, morphology, misspelling) are the ones Amazon's help page says all match types "account for". This paper is a published description of why Amazon's matching is not literal string matching. It does not describe the ads matcher itself.
- [research] Chang, Jiang, Yu, Teo, Zhang, Zhong et al., *Extreme Multi-label Learning for Semantic Matching in Product Search*, KDD 2021 (arXiv 2106.12657, 2021-06-23), https://arxiv.org/abs/2106.12657.
  - Its setting: "given a customer query, retrieve all semantically related products from a huge catalog of size 100 million, or more".
  - Lexical methods such as BM25 "fail to capture behavioral signals between queries and products".
  - A tree-based XMC model "maintains a low latency of 1.25 milliseconds per query and achieves a 65% improvement of Recall@100 (60.9% v.s. 36.8%) over a competing embedding-based DSSM model".
- [research] Reddy, Màrquez, Valero, Rao, Zaragoza, Bandyopadhyay et al., *Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search* (arXiv 2206.06588, 2022-06-14), https://arxiv.org/abs/2206.06588. The data is at https://github.com/amazon-science/esci-data.
  - The dataset has "around 130 thousand unique queries and 2.6 million manually labeled (query,product) relevance judgements". It is "multilingual with queries in English, Japanese, and Spanish".
  - The README gives "up to 40 potentially relevant results" per query.
  - Task 2 is to classify "each product as being an Exact, Substitute, Complement, or Irrelevant match for the query".
  - [seat] Amazon's research labels (Exact, Substitute, Complement, Irrelevant) mirror the auto-targeting split into query-close, substitutes and complements. The paper does not say the ads system uses these labels. The full label definitions are in the PDF, which this seat could not read (see Unreachable).
- [research] Yu et al., *COSMO: A large-scale e-commerce common sense knowledge generation and serving system at Amazon*, SIGMOD/PODS 2024, https://www.amazon.science/publications/cosmo-a-large-scale-e-commerce-common-sense-knowledge-generation-and-serving-system-at-amazon.
  - Existing e-commerce knowledge graphs "fail to discover user intentions". COSMO mines "user-centric commonsense knowledge from massive behaviors" using LLM-distilled assertions.
  - "COSMO has been deployed in Amazon search applications such as search navigation. Both offline and online A/B experiments demonstrate our proposed system achieves significant improvement."
  - [seat] It is evidence that Amazon search reads intent ("why a shopper wants this") beyond query words. It is not evidence about ad matching.
- [research] Amaldoss, Jerath & Sayedi, *Keyword Management Costs and "Broad Match" in Sponsored Search Advertising*, *Marketing Science* 35(2):259–274 (2016), doi 10.1287/mksc.2015.0919. Read via EconPapers, https://econpapers.repec.org/RePEc:inm:ormksc:v:35:y:2016:i:2:p:259-274, and IDEAS, https://ideas.repec.org/a/inm/ormksc/v35y2016i2p259-274.html (abstract only).
  - The authors name "keyword management costs". In a game-theoretic model, broad match benefits advertisers when its bid accuracy is high, and they avoid it when accuracy is very low.
  - At moderate accuracy, each advertiser gains by adopting broad match, but when all adopt it competition erodes profits, "thus creating a 'prisoner's dilemma.'"
  - The model also predicts that a search engine improves broad-match accuracy only up to the point where advertisers adopt it.
  - [seat] This is a theory paper about web search engines, not a measurement on Amazon. Its mechanism (the platform bids on the advertiser's behalf across queries the advertiser did not choose) describes Amazon's broad match, auto targeting, themes and keyword groups alike.
- [research] Ghose & Yang, *An Empirical Analysis of Search Engine Advertising: Sponsored Search in Electronic Markets*, *Management Science* 55(10):1605–1622 (2009). Read via EconPapers, https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:10:p:1605-1622 (abstract only). The data is a six-month panel of several hundred keywords from one large US retailer on **Google**.
  - "conversion rates are highest at the top and decrease with rank as one goes down the search engine results page".
  - "profits are often higher at the middle positions than at the top or the bottom ones".
  - [seat] The published abstract does not state the keyword-length or brand-term effects that working-paper versions report. Those are not carried here.
  - Other studies find conversion rising with position or lower down, and one finds naive position estimates biased; see *Position and conversion rate* below.
- [research] Simonov, Nosko & Rao, *Competition and Crowd-Out for Brand Keywords in Sponsored Search*, *Marketing Science* 37(2):200–215 (2018), doi 10.1287/mksc.2017.1065. Read via EconPapers, https://econpapers.repec.org/RePEc:inm:ormksc:v:37:y:2018:i:2:p:200-215 (abstract only). The setting is web search (Bing), not Amazon.
  - With no competitors present, a brand's own ad has an effect of 1%–4%, smaller for larger brands.
  - Competitors in paid positions 2–4 can "steal" 1%–5% of the focal brand's clicks.
  - Where the brand does not advertise and competitors do, they "steal" 18%–42%.
  - "the return on investment on defensive advertising to be strongly positive."
  - The defence question is `beyond/brand-defense-and-competition.md`'s. It is recorded here only because brand keywords are a target class.

**Position and conversion rate: four results that do not agree, and why (added 2026-11-09; `areas/bids-and-placements.md` owns placement)**

All four are on web search engines, not Amazon. Abstracts read through OpenAlex on 2026-11-09.

- [research] Ghose & Yang (*Management Science* 2009, above; doi 10.1287/mnsc.1090.1054): a hierarchical Bayesian simultaneous-equations model on a six-month Google panel of one retailer's keywords finds "conversion rates are highest at the top and decrease with rank", and "profits are often higher at the middle positions".
- [research] Rutz, Bucklin & Sonnier, *A Latent Instrumental Variables Approach to Modeling Keyword Conversion in Paid Search Advertising*, *JMR* 49(3):306–319 (2012), doi 10.1509/jmr.10.0354. On "keyword-level paid search data containing daily information on impressions, clicks, and reservations for a major lodging chain", with a latent instrumental variable for "the endogenous position", "They find that higher positions increase both the click-through and conversion rates. When advertisements are served in higher positions, approximately one-third of new conversions is due to increased click-through while approximately two-thirds are due to increased conversion rates."
- [research] Agarwal, Hosanagar & Smith, *Location, Location, Location: An Analysis of Profitability of Position in Online Advertising Markets*, *JMR* 48(6):1057–1073 (2011), doi 10.1509/jmr.08.0468. From "a field experiment for several keywords from an online retailer's ad campaign" and a hierarchical Bayesian model: "while click-through rate decreases with position, conversion rate increases with position and is even higher for more specific keywords", so "the topmost position is not necessarily the revenue-or profit-maximizing position". "Position" here is the rank number, so "increases with position" means conversion rate rises lower on the page.
- [research] Narayanan & Kalyanam, *Position Effects in Search Advertising and their Moderators: A Regression Discontinuity Approach*, *Marketing Science* 34(3):388–407 (2015), doi 10.1287/mksc.2014.0893. "Because positions are determined through an auction, there are significant selection issues in measuring position effects. A simple mean comparison of outcomes at two positions is likely to be biased", and "experimentation is rendered difficult… by competitors' bidding behavior, which induces selection biases that cannot be eliminated by randomizing the bids for the focal advertiser." Their regression-discontinuity estimates of effects on click-through and sales orders are "much smaller, and exist only in some of the positions". Effects are "stronger when the advertiser is smaller, and when the consumer has low prior experience with the keyword", and "weaker when the keyword phrase has specific brand or product information, when the ad copy is more specific as in exact matching options".
- [seat] The disagreement is between settings and methods, not a contradiction within one dataset: a retailer on Google with a structural model (top converts best), a lodging chain with a latent instrument (higher positions raise conversion), a retailer's bid experiment (conversion rises lower down), and an RD design that finds the naive position effects inflated by selection. Narayanan & Kalyanam's point applies to the observational results and, by their argument, to randomizing one's own bids as well. Amazon's placements (top of search, rest of search, product pages, off Amazon) are not numbered text-ad slots. No published study read measures conversion by Amazon placement causally. Amazon's own placement report compares placements across self-selected bids (`areas/bids-and-placements.md`).

**Does retargeting work? Field experiments behind SD views and purchases remarketing (added 2026-11-09)**

None of these is on Amazon. Abstracts read through OpenAlex on 2026-11-09.

- [research] Lambrecht & Tucker, *When Does Retargeting Work? Information Specificity in Online Advertising*, *JMR* 50(5):561–576 (2013), doi 10.1509/jmr.11.0503 (also registered as 10.1177/002224371305000508). A field experiment by "an online travel firm" compares dynamic retargeted ads ("ads with images of those same products") with "generic brand ads". "Surprisingly, the data suggest that dynamic retargeted ads are, on average, less effective than their generic equivalents. However, when consumers exhibit browsing behavior that suggests their product preferences have evolved (e.g., visiting review websites), dynamic retargeted ads no longer underperform." Their explanation is that preferences are "initially construed at a high level".
- [research] Sahni, Narayanan & Kalyanam, *An Experimental Investigation of the Effects of Retargeted Advertising: The Role of Frequency and Timing*, *JMR* 56(3):401–418 (2019), doi 10.1177/0022243718813987. A "large-scale randomized field experiment" with "an online seller of home-improvement products": "retargeting causes 14.6% more users to return to the website in four weeks"; "The impact of advertising decreases as the time since the consumer first visits the website increases. 33% of the effect of first week's advertising occurs on the very first day"; and "the effect of advertising in week 2 of the campaign is higher when the user was assigned to a non-zero level of advertising in week 1."
- [research] Bleier & Eisenbeiss, *Personalized Online Advertising Effectiveness: The Interplay of What, When, and Where*, *Marketing Science* 34(5):669–688 (2015), doi 10.1287/mksc.2015.0930. Two field and two lab experiments: "banners with a high degree of content personalization (DCP) are most effective when a consumer has just visited the advertiser's online store, but quickly lose effectiveness as time passes since that last visit. We call this phenomenon overpersonalization. Medium DCP banners… outperform high DCP banners over time." On view-through, "personalization increases ad effectiveness only on motive congruent websites, but decreases it on incongruent websites."
- [research] Johnson, Lewis & Nubbemeyer, *Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness*, *JMR* 54(6):867–884 (2017), doi 10.1509/jmr.15.0297. With a "Ghost Ads" control on "an online retailer's display retargeting campaign": "retargeting can work as the ads lifted website visits by 17.2% and purchases by 10.5%."
- [seat] Transfer to SD: the measured lifts are causal estimates from randomized holdouts on one advertiser each; they show retargeting *can* be incremental, not that a given SD remarketing line is. Three findings map onto SD settings: effect decays with time since the visit (Sahni et al.; Bleier & Eisenbeiss), which bears on the 7–90 day views lookbacks (item L); showing the exact viewed product can underperform a generic ad early in the decision (Lambrecht & Tucker; "overpersonalization" in Bleier & Eisenbeiss), which bears on `views(exactProduct …)` against `views(similarProduct …)` or category audiences; and placement context changes view-through effects (Bleier & Eisenbeiss), which bears on SD's on- and off-Amazon serving. SD audiences already "exclude past customers who purchased your advertised products or similar products in the past 30-day window" (item L). How SD incrementality is measured is `beyond/metrics-and-attribution.md`'s and `method/change-measurement.md`'s.

**Japanese query normalisation in Amazon's search Ads matching (added 2026-11-09)**

- [research] Zhang, Huang, Deng, Xiao, Mittal & Deng (Amazon), *Towards Scalability and Extensibility of Query Reformulation Modeling in E-commerce Search*, CIKM 2024, arXiv 2402.11202 (v2, 2024-10-02), https://arxiv.org/abs/2402.11202. "In Amazon product search, query reformulation has displayed its effectiveness in improving search relevance and bolstering overall revenue." For "non-English and low-traffic markets" the pipeline includes "stop word removal, stemming, script type normalization (e.g., translation between different spellings of the same word, as illustrated by "こども" to "子供" in the Japanese case), tokenization (e.g., converting "子供マスク不織布" to "子供_マスク_不織布"), and token sorting", and it "excludes the handling of identified named entities, such as brands or media titles". In the "product search Ads matching" application, "In our experiment performed in Japanese market, we included the Ads matched for" the reformulations "directly into the match set" of the query; the abstract reports "a 0.36% increase in Ads revenue in the Japanese case".
  - [seat] This is the one published Amazon text read that ties Japanese spelling, spacing and order variants to Ads matching. It describes a production experiment in 2024, not the semantics of an advertiser's match types or negatives today.
- Leads not opened:
  - the Amazon Science page *Improving relevance quality in product search using high-precision query-product semantic similarity*;
  - arXiv 1607.01869 on semantic matching of queries to ads;
  - Rutz & Bucklin (2011, *JMR*);
  - Blake, Nosko & Tadelis (2015) and Moshary (2025), cited in the prior paid-keywords research.

  None is cited for any claim.

## Stable enough for a skill

Each item is a definition or rule stated by Amazon on a current page, consistent across the pages that state it, and not a figure.

1. SP manual keyword match types are broad, phrase and exact. All three "account for plurals, misspellings, and translations". Phrase and exact also cover acronyms. Broad also covers synonyms and related terms judged by "the context of the advertised products". (Help *Understand keyword match types*; Help *Set up keyword targeting*; v1 `KeywordMatchType`.)
2. Exact match in SP is not literal: Amazon's own example maps "outside lights" to "outdoor lights". (Help *Understand keyword match types*.)
3. A keyword's match type cannot be changed after creation; a keyword in another match type can be added. A negative keyword's match type cannot be changed. (Help *Understand keyword match types*; Help *Add negative keywords or negative products targeting*.)
4. When one keyword is in several match types with different bids, the highest-bid match type is used for a matching query. (Help *Understand keyword match types*.)
5. Amazon infers a search term from context when no search term exists, and serves keywords there. SP keywords also serve on detail pages, elsewhere on Amazon and off Amazon. (Help *Understand keyword match types*; Help *Understand targeting*; Help *Understand Sponsored Products off-Amazon advertising*.)
6. SB keyword matching adds semantic matching; SB supports the `+` broad match modifier; SB negatives are exact and phrase only. (Help *Understand targeting*; Help *Understand keyword match types*; SB v3 model.)
7. Auto targeting is SP-only and has exactly four groups. Close and loose are query groups; substitutes and complements are detail-page groups. Each can be bid and paused separately, and none can be created manually. (Help *Understand keyword match types*; SP 3.0 model; Ads API guide *Auto targeting*.)
8. A product target is one ASIN per clause, exact or expanded. Expanded is the console default, adds a limited set of related products updated daily, and reports with a "Product-expanded" prefix. (Help *Set up product targeting*; Ads API guide *Sponsored Products product targeting overview*.)
9. Category refinements require the category. SP and SD refine by brand, price, rating, Prime shipping, age range (toys) and genre (books). SB refines by brand, price and rating only. (Help *Set up product targeting*; SP 3.0, SB v3, SD v3 models.)
10. Negative product targets block detail pages by ASIN or brand. They affect product targets and auto targets in their scope (ad group or campaign). (Help *Add negative keywords or negative products targeting*.)
11. Keyword groups are a beta, US-only SP target that cannot share an ad group with product targets. (Ads API guide *Sponsored Product keyword groups targeting*.)
12. SB theme targets are "keywords related to your brand" and "keywords related to your landing pages", one of each per ad group. A goal-based SB campaign creates them by default and its `smartDefault` cannot be edited. (SB v3 model; Ads API guide *Get started with Sponsored Brands campaigns*.)
13. Keyword recommendation `rank` is an order by clicks, conversions or a default Amazon calls its internal ranking mechanism. The response carries no search volume. Translations in it do not target. (SP 3.0 model.)
14. Search Term Impression Share is account-wide per search term. It is available only for terms where the account had ad impressions, and is incompatible with campaign and ad group grain. (Help *SIS report*; SP 3.0 model; v1 *Search (Impression share)*.)
15. Search term reports include only impressions that led to at least one click. (Ads API guide *Search term reports*.)
16. Targets must be relevant to the advertised product. Restricted targets may be accepted at creation but do not serve. (Help *Understand targeting*; moderation guide.)
17. Ad creative may not name a competitor. Reserve-SOV keywords may not contain another company's brand or trademark. No Amazon page read states a rule for other companies' trademarks as auction keywords. (Moderation guide; Help *Prohibited content and products for Amazon O&O supply*; Help *Branded keyword guidelines and keyword suspension*.)
18. SD audiences exclude purchasers of the advertised or similar products in the past 30 days. Views remarketing goes up to 90 days and purchases remarketing up to 365. (Help *Understand targeting in Display campaigns*; Help *Understand remarketing audience segments*.)
19. SD contextual targets with refinements, or single products, serve on Amazon only. Unrefined categories and "similar to advertised products" also serve off Amazon. (Help *Understand contextual targeting in Display*.)
20. The SD "similar to advertised products" target is added automatically in the console but must be created explicitly through the API. (Ads API guide *Sponsored Display dynamic segments overview*.)
21. The translated keyword is what targets. Native-language fields are for reporting only. (Help *Keyword translation*; Ads API guide *Keyword targeting overview*.)
22. Amazon's auction values expected relevance, and "ads with lower bid amounts, but higher relevance to the customer, can and do win". (Help *Understand Amazon Ads auctions*.)
23. An SD `audience(audienceSameAs=…)` target, an SP `shopperCohortBidding` segment and an SB audience boost each take an `audienceId` that Amazon lists through a discovery call: the Audiences API (`/audiences/taxonomy/list`, `/audiences/list`, `adType` SD or DSP) for SD, and the Targetable Entities API (`/targetableEntities/list`, by `adProduct`, `targetTypeFilter` and `pathsFilter`) for SP and SB. SD `views(…)` and `purchases(…)` clauses take ASINs or categories and a lookback, not an audience id. (OpenAPI models *Audiences*, *Targetable Entities*, *Sponsored Products 3.0*, *Sponsored Display v3*; Ads API guides *Sponsored Display audience targeting* and *Shopper cohort bidding*.)
24. Product Opportunity Explorer groups search terms into niches "based on the products customers view or purchase after searching", and shows each niche's top search terms with search volume, click share and search conversion rate. It is a Seller Central screen; the SP-API's Customer Feedback API carries its review and return insights but no search terms. (*Product Opportunity Explorer overview*; sell.amazon.com blog; SP-API *Customer Feedback v2024-06-01*.)
25. Rufus and Alexa+ were brought together as Alexa for Shopping in the US in May 2026; existing sponsored ads campaigns are automatically eligible to serve there, and Alexa+ Conversational Ads enrol advertisers automatically. (aboutamazon *Meet Alexa for Shopping*; *What agentic shopping means for advertising*.)
26. Auto collections in Sponsored Brands take keyword targeting only; manual collections take keyword or product targeting. (Help *Migrate from Product collections to Sponsored Brands collections*.)

## What cx must read at run time

The figure or state, and where it lives. Every item here changes, or differs by account or marketplace.

| What | Where (read operation or page) | Why it is not a constant |
|---|---|---|
| A target's exact expression and match type (exact versus expanded, which predicates, which theme) | `POST /adsApi/v1/query/targets`; SP 3.0 `/sp/targets/list`, `/sp/keywords/list`; SB `GET /sb/keywords`, `/sb/targets/list`, `/sb/themes/list`; SD `GET /sd/targets` (or `/sd/targets/extended`) | The console defaults (expanded; SB themes; SD similar products) differ from the API defaults |
| Minimum and maximum bid for the profile's marketplace and ad type | Ads API *Limits* page on the day; the write's per-item error | Published table with known errors (EG); changes by marketplace |
| Keyword text limits and valid characters for the marketplace | Ads API *Limits* page; the write's per-item error | Script and symbol rules differ by marketplace; library guide conflicts |
| Keyword recommendations, their rank, share and rank-of-share | `POST /sp/targets/keywords/recommendations` (v3–v5 content types); `POST /sb/recommendations/keyword` | Recomputed; 30-day (SP) versus 7-day (SB) windows |
| Product, category and brand recommendations | `POST /sp/targets/products/recommendations`; `/sp/targets/categories/recommendations`; `/sp/targets/category/{id}/refinements`; `/sp/targets/products/count`; SB `/sb/recommendations/targets/*`; SD `/sd/targets/recommendations` | Recomputed; per ASIN |
| The category tree | `GET /sp/targets/categories`; SB `/sb/targets/categories` | Catalog changes; marketplace scope not stated |
| Keyword groups available for the ASINs | `POST /sp/targeting/recommendations/keywordGroups` | Beta, US-only on 2026-11-09 |
| Negative brand candidates | `GET /sp/negativeTargets/brands/recommendations`; `/sp/negativeTargets/brands/search` | Recomputed |
| Whether a target type or theme is accepted in this marketplace and ad product | The create call's per-item result (207 `success`/`error`); theme-based bid recommendations' 422 | Availability is marketplace-specific and changing (keyword groups, themes, campaign-level negative product targets for sellers) |
| The recommendation types Amazon offers | `GET /adsApi/v1/list/recommendations`; Ads API guide *Recommendation types*; the older tactical surface `POST /recommendations/list` | "updated as new recommendation types launch" |
| Branded keywords for reserve share of voice, and whether a keyword can be reserved | `POST /adsApi/v1/create/recommendations/sb` (`BRANDED_KEYWORD`); `POST /adsApi/v1/create/keywordReservationValidations/sb` | Validation is per keyword and per brand mapping |
| Which SB ads are legacy product collections due for migration | `POST /sb/v4/migrations/list` | Amazon gives two end dates: creates "will return an error" "Post January 2027" (*Deprecations*, API migration guide) and "Beginning February 2027, product collections will no longer be supported" (ListMigrations note 2026-09-18; help GV7N6KZTH4HF4T2P); creates map to Manual Collection from August 2026 |
| Audience ids for an SD `audience(audienceSameAs=…)` target, with taxonomy and overlap | `POST /audiences/taxonomy/list` (body `adType: SD`, `categoryPath`, `countries`); `POST /audiences/list` (`adType: SD`; filters `audienceName`, `category`, `categoryPath`, `audienceId`, `status`; `canTarget=true`); `GET /insights/audiences/{audienceId}/overlappingAudiences?adType=SD` | Audience catalog, status and reach forecasts change; ids differ by country |
| Audience ids for SP `shopperCohortBidding` and SB audience boosts (Amazon-built and AMC), and SD content categories | `POST /targetableEntities/list` with `adProduct` (`SPONSORED_PRODUCTS`/`SPONSORED_BRANDS`/`SPONSORED_DISPLAY`), `targetTypeFilter: [AUDIENCE]` (or `CONTENT_CATEGORY`), `pathsFilter` `[["Audience Category","Custom-built","Product"]]` or `…"AMC"]]`; `POST /targetableEntities/paths/list` to walk the tree | AMC audiences are the advertiser's own; Amazon-built audiences per product and marketplace |
| Which SB model holds a targeting path | SB v3 YAML: `/sb/keywords`, `/sb/negativeKeywords`, `/sb/targets`, `/sb/negativeTargets`, `/sb/themes`; *Sponsored Brands 3.0* JSON and SB v4 JSON: `/sb/targets/categories`, `/sb/targets/products/count`, `/sb/negativeTargets/brands/recommendations` (`application/vnd.sbtargeting.v4+json`) | Amazon splits SB across three published models |
| A niche's top search terms with volume, click share and search conversion rate | Seller Central → Growth → Product Opportunity Explorer (screen only; no API read on 2026-11-09). Review and return insights: SP-API Customer Feedback API `getItemReviewTopics`, `getItemReviewTrends`, `getItemBrowseNode`, `getBrowseNodeReviewTopics`, `getBrowseNodeReviewTrends`, `getBrowseNodeReturnTopics`, `getBrowseNodeReturnTrends` (US, UK, FR, IT, DE, ES, JP; weekly) through `cx-amazon-sp-api` | Niches refresh weekly and new ones monthly; marketplace list and windows not stated by Amazon |
| A competitor ASIN's organic and sponsored keywords | Third-party reverse-ASIN tools (Helium 10 Cerebro, Jungle Scout Keyword Scout, DataDive, SellerSprite), outside the Ads API; the nearest first-party reads are the advertiser's own search term report, SQP and POE | Vendor estimates; collection method not published |
| Search terms that matched each target | SP/SB search term report (v3 `spSearchTerm`/`sbSearchTerm`, or v1 equivalent); SD `matchedTarget` | Account data; only clicked impressions |
| Search term impression share and rank | SIS report; v1 `metric.impressionShare`/`impressionShareRank` | Account data; 30-day and 90-day windows |
| Brand Analytics Top Search Terms and SQP | Seller Central Brand Analytics, or SP-API reports `GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT` / `…SEARCH_QUERY_PERFORMANCE_REPORT` | Needs Brand Registry and the Brand Analytics role; outside the Ads API. Whether cx can read them is `method/ads-api-surface.md`'s door question |
| Keyword translation and localization | Localization API `POST /keywords/localize`, `/targetingExpression/localize`, `/products/localize` | The help page's language table dates from 2022 |
| Restricted targets in the advertiser's category | Delivery on the target after creation (`areas/diagnosis.md`) | Amazon does not publish a full restricted-keyword list |
| Policy text | Help *Policies and guidelines* tree and *Ad policy change log* | Edited in 2025–2026 |
| Whether an SP campaign serves off Amazon | Campaign setting ("Increase reach off-Amazon (default)" / "Limit reach to Amazon"); placement report "Off Amazon" | Default on in 19 named countries |

## Pages read

All pages were read 2026-11-09 by plain GET, unless a row says otherwise. Help-center pages were read from the article JSON the page serves; their `lastModified` is given where it was returned.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Understand keyword match types (lastModified 2026-07-29) | https://advertising.amazon.com/help/GHTRFDZRJPW6764R | official, help | 2026-11-09 | Match-type definitions and examples; highest-bid rule; inferred search term; SB BMM; four auto groups; negative limits |
| Set up keyword targeting (2026-11-02) | https://advertising.amazon.com/help/GK3MNACNTXG659J9 | official, help | 2026-11-09 | 25 keywords; per-match-type bids; SB phrase semantic; IS/IR definitions |
| Set up product targeting (2026-02-20) | https://advertising.amazon.com/help/GB2JECV9CJK6R6AL | official, help | 2026-11-09 | Refinements by ad product; expanded product targeting |
| Add negative keywords or negative products targeting (2026-10-20) | https://advertising.amazon.com/help/GTEHPEG5BXY9UX5W | official, help | 2026-11-09 | Negative phrase/exact; negative products scope; 72h/96h |
| Understand targeting (2026-07-29) | https://advertising.amazon.com/help/G3XAU5G7C2JTNQTM | official, help | 2026-11-09 | Auto vs manual; SP keywords off Amazon; SB semantic table; restrictions |
| Targeting in Sponsored ads (2026-02-24) | https://advertising.amazon.com/help/GTHQHRYZGUZF7ZHX | official, help index | 2026-11-09 | The targeting article list |
| Branded keyword guidelines and keyword suspension (2025-11-05) | https://advertising.amazon.com/help/G2QZJUGUT4RGLJ6N | official, help | 2026-11-09 | Reserve-SOV keyword rules and rejection reasons, including trademarks |
| Keyword translation (2022-09-20) | https://advertising.amazon.com/help/GHPTCVTGNFZ2KTSP | official, help | 2026-11-09 | Translation method, limits, language table |
| Reserve keywords in a Sponsored Brands campaign (2026-07-07) | https://advertising.amazon.com/help/G86SD7HK6NHHRB9B | official, help | 2026-11-09 | Reserve SOV terms (5–1,000 keywords, 15–92 days, $3,000, not Spain) |
| Search Term Impression Share (SIS) report (2026-02-24) | https://advertising.amazon.com/help/G7AQQUSFVZPAAXEU | official, help | 2026-11-09 | SIS definition, 30-day share, 90-day lookback |
| Understand targeting in Display campaigns (2026-03-19) | https://advertising.amazon.com/help/GPKPWTLW6B8T683N | official, help | 2026-11-09 | Audience types; sellers vs non-sellers; 30-day purchaser exclusion |
| Understand contextual targeting in Display (2026-05-01) | https://advertising.amazon.com/help/GNTK7LTYZS3KSTAN | official, help | 2026-11-09 | On/off-Amazon by refinement; 10 products tip; relevancy guardrails |
| Understand remarketing audience segments (2026-10-23) | https://advertising.amazon.com/help/G82GQS569JWSVNRB | official, help | 2026-11-09 | Views ≤90, purchases ≤365; dynamic segments |
| Set up multi-signal targeting (2026-07-01) | https://advertising.amazon.com/help/GDTFJ44CQ2QUKX9X | official, help | 2026-11-09 | Contextual folded into multi-signal; limits; policy-restricted items contextual-only |
| Set up targeting (2026-07-27) | https://advertising.amazon.com/help/G7A36P2ZEMPT7N73 | official, help | 2026-11-09 | Ads Agent targeting suggestions; country exclusions |
| Understand Sponsored Products off-Amazon advertising (2026-10-31) | https://advertising.amazon.com/help/GYTD2Z3SYMAAMVXA | official, help | 2026-11-09 | Off-Amazon by default; 19 countries; adjustments not applied |
| Understand Sponsored Products (2026-10-20) | https://advertising.amazon.com/help/GJUCNANNV3GQVXJZ | official, help | 2026-11-09 | Default extension off Amazon; creators |
| Create a Sponsored Products campaign (2026-09-28) | https://advertising.amazon.com/help/GKLSYGFS2YD33FER | official, help | 2026-11-09 | Auto/manual choice; global campaigns and GenAI localized targets |
| Create a Sponsored Brands campaign (2026-09-30) | https://advertising.amazon.com/help/GF86HBCNDJUAC5WN | official, help | 2026-11-09 | Keyword or product per ad group; automatic collections; reserve SOV steps |
| Campaign goals for Sponsored Brands (2026-08-11) | https://advertising.amazon.com/help/GXXPFXLSVX9VD3U9 | official, help | 2026-11-09 | Target groups; ToS IS definition; reserve SOV 30–92 days, 95% SOV aim |
| Sponsored ads campaign limits (2026-07-29) | https://advertising.amazon.com/help/G86H2227323T8T4Q | official, help | 2026-11-09 | Keyword, target and negative limits |
| Suggested products (2026-02-24) | https://advertising.amazon.com/help/G9DL6CTTHZ56GU38 | official, help | 2026-11-09 | "46 times" figure; ML-suggested ASINs to advertise |
| Understand prompts on Sponsored Products and Sponsored Brands (2026-03-26) | https://advertising.amazon.com/help/GLWNW26EWQZW46WZ | official, help | 2026-11-09 | Prompts, auto-enrolled in the US |
| Set bids in a Sponsored Products campaign (2026-10-16) | https://advertising.amazon.com/help/GTMXQWASBRZTHLF2 | official, help | 2026-11-09 | Per-group auto bids; per-match-type keyword bids |
| Understand bidding on Sponsored ads (2026-11-02) | https://advertising.amazon.com/help/GDS2E64R9GQ35768 | official, help | 2026-11-09 | vCPM minimums; suggested bid basis (7 days) |
| Understand Amazon Ads auctions (2026-04-27) | https://advertising.amazon.com/help/GEXGZNBBWPZZK7P8 | official, help | 2026-11-09 | Relevance in auctions; reserve prices |
| Troubleshoot your campaign for impressions (2026-07-16) | https://advertising.amazon.com/help/G8WCYU3FQKFVSMR4 | official, help | 2026-11-09 | Product targeting low traffic; 2026-07-01 fashion detail-page change; BMM not SD |
| Targeting (policy) (2026-08-03) | https://advertising.amazon.com/help/GD6SPCK5RJZL73PU | official, policy | 2026-11-09 | Audience relevance; 1,000-user and 100-seed minimums |
| General requirements (2026-07-22) | https://advertising.amazon.com/help/G4U9JBZH3664JWX2 | official, policy | 2026-11-09 | Rights to all content; brand usage |
| Prohibited content across all supply (2026-06-19) | https://advertising.amazon.com/help/GRW23T7LB4MFMBXQ | official, policy | 2026-11-09 | No trademark-keyword rule found |
| Prohibited content and products for Amazon O&O supply (2026-04-10) | https://advertising.amazon.com/help/GTEEH3E3J2BDELBA | official, policy | 2026-11-09 | "Disparaging or criticizing a named competitor" |
| Policies and guidelines (2025-10-21) | https://advertising.amazon.com/help/G26M9XTK78AMR8TP | official, policy index | 2026-11-09 | Policy tree |
| Ad policy change log (2026-04-27) | https://advertising.amazon.com/help/G8X8M375UPCN4UUC | official, policy | 2026-11-09 | Where policy changes are logged (no targeting entry used) |
| Support Center Homepage and section indexes (Building campaigns, Bidding and budget, Before you begin, Troubleshooting, Create a campaign, Sponsored ads, References) | https://advertising.amazon.com/help/GX4827LQGBFHA2U8 (and children) | official, help index | 2026-11-09 | Navigation to the articles above |
| A guide to targeting with Sponsored Products | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official, library | 2026-11-09 | Auto basis; match type wording; bid order advice; strategies; character rule conflict; example errors |
| Best practices for your Sponsored Products ads | https://advertising.amazon.com/library/guides/sponsored-products-best-practices | official, library | 2026-11-09 | Own product pages; report thresholds; same-category ASINs |
| What is keyword targeting? | https://advertising.amazon.com/library/guides/keyword-targeting | official, library | 2026-11-09 | Auto reads titles and descriptions; exact reordering example; negative broad mention; 25–50 keywords |
| 3 steps to help start or improve your keyword strategy | https://advertising.amazon.com/blog/how-to-start-and-improve-your-keyword-strategy | official, blog | 2026-11-09 | Broad bid higher; 25 terms; organic keywords; 11.2% figure |
| A complete guide to Sponsored Brands and display ads moderation | https://advertising.amazon.com/library/guides/sponsored-brands-display-ads-moderation | official, library | 2026-11-09 | No competitor names in creative; targeting relevance |
| Sponsored Products launches expanded product targeting (2022-10-26) | https://advertising.amazon.com/resources/whats-new/expanded-product-targeting-sponsored-products | official, what's new | 2026-11-09 | Expanded targets "similar" performance, dynamic |
| Sponsored Products (solutions page; redirect from /blog/new-bidding-and-targeting-options-for-sponsored-products) | https://advertising.amazon.com/solutions/products/sponsored-products | official, solutions | 2026-11-09 | Featured Offer eligibility; redirect noted |
| Introducing Amazon Ads Agent, your AI-powered ad platform (2026-09-29) | https://advertising.amazon.com/library/news/amazon-ads-agent | official, news | 2026-11-09 | AI targeting; DVA+ combining SD, rollout from late October; 25%/10% figure |
| Limits, constraints, and quotas | https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md | official, API docs | 2026-11-09 | Bid min/max by marketplace; keyword character rules; scripts |
| Keyword targeting overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/overview.md | official, API docs | 2026-11-09 | Ad-group-level targeting; nativeLanguage for reporting |
| Sponsored Products keyword recommendations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keywords/suggestions.md | official, API docs | 2026-11-09 | Recommendation request forms; v3–v5; default ranking heuristic; impact metrics not estimates |
| Sponsored Products product targeting overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/overview.md | official, API docs | 2026-11-09 | One ASIN per clause; exact/similar; category-first |
| Sponsored Products product targeting recommendations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/suggestions.md | official, API docs | 2026-11-09 | Theme vs ASIN response; similar inputs |
| Category targeting suggestions and refinements | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/product-targeting/category-suggestions-refinements.md | official, API docs | 2026-11-09 | Tree on Amazon.com; min/max product counts; refinements |
| Auto targeting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/auto-targeting.md | official, API docs | 2026-11-09 | Four expressions auto-created; per-expression bids |
| Negative keyword targeting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/keywords.md | official, API docs | 2026-11-09 | Campaign vs ad group; v1 negative (examples EXACT only) |
| Sponsored Products negative product and brand targeting overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/negative-targeting/product-brand.md | official, API docs | 2026-11-09 | Vendors-only warning for manual campaign-level negatives |
| Get started with automatic campaigns | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/auto-campaigns.md | official, API docs | 2026-11-09 | "we recommend starting with an auto campaign" |
| Get started with manual campaigns | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/get-started/manual-campaigns.md | official, API docs | 2026-11-09 | Manual flow incl. products count |
| Sponsored Product keyword groups targeting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/keyword-group-targeting.md | official, API docs | 2026-11-09 | Beta, US; no mixing with product targets |
| Target promotion | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/target-promotion.md | official, API docs | 2026-11-09 | Auto-to-manual promotion |
| Sponsored Brands overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/overview.md | official, API docs | 2026-11-09 | SB formats: manual collection, automatic collection, store spotlight, video |
| Reserve share of voice (API guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/reserve-share-of-voice.md | official, API docs | 2026-11-09 | BRANDED_KEYWORD recommendations; keyword reservation validation; deal targets |
| Amazon Ads API v1 release notes | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v1.md | official, API docs | 2026-11-09 | Reporting API v1 GA 2026-09-30; SB Collections worldwide; no targeting change overturning this file |
| Get started with Sponsored Brands campaigns | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/campaigns/get-started-with-campaigns.md | official, API docs | 2026-11-09 | Goals; `smartDefault` TARGETING; endpoints |
| Sponsored Display contextual targeting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/contextual-targeting.md | official, API docs | 2026-11-09 | `similarProduct`; negative targets |
| Sponsored Display audience targeting | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/audience-targeting.md | official, API docs | 2026-11-09 | Audience clauses and discovery |
| Sponsored Display dynamic segments overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/dynamic-segments.md | official, API docs | 2026-11-09 | Console adds similar products; API must create it |
| Release notes | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md | official, API docs | 2026-11-09 | Dated changes: negatives 2025-05-22, v2 deprecation, keyword groups, SB themes, expanded bulksheets, SD themes, translations, Alexa+, Recommendations API |
| Recommendations API overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/overview.md | official, API docs | 2026-11-09 | List and query endpoints; modes |
| How to call the Recommendations API | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/how-to.md | official, API docs | 2026-11-09 | Object types incl. branded/unbranded keyword |
| Recommendation types | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/recommendations/recommendations-api/recommendation-types.md | official, API docs | 2026-11-09 | Four types today; BRAND_PRODUCT_KEYWORD |
| Amazon Marketing Cloud - Keyword clustering | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/playbooks/keyword-clustering.md | official, API docs | 2026-11-09 | Clustering search terms by purchased ASINs |
| Search term reports (v3) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/report-types/search-term.md | official, API docs | 2026-11-09 | Clicked impressions only; keywordType values |
| Targeting reports (v3) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/report-types/targeting.md | official, API docs | 2026-11-09 | keywordType values incl. THEME for SB |
| Migrating from: spSearchTerm (v1) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/report-types/sp-search-term.md | official, API docs | 2026-11-09 | v3→v1 search term mapping |
| Search term (Targeting), v1 | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/targeting/search-term.md | official, API docs | 2026-11-09 | SP and SB only |
| Matched target (Targeting), v1 | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/targeting/matched-target.md | official, API docs | 2026-11-09 | SD only (corrects prior research) |
| Targeting match type, v1 | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/targeting/targeting-match-type.md | official, API docs | 2026-11-09 | `targetingMatchType.value` |
| Product relevance (Product), v1 | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dimensions/product/product-relevance.md | official, API docs | 2026-11-09 | Promoted vs halo |
| Search (Impression share), v1 | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/impression-share/search.md | official, API docs | 2026-11-09 | Required/incompatible dimensions |
| Sponsored Products 3.0 model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official, OpenAPI | 2026-11-09 | Predicates; match type enums; recommendation operations and their texts |
| Amazon Ads API (all), merged v1 model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official, OpenAPI | 2026-11-09 | TargetType, ThemeMatchType, ProductMatchType, refinements |
| Sponsored Brands v3 model | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | official, OpenAPI | 2026-11-09 | SB match types, themes, predicates, recommendations |
| Sponsored Brands v4 model | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | official, OpenAPI | 2026-11-09 | SB categories, products count, brand negatives |
| Sponsored Display v3 model | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml | official, OpenAPI | 2026-11-09 | Tactics; contextual and audience clauses; lookbacks; recommendations |
| Localization model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Localization_prod_3p.json | official, OpenAPI | 2026-11-09 | Keyword, product, targeting expression localization |
| Audiences model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json | official, OpenAPI | 2026-11-09 | Audience discovery |
| Recommendations model (tactical recommendations, sponsored ads) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Recommendations_prod_3p.json | official, OpenAPI | 2026-11-09 | `/recommendations/list`, `/apply`; NEW_KEYWORD, NEW_NEGATIVE_KEYWORD, NEW_PRODUCT_TARGETING and other types |
| Analytics Reports (SP-API docs) | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics | official, docs | 2026-11-09 | Top Search Terms and SQP report rules |
| sellingPartnerSearchTermsReport schema | https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchTermsReport.json | official, GitHub amzn | 2026-11-09 | Field definitions |
| sellingPartnerSearchQueryPerformanceReport schema | https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/schemas/reports/sellingPartnerSearchQueryPerformanceReport.json | official, GitHub amzn | 2026-11-09 | Query relevant to branded catalog; search-page impressions |
| What is Amazon Brand Analytics? | https://sell.amazon.com/blog/brand-analytics | official, sell.amazon.com | 2026-11-09 | Dashboards; SQP volume and score; TST shares |
| AMALYZE, Broad, phrase, exact | https://amalyze.com/resources/guides/advertising/amazon-ppc-keyword-match-types | opinion | 2026-11-09 | Close variants at all types; no switch; no negative broad |
| AMALYZE, Close Variant glossary | https://amalyze.com/resources/glossary/close-variant | opinion | 2026-11-09 | Reordering counts; synonyms do not (exact) |
| Intentwise, Sponsored Brands Search Term Report | https://www.intentwise.com/analytics-cloud/data-source/amazon-ads/sponsored-brands-search-term-report | opinion | 2026-11-09 | SP broad vs phrase only word order; SB broad synonyms |
| Parker-Lambert, Sponsored Products behaving differently (2026-06-22) | https://parker-lambert.com/news/amazons-sponsored-products-are-behaving-differently-heres-what-changed/ | opinion | 2026-11-09 | Broad match category drift claim |
| Ad Badger, segment 4 auto-targets (2021-07-09) | https://www.adbadger.com/blog/amazon-ppc-education/should-you-segment-your-4-auto-targets-in-amazon-ads/ | opinion | 2026-11-09 | Close match dominance; segmentation |
| ClearAds, Automatic Targeting Search Term Report (2025-05-31) | https://clearadsagency.com/amazon-reports/amazons-automatic-targeting-search-term-report/ | opinion | 2026-11-09 | Auto reads bullets and backend (their claim) |
| Perpetua, product targeting campaigns (2020-11-18) | https://perpetua.io/blog-amazon-ppc-ads-product-targeting-campaigns | opinion | 2026-11-09 | Placement shares by targeting type (one seller) |
| Perpetua help, SB Theme Targeting keywords (2026-04-02) | https://help.perpetua.io/en/articles/9202814-sponsored-brands-theme-targeting-keywords | opinion | 2026-11-09 | Themes default on SBv4 |
| JumpFly, Expanded targeting (2024-07-09) | https://www.jumpfly.com/blog/expanded-brand-keyword-and-product-targeting-on-amazon-ads/ | opinion | 2026-11-09 | Expanded defaults; SB BMM usage |
| Helium 10, search volume accuracy (2024-08-23) | https://www.helium10.com/blog/helium-10-vs-jungle-scout-search-volume-accuracy/ | opinion | 2026-11-09 | Volume estimation method; vendor test |
| Jungle Scout, vs Helium 10 (2024-03-21) | https://www.junglescout.com/resources/articles/jungle-scout-vs-helium-10/ | opinion | 2026-11-09 | Vendor test against SQP |
| Semantic Product Search (arXiv 1907.00937) | https://arxiv.org/abs/1907.00937 | research | 2026-11-09 | Lexical failure modes; behaviour-trained matching |
| Extreme Multi-label Learning for Semantic Matching in Product Search (arXiv 2106.12657) | https://arxiv.org/abs/2106.12657 | research | 2026-11-09 | XMC matching at 100M scale |
| Shopping Queries Dataset (arXiv 2206.06588) | https://arxiv.org/abs/2206.06588 | research | 2026-11-09 | ESCI labels; dataset size |
| esci-data README | https://github.com/amazon-science/esci-data | research, GitHub | 2026-11-09 | Tasks; 40 results per query; languages |
| COSMO (SIGMOD/PODS 2024) | https://www.amazon.science/publications/cosmo-a-large-scale-e-commerce-common-sense-knowledge-generation-and-serving-system-at-amazon | research | 2026-11-09 | Intent knowledge in Amazon search |
| Amaldoss, Jerath & Sayedi 2016 (EconPapers) | https://econpapers.repec.org/RePEc:inm:ormksc:v:35:y:2016:i:2:p:259-274 | research | 2026-11-09 | Bibliographic record |
| Amaldoss, Jerath & Sayedi 2016 (IDEAS) | https://ideas.repec.org/a/inm/ormksc/v35y2016i2p259-274.html | research | 2026-11-09 | Abstract |
| Ghose & Yang 2009 (EconPapers) | https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:10:p:1605-1622 | research | 2026-11-09 | Abstract |
| Simonov, Nosko & Rao 2018 (EconPapers) | https://econpapers.repec.org/RePEc:inm:ormksc:v:37:y:2018:i:2:p:200-215 | research | 2026-11-09 | Abstract |
| *Gap fill 2026-11-09:* Migrate from Product collections to Sponsored Brands collections (lastModified 2026-10-05) | https://advertising.amazon.com/help/GV7N6KZTH4HF4T2P | official, help | 2026-11-09 | February 2027; auto-migration of 3-ASIN ads; 4-week overlap; auto collections keyword-only |
| Deprecations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md | official, API docs | 2026-11-09 | Product Collection: August 2026 mapping, "Post January 2027" error; docs location of SB 3.0 prod |
| Product Collection Migration Guide | https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-product-collection.md | official, API docs | 2026-11-09 | "January 2027 \| Final shutoff" |
| Sponsored Brands 3.0 model (`SponsoredBrands_prod_3p.json`) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredBrands_prod_3p.json | official, OpenAPI | 2026-11-09 | 50 paths; brand-negative recommendations, categories, products count; no `/sb/negativeKeywords` |
| How to set up Amazon Sponsored Brands reserve share of voice (dateModified 2026-10-09) | https://advertising.amazon.com/library/guides/sponsored-brands-reserve-share-of-voice | official, library | 2026-11-09 | "e.g., 14–90 days"; "$6K per campaign" US; 20 marketplaces incl. Ireland |
| Drive top-of-search visibility and engagement (RSOV what's new, dateModified 2026-10-09) | https://advertising.amazon.com/resources/whats-new/sponsored-brands-reserve-share-of-voice | official, what's new | 2026-11-09 | Marketplace list incl. Egypt, without Ireland or Spain |
| Audiences model (re-read) | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Audiences_prod_3p.json | official, OpenAPI | 2026-11-09 | `fetchTaxonomy`, `listAudiences`; filter fields; `adType` DSP/SD/ST |
| Targetable Entities model | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/TargetableEntities_prod_3p.json | official, OpenAPI | 2026-11-09 | `ListTargetableEntities`, `ListTargetableEntityPaths`; request filters; entity fields |
| Sponsored Display audience targeting (re-read) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-display/audience-targeting.md | official, API docs | 2026-11-09 | Taxonomy → discovery → `audienceSameAs` target; overlapping audiences top 30 |
| Shopper cohort bidding (Sponsored Brands) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/bidding/shopper-cohort.md | official, API docs | 2026-11-09 | `targetableEntities/list` sample; AMC and Product paths |
| Product Opportunity Explorer overview (PDF) | https://m.media-amazon.com/images/G/01/sell/guides/Product_Opportunity_Explorer_Overview.pdf | official, seller guide | 2026-11-09 | Niche definition; tabs and metrics; weekly/monthly refresh |
| Product Opportunity Explorer (sell.amazon.com tools page) | https://sell.amazon.com/tools/product-opportunity-explorer | official, sell.amazon.com | 2026-11-09 | Access via Seller Central; Professional account; 2.5x figure |
| Get product ideas with Product Opportunity Explorer (blog) | https://sell.amazon.com/blog/product-opportunity-explorer | official, sell.amazon.com | 2026-11-09 | Customer Review Insights; Returns tab; ASIN search |
| Customer Feedback v2024-06-01 (reference, dateModified 2026-09-09) | https://developer-docs.amazon/sp-api/reference/customer-feedback-v2024-06-01 | official, SP-API docs | 2026-11-09 | "same information as the Product Opportunity Explorer"; marketplaces; weekly; English only |
| New: Introducing the Customer Feedback API v2024-06-01 (changelog) | https://developer-docs.amazon.com/sp-api/changelog/new-introducing-the-customer-feedback-api-v2024-06-01 | official, SP-API docs | 2026-11-09 | Same statement; review at ASIN and browse node, returns at browse node |
| customerFeedback_2024-06-01.json | https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/models/customer-feedback-api-model/customerFeedback_2024-06-01.json | official, GitHub amzn | 2026-11-09 | Seven operations; no search-term data |
| Meet Alexa for Shopping (aboutamazon, 2026-05-13) | https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant | official, aboutamazon | 2026-11-09 | Rufus and Alexa+ brought together; US app, website, Echo Show |
| What agentic shopping means for advertising (2026-06-11, dateModified 2026-10-09) | https://advertising.amazon.com/library/news/agentic-shopping-advertising | official, news | 2026-11-09 | Campaigns auto-eligible in Alexa for Shopping; prompts; Alexa+ Conversational Ads auto-enrolled |
| A guide to targeting with Sponsored Products (re-read, dateModified 2026-10-09) | https://advertising.amazon.com/library/guides/targeting-with-sponsored-products | official, library | 2026-11-09 | "won't be bidding against yourself by adding different match types on the same keyword" in context |
| Understand Amazon Ads auctions (re-read) | https://advertising.amazon.com/help/GEXGZNBBWPZZK7P8 | official, help | 2026-11-09 | No own-advertiser rule |
| Understand keyword match types (re-read) | https://advertising.amazon.com/help/GHTRFDZRJPW6764R | official, help | 2026-11-09 | Highest-bid match type sentence, verbatim |
| Reserve keywords in a Sponsored Brands campaign; Campaign goals for Sponsored Brands; Create a Sponsored Brands campaign (re-read) | https://advertising.amazon.com/help/G86SD7HK6NHHRB9B; …/GXXPFXLSVX9VD3U9; …/GF86HBCNDJUAC5WN | official, help | 2026-11-09 | 15–92 days, $3,000, not Spain; 30–92 days; 14-day mapping |
| Limits (re-read, keyword characters) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/concepts/limits.md | official, API docs | 2026-11-09 | Hiragana, katakana, kanji, half/full-width ranges; "parts" limits |
| キーワードターゲティングとは何ですか？ (ja-jp library, dateModified 2026-10-09) | https://advertising.amazon.com/ja-jp/library/guides/keyword-targeting | official, library | 2026-11-09 | JP phrase example on unspaced text; exact reordering example |
| スポンサープロダクト広告のターゲティングに関するガイド (ja-jp library, dateModified 2026-10-20) | https://advertising.amazon.com/ja-jp/library/guides/targeting-with-sponsored-products | official, library | 2026-11-09 | Phrase example "キングDopplerコットンシーツセット"; characters; case |
| スポンサー広告に関するよくある間違いと解決策 (ja-jp library, dateModified 2026-10-09) | https://advertising.amazon.com/ja-jp/library/expert-advice/common-sponsored-ads-mistakes-and-solutions | official, library | 2026-11-09 | Match-type advice; nothing on script variants |
| Was ist Keyword-Targeting? (de-de library, dateModified 2026-10-08) | https://advertising.amazon.com/de-de/library/guides/keyword-targeting | official, library | 2026-11-09 | Phrase "Laufschuhe" not "Schuhe zum Laufen"; SB semantic example |
| Ein Leitfaden zum Targeting mit Sponsored Products (de-de library, dateModified 2026-10-13) | https://advertising.amazon.com/de-de/library/guides/targeting-with-sponsored-products | official, library | 2026-11-09 | Hyphenated compound examples; characters; case |
| Release notes (re-read: 2025-02-28, 2025-03-12, 2025-03-24, 2025-08-22, 2026-09-18) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md | official, API docs | 2026-11-09 | Audience boost ids via `ListTargetableEntities`; ListMigrations February 2027 |
| Helium 10, Cerebro (dateModified 2026-03-09) | https://www.helium10.com/tools/cerebro/ | opinion | 2026-11-09 | Reverse ASIN, organic and paid, 10 ASINs |
| Jungle Scout, Keyword Scout (dateModified 2025-01-24) | https://www.junglescout.com/features/keyword-scout/ | opinion | 2026-11-09 | Reverse ASIN, exact and broad volumes, two-year history, CPC |
| EcomCrew, DataDive Review and Case Study (2024-10-30) | https://www.ecomcrew.com/datadive-review-and-case-study/ | opinion | 2026-11-09 | DataDive's sources incl. Helium 10; MKL |
| SellerSprite, SellerSprite vs DataDive 2026 (2026-08-05) | https://www.sellersprite.com/en/blog/sellersprite-vs-datadive-2026 | opinion | 2026-11-09 | MKL via Niche Dive; SellerSprite's 30-day, top-3-pages reverse ASIN |
| DataDive home page (dateModified 2026-04-27) | https://datadive.tools/ | opinion | 2026-11-09 | No method detail |
| AMALYTIX, Product Opportunity Explorer (modified 2026-10-26) | https://www.amalytix.com/en/knowledge/controlling/amazon-product-opportunity-explorer/ | opinion | 2026-11-09 | No Brand Registry; tabs; 90/360-day windows; marketplaces; download |
| Intentwise, Product Opportunity Explorer | https://www.intentwise.com/analytics-cloud/data-source/amazon-seller/product-opportunity-explorer | opinion | 2026-11-09 | 360-day windows; Professional; five marketplaces |
| Goat Consulting, Product Opportunity Explorer (modified 2026-04-01) | https://www.goatconsulting.com/blog/product-opportunity-explorer-keyword-and-market-research-for-selling-on-amazon | opinion | 2026-11-09 | 90-day windows; no export |
| AMALYZE, Product Opportunity Explorer glossary | https://amalyze.com/resources/glossary/product-opportunity-explorer | opinion | 2026-11-09 | "Brand Registry sellers and vendors" |
| AMALYZE, Duplicate Keywords in Amazon PPC | https://amalyze.com/blog/duplicate-keywords-ppc | opinion | 2026-11-09 | Highest expected bid × CTR among duplicates |
| Ad Badger, Keyword Cannibalization (modified 2026-06-24) | https://adbadger.com/blog/keyword-cannibalization-and-placement-in-amazon-ppc/ | opinion | 2026-11-09 | Not bidding against yourself; different ad groups |
| AMALYZE, Close Variant glossary; Broad, phrase, exact (re-read) | https://amalyze.com/resources/glossary/close-variant; https://amalyze.com/resources/guides/advertising/amazon-ppc-keyword-match-types | opinion | 2026-11-09 | Hyphenation and accent variants; no compound statement |
| ECのミカタ, キーワードマッチタイプの基本ガイド (2023-07-18) | https://ecnomikata.com/column/39736/ | opinion | 2026-11-09 | Japanese keywords written with spaces; match-type examples |
| ECのミカタ, ネガティブターゲティング (2023-11-09) | https://ecnomikata.com/column/40871/ | opinion | 2026-11-09 | Negative example; nothing on script variants |
| ECのミカタ, Amazon広告のキーワード選定ガイド (2026-01-21) | https://ecnomikata.com/blog/49334/ | opinion | 2026-11-09 | Generic match-type advice; nothing on script variants |
| Zhang et al., Query Reformulation (arXiv 2402.11202, abstract and HTML v2) | https://arxiv.org/abs/2402.11202; https://arxiv.org/html/2402.11202v2 | research | 2026-11-09 | Japanese script normalisation, tokenisation, sorting; Ads matching A/B |
| OpenAlex records: Lambrecht & Tucker 2013; Sahni, Narayanan & Kalyanam 2019; Bleier & Eisenbeiss 2015; Johnson, Lewis & Nubbemeyer 2017; Rutz, Bucklin & Sonnier 2012; Agarwal, Hosanagar & Smith 2011; Narayanan & Kalyanam 2015; Ghose & Yang 2009 | https://api.openalex.org/works/https://doi.org/<DOI> for each DOI given in *Published research* | research | 2026-11-09 | Abstracts and bibliographic data |

The prior paid-keywords research (`cx-listing-playbook/research/angles/paid-keywords.md`, read 2026-10-14) was used only as a list of pages to re-open. Every claim carried here was re-read today. Two of its claims are corrected (items F and M).

**Unreachable**

- Search Engine Land, *Amazon advertising match types* (https://searchengineland.com/amazon-advertising-match-types-454405): Cloudflare 403 to a plain GET.
- Library guides https://advertising.amazon.com/library/guides/keyword-research, /negative-keywords and /product-targeting: 404 (no such guides).
- Ads API guide markdown, 404 (NoSuchKey) on the cloudfront host:
  - guides/sponsored-brands/theme-based-targeting (linked from the release notes), /theme-targeting, /keywords, /keyword-targeting, /keyword-recommendations, /product-targeting, /product-targeting/overview, /targeting;
  - guides/sponsored-display/targeting-recommendations, /targeting;
  - guides/sponsored-products/keyword-groups, /targeting/keyword-groups, /global-campaigns;
  - guides/localization/overview;
  - guides/campaign-management/entities/targets.

  The models and the remaining guides cover these topics.
- https://sell.amazon.com/tools/brand-analytics: 404.
- https://advertising.amazon.com/resources/ad-policy/sponsored-ads-policies (and its en-gb copy): 301 to help node G2NN8D3LSUR9V9EA, the Support Center Homepage; the policy text was read in the help tree instead.
- The ESCI paper PDF (https://arxiv.org/pdf/2206.06588): downloaded, but this machine's PDF tools failed (missing poppler library). The abstract and the GitHub README were used instead; full label definitions were not read.
- The Seller Central help pages for Search Query Performance and Top Search Terms: not attempted. A plain GET serves a JS shell, and the content call is outside this seat's limits. The SP-API docs and sell.amazon.com covered both.
- Helium 10, https://www.helium10.com/blog/amazon-ppc-match-types/: 404.
- Teikametrics, https://www.teikametrics.com/blog/amazon-product-targeting/: 404.
- Pacvue, https://pacvue.com/blog/amazon-keyword-match-types/: 403 (bot challenge).
- Full texts of the *Marketing Science* and *Management Science* papers: paywalled; abstracts only.
- *Gap fill 2026-11-09:*
  - Localized help-center articles (ja-jp and de-de) for *Understand keyword match types*, *Set up keyword targeting*, *Add negative keywords…* and *Sponsored ads campaign limits*: `https://advertising.amazon.com/ja-jp/help/<id>` and `/de-de/help/<id>` answer 404, and `?locale=`/`?language=` on the English URL still serves `en_US`. The localized library guides were read instead.
  - DataDive support articles *What is the Master Keyword List (MKL)?* (https://support.datadive.tools/hc/en-us/articles/4414442624921) and *How to Start a Dive*: Cloudflare 403 to a plain GET and to a fetch tool. DataDive's relevancy formula is therefore not carried.
  - Helium 10 knowledge base *Cerebro Overview* and Jungle Scout support *Keyword Scout Overview*: Cloudflare 403. The product pages were read instead.
  - https://datadive.tools/master-keyword-list: 404.
  - SellerSprite Japanese guides (https://www.sellersprite.com/jp/blog/amazon-negative-keywords-guide, …/how-to-conduct-keyword-research-for-amazon-ppc): the GET serves a title-only JS shell, as did a fetch tool.
  - MarkeZine, https://markezine.jp/article/detail/62154: bot check (403).
  - Archived Seller Central *Using Search Terms effectively* (JP and DE copies on web.archive.org): the fetch timed out with no response.
  - Seller Central help pages for Product Opportunity Explorer: not attempted (JS shell; the content call is outside this seat's limits). The sell.amazon.com pages and the seller guide PDF covered it.
  - The POE seller guide PDF: the local poppler tool fails on a missing library, so the text was extracted with macOS PDFKit instead; read in full.

## Open questions

1. **Does SP exact match reorder words?** These texts disagree:
   - the targeting guide: "same words and in the same order";
   - the keyword-targeting guide: "white running shoes" matches "running shoes white";
   - AMALYZE: reordering is a close variant.

   The help page (2026-07-29) says "exact match shopper queries as well as their close variations" and does not mention order.
2. **Can an SP negative be broad?** These texts disagree:
   - the help center (2026-10-20): "phrase and exact match types";
   - the keyword-targeting guide: "exact, phrase, or broad";
   - the SP 3.0 enum: carries `NEGATIVE_BROAD`;
   - SB: has none.

   Only a live create on a seller's profile settles it, and that write is the seller's.
3. **Campaign-level negative product targets on a seller's manual campaign.** The API guide's vendors-only warning conflicts with the US release note of 2025-05-22. Outside the US, the warning may still hold.
4. **Valid characters.** The library guide bans `&` and `"`; the API limits page allows them. The API's own reply is authoritative for the API, but the console may differ.
5. **Bid order across match types.** The targeting guide says exact highest and broad lowest; the blog says broad higher and exact lower. These are recorded as conflicting Amazon guidance; the bid itself is `areas/bids-and-placements.md`'s.
6. **SIS windows.** The SIS help page gives a 30-day share and a 90-day lookback. The SP recommendation field gives 30 days and SB's gives 7 days. Which window the v1 `metric.impressionShare` reports over a requested date range is not stated.
7. **SD views lookback.** The help page and the clause table cap views at 90 days. `TargetingPredicateNested` lists up to 365 for ASIN-grain and category-grain targeting.
8. **Keyword recommendation sort.** The operation text says "clicks or impressions"; the enum is `CLICKS`, `CONVERSIONS` and `DEFAULT`. Amazon says `DEFAULT` uses "our interal ranking mechanism" (the guide: "the default ranking heuristic"); what that mechanism reads is not published.
9. **Bid units in SP 3.0 recommendations.** The text says "minor currency units (example: cents)" in some schemas and "major and minor currency units" in others. The v1 guide's examples are in major units (0.02).
10. **The EG SP maximum of 5.50 on the limits page**: a typo, or a real cap?
11. **Does SP broad match now favour category relevance over query intent?** Parker-Lambert says so, on one case. Amazon's text says broad reads "the context of the advertised products". No measured study was found.
12. **Competitor trademarks as auction keywords.** No Amazon ads page read today states a rule. The only rule found is for reserve SOV. Whether Brand Registry or marketplace policy pages outside the ads help center cover this was not read.
13. **Keyword groups.** Still beta and US-only on 2026-11-09 by the guide. The create predicate `KEYWORD_GROUP_SAME_AS` is "Beta coming soon". Can a seller create one through v1 today?
14. **The v1 theme values** for category, peer brands, gifts and Prime Day: which ad products and marketplaces accept them? No guide documents them.
15. **What auto targeting reads.** Amazon names "titles and descriptions". Whether bullets, backend search terms or A+ content are read is not stated by Amazon. ClearAds says bullets and backend are read.
16. **SD under DVA+.** The unified console folds contextual into multi-signal targeting and DVA+ absorbs Sponsored Display. How long the SD v3 API's `T00020`/`T00030` tactics remain the API surface is not stated on the pages read.
17. **Reserve SOV duration, minimum and marketplaces.** Help pages say 15–92 days and 30–92 days, and the library guide "e.g., 14–90 days". The help page says a $3,000 minimum budget; the guide says "$6K per campaign for the U.S. marketplace". The guide's 20 marketplaces include Ireland; the what's-new list includes Egypt and not Ireland; the SB v4 model excludes goal-based campaigns in Ireland. Which figure the console enforces on the day is not settled by any page.
18. **The category tree's marketplace scope.** The guide says "Amazon.com". Is the tree per profile marketplace?
19. **Which of an advertiser's own matching targets serves** when several keyword texts, ad groups, campaigns, or a keyword and a product or auto target match one query. Amazon answers one keyword in several match types (highest bid used; "you won't be bidding against yourself"), without saying whether that reaches across ad groups and campaigns. AMALYZE says the choice uses expected bid and CTR; Ad Badger says products in different ad groups can serve together. (Partly answered in the gap fill of 2026-11-09; item Q.)
20. **Which match types a v1 negative keyword accepts.** The v1 guide shows only `EXACT`; the field's enum carries `BROAD`, `EXACT` and `PHRASE`.
21. **The tactical recommendations API after August 2026.** Its model still lists `NEW_KEYWORD`, `NEW_NEGATIVE_KEYWORD` and `NEW_PRODUCT_TARGETING` types, its guides return 404, and the v1 Recommendations API is now Amazon's "single interface". Whether the old surface still returns targeting recommendations is not stated.
22. **Japanese script and width variants in match types and negatives.** Do broad, phrase, exact, negative phrase and negative exact treat こども/子供/コドモ, full-width against half-width characters, and spaced against unspaced queries as one term? Amazon's JP examples show phrase match inside unspaced text, and Amazon's research describes script normalisation and tokenisation in Japanese Ads matching. No page states the match-type or negative rule.
23. **What a "part" is in the keyword limits** for unspaced Japanese, and whether the ideographic space (`　`) separates parts.
24. **German compounds in SP broad and exact.** Amazon's DE example says phrase "Laufschuhe" does not match "Schuhe zum Laufen", and SB semantic matching can. Whether SP broad or exact bridges compound, split and hyphenated forms is not stated.
25. **Product Opportunity Explorer's windows, eligibility and marketplaces.** Amazon's guide does not define the window behind search volume and click share (practitioners give 90 and 360 days), names only a Professional selling account, and lists no marketplaces.
26. **SB brand-negative recommendations in the v3 YAML.** `/sb/negativeTargets/brands/recommendations` is in the *Sponsored Brands 3.0* JSON and SB v4 JSON but not in the cloudfront SB v3 YAML, which holds `/sb/negativeKeywords`. Whether the YAML is a frozen legacy copy is not stated.

## Positions

Each position is a fact a model reads. Sources are listed with Amazon's first.

**P-keyword-and-product-targeting-1.** SP manual keywords have three match types: broad, phrase and exact. Amazon says all three "account for plurals, misspellings, and translations". Sources: [official] Help *Understand keyword match types* (GHTRFDZRJPW6764R); [official] Help *Set up keyword targeting* (GK3MNACNTXG659J9); [official] v1 model `KeywordMatchType`.

**P-keyword-and-product-targeting-2.** Amazon defines SP broad match as matching the keyword's terms "in any order", including "singulars, plurals, variations, synonyms, and related terms as determined by the meaning of the keyword and the context of the advertised products". It adds: "The keyword itself may not be contained in the customer shopping query." Sources: [official] Help GHTRFDZRJPW6764R.

**P-keyword-and-product-targeting-3.** Amazon defines SP phrase and exact match as also covering "close variations like misspellings, plural forms, acronyms, translations". Its own exact-match example lets "outside lights" serve "outdoor lights". Sources: [official] Help GHTRFDZRJPW6764R.

**P-keyword-and-product-targeting-4.** Amazon's pages disagree on whether exact match tolerates word reordering. One library guide says "same words and in the same order"; another gives "running shoes white" for "white running shoes". AMALYZE says reordering is a close variant. Sources: [official] *A guide to targeting with Sponsored Products*; [official] *What is keyword targeting?*; [opinion] AMALYZE, *Close Variant* glossary.

**P-keyword-and-product-targeting-5.** No Amazon match type is a literal string match. AMALYZE says close-variant matching cannot be switched off and that negatives are the only lever. Sources: [official] Help GHTRFDZRJPW6764R; [opinion] AMALYZE, *Broad, phrase, exact* and *Close Variant* glossary.

**P-keyword-and-product-targeting-6.** A keyword's match type cannot be changed after the campaign is created. A keyword with another match type can be added while the campaign runs. A negative keyword's match type cannot be changed. Sources: [official] Help GHTRFDZRJPW6764R; [official] Help *Add negative keywords or negative products targeting* (GTEHPEG5BXY9UX5W).

**P-keyword-and-product-targeting-7.** When an advertiser sets one keyword in several match types with different bids, Amazon uses the match type with the highest bid for any matching query. Sources: [official] Help GHTRFDZRJPW6764R.

**P-keyword-and-product-targeting-8.** When no customer search term exists, Amazon infers one from context and serves keywords in relevant placements. SP keywords also serve on product pages, elsewhere on Amazon, and off Amazon on sites, apps and creator content. Off-Amazon serving is on by default in 19 named countries. Sources: [official] Help GHTRFDZRJPW6764R; [official] Help *Understand targeting* (G3XAU5G7C2JTNQTM); [official] Help *Understand Sponsored Products off-Amazon advertising* (GYTD2Z3SYMAAMVXA).

**P-keyword-and-product-targeting-9.** SB keyword matching adds semantic matching on "the same meaning or intent", even for phrase match. SB supports a `+` broad match modifier that requires the marked word. Sources: [official] Help G3XAU5G7C2JTNQTM; [official] Help GK3MNACNTXG659J9; [official] Help GHTRFDZRJPW6764R.

**P-keyword-and-product-targeting-10.** SB negative keywords are exact and phrase only. SB keyword text is limited to 10 words, and negative phrase to 4 words. Sources: [official] SB v3 model `NegativeMatchType`.

**P-keyword-and-product-targeting-11.** Negative phrase blocks queries containing "the complete phrase or close variations"; negative exact blocks "the exact phrase or close variation". Negative phrase is limited to 4 words and negative exact to 10, each at most 80 characters. Sources: [official] Help GTEHPEG5BXY9UX5W; [official] Help *Sponsored ads campaign limits* (G86H2227323T8T4Q); [official] Ads API *Limits*.

**P-keyword-and-product-targeting-12.** On whether SP negatives can be broad, the help center (lastModified 2026-10-20) says phrase and exact only. The SP 3.0 enum carries `NEGATIVE_BROAD`, and one library guide mentions broad negatives. Sources: [official] Help GTEHPEG5BXY9UX5W; [official] SP 3.0 model; [official] *What is keyword targeting?*; [opinion] AMALYZE ("There is no negative broad").

**P-keyword-and-product-targeting-13.** Amazon gives these effect delays: negative keywords take up to 72 hours and negative products up to 96 hours. Sources: [official] Help GTEHPEG5BXY9UX5W.

**P-keyword-and-product-targeting-14.** Automatic targeting exists only in SP and has four groups: close match, loose match, substitutes and complements. In the API they are `QUERY_HIGH_REL_MATCHES`, `QUERY_BROAD_REL_MATCHES`, `ASIN_SUBSTITUTE_RELATED` and `ASIN_ACCESSORY_RELATED`. They are created automatically, cannot be created manually, and can each be bid and paused. Sources: [official] Help GHTRFDZRJPW6764R; [official] SP 3.0 model; [official] Ads API guide *Auto targeting*; [official] Help *Set bids in a Sponsored Products campaign* (GTMXQWASBRZTHLF2).

**P-keyword-and-product-targeting-15.** By Amazon's definitions, close and loose match are search-query groups, and substitutes and complements are detail-page groups. Sources: [official] Help GHTRFDZRJPW6764R.

**P-keyword-and-product-targeting-16.** Amazon says auto targeting "analyzes your product details, including titles and descriptions". It also describes auto as working from "previous shopping queries and your product information" and "similar products and ads". ClearAds says bullets and backend keywords are also read; Amazon does not say so on the pages read. Sources: [official] *What is keyword targeting?*; [official] *A guide to targeting with Sponsored Products*; [official] Help G3XAU5G7C2JTNQTM; [opinion] ClearAds Agency.

**P-keyword-and-product-targeting-17.** Ad Badger's Paul Haberlien says that in an unsegmented auto campaign close match takes most of the traffic, and that placement statistics blend all four groups. He recommends separate campaigns per group for control. Sources: [opinion] Ad Badger (2021-07-09).

**P-keyword-and-product-targeting-18.** An SP product target holds one ASIN per clause and is either exact or expanded ("similar"). Expanded targeting is the console default. It adds "a limited number of additional products with the highest performance potential", chosen "based on past interactions and views" and updated daily. It reports with a "Product-expanded" prefix. Sources: [official] Help *Set up product targeting* (GB2JECV9CJK6R6AL); [official] Ads API guide *Sponsored Products product targeting overview*; [official] What's new *Sponsored Products launches expanded product targeting*; [official] SP 3.0 `ASIN_EXPANDED_FROM`.

**P-keyword-and-product-targeting-19.** Amazon says a product target appears on the targeted product's detail page and on search result pages where that product ranks among the top results. In one seller's 2020 placement data, 85–92% of category, ASIN and brand targeting fell on detail pages. Sources: [official] *A guide to targeting with Sponsored Products*; [opinion] Perpetua, Angela Yuan (2020-11-18).

**P-keyword-and-product-targeting-20.** Category targets can be refined by brand, price range and star rating in SP, SB and SD. SP and SD can also refine by Prime shipping, age range (Toys & Games) and genre (Books). A refinement requires the category. SB has no expanded-ASIN target. Sources: [official] Help GB2JECV9CJK6R6AL; [official] Ads API guide *Sponsored Products product targeting overview*; [official] SP 3.0, SB v3 and SD v3 models.

**P-keyword-and-product-targeting-21.** Negative product targets keep ads off detail pages by ASIN or brand. They act on product targets and auto targets in their ad group, or in every ad group of their campaign. Amazon names one's own detail pages as a valid use. Sources: [official] Help GTEHPEG5BXY9UX5W; [official] SP 3.0 model.

**P-keyword-and-product-targeting-22.** Amazon's brand-negative recommender includes the advertiser's own brands. Its stated reason is: "targeting your own brands usually results in lower performance than targeting competitors' brands". Sources: [official] SP 3.0 model, `/sp/negativeTargets/brands/recommendations`.

**P-keyword-and-product-targeting-23.** Amazon's texts conflict on campaign-level negative product targets in a seller's manual SP campaign. The API guide says only vendors can create them. A US release note of 2025-05-22 says negatives "can now be saved on campaigns and ad group regardless of targeting type". Sources: [official] Ads API guide *Sponsored Products negative product and brand targeting overview*; [official] Ads API *Release notes*.

**P-keyword-and-product-targeting-24.** SB theme targeting has two types, "keywords related to your brand" and "keywords related to your landing pages", one of each per ad group. Amazon says themes are generated "based on historical performance and brand interactions". A goal-based SB campaign creates themes by default, and its `smartDefault` cannot be edited after creation. Sources: [official] SB v3 model; [official] Ads API guide *Get started with Sponsored Brands campaigns*; [official] Ads API *Release notes* (2023-08-17, 2025-04-17); [opinion] Perpetua help, Andrea Mamone; [opinion] JumpFly, Jennifer Gebhart.

**P-keyword-and-product-targeting-25.** SP keyword groups are an Amazon-maintained set of keywords built from the advertised ASINs and refreshed over time. On 2026-11-09 they are in beta and available only in the US. They can share an ad group with keywords but not with product targets. Sources: [official] Ads API guide *Sponsored Product keyword groups targeting*; [official] SP 3.0 model; [official] Ads API *Release notes* (2024-04-23).

**P-keyword-and-product-targeting-26.** The v1 API calls auto groups and theme groups `THEME` targets, "formerly known as Auto Targets for Sponsored Products". The enum also lists themes for product category, peer brands, gifts, Prime Day and interested audiences, without per-ad-product documentation. Sources: [official] v1 merged model.

**P-keyword-and-product-targeting-27.** SP keyword recommendations rank by `sortDimension`: `CLICKS`, `CONVERSIONS` or `DEFAULT`, where `DEFAULT` "ranks recommendations by our interal ranking mechanism", which Amazon does not describe further. They return a rank and suggested bids, but no search volume. The operation text also says "clicks or impressions". Sources: [official] SP 3.0 model, `getRankedKeywordRecommendation`; [official] Ads API guide *Sponsored Products keyword recommendations*.

**P-keyword-and-product-targeting-28.** Amazon says keyword recommendations draw on "which keywords performed well for you in the past, as well as those which performed well across Amazon more broadly", and on how often searches "translate into sales". Translations returned with them "do not affect the targeting of ads". Sources: [official] *A guide to targeting with Sponsored Products*; [official] SP 3.0 model.

**P-keyword-and-product-targeting-29.** SP product recommendations come grouped by theme: top converting targets (past 30 days, sorted by sales), similar items viewed together, complements bought together, similar items rated under 3 stars or with fewer than 5 reviews, and other books read. Only the first theme states an order. Sources: [official] SP 3.0 model, `/sp/targets/products/recommendations`.

**P-keyword-and-product-targeting-30.** The v2 suggested-keyword endpoints were deprecated on 2026-01-27 for shutoff in June 2026. Amazon names `/sp/targets/keywords/recommendations` as the replacement. Sources: [official] Ads API *Release notes*.

**P-keyword-and-product-targeting-31.** The v1 Recommendations API launched in August 2026. Its list of types "is updated as new recommendation types launch". On 2026-11-09 its keyword type is SB's `BRAND_PRODUCT_KEYWORD`, which returns a keyword, a bid range and a theme such as Generic, Branded or Seasonal. Sources: [official] Ads API guides *Recommendations API overview* and *Recommendation types*.

**P-keyword-and-product-targeting-32.** Search term impression share is account-wide per search term and per ad type. It is available only for terms where the account had ad impressions. It cannot be split by campaign or ad group. Its windows differ by surface: a 30-day share with a 90-day report lookback (help), 30 days (SP recommendations), and 7 days (SB recommendations). Sources: [official] Help *SIS report* (G7AQQUSFVZPAAXEU); [official] SP 3.0 model; [official] SB v3 model; [official] Ads API guide *Search (Impression share)*.

**P-keyword-and-product-targeting-33.** Search term reports include only impressions that led to at least one click. On SP, matched detail pages appear there as 10-character ASINs. The v1 matched-target dimension is Sponsored Display only. Sources: [official] Ads API guide *Search term reports* (v3); [official] *A guide to targeting with Sponsored Products*; [official] Ads API guide *Matched target (Targeting)*.

**P-keyword-and-product-targeting-34.** Brand Analytics Top Search Terms gives a marketplace-wide search frequency rank with the top three clicked products and their click and conversion shares. Search Query Performance gives query volume and the brand's share of impressions, clicks, cart adds and purchases, for queries "relevant to your branded catalog". Both require Brand Registry. Neither is part of the Ads API. Sources: [official] sell.amazon.com *What is Amazon Brand Analytics?*; [official] SP-API docs *Analytics Reports*; [official] amzn schemas for both reports.

**P-keyword-and-product-targeting-35.** Third-party keyword search volumes are estimates. Helium 10 and Jungle Scout each published a test favouring themselves, each on one brand's 22–31 keywords: Helium 10's Bradley Sutton scores his tool against Brand Analytics order and Jungle Scout against SQP, and Jungle Scout's Brian Connolly scores both tools against SQP volume. Sources: [opinion] Helium 10, Bradley Sutton (2024-08-23); [opinion] Jungle Scout, Brian Connolly (2024-03-21).

**P-keyword-and-product-targeting-36.** Amazon's keyword translation combines machine translation, professional linguists and closest local matching terms, for up to 1,000 keywords at once. Only the translated keyword targets. Original and native-language keywords are kept "for reporting purposes" and do not target. Sources: [official] Help *Keyword translation* (GHPTCVTGNFZ2KTSP); [official] Ads API guide *Keyword targeting overview*; [official] SP 3.0 model.

**P-keyword-and-product-targeting-37.** Valid keyword scripts and symbols differ by marketplace. Arabic script and `%` are valid only in AE, SA and EG. Devanagari and Tamil are valid everywhere except AE, SA and EG. Keywords are at most 80 characters and 10 words. Sources: [official] Ads API *Limits*.

**P-keyword-and-product-targeting-38.** Amazon publishes SP, SB and SD minimum and maximum bids per marketplace and currency on the Ads API limits page. On 2026-11-09 the SP minimum was 0.02 in USD, CAD, GBP, EUR, AUD and SGD, 2 in JPY and 1 in INR. These figures are for human readers only, and the page contains at least one apparent error (EG SP maximum 5.50). Sources: [official] Ads API *Limits*.

**P-keyword-and-product-targeting-39.** Amazon requires keywords and product targets to be relevant to the advertised product, and lists restricted targets: prescription drugs, offensive terms, and products it does not advertise. A restricted target may be accepted at creation, but "ads won't run against those targets". Sources: [official] Help G3XAU5G7C2JTNQTM; [official] *A complete guide to Sponsored Brands and display ads moderation*.

**P-keyword-and-product-targeting-40.** Amazon forbids naming competitors in ad creative and allows "a leading brand". It forbids keywords containing another company's brand or trademark only for reserve share of voice. No Amazon ads page read on 2026-11-09 states a rule on other companies' trademarks as auction keywords. Amazon's own targeting guide names "Conquest: target competitors' products" as a strategy and says "your competitors may be bidding on your branded keywords, too". Sources: [official] moderation guide; [official] Help GTEEH3E3J2BDELBA; [official] Help *Branded keyword guidelines and keyword suspension* (G2QZJUGUT4RGLJ6N); [official] *A guide to targeting with Sponsored Products*.

**P-keyword-and-product-targeting-41.** Reserve share of voice gives "a fixed, upfront price" for SB top of search on 5 to 1,000 branded keywords. Amazon rejects a reserved keyword when, among other reasons, the brand or trademark "is not yet registered with Amazon Registry" or the keyword contains another company's brand; keywords not mapped to a relevant ad within 14 days of the start are removed. Once the campaign starts, its keywords, duration and budget cannot change. Amazon's pages differ on its flight (15–92, 30–92 or "e.g., 14–90" days), its US minimum ($3,000 budget or "$6K" spend) and its marketplaces (Ireland on one list, Egypt on another); all omit Spain (figures as of 2026-11-09; `beyond/brand-defense-and-competition.md` owns them). Sources: [official] Help *Reserve keywords in a Sponsored Brands campaign* (G86SD7HK6NHHRB9B); [official] Help G2QZJUGUT4RGLJ6N; [official] Help *Create a Sponsored Brands campaign* (GF86HBCNDJUAC5WN); [official] Help *Campaign goals for Sponsored Brands* (GXXPFXLSVX9VD3U9); [official] Ads API guide *Reserve share of voice*; [official] library guide *How to set up Amazon Sponsored Brands reserve share of voice*; [official] what's new *Drive top-of-search visibility and engagement*; [official] SB v4 model.

**P-keyword-and-product-targeting-42.** SD contextual targets with refinements, or individual products, serve on Amazon only. Unrefined categories and "similar to advertised products" also serve off Amazon. The console adds "similar to advertised products" automatically; the API does not. Sources: [official] Help *Understand contextual targeting in Display* (GNTK7LTYZS3KSTAN); [official] Ads API guide *Sponsored Display dynamic segments overview*.

**P-keyword-and-product-targeting-43.** SD audience campaigns always exclude shoppers who bought the advertised or similar products in the past 30 days. Views remarketing looks back up to 90 days and purchases remarketing up to 365. Remarketing and contextual targeting need the advertiser to sell on Amazon; non-sellers get in-market and interest/lifestyle audiences. Sources: [official] Help *Understand targeting in Display campaigns* (GPKPWTLW6B8T683N); [official] Help *Understand remarketing audience segments* (G82GQS569JWSVNRB); [official] SD v3 model.

**P-keyword-and-product-targeting-44.** On Amazon's unified console, contextual targeting "is no longer a standalone feature". It is part of multi-signal targeting, which combines contextual and behavioural signals for products, in-market categories and keywords. Policy-restricted items remain contextual-only. Sources: [official] Help *Set up multi-signal targeting* (GDTFJ44CQ2QUKX9X); [official] *Introducing Amazon Ads Agent, your AI-powered ad platform*.

**P-keyword-and-product-targeting-45.** Amazon's auctions place "particular value on the ad's expected relevance to the customer". Amazon says "ads with lower bid amounts, but higher relevance to the customer, can and do win". A target sets eligibility; the auction decides which eligible ad shows. Sources: [official] Help *Understand Amazon Ads auctions* (GEXGZNBBWPZZK7P8).

**P-keyword-and-product-targeting-46.** Amazon's published research describes product search matching as behaviour-trained semantic matching. Its stated motive is that lexical matching fails on synonyms, hypernyms, morphological variants and misspellings, the same variants Amazon's ad match types say they cover. The research describes organic search, not the ads matcher. Sources: [research] Nigam et al., *Semantic Product Search* (KDD 2019); [research] Chang et al. (KDD 2021); [research] Reddy et al., ESCI (2022).

**P-keyword-and-product-targeting-47.** Amaldoss, Jerath & Sayedi model broad match as the platform bidding on the advertiser's behalf. Broad match helps advertisers when its accuracy is high. At moderate accuracy, universal adoption is a prisoner's dilemma that erodes advertisers' profits. The model is a theory of web search ads, not an Amazon measurement. Sources: [research] *Marketing Science* 35(2), 2016.

**P-keyword-and-product-targeting-48.** Sponsored Brands ads are manual collections, automatic collections, store spotlight or video. With automatic collections, Amazon picks which of the brand's products show "based on your keyword targets and shopper search queries". For the legacy Product Collection format Amazon gives two dates: from August 2026 creates make a Manual Collection instead, and creates "will return an error" "Post January 2027" (*Deprecations*, API migration guide), while the ListMigrations note and the console help say product collections "will no longer be supported" "Beginning February 2027". Sources: [official] Ads API guide *Sponsored Brands overview*; [official] Help *Create a Sponsored Brands campaign* (GF86HBCNDJUAC5WN); [official] Ads API *Release notes* (2026-09-18, 2026-09-23); [official] *Deprecations*; [official] Ads API *Product Collection Migration Guide*; [official] Help *Migrate from Product collections to Sponsored Brands collections* (GV7N6KZTH4HF4T2P).

**P-keyword-and-product-targeting-49.** Amazon's rule for an advertiser's own duplicates covers one keyword in several match types: "the match type with the highest bid will be used for any matching shopping query", and its targeting guide adds "you won't be bidding against yourself by adding different match types on the same keyword". Neither page says whether this reaches across ad groups or campaigns, or how Amazon chooses among different keyword texts, product targets or auto targets of one advertiser that match one query. AMALYZE says Amazon chooses among duplicates by "the highest expected bid and expected click-through rate (CTR)"; Ad Badger says two of a seller's products in different ad groups can both serve on one results page without "bidding against yourself". Sources: [official] Help *Understand keyword match types* (GHTRFDZRJPW6764R); [official] *A guide to targeting with Sponsored Products*; [official] Help *Understand Amazon Ads auctions* (GEXGZNBBWPZZK7P8); [opinion] AMALYZE, *Duplicate Keywords in Amazon PPC*; [opinion] Ad Badger, *Amazon PPC Keyword Cannibalization*.

**P-keyword-and-product-targeting-50.** An SD audience target is written as `audience` with `audienceSameAs` set to an Amazon audience id. Amazon lists SD audience ids with `POST /audiences/taxonomy/list` (category tree with audience counts) and `POST /audiences/list` (filters `audienceName`, `category`, `categoryPath`, `audienceId`, `status`; `canTarget` for targetable only), and overlaps with `GET /insights/audiences/{audienceId}/overlappingAudiences`. The `views(…)` and `purchases(…)` remarketing clauses take ASINs or categories and a lookback, not an audience id. Sources: [official] OpenAPI model *Audiences*; [official] Ads API guide *Sponsored Display audience targeting*; [official] SD v3 model.

**P-keyword-and-product-targeting-51.** The ids for SP `shopperCohortBidding` and SB audience boosts come from `POST /targetableEntities/list` with `adProduct`, `targetTypeFilter` `AUDIENCE` and a `pathsFilter`: `["Audience Category","Custom-built","Product"]` for Amazon-built audiences and `…"AMC"` for AMC audiences; Amazon says "Only the audiences retrieved using these filters are usable". The SP segment type field is deprecated and inferred from the id, and an SP cohort entry takes exactly one segment. The Audiences API's `adType` has no SP or SB value. Sources: [official] OpenAPI model *Targetable Entities*; [official] SP 3.0 model (`SponsoredProductsAudienceSegmentType`, `SponsoredProductsShopperCohortBidding`); [official] Ads API guide *Shopper cohort bidding* (SB); [official] Ads API *Release notes* (2025-02-28, 2025-03-12, 2025-03-24, 2025-08-22); [official] OpenAPI model *Audiences*.

**P-keyword-and-product-targeting-52.** Product Opportunity Explorer is a Seller Central tool that groups search terms into niches "based on the products customers view or purchase after searching" and shows each niche's top search terms with search volume, click share, search conversion rate and the top three clicked products, plus Customer Review Insights and return reasons. Niche metrics refresh weekly and new niches appear monthly. Amazon's pages name a Professional selling account and do not name Brand Registry; its search terms are not limited to queries where the seller's brand appeared. Sources: [official] seller guide *Product Opportunity Explorer overview*; [official] sell.amazon.com *Product Opportunity Explorer*; [official] sell.amazon.com blog *Get product ideas with Product Opportunity Explorer*.

**P-keyword-and-product-targeting-53.** The SP-API Customer Feedback API "provides the same information as the Product Opportunity Explorer (OX)" for reviews and returns only: review topics and trends per ASIN and browse node, return topics and trends per browse node, in the US, UK, FR, IT, DE, ES and JP, refreshed weekly, in English. No API read on 2026-11-09 returns POE's niche search terms or volumes. Sources: [official] SP-API *Customer Feedback v2024-06-01* reference and changelog; [official] `customerFeedback_2024-06-01.json`.

**P-keyword-and-product-targeting-54.** Reverse-ASIN tools list the queries a given ASIN ranks for organically and in sponsored slots, with the vendor's own volume estimate. Helium 10 (Cerebro) and Jungle Scout (Keyword Scout) each take up to 10 ASINs; SellerSprite says its list covers keywords that put a product in "the top 3 pages of search results in the past 30 days"; EcomCrew says DataDive pulls from Helium 10, Keepa, Google Trends and Seller Central. None of these is Amazon data. Sources: [opinion] Helium 10, *Cerebro*; [opinion] Jungle Scout, *Keyword Scout*; [opinion] SellerSprite, *SellerSprite vs DataDive 2026*; [opinion] EcomCrew, *DataDive Review and Case Study*.

**P-keyword-and-product-targeting-55.** Practitioners disagree on Product Opportunity Explorer's terms: AMALYTIX's Trutz Fries says Brand Registry is not required, AMALYZE says it serves Brand Registry sellers and vendors; Intentwise gives 360-day windows for volume, click share and conversion, Goat Consulting's Eric Sutton gives 90 days, and AMALYTIX says the screen shows today, 90 and 360 days; Intentwise lists five marketplaces and AMALYTIX (October 2026) more. Sources: [official] *Product Opportunity Explorer overview* (no window stated); [opinion] AMALYTIX; [opinion] AMALYZE glossary; [opinion] Intentwise; [opinion] Goat Consulting.

**P-keyword-and-product-targeting-56.** The Ads API accepts hiragana, katakana, kanji and half-width/full-width forms in keywords in every marketplace, and counts keyword length in "parts" (10 for a positive keyword, 4 for a negative, 10 for negative exact) without defining a part. No Amazon page read states whether match types or negatives normalise Japanese script variants, full-width against half-width characters, or spaced against unspaced text. Sources: [official] Ads API *Limits*; [official] ja-jp library guides *キーワードターゲティングとは何ですか？* and *スポンサープロダクト広告のターゲティングに関するガイド*.

**P-keyword-and-product-targeting-57.** Amazon's Japanese guides show phrase match finding a keyword inside unspaced text: phrase 「ランニングシューズ」 can show for 「女性用ランニングシューズ」 but not 「ランニング用シューズ」, and phrase 「Dopplerコットンシーツセット」 for 「キングDopplerコットンシーツセット」. Sources: [official] ja-jp library guide *キーワードターゲティングとは何ですか？*; [official] ja-jp library guide *スポンサープロダクト広告のターゲティングに関するガイド*.

**P-keyword-and-product-targeting-58.** Amazon's German guide says an SP phrase keyword „Laufschuhe" serves „Laufschuhe für Damen" but not „Schuhe zum Laufen", and that in SB semantic matching a search for „Laufschuhen" can reach keywords „Joggingschuhe" and „Schuhe zum Laufen". No Amazon page read states whether SP broad or exact bridges a compound and its split or hyphenated form; AMALYZE lists hyphenation as a close variant. Sources: [official] de-de library guide *Was ist Keyword-Targeting?*; [official] de-de library guide *Ein Leitfaden zum Targeting mit Sponsored Products*; [opinion] AMALYZE, *Close Variant* glossary.

**P-keyword-and-product-targeting-59.** Amazon researchers report that Amazon's Japanese query reformulation normalises script variants ("こども" to "子供"), tokenises unspaced queries and sorts tokens, excluding brands and media titles, and that adding the ads matched for reformulated queries to a query's match set raised Ads revenue 0.36% in a two-week Japanese A/B test. The paper does not describe advertiser match types or negatives. Sources: [research] Zhang et al., *Towards Scalability and Extensibility of Query Reformulation Modeling in E-commerce Search* (CIKM 2024, arXiv 2402.11202).

**P-keyword-and-product-targeting-60.** In May 2026 Amazon brought Rufus and Alexa+ together as Alexa for Shopping on the US Amazon app, website and Echo Show. Existing sponsored ads campaigns are automatically eligible to serve in Alexa for Shopping and to be optimized as prompts that open conversations with it; on Alexa+ devices, advertisers with sponsored ads campaigns are automatically enrolled in Alexa+ Conversational Ads. None of these surfaces has a target type of its own. Sources: [official] aboutamazon *Meet Alexa for Shopping* (2026-05-13); [official] *What agentic shopping means for advertising* (2026-06-11); [official] Ads API *Release notes* (2024-09-05, 2025-07-15).

**P-keyword-and-product-targeting-61.** Amazon publishes Sponsored Brands targeting across three models: the SB v3 YAML holds `/sb/keywords`, `/sb/negativeKeywords`, `/sb/targets`, `/sb/negativeTargets` and `/sb/themes`; the *Sponsored Brands 3.0* JSON and the SB v4 JSON hold `/sb/targets/categories`, `/sb/targets/products/count` and `/sb/negativeTargets/brands/recommendations` (media type `application/vnd.sbtargeting.v4+json`, US, CA, MX, UK, DE, FR, ES, IT, IN, JP). Sources: [official] OpenAPI models *Amazon Ads API - Sponsored Brands* 3.0 (YAML), *Sponsored Brands 3.0* (JSON) and *Sponsored Brands campaign management 4.0*.

**P-keyword-and-product-targeting-62.** In Sponsored Brands, auto collections take keyword targeting only and manual collections take keyword or product targeting. Amazon says un-migrated product collection ads with 3 ASINs will be moved to manual collections with the same ASINs, those with fewer than 3 will not, and a launched replacement runs beside the legacy ad for 4 weeks before the legacy ad is archived. Sources: [official] Help *Migrate from Product collections to Sponsored Brands collections* (GV7N6KZTH4HF4T2P).

**P-keyword-and-product-targeting-63.** Randomized field experiments outside Amazon find retargeting incremental for the advertisers studied: 14.6% more users returned within four weeks, with the effect falling as time since the visit grows and a third of the first week's effect on day one (Sahni, Narayanan & Kalyanam, a home-improvement seller), and visits up 17.2% and purchases up 10.5% (Johnson, Lewis & Nubbemeyer, an online retailer). Sources: [research] Sahni, Narayanan & Kalyanam, *JMR* 2019; [research] Johnson, Lewis & Nubbemeyer, *JMR* 2017.

**P-keyword-and-product-targeting-64.** Field experiments find that showing the exact product a shopper viewed is not always the better retargeting ad: an online travel firm's dynamic retargeted ads did worse on average than generic brand ads, except once browsing suggested refined preferences (Lambrecht & Tucker), and highly personalised banners worked best right after a store visit and lost effect quickly, with medium personalisation better over time and view-through gains only on context-congruent sites (Bleier & Eisenbeiss). Sources: [research] Lambrecht & Tucker, *JMR* 2013; [research] Bleier & Eisenbeiss, *Marketing Science* 2015.

**P-keyword-and-product-targeting-65.** Published web-search studies disagree on how conversion rate moves with ad position: Ghose & Yang find it highest at the top, Rutz, Bucklin & Sonnier find higher positions raise both click-through and conversion, and Agarwal, Hosanagar & Smith find conversion rate rises lower on the page. Narayanan & Kalyanam show naive position comparisons are inflated by auction selection, find much smaller effects at only some positions, and find them weaker for brand- or product-specific keywords and exact match. None of the four is on Amazon. Sources: [research] Ghose & Yang, *Management Science* 2009; [research] Rutz, Bucklin & Sonnier, *JMR* 2012; [research] Agarwal, Hosanagar & Smith, *JMR* 2011; [research] Narayanan & Kalyanam, *Marketing Science* 2015.

### Seat's positions (enter no skill)

- [seat] The match type is a statement of eligibility that Amazon interprets with the advertised products as context. Reading a target's performance means reading the search terms it matched, not its keyword text.
- [seat] Every Amazon-maintained target set (auto groups, expanded ASINs, SB themes, keyword groups, SD similar products, multi-signal) moves the choice of query or page from the advertiser to Amazon. The advertiser keeps the bid, the negatives and the pause. The reports are where the choice becomes visible.
- [seat] Where Amazon's pages conflict, the help center (dated and most recently edited) and the API models (enforced) are the stronger texts. The undated library guides and blogs are the weaker. The API's per-item reply settles API questions on the day.
- [seat] Amazon publishes no query volume in the Ads API. Amazon's query volumes are SQP's (only queries where the brand already appears) and Product Opportunity Explorer's (a niche's top queries, on a Seller Central screen). A volume for any other query is a third-party estimate. (Corrected in the gap fill of 2026-11-09.)
- [seat] SD views and purchases remarketing reach shoppers who have already engaged; the retargeting experiments read (P-63, P-64) are the evidence that such ads can be incremental and that their effect decays with time since the visit. No experiment on SD itself was read.
- [seat] The figures in this file (keyword counts, test windows, thresholds) are Amazon's guidance or a vendor's single-account data. They describe what Amazon or a firm said, not a rule for a seller.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** Every page in *Pages read* was re-opened on 2026-11-09 by plain GET, none sampled:
- the 33 help-center articles, with text read from each page's `window.__scV2Content` and `lastModified` checked;
- the 9 library, blog, what's-new, solutions and news pages;
- the 31 Ads API guide pages as markdown on d3a0d0y2hgofx6.cloudfront.net, including the full release notes;
- the 8 OpenAPI models, with enums, field descriptions, `maxItems` and operation texts read from the JSON or YAML;
- the SP-API analytics reports page and both amzn report schemas, and sell.amazon.com;
- the 11 practitioner pages, the 5 arXiv/GitHub/Amazon Science pages and the 4 EconPapers/IDEAS records.

Each quoted string was matched against the page text after whitespace and quote normalization, and each figure, enum and path was checked against its source. The release notes and the Ads API v1 release notes were read for 2025–2026 changes that overturn a claim. A web search on competitor trademarks as keywords turned up no Amazon page carrying a rule. Pages listed as unreachable were tried again.

No call was made to any Ads API host (advertising-api*.amazon.com), Login with Amazon, the Amazon Ads MCP server, any SP-API host, or the Seller Central help content call. Only public documentation hosts were fetched.

**Corrections (was → now).**
1. Item A, SB themes: cited to Help *Create a Sponsored Brands campaign* → that page does not mention themes; now cited to the release notes of 2023-08-17 (US) and 2023-12-11 (all regions).
2. Item A, strategy names: the seat's paraphrases ("reach new shoppers", "new products or a range", "complements") → Amazon's own words for each strategy, quoted.
3. Item B, keyword kinds: "competitor keywords" said to be named by *What is keyword targeting?* → not on that page. The kinds are now quoted from both guides: generic, branded (incl. "trademark terms"), non-branded, category short-tail/long-tail, and complementary (Help GK3MNACNTXG659J9). The targeting guide's "your competitors may be bidding on your branded keywords, too" is added.
4. Item E, v1 negatives: "`matchType` is `EXACT` or `PHRASE`" → the guide's examples show only `EXACT` and state no rule, while the enum carries `BROAD`/`EXACT`/`PHRASE`. Guide name corrected to *Negative keyword targeting*; open question 20 added.
5. Item F: "the same four are described in Help *Understand targeting*" → that page does not list the four groups.
6. Item F: "what auto reads" from an undated library guide was tagged RULE → GUIDANCE, with the full sentence quoted.
7. Item F: `autoCreateTargets` "on the ad group" → in the campaign's `autoCreationSettings`.
8. Item F, negatives in auto: the non-verbatim quote ("affect product attribute or auto targets…") → the verbatim help text. "Negative keywords apply to auto ad groups as well", unsupported on the cited page, is now sourced to *What is keyword targeting?* and the 2025-05-22 release note.
9. Item G: "Each [refinement field] has a `…Resolved` read-back field" → only the four id fields do. The `MULTISIGNAL_BROAD` description is added.
10. Item G, limits: omitted "Keywords in an ad group (excluding negative keywords): 1,000 for manual targeting" → added.
11. Item I: the invented quote "Only one theme per themeType per adGroup" → the model's verbatim "only one target can be created for each themeType per adGroup".
12. Item I: `ACQUIRE_NEW_CUSTOMERS` and `AD_VIEWS` listed as goal values → marked "PREVIEW ONLY and cannot be used as part of a request or response". The SB v4 note that goal-based campaigns are not supported in IE is added (also in item N).
13. Item J: "`biddingStrategy`… shapes the bids returned, not the keywords" (seat inference) → the model's sentence. Guide name corrected to *Sponsored Products keyword recommendations*. The guide's "integrate with version 5" note and its statement that impact metrics "are not estimates of expected performance" are added.
14. Item J, open question 8, P-27, stable item 13: `DEFAULT` "unnamed" → Amazon's text says it "ranks recommendations by our interal ranking mechanism".
15. Item J: `bidInfo` "up to three entries" → three in the v3/v4 shape, up to 15 in v5 (`ThemedBid`).
16. Item J: the *Recommendations* model was labelled "DSP-only; not used for SP targeting" → it is the sponsored-ads tactical recommendations API (2023), with NEW_KEYWORD, NEW_NEGATIVE_KEYWORD, NEW_PRODUCT_TARGETING and other types. A subsection, a run-time row and open question 21 are added. The v1 types page's `INVALID_RECOMMENDATION_TYPE` note is added.
17. Item K, formats: "product collection (manual or automatic), store spotlight and video" → the SB overview's "manual collection, automatic collection, store spotlight, or video". The legacy Product Collection ends February 2027 (release note 2026-09-18), and Collections went worldwide on 2026-09-23. New P-48.
18. Item K, reserve SOV: added the "fixed, upfront price" wording, the SB create page's "map keywords to a relevant ad within 14 days… will be removed" and "can't be reserved in multiple campaigns or ad groups", and the v1 API path (`/adsApi/v1/create/recommendations/sb` `BRANDED_KEYWORD`, `keywordReservationValidations/sb`, `advertisingDealTargets/sb`). P-41 reworded: "must be in Brand Registry" is now Amazon's rejection reason, quoted; sources added.
19. Item L: SD contextual predicates "tactic `T00020`" → usable under `T00030` and, for contextual campaigns, `T00020`. DVA+ "rolling out… beginning in late October" added.
20. Item M: "with at least one click" (not verbatim) → "that resulted in at least one click on your ad".
21. Item P and P-40: "competitor keywords" as Amazon guidance → removed; replaced by the targeting guide's sentence on competitors bidding on branded keywords.
22. Item R: the US bulksheet column `Off-Amazon ad serving` (2026-06-08) is added.
23. Seat notes worded as instructions to a skill (items G ×2, L, M, N, O: "A skill reads…", "A skill does not use it…", "never a constant in a skill") → restated as facts.
24. Practitioners, Helium 10: "given as a weekly 'velocity'" and "93.5%… versus Jungle Scout's 41.9%" against Brand Analytics → Sutton shows a monthly figure as a "velocity" based on the latest week. His 93.5% is Helium 10's order against Brand Analytics; his 41.9% is Jungle Scout's order against SQP. The seat note and P-35 are corrected to match.
25. Page names: *Introducing Amazon Ads Agent* → *Introducing Amazon Ads Agent, your AI-powered ad platform*; *Keyword recommendations* → *Sponsored Products keyword recommendations*; *Negative keywords* → *Negative keyword targeting*. `lastModified` added for *Set up product targeting* (2026-02-20) and *Policies and guidelines* (2025-10-21).
26. *Pages read*: rows added for the Reserve share of voice API guide and the Ads API v1 release notes. The policy redirect target is now named in *Unreachable* (301 to G2NN8D3LSUR9V9EA, the Support Center Homepage).

**Removals.**
1. The claim that Amazon's keyword-targeting guide names "competitor keywords", in item B, item P and P-40.
2. The "DSP-only" description of the *Recommendations* model.

No position was worded as behaviour (when to ask, a fixed sequence, a threshold as a rule, a ceiling, or how cx talks). P-17's segmentation advice is attributed to Ad Badger. No position was unsourced, so none moved to the seat's list.

**Confirmed unchanged.** All match-type, negative, auto-group, expanded-targeting, SD, SIS, SQP/TST, keyword-limit and bid-table figures matched their pages on 2026-11-09. That includes the EG SP maximum 5.50, still on the limits page. The release notes since 2025 (Reporting API v1 GA 2026-09-30, Recommendations API 2026-08-31, MCP server, SB Collections) contain nothing that overturns a targeting rule in this file.

**Still unreachable on 2026-11-09.**
- Search Engine Land match-type article (403, also via a fetch tool).
- Pacvue match-type page (403).
- Helium 10 match-type page and Teikametrics product-targeting page (404).
- sell.amazon.com/tools/brand-analytics (404).
- Library guides keyword-research, negative-keywords and product-targeting (404).
- The cloudfront guides listed in *Unreachable*, rechecked for theme-based-targeting, global-campaigns, campaign-management/entities/targets and localization/overview (404).
- The tactical-recommendations overview and get-started guides (404).
- The ESCI paper PDF: downloaded, but the local PDF tools still fail on a missing library, so the label definitions remain unread.
- The paywalled full texts of the three journal papers.

### Gap fill 2026-11-09

Done by the research seat on 2026-11-09 in answer to three completeness critics. Every page cited for a new or changed claim was opened that day by plain GET (help pages through their `window.__scV2Content` JSON, API guides as cloudfront markdown, models as JSON or YAML, papers through OpenAlex and arXiv); a fetch tool was used only where noted in *Unreachable*. No Ads API host, Login with Amazon, MCP endpoint, SP-API host or Seller Central content call was touched. This part awaits the verifier like the rest.

**Gaps filled.**
1. Product Opportunity Explorer and reverse-ASIN tools (gap 1). Added to item M: the seller guide PDF, the sell.amazon.com tools page and blog (niches, search terms with volume, click share and search conversion rate, Customer Review Insights, returns, refresh cadence, Professional account, no Brand Registry named), and the SP-API Customer Feedback API as the only API carrying POE's review and return data. Added to *What practitioners add*: Helium 10 Cerebro, Jungle Scout Keyword Scout, DataDive (through EcomCrew and SellerSprite; DataDive's own support pages were unreachable), and POE as read by AMALYTIX, Intentwise, Goat Consulting and AMALYZE, with their disagreements. Run-time rows, stable item 24, P-52 to P-55. The earlier claim that SQP is Amazon's only query volume is corrected in the practitioners' seat note and the seat's positions. The gap's statement that POE is "available to sellers without Brand Registry" is carried as: Amazon's pages name a Professional selling account and do not name Brand Registry; AMALYTIX says it is not required and AMALYZE says it serves Brand Registry sellers.
2. Unspaced Japanese and German compounds (gap 2). Added to item N: Amazon's character ranges and "parts" limits (the limits page), Amazon's ja-jp guide examples showing phrase match inside unspaced text, Amazon's de-de guide examples on a compound against separate words (SP phrase no; SB semantic yes), the record that Amazon is silent on script, width and compound normalisation in match types and negatives, and Amazon's own CIKM 2024 paper on Japanese query normalisation in search Ads matching. JP and DE practitioner pages read add nothing on normalisation; that is recorded, with the unreachable ones. Open questions 22–24, P-56 to P-59.
3. Retargeting research (gap 3). Added to *Published research*: Lambrecht & Tucker (JMR 2013), Sahni, Narayanan & Kalyanam (JMR 2019), Bleier & Eisenbeiss (Marketing Science 2015), and Johnson, Lewis & Nubbemeyer (JMR 2017, a retailer's display retargeting campaign), with the transfer to SD lookbacks, exact versus similar views audiences, and placement. P-63, P-64, and a seat note.
4. Audience id discovery (gap 4). Added to item L: the Audiences API (`/audiences/taxonomy/list`, `/audiences/list`, overlapping audiences) for SD and DSP, the Targetable Entities API (`/targetableEntities/list`, `/targetableEntities/paths/list`) for SP, SB and SD with its request filters and entity fields, the `pathsFilter` values Amazon names for Amazon-built and AMC audiences, and the v1 `AudienceTarget`/`AudienceBidAdjustment`. Run-time rows, stable item 23, P-50, P-51. `areas/bids-and-placements.md`'s "targetable-entities listing" is the path `POST /targetableEntities/list`.

**Contradictions settled or aligned.**
1. Rufus and Alexa+ (owner `beyond/ad-products-and-eligibility.md`). Re-read aboutamazon (2026-05-13) and the Ads page *What agentic shopping means for advertising* (2026-06-11): Rufus and Alexa+ were brought together as Alexa for Shopping in the US; campaigns are automatically eligible there; Alexa+ Conversational Ads run on Alexa+ devices with automatic enrolment. Item R now carries this, its heading names Alexa for Shopping, and the 2024 and 2025 notes are marked dated history. Stable item 25, P-60. [seat] The ad-products file's note that "Alexa for Shopping" appears on no ads page is contradicted by the Ads page above.
2. Reserve share of voice (owner `beyond/brand-defense-and-competition.md`). Re-read the help pages, the library guide and the what's-new page: three flights (15–92, 30–92, "e.g., 14–90" days), two US minimums ($3,000 budget, "$6K" spend), and marketplace lists that differ on Ireland and Egypt, all without Spain. Item K, open question 17 and P-41 now carry the spread and point to the owner. This file never stated a single flight as fact; P-41 had named only the keyword count and Spain.
3. and 5. SB Product Collection end date (owner `method/ads-api-surface.md`). Re-read *Deprecations*, the API migration guide, the ListMigrations note and the console help page GV7N6KZTH4HF4T2P (lastModified 2026-10-05). The API pages say creates "will return an error" "Post January 2027"; the release note and the help page say "Beginning February 2027, product collections will no longer be supported"; creates map to Manual Collection from August 2026. The run-time row, item K and P-48 now carry both dates. Added from the help page: auto-migration of 3-ASIN ads, the 4-week overlap, and auto collections being keyword-only (stable item 26, P-62).
4. Which SB spec carries which negative path (owner `method/ads-api-surface.md`). Re-read all three SB models. `/sb/negativeKeywords` is in the cloudfront SB v3 YAML (26 paths) and not in the *Sponsored Brands 3.0* JSON (50 paths); `/sb/negativeTargets/brands/recommendations` is in the *Sponsored Brands 3.0* JSON and the SB v4 JSON (48 paths), under `application/vnd.sbtargeting.v4+json`, and not in the v3 YAML. Each sibling file was right about the model it read. Item J, a run-time row, P-61 and open question 26.
6. Self-competition (owner: this file). Re-read the help sentence and the targeting guide in context. Answered: one keyword in several match types (highest bid used; "you won't be bidding against yourself by adding different match types on the same keyword"). Not answered by any Amazon page: whether that reaches across ad groups or campaigns, and different keyword texts, product or auto targets matching one query. AMALYZE and Ad Badger added as named claims. Item Q, open question 19 and P-49. For `method/change-measurement.md` open question 3 and `areas/campaign-structure.md` open question 2: the match-type case is answered; the cross-campaign case is still open on Amazon's pages.
7. Position and conversion rate (owner `areas/bids-and-placements.md`). Re-read the four abstracts through OpenAlex. Ghose & Yang: conversion highest at the top (Google, one retailer). Rutz, Bucklin & Sonnier: higher positions raise both CTR and conversion (lodging chain, latent instrument). Agarwal, Hosanagar & Smith: conversion rate "increases with position", meaning it rises lower on the page (retailer, field experiment). Narayanan & Kalyanam: naive estimates are biased by auction selection, which randomizing one's own bids does not remove; RD effects are much smaller, at some positions only, and weaker for specific and exact-match keywords. The disagreement is across settings and methods; none is on Amazon. *Published research* section and P-65; the Ghose & Yang entry points there.

**Declined.** None. Every gap was right that the file lacked the item. Gap 2 is filled with Amazon's silence recorded as such, not a rule.

**Pending verification.**
