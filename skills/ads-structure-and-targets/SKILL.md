---
name: ads-structure-and-targets
description: "How a seller's sponsored ads are built and what they target: Sponsored Products, Sponsored Brands and Sponsored Display campaigns, ad groups, portfolios, fields fixed at creation, archiving, limits, global campaigns, match types, auto groups, product, category, theme and audience targets, and brand and competitor targeting with what research and practitioners report on it. For reading, auditing or changing a seller's campaign structure and targets on Amazon."
---

## Structure

- Sponsored Products nests campaign, ad group, then product ads and targets; an ad group's products share its bids and targeting, and no ad group holds both keyword and product targets. (T1)
- Budget and bidding strategy live on the SP campaign; an ad group has no budget. (T3)
- Fixed at creation: SP auto or manual (`targetingType`), a keyword's match type, a Sponsored Brands campaign's goal and other fields listed per product; changing one means archiving and recreating. (T4)
- `ARCHIVED` is terminal, reached through a delete. (T6)
- A campaign belongs to at most one portfolio. (T7)
- A write past a quota is refused with `QUOTA_EXCEEDED` or `NON_ARCHIVED_QUOTA_EXCEEDED`. (T8)
- Sellers identify an SP product ad by SKU, vendors by ASIN. (T49)

## Sponsored Brands and Display

- A Sponsored Brands ad group holds one ad type and targets keywords or products; v4 ad groups carry no bid. (T2, T20)
- Product Collection ads are being retired: since August 2026 a create makes a Manual Collection ad. (T19)
- Sponsored Display refined contextual and single-product targets serve on Amazon only. (T37)

## Matching

- SP auto targets through close match, loose match, substitutes and complements. (T5)
- No match type is a literal string match. (T23)
- Of one keyword's several match types, the highest-bid one is used. (T22)
- An SP product target holds one ASIN, exact or expanded. (T27)

## Brand and competitors

- Any advertiser may target any brand's name or any ASIN, which Amazon calls Protect and Conquest. (T35)
- None of Amazon's share metrics names a competitor, and no Amazon field flags a search term as branded. (T32, T42)
- Field experiments on search engines, not Amazon, found a brand's own ad on its query added little when no competitor advertised and more when competitors did. (T43)

## References

- references/structure.md: hierarchy, fixed fields, archiving, portfolios, limits, global campaigns, vendors.
- references/sponsored-brands-and-display.md: SB goals, formats, v4, retirement; SD targets.
- references/targets.md: match types, auto, product and category targets, themes, recommendations.
- references/brand-and-competitors.md: brand and conquest targeting, share, experiments, law.
- The amazon-ads skill's SKILL.md and references/door.md: the door, paths, reports.
- ../ads-search-terms/SKILL.md: search terms. ../ads-bids-and-budgets/SKILL.md: bids, budgets. ../ads-review/references/metrics.md: metrics.
