---
name: ads-economics
description: "What a seller's sponsored ads earn: Amazon's ACOS, ROAS and break-even, Ads Math, the fees and returns behind the margin, attributed against ordered and total sales, TACOS, new-to-brand and long-term sales, what organic rank and published research show, and the vendor and hybrid side. For judging whether Sponsored Products, Sponsored Brands or Sponsored Display ads pay, and setting their targets."
---

## Break-even

- Amazon defines ACOS as ad spend over ad-attributed sales and ROAS as its inverse, and calls the profit margin break-even ACOS; break-even ROAS is 1 ÷ margin. (G1)
- Amazon states no general threshold makes an ACOS or ROAS good, and that new campaigns tend to run a high ACOS without failing. (G2)
- Ads Math's affordable CPA is LTV × profit margin; its per-sale calculator ignores repeat customers. (G3)

## Margin

- The margin before ads rests on Amazon's fees; Product Fees estimates are not guaranteed, and `listTransactions` returns actual charges. (G4)
- Attributed sales deduct purchases cancelled within 72 hours; returns are not among the listed deductions. (G7)

## Attributed against total

- Amazon dates an attributed purchase to the ad interaction in the campaign's time zone; Sales and Traffic dates ordered sales to the period. (G20)
- A seller's Sponsored Products attributed sales include other products the same merchant sells. (G20)
- A new-to-brand purchase is by a shopper with no purchase from the brand in the previous 12 months, judged on all shopping within the brand on Amazon, not only attributed purchases. (G10)
- Amazon's help says new-to-brand data "isn't available for Sponsored Products"; v1's *Purchases (new to brand)*, https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases-new-to-brand.md, lists it for new-to-brand purchases and sales. (G10)
- Long-term sales and ad-attributed Subscribe & Save cover Sponsored Brands and Display among others, not Sponsored Products. (G11, G12)
- No Ads API metric, report column or help page read defines TACOS. (G14)
- A total-account series alone does not separate the ads' effect from price, deals, stock or seasonality. (G26)
- In published field experiments, attributed or observational estimates of advertising returns exceeded the experimental ones. (G19)
- No Amazon source read states whether ad-attributed sales feed organic rank; no Amazon API read returns organic position. (G21, G28)

## Vendors

- A vendor's attributed sales are retail sales; its receipts are shipped COGS. (G33)

## References

- references/margin.md: ratios, Ads Math, goals, targets.
- references/fees.md: fee estimates, peak fees, returns, points, capacity.
- references/total-sales.md: other-SKU sales, new-to-brand, long-term sales, TACOS, organic rank, search counts.
- references/evidence.md: published experiments, Amazon's carry-over study.
- references/vendors.md: vendors, hybrid.
- ../ads-review/references/metrics.md: attribution windows by ad product, metric definitions.
