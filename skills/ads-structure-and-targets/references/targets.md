# Keywords and targets

Search terms and negatives are ../ads-search-terms/SKILL.md's; the search term report is in ../ads-review/references/reports.md.

## Match types

- Broad, phrase and exact all account for plurals, misspellings and translations. (T23)
- Broad matches the terms in any order, with synonyms and related terms. (T23)
- Amazon's own exact example matches "outside lights" to "outdoor lights", its guides disagree on whether exact tolerates reordering, and no match type is a literal string match. (T23)
- Where no search term exists, Amazon infers one from context and serves keywords there, and the report shows such inferred terms unmarked beside typed ones. (T24)
- Sponsored Brands keywords add semantic matching on the same meaning or intent, even in phrase match, and accept a `+` modifier in broad. (T25)
- Sponsored Brands negatives take exact and phrase only, with limits of 10 words per keyword and 4 per negative phrase. (T25)

## Compounds, scripts and spacing

- Amazon's Japanese guides show phrase match finding a keyword inside unspaced text. (T26)
- Amazon's German guide shows phrase „Laufschuhe" serving „Laufschuhe für Damen" but not „Schuhe zum Laufen", which Sponsored Brands semantic matching can reach. (T26)
- No Amazon page read states whether SP broad or exact bridges a compound and its split or hyphenated form, which AMALYZE lists as a close variant. (T26)
- Amazon researchers report that Amazon's Japanese query reformulation normalises script variants and tokenises unspaced queries, in a paper that does not describe advertiser match types or negatives. (T26)

## One keyword, several entries

- When one keyword is set in several match types with different bids, the match type with the highest bid is used, and Amazon's page says the advertiser is not bidding against itself. (T22)
- Amazon's pages read do not say whether this reaches across ad groups or campaigns, to same-match-type copies, or to different keywords and targets of one advertiser matching one query. (T22)
- Amazon's targeting guide says bids set by product priority give the top-priority product "the best opportunity to get top ad placements". (T22)
- Practitioners disagree on how a seller's own campaigns meet on one query, and none cites an Amazon page or measured data. (T22)

## Auto campaigns

- An SP auto campaign targets through four groups: close match and loose match on search queries, substitutes and complements on detail pages. (T5)
- The four groups can be paused or bid but not archived, and v1 names them `THEME` targets. (T5)
- Amazon says auto reads the product's titles and descriptions; ClearAds says bullets and backend terms too. (T5)
- Ad Badger says close match takes most of an unsegmented auto campaign's traffic. (T5)

## Product and category targets

- An SP product target holds one ASIN and is exact or expanded ("similar"); expanded is the console default and adds "a limited number of additional products with the highest performance potential" that Amazon chooses. (T27)
- Amazon says a product target appears on the targeted product's detail page and on search result pages where that product ranks among the top results. (T27)
- In one seller's 2020 placement data published by Perpetua, 85–92% of category, ASIN and brand targeting fell on detail pages. (T27)
- Category targets refine by brand, price range and star rating in SP, SB and SD, and by Prime shipping, age range and genre in SP and SD. (T28)
- Sponsored Brands has no expanded-ASIN target. (T28)

## Amazon-built targets

- Sponsored Brands theme targets are keywords related to the brand or to the landing pages, which Amazon generates "based on historical performance and brand interactions", and a goal-based campaign creates them by default. (T29)
- SP keyword groups (beta, US only on 2026-11-09) are Amazon-maintained keyword sets built from the advertised ASINs and refreshed over time. (T29)
- The v1 theme for peer brands' category searches picks the peer brands automatically, and the pages read do not say which ad product accepts it. (T29)

## Recommendations and keyword sources

- SP keyword recommendations rank by `CLICKS`, `CONVERSIONS` or `DEFAULT` and carry no search volume. (T30)
- Amazon says keyword recommendations draw on past performance and similar products. (T30)
- Product recommendations come in themes. (T30)
- The v2 suggested-keyword endpoints were shut off in June 2026. (T30)
- Third-party keyword volumes are estimates, and Helium 10 and Jungle Scout each published a test favouring itself. (T33)
- Reverse-ASIN tools list the queries an ASIN ranks for. (T33)
- Product Opportunity Explorer groups search terms into niches, and practitioners disagree on its access terms. (T33)
- The Customer Feedback API returns an ASIN's top review topics. (T33)

## Relevance

- Keywords and product targets must be relevant to the advertised product, and Amazon lists restricted targets. (T34)
- Amazon's auctions weigh the ad's expected relevance to the shopper. (T34)

## Research on matching

- Amazon's published research describes organic product search matching as behaviour-trained semantic matching, motivated by lexical matching's failures on synonyms, morphological variants and misspellings, and does not describe the ads matcher. (T40)
- Amaldoss, Jerath and Sayedi model broad match as the platform bidding on the advertiser's behalf, helping advertisers when its accuracy is high and a prisoner's dilemma at moderate accuracy, in a theory of web search ads, not an Amazon measurement. (T40)
