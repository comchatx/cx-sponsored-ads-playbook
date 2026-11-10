"""A synthetic seller's tree for the skill-creator runs of cx-sponsored-ads-playbook: no real seller, no Amazon call, no network.

    python3 -I evals/fixture.py <dir>            replaces <dir>/tenant and <dir>/stub-replies, leaves the rest of <dir>
    python3 -I evals/fixture.py <dir> --summary  the same, then prints the figures the cases are graded on, as JSON

Seller A1FIXTURESELLER, brand "Hearthly" (throws and blankets). Today is 2026-11-09, a Monday. Marketplace US (ATVPDKIKX0DER),
origin https://advertising-api.amazon.com, currency USD, profile 1111111111111111 in America/Los_Angeles (PST since 2026-11-01).
A second profile, CA 2222222222222222, has no campaigns. The seller's ASINs are B0FIXTURE1..9; competitors B0COMPET01..05.

<dir>/tenant is what the box holds after earlier sessions: landed Ads API replies and Reporting v3 rows under raw/amazon-ads/,
a few SP-API replies under raw/amazon-sp-api/, one Brand Analytics document under reports/, and the seller's notes under notes/.
<dir>/stub-replies is what Amazon answers "now", for evals/cx, out of the run's sight: the 2026-11-09 lists, budget usage,
recommendations, history, eligibility, today's offers, inventory and fees, and report-sources/, the rows a new report is cut from.

Every figure is invented. The shapes follow Amazon's documented replies as the amazon-ads door's references/door.md and the
research positions give them; where a field's format was not documented in what the positions read, the field is left out.

Catalog (notes/catalog.md):
  B0FIXTURE1 HL-FLEECE-GRY  Fleece Throw Grey 50x60        29.99   Featured Offer lost to A2OTHERSELLER9 on 2026-11-04
  B0FIXTURE2 HL-PLUSH-GRY   Plush Throw Grey 50x60         34.99 -> 39.99 on 2026-10-29; out of FBA stock since 2026-11-06
  B0FIXTURE3 HL-KNIT-CRM    Chunky Knit Throw Cream        44.99
  B0FIXTURE4 HL-SHERPA-Q    Sherpa Blanket Queen (child)   59.99   Lightning Deal 2026-11-03 at 44.99
  B0FIXTURE5 HL-WEIGHTED-15 Weighted Blanket 15 lb         79.99
  B0FIXTURE6 HL-FLEECE-CRM  Fleece Throw Cream 50x60       29.99
  B0FIXTURE7 HL-WAFFLE-OAT  Waffle Knit Throw Oatmeal      39.99   first available 2026-10-28, 0 reviews
  B0FIXTURE8 (parent)       Sherpa Blanket variation parent         not sellable, not advertisable
  B0FIXTURE9 HL-SHERPA-K    Sherpa Blanket King (child)    69.99   first available 2026-10-30, 0 reviews, never advertised

Campaigns (profile 1111111111111111):
  SP 311000000000001 "SP | Fleece Grey | Auto"     AUTO   down only  $30   B0FIXTURE1
  SP 311000000000002 "SP | Plush Grey | Manual"    MANUAL down only  $25   B0FIXTURE2; "grey throw blanket" BROAD, "plush throw blanket" PHRASE
  SP 311000000000003 "SP | Sherpa | Exact"         MANUAL down only  $50 (was $80 until 2026-10-27 03:12Z)  B0FIXTURE4
  SP 311000000000004 "SP | Weighted | Exact"       MANUAL up and down, top of search +200% (was +100% until 2026-10-22)  $60  B0FIXTURE5
  SP 311000000000005 "SP | Throws | Auto"          AUTO   down only  $35   B0FIXTURE6
  SP 311000000000006 "SP | Bedding | Auto"         AUTO   down only  $30   B0FIXTURE4 and B0FIXTURE5 in one ad group
  SP 311000000000007 "SP | Throws | Broad"         MANUAL down only  $40   ad groups Knit (B0FIXTURE3) and Fleece Cream (B0FIXTURE6)
  SP 311000000000008 "SP | Waffle | Auto"          AUTO   down only (created through the API with no strategy, 2026-10-28)  $15  B0FIXTURE7
  SB 451000000000001 "SB | Hearthly Throws | Collection"  CPC, page visits, $40  B0FIXTURE1, B0FIXTURE2, B0FIXTURE6
  SB 451000000000002 "SB | Brand | hearthly"       CPC, $15, keyword "hearthly" EXACT
  SD 461000000000001 "SD | Retarget views | Throws" vCPM, $20

SCENARIOS — three per skill. Each names its right answer and the position letters it rests on; --summary prints the figures.

ads-review
  R1 featured-offer-lost. "Sales from my fleece throw ads collapsed this week; raise the bids?" From 2026-11-04 SP Fleece Grey's
     impressions fall to a third and from 11-05 there are no rows at all; the 2026-11-02 getItemOffers shows the seller winning, the
     2026-11-09 one (stub) shows A2OTHERSELLER9 holding the Featured Offer at 26.99 against 29.99; the 2026-11-09 productAds list
     (stub, extended data) reads AD_NOT_IN_BUYBOX under a campaign that reads CAMPAIGN_STATUS_ENABLED. Right: the SP ad gets zero
     impressions without the Featured Offer whatever the bid (A8); the SB collection keeps serving and can send shoppers to the other
     seller's offer (A9); raising bids does nothing; the route is the offer (price) and Seller Support, not Advertising Support (A9).
  R2 settling-days. "My cream fleece auto campaign sold far less on Nov 5-8 for the same spend. What broke?" Nothing: the 2026-11-09
     read holds those days one to four days old, inside the seller SP 7-day click window, and conversions are restated (M3, M14);
     the 2026-11-02 read of 10-26..11-01 showed 10-29..11-01 short too, which the 2026-11-09 read has filled in (two vintages of
     the same days). Like-matured (each first read one to four days old), clicks match (145 against 143), the cream fleece's own
     sales are higher (209.93 on 7 orders against 179.94 on 6) and the gap is other-SKU sales; 7 orders against 11 is inside
     11 +/- 2 sqrt(11) for Poisson counts (A23). Read again after 11-15; no pause.
  R3 acos-conversion-then-stock. "ACOS on the plush grey campaign doubled; are CPCs up?" CPC and CTR are flat; ACOS rose because
     conversion halved after the seller's own price rise on 2026-10-29 (notes/ads-changes.md), spend = impressions x CTR x CPC (A7);
     then from 2026-11-06 the product is out of FBA stock (getInventorySummaries) and the SP ad is paused (AD_OUT_OF_STOCK, A8).

ads-bids-and-budgets
  B1 out-of-budget. "Why does SP | Sherpa | Exact stop every afternoon, and how could it spend $71 on Nov 3 with a $50 budget?" It is
     out of budget (servingStatus CAMPAIGN_OUT_OF_BUDGET, budgetUsagePercent 100 at 21:47Z today, IN_BUDGET true->false each day
     since 10-27 between about 11:20 and 14:05 Pacific, 17:55 on 11-03, back at local midnight; in budget 56% of 11-02..11-08, the
     share the budget recommendation reads); sponsored-ads budgets are not paced and wait for midnight (B23); the $71.31 report
     day is the averaged daily budget (one day up to 100% more, featureFlags not opted out, month within $50 x 30) (B22); the budget
     recommendation's missed sales are click-attributed estimates, not sales the ad would cause (B26).
  B2 placement-ceiling. "My bid on 'weighted blanket 15 lbs' is $1.20 but top of search costs me about $3 a click. Overcharged?" No:
     up and down with top of search +200% gives a maximum effective bid of 1.20 x 3 = 3.60, then up to +100% = 7.20 (B5, B6, B7);
     Amazon never charges above the maximum effective bid (B1); rest of search reaches 2.40 under the current pages' 100% and 1.80 under
     the author guide's 50% (B6). Ways down: MANUAL or down only, or a lower top-of-search adjustment.
  B3 rule-based-not-eligible. "Switch my new waffle auto campaign to rule-based bidding at ROAS 4." It reads LEGACY_FOR_SALES because
     an API campaign created with no strategy gets down only (B5); rule-based needs 10 days running (met: created 10-28) and 10
     conversions in the last 30 days (not met: the report holds 4) and a minimum daily budget (B11); so not now; no write.

ads-search-terms
  S1 harvest-and-negate. "Go through SP | Throws | Auto's search terms since Oct 12: what goes to exact, what gets negated?"
     Promote the converting terms ("throw blanket" 42 orders, "fleece throw" 27, "cream fleece throw" 3 of 15 clicks) as exact in a
     manual campaign and negate them exact in the auto (S18, practitioners' practice, not Amazon's rule); negate "electric heated
     throw blanket" (42 clicks, 0 orders: 95% upper bound about 3/42 = 7%, under the campaign's 83/942 = 8.8%, S20);
     leave "sherpa throw" (under 20 clicks, S13, C9); "christmas throw blanket" clicked only on 11-05..11-08, too recent (S21);
     "b0compet01" is a detail page, negated as a product target, not a keyword (S2, S5); "*" is a detail-page placement (S2).
  S2 negative-phrase-leak. "I negated 'heated blanket' as a phrase three weeks ago and still pay for heated searches." The negative is
     NEGATIVE_PHRASE at ad-group level in Knit only (S6): "heated blanket for couch" comes through ad group Fleece Cream, where it is
     not negated; "heated throw blanket" does not hold the complete phrase in sequence (S7); "blanket heated" depends on whether phrase
     is order-sensitive, which practitioners dispute (S19); "heated blanket" itself stopped after 10-21, inside the 72-hour buffer
     (S8). An existing negative's match type cannot be changed (S7); add new negatives (e.g. phrase "heated", 4 words or fewer).
  S3 no-asin-column. "Which search terms sold the weighted blanket in SP | Bedding | Auto, and which got impressions but no clicks?"
     The search term report has no advertised-ASIN column (S3) and its ad group holds B0FIXTURE4 and B0FIXTURE5; terms with
     impressions and no click have no row (S1), so spTargeting's impressions exceed the search-term rows'; spAdvertisedProduct gives
     per-ASIN totals only. Splitting the products into their own ad groups is what lets the terms be read by ASIN.

ads-structure-and-targets
  T1 exact-close-variants. "My exact keyword 'sherpa blanket queen' shows 'sherpa blankets queen', 'sherpa blanket queeen' and
     'sherpa queen blanket'. Is exact broken?" No match type is a literal string match: exact covers plurals and misspellings, and
     Amazon's guides disagree on reordering (T23); a variant is kept out with a negative exact in that ad group (S7).
  T2 match-type-fixed. "Change 'throw blanket' in SP | Throws | Broad from broad to phrase." A keyword's match type is fixed at
     creation (T4): add a phrase keyword beside it and pause (not archive, which is terminal, T6) the broad one; with one keyword in
     several match types the highest bid serves (T22). No write in this run; the stub refuses any PUT.
  T3 brand-searches. "Who advertises on my brand searches, and should I keep bidding on 'hearthly'?" No Amazon share metric names a
     competitor and no field flags a term as branded (T32, T42); Brand Analytics Top Search Terms (tenant/reports/...) names the three
     most-clicked products per term, where B0COMPET03 is second on "hearthly"; the brand-defence evidence is from search engines,
     not Amazon (T43).

ads-seasons
  E1 bfcm-plan. "Black Friday is coming: dates and budgets?" Black Friday 2026-11-27, Cyber Monday 2026-11-30; Amazon had not
     published US Black Friday Week dates on 2026-11-09 (E1); Amazon's guidance is +20-30% daily budgets from three to five days before
     each peak, guidance not limits, and Ad Badger's 2-3x is a practitioner view (E5, E6); the stub's budget-rule event recommendation
     gives each campaign a suggestedBudgetIncreasePercent (E3); budget rules only raise (B27); SP | Sherpa | Exact already runs out.
  E2 deal-day-conversion. "Nov 3 ACOS on SP | Sherpa | Exact was 14% against about 26% on its other days; raise bids?" The
     conversion jump is the Lightning Deal (notes/deals.md, 44.99 for 8 hours), not the ads; a deal-day rate is not the new normal and
     a post-promotion dip can follow (E9, E18); the days around it are still settling in the 7-day window (E8).
  E3 deal-claim-headline. "Run an SB headline 'Black Friday: 30% off Hearthly sherpa, lowest price ever' from Nov 20." Not as
     written: a deal must be live whenever its ad is, numeric savings only where Amazon renders them, no pricing superlatives,
     "Black Friday" is bounded by its duration (E13); the deal badge renders on its own (E12, P10).

ads-economics
  G1 break-even-with-fees. "What ACOS can the weighted blanket afford?" (79.99 - 22.00 cost - 12.00 referral - 9.10 FBA) / 79.99
     = 46.1% break-even ACOS (G1, G4), with today's fee estimate (stub); the campaign runs about 57%, so each ad sale loses money; the 2026-09-30 estimate in the tree (8.78) predates the
     holiday peak fee from 2026-10-15 (G5); estimates are not guaranteed (G4); returns are not deducted from attributed sales (G7);
     the seller's 30% target is a profit goal, not break-even.
  G2 ntb-for-sp. "How many new-to-brand customers did SP bring last month against SB?" None can be read: Amazon's help says NTB data
     "isn't available for Sponsored Products" and no SP v3 report type carries NTB columns (the stub refuses them), while v1 lists SP
     in 90 of 102 NTB fields' eligibility (G10); SB's figure is in sbCampaigns newToBrandPurchases, 14-day.
  G3 other-sku-halo. "SP | Throws | Auto runs 18% ACOS, far under the cream fleece's break-even; profitable?" About 58% of its
     attributed sales are other SKUs (sales7d against attributedSalesSameSku7d in spAdvertisedProduct, G20); on the advertised SKU
     alone ACOS is about 42%, just above its break-even of 40% ((29.99 - 7.40 - 4.50 - 6.05) / 29.99); counting the other SKUs at
     their own margins the campaign covers its cost, but attributed is not incremental (G19, G26). A new spPurchasedProduct
     report (stub source only) names the other SKUs by purchasedAsin: B0FIXTURE5 $1,919.76, B0FIXTURE4 $299.95, B0FIXTURE3 $134.97.

ads-change
  C1 regression-to-mean. "The bid raise on 'weighted blanket 15 lbs' on 10-19 cut ACOS from 69% to 48%. It worked, right?"
     The before-week was the campaign's worst (picked for being extreme, C18): the weeks of 9-28 and 10-05 ran 44% and 41%, so
     against them ACOS rose, and the log's own "under 45%" was not met; CPC rose from about 1.46 to 1.73; the unlogged top-of-search change 100 -> 200 on 10-22 is in POST /history and confounds (C1,
     who made it is not returned); a report shows only the bid that ran (C27). Verdict: not a win; not held or cannot tell (C19).
  C2 who-changed-budget. "My Sherpa budget used to be $80. Did someone change it?" POST /history: BUDGET_AMOUNT 80.0 -> 50.0 at
     2026-10-27T03:12:44Z (10-26 20:12 PDT); history does not say who (C1); the seller's log lacks it; notes list the owner, an agency
     login and a bid-tool trial (10-20..10-31) as hands that could; since then IN_BUDGET flips false every day, mostly 11:20-14:05
     Pacific, where before it the days that spent the whole $80 (16 of 29 from 09-28) flipped late, 19:51 on 10-26 and after 23:00
     on the others, and an out-of-budget campaign does not serve until midnight (B23).
  C3 too-early. "Since the -20% bid cut on SP | Throws | Broad on Nov 5, ACOS fell from 30% to 23%. It worked; cut another 20%?"
     Not yet: four days and four orders, every day inside the 7-day window and still settling (M14, E8); the log's own windows run to
     11-19 and read on or after 11-26; a test stopped on watching its results is unreliable (C16); Amazon reviews bids about every two
     weeks, practitioners wait 7-14 days (C9, C20). No verdict, and no second cut, now.

ads-launch
  L1 new-child-first-campaign. "Launch B0FIXTURE9, no reviews yet." The eligibility read (stub) is ELIGIBLE for sp; no eligibility
     reason reads reviews (L3); Amazon advises starting with an automatic SP campaign and harvesting manual targets from its search
     terms (L10); build campaign, ad group, product ad by SKU, created PAUSED (L20, T49); the initial budget recommendation (stub)
     is $18 against Amazon's $10 suggestion (L11); judge keywords after 20 clicks, negatives after two weeks (L12). No write.
  L2 variation-parent. "Advertise the parent B0FIXTURE8 so every sherpa size shows." The parent is INELIGIBLE, VARIATION_PARENT
     (L1, P1); advertise the children B0FIXTURE4 (already in SP | Sherpa | Exact, out of budget daily) and B0FIXTURE9.
  L3 honeymoon-plan. "My agency's launch plan (notes/agency-launch-plan.md): fine?" No Amazon page claims a honeymoon boost and
     practitioners disagree (L13); search-find-buy and two-step URLs are prohibited (L16); opening bids above suggestion is one
     practitioner's choice among several (L19).
"""
import datetime as dt
import gzip
import hashlib
import json
import os
import shutil
import sys

