---
name: ads-search-terms
description: "What shoppers' search terms and negatives look like in a seller's sponsored ads: what the search term report and the bulksheet search term tab hold and leave out, how negative keywords and negative product and brand targets work at each level in Sponsored Products, Sponsored Brands and Sponsored Display, where Amazon's own texts disagree, Amazon's own harvest, and how practitioners and research judge a term with clicks and no orders. For reading search terms, harvesting them or adding negatives in a seller's ads."
---

## The report

- The Ads API search term report, asked for through the amazon-ads skill, holds only clicked terms; Amazon's console help and v3 FAQ disagree on whether the console report holds impressions. (S1)
- `*` is a detail-page placement; ASIN-shaped terms are detail pages, on auto and product-targeting rows only. (S2)
- The SP search term report has no advertised-ASIN column. (S3)
- The matched target dimension exists for SD only. (S4)
- The bulksheet search term tab always looks back 7 days. (S15)

## Negatives

- Negative keywords stop ads on search pages for matching queries; negative ASIN and brand targets stop ads on those detail pages, acting only on product-attribute and automatic targets. (S5)
- Negatives sit at ad group or campaign level; SB has "no campaign-level negative targeting", SD's are ad-group level. (S6)
- Amazon states a negative keyword takes effect within 72 hours, a negative product 96. (S8)
- An existing negative keyword's match type cannot be changed. (S7)
- Console help and bulksheets offer negative exact and phrase only; the SP 3.0 and v1 models also accept broad. (S9)
- Amazon's texts conflict on campaign-level negative product targets in a seller's manual SP campaign. (S11)
- No Amazon model, help page or bulksheet tab read on 2026-11-09 carries a shared negative keyword list or portfolio-level negatives. (S23)
- Amazon's brand-negative recommender includes the advertiser's own brands, its reason naming no metric. (S12)

## Terms

- Amazon's targeting guide puts a minimum click count and a period before judging. (S13)
- Practitioners' points for a term with clicks and no orders differ, tied to price, margin or conversion rate. (S17)
- With zero conversions in n clicks, the 95% upper bound on conversion rate is about 3/n, good for n over 30. (S20)
- Delayed-feedback models treat not-yet-converted recent clicks as uncertain, not negative. (S21)
- Target promotion groups are Amazon's harvest from auto into manual ad groups, on heuristics its specification omits. (S14)
- Several practitioners negate a term moved to exact at its source. (S18)

## References

- references/search-term-report.md: rows, columns, bulksheets.
- references/negatives.md: levels, match types, paths, conflicts.
- references/terms.md: thresholds, harvest, small counts.
- ../ads-review/references/metrics.md: metric definitions.
- ../ads-review/references/reports.md: report types.
