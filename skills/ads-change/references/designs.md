# Measurement designs

## Ratios

Amazon's derived metrics are computed by aggregating numerator and denominator across rows at the chosen grain and then dividing. (C7)

## Shared budgets and auctions

When test and control arms share budgets or auctions, a measured bid effect can be "severely biased" unless each arm keeps a separate budget. (C15)
In an Airbnb pricing meta-experiment, at least 20% of the individual-randomized estimate was interference bias, which cluster randomization removed. (C15)
In simulation, blocked cluster randomization cut the naive bias by as much as 62%, at the cost of higher variance. (C15)
Wager and Xu estimate marginal responses with ±1 randomized shocks per unit while staying at a fixed market equilibrium. (C15)

## Switchbacks

Amazon's pricing scientists, unable to split shoppers for a price test, run switchbacks over time, report that random-days switchbacks cut standard error by 60%, and name carryover through recommendations. (C23)
Amazon-authored work on advertiser experiments states that auction competition between treated and control advertisers biases simple advertiser randomisation. (C23)
Bojinov, Simchi-Levi and Zhao set optimal switchback assignment under carryover of order *m*, with the Horvitz-Thompson estimator unbiased for lag *p* ≥ *m*, and suggest periods shorter than the carryover. (C23)
Hershaff, a seller, reports (Substack, 2026-02-13) that a month-long daily ad on/off switchback gave an incremental ROAS of 1.25 on total sales against platform ROAS near 2.35, rising to 1.54 with an MMM-estimated adstock. (C23)
Hershaff calls 1.25 a floor, because a daily switchback assumes no carryover. (C23)

## Staggered changes

With treatment at different times, the two-way fixed-effects estimator equals a weighted average of all two-group/two-period comparisons with weights that may be negative, so its coefficient can be negative while every effect is positive. (C24)
In event studies, apparent pretrends can arise solely from effect heterogeneity. (C24)
A staggered difference-in-differences is unbiased for a weighted average effect under random assignment of the adoption date. (C24)
With a treatment of varying dose, parallel trends does not rule out selection bias across doses. (C24)

## Synthetic control

Abadie's conditions for a synthetic control are an effect large against the outcome's volatility, donors that did not adopt similar changes, no anticipation, no interference and a close pre-period fit, with inference by placebo reassignment. (C25)

## Variance and checks

CUPED cuts the variance of a treatment-control difference to var(Y)(1−ρ²) with a pre-period covariate, about 50% on Bing. (C26)
The same metric over 1–2 pre-period weeks "works well", and "Never use covariates that could be affected by the treatment". (C26)
A sample ratio mismatch between arms, detected by a chi-square test, implies a selection bias that invalidates the results most of the time. (C26)
Carryover from earlier experiments on the same units lasted more than three weeks at Bing and was detected with A/A tests. (C26)

## Many tests

Across many tests, a step-up procedure controls the false discovery rate (the expected share of falsely rejected hypotheses) for independent tests. (C28)
Multilevel models instead shrink estimates toward each other. (C28)
Winners chosen from a group of experiments carry a selection bias, for which Lee and Shen give a correction. (C28)
An objective Bayesian prior needs historical A/B data; Bing's was built from thousands of experiments. (C28)
With fat-tailed effects, a lean strategy of more ideas on smaller samples is preferred. (C28)

## Intent-to-treat

Intent-to-treat compares whole groups and stays valid but less precise. (C29)
Public-service-ad control experiments are invalid when delivery algorithms optimise for performance. (C29)

## The listing playbook's verdicts

In `cx-listing-playbook`'s effect review, *held* means the targeted metric moved, after the control's movement is taken out, in the expected direction by at least the smallest move logged before the change, with orders not falling and no confounder or event explaining it. (C19)
*Not held* means the window held enough data to have seen that move and did not, or the metric moved the wrong way. (C19)
*Cannot tell* is every other case. (C19)