root = sys.argv[1]
SUMMARY = "--summary" in sys.argv[2:]
T = os.path.join(root, "tenant")
S = os.path.join(root, "stub-replies")
shutil.rmtree(T, ignore_errors=True)
shutil.rmtree(S, ignore_errors=True)
for stale in ("stub-state", "cx-calls.log"):
    p = os.path.join(root, stale)
    shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else (os.path.exists(p) and os.remove(p))

M = "ATVPDKIKX0DER"
SELLER = "A1FIXTURESELLER"
PROFILE = "1111111111111111"
PROFILE_CA = "2222222222222222"
ORIGIN = "https://advertising-api.amazon.com"
TODAY = dt.date(2026, 11, 9)
FIRST = dt.date(2026, 9, 28)
LAST = dt.date(2026, 11, 8)
DAYS = [FIRST + dt.timedelta(n) for n in range((LAST - FIRST).days + 1)]
D = dt.date.fromisoformat


def put(base, rel, data):
    path = os.path.join(base, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(data if isinstance(data, str) else json.dumps(data, indent=2))


def tree(rel, data):
    put(T, rel, data)


def stub(rel, data):
    put(S, rel, data)


def u(*parts):
    """A stable number in [0, 1) from its parts."""
    return int(hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:12], 16) / float(1 << 48)


def jit(amp, *parts):
    return 1 + amp * (2 * u(*parts) - 1)


def epoch_ms(iso):
    return int(dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)


# ---------------------------------------------------------------------------------------------------------------------------
# Catalog and prices

CATALOG = {
    "B0FIXTURE1": ("HL-FLEECE-GRY", "Hearthly Fleece Throw Blanket 50x60, Grey", 29.99),
    "B0FIXTURE2": ("HL-PLUSH-GRY", "Hearthly Plush Throw Blanket 50x60, Grey", 34.99),
    "B0FIXTURE3": ("HL-KNIT-CRM", "Hearthly Chunky Knit Throw Blanket, Cream", 44.99),
    "B0FIXTURE4": ("HL-SHERPA-Q", "Hearthly Sherpa Fleece Blanket Queen 90x90, Navy", 59.99),
    "B0FIXTURE5": ("HL-WEIGHTED-15", "Hearthly Weighted Blanket 15 lb, 60x80, Grey", 79.99),
    "B0FIXTURE6": ("HL-FLEECE-CRM", "Hearthly Fleece Throw Blanket 50x60, Cream", 29.99),
    "B0FIXTURE7": ("HL-WAFFLE-OAT", "Hearthly Waffle Knit Throw Blanket 50x60, Oatmeal", 39.99),
    "B0FIXTURE9": ("HL-SHERPA-K", "Hearthly Sherpa Fleece Blanket King 108x90, Navy", 69.99),
}
SKU = {a: v[0] for a, v in CATALOG.items()}


def price(asin, day):
    if asin == "B0FIXTURE2" and day >= D("2026-10-29"):
        return 39.99
    if asin == "B0FIXTURE4" and day == D("2026-11-03"):
        return 44.99
    return CATALOG[asin][2]


# ---------------------------------------------------------------------------------------------------------------------------
# The advertising account: entities

CAMPAIGNS = {
    # id: (name, targetingType, strategy, placement adjustments, budget, start, created, portfolio)
    "311000000000001": ("SP | Fleece Grey | Auto", "AUTO", "LEGACY_FOR_SALES", [], 30.0, "2026-03-02"),
    "311000000000002": ("SP | Plush Grey | Manual", "MANUAL", "LEGACY_FOR_SALES", [], 25.0, "2026-03-02"),
    "311000000000003": ("SP | Sherpa | Exact", "MANUAL", "LEGACY_FOR_SALES", [], 50.0, "2026-04-10"),
    "311000000000004": ("SP | Weighted | Exact", "MANUAL", "AUTO_FOR_SALES", [{"placement": "PLACEMENT_TOP", "percentage": 200}], 60.0, "2026-05-04"),
    "311000000000005": ("SP | Throws | Auto", "AUTO", "LEGACY_FOR_SALES", [], 35.0, "2026-03-02"),
    "311000000000006": ("SP | Bedding | Auto", "AUTO", "LEGACY_FOR_SALES", [], 30.0, "2026-05-04"),
    "311000000000007": ("SP | Throws | Broad", "MANUAL", "LEGACY_FOR_SALES", [], 40.0, "2026-06-15"),
    "311000000000008": ("SP | Waffle | Auto", "AUTO", "LEGACY_FOR_SALES", [], 15.0, "2026-10-28"),
}
CREATED = {"311000000000008": "2026-10-28T19:20:40Z"}

AD_GROUPS = {
    # id: (campaign, name, defaultBid)
    "321000000000011": ("311000000000001", "Fleece Grey", 0.85),
    "321000000000021": ("311000000000002", "Plush Grey", 0.90),
    "321000000000031": ("311000000000003", "Sherpa Queen", 1.40),
    "321000000000041": ("311000000000004", "Weighted 15 lb", 1.00),
    "321000000000051": ("311000000000005", "Throws Auto", 0.75),
    "321000000000061": ("311000000000006", "Bedding Auto", 0.80),
    "321000000000071": ("311000000000007", "Knit", 0.90),
    "321000000000072": ("311000000000007", "Fleece Cream", 0.80),
    "321000000000081": ("311000000000008", "Waffle Auto", 0.70),
}

ADS = {
    # id: (adGroup, asin)
    "331000000000011": ("321000000000011", "B0FIXTURE1"),
    "331000000000021": ("321000000000021", "B0FIXTURE2"),
    "331000000000031": ("321000000000031", "B0FIXTURE4"),
    "331000000000041": ("321000000000041", "B0FIXTURE5"),
    "331000000000051": ("321000000000051", "B0FIXTURE6"),
    "331000000000061": ("321000000000061", "B0FIXTURE4"),
    "331000000000062": ("321000000000061", "B0FIXTURE5"),
    "331000000000071": ("321000000000071", "B0FIXTURE3"),
    "331000000000072": ("321000000000072", "B0FIXTURE6"),
    "331000000000081": ("321000000000081", "B0FIXTURE7"),
}

KEYWORDS = {
    # id: (adGroup, text, matchType, bid now, bid on 2026-11-02)
    "341000000000021": ("321000000000021", "grey throw blanket", "BROAD", 0.95, 0.95),
    "341000000000022": ("321000000000021", "plush throw blanket", "PHRASE", 0.90, 0.90),
    "341000000000031": ("321000000000031", "sherpa blanket queen", "EXACT", 1.50, 1.50),
    "341000000000032": ("321000000000031", "sherpa fleece blanket", "EXACT", 1.20, 1.20),
    "341000000000041": ("321000000000041", "weighted blanket 15 lbs", "EXACT", 1.20, 1.20),
    "341000000000042": ("321000000000041", "weighted blanket queen", "EXACT", 1.05, 1.05),
    "341000000000071": ("321000000000071", "throw blanket", "BROAD", 0.80, 1.00),
    "341000000000072": ("321000000000072", "warm blanket", "BROAD", 0.72, 0.90),
}

