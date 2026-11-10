# Decomposition: the metric chain, benchmarks and change methods

## The chain

- Amazon defines click-through rate as clicks over impressions and cost per click as cost over clicks, so on a cost-per-click row spend equals impressions × CTR × CPC (A7).
- Optmyzr describes the metrics as a chain from impressions through CTR, clicks, conversion rate and orders to sales and ACoS, and names three root causes of an ACoS rise: traffic, conversion rate, and demand or market shift (A7).
- Optmyzr calls a conversion-rate drop "the most misdiagnosed cause of ACoS spikes" (A7).
- Chuck Kessler (Canopy) orders a conversion drop's causes from the Featured Offer first, and Bob Norberg (eComEngine) puts availability first and ads last (A7).
- What each metric counts: references/metrics.md.

## Benchmarks

- Amazon's benchmark metrics give the 25th, 50th and 75th percentiles of unnamed peer brands in a category (A20).
- Third-party quarterly benchmarks, Tinuiti's as summarized by Karooya, report spend and CPC moves across their clients (A20).

## Splitting a change

- The log-mean Divisia index splits the change in a product of factors exactly into one term per factor (A21).
- An aggregated rate can show a pattern none of its units shows, which is Simpson's paradox (A21).
- Root-cause methods exist for advertising revenue and derived measures, Adtributor among them (A22).
- Given an analyst-supplied causal graph, the methods of Budhathoki et al., Amazon researchers, attribute a distribution change or an outlier to its mechanisms, and DoWhy's `gcm` module implements them (A22).

## Telling a shift from noise

- For Poisson counts the k-sigma limits are c ± k√c, and when an indicator varies more than chance alone, ignoring the over-dispersion classifies too many units as abnormal (A23).
- CUSUM charts detect sustained mean shifts of 2 sigma or less more efficiently than Shewhart charts, and EWMA charts weight past data so a small or gradual drift can be detected (A23).
- PELT finds changepoints in time linear in the series length (A23).
