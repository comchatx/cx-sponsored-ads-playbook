---
name: ads-structure-and-targets
description: "How a seller's sponsored ads are built and what they target: Sponsored Products, Sponsored Brands and Sponsored Display campaigns, ad groups, portfolios, fields fixed at creation, archiving, limits, global campaigns, match types, auto groups, product, category, theme and audience targets, and brand and competitor targeting with what research and practitioners report on it. For reading, auditing or changing a seller's campaign structure and targets on Amazon."
---

## Structure

- Sponsored Products nests campaign, ad group, then product ads and targets; an ad group's products share its bids, and no ad group holds both keyword and product targets. (T1)
- Budget and bidding strategy live on the SP campaign; an ad group has no budget. (T3)
- Fixed at creation: SP auto or manual (`targetingType`), a keyword's match type, a Sponsored Brands campaign's goal and other fields listed per product; changing one means archiving and recreating, though a keyword in another match type can be added beside the old one; while both run, the higher-bid one is used on a query both match, and Amazon's pages do not say whether across ad groups or campaigns. (T4, T22)
- `ARCHIVED` is terminal, reached through a delete. (T6)

## Sponsored Brands

- A Sponsored Brands ad group holds one ad type and targets keywords or products; v4 ad groups carry no bid. (T2, T20)

## Matching

- SP auto targets through close match, loose match, substitutes and complements. (T5)
- No match type is a literal string match. (T23)
- An SP product target holds one ASIN, exact or expanded. (T27)
- Which keyword or target matched a search term, its match type, ad group and campaign: ../ads-search-terms/references/search-term-report.md.

## Brand and competitors

- Any advertiser may target any brand's name or ASIN (Amazon's Protect and Conquest). (T35)
- None of Amazon's share metrics names a competitor; Brand Analytics Top Search Terms names a term's three most-clicked products and needs Brand Registry. (T32)
- No Amazon field flags a search term as branded. (T42)
- Field experiments on search engines, not Amazon, found a brand's own ad on its query added little when no competitor advertised and more when competitors did. (T43)

## References

- references/structure.md: hierarchy, fixed fields, archiving, portfolios, limits, quota errors, global campaigns, vendors.
- references/sponsored-brands-and-display.md: SB goals, formats, v4, retirement; SD targets.
- references/targets.md: match types, auto, product and category targets, themes, recommendations.
- references/brand-and-competitors.md: brand and conquest targeting, share, Top Search Terms, experiments, law.
- The amazon-ads skill's references/door.md: Ads API paths and reports. The amazon-sp-api skill's references/door.md: SP-API reports, Brand Analytics among them.
- ../ads-search-terms/SKILL.md: search terms. ../ads-bids-and-budgets/SKILL.md: bids, budgets. ../ads-review/references/metrics.md: metrics.
