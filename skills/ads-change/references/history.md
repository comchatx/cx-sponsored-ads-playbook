# Change history

## What it returns

Amazon's change history, `POST /history`, returns up to 90 days of Sponsored Products and Sponsored Brands campaign changes, each with its previous value, new value and Unix timestamp. (C1)
Its campaign change types include STATUS, IN_BUDGET, BUDGET_AMOUNT, END_DATE, SMART_BIDDING_STRATEGY and PLACEMENT_GROUP. (C1)
Amazon's model states "Changes for Sponsored Display campaigns are not returned", and that the history "doesn't return information about who made the change". (C1)

## An event

An event carries `entityType`, `entityId`, `changeType`, string `previousValue` and `newValue`, a UTC epoch `timestamp` and `metadata`. (C2)
`fromDate` reaches back as far as the model states: 90 days on 2026-11-09. (C2)
`THEME` events need `Accept: application/vnd.historyresponse.v1.1+json`; without it the call answers 400. (C2)
The history's bidding-strategy and placement enums differ from Sponsored Products 3.0's. (C2)
It has no event type for negative product targets, audience or shopper bid adjustments, ad creative or budget-rule associations. (C2)

## What no field records

No field in Amazon's change history, write replies or report rows records a change's reason, expected effect, judging metric or windows. (C6)