AUTO_GROUPS = [("QUERY_HIGH_REL_MATCHES", "close-match"), ("QUERY_BROAD_REL_MATCHES", "loose-match"),
               ("ASIN_SUBSTITUTE_RELATED", "substitutes"), ("ASIN_ACCESSORY_RELATED", "complements")]
TARGETS = {}  # id: (adGroup, expression type, report targeting text, bid)
for ag, base in (("321000000000011", 351000000000110), ("321000000000051", 351000000000510),
                 ("321000000000061", 351000000000610), ("321000000000081", 351000000000810)):
    for n, (etype, text) in enumerate(AUTO_GROUPS, 1):
        TARGETS[str(base + n)] = (ag, etype, text, AD_GROUPS[ag][2])
T_ID = {(v[0], v[2]): k for k, v in TARGETS.items()}

NEG_KEYWORDS = {"361000000000071": ("321000000000071", "heated blanket", "NEGATIVE_PHRASE", "2026-10-20T17:30:12Z")}
CAMPAIGN_NEG_KEYWORDS = {"362000000000051": ("311000000000005", "blanket for dogs", "NEGATIVE_PHRASE", "2026-07-08T15:02:44Z")}


def camp_of(ag):
    return AD_GROUPS[ag][0]


# ---------------------------------------------------------------------------------------------------------------------------
# Traffic model: every row of every report is cut from one cube of (term, ad, day) clicks and orders.

LAGS = [(0, .45), (1, .18), (2, .10), (3, .07), (4, .05), (5, .04), (6, .03)] + [(k, .06 / 7) for k in range(7, 14)] + [(k, .02 / 16) for k in range(14, 30)]


def lag_of(*parts):
    x, acc = u("lag", *parts), 0.0
    for k, p in LAGS:
        acc += p
        if x < acc:
            return k
    return 29


PBDD = {D("2026-10-04"): (1.10, 1.00, .92), D("2026-10-05"): (1.12, 1.02, .90), D("2026-10-06"): (1.35, 1.10, .85),
        D("2026-10-07"): (1.35, 1.10, .85), D("2026-10-08"): (1.0, 1.0, .95)}


class Term:
    def __init__(self, ag, tgt, search, clicks, cpc, cvr, ctr=.005, ads=None, other=.08, mix=None, start=None, end=None):
        self.ag, self.tgt, self.search = ag, tgt, search
        self.clicks, self.cpc, self.cvr, self.ctr = clicks, cpc, cvr, ctr
        self.ads = ads or [(a, 1.0) for a, (g, _) in ADS.items() if g == ag]
        self.other = other
        self.mix = mix or [("B0FIXTURE5", .5), ("B0FIXTURE4", .3), ("B0FIXTURE3", .2)]
        self.start, self.end = (D(start) if start else None), (D(end) if end else None)

    @property
    def camp(self):
        return camp_of(self.ag)


def kw(ag, text):
    return next(k for k, v in KEYWORDS.items() if v[0] == ag and v[1] == text)


AG = {name: k for k, (c, name, b) in AD_GROUPS.items()}
TERMS = []


def add(ag_name, target, rows, **kw_):
    ag = AG[ag_name]
    tgt = T_ID.get((ag, target)) or kw(ag, target)
    for row in rows:
        search, clicks, cpc, cvr = row[:4]
        extra = row[4] if len(row) > 4 else {}
        TERMS.append(Term(ag, tgt, search, clicks, cpc, cvr, **{**kw_, **extra}))


mix_grey = dict(mix=[("B0FIXTURE6", .5), ("B0FIXTURE2", .3), ("B0FIXTURE3", .2)])
add("Fleece Grey", "close-match", [("grey fleece throw", 4.0, .80, .12), ("fleece throw blanket grey", 3.0, .80, .12)], **mix_grey)
add("Fleece Grey", "loose-match", [("soft throw blanket", 3.0, .78, .08)], **mix_grey)
add("Fleece Grey", "substitutes", [("b0compet02", 2.0, .70, .06)], **mix_grey)
add("Fleece Grey", "complements", [("*", 1.5, .62, .05)], **mix_grey)
add("Plush Grey", "grey throw blanket", [("grey throw blanket", 7.0, .92, .12), ("gray throw blanket", 3.0, .92, .12), ("grey blanket for couch", 3.0, .90, .11)], **mix_grey)
add("Plush Grey", "plush throw blanket", [("plush throw blanket", 4.0, .93, .12), ("plush throw blanket grey", 2.0, .93, .13)], **mix_grey)
mix_sherpa = dict(other=.06, mix=[("B0FIXTURE5", .7), ("B0FIXTURE3", .3)])
add("Sherpa Queen", "sherpa blanket queen", [("sherpa blanket queen", 30.0, 1.45, .105), ("sherpa blankets queen", 6.0, 1.45, .10),
                                             ("sherpa blanket queeen", 1.5, 1.40, .09), ("sherpa queen blanket", 4.0, 1.42, .10)], **mix_sherpa)
add("Sherpa Queen", "sherpa fleece blanket", [("sherpa fleece blanket", 12.0, 1.15, .10), ("sherpa fleece blankets", 3.0, 1.15, .09)], **mix_sherpa)
mix_w = dict(other=.07, mix=[("B0FIXTURE4", .6), ("B0FIXTURE6", .4)])
add("Weighted 15 lb", "weighted blanket 15 lbs", [("weighted blanket 15 lbs", 14.0, 1.45, .046), ("weighted blanket 15 lb", 5.0, 1.45, .046),
                                                 ("15 lb weighted blanket", 4.0, 1.44, .045)], **mix_w)
add("Weighted 15 lb", "weighted blanket queen", [("weighted blanket queen", 8.0, 1.45, .047), ("weighted blankets queen", 2.0, 1.45, .045)], **mix_w)
mix_auto = dict(other=.40, mix=[("B0FIXTURE5", .6), ("B0FIXTURE4", .25), ("B0FIXTURE3", .15)])
add("Throws Auto", "close-match", [("throw blanket", 16.0, .78, .12), ("fleece throw", 10.0, .76, .12), ("fleece throw blanket", .80, .75, .13), ("cream fleece throw", .55, .74, .20), ("fleece blanket", .90, .76, .05),
                                   ("hearthly blanket", .22, .55, .33), ("soft throw blanket cream", .50, .74, .10)], **mix_auto)
add("Throws Auto", "loose-match", [("electric heated throw blanket", 1.45, .90, .0), ("sherpa throw", .32, .80, .0),
                                   ("throw blanket for couch", 1.20, .78, .09),
                                   ("christmas throw blanket", 3.0, .82, .0, dict(start="2026-11-05"))], **mix_auto)
add("Throws Auto", "substitutes", [("b0compet01", .50, .70, .0), ("b0compet04", .40, .70, .10)], **mix_auto)
add("Throws Auto", "complements", [("*", 1.10, .60, .06)], **mix_auto)
A61, A62 = "331000000000061", "331000000000062"
add("Bedding Auto", "close-match", [("weighted blanket", 1.5, .95, .05, dict(ads=[(A62, .85), (A61, .15)])),
                                    ("sherpa blanket", 1.2, .92, .08, dict(ads=[(A61, .8), (A62, .2)])),
                                    ("weighted blanket for adults", .06, .95, .0, dict(ads=[(A62, 1.0)], ctr=.0006))])
add("Bedding Auto", "loose-match", [("heavy blanket for sleeping", .6, .90, .06, dict(ads=[(A62, .7), (A61, .3)])),
                                    ("queen blanket", .8, .85, .03, dict(ads=[(A61, .6), (A62, .4)])),
                                    ("king size blanket", .05, .85, .0, dict(ads=[(A61, 1.0)], ctr=.0005))])
add("Bedding Auto", "complements", [("*", .7, .70, .04, dict(ads=[(A61, .5), (A62, .5)]))])
mix_b = dict(other=.10, mix=[("B0FIXTURE6", .5), ("B0FIXTURE1", .5)])
add("Knit", "throw blanket", [("throw blanket", 6.0, .88, .07), ("knit throw blanket", 3.0, .90, .12), ("chunky knit blanket", 2.5, .92, .10),
                              ("heated blanket", 1.2, .86, .0, dict(end="2026-10-21")), ("heated throw blanket", .6, .86, .0),
                              ("blanket heated", .2, .85, .0), ("cream throw blanket", 1.0, .88, .08)], **mix_b)
add("Fleece Cream", "warm blanket", [("warm blanket", 3.0, .78, .06), ("warm fleece blanket", 1.5, .78, .10),
                                     ("heated blanket for couch", .45, .80, .0), ("warm blanket for winter", 1.0, .77, .05)], **mix_b)
add("Waffle Auto", "close-match", [("waffle knit throw", 1.8, .62, .07), ("waffle blanket", 2.2, .60, .05)], start="2026-10-28")
add("Waffle Auto", "loose-match", [("cotton throw blanket", 1.5, .58, .04)], start="2026-10-28")
add("Waffle Auto", "complements", [("*", .9, .50, .03)], start="2026-10-28")

KW15 = kw(AG["Weighted 15 lb"], "weighted blanket 15 lbs")


def mods(term, day):
    """(clicks, cpc, cvr) multipliers for one term on one day."""
    c, p, v = PBDD.get(day, (1.0, 1.0, 1.0))
    camp = term.camp
    if camp == "311000000000001":  # Featured Offer lost about 10:00 PST on 11-04
        c *= .35 if day == D("2026-11-04") else (0.0 if day > D("2026-11-04") else 1.0)
    if camp == "311000000000002":
        if day >= D("2026-10-29"):
            v *= .5  # the seller's own price rise
        c *= .25 if day == D("2026-11-06") else (0.0 if day > D("2026-11-06") else 1.0)
    if camp == "311000000000003" and day == D("2026-11-03"):
        c, v = c * 1.6, v * 1.9
    if camp == "311000000000004":
        if D("2026-10-12") <= day <= D("2026-10-18"):
            v *= .78
        if term.tgt == KW15:
            if day == D("2026-10-19"):
                c, p = c * 1.1, p * 1.06
            elif D("2026-10-20") <= day <= D("2026-10-21"):
                c, p = c * 1.2, p * 1.12
            elif day >= D("2026-10-22"):
                c, p = c * 1.35, p * 1.24
        elif day >= D("2026-10-22"):
            c, p = c * 1.1, p * 1.12
    if camp == "311000000000007":
        if day == D("2026-11-05"):
            c, p = c * .82, p * .85
        elif day > D("2026-11-05"):
            c, p = c * .75, p * .8
    return c, p, v


def spend_cap(camp, day):
    if camp == "311000000000003":
        if day == D("2026-11-03"):
            return 71.30
        return 80.0 if day <= D("2026-10-26") else 50.0 * jit(.004, "cap", day)
    return None


def budget_on(camp, day):
    if camp == "311000000000003" and day <= D("2026-10-26"):
        return 80.0
    return CAMPAIGNS[camp][4]


class Cell:
    __slots__ = ("term", "ad", "day", "impressions", "clicks", "cost", "orders")

    def __init__(self, term, ad, day):
        self.term, self.ad, self.day = term, ad, day
        self.impressions = self.clicks = 0
        self.cost = 0.0
        self.orders = []  # (lag, purchased asin, units, sales)


