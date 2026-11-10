# The search term report

## What has a row

- The Ads API search term report, in reporting v3 and in v1, holds only terms with at least one ad click, so a term with impressions and no click has no row. (S1)
- Amazon's console help says the same of the console report, while its v3 FAQ says the console report also holds impressions; the two texts have not been reconciled. (S1)

## What a term looks like

- A search term of `*` is a detail-page placement with no keyword. (S2)
- ASIN-shaped terms are the detail pages the ad appeared on, and they show only on auto and product-targeting rows. (S2)
- A negative ASIN target stops ads on such a detail page, while a negative keyword stops ads on search pages for matching queries. (S2, S5)

## Columns

- The Sponsored Products search term report carries the keyword or targeting expression, the match type, and the ids of keyword, ad group and campaign. (S3)
- It has no advertised-ASIN column. (S3)
- ../ads-structure-and-targets/references/structure.md: what products in one ad group share, and practitioners' per-ASIN structures.
- ../ads-review/references/reports.md: report types and columns across ad products.

## Sponsored Display's matched target

- The matched target dimension (v3 `matchedTargetAsin`) holds the detail pages an ad appeared on that drew at least one click, and it exists for Sponsored Display only. (S4)
- One developer reports that since mid-July 2026 it carries no customer search terms, also for past dates re-requested, and Amazon has not answered the report. (S4)

## The bulksheet search term tab

- The bulksheet search term tab always uses a 7-day lookback, whatever the file's range. (S15)
- It carries the source campaign, ad group, keyword and target ids. (S15)
- Its page defines CTR and conversion rate inverted. (S15)
- ../ads-review/references/metrics.md: how each metric is defined.
