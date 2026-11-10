# Fees, returns, points and stock behind the margin

## Amazon's fees

- The margin before ads rests on Amazon's fees. (G4)
- The referral fee is a category-specific percentage of the total price or a minimum, whichever is greater; the fee category may differ from the one shoppers see, and media adds a closing fee. (G4)
- FBA charges fulfilment by price, weight and dimensions, monthly storage, aged inventory past 181 days, returns processing, removal, disposal, liquidation and inbound placement. (G4)
- The SP-API Product Fees API estimates fees per SKU or ASIN at a supplied price; Amazon states the estimates are not guaranteed. (G4)
- The FBA Fee Preview report holds per-SKU estimates updated at least every 72 hours. (G4)
- The Finances API's `listTransactions` returns the actual charges and may omit the last 48 hours. (G4)

## Fees move

- The 2026 US letter raised FBA fees by $0.08 a unit on average from 2026-01-15. (G5)
- The 2027 letter raises fulfilment by $0.19 a unit on average (about 0.8% of average selling price), mostly from 2027-01-15. (G5)
- From 2027-02-01 the 2027 letter drops the storage utilization surcharge and folds aged inventory into an age-based storage rate that Amazon says is flat or lower for inventory turning in under six months and higher for aged inventory. (G5)
- From 2027-02-01 the 2027 letter applies the low-inventory-level fee only below 28 days of supply. (G5)
- A 3.5% fuel and logistics surcharge on the fulfilment fee (about $0.17 per US FBA unit) applies from 2026-04-17 in the US and Canada, to Buy with Prime and MCF from 2026-05-02, and on top of peak fees. (G5)
- Holiday peak fees, about $0.32 a unit over non-peak, run 2026-10-15 to 2027-01-14. (G5)
- The Data Kiosk economics dataset itemises the fee types, shows a fee separately on each side of a change date and previews fees up to 120 days ahead. (G5)

## Fulfilment programs

- Multi-Channel Fulfillment fulfils orders placed on the seller's own website or other sales channels, not Amazon-store orders. (G6)
- Seller Fulfilled Prime commits the seller to fast free delivery and free returns for domestic Prime customers. (G6)

## Returns and net sales

- Attributed sales do not reflect cart discounts, and deduct payment failures and purchases cancelled within 72 hours, deductions taking up to 7 days; returns are not among the listed deductions. (G7)
- Data Kiosk's net product sales subtract refunds by refund request time, and its net proceeds subtract fees, ad charges and seller-entered unit costs. (G7)
- Per-ASIN returns sit in Data Kiosk's `returns` group, mapped to ship day and computed about 45 days late. (G7)
- FBA returns are in `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` and seller-fulfilled returns in the returns reports. (G7)
- Sales and Traffic carries refunds only by date, not by ASIN. (G7)
- Nova Analytics, FiveX and My Amazon Guy put a returns allowance into the margin before ads, and none of their pages computes ACoS or TACoS on revenue net of returns. (G7)

## Points on Amazon.co.jp

- On Amazon.co.jp points are granted at a rate set by Amazon or the seller, in Points Central up to 50% per listing. (G8)
- A default 1% has been auto-applied from November 1, 2021 to listings the seller had not set. (G8)
- One point is used as one yen, and the seller bears one yen per point. (G8)
- In Amazon's Product Pricing model, landed price is listing price plus shipping minus points, and an offer may be ineligible for the Buy Box when that exceeds the competitive price threshold. (G8)
- The Product Fees estimate accepts points, a program that exists only in Japan. (G8)

## Stock and capacity

- Amazon staff state that FBA capacity for established accounts rests on IPI score and sales, and that IPI runs 0–1,000. (G15)
- Amazon's inventory planning report gives per-SKU days of supply and excess. (G15)