CELLS = []
carry = {}
CAPPED = set()  # (campaign, day) that spent its whole cap: history shows those as IN_BUDGET true -> false
for day in DAYS:
    by_camp = {}
    for i, term in enumerate(TERMS):
        if CAMPAIGNS[term.camp][5] > day.isoformat() or (term.start and day < term.start) or (term.end and day > term.end):
            continue
        c, p, v = mods(term, day)
        for ad, share in term.ads:
            cell = Cell(term, ad, day)
            exp = term.clicks * share * c * jit(.25, "clk", i, ad, day)
            key = ("c", i, ad)
            carry[key] = carry.get(key, 0.0) + exp
            cell.clicks = int(carry[key] + .5) - int(carry[key] - exp + .5)
            cell.impressions = int(round(term.clicks * share * c / term.ctr * jit(.18, "imp", i, ad, day)))
            cell.cost = cell.clicks * term.cpc * p * jit(.06, "cpc", i, ad, day)
            by_camp.setdefault(term.camp, []).append((i, cell, v))
    for camp, cells in by_camp.items():
        cap = spend_cap(camp, day)
        total = sum(cl.cost for _, cl, _ in cells)
        if cap is not None and total > cap:
            CAPPED.add((camp, day))
            s = cap / total
            for _, cl, _ in cells:
                cl.clicks = int(round(cl.clicks * s))
                cl.impressions = int(round(cl.impressions * (.55 + .45 * s)))
            total2 = sum(cl.clicks * cl.term.cpc for _, cl, _ in cells) or 1.0
            for _, cl, _ in cells:
                cl.cost = cap * cl.clicks * cl.term.cpc / total2
        for i, cl, v in cells:
            exp = cl.clicks * cl.term.cvr * v
            key = ("o", i, cl.ad)
            carry[key] = carry.get(key, 0.0) + exp
            n = int(carry[key] + .5) - int(carry[key] - exp + .5)
            own = ADS[cl.ad][1]
            for j in range(n):
                lag = lag_of(i, cl.ad, day, j)
                asin = own
                if u("oth", i, cl.ad, day, j) < cl.term.other:
                    x, acc = u("mix", i, cl.ad, day, j), 0.0
                    for a, w in cl.term.mix:
                        acc += w
                        if x < acc:
                            asin = a
                            break
                units = 2 if u("units", i, cl.ad, day, j) < .06 else 1
                cl.orders.append((lag, asin, units, round(units * price(asin, day + dt.timedelta(lag)), 2)))
            cl.cost = round(cl.cost, 2)
            CELLS.append(cl)


def seen(day, lag, read):
    return day + dt.timedelta(lag) <= read - dt.timedelta(1)


def metrics(cells, read, own_asins):
    """The Reporting v3 SP metric family over a group of cells, as read on date `read`."""
    out = {"impressions": sum(c.impressions for c in cells), "clicks": sum(c.clicks for c in cells), "cost": round(sum(c.cost for c in cells), 2)}
    for w in (1, 7, 14, 30):
        o = [(c, x) for c in cells for x in c.orders if x[0] < w and seen(c.day, x[0], read)]
        same = [(c, x) for c, x in o if x[1] in own_asins(c)]
        out[f"purchases{w}d"] = len(o)
        out[f"purchasesSameSku{w}d"] = len(same)
        out[f"unitsSoldClicks{w}d"] = sum(x[2] for _, x in o)
        out[f"unitsSoldSameSku{w}d"] = sum(x[2] for _, x in same)
        out[f"sales{w}d"] = round(sum(x[3] for _, x in o), 2)
        out[f"attributedSalesSameSku{w}d"] = round(sum(x[3] for _, x in same), 2)
        if w == 7:
            out["salesOtherSku7d"] = round(out["sales7d"] - out["attributedSalesSameSku7d"], 2)
            out["unitsSoldOtherSku7d"] = out["unitsSoldClicks7d"] - out["unitsSoldSameSku7d"]
    out["costPerClick"] = round(out["cost"] / out["clicks"], 4) if out["clicks"] else 0.0
    out["clickThroughRate"] = round(out["clicks"] / out["impressions"], 6) if out["impressions"] else 0.0
    return out


def ad_asin(c):
    return {ADS[c.ad][1]}


def camp_asins(c):
    return {ADS[a][1] for a, (g, _) in ADS.items() if camp_of(g) == c.term.camp}


def active(m):
    return m["impressions"] or m["clicks"] or m["cost"] or m["purchases30d"]


def group(cells, keyf):
    g = {}
    for c in cells:
        g.setdefault(keyf(c), []).append(c)
    return g


def sp_campaign_rows(read, start, end):
    rows = []
    for (camp, day), cells in sorted(group([c for c in CELLS if start <= c.day <= end], lambda c: (c.term.camp, c.day)).items(), key=lambda kv: (kv[0][1], kv[0][0])):
        m = metrics(cells, read, camp_asins)
        if not active(m):
            continue
        rows.append({"date": day.isoformat(), "campaignId": camp, "campaignName": CAMPAIGNS[camp][0], "campaignStatus": "ENABLED",
                     "campaignBudgetAmount": budget_on(camp, day), "campaignBudgetType": "DAILY_BUDGET", "campaignBudgetCurrencyCode": "USD",
                     **m, "spend": m["cost"]})
    return rows


PLACEMENTS = ["Top of Search on-Amazon", "Other on-Amazon", "Detail Page on-Amazon", "Off Amazon"]


def placement_profile(camp, day):
    # (click share, cpc multiplier, conversion multiplier, impressions per click)
    if camp == "311000000000004":
        if day >= D("2026-10-22"):
            return [(.45, 2.40, 1.20, 90), (.20, .70, 1.0, 220), (.30, .62, .85, 300), (.05, .50, .5, 600)]
        return [(.32, 1.70, 1.20, 95), (.25, .80, 1.0, 220), (.38, .72, .85, 300), (.05, .55, .5, 600)]
    return [(.30, 1.35, 1.20, 90), (.25, .85, 1.0, 220), (.40, .80, .85, 300), (.05, .55, .5, 600)]


def sp_placement_rows(read, start, end):
    rows = []
    for (camp, day), cells in sorted(group([c for c in CELLS if start <= c.day <= end], lambda c: (c.term.camp, c.day)).items(), key=lambda kv: (kv[0][1], kv[0][0])):
        m = metrics(cells, read, camp_asins)
        if not active(m):
            continue
        prof = placement_profile(camp, day)
        clicks = [int(m["clicks"] * s) for s, *_ in prof]
        for k in sorted(range(4), key=lambda k: -(m["clicks"] * prof[k][0] - clicks[k]))[:m["clicks"] - sum(clicks)]:
            clicks[k] += 1
        wsum = sum(cl * p[1] for cl, p in zip(clicks, prof)) or 1.0
        orders = [(c, x) for c in cells for x in c.orders]
        place_of = {}
        for n, (c, x) in enumerate(orders):
            weights = [cl * p[2] for cl, p in zip(clicks, prof)]
            tot, r, acc = sum(weights) or 1.0, u("pl", camp, day, n), 0.0
            for k, wgt in enumerate(weights):
                acc += wgt / tot
                if r < acc:
                    place_of[n] = k
                    break
            else:
                place_of[n] = 0
        imp_left = m["impressions"]
        for k, name in enumerate(PLACEMENTS):
            cost = round(m["cost"] * clicks[k] * prof[k][1] / wsum, 2)
            imp = imp_left if k == 3 else min(imp_left, int(m["impressions"] * clicks[k] * prof[k][3] / max(1, sum(cl * p[3] for cl, p in zip(clicks, prof)))))
            imp_left -= imp if k != 3 else 0
            row = {"date": day.isoformat(), "campaignId": camp, "campaignName": CAMPAIGNS[camp][0], "placementClassification": name,
                   "impressions": imp, "clicks": clicks[k], "cost": cost}
            mine = [(c, x) for n, (c, x) in enumerate(orders) if place_of[n] == k]
            for w in (1, 7, 14, 30):
                o = [(c, x) for c, x in mine if x[0] < w and seen(c.day, x[0], read)]
                same = [(c, x) for c, x in o if x[1] in camp_asins(c)]
                row[f"purchases{w}d"] = len(o)
                row[f"purchasesSameSku{w}d"] = len(same)
                row[f"unitsSoldClicks{w}d"] = sum(x[2] for _, x in o)
                row[f"unitsSoldSameSku{w}d"] = sum(x[2] for _, x in same)
                row[f"sales{w}d"] = round(sum(x[3] for _, x in o), 2)
                row[f"attributedSalesSameSku{w}d"] = round(sum(x[3] for _, x in same), 2)
            row["costPerClick"] = round(cost / clicks[k], 4) if clicks[k] else 0.0
            row["clickThroughRate"] = round(clicks[k] / imp, 6) if imp else 0.0
            row["spend"] = cost
            if imp or clicks[k]:
                rows.append(row)
    return rows


def target_cols(tgt):
    if tgt in KEYWORDS:
        ag, text, mt, bid, _ = KEYWORDS[tgt]
        return {"keywordId": tgt, "keyword": text, "keywordType": mt, "matchType": mt, "targeting": text}
    ag, etype, text, bid = TARGETS[tgt]
    return {"keywordId": tgt, "keyword": text, "keywordType": "TARGETING_EXPRESSION_PREDEFINED", "matchType": "TARGETING_EXPRESSION_PREDEFINED", "targeting": text}


def bid_on(tgt, day):
    if tgt in KEYWORDS:
        if tgt == KW15 and day < D("2026-10-19"):
            return 0.90
        if tgt in ("341000000000071", "341000000000072") and day < D("2026-11-05"):
            return KEYWORDS[tgt][4]
        return KEYWORDS[tgt][3]
    return TARGETS[tgt][3]


def sp_targeting_rows(read, start, end, by_term=False):
    rows = []
    keyf = (lambda c: (c.term.ag, c.term.tgt, c.term.search, c.day)) if by_term else (lambda c: (c.term.ag, c.term.tgt, c.day))
    for key, cells in sorted(group([c for c in CELLS if start <= c.day <= end], keyf).items(), key=lambda kv: (kv[0][-1], kv[0][:-1])):
        ag, tgt, day = key[0], key[1], key[-1]
        m = metrics(cells, read, camp_asins)
        if by_term and not m["clicks"]:
            continue  # the search term report holds only terms with an ad click
        if not active(m):
            continue
        row = {"date": day.isoformat(), "campaignId": camp_of(ag), "campaignName": CAMPAIGNS[camp_of(ag)][0], "adGroupId": ag,
               "adGroupName": AD_GROUPS[ag][1], **target_cols(tgt), "keywordBid": bid_on(tgt, day), "adKeywordStatus": "ENABLED"}
        if by_term:
            row["searchTerm"] = key[2]
        rows.append({**row, **m})
    return rows


def sp_advertised_rows(read, start, end):
    rows = []
    for (ad, day), cells in sorted(group([c for c in CELLS if start <= c.day <= end], lambda c: (c.ad, c.day)).items(), key=lambda kv: (kv[0][1], kv[0][0])):
        m = metrics(cells, read, ad_asin)
        if not active(m):
            continue
        ag, asin = ADS[ad]
        rows.append({"date": day.isoformat(), "campaignId": camp_of(ag), "campaignName": CAMPAIGNS[camp_of(ag)][0], "adGroupId": ag,
                     "adGroupName": AD_GROUPS[ag][1], "adId": ad, "advertisedAsin": asin, "advertisedSku": SKU[asin],
                     "campaignBudgetCurrencyCode": "USD", **m, "spend": m["cost"]})
    return rows


def sp_purchased_rows(read, start, end):
    """spPurchasedProduct: each ad's other-SKU purchases, by purchased ASIN and ad-interaction day."""
    rows = []
    for (ad, day), cells in sorted(group([c for c in CELLS if start <= c.day <= end], lambda c: (c.ad, c.day)).items(), key=lambda kv: (kv[0][1], kv[0][0])):
        ag, asin = ADS[ad]
        for p in sorted(set(x[1] for c in cells for x in c.orders if x[1] != asin)):
            row = {"date": day.isoformat(), "campaignId": camp_of(ag), "campaignName": CAMPAIGNS[camp_of(ag)][0], "adGroupId": ag,
                   "adGroupName": AD_GROUPS[ag][1], "advertisedAsin": asin, "advertisedSku": SKU[asin], "purchasedAsin": p,
                   "campaignBudgetCurrencyCode": "USD"}
            for w in (1, 7, 14, 30):
                o = [x for c in cells for x in c.orders if x[1] == p and x[0] < w and seen(c.day, x[0], read)]
                row[f"purchasesOtherSku{w}d"] = len(o)
                row[f"unitsSoldOtherSku{w}d"] = sum(x[2] for x in o)
                row[f"salesOtherSku{w}d"] = round(sum(x[3] for x in o), 2)
            if row["purchasesOtherSku30d"]:
                rows.append(row)
    return rows


