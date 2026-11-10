# Vendor and hybrid economics

## A vendor's sales and receipts

- A vendor's attributed sales are retail sales, which Amazon states "don't reflect any discounts applied in the cart" and "don't include tax". (G33)
- Amazon defines the vendor's own receipts separately, as shipped COGS, "the price Amazon paid to a vendor for item procurement". (G33)
- A vendor's total-sales side is Vendor Retail Analytics, by `MANUFACTURING` or `SOURCING` view, reported in Pacific Standard Time whatever the marketplace. (G27)

## Vendor Sales report

- The Vendor Sales report requires `reportPeriod`, `distributorView` (`MANUFACTURING` or `SOURCING`) and `sellingProgram` (`RETAIL`, `BUSINESS` or `FRESH`). (G35)
- The manufacturing view covers ASINs the vendor manufactures, whoever sourced them to Amazon; the sourcing view covers ASINs sourced directly from the vendor group. (G35)
- `orderedRevenue` and `orderedUnits` are populated only in the manufacturing view, while shipped revenue, shipped COGS and shipped units are in both. (G35)
- Amazon's SLA is end of day Monday (48 hours) for a weekly period and 72 hours for a non-Saturday daily period. (G35)
- A report requested before its period is available ends with `processingStatus` `FATAL`. (G35)
- DAY data looks back 1,460 days with a 15-day maximum span. (G35)
- In the Data Kiosk vendor dataset, the view a vendor sees follows the role assigned to it, and the sourcing view is the distributor view and has no glance views. (G35)
- In that dataset a vendor group that manufactures nothing gets an error for the manufacturing view, and several manufacturing metrics cannot be grouped by `vendorCode`. (G35)

## Glance views and real-time reports

- Amazon counts vendor glance views only when Amazon retail is the featured merchant: Data Kiosk's `glanceViews` are "Glance views where Retail is the featured offer". (G36)
- Data Kiosk's `lostFeaturedOffer` is the share of glance views where the vendor's offer does not win the Featured Offer. (G36)
- The real-time traffic report's glance views differ from the Vendor Central dashboard's, are less accurate for concluded days and arrive about 65 to 115 minutes after the hour. (G36)
- The real-time sales report gives hourly ordered units and revenue five minutes after the hour, with cancellations shown at their own time as negative units. (G36)
- Amazon's tip computes conversion as ordered units over glance views. (G36)
- Reason Automation (Andrew Hamada, 2025) reports that Vendor Central renamed glance views to "featured offer page views", which in their account count only when a 1P offer is featured, appear only in the manufacturing view and come with no sessions for 1P vendors. (G36)

## Net PPM

- Amazon gives two current definitions of Net PPM, its own margin on a vendor's product. (G34)
- The Net PPM report schema's definition is "(Product Revenue – Product COGS – Vendor Funded Coop) / Product Revenue", a fraction from 0 to 1 measuring Amazon's profitability, in a vendor-only report that takes only `reportPeriod` and is in Pacific time. (G34)
- Data Kiosk's definition is "(Shipped Revenue - Shipped CCOGS + CCOGS - Sales Discount) / Shipped Revenue", where contra-COGS is "the dollars realized by customer outbound shipments minus Display Ads Contra COGS". (G34)
- MerchantSpring (Seiton) and SellerApp (Purohit) state that a vendor's advertising spend is not part of Net PPM. (G34)
- Seiton gives approximate Net PPM targets of about 40–45% for hardlines, 30–37% for softlines and 27–35% for consumables, which she says vary by sub-category and over time. (G34)

## Vendor TACoS

- No Amazon page read on 2026-11-09 defines TACoS for a vendor or names its total-sales denominator. (G37)
- m19 offers three vendor TACoS variants: spend over manufacturing ordered sales, over manufacturing shipped sales and over sourcing shipped sales, and says manufacturing metrics may include products sourced from distributors and wholesalers. (G37)
- Pare.so (George Reid, 2026) states that a hybrid brand's two TACoS denominators come from Vendor Central and Seller Central and that blending them without correction produces a meaningless metric. (G37)

## Brand Analytics for vendors

- Search Query Performance and Search Catalog Performance are available through the SP-API to sellers only. (G38)
- Repeat Purchase (18 stores), Market Basket and Search Terms are available to sellers and vendors with the Brand Analytics role and Brand Registry, Search Terms also requiring a brand representative. (G38)
- AMALYTIX (Trutz Fries, October 2026) reports that Vendor Central offers vendors Top Search Terms, Repeat Purchase Behavior and Market Basket Analysis, but not Search Query Performance or Search Catalog Performance, as checked in a vendor account in October 2026. (G38)

## Hybrid brands

- MerchantSpring (Rachel Seiton, "The Hybrid Playbook", 2026-08-13) advises two advertising strategies for a hybrid brand: 1P products on the upper funnel and broad category terms, and 3P on the lower funnel, retargeting, branded defence and conversion promotions. (G39)
- Seiton warns that a budget too small for both underperforms on both. (G39)
- Seiton states, citing ChannelEngine, that Amazon has terminated smaller vendor relationships in waves since late 2024, the latest with a termination date of 2 August 2026, which no Amazon page read states. (G39)

## Research on reseller and marketplace

- Hagiu and Wright (2015) model a platform's choice between marketplace and reseller as a choice of who holds control over a noncontractible marketing activity, spillovers across products shifting the choice toward reselling. (G40)
- Abhishek, Jerath and Zhang (2016) find in a stylised model that agency selling is more efficient than reselling and gives the manufacturer control of retail prices, reselling being preferred when the e-tailer gains from sales of associated products. (G40)
- Zhu and Liu (2018) find that Amazon is more likely to enter successful third-party product spaces and less likely where products need greater seller effort to grow, its entry discouraging affected sellers from pursuing growth on the platform. (G40)
- Farronato, Fradkin and MacKay (2023) find that Amazon-branded products rank higher than observably similar products in search, with a prominence 30–60% of that given to sponsored products. (G40)
- Bergen and John (1997) model co-op advertising and find that more generous manufacturer participation rates are called for with less targetable media, less differentiated retailers, more differentiated brands and more upscale products. (G41)
- Besanko, Dubé and Gupta (2005) measure a retailer's pass-through of wholesale price changes and find it varies widely across products and categories, averages above 60% own-brand in 9 of 11 categories, and includes cross-brand effects. (G41)
