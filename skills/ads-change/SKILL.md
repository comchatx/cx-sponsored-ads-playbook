---
name: ads-change
description: "What a change to a seller's sponsored ads leaves behind and how its effect can be read: Amazon's change history and its gaps, write replies and refusals, the tests Amazon offers and lacks, practitioners' and vendors' methods, and what research finds about before/after, bids, positions, holdouts and switchbacks. For changing sponsored ads or judging whether an ad change worked."
---

## Change history

- `POST /history` returns up to 90 days of change events for SP and SB campaigns, each with its `entityType`, old and new values and timestamp; not Sponsored Display's, nor who made them (C1, C2).
- It has no event for negative product targets, audience or shopper bid adjustments, ad creative or budget-rule associations (C2).
- No history, reply or report field records a change's reason, expected effect, judging metric or windows (C6).

## Writes

- Writes answer HTTP 207, each item's status in the body; v1's `partialSuccess` is written with some fields refused (C3).
- No v1, SP v3, SB v3, SB v4, SD v3 or Portfolios write takes an idempotency key; creates share no transaction; a chain stopped part-way shows `CAMPAIGN_INCOMPLETE` or `AD_GROUP_INCOMPLETE` (C3).
- A seller's campaign create reusing a campaign name is refused (C4).
- Some edits to entities Amazon created automatically are refused (C5).

## Testing

- No Amazon page or model read offers a randomized test for sponsored ads; Manage Your Experiments covers listing content only (C10).
- Amazon recommends limiting changes while testing bidding strategies, to attribute a difference to a specific change, and reviewing bids about once every two weeks (C9).
- Practitioners disagree on how long to wait after a bid change (C20).

## Before and after

- Across 25 large ad field experiments the median ROI confidence interval exceeded 100 percentage points (C13).
- Position differences won by bidding carry selection bias that randomizing one advertiser's bids cannot eliminate (C14).
- A report shows outcomes only at the bid that ran (C27).
- A campaign picked after an extreme period shows a change that is partly regression to the mean (C18).
- Ordinary p-values are unreliable when a test stops on watching its results (C16).
- `cx-listing-playbook`'s effect review returns held, not held or cannot tell (C19).

## References

- references/history.md: event fields, `fromDate`, `THEME`, missing event types.
- references/writes.md: 207 replies, idempotency, refusals, target types.
- references/tests.md: Amazon's advice, missing tests and own experiments, practitioners' waits, vendors.
- references/findings.md: organic, noise, positions, durability.
- references/designs.md: ratios, interference, switchbacks, CUPED, verdicts.
- ../ads-review/references/metrics.md: metric definitions.
- The amazon-ads skill's references/door.md: paths, headers, the token.