# Sponsored Brands (CPC: clicks only, 14 days) and Sponsored Display (vCPM: clicks and views, 14 days).
SB = {
    "451000000000001": ("SB | Hearthly Throws | Collection", 40.0, 9000, 38, .70, .09, .55, ["B0FIXTURE1", "B0FIXTURE2", "B0FIXTURE6"]),
    "451000000000002": ("SB | Brand | hearthly", 15.0, 800, 22, .45, .20, .20, ["B0FIXTURE4", "B0FIXTURE6", "B0FIXTURE5"]),
}
SD = {"461000000000001": ("SD | Retarget views | Throws", 20.0, 25000, 20, .06, 1.2, .40, ["B0FIXTURE6", "B0FIXTURE3", "B0FIXTURE1"])}
BRAND_DAYS = {}
for cid, (name, budget, imp, clk, cpc, cvr, ntb, asins) in SB.items():
    for day in DAYS:
        c, p, v = PBDD.get(day, (1.0, 1.0, 1.0))
        if cid == "451000000000001" and day >= D("2026-11-04"):
            v *= .7
        clicks = int(round(clk * c * jit(.2, "sbc", cid, day)))
        orders = []
        exp = clicks * cvr * v
        carry[("sb", cid)] = carry.get(("sb", cid), 0.0) + exp
        n = int(carry[("sb", cid)] + .5) - int(carry[("sb", cid)] - exp + .5)
        for j in range(n):
            a = asins[int(u("sba", cid, day, j) * len(asins))]
            lag = lag_of("sb", cid, day, j)
            units = 2 if u("sbu", cid, day, j) < .08 else 1
            orders.append((lag, a, units, round(units * price(a, day + dt.timedelta(lag)), 2), u("ntb", cid, day, j) < ntb, False))
        BRAND_DAYS[(cid, day)] = {"impressions": int(round(imp * c * jit(.15, "sbi", cid, day))), "clicks": clicks,
                                  "cost": round(clicks * cpc * p * jit(.05, "sbp", cid, day), 2), "orders": orders}
for cid, (name, budget, imp, clk, cvr, views, ntb, asins) in SD.items():
    for day in DAYS:
        c, p, v = PBDD.get(day, (1.0, 1.0, 1.0))
        impressions = int(round(imp * c * jit(.15, "sdi", cid, day)))
        viewable = int(round(impressions * .68))
        clicks = int(round(clk * c * jit(.2, "sdc", cid, day)))
        orders = []
        for kind, exp in (("click", clicks * cvr * v), ("view", views * v)):
            carry[("sd", cid, kind)] = carry.get(("sd", cid, kind), 0.0) + exp
            n = int(carry[("sd", cid, kind)] + .5) - int(carry[("sd", cid, kind)] - exp + .5)
            for j in range(n):
                a = asins[int(u("sda", cid, kind, day, j) * len(asins))]
                lag = lag_of("sd", cid, kind, day, j)
                orders.append((lag, a, 1, price(a, day + dt.timedelta(lag)), u("sdn", cid, kind, day, j) < ntb, kind == "view"))
        BRAND_DAYS[(cid, day)] = {"impressions": impressions, "impressionsViews": viewable, "clicks": clicks,
                                  "cost": round(viewable / 1000 * 1.10 * p * jit(.05, "sdp", cid, day), 2), "orders": orders}


def brand_rows(table, read, start, end):
    rows = []
    for day in DAYS:
        if not start <= day <= end:
            continue
        for cid, spec in table.items():
            d = BRAND_DAYS[(cid, day)]
            o = [x for x in d["orders"] if x[0] < 14 and seen(day, x[0], read)]
            clk = [x for x in o if not x[5]]
            row = {"date": day.isoformat(), "campaignId": cid, "campaignName": spec[0], "campaignStatus": "ENABLED",
                   "campaignBudgetAmount": spec[1], "campaignBudgetCurrencyCode": "USD", "impressions": d["impressions"]}
            if table is SB:
                row["campaignBudgetType"] = "DAILY"
            else:
                row["impressionsViews"] = d["impressionsViews"]
            row.update({"clicks": d["clicks"], "cost": d["cost"], "purchases": len(o), "sales": round(sum(x[3] for x in o), 2),
                        "unitsSold": sum(x[2] for x in o), "purchasesClicks": len(clk), "salesClicks": round(sum(x[3] for x in clk), 2),
                        "newToBrandPurchases": sum(1 for x in o if x[4]), "newToBrandSales": round(sum(x[3] for x in o if x[4]), 2)})
            if table is SB:
                row["newToBrandUnitsSold"] = sum(x[2] for x in o if x[4])
                row["detailPageViews"] = int(round(d["clicks"] * 1.6))
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------------------------------------------------------
# Reports: the landed ones (earlier sessions) and the stub's sources (what a report created today is cut from)

REPORT_TYPES = {
    # reportTypeId: (adProduct, groupBy, builder)
    ("spCampaigns", "campaign"): ("SPONSORED_PRODUCTS", ["campaign"], sp_campaign_rows),
    ("spCampaigns", "campaignPlacement"): ("SPONSORED_PRODUCTS", ["campaign", "campaignPlacement"], sp_placement_rows),
    ("spTargeting", "targeting"): ("SPONSORED_PRODUCTS", ["targeting"], sp_targeting_rows),
    ("spSearchTerm", "searchTerm"): ("SPONSORED_PRODUCTS", ["searchTerm"], lambda r, s, e: sp_targeting_rows(r, s, e, by_term=True)),
    ("spAdvertisedProduct", "advertiser"): ("SPONSORED_PRODUCTS", ["advertiser"], sp_advertised_rows),
    ("spPurchasedProduct", "asin"): ("SPONSORED_PRODUCTS", ["asin"], sp_purchased_rows),
    ("sbCampaigns", "campaign"): ("SPONSORED_BRANDS", ["campaign"], lambda r, s, e: brand_rows(SB, r, s, e)),
    ("sdCampaigns", "campaign"): ("SPONSORED_DISPLAY", ["campaign"], lambda r, s, e: brand_rows(SD, r, s, e)),
}
n_report = [0]


def land_report(rtype, gkey, start, end, read, created):
    ad_product, group_by, build = REPORT_TYPES[(rtype, gkey)]
    rows = build(D(read), D(start), D(end))
    cols = list(dict.fromkeys(k for r in rows for k in r))
    n_report[0] += 1
    rid = f"{n_report[0]:08x}-f1x7-4ad5-9e0a-{hashlib.sha256((rtype + gkey + start + end + read).encode()).hexdigest()[:12]}"
    d = f"raw/amazon-ads/reports/{rtype}/{PROFILE}_{start}_{end}_DAILY_{gkey}/1"
    ask = {"name": f"{rtype} {start}..{end}", "startDate": start, "endDate": end,
           "configuration": {"adProduct": ad_product, "groupBy": group_by, "columns": cols, "reportTypeId": rtype, "timeUnit": "DAILY", "format": "GZIP_JSON"}}
    tree(f"{d}/report.json", rows)
    tree(f"{d}/receipt.json", {"origin": ORIGIN, "profileId": PROFILE, "reportId": rid, "status": "COMPLETED", "createdAt": created,
                               "generatedAt": created.replace(":05:", ":41:"), "landedAt": created.replace(":05:", ":44:"),
                               "document": "report.json", "decompressed": True, "rows": len(rows), "ask": ask})
    return rows


