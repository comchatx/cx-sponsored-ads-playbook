# Brand and competitor targeting

Metric definitions are in ../ads-review/references/metrics.md.

## What Amazon allows

- Any advertiser may target any brand's name as a keyword and any ASIN as a product target, which Amazon calls Protect and Conquest. (T35)
- Amazon suggests bidding on one's own branded keywords and own product pages. (T35)
- Ad creative may not name or disparage a competitor, and may say "a leading brand". (T35)

## Reserve share of voice

- Reserve share of voice sells Sponsored Brands top-of-search placement on the advertiser's own exact branded keywords at a fixed upfront price, through v1 operations. (T36)
- Its keywords, flight and budget are fixed once it starts. (T36)
- Amazon's own pages state different flight lengths, minimums and marketplaces. (T36)
- Amazon reports its beta raised top-of-search share from 62.7% to 99.3%, a before/after comparison. (T36)

## Share and branded-search data

- Search term impression share is the account's share of one ad product's impressions on a term, account-wide, not splittable by campaign, and in windows that differ by surface. (T31)
- Top-of-search impression share divides a campaign's top-of-search impressions by those it was eligible for. (T31)
- v3's columns page lists top-of-search impression share for `spCampaigns`, `sbCampaigns` and `sbTargeting` and the report type pages add `spTargeting`, while v1 offers it with campaign-level dimensions only. (T31)
- Sponsored Brands v2's search-term share fields stop on 2026-11-10. (T31)
- No API was found for the console's brand impression share dashboard. (T31)
- None of Amazon's share metrics names a competitor. (T32)
- Brand Analytics Top Search Terms names the three most-clicked products per term and needs Brand Registry. (T32)
- Branded-search metrics (searches for the brand after an ad interaction) exist for Sponsored Brands, display, TV and DSP but not Sponsored Products. (T42)
- No Amazon field flags a search term as branded; keyword recommendations carry a `keywordTheme` label. (T42)

## Field experiments on brand queries

- The experiments below ran on search engines, not Amazon's store. (T43)
- On a brand's own query, the brand's own ad added little when no competitor advertised: on Bing about 1–4% of clicks, and on eBay no measurable short-term benefit, with organic clicks capturing 99.5% of the forgone paid clicks. (T43)
- It added more when competitors advertised: brands not advertising lost 18–42% of clicks. (T43)
- Competitors' ads took 1–2% of a brand query's traffic on Bing. (T43)
- At Edmunds.com, shutting off paid links lost more than half the paid traffic. (T43)
- A firm pausing Google search ads in random US markets lost customers, but only 63% as many as a non-experimental estimate implied. (T43)

## Models and law

- Game-theory models find mutual bidding on each other's brand names can be a prisoner's dilemma that profits the platform, and competing bids can cycle (Edgeworth cycles). (T44)
- When Google opened trademarks to rivals' keyword bidding in continental Europe in 2010, navigational searches became less likely to reach the trademark owner, more so for lesser-known marks. (T45)
- The Ninth Circuit held in 2015 that Amazon showing other brands' watches for a search of "mtm special ops" was not likely to confuse shoppers, because Amazon labels each result with its name, manufacturer and photo. (T45)
- The Second Circuit in 2021 vacated the FTC's order against 1-800 Contacts' settlement agreements requiring rivals to refrain from search advertising on its trademarks and to use them as negative keywords. (T45)

## Practitioners and Amazon figures

- Perpetua's rule of thumb is that branded spend above 40% of ad spend likely buys traffic the brand would get anyway. (T46)
- Haus reports, from Google branded-search tests, significant lift for 82% of brands facing high competition on their brand terms against 35% facing low competition. (T46)
- Amazon's 2023 goal-based campaigns page states that, from Amazon data of 6,000 advertisers (June 2023), on average 60% of shoppers who searched for a brand bought from a competitor brand within 30 days. (T48)
- Practitioner figures on Sponsored Brands video against competitors (Skale Strategy, ATTN Agency, BTR Media) are published without a stated method. (T48)
- No Amazon page read states whether Store pages carry other brands' ads, which Perpetua's 2021 guide says they cannot. (T48)

## Competitor stock-outs

- Perpetua's Competitor Signals raises bids when a competitor goes out of stock and normalises them on restock. (T47)
- Jarvio and Netpeak advise product-targeting a rival's page during its stock-outs. (T47)
- Eva calls a rival's stock-out a window of "typically 2 to 6 weeks" and warns that conquest-driven sales can stock out the conquering ASIN. (T47)
- None of these four publishes a measured effect. (T47)
- Stock-out studies outside advertising find that a model accounting for availability predicts significantly larger stock-out effects on profitability than one ignoring it. (T47)
