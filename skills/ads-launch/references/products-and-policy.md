# Ad products and policy

## Product eligibility

- Amazon's product eligibility read takes up to 50 products, only products sold by the profile's merchant, and returns per product and ad type an overall status: `ELIGIBLE`, `ELIGIBLE_WITH_WARNING` ("may not receive impressions") or `INELIGIBLE` ("cannot be included in an advertisement"). (P1)
- The overall status inherits the highest severity among the named reasons, such as `NOT_IN_BUYBOX`, `OUT_OF_STOCK`, `LISTING_SUPRESSED`, `MISSING_IMAGE`, `RESTRICTED_CATEGORY` and `VARIATION_PARENT`. (P1)
- The product metadata read returns availability, price, best seller rank and eligibility for up to 300 products. (P1)

## Program eligibility

- Amazon's program eligibility read returns per marketplace and program (`SB`, `SD`, `SPOT`, `DTC`, `MAAS`) whether the account may use it, with reasons covering standing, terms, brand relation, business verification, tax, billing and payment. (P2)
- Most advertisers are verified automatically; the others are verified through verification tasks. (P2)
- Sponsored Brands does not support adult, used or refurbished products and is limited to a listed set of categories. (P3)
- Streaming TV needs a professional seller with Brand Registry or a vendor account, is not available to Health and Personal Care advertisers and is offered through the API in the marketplaces, and at the stage, that Amazon's *Sponsored TV overview* gives (https://advertising.amazon.com/API/docs/en-us/guides/sponsored-tv/overview). (P3)

## What an ad shows

- A Sponsored Products ad includes the product's title, image and price, the list price when the offer is below it, and the Prime badge when the offer has Prime shipping. (P10)
- Amazon's responsive display creatives add live deal, coupon and Subscribe & Save badges and star ratings from the listing, showing the highest discount when several are active. (P10)

## Sponsored Products video

- SP video runs only in the marketplaces Amazon's *Understand Sponsored Products video* names (https://advertising.amazon.com/help/G45ASMDJY8XXQQFK), is not for Books, is billed per click from the campaign budget and is approved in 48–72 hours. (P4)
- It can be auto-assembled from existing detail-page or uploaded video, with no new video generated. (P4)
- Amazon's help page calls auto-assembly "an opt-in feature", while the API guide says "All campaigns are opted in to auto-assembled videos by default". (P4)

## Prompts

- Prompts are an AI-generated extension of SP and SB campaigns in the marketplaces Amazon's *Understand prompts on Sponsored Products and Sponsored Brands* names (https://advertising.amazon.com/help/GLWNW26EWQZW46WZ), built from detail-page, Brand Store and campaign data, auto-enrolled, billed per click from the campaign budget and pausable per prompt. (P11)
- A prompt can open a Rufus dialog, can show in shopping results and on product pages, and is not available to authors and publishers. (P11)
- Prompts have been generally available since 2026-03-25, a date Ad Badger agrees on. (P11)
- They are reported in the `spPromptAdExtension` and `sbPromptAdExtension` v3 report types, whose data delivery ends with v3 on 2027-06-30. (P11)

## Alexa for Shopping, Rufus and Alexa+

- In May 2026 (announced 2026-05-13) Amazon brought Rufus and Alexa+ together as Alexa for Shopping for US shoppers on the Amazon Shopping app, website and Echo Show, with Alexa+ continuing on Alexa-enabled devices; outside the US the assistant is Rufus. (P12)
- Existing sponsored ads campaigns are automatically eligible to serve in Alexa for Shopping without additional setup, and advertisers with sponsored ads campaigns are automatically enrolled in Alexa+ Conversational Ads. (P12)
- No Ads API release note, guide or contract names Alexa for Shopping, and no report field or placement value separates Alexa for Shopping or Alexa+ traffic, the v1 inventory type `ALEXA_DEVICES` aside. (P12)
- Amazon said in 2024 that reports would not carry Rufus metrics, and in 2025 that Alexa+ metrics would be consolidated in existing reporting. (P12)
- No page says which bid adjustments apply in Alexa for Shopping, and Branded Conversations has no API or date. (P12)

## Sponsored Services

- Sponsored Services, announced at unBoxed 2026, is a US campaign type for local and online service providers bought with Cost Per Outcome bidding, available only through the Amazon Ads Unified API from Q4 2026, with console access in 2027. (P14)

## Creators

