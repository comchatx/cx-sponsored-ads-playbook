# Break-even, Ads Math and targets

## Amazon's ratios

- Amazon defines ACOS as ad spend over ad-attributed sales, times 100, and ROAS as its inverse. (G1)
- Amazon states that to keep a profit ACOS must sit below the profit margin, and calls that margin break-even ACOS. (G1)
- Amazon's Ads Math gives margin as (revenue − cost of goods) ÷ revenue and break-even ROAS as 1 ÷ that margin. (G1)
- Amazon states there is no general threshold for a good ACOS or ROAS. (G2)
- In Amazon's words a good ROAS is one profitable for the advertiser, read with margin, lifetime value and lift. (G2)
- Amazon states that new campaigns tend to run a high ACOS without failing. (G2)
- One Amazon FBA guide, *How to Help Increase Sales with FBA and Advertising*, still prints $2–4 per $1. (G2)

## Ads Math's click chain

- CPA = CPC ÷ conversion rate. (G3)
- Profit per sale = average order value × gross profit margin; net profit per sale = profit per sale − CPA. (G3)
- Amazon says this calculator is for one-off purchases and ignores repeat customers. (G3)
- Customer LTV = average order value × average orders. (G3)
- Affordable CPA = LTV × profit margin, which Amazon defines as the upper limit of ad spend per new customer to break even over the customer's lifetime. (G3)

## Goals in Amazon's guidance and API

- Amazon's Sponsored Products guidance names objectives to set before a campaign: brand exposure, new product, inventory clearance, peak season. (G9)
- In Ads API v1, `goalSettings` is not available for Sponsored Products, while a Sponsored Brands goal is read-only with a required KPI. (G9)
- The v1 model's `Goal`, `KPI` and `BidStrategy` enums name the options. (G9)

## Practitioners' targets from margin

- My Amazon Guy (Ken Zhou) computes a "true" break-even ACoS for setting campaign targets. (G16)
- EightX takes break-even TACoS as the pre-ad margin. (G16)
- Perpetua's Sponsored Products goal setup takes an initial target from 30 days' ACoS. (G16)
- Helium 10 describes ad spend that follows stock levels across marketplaces. (G16)
