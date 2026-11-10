# Attributed sales, total sales and organic

## Two sales figures

- Amazon dates an ad-attributed purchase to the ad interaction in the campaign's time zone, without tax or cart discounts and net of cancellations within 72 hours. (G20)
- Sales and Traffic counts ordered product sales as price × units for the period's date. (G20)
- For a seller's Sponsored Products, attributed sales include the advertised product and any other product the same merchant sells. (G20)
- Reporting v3 splits them by `SameSku`/`OtherSku` and `purchasedAsin`, and v1 by the Promoted and Halo qualifiers. (G20)
- v1's base conversion metrics include halo; the promoted-only figure carries the `Promoted` qualifier. (G20)
- Sponsored Products and Sponsored Brands CPC campaigns report 0 for conversions from views. (G20)
- `getOrderMetrics` takes an IANA time zone for the day boundary, so seller-side daily ordered sales can be cut on the ads profile's time zone. (G23)
- No Amazon page read states the time zone of a Sales and Traffic report day. (G23)
- Data Kiosk Economics returns, per MSKU and day, ad charges by ad type beside ordered and net product sales; those charges are spend, not attributed sales. (G23)
- ../ads-review/references/metrics.md: the ads metrics, their definitions and attribution.

## New-to-brand

- A new-to-brand purchase is one by a shopper with no purchase from the brand in the previous 12 months, judged on all shopping within the brand on Amazon, not only attributed purchases. (G10)
- Amazon's new-to-brand help page says the metrics are for Sponsored Brands and Display and the data "isn't available for Sponsored Products". (G10)
- Reporting v3 carries new-to-brand columns in no Sponsored Products report type. (G10)
- v1's *Purchases (new to brand)* page, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases-new-to-brand.md, names Sponsored Products in the eligibility of its new-to-brand purchase and sales fields, not new-to-brand ROAS, view-attributed fields included, although Amazon reports 0 view conversions for Sponsored Products. (G10)

## Long-term sales

- Long-term sales is attributed sales plus the estimated 365-day value of new-to-brand shopper engagements, modelled from the brand's historical shopping patterns. (G11)
- It is offered with long-term ROAS for Sponsored Brands, Display, TV, DSP and Full-Funnel, not Sponsored Products. (G11)
- Amazon calls it an ad-attributed measure that estimates incremental sales value, and no Amazon page read describes a holdout or unexposed comparison in its calculation. (G11)
- Since 2026-09-25 its US estimates use machine-learning models in place of heuristics, with 30-, 60-, 90- and 180-day horizons beside 365 days. (G11)
- Its cohort fields (`metric.cohortAccumulatedSales*`), which Amazon presents for checking estimates against actual cohort sales, require `campaign.id` and "aren't summable across cohorts". (G11)

## Subscribe & Save and repeat purchase

- Subscribe & Save subscriptions attributed to ads are reported for Sponsored Brands, display, TV, DSP and Full-Funnel, not Sponsored Products. (G12)
- The Repeat Purchase report and the Replenishment API report repeat and subscriber value. (G12)
- Subscribe & Save needs Brand Registry, starts at a 0% seller-funded discount and can block one-time purchases under `REPLENISHMENT_ONLY_ORDERING`. (G12)

## TACOS

- Amazon names TACOS on two Amazon Ads pages, once as ad spend as a percentage of total sales and once as total sales "(organic and paid)" set against ad spend. (G14)
- Neither page names the sales field, the ad products counted or the window, and no Ads API metric, report column or help page read defines it. (G14)
- The TACOS benchmark ranges read (Helium 10) cite no data source, a point PPC Land makes in general. (G14)

## A total-account series

- A total-account series (ad spend, attributed sales, ordered sales, their ratio) shows how the quantities moved together over the dates read. (G26)
- Price, deals, stock, Featured Offer share, reviews, seasonality and competitors' actions move ordered sales over the same dates, and the series alone does not separate their effect from the ads'. (G26)

## Organic rank and search counts

- No Amazon help page, API document, policy or staff reply states whether ad-attributed sales feed organic rank; Amazon's words stop at Sponsored Products helping offers "rise through search results". (G21)
- No Amazon API or report read returns a product's organic search position. (G28)
- Catalog Items returns Best Sellers Rank, the Ads API an advertiser's paid impression share and rank per search term, and Brand Analytics search-funnel counts and shares. (G28)
- The console's Search Term Impression Share report is listed as not available in the API. (G28)
- Every organic-rank series is a third-party sample (Helium 10, SmartScout, DataDive, Jungle Scout), none read validated against Amazon data. (G28)
- BSR is relative to the category, and its mapping to quantity is modelled as a power law (Chevalier & Goolsbee's slope 0.9 to 1.3 on 2001 book data). (G28)
- Keepa's `monthlySold` ("bought in past month") is a variation-specific floor bucket most ASINs lack, moving only at bucket boundaries. (G28)
- Search Query Performance gives, per query, an ASIN's and the brand's impressions, clicks, cart adds and purchases on the search results page beside the query's totals and shares, by Sunday–Saturday week, month or quarter. (G22)
- It is for brand-registered sellers with the Brand Analytics role, through SP-API with an `asin` list of at most 200 characters. (G22)
- Neither Search Query Performance nor Search Catalog Performance has a field separating paid from organic, and Search Catalog Performance's impressions "include sponsored search results". (G22)
- Trellis reads Search Query Performance's counts as organic and paid combined. (G22)
- ../ads-review/references/reports.md: the ads reports.
- The amazon-ads skill's references/door.md: how a report is asked for and landed.
