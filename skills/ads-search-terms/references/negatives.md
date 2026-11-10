# Negatives

## What a negative stops

- Negative keywords stop ads on search pages for matching queries. (S5)
- Negative ASIN and brand targets stop ads on those detail pages and act only on product-attribute and automatic targets. (S5)
- These targets act in the ad group or, at campaign level, in every ad group, and they can name the advertiser's own pages or a competitor's. (S5)
- Amazon states a buffer before a negative takes effect: up to 72 hours for negative keywords and 96 hours for negative products. (S8)

## Levels

- Negatives exist at two levels only, ad group and campaign (`TargetLevel` `AD_GROUP`, `CAMPAIGN`). (S6)
- In Sponsored Products a campaign negative keyword applies to every ad group of the campaign, and an ad-group one to that ad group only. (S6)
- Sponsored Brands has "no campaign-level negative targeting", and Sponsored Display negatives are ad-group level. (S6)
- Each Sponsored Products bulksheet negative row carries its campaign id and, at ad-group level, its ad group id, with match type `negativeExact` or `negativePhrase`; a row with a blank Operation is ignored on upload. (S6)

## Match types

- Negative phrase blocks queries containing "the complete phrase or close variations", and negative exact "the exact phrase or close variation". (S7)
- Negative phrase is limited to 4 words and negative exact to 10, each at most 80 characters; these figures were read from Amazon's help and API limits pages on 2026-11-09. (S7)
- The match type of an existing negative keyword cannot be changed. (S7)
- The console help and bulksheets offer negative exact and phrase only, while the Sponsored Products 3.0 and v1 models also accept a broad negative match type, and one keyword guide mentions "exact, phrase, or broad". (S9)
- AMALYZE writes "There is no negative broad". (S9)
- Practitioners disagree on whether negative phrase is order-sensitive: Ad Badger and Scale Insights say it blocks the words in sequence, JumpFly says in any order. (S19)

## Where negatives are written

- In v1 a negative keyword, ASIN or brand is a target created with `negative: true` on v1's create-targets operation, and v1's query-targets operation filters by `negativeFilter`. (S10)
- Sponsored Products 3.0 writes negatives as ad-group negative keywords, campaign negative keywords and negative targets. (S24)
- Sponsored Brands writes them as negative keywords and negative targets, at most 100 per call. (S24)
- Sponsored Display writes ad-group negative targeting clauses, and the Sponsored Display 3.0 model has no negative keyword operation. (S24)
- The v1 target tables have no Sponsored Display column, while the v1 `AdProduct` enum and the campaign-management overview include it, and no release note of 2026, as read on 2026-11-09, announces it in v1 campaign management. (S24)

## Campaign-level negative product targets

- Three Amazon texts conflict on campaign-level negative product targets in a seller's manual Sponsored Products campaign. (S11)
- The API guide says vendors only. (S11)
- The 2025-05-22 release note says every US campaign and ad group has the same negative options. (S11)
- The Sponsored Products 3.0 model says campaign negative targeting clauses are "only available for AUTO campaigns". (S11, S24)

## Amazon's brand-negative recommender

- Amazon's brand-negative recommender for Sponsored Products and Sponsored Brands includes the advertiser's own brands, "because targeting your own brands usually results in lower performance than targeting competitors' brands". (S12)
- The statement names no metric and shows no data. (S12)

## Shared lists

- No Amazon model, help page or bulksheet tab read on 2026-11-09 carries a shared negative keyword list or portfolio-level negatives. (S23)
- Karooya wrote in 2019 that "the shared negative keyword list has been missing from Amazon Ads", and its tool adds each list entry as campaign-level negative keywords in every associated campaign. (S23)
- RedHen Labs wrote on 2026-08-27 (read 2026-11-09), naming no marketplace, that it kept 69 campaign-level exact negatives across 43 campaigns. (S23)
- SellerSprite writes that Amazon allows reusable negative keyword lists and that portfolios can carry negatives across campaigns. (S23)
