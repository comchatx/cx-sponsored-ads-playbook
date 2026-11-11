# Sponsored Brands and Sponsored Display

## Sponsored Brands campaigns

- A Sponsored Brands ad group holds one type of ad and targets either keywords or products. (T2)
- Automatic collections take keyword targets only. (T2)
- A Sponsored Brands v4 campaign holds several ad groups with several ads each, and its ad groups carry no bid. (T20)
- Moderation rejects an ad, not the campaign. (T20)
- Legacy v3 campaigns hold read-only ad groups, and a migrated campaign gets a new id, with the old one kept as `legacyCampaignId`. (T20)

## Goals

- Sponsored Brands goal-based campaigns have two goals: drive page visits, on CPC and the default when neither goal nor cost type is sent, and grow brand impression share, on vCPM and measured by top-of-search impression share. (T13)
- Earlier Sponsored Brands campaigns are tagged "Drive page visits". (T13)
- The marketplaces where goal-based campaigns are not supported are named in Amazon's *Sponsored Brands v4* model, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json. (T13)

## Formats

- Sponsored Brands formats are manual and automatic collections (3–10 products, the type fixed once the ad group exists), store spotlight and video. (T38)
- Under drive page visits every format can serve on search, detail pages and the home page. (T38)
- Sponsored Brands video has its own placement and auction, and video creative follows chapters 1 to 5 of Amazon's moderation guide. (T38)
- The ASIN list of a Store page returns only ASINs placed directly on that page. (T38)

## Product Collection retirement

- Sponsored Brands Product Collection ads are being retired: since August 2026 a create makes a Manual Collection ad. (T19)
- Amazon's pages give January 2027 for creates to error and February 2027 for the end of support. (T19)
- The Sponsored Brands v4 migration list returns recommended replacements. (T19)

## Sponsored Brands model files

- Amazon publishes Sponsored Brands targeting across three model files. (T39)
- The SB 3.0 YAML holds the keyword, negative keyword, target, negative target and theme operations. (T39)
- The JSON file titled "Sponsored Brands 3.0" and the SB 4.0 JSON hold the category target, product target count and negative brand target recommendation operations, and neither of those two carries the negative keyword operations. (T39)

## Sponsored Display targets

- Sponsored Display contextual targets with refinements, and single products, serve on Amazon only. (T37)
- Unrefined categories and "similar to advertised products" also serve off Amazon; the console adds "similar to advertised products" on its own, and the API does not. (T37)
- Audience campaigns exclude shoppers who bought the advertised or similar products in the past 30 days. (T37)
- View audiences reach back up to 90 days and purchase audiences up to 365, including viewers or buyers of a given brand. (T37)
- Audience ids come from the audience list. (T37)
- On the unified console, contextual targeting is part of multi-signal targeting. (T37)
- Randomised experiments outside Amazon found retargeting incremental for the advertisers studied, and showing the exact product a shopper viewed was not always the better ad. (T41)
