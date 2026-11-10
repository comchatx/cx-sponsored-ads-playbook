---
name: ads-search-terms
description: "What shoppers' search terms and negatives look like in a seller's sponsored ads: what the search term report and the bulksheet search term tab hold and leave out, how negative keywords and negative product and brand targets work at each level in Sponsored Products, Sponsored Brands and Sponsored Display, where Amazon's own texts disagree, Amazon's own harvest, and how practitioners and research judge a term with clicks and no orders. For reading search terms, harvesting them or adding negatives in a seller's ads."
---

## The report

- The Ads API search term report holds only clicked terms; Amazon's texts disagree on whether the console report holds impressions. (S1)
- The SP search term report has no advertised-ASIN column. (S3)
- `*` is a detail-page placement; ASIN-shaped terms are detail pages, on auto and product-targeting rows only; negative ASIN targets stop ads on such pages, negative keywords on search pages for matching queries. (S2, S5)
- The bulksheet search term tab always looks back 7 days. (S15)

## Negatives

- Negative ASIN and brand targets act only on product-attribute and automatic targets. (S5)
- Negatives sit at ad group or campaign level; an SP campaign negative keyword covers every ad group, an ad-group one only its own; SB has "no campaign-level negative targeting", SD's are ad-group level. (S6)
- Amazon states a negative keyword takes effect within 72 hours, a negative product 96. (S8)
- An existing negative keyword's match type cannot be changed. (S7)
- Console help and bulksheets offer negative exact and phrase only; SP 3.0 and v1 also accept broad. (S9)
- No Amazon model, help page or bulksheet tab read on 2026-11-09 carries a shared negative keyword list or portfolio-level negatives. (S23)

## Terms

- Amazon's targeting guide puts a minimum click count and a period before judging, and recommends phrase or exact for negatives. (S13)
- Practitioners' points for a term with clicks and no orders differ, tied to price, margin or conversion rate. (S17)
- With zero conversions in n clicks, the 95% upper bound on conversion rate is about 3/n, good for n over 30. (S20)
- Delayed-feedback models treat not-yet-converted recent clicks as uncertain, not negative. (S21)
- Target promotion groups are Amazon's harvest from auto into manual ad groups, its Target Promotion guide describing no negative in the source; several practitioners negate a term moved to exact at its source, Adbrew calling its move thresholds "practitioner defaults … not Amazon rules". (S14, S18)

## References

- references/search-term-report.md: rows, columns, bulksheets.
- references/negatives.md: levels, match types, paths, conflicts.
- references/terms.md: thresholds, harvest, small counts.
- ../ads-change/references/tests.md: Amazon's click and week figures.
- ../ads-structure-and-targets/references/structure.md: ad groups, per-ASIN structures.
- ../ads-review/references/reports.md: report types, advertised product.
- ../ads-review/references/metrics.md: metric definitions.
