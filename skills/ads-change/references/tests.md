# Tests: Amazon's, practitioners' and vendors'

## Amazon's guidance

Amazon recommends limiting changes while testing bidding strategies, so that a difference in performance can be attributed to a specific change. (C9)
Amazon recommends reviewing bids "about once every two weeks", and judging a negative keyword "after it has received at least 20 clicks" and after "two weeks or more". (C9)
No Amazon page read states a statistical test or confidence level for an ad change. (C9)

## No randomized test for sponsored ads

No Amazon page or model read offers a randomized test for sponsored ads. (C10)
Manage Your Experiments covers listing content only: images, titles, bullets, descriptions and A+. (C10)
Brand Lift surveys exposed and unexposed groups, excludes SP, and its API paths sit under DSP; the launch page's `/measurementStudies/brandLift` paths are in no model. (C10)
Creative Testing is a pre-launch DSP panel survey, and SalesDuo's Borle (2026) agrees. (C10)
SB v4 lets several ads share an ad group, with no stated split. (C10)
DSP alone has ten 10% customer holdout groups, on a page that advises against before/after comparison of bid adjustments. (C10)
Multi-touch attribution divides credit and is beta in the US; AMC's exposed against non-exposed conversions are an observational split; MMM feeds a model the advertiser runs. (C10)
No Ads API model or release note read has an experiment, split or holdout operation, and no page read offers sellers a self-serve SP incrementality measurement. (C10)

## Amazon's own experiments

Amazon states it is "continually experimenting to refine and improve our ad auctions", including "introducing, removing, or modifying the data points or factors used in the auction process". (C22)
Amazon-authored product-search papers report online A/B tests on 50 million and 140 million queries, and a ranking change serving customers since 2025. (C22)
Amazon reports that 80% of bid changes on clicked SP search ads came within one day of a prior change (2019–2024). (C22)
Amazon reports that in one study competitors' average bids on keywords an advertiser stopped bidding on dropped about 83%, from $15.96 to $2.74. (C22)

## Practitioners

Practitioners disagree on how long to wait after a bid change: Ad Badger's automated bidder typically a 24-hour window, Ad Badger's blog at least seven days, Pare's George Reid 7–14 days, and BidX's Selina Krüger the seventh day after the observation period when the gap to target ACoS is small. (C20)
Ad Badger's August 2026 attribution article states a 14-day SP window and order-date reporting, which Amazon's v1 overview contradicts. (C20)
Eva Commerce's Hai Mag proposes a geo holdout for branded SP, though the v1 model gives SP no location target. (C20)
Hai Mag says 80–90% of branded-ad traffic and sales return organically when the ad is removed, without a source. (C20)
Perpetua measures category-term incrementality with Total ACoS. (C20)
Seller Labs says conversion "swings on single orders" below a few hundred sessions a month and uses 60- or 90-day windows or skips such ASINs, where Amazon's targeting guide gives 20 clicks for judging a negative. (C20)

## Vendors, in their own words

Skai calls holdout testing the "gold standard" and computes iROAS as incrementality score × ROAS. (C21)
Pacvue describes its iROAS as using "multiple advanced linear regression data models". (C21)
Intentwise calls its What Changed comparison "the starting point". (C21)
Teikametrics states it updates Amazon bids "Hourly". (C21)
Helium 10's change log labels a change's source, including "In Seller Central or 3rd party". (C21)
