# Events and themes in the Ads API

## Events

`POST /sp/v1/events` returns individual and grouped special events with suggested date ranges in the advertiser's marketplace, each with an `eventId`. (E3)
Budget-rule event recommendations (`EVENTS_FOR_EXISTING_CAMPAIGN`) return, per campaign, the events Amazon recommends with a `suggestedBudgetIncreasePercent`. (E3)
Amazon chooses those events from the campaign's products, and they change when the products change. (E3)
Recommended events exist for Sponsored Products and Sponsored Brands only. (E3)
A budget rule tied to an unannounced event is created with empty dates, which Amazon fills in when the dates are announced. (E3)
Budget rules at large: ../ads-bids-and-budgets/references/budgets.md.

## Themes

Theme-based bid recommendations offer `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT` and `BFCM_HOLIDAY` beside `CONVERSION_OPPORTUNITIES`. (E4)
They are computed from recent winning bids for similar products, and their impact estimates assume the campaign does not run out of budget. (E4)
In Ads API v1, `Bid.theme` carries the same four values. (E4)
Keyword recommendations offer a `SPECIAL_DAYS` theme for high sales events such as Prime Day. (E4)
The v1 target model offers the theme targets `KEYWORDS_RELATED_TO_PRIME_DAY`, which matches queries only through the end of Prime Day, and `KEYWORDS_RELATED_TO_GIFTS`. (E4)
The SP 3.0, SB 3.0 and SB 4.0 specs read do not carry the Prime Day theme. (E4)

## Amazon Business

On Amazon Business the business-shopper bid adjustment goes up to 900%. (E19)
Amazon suggests a business-shopper adjustment of 20–120% for Prime Day and 20–50% for about two weeks around the holidays. (E19)
