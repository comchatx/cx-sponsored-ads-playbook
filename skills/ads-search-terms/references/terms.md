# Judging and harvesting terms

## Amazon's guide

- Amazon's targeting guide puts a minimum click count before judging a keyword for a negative and a period before judging a negative, and recommends phrase or exact for negatives. (S13)
- ../ads-change/references/tests.md: the same guide's click count and period, quoted in figures.

## Practitioners' thresholds

- Practitioners judge a term with clicks and no orders at different points and tie the count to price, margin or conversion rate. (S17)
- Ad Badger (Michael Erickson Facchin) negates at 2,500 impressions with CTR under 0.18% and no conversions, more than $35 spend with no conversions, or more than 34 clicks without one, calls these "starting points" and exempts competitor brand terms. (S17)
- Jungle Scout (Galeana) judges at 10 clicks; Seller Labs at 20–30; Canopy at 20–30 for $30–100 products and 40–50 above $100. (S17)
- Scale Insights' default "Unique Word with 0 Sales" filter is at 25 clicks per word, not per term. (S17)
- Scale Insights' word rule aggregates single words across search terms per product and adds non-performing words as ad-group negative phrase, skipping singular and plural forms of words in the product title. (S17)
- Ad Badger's PPC Den page says branded terms may convert every couple of clicks where competitor terms may need fifty, and that one rule across the board kills keywords "that were slow, not bad". (S17)

## Harvesting

- Sponsored Products target promotion groups are Amazon's own harvest: they link an auto ad group to manual destination ad groups and move converting search terms and ASINs into them. (S14)
- They move them on recommendations "based on performance heuristics" that the specification does not state. (S14)
- The Target Promotion guide does not describe adding negatives in the source. (S14)
- Several practitioners add a term moved to exact as a negative where it came from. (S18)
- Seller Labs adds it as negative exact in the auto campaign, and Canopy in auto and broad. (S18)
- Ad Badger adds it in broad and auto for a term kept in exact at a lower bid. (S18)
- Helium 10's Prestozon rule adds it as negative exact in the broad ad group and negative phrase in the auto campaign. (S18)
- Adbrew negates a term that reaches exact in every auto, broad and phrase campaign of its product group. (S18)
- Adbrew (Ayush Chaudhary) moves a term to phrase at one order in 30 days within 1.5× target ACoS and to exact at two orders at or under target, excludes the last 7 days, and calls these "practitioner defaults … not Amazon rules". (S18)

## Small counts

- With zero conversions in n clicks, the 95% upper bound on the conversion rate is about 3/n, the rule of three, a good approximation when n is greater than 30 (Hanley and Lippman-Hand). (S20)
- At single-keyword sample sizes the normal-approximation interval for a conversion rate has poor coverage, and the Wilson and Jeffreys intervals perform better (Brown, Cai and DasGupta). (S20)
- Ratio metrics such as CPC and ACOS need delta-method variance (Deng, Knoblich and Lu). (S20)
- Conversions can arrive long after the ad interaction, and delayed-feedback models treat not-yet-converted recent clicks as uncertain rather than negative (Chapelle). (S21)
- In paid search, keyword conversion data are sparse and position is endogenous (Rutz, Bucklin and Sonnier). (S21)
- In that research, a keyword list built on estimated conversion rates outperformed lists built on observed conversion and click-through rates. (S21)

## Relevance labels

- Amazon's ESCI dataset labels query-product pairs Exact, Substitute, Complement or Irrelevant (Reddy et al.). (S22)