L = {}
L["sp_0928"] = land_report("spCampaigns", "campaign", "2026-09-28", "2026-10-11", "2026-10-26", "2026-10-26T16:05:10Z")
L["sp_1026_r1102"] = land_report("spCampaigns", "campaign", "2026-10-26", "2026-11-01", "2026-11-02", "2026-11-02T16:05:12Z")
L["sp_1012"] = land_report("spCampaigns", "campaign", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:08Z")
L["pl_1012"] = land_report("spCampaigns", "campaignPlacement", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:20Z")
L["tg_1012"] = land_report("spTargeting", "targeting", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:31Z")
L["st_1012"] = land_report("spSearchTerm", "searchTerm", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:43Z")
L["ap_1012"] = land_report("spAdvertisedProduct", "advertiser", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:55Z")
L["sb_1012"] = land_report("sbCampaigns", "campaign", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:58Z")
L["sd_1012"] = land_report("sdCampaigns", "campaign", "2026-10-12", "2026-11-08", "2026-11-09", "2026-11-09T15:05:59Z")

RETENTION = {"spCampaigns": 95, "spTargeting": 95, "spSearchTerm": 65, "spAdvertisedProduct": 95, "spPurchasedProduct": 95, "sbCampaigns": 60, "sdCampaigns": 65}
for (rtype, gkey), (ad_product, group_by, build) in REPORT_TYPES.items():
    stub(f"report-sources/{rtype}-{gkey}.json", {"reportTypeId": rtype, "adProduct": ad_product, "groupBy": group_by,
                                                 "maxDays": 31, "retentionDays": RETENTION[rtype], "read": TODAY.isoformat(),
                                                 "rows": build(TODAY, FIRST, LAST)})


# ---------------------------------------------------------------------------------------------------------------------------
# Entity lists: landed on 2026-11-02 in the tree, answered fresh for 2026-11-09 by the stub

def ext(serving, created="2026-03-02T17:00:00Z", updated="2026-10-01T17:00:00Z", details=()):
    return {"creationDateTime": created, "lastUpdateDateTime": max(created, updated), "servingStatus": serving, "servingStatusDetails": list(details)}


def sp_lists(now):
    fresh = now == "2026-11-09"
    camps = []
    for cid, (name, ttype, strat, pb, budget, start) in CAMPAIGNS.items():
        serving = "CAMPAIGN_STATUS_ENABLED"
        details = []
        if fresh and cid == "311000000000003":
            serving = "CAMPAIGN_OUT_OF_BUDGET"
            details = [{"name": "CAMPAIGN_OUT_OF_BUDGET", "message": "Campaign daily budget has been exceeded."}]
        camps.append({"campaignId": cid, "name": name, "campaignType": "SPONSORED_PRODUCTS", "targetingType": ttype, "state": "ENABLED",
                      "dynamicBidding": {"strategy": strat, "placementBidding": pb}, "startDate": start,
                      "budget": {"budgetType": "DAILY", "budget": budget, "effectiveBudget": budget},
                      "extendedData": ext(serving, created=CREATED.get(cid, f"{start}T17:00:00Z"),
                                          updated={"311000000000003": "2026-10-27T03:12:44Z", "311000000000004": "2026-10-22T16:40:09Z"}.get(cid, f"{start}T17:00:00Z"),
                                          details=details)})
    groups = [{"adGroupId": g, "campaignId": c, "name": n, "state": "ENABLED", "defaultBid": b,
               "extendedData": ext("AD_GROUP_STATUS_ENABLED", created=CREATED.get(c, f"{CAMPAIGNS[c][5]}T17:00:00Z"))} for g, (c, n, b) in AD_GROUPS.items()]
    ads = []
    for a, (g, asin) in ADS.items():
        serving = "AD_STATUS_LIVE"
        if fresh and asin == "B0FIXTURE1":
            serving = "AD_NOT_IN_BUYBOX"
        if fresh and asin == "B0FIXTURE2":
            serving = "AD_OUT_OF_STOCK"
        ads.append({"adId": a, "adGroupId": g, "campaignId": camp_of(g), "sku": SKU[asin], "asin": asin, "state": "ENABLED",
                    "extendedData": ext(serving, created=CREATED.get(camp_of(g), f"{CAMPAIGNS[camp_of(g)][5]}T17:00:00Z"))})
    keywords = [{"keywordId": k, "adGroupId": g, "campaignId": camp_of(g), "keywordText": t, "matchType": mt, "state": "ENABLED",
                 "bid": (bid if fresh else old), "extendedData": ext("TARGETING_CLAUSE_STATUS_LIVE", created=f"{CAMPAIGNS[camp_of(g)][5]}T17:00:00Z",
                                                                    updated={"341000000000041": "2026-10-19T18:05:31Z"}.get(k, "2026-06-15T17:00:00Z" if not fresh or k not in ("341000000000071", "341000000000072") else {"341000000000071": "2026-11-05T17:12:03Z", "341000000000072": "2026-11-05T17:12:05Z"}[k]))}
                for k, (g, t, mt, bid, old) in KEYWORDS.items()]
    targets = [{"targetId": t, "adGroupId": g, "campaignId": camp_of(g), "expressionType": "AUTO", "expression": [{"type": et}],
                "resolvedExpression": [{"type": et}], "state": "ENABLED", "bid": bid,
                "extendedData": ext("TARGETING_CLAUSE_STATUS_LIVE", created=CREATED.get(camp_of(g), f"{CAMPAIGNS[camp_of(g)][5]}T17:00:00Z"))}
               for t, (g, et, text, bid) in TARGETS.items()]
    negs = [{"keywordId": k, "adGroupId": g, "campaignId": camp_of(g), "keywordText": t, "matchType": mt, "state": "ENABLED",
             "extendedData": {"creationDateTime": c, "lastUpdateDateTime": c, "servingStatus": "TARGETING_CLAUSE_STATUS_LIVE"}} for k, (g, t, mt, c) in NEG_KEYWORDS.items()]
    cnegs = [{"keywordId": k, "campaignId": cid, "keywordText": t, "matchType": mt, "state": "ENABLED",
              "extendedData": {"creationDateTime": c, "lastUpdateDateTime": c, "servingStatus": "TARGETING_CLAUSE_STATUS_LIVE"}} for k, (cid, t, mt, c) in CAMPAIGN_NEG_KEYWORDS.items()]
    return {"sp-campaigns-list": {"campaigns": camps, "totalResults": len(camps)},
            "sp-adGroups-list": {"adGroups": groups, "totalResults": len(groups)},
            "sp-productAds-list": {"productAds": ads, "totalResults": len(ads)},
            "sp-keywords-list": {"keywords": keywords, "totalResults": len(keywords)},
            "sp-targets-list": {"targetingClauses": targets, "totalResults": len(targets)},
            "sp-negativeKeywords-list": {"negativeKeywords": negs, "totalResults": len(negs)},
            "sp-campaignNegativeKeywords-list": {"campaignNegativeKeywords": cnegs, "totalResults": len(cnegs)},
            "sp-negativeTargets-list": {"negativeTargetingClauses": [], "totalResults": 0},
            "sb-v4-campaigns-list": {"campaigns": [
                {"campaignId": "451000000000001", "name": SB["451000000000001"][0], "state": "ENABLED", "budget": 40.0, "budgetType": "DAILY",
                 "startDate": "2026-03-15", "brandEntityId": "ENTITYFIXTURE1", "goal": "PAGE_VISIT", "costType": "CPC", "bidding": {"bidOptimization": True},
                 "extendedData": {"servingStatus": "CAMPAIGN_STATUS_ENABLED", "creationDate": 1773594000000}},
                {"campaignId": "451000000000002", "name": SB["451000000000002"][0], "state": "ENABLED", "budget": 15.0, "budgetType": "DAILY",
                 "startDate": "2026-03-15", "brandEntityId": "ENTITYFIXTURE1", "goal": "PAGE_VISIT", "costType": "CPC", "bidding": {"bidOptimization": True},
                 "extendedData": {"servingStatus": "CAMPAIGN_STATUS_ENABLED", "creationDate": 1773594000000}}], "totalResults": 2},
            "sd-campaigns": [{"campaignId": 461000000000001, "name": SD["461000000000001"][0], "tactic": "T00030", "startDate": "20260401",
                              "state": "enabled", "costType": "vcpm", "budget": 20.0, "budgetType": "daily"}],
            "portfolios-list": {"portfolios": [{"portfolioId": "401000000000001", "name": "Hearthly Core", "state": "ENABLED", "inBudget": True,
                                                "budget": {"policy": "NO_CAP", "currencyCode": "USD"}}], "totalResults": 1}}


for key, body in sp_lists("2026-11-02").items():
    tree(f"raw/amazon-ads/{key}-{PROFILE}-2026-11-02.json", body)
for key, body in sp_lists("2026-11-09").items():
    stub(f"{key}-{PROFILE}-2026-11-09.json", body)
for key in ("sp-campaigns-list", "sb-v4-campaigns-list"):
    stub(f"{key}-{PROFILE_CA}-2026-11-09.json", {"campaigns": [], "totalResults": 0})
stub(f"sd-campaigns-{PROFILE_CA}-2026-11-09.json", [])

PROFILES = [
    {"profileId": int(PROFILE), "countryCode": "US", "currencyCode": "USD", "dailyBudget": 999999999.0, "timezone": "America/Los_Angeles",
     "accountInfo": {"marketplaceStringId": M, "id": SELLER, "type": "seller", "name": "Hearthly"}},
    {"profileId": int(PROFILE_CA), "countryCode": "CA", "currencyCode": "CAD", "dailyBudget": 999999999.0, "timezone": "America/Los_Angeles",
     "accountInfo": {"marketplaceStringId": "A2EUQ1WTGCTBG2", "id": SELLER, "type": "seller", "name": "Hearthly"}},
]
tree("raw/amazon-ads/v2-profiles-2026-11-02.json", PROFILES)
stub("v2-profiles-2026-11-09.json", PROFILES)
stub(f"accountBudgets-featureFlags-{PROFILE}-2026-11-09.json", {"featureFlags": {"isOptedOutForAverageDailyBudgetIncrease": False}})

# Budget usage now (stub only: it is today's), and the 7-day budget recommendation.
usage = []
for n, cid in enumerate(CAMPAIGNS):
    pct = {"311000000000003": 100.0, "311000000000001": 0.0, "311000000000002": 0.0}.get(cid, round(35 + 30 * u("use", cid), 1))
    usage.append({"campaignId": cid, "budget": CAMPAIGNS[cid][4], "budgetUsagePercent": pct,
                  "usageUpdatedTimestamp": "2026-11-09T21:47:12Z" if cid == "311000000000003" else "2026-11-09T22:40:03Z"})
stub(f"sp-campaigns-budget-usage-{PROFILE}-2026-11-09.json", {"success": usage, "error": []})
stub(f"sb-campaigns-budget-usage-{PROFILE}-2026-11-09.json", {"success": [
    {"campaignId": c, "budget": SB[c][1], "budgetUsagePercent": round(40 + 25 * u("sbuse", c), 1), "usageUpdatedTimestamp": "2026-11-09T22:40:03Z"} for c in SB], "error": []})
sp_recs = []
for cid in CAMPAIGNS:
    if cid == "311000000000003":
        sp_recs.append({"campaignId": cid, "suggestedBudget": 82.0,
                        "sevenDaysMissedOpportunities": {"startDate": "20261102", "endDate": "20261108", "percentTimeInBudget": 0.56,
                                                         "estimatedMissedImpressionsLower": 2900, "estimatedMissedImpressionsUpper": 4400,
                                                         "estimatedMissedClicksLower": 17, "estimatedMissedClicksUpper": 27,
                                                         "estimatedMissedSalesLower": 104.0, "estimatedMissedSalesUpper": 171.0},
                        "budgetRuleRecommendation": None})
    elif cid == "311000000000008":
        sp_recs.append({"campaignId": cid, "suggestedBudget": None, "sevenDaysMissedOpportunities": None, "budgetRuleRecommendation": None})
stub(f"sp-campaigns-budgetRecommendations-{PROFILE}-2026-11-09.json", {"budgetRecommendationsSuccessResults": sp_recs, "budgetRecommendationsErrorResults": []})
stub(f"sp-campaigns-budgetRules-recommendations-{PROFILE}-2026-11-09.json", {"recommendedBudgetRuleEvents": [
    {"eventId": "fixture-evt-black-friday-2026", "eventName": "Black Friday", "startDate": "2026-11-27", "endDate": "2026-11-27", "suggestedBudgetIncreasePercent": 40},
    {"eventId": "fixture-evt-cyber-monday-2026", "eventName": "Cyber Monday", "startDate": "2026-11-30", "endDate": "2026-11-30", "suggestedBudgetIncreasePercent": 35}]})

# Change history: SP and SB campaign-level and keyword events, UTC epoch ms. The tree holds the 2026-11-02 read.
EVENTS = [
    ("KEYWORD", KW15, "BID_AMOUNT", "0.9", "1.2", "2026-10-19T18:05:31Z",
     {"campaignId": "311000000000004", "adGroupId": "321000000000041", "keyword": "weighted blanket 15 lbs", "keywordType": "KEYWORD_EXACT"}),
    ("NEGATIVE_KEYWORD", "361000000000071", "STATUS", "CREATED", "ENABLED", "2026-10-20T17:30:12Z",
     {"campaignId": "311000000000007", "adGroupId": "321000000000071", "keyword": "heated blanket", "negativeTargetingType": "NEGATIVE_KEYWORD_PHRASE"}),
    ("CAMPAIGN", "311000000000004", "PLACEMENT_GROUP", "100", "200", "2026-10-22T16:40:09Z", {"campaignId": "311000000000004", "placementGroupPosition": "TOP_OF_SEARCH"}),
    ("CAMPAIGN", "311000000000003", "BUDGET_AMOUNT", "80.0", "50.0", "2026-10-27T03:12:44Z", {"campaignId": "311000000000003", "campaignBudgetType": "DAILY"}),
    ("CAMPAIGN", "311000000000008", "STATUS", "CREATED", "ENABLED", "2026-10-28T19:20:40Z", {"campaignId": "311000000000008", "campaignBudgetType": "DAILY"}),
    ("KEYWORD", "341000000000071", "BID_AMOUNT", "1.0", "0.8", "2026-11-05T17:12:03Z",
     {"campaignId": "311000000000007", "adGroupId": "321000000000071", "keyword": "throw blanket", "keywordType": "KEYWORD_BROAD"}),
    ("KEYWORD", "341000000000072", "BID_AMOUNT", "0.9", "0.72", "2026-11-05T17:12:05Z",
     {"campaignId": "311000000000007", "adGroupId": "321000000000072", "keyword": "warm blanket", "keywordType": "KEYWORD_BROAD"}),
]
for day in sorted(d for c, d in CAPPED if c == "311000000000003" and d <= D("2026-10-26")) + [D("2026-10-27") + dt.timedelta(n) for n in range(14)]:
    if day == D("2026-10-26"):
        out = dt.datetime(2026, 10, 27, 2, 51, 37)  # the day's $80 was spent before the 03:12:44Z cut to 50.0
    elif day < D("2026-10-26"):
        out = dt.datetime.combine(day + dt.timedelta(1), dt.time(6, 4 + int(20 * u("late", day))))
    elif day == D("2026-11-03"):
        out = dt.datetime.combine(day + dt.timedelta(1), dt.time(1, 55, 21))
    elif day == TODAY:
        out = dt.datetime(2026, 11, 9, 21, 47, 12)
    else:
        mins = int(19 * 60 + 210 * u("oob", day))
        out = dt.datetime.combine(day, dt.time(mins // 60, mins % 60, int(59 * u("s", day))))
    EVENTS.append(("CAMPAIGN", "311000000000003", "IN_BUDGET", "true", "false", out.strftime("%Y-%m-%dT%H:%M:%SZ"), {"campaignId": "311000000000003", "campaignBudgetType": "DAILY"}))
    if day < TODAY:
        back = dt.datetime.combine(day + dt.timedelta(1), dt.time(7 if day + dt.timedelta(1) <= D("2026-11-01") else 8, 0, 3))
        EVENTS.append(("CAMPAIGN", "311000000000003", "IN_BUDGET", "false", "true", back.strftime("%Y-%m-%dT%H:%M:%SZ"), {"campaignId": "311000000000003", "campaignBudgetType": "DAILY"}))


def history(until):
    ev = [{"entityType": e, "entityId": i, "changeType": c, "previousValue": p, "newValue": n, "timestamp": epoch_ms(t), "metadata": m}
          for e, i, c, p, n, t, m in EVENTS if t <= until]
    ev.sort(key=lambda x: -x["timestamp"])
    return {"events": ev, "totalResults": len(ev)}


tree(f"raw/amazon-ads/history-{PROFILE}-2026-11-02.json", history("2026-11-02T16:00:00Z"))
stub(f"history-{PROFILE}-2026-11-09.json", history("2026-11-09T23:59:59Z"))

# Launch reads (stub): product eligibility for every catalog ASIN, product metadata, and an initial budget recommendation.
elig = []
for asin, (sku, title, pr) in list(CATALOG.items()) + [("B0FIXTURE8", (None, "Hearthly Sherpa Fleece Blanket (variation parent)", None))]:
    status, reasons = "ELIGIBLE", []
    if asin == "B0FIXTURE1":
        status, reasons = "ELIGIBLE_WITH_WARNING", [{"name": "NOT_IN_BUYBOX", "message": "This product is not the featured offer and may not receive impressions.", "severity": "WARNING"}]
    if asin == "B0FIXTURE2":
        status, reasons = "ELIGIBLE_WITH_WARNING", [{"name": "OUT_OF_STOCK", "message": "This product is out of stock and may not receive impressions.", "severity": "WARNING"}]
    if asin == "B0FIXTURE8":
        status, reasons = "INELIGIBLE", [{"name": "VARIATION_PARENT", "message": "Variation parent products cannot be advertised. Advertise the child products.", "severity": "INELIGIBLE"}]
    pd = {"asin": asin} if sku is None else {"asin": asin, "sku": sku}
    elig.append({"productDetails": pd, "overallStatus": status, "eligibilityStatusList": reasons})
stub(f"eligibility-product-list-{PROFILE}-2026-11-09.json", {"productResponseList": elig})
meta = []
for asin, (sku, title, pr) in CATALOG.items():
    created = {"B0FIXTURE7": "2026-10-28T00:00:00Z", "B0FIXTURE9": "2026-10-30T00:00:00Z"}.get(asin, "2025-09-15T00:00:00Z")
    avail = "OUT_OF_STOCK" if asin == "B0FIXTURE2" else "IN_STOCK"
    meta.append({"asin": asin, "sku": sku, "title": title, "createdDate": created, "availability": avail,
                 "priceToPay": {"amount": price(asin, TODAY), "currency": "USD"}})
stub(f"product-metadata-{PROFILE}-2026-11-09.json", {"ProductMetadataList": meta})
stub(f"sp-campaigns-initialBudgetRecommendation-{PROFILE}-2026-11-09.json", {"dailyBudget": 18.0, "recommendationId": "fixture-ibr-20261109", "specialEvents": []})

# ---------------------------------------------------------------------------------------------------------------------------
# SP-API replies


def offers(asin, we_win, ours, other):
    a = {"SellerId": SELLER, "MyOffer": True, "IsBuyBoxWinner": we_win, "IsFulfilledByAmazon": True, "IsFeaturedMerchant": True,
         "ListingPrice": {"CurrencyCode": "USD", "Amount": ours}, "Shipping": {"CurrencyCode": "USD", "Amount": 0.0}, "SubCondition": "new"}
    b = {"SellerId": "A2OTHERSELLER9", "MyOffer": False, "IsBuyBoxWinner": not we_win, "IsFulfilledByAmazon": True, "IsFeaturedMerchant": True,
         "ListingPrice": {"CurrencyCode": "USD", "Amount": other}, "Shipping": {"CurrencyCode": "USD", "Amount": 0.0}, "SubCondition": "new"}
    return {"payload": {"ASIN": asin, "marketplaceId": M, "status": "Success", "ItemCondition": "New",
                        "Summary": {"TotalOfferCount": 2, "NumberOfOffers": [{"condition": "new", "fulfillmentChannel": "Amazon", "OfferCount": 2}],
                                    "BuyBoxPrices": [{"condition": "New", "LandedPrice": {"CurrencyCode": "USD", "Amount": ours if we_win else other},
                                                      "ListingPrice": {"CurrencyCode": "USD", "Amount": ours if we_win else other}}]},
                        "Offers": [a, b]}}


tree("raw/amazon-sp-api/getItemOffers-B0FIXTURE1-2026-11-02.json", offers("B0FIXTURE1", True, 29.99, 31.49))
stub("getItemOffers-B0FIXTURE1-2026-11-09.json", offers("B0FIXTURE1", False, 29.99, 26.99))
stub("getItemOffers-B0FIXTURE4-2026-11-09.json", offers("B0FIXTURE4", True, 59.99, 64.99))


def inventory(day, plush_inbound_receiving):
    out = []
    for asin, (sku, title, pr) in CATALOG.items():
        q = {"HL-PLUSH-GRY": 0, "HL-FLEECE-GRY": 140, "HL-SHERPA-Q": 310, "HL-WEIGHTED-15": 95, "HL-FLEECE-CRM": 420,
             "HL-KNIT-CRM": 88, "HL-WAFFLE-OAT": 260, "HL-SHERPA-K": 180}[sku]
        inb = 240 - plush_inbound_receiving if sku == "HL-PLUSH-GRY" else 0
        rec = plush_inbound_receiving if sku == "HL-PLUSH-GRY" else 0
        out.append({"asin": asin, "fnSku": "X00FIX" + asin[-1] * 4, "sellerSku": sku, "condition": "NewItem", "productName": title,
                    "lastUpdatedTime": ("2026-11-06T09:12:00Z" if sku == "HL-PLUSH-GRY" and not plush_inbound_receiving else f"{day}T08:00:00Z"), "totalQuantity": q + inb + rec,
                    "inventoryDetails": {"fulfillableQuantity": q, "inboundWorkingQuantity": 0, "inboundShippedQuantity": inb, "inboundReceivingQuantity": rec,
                                         "reservedQuantity": {"totalReservedQuantity": 0, "pendingCustomerOrderQuantity": 0, "pendingTransshipmentQuantity": 0, "fcProcessingQuantity": 0},
                                         "unfulfillableQuantity": {"totalUnfulfillableQuantity": 0}}})
    return {"payload": {"granularity": {"granularityType": "Marketplace", "granularityId": M}, "inventorySummaries": out}, "pagination": {}}


tree("raw/amazon-sp-api/getInventorySummaries-2026-11-07.json", inventory("2026-11-07", 0))
stub("getInventorySummaries-2026-11-09.json", inventory("2026-11-09", 60))


def fees(asin, pr, referral, fba, when):
    money = lambda x: {"CurrencyCode": "USD", "Amount": x}
    return {"payload": {"FeesEstimateResult": {
        "Status": "Success",
        "FeesEstimateIdentifier": {"MarketplaceId": M, "IdType": "ASIN", "SellerId": SELLER, "IdValue": asin, "IsAmazonFulfilled": True,
                                   "PriceToEstimateFees": {"ListingPrice": money(pr), "Shipping": money(0.0)}, "SellerInputIdentifier": f"fixture-{asin}-{when[:10]}"},
        "FeesEstimate": {"TimeOfFeesEstimation": when, "TotalFeesEstimate": money(round(referral + fba, 2)), "FeeDetailList": [
            {"FeeType": "ReferralFee", "FeeAmount": money(referral), "FeePromotion": money(0.0), "FinalFee": money(referral)},
            {"FeeType": "VariableClosingFee", "FeeAmount": money(0.0), "FinalFee": money(0.0)},
            {"FeeType": "PerItemFee", "FeeAmount": money(0.0), "FinalFee": money(0.0)},
            {"FeeType": "FBAFees", "FeeAmount": money(fba), "FinalFee": money(fba),
             "IncludedFeeDetailList": [{"FeeType": "FBAPerUnitFulfillmentFee", "FeeAmount": money(fba), "FinalFee": money(fba)}]}]},
        "Error": None}}}


tree("raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE5-2026-09-30.json", fees("B0FIXTURE5", 79.99, 12.00, 8.78, "2026-09-30T18:20:11Z"))
stub("getMyFeesEstimateForASIN-B0FIXTURE5-2026-11-09.json", fees("B0FIXTURE5", 79.99, 12.00, 9.10, "2026-11-09T16:02:11Z"))
tree("raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE6-2026-11-02.json", fees("B0FIXTURE6", 29.99, 4.50, 6.05, "2026-11-02T16:30:40Z"))
tree("raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE4-2026-11-02.json", fees("B0FIXTURE4", 59.99, 9.00, 8.40, "2026-11-02T16:30:52Z"))
tree("raw/amazon-sp-api/getMyFeesEstimateForASIN-B0FIXTURE3-2026-11-02.json", fees("B0FIXTURE3", 44.99, 6.75, 7.35, "2026-11-02T16:31:05Z"))

# Brand Analytics Top Search Terms, one week (Sunday to Saturday), as the SP-API report flow lands it.
tst = {"reportSpecification": {"reportType": "GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT", "reportOptions": {"reportPeriod": "WEEK"},
                               "dataStartTime": "2026-11-01", "dataEndTime": "2026-11-07", "marketplaceIds": [M]},
       "dataByDepartmentAndSearchTerm": []}
for term, rank, rows in (("hearthly", 48210, [("B0FIXTURE4", .3812, .4405), ("B0COMPET03", .1704, .1190), ("B0FIXTURE6", .1123, .1388)]),
                         ("hearthly blanket", 91544, [("B0FIXTURE4", .3302, .3810), ("B0FIXTURE1", .1450, .0910), ("B0COMPET03", .1211, .1022)]),
                         ("sherpa blanket queen", 6120, [("B0COMPET05", .1830, .2011), ("B0FIXTURE4", .1222, .1305), ("B0COMPET02", .0950, .0810)])):
    for n, (asin, cs, vs) in enumerate(rows, 1):
        title = CATALOG[asin][1] if asin in CATALOG else {"B0COMPET03": "Snugwell Fleece Throw Blanket", "B0COMPET05": "Driftmoor Sherpa Blanket Queen",
                                                          "B0COMPET02": "Pinecot Plush Blanket Queen"}[asin]
        tst["dataByDepartmentAndSearchTerm"].append({"departmentName": "Amazon.com", "searchTerm": term, "searchFrequencyRank": rank,
                                                     "clickedAsin": asin, "clickedItemName": title, "clickShareRank": n, "clickShare": cs, "conversionShare": vs})
d = f"reports/GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT/{M}_2026-11-01_2026-11-07_fixture0/1"
tree(f"{d}/report.json", tst)
tree(f"{d}/receipt.json", {"reportId": "92000", "processingStatus": "DONE", "createdTime": "2026-11-09T15:10:00+00:00", "document": "report.json",
                           "source": "createReport", "ask": {"reportType": "GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT", "marketplaceIds": [M],
                                                             "dataStartTime": "2026-11-01", "dataEndTime": "2026-11-07", "reportOptions": {"reportPeriod": "WEEK"}}})

# ---------------------------------------------------------------------------------------------------------------------------
# The seller's notes

tree("notes/catalog.md", """# Hearthly catalog (US)

| ASIN | SKU | Product | Price | Notes |
|---|---|---|---|---|
| B0FIXTURE1 | HL-FLEECE-GRY | Fleece Throw 50x60, Grey | 29.99 | |
| B0FIXTURE2 | HL-PLUSH-GRY | Plush Throw 50x60, Grey | 39.99 | 34.99 until 2026-10-29 |
| B0FIXTURE3 | HL-KNIT-CRM | Chunky Knit Throw, Cream | 44.99 | |
| B0FIXTURE4 | HL-SHERPA-Q | Sherpa Blanket Queen 90x90, Navy | 59.99 | child of B0FIXTURE8 |
| B0FIXTURE5 | HL-WEIGHTED-15 | Weighted Blanket 15 lb, 60x80 | 79.99 | |
| B0FIXTURE6 | HL-FLEECE-CRM | Fleece Throw 50x60, Cream | 29.99 | |
| B0FIXTURE7 | HL-WAFFLE-OAT | Waffle Knit Throw 50x60, Oatmeal | 39.99 | new, live 2026-10-28, no reviews yet |
| B0FIXTURE8 | — | Sherpa Blanket (variation parent: Queen, King) | — | parent |
| B0FIXTURE9 | HL-SHERPA-K | Sherpa Blanket King 108x90, Navy | 69.99 | new size, live 2026-10-30, no reviews yet, not advertised yet |

Brand Registry: Hearthly, registered trademark. Professional selling plan. All FBA.
""")
tree("notes/costs.csv", """sku,asin,unit_cost_usd,inbound_freight_per_unit_usd,note
HL-FLEECE-GRY,B0FIXTURE1,6.90,0.50,
HL-PLUSH-GRY,B0FIXTURE2,9.40,0.60,cost rose from 8.10 in October
HL-KNIT-CRM,B0FIXTURE3,12.80,0.90,
HL-SHERPA-Q,B0FIXTURE4,16.20,1.30,
HL-WEIGHTED-15,B0FIXTURE5,20.50,1.50,
HL-FLEECE-CRM,B0FIXTURE6,6.90,0.50,
HL-WAFFLE-OAT,B0FIXTURE7,11.20,0.80,
HL-SHERPA-K,B0FIXTURE9,19.60,1.50,
""")
tree("notes/targets.md", """# Ads targets the seller set

- Target ACOS for every campaign: 30%. Set in March 2026 "so ads stay profitable".
- Returns: about 6% of units on the weighted blanket and 3% on the throws, from Seller Central's returns, 2026 to date.
- Monthly ad budget the seller is comfortable with: about $9,000 across SP, SB and SD.
""")
def _acos(rows, cid, a, b):
    rs = [r for r in rows if r["campaignId"] == cid and a <= r["date"] <= b]
    return round(100 * sum(r["cost"] for r in rs) / max(0.01, sum(r["sales7d"] for r in rs)))


W_BAD = _acos(L["sp_1012"], "311000000000004", "2026-10-12", "2026-10-18")
B_OCT = _acos(L["sp_1012"], "311000000000007", "2026-10-22", "2026-11-04")
tree("notes/ads-changes.md", f"""# Ads changes (the seller's own log)

Who can change the ads: the owner's login; the agency login (Northfield Digital, since June 2026); a bid tool on trial
(BidPilot, connected 2026-10-20, disconnected 2026-10-31).

- **2026-10-19** — SP | Weighted | Exact: bid on "weighted blanket 15 lbs" exact 0.90 -> 1.20. Why: last week (10-12..10-18) the
  campaign's ACOS was {W_BAD}%, its worst week this quarter. Expected: ACOS back under 45% and more orders within two weeks.
  Judge on: campaign ACOS and orders from spCampaigns daily. Before 10-12..10-18; after 10-20..11-01.
- **2026-10-20** — SP | Throws | Broad, ad group Knit: added negative phrase "heated blanket". Why: heated-blanket searches click
  and never buy (we sell no heated blankets).
- **2026-10-29** — not an ads change: HL-PLUSH-GRY price 34.99 -> 39.99, because its cost went up.
- **2026-11-03** — Lightning Deal on HL-SHERPA-Q (see deals.md).
- **2026-11-05** — SP | Throws | Broad: every keyword bid -20% (throw blanket 1.00 -> 0.80; warm blanket 0.90 -> 0.72). Why: ACOS
  since 10-22 was about {B_OCT}%, above target; want it under 28%. Expected: ACOS down at least 5 points, orders no more than 15% lower.
  Windows: before 2026-10-22..2026-11-04; after 2026-11-06..2026-11-19; read on or after 2026-11-26 (7-day attribution).
  If it cannot be told: extend once by two weeks.
""")
tree("notes/deals.md", """# Deals and promotions

- **Lightning Deal, 2026-11-03**, HL-SHERPA-Q (B0FIXTURE4): 09:00-17:00 PST, deal price $44.99 (regular $59.99). Ran; sold through
  its deal quantity at about 16:40.
- **Black Friday Week Best Deal**, submitted 2026-10-14 and approved: HL-SHERPA-Q at $47.99 (regular $59.99). Dates:
  "Amazon's Black Friday Week" — Amazon has not announced them yet. Fee: $100 plus 1.5% of promotional sales, capped at $5,000.
- No coupons running.
""")
tree("notes/agency-launch-plan.md", """# Launch plan for the Sherpa King (B0FIXTURE9), from the agency, 2026-11-06

1. The first 30 days are the "honeymoon period": Amazon boosts every new listing's organic rank for 30 days, so we spend hard now.
2. Bid 3x Amazon's suggested bid on every keyword for the first two weeks.
3. Friends-and-family orders: 40 orders through a two-step URL (search "sherpa blanket king" then click our listing) to seed rank.
4. Exact-match campaigns only on our 20 best keywords from day one; no auto campaign ("auto wastes money").
5. Pause any keyword with 5 clicks and no order.
""")

if SUMMARY:
    def acos(rows, cid=None, start="0000", end="9999", sales="sales7d"):
        rs = [r for r in rows if (cid is None or r["campaignId"] == cid) and start <= r["date"] <= end]
        c, s = sum(r["cost"] for r in rs), sum(r[sales] for r in rs)
        k, o = sum(r["clicks"] for r in rs), sum(r.get("purchases7d", r.get("purchases", 0)) for r in rs)
        return {"cost": round(c, 2), "sales": round(s, 2), "acos": round(c / s, 4) if s else None, "clicks": k, "orders": o,
                "cpc": round(c / k, 3) if k else None, "cvr": round(o / k, 4) if k else None}

    now = sp_campaign_rows(TODAY, FIRST, LAST)
    out = {}
    out["R1_fleece_grey_by_day"] = {r["date"]: [r["impressions"], r["clicks"], r["cost"]] for r in L["sp_1012"] if r["campaignId"] == "311000000000001" and r["date"] >= "2026-10-31"}
    out["R2_auto_vintages"] = {"read_1102": {r["date"]: r["sales7d"] for r in L["sp_1026_r1102"] if r["campaignId"] == "311000000000005"},
                               "read_1109": {r["date"]: r["sales7d"] for r in L["sp_1012"] if r["campaignId"] == "311000000000005" and r["date"] >= "2026-10-26"},
                               "cost_by_day_1109": {r["date"]: r["cost"] for r in L["sp_1012"] if r["campaignId"] == "311000000000005" and r["date"] >= "2026-10-29"}}
    out["R3_plush"] = {"10-15..10-28": acos(L["sp_1012"], "311000000000002", "2026-10-15", "2026-10-28"),
                       "10-29..11-05": acos(L["sp_1012"], "311000000000002", "2026-10-29", "2026-11-05"),
                       "rows_after_11-05": [r["date"] for r in L["sp_1012"] if r["campaignId"] == "311000000000002" and r["date"] > "2026-11-05"]}
    out["B1_sherpa_cost_by_day"] = {r["date"]: [r["campaignBudgetAmount"], r["cost"]] for r in L["sp_1012"] if r["campaignId"] == "311000000000003" and r["date"] >= "2026-10-24"}
    out["B1_nov_spend_to_date"] = round(sum(r["cost"] for r in L["sp_1012"] if r["campaignId"] == "311000000000003" and r["date"] >= "2026-11-01"), 2)
    pl = [r for r in L["pl_1012"] if r["campaignId"] == "311000000000004" and r["date"] >= "2026-10-23"]
    out["B2_weighted_placements_10-23..11-08"] = {p: {"clicks": sum(r["clicks"] for r in pl if r["placementClassification"] == p),
                                                      "cpc": round(sum(r["cost"] for r in pl if r["placementClassification"] == p) / max(1, sum(r["clicks"] for r in pl if r["placementClassification"] == p)), 3),
                                                      "max_daily_cpc": max([r["costPerClick"] for r in pl if r["placementClassification"] == p] or [0])} for p in PLACEMENTS}
    out["B3_waffle_30d"] = acos(L["sp_1012"], "311000000000008")
    st = L["st_1012"]

    def terms(cid, start="0000"):
        agg = {}
        for r in st:
            if r["campaignId"] == cid and r["date"] >= start:
                a = agg.setdefault((r["adGroupName"], r["targeting"], r["searchTerm"]), {"clicks": 0, "cost": 0.0, "orders7d": 0, "sales7d": 0.0, "impressions": 0, "first": r["date"], "last": r["date"]})
                a["clicks"] += r["clicks"]; a["cost"] = round(a["cost"] + r["cost"], 2); a["orders7d"] += r["purchases7d"]
                a["sales7d"] = round(a["sales7d"] + r["sales7d"], 2); a["impressions"] += r["impressions"]; a["last"] = max(a["last"], r["date"])
        return {" / ".join(k): v for k, v in sorted(agg.items(), key=lambda kv: -kv[1]["clicks"])}

    out["S1_throws_auto_terms"] = terms("311000000000005")
    out["S2_broad_terms_heated"] = {k: v for k, v in terms("311000000000007").items() if "heated" in k}
    tg = [r for r in L["tg_1012"] if r["campaignId"] == "311000000000006"]
    out["S3_bedding"] = {"targeting_impressions": sum(r["impressions"] for r in tg),
                         "search_term_impressions": sum(r["impressions"] for r in st if r["campaignId"] == "311000000000006"),
                         "terms": terms("311000000000006"),
                         "by_ad": {r_ad: acos([r for r in L["ap_1012"] if r["adId"] == r_ad]) for r_ad in (A61, A62)}}
    out["T1_sherpa_exact_terms"] = {k: v for k, v in terms("311000000000003").items() if "sherpa blanket queen" in k.split(" / ")[1]}
    out["E2_sherpa_by_day"] = {r["date"]: {"cost": r["cost"], "clicks": r["clicks"], "orders7d": r["purchases7d"], "sales7d": r["sales7d"],
                                           "acos": round(r["cost"] / r["sales7d"], 3) if r["sales7d"] else None,
                                           "cvr": round(r["purchases7d"] / r["clicks"], 3) if r["clicks"] else None}
                               for r in L["sp_1012"] if r["campaignId"] == "311000000000003" and r["date"] >= "2026-10-27"}
    out["G1"] = {"break_even_now": round((79.99 - 22.00 - 12.00 - 9.10) / 79.99, 4), "break_even_sep_fees": round((79.99 - 22.00 - 12.00 - 8.78) / 79.99, 4),
                 "weighted_acos_10-12..11-08": acos(L["sp_1012"], "311000000000004")}
    sb = L["sb_1012"]
    out["G2_sb_ntb_10-12..11-08"] = {c: {"purchases": sum(r["purchases"] for r in sb if r["campaignId"] == c),
                                         "newToBrandPurchases": sum(r["newToBrandPurchases"] for r in sb if r["campaignId"] == c)} for c in SB}
    ap = [r for r in L["ap_1012"] if r["campaignId"] == "311000000000005"]
    cost, s7, same = sum(r["cost"] for r in ap), sum(r["sales7d"] for r in ap), sum(r["attributedSalesSameSku7d"] for r in ap)
    out["G3_throws_auto"] = {"cost": round(cost, 2), "sales7d": round(s7, 2), "sameSku7d": round(same, 2), "acos": round(cost / s7, 4),
                             "acos_same_sku": round(cost / same, 4), "other_share": round(1 - same / s7, 4),
                             "break_even_B0FIXTURE6": round((29.99 - 7.40 - 4.50 - 6.05) / 29.99, 4)}
    pp = [r for r in sp_purchased_rows(TODAY, D("2026-10-12"), D("2026-11-08")) if r["campaignId"] == "311000000000005"]
    out["G3_throws_auto"]["other_sku_by_purchasedAsin"] = {a: {"salesOtherSku7d": round(sum(r["salesOtherSku7d"] for r in pp if r["purchasedAsin"] == a), 2),
                                                               "unitsSoldOtherSku7d": sum(r["unitsSoldOtherSku7d"] for r in pp if r["purchasedAsin"] == a)}
                                                           for a in sorted(set(r["purchasedAsin"] for r in pp))}

    def weekly(rows, cid, weeks):
        return {f"{a}..{b}": acos(rows, cid, a, b) for a, b in weeks}

    wk = [("2026-09-28", "2026-10-04"), ("2026-10-05", "2026-10-11"), ("2026-10-12", "2026-10-18"), ("2026-10-20", "2026-11-01"), ("2026-11-02", "2026-11-08")]
    out["C1_weighted_weekly_landed"] = {**weekly(L["sp_0928"], "311000000000004", wk[:2]), **weekly(L["sp_1012"], "311000000000004", wk[2:])}
    out["C3_broad"] = {"before 10-22..11-04": acos(L["sp_1012"], "311000000000007", "2026-10-22", "2026-11-04"),
                       "after 11-05..11-08": acos(L["sp_1012"], "311000000000007", "2026-11-05", "2026-11-08")}
    print(json.dumps(out, indent=1))
else:
    print(T)