- Creator Connections lets a brand offer creators a commission on net price for sales within 24 hours of a click. (P15)
- It needs a Brand Registry role and an Amazon Ads account advertising in, and based in, the countries Amazon's *Understand Amazon Creator Connections* lists (https://advertising.amazon.com/help/GPARAL6JVGFEJKG2). (P15)
- Its results are reported only in its own portal at campaign level, and its charges appear on the advertising invoice; in India the same name will cover SP creator content. (P15)
- An invite-only Sponsored Content Requests program inside Creator Connections is described by trade press only. (P17)
- SP creator placements are part of off-Amazon reach, with the CPC set from the maximum bid, expected performance and sales, and clicks drawing on the same campaign budget. (P16)
- Reporting splits creator content as "Off Amazon" and creator storefronts as "Other – On Amazon"; "Limit reach to Amazon" keeps ads on Amazon properties, creator storefronts included. (P16)
- A creator tag on the account deny list excludes that creator from all active SP and Display campaigns, and creators earn affiliate commission besides. (P16)
- PPC Land and Ad Badger report the start of creator placements as 2026-08-10 with campaigns enrolled by default, and Ad Badger notes creator clicks can lower on-Amazon impression share while spend holds. (P16)

## Ad content policy

- On Amazon O&O supply, ads may not use all capitals (outside the marketplace exception that Amazon's *Prohibited content and products for Amazon O&O supply*, https://advertising.amazon.com/help/GTEEH3E3J2BDELBA, names), scare tactics, unsubstantiated warranty claims, calls to action in custom images, deal teasers, social links, contact details or disparagement of competitors. (P6)
- On that supply, seasonal or holiday promotions start, in the policy's words, "no earlier than 8 weeks leading up to the event". (P6)
- Claims must be accurate and substantiated. (P6)
- Tobacco and nicotine, weapons (some knives excepted), THC or CBD, political ads, religious services, fundraising or proselytizing (religious books and merchandise excepted) and adult sexual products are prohibited across all supply. (P6)
- Consumer healthcare products are tiered by sensitivity; tiers 2 and 3 are prohibited on Fire TV, Fire tablet, Alexa and the store homepage and barred from audience building. (P6)
- Ad text must be in a language the marketplace's shoppers understand, and Amazon translates SB and display text automatically within 24 hours in the marketplaces Amazon's help page Sponsored ads translation lists (https://advertising.amazon.com/help/GJ67QHHYCKMEJGG9). (P7)
- Creative may not reference Amazon products or services or use Amazon branded elements. (P8)

## Moderation

- Moderation combines automated and human review, usually within 24 hours and up to 3 business days. (P9)
- Since February 2026 Amazon emails only rejections; an appeal goes through the rejection link, and repeat violations can lead to suspension. (P9)
- Pre-moderation checks one entity's components before submission. (P9)
- The moderation results read reports SP, SB and display moderation status (`APPROVED`, `IN_PROGRESS`, `REJECTED`, `FAILED`) with reasons and an expected time. (P9)
- The legacy SB moderation endpoint shut off on 2025-12-15, and the asset library runs no eligibility check on images. (P9)

## Billing

- Sponsored ads are billed at most once per click. (P13)
- Sellers pay by card, seller account funds or invoice, vendors by card, deduction from payments or invoice, and KDP authors by card or invoice; a payment failure pauses campaigns. (P13)
- Invoices come each time accumulated cost reaches the credit limit and at least monthly, on the second day of the next month. (P13)
- An invoice differs from campaign cost by invalid-traffic adjustments, over-delivery and promotional credits, taxes, regulatory advertising fees and charges carried across a month boundary. (P13)
- Some countries add a regulatory advertising fee; Amazon stopped charging the Canadian one after 2025-07-31 and began refunding it on 2026-04-15. (P13)
- Amazon's vendor payment methods are card (charged at each credit limit), deduction from retail proceeds by vendor code (which fails if that code's available funds are short) and monthly invoice due in 30 days. (P20)
- Vendor invoicing is invite-only; deduction from payments is not available to third parties managing payments or to accounts without retail activity in the last 6 months; a failed payment pauses campaigns. (P20)

## API terms

- The Amazon Advertising API License Agreement limits confidential information to the advertising participant it relates to and to use on behalf of the participant who authorised it, and forbids generating repetitive or invalid interactions. (P19)
- The Partner Network Policies forbid combining Amazon data with other third-party sources without Amazon's written approval and require deletion when it is no longer needed. (P19)
- The Ads API is offered only to companies that do not operate a significant e-commerce business, a demand-side ad platform or an ad network. (P19)
- For SP-API data Amazon requires incident notice within 24 hours, deletion within 30 days of the triggering event, and stored data kept separate or tagged by origin. (P19)
- The SP-API Acceptable Use Policy forbids aggregating data across authorised users' businesses to provide to others, and requires being explicit about calculations and the use of AI models, their accuracy and data freshness, with data integrity and validation checks on AI analysis that materially affects a business. (P19)
