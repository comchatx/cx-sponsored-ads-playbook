# Metrics: attribution, definitions, traffic quality and settling

## Attribution

- Sponsored ads report a conversion on the date of the ad interaction, the traffic date, which may differ from the conversion date (M1).
- Legacy Sponsored Brands and Display, Video and Audio campaigns reported on the conversion date before unified reporting and now report on the traffic date, which moves conversions earlier without changing their total (M1).
- Amazon attributes each conversion to at most one ad interaction across all campaigns and all advertisers, ranked promoted-product clicks, brand-halo clicks, promoted-product views, brand-halo views, then last touch with the last click before the last view (M2).
- Amazon states that Sponsored Products for sellers is merchant-based and does not normally compete for attribution with brands, except that where the same advertiser wins as both merchant and brand, the more relevant ad is chosen; the page does not say whether "the same advertiser" is the advertising account, the global account or the brand (M25).
- Lookback and credited products differ by ad product and advertiser: SP for sellers is 7 days on clicks, crediting the advertised product and anything else the merchant sells (M3).
- SP for vendors and authors is 14 days on clicks, crediting the advertised and same-brand products sold by Amazon; SB, display, Streaming TV and DSP are 14 days and credit the brand halo (M3).
- Unified reporting and v1 drop window suffixes, so an SP base metric is 7-day for sellers and 14-day for vendors, and other campaign types are 14-day (M3).
- Ad Badger's description of SP and SB as 14-day click attribution, with reports built by order date, contradicts Amazon's attribution page (M3).
- SP and CPC Sponsored Brands attribute to clicks only; vCPM Sponsored Brands, display, Streaming TV and DSP also credit views meeting the MRC standard (M4).
- From 2026-01-01 vCPM SB and display use a shopping-signal enhanced view model with a shorter window, keeping the old 14-day model as "all views" metrics, and Amazon publishes no incrementality figure for the new model (M4).
- KENP read is attributed to reading up to 14 days after an ad click and reported on the day the pages were read (M12).
- Amazon's multi-touch attribution, a US beta, splits credit across ad touches in proportion to their value and is published as Reporting v1's 56 `metric.multiTouch*` fields beside last-touch ones, each requiring its last-touch counterpart (M16).
- Amazon's launch page places it in "most report types for version 3", but the v3 column pages show no multi-touch column and every v1 multi-touch field gives its v3 name as "N/A" (M16).
- Lily Tong, a director of measurement at Amazon Ads, quoted by Digiday, said roughly 20% of a brand's sales value shows up after the attribution window, from an Amazon analysis of more than 2 million campaigns in June across all ad products, not split out for Sponsored Products (M19).
- Digiday reports agencies split on long-term sales, some treating it as "a forecast that shifts whenever the campaign mix changes" (M19).

## Definitions

- CTR is clicks ÷ impressions, CPC cost ÷ clicks, CPM cost ÷ impressions × 1,000, and vCPM cost ÷ viewable impressions × 1,000 (M6).
- Unified reporting and v1 have no ACOS field, while v3 has `acosClicks7d` and `acosClicks14d` on targeting, search-term, advertised-product and ad-extension types but not `spCampaigns` (M6).
- In unified reporting and v1 "purchase rate" (`metric.purchaseRate`) is purchases ÷ impressions, and the per-click rate is "purchase rate over clicks" (`metric.purchaseRateOverClicks`, v3 "14 Day Conversion Rate") (M7).
- Amazon's Sponsored Products search-term help page, modified 2026-05-18, still calls the per-click rate "Purchase rate" (M7).
- Reporting v3 carries SP 1-, 7-, 14- and 30-day click-attributed purchases, sales and units with same-SKU and other-SKU variants; v1 has no day-count variant (M8).
- Sponsored Brands `purchases` and `sales` count 14 days after a click or a view, and `sales14d` includes view-attributed sales for vCPM campaigns (M8).
- A purchase is an order event that can hold several units (M9).
- Attributed sales exclude tax and cart discounts, can include items sold by Amazon or other sellers and used items, and lose payment failures and cancellations within 72 hours, deducted over up to 7 days (M9).
- Amazon reports no impressions, clicks or other traffic at the converted-product level, because one interaction can lead to several products (M10).
- Detail page views, add to cart, viewable impressions and vCPM are not offered for SP in v1; detail page views are not unique per customer and include halo in unified reporting (M11).
- Unified reporting renames metrics and widens some definitions (M17).
- The console's legacy report centres shut on 2026-12-31, with saved reports, schedules and history deleted, and new legacy reports and edits stop on 2026-12-17; Amazon says these dates are subject to change (M17).

## Traffic quality

- Impressions and clicks are net of invalid traffic, with gross and invalid counts reported separately (M5).
- Amazon filters before the bid and after the impression, monitors for up to 30 days, bills net of what it finds, and can change console cost for 72 hours (M5).
- Amazon names a fall in invalid-traffic rate with a rise in CTR or clicks and a fall in CVR as a signal of undetected invalid traffic, while an IVR level alone is not one (M5).
- The MRC accreditation renewed on 2026-07-08 covers Sponsored Products gross clicks and clicks net of SIVT on Amazon placements, in total only (M15).
- Impressions and conversions are not accredited, and Sponsored Brands and Sponsored Display are not on the MRC list (M15).

## Days, zones and currencies

- v1 aggregates days in each campaign's time zone (`timeZone.value`) and money in the campaign budget currency, needing `budgetCurrency.value` with money metrics and `convertedCurrency.value` for converted figures (M13).
- v2 and v3 reports use the profile's time zone, change history timestamps are UTC, and console downloads use the account's registered zone (M13).

## Settling

- Amazon's settling schedule: data within about 12 hours, impressions and clicks changing for up to three days, and conversions first within 24 hours and restated at 1, 7 and 28 days, up to 42 days for a 14-day window (M14).
- Another Amazon page says "subject to change for up to 60 days", and Stream v2 has a 70-day window (M14).
- Amazon advises waiting at least five days for accurate clicks, and the console's sales take up to 48 hours (M14).
- No report marks a day final, and Amazon's P99 target from impression to availability is 12 hours (M14).
- Optmyzr pulled 14,991 campaigns' 14-day figures daily over 17 days and found attributed sales in the top 5% growing at least 18.75% after the first read (M20).

## Measurement standards and research

- The IAB/MRC Retail Media Measurement Guidelines (January 2024) require attribution windows that are empirically supported and disclosed before the campaign, encourage day-level lag data, require viewable impressions for attributing outcomes to exposure, a click being able to stand in, require a disclosed basis for 12-month forecasts, and highly recommend RCTs for incrementality (M22).
- Amazon's attribution page says viewability is inferred from historical data and placement characteristics where it is not measured directly (M22).
- The IAB and IAB Europe guidelines of November 2025 grade new-to-brand percentage, platform-reported incrementality and simple multi-touch attribution as "Weak" causal evidence and experiments as "Strong" (M22).
- A surrogate index of short-term outcomes recovers a long-term effect only under the surrogacy assumption that the long-term outcome is independent of treatment given the surrogates (M21).
- Attribution research finds last-click credit differs substantially from model-based credit, attribution weights follow exposure counts where profitable allocation does not, and game-theoretic credit is variable importance unless causal assumptions hold (M23).
- The same research finds single-campaign effects measured by holdout imprecise and 78% of a display campaign's purchase lift coming from people who never clicked, and describes ghost ads, which compare the exposed with their randomized would-have-been-exposed counterparts (M23).
- Persistence modelling separates temporary from permanent effects, and Qin found every Amazon brand KPI she studied stationary, so no marketing effect lasted forever (M24).
