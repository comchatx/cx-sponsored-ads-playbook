# Amazon's suggestions, its own changes and outside tools

## Suggested bids

- Suggested bids and ranges are calculated from bids of similar ads that won impressions over the past 7 days, offered as low, median and high and updated daily, so they exist for an ASIN with no history of its own. (B13)
- The console gives a separate suggestion for events in the next 45 days. (B13)
- The SP target bid recommendation returns up to three values per target by theme, and its v5 version adds impression estimates. (B13)
- A per-placement analysis is currently available only for existing ad group requests in the US. (B13)
- Performance Estimate figures and the old theme-based impact metrics are not a forecast and do not consider budget constraints. (B13)
- The v2 SP target bid recommendations and the v3 theme-based version of the SP target bid recommendation were announced for shutoff on 2025-05-15, though the SP v3 model read on 2026-11-09 still lists that v3 version. (B13)

## Recommendations

- Amazon's bid, budget and targeting recommendations are dated estimates refreshed about daily. (B36)
- Applying one is the same write to the named campaign, keyword or placement that any other change uses. (B36)
- The cross-product v1 Recommendations API (August 2026) serves the types its *Recommendation types* page lists (four on 2026-11-09); Amazon adds types over time, and its guide tells readers to tolerate `recommendationType` values they do not recognise. (B36)
- A v1 recommendation carries a `state` (`ACTIVE`, `APPLIED`, `DEFERRED`, `DISMISSED`, `EXPIRED`, `INACTIVE`) and `potentialImpacts`, "Estimated customer benefits if recommendation is followed". (B36)
- The three recommendation surfaces (product-specific recommendations, the recommendation list and apply operations, and the v1 recommendations query) have different shapes. (B36)

## Changes Amazon makes itself

- Amazon changes a seller's bids, budgets, targets and creative without a seller write, through its own switches on the campaign, portfolio or ad extension. (B35)
- For Alexa for Shopping, Alexa+ and prompts, it does so through automatic eligibility with no documented campaign switch. (B35)
- Auto targeting, keyword groups, SB theme targeting, SB cost-control rules and the v1 `autoCreateTargets` flag choose and refresh targets. (B35)
- Every US SP campaign is opted in to auto-assembled videos; the opt-out, `optOuts.videoExtension`, leaves videos already delivering running until paused through the ad extension. (B35)
- Campaigns were "automatically enrolled in prompts". (B35)
- SB headlines can be rewritten under DCO consent. (B35)
- Full-Funnel, DVA+ and Amazon's creative tools hand planning, targeting or creative to Amazon. (B35)

## Amazon Ads Agent and Seller Assistant

- From 2026-09-29, Amazon Ads Agent is the name of Amazon's unified ad platform holding sponsored ads, Display, Video and Audio and Full-Funnel Campaigns. (B37)
- Inside it, a closed-beta chat proposes keyword, bid and budget changes and applies them after the advertiser approves, with no public API. (B37)
- The help centre's "formerly known as Amazon DSP" is the same platform name written into DSP passages. (B37)
- Seller Central's Seller Assistant (Project Amelia in its 2024 beta, agentic from September 2025) checks whether each product's listing and inventory are ready to advertise, and drafts SP and SB campaigns the seller approves. (B38)
- Amazon describes an SP auto-optimization, switched on in campaign settings and dated to January 2027 in the US, that expands product targeting, adds relevant keywords and pauses underperforming ones, and holds every bid under a seller-set maximum, with actions the advertiser can edit or reverse at any time. (B38)
- No page states its thresholds or anything on source negatives, and on 2026-11-09 no Ads API release note or model field documents it or Seller Assistant. (B38)
- The change history API does not record who made a change. (B38)
- Seller Assistant workflows run "even when the seller isn't logged in", the seller choosing per workflow whether it surfaces recommendations or takes actions, which are reviewed and approved before they are carried out and logged in an audit trail. (B38)
- Amazon's examples of those workflows are pricing, restocking, listings and account health, not ads. (B38)

## Outside bid tools

- Third-party bid tools set each target's bid from its value per click times a target ACoS (Ad Badger and AdLabs: revenue per click, order value × conversion rate) on a daily or hourly schedule, and write it through the same Ads API endpoints. (B39)
- They state that they add negatives from wasted spend, cut bids and pause by hour, pause and revive targets and tie bids to organic rank, none of which Amazon's documented rules do. (B39)
- Auto-to-manual harvesting is offered both by these tools and by Amazon's target promotion groups. (B39)
- Helium 10, Intentwise, Ad Badger and Adbrew now sell MCP connections or Claude skills, alongside Amazon's own MCP server. (B39)
- Pacvue describes "approval-based execution with defined guardrails" and dayparting from Marketing Stream data and 14-day hourly patterns. (B39)
- Skai describes daily bid and budget optimizations, negatives and harvesting automated on user conditions, and outside agents' bid and budget changes each subject to human approval. (B39)

## Amazon's lift figures

- Amazon's published lift figures for its own automation are vendor-reported comparisons from beta or internal data, with no randomised holdout described. (B40)
- The Ads Agent figures are "Based on beta estimates", and Sponsored Brands DCO's "up to 1.6% CTR lift" is "Based on internal testing". (B40)
- Full-Funnel's "67% higher Long-Term ROAS" is "against the blended average of other campaign performance across beta advertisers", and the creative-tool gains are "versus their results before adopting the suite". (B40)
- The auto-optimization, ads data manager and prompt figures compare adopters or clickers with those who did not. (B40)
- Improvado's Ivo Petrovic reads the Full-Funnel figure as "not a holdout test on your account". (B40)
- In an auction, a gain measured on a few early adopters can overstate the gain once many use the same automation. (B40)
- Baidu's AiAds authors expected its advantage to "gradually abate", and Blake and Coey found naive estimates ignoring test-control interference "exaggerate the treatment's effectiveness by about a factor of 2". (B40)
