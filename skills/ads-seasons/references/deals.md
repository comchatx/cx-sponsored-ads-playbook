# Deals, coupons and promotions

## Deal types

A Lightning Deal runs 4–12 hours, as Amazon determines, and a Best Deal several days. (E9)
Both need a Professional plan and can carry a Deals badge. (E9)
For deals, "Seller promotions" names a four-star seller rating and the Sell on Amazon guide an overall rating of at least four stars. (E9)
*Amazon deals* requires a sales history on Amazon, a product rating of at least four stars and a seller rating of at least 3.5, and makes deals invite-only. (E9)
Coupons need a 3.5-star rating, hold up to 200 ASINs, expire after 90 days and show a coupon badge with the discount in shopping results. (E9)
Price discounts run up to 30 days on limited units. (E9)
Amazon's Prime Day coupon criteria are a discount above 5%, dates coinciding with Prime Day and the audience set to Prime members. (E9)

## Deadlines and fees

Deal submission windows differ by marketplace and year, and deal fees by marketplace; for holiday 2026 Amazon stated them in News_Amazon's Seller Forums posts "Holiday 2026: Same fees, same eligibility, earlier deadlines" for the US (https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff) and "Peak season 2026: Inventory dates, peak fees, deal cutoffs and promotions" for the UK and EU (https://sellercentral.amazon.co.uk/seller-forums/discussions/t/d8c34b0b-86ed-4aec-9b0a-8be6eabb8fb0). (E10)
In those posts Best Deals, Lightning Deals and Prime Exclusive Price Discounts cost an upfront fee per promotion plus a capped share of promotional sales, and the UK and EU post discounts the upfront fee for early submission. (E10)
A promotion's own fee rates are in the Promotions API's fee snapshot. (E10, E14)
Prime Exclusive Discounts in the UK and EU need a 3.5-star rating. (E10)
PBDD 2026 promotional prices are excluded from the 30- and 60-day lookbacks that set the maximum BFCM deal price. (E11)
Amazon's Prime Day 2026 staff post for sellers, "Prime Day 2026: Your Deals Deadline Extended!" (https://sellercentral.amazon.com/seller-forums/discussions/t/9412e643-a006-464d-824a-0121d07c1b63), extended the Prime-Exclusive Best Deal and Lightning Deal deadline. (E26)
The same post required inventory in the network or in transit, and stated that deals are suppressed if ASINs are not buyable at event time. (E26)

## Reading promotions

The SP-API Promotions API (2025-12-01), for sellers, lists coupons, deals, price discounts and basket-building promotions with status, schedule (`startDate`, `endDate` and the event's `eventId`) and validation issues. (E14)
It also carries Prime-exclusive and brand-tailored customer segments, badge display, a stacking flag and a fee snapshot. (E14)
It is read-only, has no Brand Tailored Promotions type, and no operation read creates or reports Brand Tailored Promotions or Customer Engagement. (E14)

## Brand Tailored Promotions

Brand Tailored Promotions are for Brand Representatives in Brand Registry, in the stores sell.amazon.com's "What are Amazon Brand Tailored Promotions?" lists (https://sell.amazon.com/blog/brand-tailored-promotions). (E21)
They give 10–50% off to an audience of at least 1,000 shoppers chosen by goal (acquisition, re-engagement, retention, cross-sell), each eligible customer redeeming once. (E21)
One starts at least 48 hours after creation and within 60 days, and ends within 90 days of its start; a brand holds up to 20 at once. (E21)
Once one is live, only its budget can change, and only upward. (E21)
It shows a badge only to the audience and stacks with coupons, and its fees are stated only on a Seller Central help page. (E21)
Practitioners disagree on the best audience: Desert Cactus reports recent customers, Intentwise says many agencies favour cart abandoners, and none publishes a holdout test. (E21)

## Customer Engagement

The Customer Engagement tool sends free marketing emails, delivered by Amazon, to a Brand Registry brand's followers and, since 2022, its repeat, recent and high-spend customers. (E22)
It reports open rate, click-through, delivered emails, opt-outs, sales and conversion. (E22)
Amazon says brands with 1,000 or more followers "will have the best experience". (E22)
