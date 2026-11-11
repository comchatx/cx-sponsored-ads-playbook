# Seasons, events and deals

Read 2026-11-09 by the research seat.
Tags: [official] Amazon's own words (page name, URL, read 2026-11-09) · [opinion] a named practitioner, vendor, journalist or litigant · [research] published research · [law] a statute or a court's own release, quoted from the public text (not Amazon's words; added in the 2026-11-09 gap fill for the EU price-indication rule) · [seat] this seat's reading or inference.

## What this covers

This file covers how Amazon's retail calendar works on a seller's sponsored ads. It covers the tentpole events: Prime Day, Prime Big Deal Days (PBDD), the Big Spring Sale, Black Friday Week and Cyber Monday (BFCM), the holiday season, back to school, and regional events in Japan, India, Europe, Mexico and the Middle East. For each, it records:

- what Amazon says to do with budgets, bids and timelines;
- the console and API machinery that carries event dates (recommended events in budget rules, event-based bid rules, theme-based bid suggestions, the SPECIAL_DAYS keyword theme, special-event budgets in the initial budget recommendation);
- what is known about CPC and competition at peaks, including Amazon's own statements on reserve pricing and the allegations of the August 2026 FTC complaint;
- the ramp before an event and the tail after it (retargeting, halo, attribution lag);
- deals, coupons and Prime Exclusive Discounts (PEDs): their types, eligibility, fees, deadlines and reference-price rules, and how they surface inside ads (deal badges, Sponsored Brands deal call-to-action, the Brand Store Featured Deals widget, ad-policy rules on deal claims);
- seasonal search volume (Brand Analytics, Search Query Performance, Data Kiosk benchmarking) and how a year-over-year comparison lines up when an event moves week;
- 2025–2026 dates and what changed, including the UK and EU calendars, which run under different names and on different dates from the US (A12);
- the post-Christmas window practitioners call "Q5" and Amazon's "extend" phase (H5, practitioners §7);
- Brand Tailored Promotions and the Customer Engagement email tool, the seller-side remarketing levers that reach some of the same shoppers as Sponsored Display remarketing (F7, F8);
- the EU price-indication rule (the lowest price of the prior 30 days) and Amazon's reference-price pages per store, which bound what a deal badge and an ad's savings claim can say in the EU (F10);
- published research on promotion effects, pre- and post-promotion dips, how advertising and price promotion interact, and causal measurement around seasonal interventions.

It does not restate material owned by sibling files, and points to them instead:

- `areas/budgets-and-pacing.md`: daily budget mechanics, the monthly averaging rule and budget pacing in general.
- `areas/bids-and-placements.md`: bidding strategies and placement multipliers.
- `areas/campaign-structure.md`: campaign architecture.
- `areas/keyword-and-product-targeting.md`: targeting.
- `areas/search-terms-and-negatives.md`: search-term harvesting and negatives.
- `areas/launch.md`: new-product launch.
- `areas/ads-organic-and-total.md`: the organic halo and TACOS.
- `areas/diagnosis.md`: diagnosis of a performance drop.
- `beyond/ad-products-and-eligibility.md`: ad-product eligibility.
- `beyond/metrics-and-attribution.md`: attribution windows in depth.
- `beyond/goals-and-economics.md`: break-even ACOS and margin.
- `beyond/brand-defense-and-competition.md`: competitor conquesting.
- `beyond/automation-and-amazon-tools.md`: Amazon's automation in general.
- `method/ads-api-surface.md`: the API inventory.
- `method/reporting.md`: report mechanics.
- `method/change-measurement.md`: before/after measurement design.

This file holds only the event- and deal-specific slice of each.

## Amazon's own rules and guidance

Every item is marked **RULE** (a documented mechanism, limit or policy) or **GUIDANCE** (advice Amazon gives). The figures are those on the page on the date read. Items marked "for human readers only" are context that a skill should not hard-code.

### A. The event calendar, 2025–2026

A1. **RULE: Prime Day 2026 ran four days in June.** aboutamazon says: "Prime Day 2026 runs from June 23 at 12:01 a.m. PDT through June 26"; the Amazon Ads events page says: "Amazon's 2026 Prime Day event will start June 23 at 12:01 a.m. PDT and run through June 26." "When is Amazon Prime Day" adds that it ends "on Friday, June 26 at 11:59 p.m. Pacific Time". The countries were Austria, Belgium, Canada, Colombia, Egypt, France, Germany, Italy, Ireland, Luxembourg, Mexico, the Netherlands, Poland, Portugal, Saudi Arabia, Singapore, South Africa, Spain, Sweden, Turkey, the UAE, the UK and the US. "Prime members in Australia, Brazil, India, and Japan will be able to shop Prime Day deals later this summer." (The Ads events page's list omits South Africa.) Amazon also states "More than 200 million paid Prime members in 25 countries". The shopper tools named include "Price history... up to 365 days of pricing insights", deal alerts, and auto-buy through Alexa for Shopping. [official] aboutamazon, "Prime Day 2026 date", https://www.aboutamazon.com/news/retail/amazon-prime-day-2026-date, and "When is Amazon Prime Day", https://www.aboutamazon.com/news/retail/when-is-amazon-prime-day; Amazon Ads, "Prime Day" events page, https://advertising.amazon.com/events/prime-day; all read 2026-11-09.

A2. **RULE: Prime Day's history moves the event across weeks and lengths.** [official] aboutamazon, "The history of Prime Day", https://www.aboutamazon.com/news/retail/the-history-of-prime-day, read 2026-11-09.

| Year | Dates | Notes |
|---|---|---|
| 2019 | July 15–16 | The first 48-hour event |
| 2020 | October 13–14 | India in August |
| 2021 | June 21–22 | |
| 2022 | July 12–13 | |
| 2023 | July 11–12 | |
| 2024 | July 16–17 | |
| 2025 | July 8–11 | Over 25 countries; the first four-day event |
| 2026 | June 23–26 | Four days, per A1 |

On 2025, Amazon wrote: "At 96 hours, this will be double the duration", and introduced "Today's Big Deals" ([official] "What makes Prime Day 2025 different", https://www.aboutamazon.com/news/retail/what-makes-prime-day-2025-different, read 2026-11-09). Its recap called 2025 the "biggest Prime Day event ever", with record sales for independent sellers ([official] "Prime Day 2025 recap", https://www.aboutamazon.com/news/retail/prime-day-2025-recap, read 2026-11-09). The point that matters at run time: the start date has ranged from June 21 to October 13, it moved by two weeks or more between consecutive years in 2020, 2021, 2022 and 2026, and in 2025 it changed length.

A3. **RULE: Prime Big Deal Days 2026 ran October 6–7, for 48 hours.** "It started at 12:01 a.m. PDT on Tuesday, October 6 (3:01 a.m. EDT) and ends at 11:59 p.m. PDT on Wednesday, October 7". "Today's Big Deals drop at midnight, 8 a.m., and 1 p.m. PDT". It covered more than 35 categories, was Prime-only, and had early deals before the event. The same page notes that "Prime Day typically runs over four days in summer." [official] aboutamazon, "Prime Big Deal Days FAQ", https://www.aboutamazon.com/news/retail/amazon-prime-big-deal-days-faq, and "Prime Big Deal Days 2026: October 6–7", https://www.aboutamazon.com/news/retail/amazon-prime-big-deals-day-2026-when-october-6-7, read 2026-11-09.

A4. **RULE: The Big Spring Sale 2026 ran March 25–31.** Seven days, from 12:01 a.m. PDT to 11:59 p.m. PDT, with daily themed deal drops. [official] aboutamazon, "Big Spring Sale FAQ", https://www.aboutamazon.com/news/retail/amazon-big-spring-sale-faq, read 2026-11-09.

A5. **RULE: Black Friday 2026 is November 27 and Cyber Monday 2026 is November 30.** As of 2026-11-09, Amazon's US page gave no Black Friday Week start or end date. It said: "Black Friday 2026 falls on November 27" and "Customers can start browsing early deals in the Holiday Shop now and use Alexa for Shopping to track prices and set deal alerts. Check back soon for more information". The old 2025 URLs now redirect to the 2026 content. [official] aboutamazon, "When is Black Friday 2026? Here's everything you need to know", https://www.aboutamazon.com/news/retail/when-is-amazon-black-friday-faq (.../when-is-black-friday-2025 redirects there), and .../when-is-cyber-monday-2025, which redirects to .../when-is-amazon-cyber-monday-faq ("Cyber Monday 2026 falls on November 30"); read 2026-11-09. A web search on 2026-11-09 found no Amazon announcement of the US Black Friday Week 2026 window; in 2025 Yahoo Shopping dated Amazon's announcement to Nov. 9 (A6).

A6. **For human readers only: the 2025 Black Friday Week ran November 20 to December 1, 2025, and Amazon published no recap.** The dates come from press reports of Amazon's announcement: Yahoo Shopping wrote that "Amazon's Black Friday sale will begin on Thursday, Nov. 20 and run through Monday, Dec. 1" ([opinion] Yahoo Shopping, "Amazon just dropped all the details about its Black Friday sale", https://shopping.yahoo.com/deals/articles/amazon-just-dropped-details-black-160508522.html, read 2026-11-09). Modern Retail reported that Amazon published no post-BFCM recap in 2025 and no post-PBDD recap in October 2025, "the first time it has skipped such an announcement since at least 2016" ([opinion] Modern Retail, "Marketplace Briefing: Amazon skips its Black Friday and Cyber Monday recap...", https://www.modernretail.co/marketing/marketplace-briefing-amazon-skips-its-black-friday-and-cyber-monday-recap-for-the-first-time-since-2016/, read 2026-11-09). The consequence for a skill: Amazon-wide event results for BFCM 2025 and PBDD 2025 exist only from third parties.

A7. **RULE: Japan's 2026 events.** Amazon Japan says Amazon Black Friday will be held in November 2026, and that the dates will be announced on the morning of Thursday, November 19 ("開催期間...の詳細は、11月19日（木）の午前中に...お知らせします"). The page's related-news links list 新生活セール (the new-life sale) on Mar 6–9, 2026 (four days), 初売り (the New Year sale) from Jan 3, 2026 (five days), and an "Amazon プライムデー ステージ", a four-day venue event at Roppongi Hills from July 2 (not a sale). [official] aboutamazon.jp, "Amazon ブラックフライデー 2026", https://www.aboutamazon.jp/news/retail/amazon-black-friday-2026, read 2026-11-09.

The press reported Japan's Prime Day 2026 as a 先行セール (early sale) on Jul 7–9 and the main event on Jul 10 (Fri)–13 (Mon), four days, with more than 3 million items ([opinion] Impress Watch, https://www.watch.impress.co.jp/docs/news/2123919.html, July 10, 2026, read 2026-11-09). Japan's Prime Day therefore ran about two and a half weeks after the 22-country event.

A8. **RULE: India's Great Indian Festival.**

- 2026: the festival "continues through November 10", spanning Navratri, Dussehra, Dhanteras, Diwali and Bhai Dooj. Its deal formats include Blockbuster Deals, Top 100 and 8 PM Deals ([official] aboutamazon.in, "Amazon Great Indian Festival", https://www.aboutamazon.in/amazon-great-indian-festival, and ".../amazon-great-indian-festival-2026-dates", read 2026-11-09).
- 2025: the festival started Sep 23 with 24-hour Prime early access and ended Oct 20 (from the hub page's older cards, "Amazon Great Indian Festival 2025 starts on September 23rd" and "...2025 ends 20 October").
- Seller results, first week of 2026: "Overall seller sales grew up to 3.5x compared to business-as-usual (BAU) during the first week". Seller participation rose nearly 30%, and referral fees were zero below ₹1,000 ([official] aboutamazon.in, "Seller growth during Great Indian Festival 2026", https://www.aboutamazon.in/news/small-business/amazon-seller-growth-great-indian-festival-2026, read 2026-11-09).

India's main event therefore runs for weeks, not days, and its dates follow the lunar festival calendar.

A9. **GUIDANCE (calendar, for human readers only): Amazon Ads' global retail calendar.** The 2025 calendar lists, by country:

- Japan: Hatsuuri (Jan 1–3), White Day (Mar 14), the new fiscal year (Mar–Apr), Golden Week (Apr 29–May 6), Obon (Aug 13–16), Silver Week (September) and BFCM (Nov 28–Dec 1).
- India: Diwali (listed as Oct 23) and back to school in June.
- Mexico: Hot Sale (May 26–Jun 3) and El Buen Fin (Nov 14–17).
- Türkiye: Smiling Friday.
- Cross-market: Singles' Day (11.11), Boxing Day, and Ramadan (Feb 28–Mar 29, 2025).

[official] Amazon Ads, "2025 retail holiday calendar", https://advertising.amazon.com/library/guides/global-shopping-events, read 2026-11-09. The page's year is 2025; the 2026 dates of the lunar and movable holidays differ.

A10. **GUIDANCE: The holiday season and back to school.**

- Holiday: "October is the unofficial start of the holiday season" ([official] Amazon Ads, "Holidays" events page, https://advertising.amazon.com/events/holidays, read 2026-11-09). The 2026 holiday guide splits the season into "build (October), peak (November through Cyber Monday), and extend (December and beyond)" ([official] "Holiday advertising guide", https://advertising.amazon.com/library/guides/holiday-advertising-guide, read 2026-11-09).
- Back to school runs August–September and is the "second largest shopping season of the year". Amazon cites NRF: 56% of US households start shopping by July ([official] "Back-to-school marketing", https://advertising.amazon.com/library/guides/back-to-school-marketing, read 2026-11-09).
- The guides for Halloween, Mother's Day, New Year and Lunar New Year were read (their page titles carry 2024, except Mother's Day, which is undated). They carry generic timing advice and no ad mechanics beyond what is recorded here ([official] the Amazon Ads library guides named in Pages read).

A11. **RULE: Prime Day for Amazon Business (B2B).** "This June, Prime Day comes to Amazon Business in the United States, Canada, Mexico, the United Kingdom, Germany, France, Italy, and Spain." Business customers order 70% more units per order. B2B dates of note: the Business Gift Guide runs October to December, and the Business Savings Event runs late December to January. [official] Amazon Ads, "Prime Day 2026: Advanced advertising strategies", https://advertising.amazon.com/library/guides/prime-day-guide-advanced-strategies, and "Holiday advertising guide", read 2026-11-09.

A12. **RULE: The UK and EU calendar runs under its own names, local times and dates (gap fill 2026-11-09).**

| Event | UK / EU 2025–2026 | US for comparison | Source |
|---|---|---|---|
| Spring event 2026 | "Amazon Spring Deal Days" (UK), "Frühlingsangebote" (DE): March 10–16, 2026, "running from 00:01 on 10 March until 23:59 on 16 March" (UK); "Vom 10. März (0:00 Uhr) bis zum 16. März (23:59 Uhr)" (DE), in Austria, Belgium, Germany, Spain, France, Ireland, Italy, the Netherlands, Poland, Portugal, Sweden, Turkey and the UK | Big Spring Sale, March 25–31, 2026 (A4) | [official] About Amazon UK, "Amazon Spring Deal Days returns with seven days of savings" (London, 3 March 2026); Amazon Press Center DE, "Kräftig sparen zum Saisonstart: Amazons Frühlingsangebote kehren am 10. März zurück" |
| Prime Day 2026 | June 23–26; UK "The event runs until Friday 26 June"; DE "vom 23. Juni um 00:01 Uhr bis zum 26. Juni um 23:59" | June 23–26 from 12:01 a.m. PDT (A1) | [official] About Amazon UK, "Amazon launches Prime Day with surprise deliveries, daily Epic Prime Deals, and four days of savings for members"; Amazon Press Center DE, "Der Countdown läuft: Prime Day bietet Hunderttausende Angebote vom 23. bis 26. Juni" |
| October event 2026 | "Prime Big Deal Days" (UK, EU) and "Prime Deal Days" (DE): October 6–7. UK: "from Tuesday, 6 October at 12:01 BST until Wednesday, 7 October at 23:59 p.m. BST". EU page: "Starting October 6 at 12:01 a.m. CET". DE: "Ab 6. Oktober um 00:01 Uhr ... 48 Stunden lang". 22 countries; the DE release adds "Die Termine können je nach Land variieren" (dates may vary by country) | October 6–7 from 12:01 a.m. PDT (A3) | [official] About Amazon UK, "Amazon Prime Big Deal Days 2026: Deal event returns to the UK from 6 to 7 October" and "Prime Big Deal Days: Save big on autumn and Christmas shopping from October 6-7th"; About Amazon EU, "Prime Big Deal Days is back October 6-7"; About Amazon Deutschland, "Was sind die Amazon Prime Deal Days?"; Amazon Press Center DE, "Die Prime Deal Days kehren am 6. und 7. Oktober zurück..." |
| Black Friday Week 2025 | November 20 to December 1, 2025, 12 days, in the UK ("LONDON UK, 09:00 GMT 13 November 2025 - Amazon today announced the dates for its Black Friday Week in the UK, kicking off 20 November and running until 1 December") and DE ("Ab Donnerstag, den 20. November 2025 um 00:01 Uhr bis zum 1. Dezember 2025 um 23:59 Uhr"), announced on November 13, 2025 | November 20 to December 1, 2025 (A6, from press) | [official] Amazon Press Center UK, "It's the Season for Savings: Amazon's Black Friday Week Offers Deep Discounts on Customer-Favourite Brands from 20 November until 1 December"; Amazon Press Center DE, "Der Countdown läuft: Die Black Friday Woche kehrt vom 20. November bis zum 1. Dezember zurück" |
| Black Friday Week 2026 | Not announced on About Amazon UK, About Amazon Deutschland or the DE press archive as of 2026-11-09; the UK seller post sets the BFW deal cutoff at November 18 (F9) | Not announced (A5) | as read 2026-11-09 |

All read 2026-11-09. Three points follow from the table. The spring event is a different event in Europe: two weeks earlier than the US sale, under another name. The EU and UK events start at local midnight (BST, CET, "00:01 Uhr"), not at 12:01 a.m. PDT, so a same-named event begins about 8–9 hours earlier in Europe than in the US [seat, from the stated time zones]. And the German October event is named "Prime Deal Days", which matters to any matching by event name (for example `schedule.eventId` in the Promotions API, F6) [seat]. The DE Prime Deal Days release also says "Viele Produkte sind dabei stark reduziert oder zum niedrigsten Preis der vergangenen zwölf Monate erhältlich" (many products at the lowest price of the past twelve months); this is a retail claim in Amazon's release, and F10 has the 30-day rule a deal's reduction is measured against.

### B. Amazon's event-prep guidance for ads: timelines, budgets, bids

B1. **GUIDANCE: Timeline before the holiday peak.**

- Sponsored Products: "Launch campaigns by early October to test your keywords and bids"; then "Monitor... every one to two weeks".
- Budgets: "Increase daily budgets by 20 to 30 percent around Black Friday and Cyber Monday and start scaling three to five days ahead of each peak event."
- Budget rules automate this, "automatically increasing your budget by the amounts you set during specific timeframes".

[official] "Holiday advertising guide", https://advertising.amazon.com/library/guides/holiday-advertising-guide, read 2026-11-09.

B2. **GUIDANCE: Prime Day guidance for Sponsored Products.** "Launch Sponsored Products campaigns for your high-performing items and products with deals. Review performance in real time and optimize bids during peak hours." Amazon also advises to "Compare activity before, during, and after Prime Day". The guide points to long-term sales metrics (purchases plus "projected revenue from new customer engagement over the next 12 months"), new-to-brand metrics, and "Keyword Groups for Sponsored Brands and display ads", and advises cost controls in both Sponsored Brands and display. Its figure is narrower: "Advertisers that utilized cost controls in their display ads campaigns saw, on average, a 2.6X uplift in ad-attributed sales per campaign" (worldwide, Jan–Mar 2025; for human readers only). Sponsored Products video is US only. [official] "Prime Day 2026: Advanced advertising strategies", https://advertising.amazon.com/library/guides/prime-day-guide-advanced-strategies, read 2026-11-09.

B3. **GUIDANCE: Amazon's seller-side Prime Day tips.**

- "During peak shopping events like Prime Day, your ads may receive more clicks than normal, which means you may run out of budget quicker than expected. When that happens, your ads pause until midnight the next day. One way to prevent this and keep your campaigns active is to increase your budget, and budget rules makes it easy to do in advance."
- "Schedule-based rules allow you to change budgets on your campaigns prior to special events like Prime Day, or based on a custom period. The rule will increase the campaign budget by the percentage you specify, either during the date range you set in the rule or during the special event selected."
- "When adjusting your ad campaigns for Prime Day, stay competitive by setting your bids to the maximum amount you're willing to pay for a click. You can lower your bids again anytime you choose."
- Dynamic bidding "increases your bids in real time for impressions that may convert to a sale" and "reduces your bids for impressions that are less likely to convert".
- Brand Store: create a Prime Day version and "submit it for approval at least a week before Prime Day"; "giving yourself at least one week for the moderation of your content".

[official] sell.amazon.com, "Prime Day tips" (May 19, 2026), https://sell.amazon.com/blog/prime-day-tips, read 2026-11-09.

The "pause until midnight" sentence is the stated consequence of running out of budget. The monthly averaging rule that sits under it belongs to `areas/budgets-and-pacing.md`.

B4. **RULE: Daily budget overspend on any one day.** Amazon may "spend up to 100% more than the average daily budget on any given day... averaged over the course of a month". [official] Amazon Ads, "Sponsored ads daily budgeting policy and options" (May 9, 2023), https://advertising.amazon.com/resources/whats-new/sponsored-ads-daily-budgeting-policy-and-options, read 2026-11-09. The full mechanics are in `areas/budgets-and-pacing.md`. What matters here is that on an event day a campaign can spend up to twice its daily budget before any budget rule raises it.

B5. **GUIDANCE: Amazon Business bid adjustment.** The Amazon Business bid adjustment is "adjustable up to 900%"; "Start with 20%–120%". Amazon also describes B2B-exclusive campaigns, and phasing the B2B budget across pre-event, during, and "2 weeks after Prime Day". For the holidays: "Start small with a 20-50% increase, run for about two weeks". [official] "Prime Day 2026: Advanced advertising strategies" and "Holiday advertising guide", read 2026-11-09. The 900% is a limit; the 20%–120% and 20–50% figures are Amazon's suggestions, not rules.

B6. **GUIDANCE: Lead times for creative and stores.** These belong at the front of any event timeline:

- "Creative processing turnaround time for IAB standard ads is 3 business days" ([official] Amazon Ads, "General policies", https://advertising.amazon.com/resources/ad-policy/general-policies, read 2026-11-09).
- A Store version must be submitted at least 48 hours before its start, and sales-event content may start no more than 7 days before the event ([official] "Black Friday and Cyber Monday advertising tips", https://advertising.amazon.com/library/guides/black-friday-and-cyber-monday-advertising-tips, read 2026-11-09).
- sell.amazon.com advises "at least a week" (B3).
- Production timelines for Amazon-built creative are listed on the production-timelines page ([official] https://advertising.amazon.com/resources/ad-policy/production-timelines, read 2026-11-09).

B7. **GUIDANCE: The FBA holiday timeline.**

| Weeks before | Step |
|---|---|
| 10–12 | Pick products |
| 7–9 | Stock and ship |
| 4–6 | Optimize listings |
| 3 | "Promote and advertise: Create a Brand Store, Create a sponsored ad, Create a coupon, Create a promotion, Create a Prime Exclusive Discount" |

[official] sell.amazon.com, "FBA holiday guide", https://sell.amazon.com/fulfillment-by-amazon/holiday, read 2026-11-09.

B8. **GUIDANCE: "Myths" page on judging ads at a peak.**

- "A temporary spike in ACOS doesn't mean your ads aren't working". The page then defines the wider view in Amazon's own words: "ACOS only measures the efficiency of ad-attributed sales, not the full picture. That's where total advertising cost of sales (TACOS) comes in. TACOS reveals whether your total sales (organic and paid) are growing in relation to your ad spend." A second Amazon page gives the ratio itself: "TACOS shows your ad spend as a percentage of total sales" ([official] Amazon Ads, "The author's guide to Sponsored Products", https://advertising.amazon.com/library/guides/authors-guide-to-sponsored-products, read 2026-11-09; written for book authors). Neither page names the sales field, the ad products or the dates that enter the ratio (contradiction 1 in Verification).
- "check 7–14-day attribution before making changes. Sales during peak events often occur days after the initial ad click."
- "many brands see conversion rates drop during major sales events. Shoppers are in discovery mode".
- About 2–3 weeks before the event, "use the Sponsored Brands video ad format to spotlight upcoming holiday deals".
- Brand Stores updated in the last 90 days had 9% more repeat visitors and 10% higher attributed sales per visitor (for human readers only).
- Amazon cites Mintel: "31% of shoppers planning to make purchases between Cyber Monday (December 1, 2025) and New Year's".

[official] Amazon Ads, "Holiday advertising myths: What experts want you to know", https://advertising.amazon.com/library/guides/common-holiday-advertising-myths, read 2026-11-09.

B9. **GUIDANCE: Spending intent across the season.** The holiday guide cites EMARKETER/Gallup: spending intentions fell from $1,007 in October 2025 to $778 in November. It also cites ECDB: "In 2025, worldwide online sales reached $1.5 trillion in Q4, 31.2% above the average quarterly revenue of Q1–Q3". For human readers only. [official] "Holiday advertising guide", read 2026-11-09.

B10. **GUIDANCE: Amazon's own effect figures, all with their baselines and for human readers only.**

- Prime Day 2025: "Advertisers saw an increase of 137% in sales using Sponsored Products, Sponsored Brands, and display ads during Prime Day when compared to average category growth". Baseline 06/29/25–07/05/25, tentpole 07/06/25–07/12/25; advertisers spending at least $5, across the 20 marketplaces the footnote lists (AE, AU, BE, BR, CA, DE, EG, ES, FR, IT, JP, MX, NL, PL, SA, SE, SG, TR, UK, US). Sponsored Brands plus display: 39% ([official] "Prime Day 2026: Advanced advertising strategies").
- Holiday gifting 2025: a 145% increase in sales versus average category growth; baseline 11/16/25–12/06/25, tentpole 12/07/25–12/27/25; advertisers spending at least $1 in 14 marketplaces ([official] "Holiday advertising guide").
- UK Sponsored Products at Christmas: +75pp in sales versus category, Dec 4–31, 2022 versus Nov 6–Dec 3 ([official] "3-step guide to the peak season", https://advertising.amazon.com/library/guides/boost-seasonal-sales).
- Kantar 2022: 58.8% of US shoppers and 40.6% of JP shoppers said they were likely to buy from an ad on Amazon during BFCM (same page).
- Mother's Shea, quoted in an Amazon guide: "Our 2022 holiday sales were up 112% compared to 2021, with traffic up 87% and conversion up by 10% compared to the pre-holiday season" ([official] Amazon Ads, "How retail tentpole moments can deliver year-round results", Sep 9, 2023, https://advertising.amazon.com/blog/retail-tentpole-events-to-drive-year-round-results).
- L'Oréal: 78% of sales in the 48-hour PBDD window ([official] "Sales promotion guide", https://advertising.amazon.com/library/guides/sales-promotion).
- Noé Feretti (Panier des Sens), quoted by Amazon: in Q4, ad-driven sales are about 65% of total sales ([official] "Holiday advertising guide").

All pages read 2026-11-09. Each of these compares advertisers with "average category growth" or with a pre-period. None is a controlled test, and the baseline windows sit next to the event.

B11. **GUIDANCE: Amazon on the risk of promotions.** "Regular promotions can condition customers to wait for deals"; "Promotional periods can create artificially inflated sales figures". [official] Amazon Ads, "Sales promotion guide", https://advertising.amazon.com/library/guides/sales-promotion, read 2026-11-09.

B12. **GUIDANCE: The console is "Amazon Ads Agent".** The unBoxed 2026 announcements describe "Amazon Ads Agent", which brings "together the ads console and Amazon DSP into a single buying surface". Shopper-facing AI is "Alexa for Shopping", where "Branded Conversations" run. Nothing in those announcements is seasonal. [official] Amazon Ads, "unBoxed 2026 news announcements", https://advertising.amazon.com/library/news/unboxed-2026-news-announcements, read 2026-11-09. The rename is stated elsewhere: "On May 13, 2026, Rufus was renamed Alexa for Shopping" ([official] aboutamazon, "'Amazon Rufus' AI experience comes to the Amazon Shopping app", https://www.aboutamazon.com/news/retail/amazon-rufus, read 2026-11-09). Console names in older guides ("campaign manager") refer to the same surfaces.

### C. Budget rules and Amazon's recommended events

C1. **RULE: There are two kinds of budget rule.**
- Schedule-based rules let you "set budgets in advance for special events, such as Prime Day and Halloween".
- Performance-based rules use ROAS, CTR or CVR.

The guide also describes two kinds of bidding rule (schedule bid rules and rule-based bidding with ROAS guardrails), and promises to "Optimize your budget for key events, with personalized recommendations". [official] Amazon Ads, "Budget and bidding rules", https://advertising.amazon.com/library/guides/budget-rules, read 2026-11-09.

C2. **RULE: Recommended events are chosen per campaign, from its products, and can change.** When budget rules launched in the console for Sponsored Products (Aug 12, 2021), Amazon wrote:
- "We'll recommend events based on the products in your campaign when we anticipate more demand... If you remove or update products from a campaign, we will not remove the rule, but the recommendations might change."
- "During shopping events, we will provide recommended budgets based on historical shopping activities."
- Performance rules evaluate the previous 7 days and need a minimum daily budget of $10.

[official] Amazon Ads, "Budget rules now available in Amazon advertising console globally" (URL slug dynamic-budget-control), https://advertising.amazon.com/resources/whats-new/dynamic-budget-control, read 2026-11-09.

C3. **RULE: Recommended events in the API.** The API guide says:
- "Schedule-based budget rules can be set to increase daily budgets for any date range or recommended events, such as Black Friday or Cyber Monday. During shopping events, recommended budgets based on historical shopping activities will be provided."
- Performance-based rules use "the previous 7 days for sellers and 14 days for vendors".

[official] Ads API, "Budget rules overview", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/overview.md, read 2026-11-09.

C4. **RULE: Which ad products get recommended events, and what happens when an event's dates are not yet announced.**
- "Recommended events are only available for Sponsored Products and Sponsored Brands."
- "For events that are available in the list before the dates are announced, the start and end date are empty during rule creation. Later, these rules are automatically updated when the dates are announced."
- Weekly recurrence applies only to custom date ranges.
- An intraday (hours-of-day) schedule is available only in US, CA, UK, IN and JP, and hours-of-day rules carry a minimum budget.
- The guide's Sponsored Brands example (`POST /sb/campaigns/budgetRules/recommendations`) returned Halloween 20201027–20201031 with a 20% suggested increase.

[official] Ads API, "Schedule-based budget rules", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/schedule-based.md, read 2026-11-09. For hours of day, see also [official] "Hours of day now available for schedule-based budget rules" (Nov 30, 2023), https://advertising.amazon.com/resources/whats-new/hours-of-day-available-for-schedule-based-budget-rules, read 2026-11-09.

Sponsored Display has `/sd/budgetRules`, `/sd/campaigns/budgetRecommendations` and `/sd/campaigns/budget/usage` but no recommended-events endpoint. Its budget-rule model nonetheless carries `eventTypeRuleDuration` (`eventId` required, "available from the budget rules recommendation API"), and its `RecurrenceType` enum is DAILY | WEEKLY ([official] SD 3.0 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml, read 2026-11-09).

C5. **RULE: The Sponsored Products event list endpoint.** `POST /sp/v1/events` (operationId SPGetAllRuleEvents) "Gets all special individual and grouped events with suggested date range in advertiser's marketplace."
- It returns `events[]` (`eventId`, `eventName`, `startDate`, `endDate`, ISO-8601) and `groupedEvents[]` (`groupedEventId`, `groupedEventName`, `startDate`, `endDate`).
- Permission needed: advertiser_campaign_edit or advertiser_campaign_view.

[official] Ads API, Sponsored Products 3.0 OpenAPI, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json, read 2026-11-09.

C6. **RULE: The per-campaign budget-rule recommendation.** `POST /sp/campaigns/budgetRules/recommendations` (SPGetBudgetRulesRecommendation; content type `application/vnd.spbudgetrulesrecommendation.v3+json`).
- Request: `{recommendationType: EVENTS_FOR_EXISTING_CAMPAIGN, campaignId}`.
- Response: `recommendedBudgetRuleEvents[]`, each with `eventId`, `eventName`, `startDate`/`endDate` (YYYYMMDD) and `suggestedBudgetIncreasePercent`.

[official] SP 3.0 OpenAPI, read 2026-11-09.

C7. **RULE: The budget-rule object.**

Paths:
- `POST/PUT/GET /sp/budgetRules`
- `GET /sp/budgetRules/{budgetRuleId}`
- `/sp/budgetRules/{id}/campaigns`
- `POST /sp/campaigns/{campaignId}/budgetRules`
- `GET /sp/campaigns/{campaignId}/budgetRules`
- `DELETE /sp/campaigns/{campaignId}/budgetRules/{budgetRuleId}`
- `POST /sp/budgetRulesAssociation` and `/sp/budgetRulesAssociation/delete`

`SPBudgetRuleDetails` fields:
- `name`: "unique within a campaign".
- `ruleType`: SCHEDULE | PERFORMANCE.
- Duration, one of two forms:
  - `duration.dateRangeTypeRuleDuration`: `startDate`/`endDate` YYYYMMDD, inclusive; the start must be "greater than or equal to current date".
  - `duration.eventTypeRuleDuration`: `eventId` "available from the budget rules recommendation API"; `eventName`, `startDate` and `endDate` are read-only, and the "startDate... present only for announced events".
- `recurrence`: type enum DAILY only in the model; `daysOfWeek`; `intraDaySchedule` with `startTime`/`endTime` in hh:mm:ss.
- `budgetIncreaseBy`: `{type: PERCENT, value}`.
- `performanceMeasureCondition`: `metricName` ACOS/CTR/CVR/ROAS, plus `comparisonOperator` and `threshold`.

Create answers 207 (multi-status). The list response carries `ruleState` (ACTIVE | PAUSED), `ruleStatus` (a read-only string), `createdDate` and `lastUpdatedDate`. [official] SP 3.0 OpenAPI, read 2026-11-09.

Discrepancy: the guide in C4 says weekly recurrence exists for custom ranges, but the SP model's RecurrenceType enum lists DAILY only (the SD 3.0 model lists DAILY | WEEKLY, C4). Sponsored Brands has the parallel paths `/sb/budgetRules`, `/sb/campaigns/budgetRecommendations` and `/sb/campaigns/budget/usage` ([official] SB 4.0 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json, and SB 3.0 yaml, read 2026-11-09).

C8. **RULE: Performance rules by ad product.** ACOS, CTR and CVR are available for SP and SD. Impression share (IS) and new-to-brand (NTB) are SB only, and IS is unavailable for video. ROAS works on all three. Sellers are evaluated over 7 days, vendors over 14. [official] Ads API, "Performance-based budget rules", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/performance-based.md, read 2026-11-09. SB's IS and NTB metrics launched Apr 8, 2023 ([official] "New metrics available for Sponsored Brands performance-based budget rules", https://advertising.amazon.com/resources/whats-new/sponsored-brands-performance-based-budget-rules, read 2026-11-09). The guide words the window as "within 7 days of an ad click" for sellers and "within 14 days of an ad click" for vendors.

C9. **RULE: History endpoints and API version.** The budget-rule history endpoints were deprecated on 8/31/2023 ([official] Ads API, "Deprecations", https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md, read 2026-11-09). The Ads API v1 merged spec has no budget-rule, event-list or optimization-rule endpoints, so budget rules, the event list and bid rules stay on the SP/SB/SD v3 paths. (Its `/adsApi/v1/create/events` is the Event Manager conversion-event endpoint, permissions `event_manager_view`/`event_manager_edit`, unrelated to shopping events.) The v1 spec does carry event themes in two places: the unified bid recommendation object `Bid` has a `theme` field whose `BidRecommendationTheme` enum is `BFCM_HOLIDAY`, `CONVERSION_OPPORTUNITIES`, `FALL_PRIME_DEAL_EVENT`, `PRIME_DAY`; and theme targets (`themeTarget.matchType`) include `KEYWORDS_RELATED_TO_PRIME_DAY` ("Search terms that shoppers are likely to use during Prime Day... These keywords will only match queries through the end of Prime Day") and `KEYWORDS_RELATED_TO_GIFTS` ("Search terms related to gifts") ([official] AmazonAdsAPIALLMerged_prod_3p.json, https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json, read 2026-11-09). Which ad products accept those theme targets is not stated next to the enum; the SP 3.0, SB 3.0 and SB 4.0 specs read here do not contain `KEYWORDS_RELATED_TO_PRIME_DAY`.

C10. **RULE: Budget recommendations report missed opportunity, which is how a capped campaign shows up.** `POST /sp/campaigns/budgetRecommendations` (`application/vnd.budgetrecommendation.v3+json`) returns:
- `suggestedBudget`;
- `sevenDaysMissedOpportunities`: `percentTimeInBudget` (0–1), `estimatedMissedImpressionsLower/Upper`, `estimatedMissedClicksLower/Upper`, `estimatedMissedSalesLower/Upper`, `startDate`/`endDate`;
- `budgetRuleRecommendation`: `{ruleId, ruleName, suggestedBudgetIncreasePercent}`.

`POST /sp/campaigns/budget/usage` reports budget usage. [official] SP 3.0 OpenAPI, read 2026-11-09.

C11. **RULE: The initial budget recommendation includes special events.** `POST /sp/campaigns/initialBudgetRecommendation` returns `specialEvents[]` (maxItems 5). Each carries `eventKey`, `eventName`, `startDate`, `endDate`, `dailyBudget` ("Recommended daily budget for the new campaign during the special event period") and `benchmark`; `budgetModifier` is deprecated. [official] SP 3.0 OpenAPI, read 2026-11-09.

### D. Bids at events: bid rules, theme-based bid suggestions, the special-days theme

D1. **RULE: Event-based bid rules in the console.** Event-based bid rules launched for Sponsored Products on Jan 2, 2025: "Note: 'Recurring Events' are only available in the JP marketplace while 'Individual Events' are available WW". [official] Amazon Ads, "Events for schedule bid rules, now available for Sponsored Products advertisers in the advertising console" (URL slug event-based-bid-rules-for-sponsored-products-advertisers), https://advertising.amazon.com/resources/whats-new/event-based-bid-rules-for-sponsored-products-advertisers, read 2026-11-09. Schedule-based bid rules (time of day, days of week, date ranges) launched Nov 6, 2023 ([official] "Schedule based bid rules now available for Sponsored Products", https://advertising.amazon.com/resources/whats-new/schedule-based-bid-rules-available-for-sponsored-products, read 2026-11-09).

D2. **RULE: The schedule bid rule object in the API.** Paths: `POST/PUT /sp/rules/optimization`, `POST /sp/rules/optimization/search`, `POST /sp/campaigns/{campaignId}/optimizationRules`.

v1 content type `application/vnd.spoptimizationrules.v1+json`:
- `ruleCategory` BID, `ruleSubCategory` SCHEDULE.
- `action.actionDetails` `{actionOperator: INCREMENT, actionUnit: PERCENT, value}`, where value is "An integer between 1 & 100, representing the percent increase on base bid."
- `actionType` ADOPT.
- `recurrence` `{type: DAILY|WEEKLY, daysOfWeek, timesOfDay, duration {eventId, eventName, startTime, endTime}}`. The times are "ISO 8061" (sic), and `startTime` is "Not Required only when eventId present". The duration's description reads: "The duration of an optimization rule based on special events (example: Prime Day) or custom date ranges."
- `status`: ENABLED/ENDED/PAUSED/SCHEDULED, but "Only ENABLED and PAUSED are accepted in requests".

v2 content type:
- `ruleCategory` BID/BUDGET/TARGETING; subCategory PERFORMANCE/SCHEDULE.
- Condition attributes: ACOS, CLICKS, CPC, CTR, CVR, IMPRESSIONS, ORDERS, ROAS, SALES, SPEND.
- Targeting `lookbackDays` 3–65.
- "Budget rules are not supported for this operation."

Sponsored Brands exposes `/sb/rules/optimization` (beta), with associate, list and disassociate. [official] SP 3.0 OpenAPI; SB 4.0 OpenAPI; read 2026-11-09.

The ceiling to note is that a schedule bid rule can raise a base bid by 1% to 100% in one rule.

D3. **RULE: Rule-based bidding (ROAS guardrail) has entry conditions and an automatic off-switch.**
- Entry: the campaign must have run at least 10 days and have at least 10 conversions in 30 days.
- The guardrail uses the previous 21 days.
- Amazon disables the rule if the "ROAS of the campaign for the last 20 days drops to less than 30% of your ROAS over a 20-to-40-day period".
- Minimum budgets include US 10, IN 300, JP 600 and MX 50.
- Path: `/sp/rules/campaignOptimization`.

[official] Ads API, "Bidding rules overview", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/overview.md, read 2026-11-09. An event that changes ROAS sharply sits inside these windows. The 21-day and 20/40-day figures are the ones a skill reads against the event dates.

D4. **RULE: Theme-based bid recommendations carry the event themes.** `POST /sp/targets/bid/recommendations` (content types v3/v4/v5 are all still listed in the spec; the Deprecations page dates the v3 content type's deprecation to "May 15,2025", with v4 as replacement).
- The theme enum includes `BFCM_HOLIDAY`, `CONVERSION_OPPORTUNITIES`, `FALL_PRIME_DEAL_EVENT` and `PRIME_DAY` ("This API currently supports...").
- `bidRecommendations` has maxItems 2.
- v5 returns `suggestedBidImpactMetrics` and an 8-bid analysis (`includeAnalysis`; US, existing ad groups).
- Placements: PLACEMENT_TOP, PLACEMENT_REST_OF_SEARCH, PLACEMENT_PRODUCT_PAGE.

[official] SP 3.0 OpenAPI; Ads API "Deprecations" (v3 date); read 2026-11-09. The quickstart says the bids are "calculated from a group of recent winning bids for similar products". It also says impact metrics are "computed assuming your campaign does not run out of budget" ([official] Ads API, "Theme-based bid suggestions quickstart guide", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/bid-suggestions/theme-based-bid-suggestions-quickstart-guide.md, read 2026-11-09). That assumption matters on a peak day, when campaigns cap out (B3).

D5. **RULE: The SPECIAL_DAYS keyword theme.** In `/sp/targets/keywords/recommendations` v5:
- "CONVERSION_OPPORTUNITIES - The default theme which aims to maximize number of conversions".
- "SPECIAL_DAYS - A theme available during high sales events such as Prime Day, to anticipate an increase in sales and competition."
- Bidding strategy values: LEGACY_FOR_SALES (down only), AUTO_FOR_SALES (up and down), MANUAL.

[official] SP 3.0 OpenAPI, read 2026-11-09.

D6. **GUIDANCE: Amazon's post-event example on dynamic bids.** In a hypothetical case, a wireless audio brand ran up-and-down bidding with a 100% top-of-search multiplier, and ROAS fell from 4.1 to 2.9. Amazon's answer: "Lower top-of-shopping results multipliers and test down-only bidding". A kitchen brand's ACOS went from 19% in early October to 34% in Cyber Monday week. [official] Amazon Ads, "Post-event advertising strategy", https://advertising.amazon.com/library/guides/post-event-advertising-strategy, read 2026-11-09. These are scenarios Amazon built for illustration, not measured cases. The up-to-100% raise under up-and-down bidding is in `areas/bids-and-placements.md`.

### E. CPC and the auction at peaks

E1. **RULE: Amazon's own words on peak-period pricing.** Amazon's response to the FTC says:
- "Our auction looks at a combination of which ad is most relevant to the customer and the price an advertiser is willing to pay... When the winning advertiser's bid exceeds both the hard and soft reserve, they pay the soft reserve, which is less than they were willing to pay. When the winning advertiser's bid exceeds the hard reserve but doesn't meet the soft reserve, we still grant the placement to that advertiser and they pay their bid. In no scenario does an advertiser pay more than their bid."
- Reserves "are determined in real time and aren't predictable in advance by anyone, including Amazon or the advertiser."
- Amazon says it "updated our Amazon Ads Help content to explicitly explain the use of reserve prices."
- Amazon's figures: from 2019 through 2024 the average SP search CPC "remained flat adjusted for inflation", conversion rates "grew 24% from 2021 to 2025", "Average winning bids fell 50% from 2019 to 2025", and "roughly 92% of placed ads are not given to the highest bid".
- The response does not mention peak periods, seasons or Prime Day; the peak/non-peak wording is the help page's (E2).

[official] aboutamazon, "Amazon's response to the FTC's lawsuit regarding Sponsored Ads", https://www.aboutamazon.com/md/company-news/amazon-ftc-sponsored-ads-lawsuit-response, read 2026-11-09.

E2. **RULE, as quoted by the complaint: the help-page wording.** The complaint reproduces the March 2026 version of the Amazon Ads help page "Amazon Ads auctions", under "Ad selection and pricing": "Other reserves influence your final CPC or vCPM based on factors including the likelihood that the ad will lead to a sale, predicted return on your ad spend, the value of any competing bids, placement, context, and predicted performance (e.g., the same ad placement may have a different value during a peak shopping period than a non-peak period). As a result, the price charged to you may exceed the runner-up bid but will never exceed the maximum bid you authorize." The complaint says reserve pricing was first mentioned on October 30, 2025, on a Support Center page labelled "Understand Amazon Ad auctions", whose wording (¶147) already read: "the same ad placement may have a different value during peak shopping period than a non-peak period". The help page itself is a sign-in shell to this seat (see Unreachable), so the wording is taken from the complaint's quotation. [official, via the complaint] FTC et al. v. Amazon, Case 2:26-cv-03097 (W.D. Wash., filed 08/31/26), ¶¶146–148, https://www.illinoisattorneygeneral.gov/News-Room/Current-News/FILED%20PUBLIC%20Amazon%20Complaint%208.31.26.pdf, read 2026-11-09.

E3. **Allegations, not findings: what the complaint says about peak events.** [opinion] These are the allegations of the FTC and 22 state attorneys general. They are untested in court, and Amazon disputes them (E1).
- "during the Christmas holiday season and other peak shopping events (referred to as 'high velocity events' or 'HVEs'), Amazon often raises its maximum surcharge levels" (¶68).
- An internal quote on Prime Day 2023: "Advertisers may expect other advertisers to be increasing bids in preparation for PD [Prime Day], so the CPC increases may not be unexpected" (¶70).
- The 2021 early-December "CPC Spike" incident (¶71).
- Amazon allegedly decided "to mask future surcharge increases by gradually implementing them in advance of peak shopping days" (¶72).
- The HVEs named are Prime Day, Prime Early Access Sale, Prime Big Deal Days, and the holiday sales from Thanksgiving through Christmas (¶220).
- A 2021 objective of "RoAS parity" between high-velocity events and other days (¶225).
- "In 2021 and 2022, Amazon raised surcharge constraints... during Prime Day and after Thanksgiving" (¶226).
- An internal 2021 document, "Pricing Introduction", quoted at ¶157: "Before Black Friday, we introduced seasonal adjustments to reserve prices, which enabled SB to monetize large-scale seasonal events till the end of the year." The quoted passage does not say which year's Black Friday.

Source: the complaint as above, read 2026-11-09. The plaintiffs are the FTC, 20 states, the People of California and Maryland's Consumer Protection Division (22 state plaintiffs).

Texas sued separately the same day under the Texas Deceptive Trade Practices Act. Its press release alleges that "undisclosed 'soft reserve' prices... push the winner's cost up toward its own maximum bid—by roughly 17% on ordinary shopping days and more than 25% during peak events like Prime Day. Advertisers now pay their own bid nearly 80% of the time." [opinion, a litigant's allegation] Texas Attorney General, "Attorney General Ken Paxton Sues Amazon for Rigging Advertising Auctions That Overcharged Businesses $4.5 Billion in a Single Year...", Aug 31, 2026, https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-amazon-rigging-advertising-auctions-overcharged-businesses-45, read 2026-11-09. The Texas petition itself was not read.

E4. **What this means for reading CPC [seat].** Two points stand on Amazon's own words. The price paid can sit anywhere between the runner-up price and the advertiser's own bid (E1, E2). And the help wording quoted in the complaint says a placement "may have a different value during a peak shopping period than a non-peak period" (E2); Amazon's FTC response does not address peaks. So a CPC rise on an event day can come from competing bids, from reserve prices, or from both, and no seller-side report separates them. The rise is bounded only by the advertiser's bid. The quantity cx can see is CPC divided by bid, per target, before and during the event (see Ad Badger in "What practitioners add").

### F. Deals, coupons and Prime Exclusive Discounts: types, eligibility, fees, deadlines

F1. **RULE: Deal types and who may run them.**
- "There are two types of deals: Lightning Deals and Best Deals. A Lightning Deal can run from 4 to 12 hours, as determined by Amazon. A Best Deal can run for a select number of days. The deal is applied automatically without a code. Both deals can feature special merchandizing like a Deals Badge to help them stand out."
- Eligibility: "You'll need a Professional selling plan and an overall rating of at least four stars to create deals. Only select products are eligible for Lightning Deals."
- Visibility: "Customers will see your deals on product detail pages, in search results, and on the Deals page."
- Deals are created from Advertising > Deals in Seller Central.

[official] sell.amazon.com, "Seller promotions" (May 27, 2026), https://sell.amazon.com/blog/seller-promotions, read 2026-11-09.

F2. **RULE: Coupons.**
- "To be eligible for coupons, you must have a Professional selling plan and an overall rating of at least 3.5 stars... there is a redemption cost each time a coupon is used."
- "You can add up to 200 ASINs to a coupon."
- "All coupons expire after 90 days"; Amazon suggests a duration of "two to three months".
- "Customers can also find coupons through search results, on the Amazon Deals page, and on products they've added to their carts."
- On stacking: "Avoid unintended 'discount stacking.' This happens when you add a coupon to a product that already has an active discount. This can lead to extreme discounts."

[official] "Seller promotions", read 2026-11-09. For Prime Day, Amazon also writes: "When you create a coupon, the product appears in shopping results with a coupon badge showing the amount of the discount." The criteria it gives are to "Discount the product more than 5%", "Schedule the dates to coincide with Prime Day" and "Set the audience to Amazon Prime members" ([official] "Prime Day tips", read 2026-11-09).

F3. **RULE: Price discounts and Prime Exclusive Discounts.**
- "Pricing discounts are time-bound campaigns in which you can offer discounted prices on your products for up to 30 days on a limited number of units. For example, you can create a price discount specifically for Prime customers... Price discounts for products with a validated reference price appear with a strike-through price in search results and on product detail pages."

[official] "Seller promotions" and "Prime Day tips", read 2026-11-09. The detailed PED and price-discount rules (the event-price ceiling and reference-price checks) are on Seller Central help pages that this seat cannot reach (see Unreachable). They are not stated here.

F4. **RULE: Holiday 2026 deal deadlines, fees and the reference-price lookback.**
- Submission windows: "July 8 to September 8 for Prime Big Deal Days"; "July 8 to October 20 for Black Friday Week and Cyber Monday".
- Early-submission discount: "Submit your Prime Big Deal Days deals by August 5 and Black Friday Week and Cyber Monday deals by September 5 to save $50 on the upfront promotion fee."
- Lookback: "Prime Big Deal Days promotional prices are excluded from the 30-day and 60-day lookback window and won't affect the maximum deal price required for Black Friday Week and Cyber Monday deals."
- Fees "for Best Deals, Lightning Deals, and Prime Exclusive Price Discounts will be the same as Prime Day": "Upfront fee: $100 per promotion, plus... Variable fee: 1.5% of promotional sales (capped at $5,000)".
- Inventory deadlines for PBDD: Sep 2 (AWD), Sep 9 (FBA, minimal shipment splits), Sep 16 (Amazon-optimized splits). For BFCM: Oct 14, Oct 21, Oct 28.
- Holiday peak fulfillment fees run Oct 15, 2026 to Jan 14, 2027, averaging $0.32 per unit, with the 3.5% fuel and logistics surcharge on top.

[official] Seller Forums, News_Amazon, "Holiday 2026: Same fees, same eligibility, earlier deadlines", https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff, read 2026-11-09.

In a reply on the same thread, a seller wrote that registration showed "$50 per day + 1.5%" ([opinion] a seller reply on the same thread). The Promotions API model has a FeeFrequency enum of ONE_TIME | DAILY (F6), so a per-day upfront fee is something the model can represent. Which one applies to a given deal is read from its fee snapshot, not assumed. Third parties report that the PBDD 2026 deal deadline was extended to September 22 ([opinion] Ad Badger citing EcomCrew; bebolddigital).

F5. **GUIDANCE: Timing of self-service promotions.** "watch for submission timelines in Seller Central. Self-service options like coupons and discounts can be set up closer to event dates." [official] sell.amazon.com, "Prime Day", https://sell.amazon.com/prime-day, read 2026-11-09. A seller on the Holiday 2026 thread asked whether price discounts for PBDD also had to be in by September 8, "in the previous years you had until the actual day of"; the answer was not on the page ([opinion] a seller reply on the same thread).

F6. **RULE: How deals and promotions appear in the Promotions API (SP-API, version 2025-12-01).**

Operations:
- `GET /promotions/2025-12-01/promotions` (`searchPromotions`, 0.1 rps, burst 4).
- `GET /promotions/2025-12-01/promotions/{promotionId}` (`getPromotion`).
- `GET .../promotions/{promotionId}/selections/{selectionId}` (`getSelection`, up to 100 items; ITEMS selections only).

Search filters:
- `statuses`: PROCESSING, UPCOMING, RUNNING, EXPIRED, FAILED, CANCELLING, CANCELLED.
- `promotionTypes`: BASKET_BUILDING, DEAL, PRICE_DISCOUNT, COUPON.
- `asins`, `skus`.
- Date windows: `startDateBefore/After`, `endDateBefore/After`, `updateDateBefore/After`.
- `revision`: LATEST/PUBLISHED/ANY.
- `includedData`: ISSUES, CUSTOMER_SEGMENTS.

Fields:
- `couponType`: STANDARD, SUBSCRIBE_AND_SAVE, REORDER_REWARDS.
- `schedule.eventId`: "For event promotions, this field contains the event name when available (for example, `Prime Day`). For historic event promotions, this field may contain `EVENT` as a placeholder."
- `customerSegments`, where `PROGRAM` segments include `PRIME_EXCLUSIVE`, `MOM` and `STUDENT`.
- `merchandising.displayOnWebsite`: ALLOWED | NOT_ALLOWED ("Whether the promotion badge and details are displayed on the product detail pages and search results").
- `benefit.stacking`: ALLOWED | NOT_ALLOWED.
- `feeSnapshot.previewedFeeRates`, with `upfrontFee {rate, frequency}` and `variableFee {salesPercentage, feeCapAmount}`.
- `issues`.

[official] amzn/selling-partner-api-models, `models/promotions-api-model/promotions_2025-12-01.json`, https://github.com/amzn/selling-partner-api-models, read 2026-11-09.

Gap fill 2026-11-09, from the same model and the SP-API docs page: the model's three paths are all GET (`searchPromotions`, `getPromotion`, `getSelection`), though its info block says the API "enables selling partners to create and manage promotions". The docs page lists the API for "Sellers" only, in the NA, EU and FE regions, with the Pricing or Product Listing role, and dates its release notes to August 26, 2026 ([official] SP-API, "Promotions API", https://developer-docs.amazon/sp-api/docs/promotions-api, read 2026-11-09). `CustomerSegment.segmentType` is `BRAND` | `PROGRAM`. `BRAND` is described as a "Brand-tailored audience that targets customers interested in specific brands": its `segmentId` "contains the segment / audience ID", and `segmentDetails.brandSegmentDetails.brandId` is required. `PROGRAM` carries program names such as `PRIME_EXCLUSIVE`. `customerSegments` is returned only when `includedData=CUSTOMER_SEGMENTS` is sent. The `promotionType` enum has no Brand Tailored Promotions value (BASKET_BUILDING, DEAL, PRICE_DISCOUNT, COUPON).

F7. **RULE: Brand Tailored Promotions (BTP) (gap fill 2026-11-09).**
- Who: "Brand Tailored Promotions are available to Brand Representatives enrolled in Brand Registry and operating in Amazon's stores in the US, UK, Spain, France, Italy, Germany, and Japan." You need "a brand enrolled in Amazon Brand Registry and be designated as the Brand Representative for the primary account."
- Discount: "promotional discounts on your catalog or specific products ranging from 10% to 50% off. Each eligible customer can redeem the promotion on a single purchase."
- Audiences, by goal:
  - "New customer acquisition: Customers who have shown interest in your brand through clicks or cart adds in the last 90 days but haven't purchased yet".
  - "Customer re-engagement: Your brand's most loyal customers who are declining in sales, and lapsed customers who showed high intent but haven't purchased recently".
  - "Customer retention: Your brand's most loyal customers that are declining in sales, repeat purchasers, and your highest-spending customers from the last 12 months".
  - The create flow also names a Cross-sell goal. The page says "one of three goals" and then lists four.
- Size: "You can create tailored promotions for an audience size of 1,000 or more", and the audience "may change throughout the life of your promotion ... based on the audience refresh timeframe". "If the audience size is less than 1,000 for promotions with specific products, add more products".
- Product eligibility: products with one to four reviews need an average of 2.5 stars, five or more reviews at least 3 stars; "New" condition; not "Adult"; products with no reviews are eligible.
- Timing and limits: the start date must be "at least 48 hours in the future and within 60 days of the creation date, and the end date within 90 days of the start date". An optional maximum budget can be set. "Up to six hours before the promotion goes live, you can edit the customer discount and budget. After the promotion is live, only the budget can be edited, and it can only be increased." Deactivation "may take up to four hours", and an ended promotion "can't be reactivated". "You can only have 20 active or scheduled promotions at one time."
- Where shoppers see it: eligible customers "see the promotion on search detail pages, the promotion shopping page, and the Brand Stores page. They will also see a green badge that shows the brand promotion." The promotion cannot be shared.
- Stacking: "Yes, customers can stack a promotion on top of other promotions like coupons ... Brand Tailored Promotions are set as 'preferential' so the promotion code with the highest discount applies to the product."
- Events: "You can help maximize sales by deploying Brand Tailored Promotions during key shopping events like Prime Day or Black Friday."
- Fees: the page does not state them: "Visit the Seller Central Brand Tailored Promotions help page to review costs." That help page is a Seller Central help shell this seat cannot read (Unreachable).
- Where it is created: Seller Central, Advertising > Brand Tailored Promotions. No create or update operation exists in the SP-API Promotions model (above).

[official] sell.amazon.com, "What are Amazon Brand Tailored Promotions?" (Jan 20, 2026, Mickey Toogood), https://sell.amazon.com/blog/brand-tailored-promotions, read 2026-11-09.

The 2023 launch post listed six audiences: Brand Followers ("Customers who have clicked to follow your brand in Amazon's store"), Repeat Customers ("ordered your brand's products more than once in the last 12 months"), Recent Customers, High-Spend Customers ("in the last 12 months"), Potential New Customers ("clicked on your brand and products or added to cart recently, but have not purchased in the last 12 months") and Cart Abandoners ("added one or more of your brand's products in their cart, but haven't purchased in the last three months"). At launch the redemption was "limited to one unit redemption per customer", and the tool was US-only ([official] sell.amazon.com, "Brand Tailored Promotions: Offer exclusive discounts for loyal customers", Aug 1, 2023, Benjamin Hartman, https://sell.amazon.com/blog/announcements/brand-tailored-promotions, read 2026-11-09). The 2026 page groups audiences by goal and does not repeat the six names or the one-unit limit. Its cart-interest window is 90 days, where the 2023 cart-abandoner window was three months. The Brand Registry page lists BTP among the brand's promotion tools, "exclusive discounts tailored to recent, repeat, or high-spend customers, plus other audiences" ([official] sell.amazon.com, "Amazon Brand Registry", https://sell.amazon.com/brand-registry, read 2026-11-09).

F8. **RULE: Customer Engagement emails (brand followers and tailored audiences) (gap fill 2026-11-09).**
- "The Customer Engagement tool empowers brand owners registered in Brand Registry to engage with their Amazon followers through email. Brands with 1000 or more followers on Amazon Store will have the best experience when using this tool. However, this tool is accessible to all brands with followers." Themed templates (holidays, New Year resolutions, game day) are chosen from a "Select event type" menu ([official] Seller Forums, News_Amazon, "Create engaging email campaigns with themed templates in 'Customer Engagement' (beta) tool", about 2021 (the page shows "5 years ago"), https://sellercentral.amazon.com/seller-forums/discussions/t/e3f3a064ed378b7031537558efb43a18, read 2026-11-09).
- In September 2022 Amazon "introduced three new audience types within the Amazon Customer Engagement tool ... sellers can now expand beyond brand followers when sending free marketing emails to reach their most loyal customers, such as repeat customers, recent customers, and high-spend customers". "Sellers select the customer audience types and Amazon sends the marketing email directly to those customers." The reporting metrics named are "open rate, click-through rates, emails delivered, opt-out rates, sales, and conversion". The tool is "available at no cost in Seller Central"; the release said Tailored Audiences was in beta, with availability to all US sellers planned for early 2023 ([official] Amazon Press Center, "Amazon Launches Free Email Marketing Capabilities for Sellers to Reach Their Repeat, Recent, and High-Spend Amazon Customers", Sep 14, 2022, https://press.aboutamazon.com/2022/9/amazon-launches-free-email-marketing-capabilities-for-sellers-to-reach-their-repeat-recent-and-high-spend-amazon-customers, read 2026-11-09).
- No current Amazon page read states the tool's 2026 eligibility, send limits or markets. Neither the Ads API nor the SP-API surfaces read carries Customer Engagement or BTP audiences as an object a third party can create.

How these sit next to Sponsored Display remarketing [seat, from the definitions]: BTP's cart-interest and lapsed-customer audiences, Customer Engagement's followers and recent customers, and SD's `views(...)` and `purchases(...)` audiences (H2) are all built from a shopper's past views, carts or purchases of the brand. BTP and Customer Engagement carry no media cost on the pages read; BTP's cost is the discount, plus any fee on its unreadable help page. SD pays per click or impression and shows an ad without a discount. No Amazon page read says whether a shopper in a BTP audience is excluded from, or counted in, an SD audience. Nor does any page say how a BTP redemption is attributed in ad reports. AMC's promotional columns cover coupons, point-of-sale discounts and price discounts (I6), and say nothing on BTP codes.

F9. **RULE: UK and EU holiday 2026 deal deadlines, fees and inventory dates (gap fill 2026-11-09).**
- Deal submission window "from now until: September 23 for Prime Big Deal Days; November 18 for Black Friday Week". The early-submission discount: "Submit your Prime Big Deal Days deals by August 5 and Black Friday Week deals by September 5 to save 30% on the upfront promotion fee" (the US post gives $50 off, F4).
- "Prime Exclusive Discounts now require a minimum product rating of 3.5."
- Fees for Best Deals, Lightning Deals and PEDs, "the same as Prime Day":

| Store | Upfront fee | Variable fee |
|---|---|---|
| United Kingdom | £12 per promotion | 0.75% of promotional sales, capped at £600 |
| Germany | €16 per promotion | 0.75%, capped at €1,000 |
| France, Italy, Spain | €10 per promotion | 0.5%, capped at €300 |

- Inbound dates for Prime-badge eligibility: "September 9, 2026 (September 16 for UK): Prime Big Deal Days; October 21, 2026 (October 28 for UK): Black Friday Week".
- The festive peak fulfilment fee runs October 15, 2026 to January 14, 2027 in the UK (average £0.12 per parcel item, £0.07 per large envelope) and Germany (average €0.27 per unit), with the 1.5% fuel and logistics surcharge on top.

[official] Seller Forums UK, News_Amazon, "Peak season 2026: Inventory dates, peak fees, deal cutoffs and promotions" (posted about July 2026; the page shows "4 months ago"), https://sellercentral.amazon.co.uk/seller-forums/discussions/t/d8c34b0b-86ed-4aec-9b0a-8be6eabb8fb0, read 2026-11-09. All figures are for human readers only; a skill reads the season's post. The European BFW cutoff (November 18) falls about four weeks after the US one (October 20, F4).

F10. **RULE: The EU price-indication rule and Amazon's reference prices per store (gap fill 2026-11-09).**
- The law, in Germany's text: "Wer zur Angabe eines Gesamtpreises verpflichtet ist, hat gegenüber Verbrauchern bei jeder Bekanntgabe einer Preisermäßigung für eine Ware den niedrigsten Gesamtpreis anzugeben, den er innerhalb der letzten 30 Tage vor der Anwendung der Preisermäßigung gegenüber Verbrauchern angewendet hat." (Whoever must state a total price must, with every announcement of a price reduction, state the lowest total price applied to consumers in the 30 days before the reduction.) Paragraph 2 covers a stepwise, uninterrupted reduction, where the reference is the lowest price before the first step. Paragraph 4 exempts "individuellen Preisermäßigungen" (individual price reductions) and perishable goods ([law] Preisangabenverordnung (PAngV) § 11, https://www.gesetze-im-internet.de/pangv_2022/__11.html, read 2026-11-09). The EU source is Article 6a of Directive 98/6/EC, as inserted by Directive (EU) 2019/2161. EUR-Lex returned an empty 202 bot challenge to this seat (Unreachable), so the Directive's own wording is not quoted here.
- The EU court, on how the percentage is computed: "a price reduction which is announced by a trader in the form of a percentage, or in the form of a promotional statement intended to stress the advantageous price of an offer, must be determined on the basis of the lowest price applied by the trader during a period not shorter than 30 days prior to the application of the price reduction." The consumers' association had argued "it is not sufficient simply to state the lowest price in the last 30 days in the advertisement" ([law] Court of Justice of the EU, Press Release No 152/24, Judgment in Case C-330/23 Aldi Süd, 26 September 2024, https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-09/cp240152en.pdf, read 2026-11-09).
- Amazon's EU stores, on their "Reference Pricing and Savings" help pages (nodeId GQ6B6RH72AX8D2TD, served in English to this seat):
  - Amazon.fr: "For price reduction announcements, such as limited-time promotions, we display the lowest recent price of the product on Amazon.fr in the last 30 days before the price reduction is applied."
  - Amazon.es: the same sentence for Amazon.es.
  - Amazon.it: "we show the product's Lowest Price on Amazon.it in the last 30 days before the price reduction was applied."
  - Amazon.com.be and Amazon.se: "in the past 30 days prior to the application of the price reduction".
  - Amazon.pl: "najniższą cenę z 30 dni przed obniżką" (the lowest price of the 30 days before the reduction).
  - On the same pages, the "Was Price" is a median: "the median selling price paid by customers for a product on Amazon.fr, over the last 90 days, excluding promotional prices". An RRP shows only "if the product price applied in Amazon.fr or by at least one retailer was equal to or higher than the RRP in the last 90 days".
  - Amazon.de (English and German versions): no 30-day sentence. Its "Statt-Preis" (Was Price) is "der mittlere Verkaufspreis ... ausgenommen Aktionspreise", and it adds that deal-event badges (for example Black Friday) "können gelegentlich bei einem Angebot erscheinen, das zuvor nicht gekennzeichnet war ... Wenn ein Deal-Badge zu einem Angebot hinzugefügt wird, ohne dass es zu einer Preisänderung kommt, bedeutet dies, dass das Angebot bereits vorher ein aktiver Deal war" (a badge added without a price change means the deal was already active).
  - Amazon.nl: the page served no matching text.
  - Amazon.co.uk (the UK is outside the EU): "Lowest price in 30 Days means that the current price is lower than, or equal to, the lowest featured offer price for this item sold on Amazon.co.uk in the past 30 days."

  [official] Amazon customer help, "Reference Pricing and Savings", https://www.amazon.fr/gp/help/customer/display.html?nodeId=GQ6B6RH72AX8D2TD and the same nodeId on amazon.de, .co.uk, .it, .es, .com.be, .se, .pl, .nl, read 2026-11-09.
- In Germany, a court ruling on Amazon's own event pricing: the Munich I Regional Court ruled that Amazon's price advertising for its October 2024 "Prime Deal Days" was unlawful in three cases. These included a 19% discount computed from the RRP and one from a "customer average price". The court held that "according to the Price Indication Regulation, discounts must refer to the lowest price of the last 30 days". Amazon said it would appeal, and the ruling was "not yet final (Ref. 4 HK O 13950)" ([opinion, press report of a ruling] heise online, Volker Briegleb, "Court: Amazon must label special offers more transparently", July 16, 2025, https://heise.de/-10488538, read 2026-11-09). The appeal's outcome was not found.
- Amazon Ads' own advertising-copy policy (`/resources/ad-policy/creative-acceptance/advertising-copy`, in every locale tried) redirects to a sign-in help shell (help GQBSYPQKDK5G9EQX). A web-search summary of that page describes an EU rule that price-reduction claims on ads be calculated against the lowest price of at least the preceding 30 days, excluding the UK. This seat could not read the page, so the claim is not stated here as a rule (Unreachable; Open questions).

What this does to a deal badge and an ad's savings claim [seat, from the texts above]. In an EU store, a percentage or "deal" claim is measured against the lowest price of the prior 30 days. That reference is not Amazon's 90-day median "Was Price", and it is not the 90-day average AMC uses for `price_discount_amt` (I6). A price raised in the 30 days before an event therefore raises nothing: the lowest price in the window stays the reference. A coupon or price discount run in the month before an event sets a lower reference for the event. Amazon's own UK "Lowest price in 30 Days" badge uses the same 30-day window, though the UK is outside the Directive. In the US, the 30-day and 60-day lookbacks of F4 are Amazon's own deal-price rules, not a statute, and their mechanics sit on unreadable help pages (Open question 5). For ad creative, the policy rules already in G5 and G6 (savings must match between ad and landing page; "up to X%" needs 10% of the selection at X) then act on a percentage that, in the EU, was computed from the 30-day low.

### G. How deals surface inside ads, and the ad policy on deal and event claims

G1. **RULE: Responsive eCommerce Creative (REC) deal badges, in Sponsored Display and display.**
- "If your product qualifies for Deal of the Day, Lightning Deal, or Best Deal, the creative will automatically render a deal badge... REC deal badging is only available on the 'Shop now' variation."
- At BFCM, REC is "Deals-enabled: REC automatically pulls product pricing and information from detail pages and displays associated deals badges (including a BFCM badge) for selected deal types." "If the deal changes, discount messaging updates automatically on your ads."
- REC holds up to 20 ASINs and is "out-of-stock-aware, hiding any products that are no longer in stock".
- The custom REC headline "cannot contain a price or deal".

[official] Amazon Ads, "Holiday shopping season performance-boosting tips", https://advertising.amazon.com/library/guides/holiday-shopping-season-performance-boosting-tips, and "Black Friday and Cyber Monday advertising tips", https://advertising.amazon.com/library/guides/black-friday-and-cyber-monday-advertising-tips, read 2026-11-09.

G2. **RULE: The Sponsored Brands product collection gets a deal call-to-action automatically.** "Ideally, choose product deals since Amazon promotes them by automatically displaying a new CTA (call to action) with deals, messaging, and a seasonal lifestyle image in the ad creative." [official] Amazon Ads, "Key events store prep", https://advertising.amazon.com/library/guides/key-events-store-prep, read 2026-11-09. The sentence was still on the page on 2026-11-09.

The Product Collection format's end, as Amazon's own pages date it (re-opened 2026-11-09 for contradiction 2):
- June 2026: deprecation announced.
- "Starting August 2026, requests to create new Product Collection ads will succeed but create a Manual Collection ad instead. Any custom images provided will be accepted but will not render." In v1, `productCollectionSettings` "will be automatically mapped to `manualCollectionSettings`". Manual collections need at least 3 ASINs and titles of at most 32 characters.
- "Shutoff Date: January 2027"; "Post January 2027, requests to create new Product Collection ads will return an error" ([official] Ads API, "Deprecations", section "June 2026 - Deprecation of Sponsored Brands Product Collection Ad Type", https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md). The migration guide's timeline says the same ("January 2027: Final shutoff. All API requests to create Product Collection ads will be rejected with an error"). It also answers "Will my existing Product Collection ads stop serving impressions?" with "No. Existing Product Collection ads will continue to serve impressions and can be read, queried, paused, or deleted via the current API endpoints" ([official] Ads API, "Migration Guide for Product Collection to Collections Ad Type", https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-product-collection.md).
- "Beginning February 2027, product collections will no longer be supported." This comes with `ListMigrations` (`POST /sb/v4/migrations/list`), which returns recommended `MANUAL_COLLECTION` and `AUTO_COLLECTION` replacements per Product Collection ad ([official] Ads API, release notes, "Introducing the ListMigrations API for Sponsored Brands Product Collection migration", September 18, 2026, https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md; SB 4.0 OpenAPI operation `ListMigrations`).
- `creativeType` tells the types apart: `PRODUCT_COLLECTION` for legacy ads, `MANUAL_COLLECTION` and `AUTO_COLLECTION` for the new ones (migration guide).

All read 2026-11-09. So two dates stand on Amazon's pages. January 2027 is the create shutoff in the Deprecations page and the migration guide. February 2027 is the release note's end of support. The guide's statement that existing ads keep serving does not say until when. Neither the Collections guide nor the migration guide mentions deals, a deals CTA or a seasonal image ([official] Ads API, "Collections", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/ads/collections.md, read 2026-11-09). A Product Collection created since August 2026 is in fact a Manual Collection, whose custom image does not render [seat, from the transition note]. So whether the automatic deals CTA applies to it is not stated.

G3. **RULE: Brand Store deals pages.**
- The Store creates an automatic "All Deals" page that "Displays and removes deals based on their active dates". "Amazon won't automatically create an All Deals page if you use the Featured Deals widget and add it in one of your store pages."
- Policy: "Don't call out Amazon's high-traffic events, such as 'Prime Day Brand Store.'" and "Don't call out numerical discounts or any percentages".
- For human readers only: SB "drive page visit" ads with a Store landing page had 28% higher ROAS (H2 2024), and SB video with a Store landing page had a 23% higher average conversion rate.

[official] "Key events store prep", read 2026-11-09.

G4. **RULE: Brand Store promotional messaging at BFCM.**
- "promotional messaging is only permitted in your Brand Store when used with the Featured Deals widget (FDW)". The FDW "shows products with active promotions (including 'Subscribe & Save')". "At least four ASINs need to be added to activate the FDW". The approved layout is "FDW on top, text banner in the middle, Product Grid at the bottom".
- "Sales events... should start no more than seven days prior to the event... and be removed or updated within 24 hours of the event date, unless the event is considered to last longer (like Cyber Week)."
- "Brand Stores cannot be scheduled within 24 hours of the intended start date... Please submit your Brand Store at least 48 hours ahead".
- Banned copy includes "Today only", "Save 50%" and "Huge savings".

[official] "Black Friday and Cyber Monday advertising tips", read 2026-11-09.

G5. **RULE: Deal claims and event names in creative.**
- "All deals advertised should be live at the time the ad is live. Deal teasing is not permitted."
- "Price deal mismatch: All prices or savings must be in the same format on the ad creative and landing page."
- Off-site, "BFCM messaging will be allowed only if you have an official BFCM deal linking back to Amazon. However, the BFCM logo can never be used."
- Wording by duration:

| Wording | Maximum duration |
|---|---|
| "available on Black Friday only" | 24 hours |
| "Black Friday Week" | about 8 days, beginning 8 days before and ending by the last day of the event (Event days policy) |
| "Black Friday weekend" | about 3 days (Nov 23–28) |
| "Cyber Monday Week" | not named in the Event days policy |
| "Black Friday" / "Cyber Monday" | about 14 days (Nov 17–Dec 4) |
| "11:11" (the page's spelling; "Singles' Day") | about 21 days (Oct 28–Nov 19); "11:11 only" or "Singles Day only" means Nov 11 alone |

- In the UAE and KSA the term is "White Friday", and it may run through Dec 7. Australia runs through Dec 4. Brazil may use "Black Friday" Nov 6–27.

[official] "Black Friday and Cyber Monday advertising tips", read 2026-11-09; the two "Week" rows are Amazon Ads' "Event days" policy (https://advertising.amazon.com/help/GQ3SJ5QCWCQCKCYQ), read 2026-11-10, where the guide, read again that day, still says "approximately seven days" for both. The calendar dates in that table are the page's, for its year; a skill reads them from the page each season.

G6. **RULE: Discount-range claims and dynamic prices.**
- "If you advertise a range of discounts (by displaying 'up to' or 'from,' plus a percentage discount), at least 10% of all the ASINs in the promotion selection must be offered at or above the maximum discount advertised."
- "If the claim on the ad becomes inaccurate due to dynamic pricing on the landing page, creatives must be paused and updated to use qualified claims".

[official] "Holiday shopping season performance-boosting tips", read 2026-11-09. The quick reference also lists "Has pricing and savings claims that are the same on the ad and landing page" ([official] Amazon Ads, "Ad policy quick reference", https://advertising.amazon.com/resources/ad-policy/quick-reference, read 2026-11-09). The "Sponsored ads additional policies" page was read; it is contractual terms text and carries no deal, event or Black Friday content ([official] https://advertising.amazon.com/resources/ad-policy/sponsored-ads-additional-policies, read 2026-11-09).

G7. **RULE: The Brand Store Creative deal message in DSP.** Amazon DSP's Brand Store Creative can carry deal messaging (launched Jun 30, 2024). [official] Amazon Ads, "Highlight deals using Brand Store creative", https://advertising.amazon.com/resources/whats-new/highlight-deals-using-brand-store-creative, read 2026-11-09. This is a DSP surface, outside the SP/SB/SD scope of `cx-amazon-ads` except as context.

### H. After the event: retargeting, halo, the extend phase

H1. **GUIDANCE: Amazon's post-event plays.**
- In its hypothetical scenarios, a skincare brand would "Launch Sponsored Display re-engagement campaign to reach gift set buyers to promote core skincare ASINs".
- A fashion brand would shift its messaging from "holiday party looks" to "winter layers".
- Amazon quotes Florian Nottorf (Adference): "Engage warm leads in the week after the event... Use Sponsored Display views remarketing to reengage event browsers and filter by traffic window".
- It quotes Laura Meyer (Envision Horizons): "Refresh Sponsored Brands headlines to highlight your promotions (for example, 'Save on XYZ'). Manually bid on high-ranking and priority shopping queries to continue to reach relevant audiences after the event."

[official, with partner quotes] Amazon Ads, "Post-event advertising strategy", https://advertising.amazon.com/library/guides/post-event-advertising-strategy, read 2026-11-09. After BFCM, Amazon advises remarketing to viewers who didn't buy, promoting complementary products and reviewing top sellers ([official] "Black Friday and Cyber Monday advertising tips"). The holiday guide's third phase is "extend (December and beyond)" ([official] "Holiday advertising guide").

H2. **RULE: The look-back windows a post-event audience can use, in Sponsored Display.**
- Views expressions take `lookback` of 7, 14, 30, 60 or 90 days: `views(exactProduct lookback=30)`, `views(similarProduct ...)`, `views(asinCategorySameAs=... lookback=...)`.
- Purchases expressions take 7, 14, 30, 60, 90, 180 or 365 days: `purchases(relatedProduct|exactProduct ...)`.

[official] Ads API, SD 3.0 OpenAPI, https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml, read 2026-11-09. A views audience built in the week after an event at lookback 7 or 14 contains the event-window viewers. At lookback 30 it still does for roughly a month after the event.

H3. **GUIDANCE: Amazon's measurement view of the halo.** Amazon advises to "Compare activity before, during, and after Prime Day", and points to long-term sales (12 months) and new-to-brand metrics ([official] "Prime Day 2026: Advanced advertising strategies"). The "myths" page names TACOS as the wider lens over a peak ACOS spike: "TACOS reveals whether your total sales (organic and paid) are growing in relation to your ad spend" ([official] "Holiday advertising myths: What experts want you to know"). The author's guide gives the ratio itself: "TACOS shows your ad spend as a percentage of total sales" ([official] "The author's guide to Sponsored Products"; both read 2026-11-09; see B8). How ad-driven sales relate to organic rank is covered in `areas/ads-organic-and-total.md`.

H4. **GUIDANCE: Amazon on what promotions do afterwards.** "Regular promotions can condition customers to wait for deals" ([official] "Sales promotion guide", read 2026-11-09). The remarketing guide and the product promotion guide were read. They repeat the generic remarketing advice and add no event-specific mechanism ([official] https://advertising.amazon.com/library/guides/remarketing and https://advertising.amazon.com/library/guides/product-promotion, read 2026-11-09). Target Promotion, which harvests high-performing targets in Sponsored Products, launched Jul 25, 2024 ([official] "Target promotion for Sponsored Products", https://advertising.amazon.com/resources/whats-new/target-promotion-for-sponsored-products, read 2026-11-09). It is the console's mechanism for moving event search terms into manual campaigns; see `areas/search-terms-and-negatives.md`.

H5. **GUIDANCE: The post-Christmas window in Amazon's words (gap fill 2026-11-09).** None of the Amazon pages read uses the term "Q5". What they do say:
- Phase 3 of the holiday guide: "Phase 3, December and beyond: Keep campaigns running through December to reach last-minute gift shoppers and post-holiday deal seekers. Re-engage visitors who browsed but didn't purchase during peak events and review new-to-brand metrics to turn seasonal buyers into repeat customers." ([official] "Holiday advertising guide", read 2026-11-09.)
- The trends page cites Mintel: "31% plan to do holiday shopping from Cyber Monday through New Year's. This means the window to purchase is stretched across nearly three months". It advises splitting each event into "Lead-up, Peak, and Lead-out phases". It ranks "Gift cards/vouchers 54%" first among 2024 US winter-holiday gift purchases, and says that with Thanksgiving on November 27, 2025, "advertisers can expect a higher concentration of sales in December than before" ([official] Amazon Ads, "Trends for 2025 holiday marketing strategies", https://advertising.amazon.com/library/guides/holiday-shopping-trends, read 2026-11-09). The 31% Mintel figure is the one B8 quotes from the myths page.
- The New Year guide: "It's also important to continue to advertise new products or offer discounts for the New Year in January, as customers are following up on New Year's resolutions". It also names last-minute and belated-gift shoppers "right before the New Year" and Valentine's Day as the next moment ([official] Amazon Ads, "New Year's Ads: 5 Marketing Campaign Ideas to Inspire in 2024", https://advertising.amazon.com/library/guides/new-years-ads, read 2026-11-09).
- The post-event guide's fashion scenario (hypothetical) marks "Extend holiday deals into January and maintain Sponsored Brands investment" as the incorrect answer. The correct ones are, for skincare, a Sponsored Display re-engagement campaign to gift-set buyers, and for fashion, "Reallocate budget toward high-performing branded terms and reposition outerwear with non-holiday messaging", with "January layering" copy ([official] "Post-event advertising strategy", read 2026-11-09). These are Amazon's teaching scenarios, not measured cases.
- B2B: the Amazon Business "Business Savings Event (late December to next January)" (A11).
- Fees and returns that span the window: the US holiday peak fulfilment fee runs to January 14, 2027 (F4), as do the UK and DE festive fees (F9). The trade press reports an Amazon Seller News post of October 16, 2026: items bought on Amazon.com from November 1 to December 31, 2026 can be returned until January 31, 2027 (Apple products until January 15), and "This policy will apply every year" ([opinion, press quoting Amazon] PPC Land, Luis Rijo, "Amazon makes its January 31 holiday return deadline an annual rule", October 20, 2026, https://ppc.land/amazon-makes-its-january-31-holiday-return-deadline-an-annual-rule/, read 2026-11-09; the Seller News post itself was not read). For human readers only.

So Amazon's "extend" phase is defined by the shopper groups it names (last-minute gift buyers, post-holiday deal seekers, peak-event browsers, new-to-brand buyers to retain, January resolution shoppers), not by an auction claim. No Amazon page read says anything about CPCs or competition after December 25.

### I. Attribution lag and report timing around events

I1. **RULE: The data restates.**
- "Initial impression and click data is available using the API within 12 hours. Note that small changes to impression and click data may happen up to three days after the initial click date due to the traffic validation process."
- "Initial conversion data is available within 24 hours, but may change as part of the restatement process. Restatements of conversion data occur 1, 7, and 28 days after the conversion event. Because conversions are reported on the date of the ad interaction, restatement includes all dates in your attribution window. For example, if your attribution window is 14 days, restatement can update attribution up to 42 days (14 plus 28) after the report date."

[official] Ads API, "Reporting v3 FAQ", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/faq.md, read 2026-11-09.

I2. **RULE: Attribution windows by ad product.**
- Sponsored Products uses 7 days for sellers and 14 days for vendors: `purchases7d/14d`, `sales7d/14d`, "[SP: 7d sellers / 14d vendors]" ([official] Ads API, "Purchases (Amazon retail conversions)", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md, read 2026-11-09).
- The v3 `sales` column for SB and SD is "Total value of sales occurring within 14 days of an ad click or view".
- `sales14d` in SP reports "Includes sales attributed to both clicks and views for `vCPM` campaigns, but only sales attributed to clicks for `CPC` campaigns".

[official] Ads API, "Reporting v3 columns", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/columns.md, read 2026-11-09. Depth is in `beyond/metrics-and-attribution.md`.

I3. **RULE: Conversions are dated to the ad interaction ("traffic date") in v1 reporting.** "All conversion metrics are now reported on 'traffic date,' meaning conversions are reported on the date of the ad interaction rather than the date the conversion occurred." [official] Ads API, "Ads API v1 reporting overview", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/overview.md, read 2026-11-09. The deprecations page puts the "Hard shutoff date: Stream Version 1, v3 reporting, and Sponsored Ads v2 reporting will stop delivering data on June 30, 2027" ([official] "Deprecations", read 2026-11-09).

The consequence on an event day: a click on the last event day whose purchase arrives a week later is reported against the event day. The event day's sales figure keeps growing for the length of the attribution window, plus the restatements.

I4. **RULE: Day boundaries follow the campaign's time zone, and hourly data is kept 14 days.** In v1 reporting, "performance is measured and data is aggregated based on each campaign timezone". The worked example maps 11/5/2025 EST to 05:00Z–04:59Z and JST to 15:00Z–14:59Z of the previous day.

Retention and maximum report range by time dimension:

| Dimension | Retention | Max report range |
|---|---|---|
| `hour.value` | 14 days | 14 days |
| `date.value` | 24 months | 120 days |
| `week.value` | 24 months | 15 months |
| `month.value` | 6 years | 25 months |

[official] Ads API, "Dates and historical data retention", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dates.md, read 2026-11-09. Amazon announces events in PDT (A1, A3), so an event's first hours fall on a different report date in campaigns set to other time zones. The hourly read of an event must be pulled within 14 days of it. Date-level reports allow a year-over-year read up to 24 months back.

I5. **GUIDANCE: Read the 7–14-day attribution before changing anything.** "check 7–14-day attribution before making changes. Sales during peak events often occur days after the initial ad click." [official] "Holiday advertising myths: What experts want you to know", read 2026-11-09.

I6. **RULE: Separating deal effect from media effect (AMC).**
- On Oct 20, 2026, the AMC Amazon Retail Purchases dataset added 13 promotional signal columns, with history since Sep 24, 2024. Amazon says these let "advertisers... separate the effect of their media from the effect of their deals".
- On Oct 27, 2026, extended AMC retention for traffic events beyond the default 13 months became generally available, "backfilled with data back to June 2023" and accumulating "up to a maximum of 5 years".
- On Nov 2, 2026, AMC's new-to-brand purchase, unit and sales metric columns began to include modeled conversions (the `new_to_brand` flag already did).
- The promotional columns have a shorter history than the rest of the dataset: "2 years (starting September 24, 2024), not the full 5-year (60-month) window" (dataset page).

[official] Ads API, "Ads API v1 release notes", https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v1.md, read 2026-11-09.

The columns:
- `coupon_discount_amt/id/name/type` (AMOUNT_OFF, PERCENT_OFF).
- `point_of_sale_discount_*` (BUY_X_GET_AMOUNT_OFF, BUY_X_GET_PERCENT_OFF).
- `price_discount_*` (BEST_DEAL, DEAL_OF_THE_DAY, LIGHTNING_DEAL).
- `price_discount_amt` is measured against the "average selling price during the 90 days preceding the promotion start date".
- `unit_price` "Includes price discounts except when price_discount_type = LIGHTNING_DEAL".

Limits:
- The dataset reflects "only vendor or seller self-funded promotions"; Subscribe & Save discounts, Amazon-funded promotions and loyalty or reward points are excluded.
- `net_unit_price` subtracts point-of-sale and coupon amounts, and subtracts `price_discount_amt` only for Lightning Deals.
- It reports the "highest-impacting promotion per type".
- "A blank promotional field... does not mean the discount was zero."

[official] Ads API, "AMC Amazon Retail Purchases (paid)", https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid.md, read 2026-11-09. This is a paid AMC feature, with one window of exception: the page says "Starting June 1, 2026, you can query this dataset at no cost through December 31, 2026 in every region where it is available". It lists the US, CA, JP, AU, FR, IT, ES, UK, DE, MX, BR, NL, SE, PL, BE, AE, SA, TR, EG, IE, ZA, NG, SG and IN marketplaces (gap fill 2026-11-09).

I7. **RULE, as design inputs: what separating a deal's effect from the ads' effect can rest on (gap fill 2026-11-09).**
- The release note's claim, verbatim: "Until now, advertisers could not tell promotional purchases apart from full-price purchases in AMC. With promotional signals, advertisers can separate the effect of their media from the effect of their deals. They can also compare path to conversion and new-to-brand acquisition for promotional and full-price purchases, and see which promotion types and discount depths perform best." ([official] "Ads API v1 release notes", read 2026-11-09.)
- How far the columns reach: they are purchase-level and carry `user_id` ("the user ID of the shopper that purchased the item", type `adUserId`). [seat] That key is what would let an AMC query split ad-exposed from unexposed purchasers within the same days. They cover self-funded coupons, point-of-sale discounts and price discounts only. They report the highest-impacting promotion per type, start September 24, 2024, and treat a blank as unknown, not zero (I6). `price_discount_amt` is measured against a 90-day average, which is not the EU's 30-day legal reference (F10).
- [seat, design reading tied to the research in R7–R9] At a tentpole event the deal, the event's own traffic and the ad change start on the same day. A same-event before/after (the event week against the weeks before it) therefore credits all three to whichever one is being judged. Amazon's own effect figures carry this limit (B10). Two designs are open on what Amazon provides. The first is the AMC split: within the event window, compare promotional and full-price purchases among ad-exposed and unexposed shoppers, using the promotional columns. The second is an event-to-event comparison: the same event in two years, keyed on the event dates (`POST /sp/v1/events`, A12) rather than ISO weeks (J3), with the deal held constant or varied and the ads varied or held constant. Neither design is a randomised test. Design detail is `method/change-measurement.md`'s.

### J. Seasonal search volume and year-over-year alignment

J1. **RULE: Search Query Performance (SQP) periods and limits.** `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT`:
- Availability: sellers with the Brand Analytics role who are registered in Brand Registry. Stores: US, CA, MX, BR, ES, UK, FR, NL, DE, IT, SE, TR, SA, AE, IN, SG, AU, JP.
- Request-only, JSON output.
- `reportOptions.asin` is space-separated with a 200-character limit; `reportPeriod` is WEEK, MONTH or QUARTER.
- "Requests cannot span multiple periods". For WEEK, "dataStartTime must be a Sunday and dataEndTime must be a Saturday". MONTH allows a maximum of 17 months.
- Fields: `searchQuery`, `searchQueryScore`, `searchQueryVolume`; impression, click, cart-add and purchase totals and ASIN shares; `totalMedianClickPrice`, `asinMedianClickPrice` and their purchase-price equivalents; and same-day, one-day and two-day shipping click counts.

The Search Catalog Performance and Search Terms reports follow the same period rules; Search Terms adds DAY and carries `searchFrequencyRank`. [official] SP-API, "Report type values – Analytics", https://developer-docs.amazon/sp-api/docs/report-type-values-analytics, read 2026-11-09.

J2. **RULE: How far back Brand Analytics goes and how fast it arrives.** "Data in Brand Analytics usually goes back three years and is generally available within three days, with quarter-end data typically available within one week." The sentence sits in the page's Demographics-dashboard section, though it is worded for Brand Analytics as a whole; the "Use filters to view data for a specific week, month, or quarter" line before it is about the Demographics dashboard, not SQP. [official] sell.amazon.com, "Brand Analytics", https://sell.amazon.com/blog/brand-analytics, read 2026-11-09.

J3. **RULE: Data Kiosk's year-over-year benchmark aligns by ISO week number, not by event.**
- "Every numeric metric can carry a timeRangeBenchmarking object... WEEK: weekOverWeek, yearOverYear — The preceding Sunday-to-Saturday week; the same ISO week number in the prior year. MONTH: monthOverMonth, yearOverYear — The preceding calendar month; the same calendar month in the prior year."
- "no benchmarking is available at DAY granularity."
- The `startDate` "Must be no more than two years ago".
- The promotion group includes `promotionConversionRate`, `promotionGlanceViewCnt`, `promotionOrderedUnitsWithRevenue`, `promotionOrderedPrice`, `promotionDiscountPct`, `promotionDiscountAmt`, `promotionStartDate`, `promotionEndDate`, `promotionAsinStateType`, `promotionType`, `promotionStatus`, `dealId` and `dealTitle`. The attribute fields "are not additive across periods".
- Returns are computed with a "delay of about 45 days".

[official] SP-API, "Seller analytics dataset guide (Data Kiosk)", https://developer-docs.amazon/sp-api/docs/seller-analytics-dataset-guide, read 2026-11-09. Taken with A2: Prime Day 2026 (June 23–26) fell in ISO week 26 of 2026. ISO week 26 of 2025 is June 23–29, 2025, two weeks before Prime Day 2025 (July 8–11, ISO week 28). A week-level `yearOverYear` benchmark therefore compares an event week with a non-event week whenever the event moves week. By contrast, PBDD fell in ISO week 41 in both 2025 (Oct 7–8, the date a seller gives on the Holiday 2026 forum thread; Amazon's pages read here do not state the 2025 dates) and 2026 (Oct 6–7), and Black Friday in ISO week 48 in both years [seat, computed from the dates above]. Data Kiosk weeks run Sunday to Saturday while ISO weeks run Monday to Sunday, so how the two week definitions match up at the edges is not stated on the page.

J4. **RULE: Amazon's own forecasters treat the event's moving week as a special case.** "There's a special construction to the [Prime Day] forecast. It's a different week of the year than every other year," and "The dates that Prime Day falls on, as well as the types of deals available, change from year to year." (Abhishek Gupta, SCOT demand forecasting.) [official] Amazon Science, "How events like Prime Day helped Amazon navigate the pandemic", https://www.amazon.science/latest-news/how-peak-events-like-prime-day-helped-amazon-navigate-the-pandemic, read 2026-11-09.

## What practitioners add

Everything in this section is [opinion]: what a named practitioner, agency or vendor says. The data behind it is their own client book or platform, not a controlled sample. The dates are those of the page.

### 1. The ramp before the event

- **Florian Nottorf (Adference), quoted on Amazon's Prime Day guide:** "Traffic doesn't spike before Prime Day, but it does grow... Are any marked 'limited by budget'?... Start scaling budgets 3–5 days ahead of Prime Day and go for 20–30% increments", and "keep budgets open, especially for branded and non-branded search campaigns with strong ROAS." (Amazon Ads, "Prime Day 2026: Advanced advertising strategies", read 2026-11-09.)
- **Ad Badger ("The Badger"), "Prime Big Deal Days 2026 PPC Playbook: Bids & Budgets"** (published 2026-09-25, modified 2026-10-20 per the page metadata; https://www.adbadger.com/blog/prime-big-deal-days-ppc-strategy/, read 2026-11-09). Its calendar:
  - Phase 1, "now to October 3": save a CPC baseline, clean negatives from the last 60 days of search terms, and rebuild break-even ACOS on discounted ASINs.
  - Two days before (Oct 4–5): raise budgets 1.5–2.5x. "Starting about 48 hours before a Prime event, we consistently see impressions rise while clicks and conversions stay flat, so ACoS jumps."
  - "Leave most bids alone. Paying event-level CPCs for window shoppers is the most common way sellers burn budget before the event even starts."
  - "Much of the traffic you buy on October 4–5 converts on October 6–7".
  - Push only ASINs that "can survive a sales spike of 2x or more without stocking out."
- **Ad Badger's worked example of how a deal moves break-even ACOS:** a $30 product with a 30% margin before ads has a 30% break-even ACOS. Discounted 20% to $24, the margin falls to about 12.5%, and so does break-even ACOS. The formula itself belongs to `beyond/goals-and-economics.md`.
- **Amazon's "boost seasonal sales" peer tips** (Amazon Ads, read 2026-11-09):
  - Joie Roberts: "launch my first holiday advertising campaigns right after Halloween"; "I check and adjust on Friday mornings and Mondays".
  - Bryan Cohen (Best Page Forward, an author-marketing coach) judges how profitable each book is "after receiving 100 clicks"; the advice is written for KDP authors.
  - Gavin Cheung (MotionGrey) is also quoted.
- **Laura Meyer (Envision Horizons), quoted by Amazon:** "Review all budget caps (account-level caps, portfolio caps) a week before the event and take screenshots for your records. Uncapped budgets can lead to spending more than bargained for." (Amazon Ads, "Post-event advertising strategy".)
- **Where they disagree.** Amazon's holiday guide and Nottorf say +20–30% starting 3–5 days out. Ad Badger says 1.5–2.5x from two days out and 2–3x on event days. The Marketplace Ad Pros data in section 2 found no lift difference between budget raisers and holders.

### 2. During the event: budgets, bids, CPC

- **Ad Badger** (as above):
  - "Our standing Prime Day recommendation is 2–3x normal budgets on event days."
  - Bids: "+10% across the board" and "+50–100% on your tagged top converters only".
  - Placements: "Use a placement adjustment on your top converters instead of raising base bids on everything".
  - "Don't make pause decisions during the event. Same-day ACoS on October 6 is missing most of the sales those clicks will eventually generate."
  - Its five-year app averages for July Prime Day ("the October event is smaller"): clicks about +70%, sales about +130%, daily spend about +78%, CVR about +35%, ACoS 31% to 25%. Its CTR figure, from July 2019, went from 0.37% to 0.19%.
  - The CPC/bid ratio test: "Divide average CPC by max bid for your high-volume keywords over the last 30 days. If the ratio sits around 0.90–1.00, you're effectively paying your own bid... If it sits around 0.50–0.75, you still have headroom."
  - It ties this to the FTC complaint, which alleges "that prices rose far more around Prime Day and Black Friday, ramped in gradually beforehand", and advises: "Export weekly CPC by campaign now, before the ramp".
- **Marketplace Ad Pros, "Prime Day 2026 Ad Benchmarks"** (modified 2026-09-30; https://marketplaceadpros.com/guides/amazon-prime-day-2026-ad-benchmarks/, read 2026-11-09). Several hundred US advertisers, each compared against matched Tue–Fri days from the two weeks before the pre-event ramp.
  - Median SP ad sales +30%; total sales +37% (in the 43% subset with Seller Central data); 76% of advertisers grew.
  - 75% spent more on SP, but only 13.7% raised budgets by 20% or more, and 51% cut budgets. Raisers and holders both showed a 1.30x lift (their caveat: correlational).
  - Median SP CPC rose 10% ($1.19 to $1.31); SB CPC rose 2% ($1.18 to $1.20). SP ACOS went from 33% to 35%.
  - SD spend fell 17% and impressions 37%, while ACOS improved from 34% to 25%. SD CPC is omitted because it blends cost types.
  - Spread: SP spend ran p25 1.00x to p75 1.87x; ad sales p25 0.89x to p75 1.95x.
  - 76% launched new campaigns and 53% advertised new products. Median SP spend index by category ranged from Electronics 1.78x to Office Products 1.03x.
  - Attribution: about 95% mature in their pull; "June 26 clicks fully mature around July 10".
- **Skai, "Prime Day 2026 Preview: 7 Shifts From 2025"** (https://skai.io/blog/prime-day-2026-preview-7-shifts-from-2025-to-guide-your-2026-playbook/, read 2026-11-09). A same-store cohort on Skai's platform, for Prime Day 2025:
  - CPC was $1.80, down 10.4% from $2.01 in 2024. CTR was 0.32% versus 0.24%.
  - Daily spend ran nearly 3x the 30-day baseline. Against that baseline, clicks were +108%, impressions +114% and conversions +153%.
  - Year-over-year by half (Day 1 of 2024 against Days 1–2 of 2025; Day 2 of 2024 against Days 3–4 of 2025): first half spend +19.6%, clicks +26.1%, CPC −5.2%; second half spend +0.3%, clicks +19.7%, CPC −16.2%.
  - Spend share 2023 / 2024 / 2025: DSP 8.7% / 13.6% / 15.6%; SB 17.4% / 14.5% / 10.9%; SD 3.3% / 2.6% / 1.3%; SP 71.6% / 69.2% / 72.0%.
  - Discounting, citing Momentum Commerce: 25.6% of US products were discounted versus 23.6%, at an average depth of 21.7% versus 24.4%.
  - Skai advises: "Broaden targeting during peak windows."
- **Tinuiti, "Prime Day 2026: Record Sales Meet Shifting Consumer Baskets"** (Joe O'Connor and Andy Taylor, July 1, updated July 16, 2026; https://tinuiti.com/blog/amazon/prime-day-recap/, read 2026-11-09):
  - Total Amazon ad spend +19% YoY. Amazon DSP +59%, at 35% of spend.
  - Day 1 took 28% of spend (31% in 2025). Day 1 SP sales ran more than 300% above the Q2 daily average.
  - Share of sales: day 1 fell from 34% to 31%, while the last day rose from 23% to 27%.
  - Excluding event days from both years, SP growth was 23%, against 38% for the quarter.
  - DSP spend peaked on the final day at more than 300% of day one of the quarter, and stayed elevated over the weekend after for retargeting.
  - Market context it cites: Adobe, $26.4B online and +9.3%; Numerator, AOV −11%. Apparel was hurt by the event's closeness to Father's Day, and Tinuiti expects a softer Q3 YoY.
- **Acadia, "Amazon Prime Day 2026 – The Results"** (July 1, 2026; Ross Walker, Michael Childers and Meg Scavo; https://acadia.io/amazon-prime-day-2026-the-results/, read 2026-11-09):
  - Revenue +23% YoY across clients. Days 2 and 3 grew most (+30% and +28% versus PD 2025), and the four-day curve was "strikingly flat".
  - Incrementality: "trust the YoY growth number this year, not the period-over-period lift, and don't compare this June's incrementality against last July's". The reason given is that the 2025 baseline was "the sleepy, travel-heavy week after the Fourth of July". Daily sales ran "roughly 185% above the pre-event run rate".
  - Agency ad spend +24% YoY. Ad conversion was "very high on Day 1, then eroding through the middle days... Day 4 ad conversion running well below Day 1".
  - Sponsored prompts: spend +600% against the prior period. Prompt engagement converted at about 12%, against about 17% for standard sponsored ads.
  - Amazon changed its merchandising mid-event: "home-page banners and modules shifted from bright blue to bold red".
- **Pacvue** is cited by others: "average CPCs increased as much as +70% compared to the year prior" (Acadia's Prime Day 2024 recap, kept further down the same page, so Prime Day 2024 against 2023), and Pacvue's Q3 benchmarks show "an 18% YoY CPC increase on Sponsored Products" (Pare, 2026-10-08). Pacvue's own page returned 403 (see Unreachable).
- **Pare, post-PBDD** (George Reid, 2026-10-08; https://pare.so/blog/amazon-prime-big-deal-days-post-event-ppc-rank-dsP-strategy-2026, read 2026-11-09): PBDD 2026 Day 1 came in "nearly 30% ahead of last year's comparable event". Pare writes that some categories ran CPCs "16% to 100% above normal" and cites Brandon Fishman's analysis for the same range.
- **Where they disagree on CPC.** Skai saw a lower CPC in Prime Day 2025 than 2024 (−10.4%). Marketplace Ad Pros saw median SP CPC at Prime Day 2026 +10% against the pre-event baseline. Pare and Fishman cite 16–100% above normal for PBDD 2026. These measure different things (YoY event-to-event, event-to-baseline, category ranges) on different books. No two of them are comparable.

### 3. Deals and promotion mix

- **Acadia:** "Prime Exclusive Discounts (PEDs) were the core recommendation and dominant tactic, with coupons as the fallback for brands that couldn't meet PED price floors". "We had essentially no brands running Lightning Deals or Spotlight Deals."
  - Tiering: hero ASINs at 30–40% off, the rest of the catalog at 15–20%.
  - On badges: "discounts could still display to customers even when the backend showed a pricing requirement issue, but the stronger event badge would not show."
  - "because PEDs refresh on a 24-hour cycle, holding off on correcting reference-price errors until closer to the event paid off".
  - Deals for the June event were "locked to an April 30 deadline". Some brands had to cut planned promotional pricing right after the Big Spring Sale "to establish a clean reference price".
  - Shoppers saw a new price-history tool showing "the item's 30-day pricing range". Amazon's own page says "up to 365 days of pricing insights" (A1); the two descriptions differ.
- **Ad Badger,** citing EcomCrew's summary of the seller notice, says PBDD promotional prices are excluded from the 30- and 60-day lookbacks for BFCM deal prices. This matches F4.

### 4. After the event: retargeting, halo, how long to wait

- **Ad Badger:**
  - "Bring budgets down to about 1.5x on October 8 and back to normal by October 10. Return bids to pre-event levels on October 8."
  - "A short Sponsored Display retargeting push over October 8–14". It cites Numerator: 56% of event shoppers compared prices or products with other retailers.
  - "Book your real post-event review for October 21", that is, 14 days later.
  - "A successful Prime event often shows a higher ACoS alongside a lower TACoS... compare organic sales in the two weeks after the event against the two weeks before."
- **Pare:**
  - Hold ad-driven velocity for 48–72 hours after the event, because "Amazon's ranking signals take days to consolidate".
  - Launch DSP retargeting on event-window detail-page viewers "timed to fire 20–30 days post-event".
  - Pare says that most brands put less than 1% of ad budget into SD and DSP retargeting.
- **Acadia:**
  - "Be skeptical of expensive lead-out media for everyone else... for most brands, dollars spent during the event return far more than dollars spent after it. Going-dark tests across brands large and small show consistently thin post-event lift over baseline."
  - The exceptions it names: defending organic rank actually won, and relaunching Brand Tailored Promotions (about 42% of its clients) to lapsed customers, cart abandoners and complementary-product buyers.
- **Halo for non-participants (Acadia):** "a 46% lift for non-participants last year, 116% the year before... That free ride is disappearing... The halo has become a penalty for opting out." Acadia gives no 2026 figure for non-participants.
- **Where they disagree.** Pare says hold spend for 48–72 hours and retarget at 20–30 days. Ad Badger says taper from the day after and retarget for days 1–7. Acadia says trim post-event media to the minimum. Florian Nottorf (Adference), quoted in Amazon's post-event guide, says "Engage warm leads in the week after the event is over". None of the three practitioners publishes a controlled comparison. Acadia's "going-dark tests" are the only claim of a test, and the page does not publish them.

- **Brand Tailored Promotions, practitioners (gap fill 2026-11-09).**
  - Acadia's Prime Day 2026 recap names the relaunch of BTP (about 42% of its clients) to lapsed customers, cart abandoners and complementary-product buyers as one of the lead-out uses it supports (section 4).
  - Intentwise (Explained: What is Brand Tailored Promotions?, published 2023-08-14, modified 2026-07-02, https://www.intentwise.com/blog/brand-tailored-promotions-explained-tips-best-practices, read 2026-11-09) quotes Joe Stefani (Desert Cactus), testing since mid-July 2023: "recent customers have a roughly 3x higher percentage share of redemptions than the next most-engaged audience, repeat customers". It quotes Liran Hirschkorn (Incrementum Digital) on cart-abandoner promotions: "a lot of these sales you would not have gotten". Neither gives the data behind the claim.
  - Intentwise lists the drawbacks. BTP can combine with a coupon or deal already running. The promotions were "only available at the brand level" (written in 2023; Amazon's 2026 page offers ASIN-level promotions, F7, so this one is out of date). And shoppers get no notification: the promotion shows as a green "Follower promo" or "Exclusive promo" badge where the shopper already browses. "Sponsored Products ads can also help move the needle here. They allow the coupon to be seen on the search results page."
  - Where they disagree: Stefani reads recent customers as the strongest audience, while "a lot of agencies and brands are excited about the cart abandonment audience" (Intentwise). No one publishes an incremental-sales test of a BTP audience against a holdout.

### 5. Attribution lag as practitioners see it

- **Ad Badger:** "Sponsored Products and Sponsored Brands use a 14-day click attribution window... a keyword that looks like a 60% ACoS loser on day 5 can finish as a 22% ACoS winner on day 14." This conflicts with Amazon's documentation for sellers, where SP uses a 7-day window (I2). For a seller, the SP window is 7 days; for a vendor, 14. Restatement continues up to 28 days after the conversion either way (I1). The same page says "Amazon's reports are built by order date", which conflicts with Amazon's statement that v1 reports date conversions to the ad interaction (I3).
- **Acadia:** "data attribution was noticeably less laggy than in prior years. Near-real-time spend data made it far easier to push or pull ad aggressiveness... without bracing for a TACoS jump once the data fully baked."
- **Marketplace Ad Pros:** "June 26 clicks fully mature around July 10", 14 days after the last event day.
- **Joe Shelerud (Ad Advance), quoted on Amazon's "myths" page:** "impressions can surge by double digits while conversion rates stay flat or even decline". On the same page Adam Mellott (BTR Media) is quoted on reading a short-term ACOS climb against total sales. Ritu Java (PPC Ninja, on small budgets and long-tail keywords), Alessandro Carnati (Digital Turnover, on AMC insights) and Jérôme de Guigné (e-Comas, on Sponsored TV and brand searches) are quoted on other topics, not on ACOS against TACOS.

### 6. What practitioners say about the auction, and what the record shows

The FTC and 22 states allege that Amazon raised reserve-price "surcharges" during high-velocity events and ramped them in ahead of peaks (E3). Amazon says reserves are set in real time, that no one can predict them, and that no advertiser ever pays above their bid (E1). Texas, in its separate suit, alleges that soft reserves push the winner's cost toward its maximum bid by "roughly 17% on ordinary shopping days and more than 25% during peak events like Prime Day", and that advertisers "pay their own bid nearly 80% of the time" (E3). Ad Badger's practical response is to log a CPC baseline and the CPC/bid ratio before the ramp (section 2). This seat found no practitioner dataset that separates reserve effects from competition effects at an event.

### 7. "Q5": December 26 to mid-January (gap fill 2026-11-09)

"Q5" is a practitioners' name; no Amazon page read uses it (H5).
- **Evolve AMZ (Ian Smith), "Amazon Q5 Explained: The Cheapest Traffic of the Year"** (published 2026-09-08, https://evolveamz.com/amazon-q5-strategy-2026/, read 2026-11-09).
  - Definition: "the informal fifth quarter, running from roughly December 26 to mid-January. Defined by the exit of seasonal advertisers after the final shipping cutoff, combined with continued consumer demand driven by gift card redemption, self-purchase and returns-related browsing. Not an official Amazon term".
  - Its figures: "CPMs commonly fall 28% or more against the Q4 peak"; gift cards are "something in the region of 39 to 50% of total holiday budgets, and redemption concentrates between December 26 and mid-January"; "Roughly 74% keep shopping past the holiday cutoff". The page links Ad Badger and a Tinuiti benchmark index for some numbers. The 28% CPM figure carries no dataset this seat could trace.
  - Its counterpoint, which it calls "the catch": "Benchmark data shows January 2026 carried the highest ACoS of the year at 32.50%, against October's low of 28%". "Cheaper impressions do not automatically mean cheaper sales", because "December 19 to 31 traffic is overwhelmingly self-purchase and gift card redemption rather than gift-giving" and "average order values are lower, browsing is heavier".
- **Ad Badger, "Amazon Advertising Benchmarks 2026: Stats Every Seller Needs"** (published 2026-03-10, modified 2026-09-15, https://www.adbadger.com/blog/amazon-advertising-stats/, read 2026-11-09). The source of Evolve's ACoS point: "January 2026 had the highest ACOS of the year at 32.50% and October 2025 had the lowest ACOS of the year at 28%". Its 2026 platform averages are CPC $1.22 and ACOS 29.6% ("Source: Ad Badger app data, January–August 2026"). Its monthly CPC series is not in the page text read. For human readers only.
- **Intentwise (Michael Waters), "Guide: Ad tactics for the week after Christmas"** (December 17, 2023, modified 2026-07-20, https://www.intentwise.com/blog/tactics-for-week-after-christmas, read 2026-11-09). From Intentwise's own data: "Conversion rates were 13.4% for the week ending on December 23. The following week, however, conversions fell to 11.03%." It cites "one study" (unnamed) for "as much as 27% of holiday shoppers start spending their gift card money in the week after Christmas". It advises comparing against "your own sales and advertising data during the same week last year", running deals on overstocked items, and shifting spend to New Year's-resolution categories.
- **Pattern, "Amazon Advertising Post-Holiday: Where to Focus Now"** (page dated December 21, 2021; schema dateModified 2026-08-14; https://www.pattern.com/blog/amazon-advertising-post-holiday-where-to-focus-now, read 2026-11-09). Pattern asserts, without data: "there will be less traffic to capture and less competition for ad space. You'll start to see your CPCs go down"; "many shoppers will be cashing in on their holiday gift cards ... ramp up your retargeting campaigns"; "many brands have used up their December ad budget by now".
- **Teikametrics (Andrew Waber), in MarTech, "Amazon ad spend rises over Cyber 5, but most efficient sales days still ahead"** (December 12, 2019, https://martech.org/amazon-ad-spend-rises-over-cyber-5-but-most-efficient-sales-days-still-ahead, read 2026-11-09). This covers the weeks before Christmas, not Q5: "across a same-set of more than 700 Amazon sellers, ad conversion rates continue to rise from Cyber Monday all the way through the Dec. 22 shipping cutoff. Yet, the average cost-per-conversion declines over the same period". Waber attributes this to brands that "blow through a fixed budget for the season" and then taper. Over Cyber 5, spend rose "92% from pre-holiday levels on average" while "CPCs either remained flat, declined, or rose at a level far below the corresponding spend increase".
- **Pacvue and Helium 10, "Q4 2025 Retail Media Benchmark Report"** (PDF, January 2026, https://www.helium10.com/app/uploads/2026/01/2025-SMB-Q4_Benchmark_Report.pdf, read 2026-11-09). Its text says Q4 2025 gains "came from stronger conversion and engagement at a time when CPCs often remained stable or declined", and that "Sponsored Brands ROAS almost reached parity with Sponsored Products ROAS—and even surpassed it during Cyber 5". The basis is "thousands of advertisers utilizing Pacvue's platform". Its weekly CPC charts are images, with no post-Christmas figure in the text.
- **Where they disagree.** Pattern and Evolve say CPC or CPM falls after Christmas. Ad Badger's data has January as the year's worst ACOS month, and Intentwise's has conversion falling about 2.4 points in the week after Christmas. Both sides can be true at once (cheaper traffic, lower conversion), and Evolve says exactly that. No one read publishes a CPC series for December 26 to January 15 against the weeks before, by category, with its sample.

### 8. EU pricing and deal claims (gap fill 2026-11-09)

- **Omnia Retail, "Black Friday Pricing Data Report: What 60,000 Products Tell Us About Retailer Behavior"** (updated October 2, 2026, https://www.omniaretail.com/blog/black-friday-pricing-data-report-2025, read 2026-11-09). Six weeks of daily prices around Black Friday 2025 for about 60,000 products in Germany and the Netherlands, across all retailers it tracks (not Amazon alone). Prices fell "steadily from the very start of the six-week window", and recovered to an index of about 102–103 within a week. Sporting Goods prices "climbed up in the first couple of weeks of the window, peaking roughly a month before Black Friday, before dropping sharply in the final two weeks". It advises "checking any deep Black Friday cut against your own 30-day price history before it goes live", citing the Omnibus Directive.
- This seat found no named Amazon practitioner publishing data on how the EU 30-day rule changed deal eligibility, deal badges or ad savings claims on Amazon's EU stores.

## Published research

Everything here is [research]. Where a paper was not opened in full, this file uses only its abstract (marked).

R1. **Pre- and post-promotion dips exist but are hidden in store-level data.** Van Heerde, Leeflang and Wittink (2000), "The Estimation of Pre- and Postpromotion Dips with Store-Level Scanner Data", *Journal of Marketing Research* 37(3), doi:10.1509/jmkr.37.3.383.18782 (abstract via Crossref, read 2026-11-09).
- Store-level scanner data for tuna and toilet tissue, with distributed lead and lag models (Almon, unrestricted dynamic effects, exponential decay).
- Four discount types: unsupported, display-only, feature-only, feature and display.
- They "estimate the dip to be between 4 and 25% of the current sales effect", and note that dips are "difficult to detect by traditional models (and by a visual inspection of the data)".
- Transfer to Amazon: the category is storable goods offline. It shows that a dip after an event can be real while invisible to a simple before/after comparison. A post-event week on Amazon carries a dip, retargeting, and the halo all at once.

R2. **Stockpiling also brings benefits.** Ailawadi, Gedenk, Lutzky and Neslin (2007), "Decomposition of the Sales Impact of Promotion-Induced Stockpiling", *JMR* 44(3), doi:10.1509/jmkr.44.3.450 (abstract, read 2026-11-09).
- The benefits of stockpiling are "substantial": in order of importance, increased consumption, then preemptive brand switching, then repeat purchases. They "easily offset" the purchase acceleration by loyal customers.
- Transfer: on Amazon, a deal on a consumable can pull demand forward (the "five bottles of sunscreen" Acadia describes) and also take future purchases from competitors. Which dominates is category-specific.

R3. **Long-term promotion sensitivity.** Mela, Gupta and Lehmann (1997), "The Long-Term Impact of Promotion and Advertising on Consumer Brand Choice", *JMR* 34(2), doi:10.1177/002224379703400205 (abstract, read 2026-11-09).
- 8¼ years of panel data for a frequently purchased packaged good.
- "consumers become more price and promotion sensitive over time because of reduced advertising and increased promotions."
- Transfer: this is the academic form of Amazon's own line, "Regular promotions can condition customers to wait for deals" (B11). It concerns consumer response over years, not a single event.

R4. **Causal impact of an intervention under seasonality.** Brodersen, Gallusser, Koehler, Remy et al. (2015), "Inferring causal impact using Bayesian structural time-series models", *Annals of Applied Statistics* 9(1), doi:10.1214/14-aoas788 (abstract, read 2026-11-09).
- It proposes a state-space model that builds a synthetic counterfactual from covariates and can "flexibly accommodate multiple sources of variation, including local trends, seasonality and the time-varying influence of contemporaneous covariates".
- It was demonstrated on an online ad campaign's effect on search-related site visits.
- Transfer: this is the method family for reading an event's lift for one seller against a counterfactual built from its other ASINs or from category search volume (SQP), rather than against the week before. Design detail belongs to `method/change-measurement.md`.

R5. **Amazon's own peak forecasting.** Amazon Science, "Peak period demand forecasting with proxy data: GNN-enhanced meta-learning" (publication page, https://www.amazon.science/publications/peak-period-demand-forecasting-with-proxy-data-gnn-enhanced-meta-learning, read 2026-11-09). It uses non-peak proxy data to forecast peak-event demand. The publication page's abstract reports the model outperforming baselines "by 26.24% on the in-ternal vending machine dataset and 8.7% on the public JD.com dataset over the Mean Absolute Error" (WACV 2024 Workshop on Physical Retail AI). Transfer: peaks are forecast as a distinct regime from normal weeks, and Amazon's SCOT team says each Prime Day needs a "special construction" (J4).

R6. **What the complaint's internal documents describe (a legal filing, not research).** The internal memo the complaint quotes says: "Perceptibility is affected by seasonality and reporting frequency/aggregation" and "seasonal fluctuations in competition and reporting lag would obfuscate changes to the incentives in the auction" (¶223). This is an allegation (E3). It is listed here only because it states, from inside the auction team as alleged, the measurement problem this file describes: an event's CPC change cannot be read cleanly from seller reports.

R7. **Advertising and price sensitivity: three empirical generalizations (gap fill 2026-11-09).** Kaul and Wittink (1995), "Empirical Generalizations About the Impact of Advertising on Price Sensitivity and Price", *Marketing Science* 14(3, supplement), G151–G160, doi:10.1287/mksc.14.3.g151 (abstract via Crossref, read 2026-11-09).
- A review of prior marketing studies, whose "seemingly conflicting results" the authors reconcile into three generalizations: "(1) an increase in price advertising leads to higher price sensitivity among consumers, (2) the use of price advertising leads to lower prices, and (3) an increase in nonprice advertising leads to lower price sensitivity among consumers." "Managers need to coordinate their advertising and pricing decisions to attain maximum profits."
- Transfer: the data is the offline literature to 1995, with advertising split into price and non-price messages. On Amazon, every SP placement shows the price, and deal badges, REC deal badging and the SB deals CTA (G1, G2) make an event ad a price message [seat]. Read through R7, the advertising at an event is the kind that raises shoppers' price sensitivity. Brand-building formats (SB video, Store, Sponsored TV) are the closer analogue of non-price advertising [seat]. No Amazon study of this split was found.

R8. **Long-run effects of the marketing mix: discounting has the smallest total effect, and its long-run share is the smallest (gap fill 2026-11-09).** Ataman, van Heerde and Mela (2010), "The Long-Term Effect of Marketing Strategy on Brand Sales", *Journal of Marketing Research* 47(5), 866–882, doi:10.1509/jmkr.47.5.866 (abstract via Crossref, read 2026-11-09).
- Data and method: "a multivariate dynamic linear transfer function model to five years of advertising and scanner data for 25 product categories and 70 brands in France."
- Findings: "the total (short-term plus long-term) sales elasticity is 1.37 for product and .74 for distribution. Conversely, the total elasticities for advertising and discounting are only .13 and .04, respectively." "The long-term effects of discounting are one-third the magnitude of the short-term effects. The ratio is reversed from other aspects of the mix (in which long-term effects exceed four times the short-term effects)".
- Transfer: these are mature packaged-goods brands in French retail. On Amazon, "product" and "distribution" map loosely to listing quality and to stock and Featured Offer availability [seat]. The finding that bears on events is the ratio: a deal's sales effect is mostly short-term, while advertising's is mostly long-term. A same-week reading of an event therefore overstates the deal's share of what lasts, and understates the ads' share [seat]. Amazon's own "long-term sales" metric (B2, H3) is the closest seller-side read of the second part.
- The authors' companion paper on new brands (Ataman, Mela and van Heerde 2008, "Building Brands", *Marketing Science* 27(6), 1036–1054, doi:10.1287/mksc.1080.0358, abstract) finds, across 225 launches in 22 categories, that distribution breadth and product innovation give "greater marginal increases in sales for new brands than either discounting, feature/display, or advertising" (abstract read 2026-11-09).

R9. **Advertising shifts the whole demand curve, so a price-elasticity reading alone misleads (gap fill 2026-11-09).** Erdem, Keane and Sun (2007), "The Impact of Advertising on Consumer Price Sensitivity in Experience Goods Markets", SSRN working paper, doi:10.2139/ssrn.965468 (abstract via Crossref, read 2026-11-09).
- Nielsen scanner panel data for toothpaste, toothbrushes, detergent and ketchup. Advertising raised marginal consumers' willingness to pay "for 17 of the 18 brands"; "a decrease in the equilibrium price is perfectly consistent with a scenario where advertising actually raises each individual consumer's willingness to pay". "To understand how advertising affects consumer price sensitivity one needs to estimate how it shifts the whole distribution of willingness to pay". Heinz ketchup was the exception.
- Transfer: an event's lower price and higher ad spend move demand together. A rise in measured price elasticity at an event does not by itself show that the ads made shoppers more price-sensitive [seat].

R10. **What R7–R9 mean for reading an event (gap fill 2026-11-09) [seat].** The research measures ad-by-price interaction on panel and scanner data with long series and many brands. A single seller's event has one deal, one ad plan and one event's traffic, starting on the same day. The interaction cannot be estimated from that event's before/after. It can be estimated only where one of the three varies while the others do not: across shoppers within the event (the AMC promotional columns, I7), or across events (the same event in two years, keyed on event dates, J3, A12). R1's dips and R2's stockpiling sit on top: the weeks after an event carry the deal's pull-forward as well as any ad carry-over. Brodersen et al.'s counterfactual method (R4) is the tool for the across-time case.

Not found: a published, peer-reviewed study of sponsored-ads CPC or ROAS on Amazon during tentpole events, or of the interaction of Amazon deals and sponsored ads. The figures above are vendor aggregates.

## Stable enough for a skill

Each item is a mechanism or definition that held across the pages read. A skill can rely on it, but reads the figures it carries at run time.

1. **Event dates come from Amazon and move every year.** Since 2019 Prime Day has started in five different ISO weeks (25, 26, 28, 29, 42) and run at two lengths (48 hours 2019–2024, 96 hours from 2025). The 2026 event ran June 23–26 outside AU/BR/IN/JP, while JP ran July 10–13. Black Friday Week dates were still unannounced on 2026-11-09, and JP's will be announced on Nov 19. Sources: "The history of Prime Day"; "Prime Day 2026 date"; "When is Amazon Black Friday"; aboutamazon.jp "Amazon ブラックフライデー 2026"; Impress Watch.
2. **The SP API carries the event list, with an id per event, and recommends per-campaign events with a suggested budget-increase percent.** `POST /sp/v1/events`; `POST /sp/campaigns/budgetRules/recommendations` with `EVENTS_FOR_EXISTING_CAMPAIGN`. Sources: SP 3.0 OpenAPI; "Budget rules overview".
3. **An event-type budget rule can exist before its dates are announced, and Amazon fills the dates in later.** Recommended events exist for SP and SB only. Sources: "Schedule-based budget rules"; SP 3.0 OpenAPI (`eventTypeRuleDuration`).
4. **Schedule bid rules can raise a base bid by 1–100% for an event id or a date range.** "Recurring Events" are JP only; "Individual Events" are worldwide. Sources: SP 3.0 OpenAPI (`/sp/rules/optimization`); "Event-based bid rules for Sponsored Products advertisers".
5. **Theme-based bid suggestions have event themes** (`PRIME_DAY`, `FALL_PRIME_DEAL_EVENT`, `BFCM_HOLIDAY`), and the keyword recommendations have a `SPECIAL_DAYS` theme. The impact estimates assume the campaign does not run out of budget. The Ads API v1 spec carries the same four themes in its unified bid recommendation (`Bid.theme`) and a `KEYWORDS_RELATED_TO_PRIME_DAY` theme target that matches queries only "through the end of Prime Day". Sources: SP 3.0 OpenAPI; "Theme-based bid suggestions quickstart guide"; Ads API v1 merged OpenAPI.
6. **When a campaign runs out of budget on an event day, its ads pause until midnight. The daily budget can be exceeded by up to 100% on one day within the monthly average.** Sources: sell.amazon.com "Prime Day tips"; "Sponsored ads daily budgeting policy and options".
7. **The budget recommendation reports the share of time a campaign was in budget and its estimated missed impressions, clicks and sales over seven days.** Source: SP 3.0 OpenAPI (`/sp/campaigns/budgetRecommendations`).
8. **CPC at a peak is bounded only by the bid.** Amazon's help wording, as quoted in the complaint, says a placement "may have a different value during a peak shopping period than a non-peak period" and that the price "will never exceed the maximum bid you authorize"; Amazon's FTC response says "In no scenario does an advertiser pay more than their bid." Sources: the help-page wording quoted in FTC et al. v. Amazon ¶¶147–148; Amazon's FTC response.
9. **Event-day conversions keep arriving after the event and restate for up to 28 days.** SP sellers use a 7-day window, vendors 14; SB and SD use 14. Conversions are dated to the ad interaction. Sources: "Reporting v3 FAQ"; "Purchases (Amazon retail conversions)"; "Reporting v3 columns"; "Ads API v1 reporting overview".
10. **Report days follow the campaign time zone; events are announced in PDT; hourly data is retained 14 days.** Sources: "Dates and historical data retention"; aboutamazon event pages.
11. **Deal types, eligibility and visibility.** Lightning Deals run 4–12 hours as Amazon sets them; Best Deals run several days. Deals require a four-star rating, coupons 3.5 stars; coupons expire after 90 days; price discounts run up to 30 days. Deals and coupons appear in search results, on detail pages and on the Deals page. Sources: sell.amazon.com "Seller promotions"; "Prime Day tips".
12. **Deal deadlines and fees for an event are announced per season.** For holiday 2026: PBDD deals July 8–Sep 8; BFCM July 8–Oct 20; $100 per promotion plus 1.5% capped at $5,000. PBDD prices are excluded from the BFCM 30/60-day lookbacks. Source: Seller Forums "Holiday 2026: Same fees, same eligibility, earlier deadlines".
13. **Deals surface in ads automatically, by mechanism.** REC renders a deal badge (and the BFCM badge) for qualifying deal types on the "Shop now" variation. The SB product collection shows a deals CTA. Brand Stores get an All Deals page and the Featured Deals widget. Sources: "Holiday shopping season performance-boosting tips"; "Black Friday and Cyber Monday advertising tips"; "Key events store prep".
14. **Ad policy on deals.** The advertised deal must be live while the ad runs (no teasing). Ad and landing page must carry the same price or savings format. Event names are bounded by duration. "Up to X%" needs at least 10% of the selection at or above X. A REC headline carries no price or deal. Store messaging needs the FDW with at least four ASINs. Source: "Black Friday and Cyber Monday advertising tips"; "Holiday shopping season performance-boosting tips".
15. **The Promotions API lists a seller's promotions with type, status, schedule, `eventId`, Prime-exclusive segment, display flag and fee snapshot.** Source: amzn/selling-partner-api-models `promotions_2025-12-01.json`.
16. **SQP and the Brand Analytics reports run on Sunday–Saturday weeks, calendar months or quarters, and cannot span periods. Data Kiosk's YoY benchmark compares the same ISO week number or the same calendar month,** so a moving event breaks week-on-week YoY alignment. Sources: SP-API "Report type values – Analytics"; "Seller analytics dataset guide"; sell.amazon.com "Brand Analytics".
17. **A post-event Sponsored Display audience can reach event-window viewers through `views(...)` look-backs of 7–90 days and purchasers through `purchases(...)` look-backs of 7–365 days.** Source: SD 3.0 OpenAPI.
18. **Amazon's published event-effect figures compare advertisers with "average category growth" or with an adjacent pre-period.** They are not controlled tests. Sources: "Prime Day 2026: Advanced advertising strategies"; "Holiday advertising guide".
19. **The UK and EU events carry their own names, local start times and, for the spring event, their own dates.** In 2026: spring March 10–16 in 13 European countries, against March 25–31 in the US; Prime Day June 23–26 in both; the October event on October 6–7, named "Prime Deal Days" in Germany; Black Friday Week 2025 November 20 to December 1, announced November 13. Sources: About Amazon UK, About Amazon EU, About Amazon Deutschland and Amazon Press Center DE/UK pages (A12).
20. **Amazon's holiday "extend" phase runs from December into January**, with the shopper groups Amazon names (last-minute gift buyers, post-holiday deal seekers, peak-event browsers, new-to-brand buyers to retain, New Year resolution shoppers). Amazon makes no auction claim for the period, and "Q5" is a practitioners' term. Sources: "Holiday advertising guide"; "Trends for 2025 holiday marketing strategies"; "New Year's Ads"; "Post-event advertising strategy" (H5).
21. **Brand Tailored Promotions are Brand Registry discounts of 10–50%, targeted to audiences of at least 1,000 shoppers built from the brand's views, cart adds and purchases.** They are created in Seller Central (US, UK, ES, FR, IT, DE, JP), up to 20 at a time, start at least 48 hours ahead, show a green badge only to the audience, and stack with coupons. Their fees sit on an unreadable help page. Sources: sell.amazon.com "What are Amazon Brand Tailored Promotions?"; "Brand Tailored Promotions: Offer exclusive discounts for loyal customers" (F7).
22. **The SP-API Promotions API is read-only in its 2025-12-01 model, for sellers.** It can tag a promotion's audience as a brand segment (`segmentType` `BRAND`, "Brand-tailored audience") when `includedData=CUSTOMER_SEGMENTS` is sent. It has no Brand Tailored Promotions type. Sources: Promotions API model; SP-API "Promotions API" (F6).
23. **In EU stores, a price-reduction claim is measured against the lowest price of the prior 30 days.** This is German law, read by the EU court to cover percentages and "price highlight" statements. Amazon's FR, ES, IT, BE, SE and PL reference-price pages say they display that 30-day low for limited-time promotions. Amazon's "Was Price" is a separate 90-day median. Sources: PAngV § 11; CJEU Press Release 152/24 (C-330/23); Amazon "Reference Pricing and Savings" pages (F10).
24. **SB Product Collection: since August 2026, creates become Manual Collections. Creates are refused after January 2027 (Deprecations, migration guide), and support ends from February 2027 (release note of September 18, 2026).** Existing ads keep serving, per the migration guide, with no end date stated. `POST /sb/v4/migrations/list` recommends replacements. Sources: "Deprecations"; "Migration Guide for Product Collection to Collections Ad Type"; release notes index; SB 4.0 OpenAPI (G2).
25. **The AMC Amazon Retail Purchases dataset is queryable at no cost from June 1 to December 31, 2026**, and its promotional columns are Amazon's stated means to "separate the effect of their media from the effect of their deals". Sources: "AMC Amazon Retail Purchases (paid)"; "Ads API v1 release notes" (I6, I7).

## What cx must read at run time

The calls are listed by surface. "Where the figure lives" names the field that holds it. Nothing here is a fixed value in a skill.

### Ads API (Sponsored Products, Sponsored Brands, Sponsored Display v3 paths)

| Need | Operation | Where the figure lives |
|---|---|---|
| Event calendar in the seller's marketplace | `POST /sp/v1/events` (SPGetAllRuleEvents) | `events[].eventId/eventName/startDate/endDate`, `groupedEvents[]` |
| Events Amazon recommends for this campaign | `POST /sp/campaigns/budgetRules/recommendations` (`application/vnd.spbudgetrulesrecommendation.v3+json`, `recommendationType: EVENTS_FOR_EXISTING_CAMPAIGN`); SB: `POST /sb/campaigns/budgetRules/recommendations` | `recommendedBudgetRuleEvents[].suggestedBudgetIncreasePercent`, `startDate/endDate` (YYYYMMDD; empty if unannounced) |
| Existing budget rules and their state | `GET /sp/budgetRules`, `GET /sp/campaigns/{campaignId}/budgetRules`, `GET /sp/budgetRules/{id}/campaigns`; `/sb/budgetRules`; `/sd/budgetRules` | `ruleDetails.ruleType`, `duration.eventTypeRuleDuration.eventId` / `dateRangeTypeRuleDuration`, `budgetIncreaseBy.value`, `ruleState`, `ruleStatus` |
| Create or attach an event budget rule | `POST /sp/budgetRules`; `POST /sp/campaigns/{campaignId}/budgetRules`; `POST /sp/budgetRulesAssociation` | 207 multi-status per item |
| Budget headroom and missed opportunity | `POST /sp/campaigns/budgetRecommendations` (`application/vnd.budgetrecommendation.v3+json`); `POST /sp/campaigns/budget/usage`; SB `/sb/campaigns/budgetRecommendations`, `/sb/campaigns/budget/usage` | `suggestedBudget`, `sevenDaysMissedOpportunities.percentTimeInBudget`, `estimatedMissed*Lower/Upper`, `budgetRuleRecommendation.suggestedBudgetIncreasePercent` |
| Special-event budgets for a new campaign | `POST /sp/campaigns/initialBudgetRecommendation` | `specialEvents[].eventKey/eventName/startDate/endDate/dailyBudget/benchmark` |
| Event bid suggestions | `POST /sp/targets/bid/recommendations` (v4/v5); Ads API v1 `/adsApi/v1/query/recommendations` and `/adsApi/v1/recommendations` (unified `Bid` object) | theme `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT`, `BFCM_HOLIDAY`; `bidRecommendations[]`; v5 `suggestedBidImpactMetrics`; v1 `Bid.theme` |
| Prime Day / gift keyword themes as targets | Ads API v1 targets (`/adsApi/v1/create/targets`, `query/targets`) | `themeTarget.matchType` `KEYWORDS_RELATED_TO_PRIME_DAY`, `KEYWORDS_RELATED_TO_GIFTS` |
| Event keyword theme | `POST /sp/targets/keywords/recommendations` (v5) | theme `SPECIAL_DAYS` when offered |
| Schedule and event bid rules | `POST /sp/rules/optimization/search`; `POST/PUT /sp/rules/optimization`; `POST /sp/campaigns/{campaignId}/optimizationRules`; SB `/sb/rules/optimization` (beta) | `recurrence.duration.eventId`, `action.actionDetails.value` (1–100), `status` |
| Rule-based bidding guardrail state | `/sp/rules/campaignOptimization` | rule and its ROAS guardrail; the 10-day, 10-conversion, 21-day and 20/40-day conditions are in the guide |
| Campaign bidding strategy and placement multipliers before and after the event | SP campaigns endpoints (see `method/ads-api-surface.md`) | `dynamicBidding.strategy`, `placementBidding[]` |
| Performance by day and hour around the event | v3 reports `spCampaigns`, `spTargeting`, `spSearchTerm`, `spAdvertisedProduct`, `sbCampaigns`, `sdCampaigns`; v1 reporting with `date.value`/`hour.value` | `cost`, `clicks`, `impressions`, `purchases7d`/`sales7d` (SP seller), `purchases14d`/`sales14d` (vendor), `sales` (SB/SD 14d), `timeZone.value` |
| Restated conversions | the same report pulled again later; restatement happens 1, 7 and 28 days after the conversion and spans the attribution window ("Reporting v3 FAQ") | same fields; differences between pulls are restatement |
| SD post-event audiences | SD targeting endpoints (SD 3.0) | `views(exactProduct lookback=N)`, `purchases(... lookback=N)` |
| Promotion effect separated from media | AMC Amazon Retail Purchases (paid; no cost June 1–Dec 31, 2026) | `price_discount_type/amt`, `coupon_discount_*`, `point_of_sale_discount_*`, `net_unit_price`, `user_id` |
| SB Product Collection ads still running, and their replacements | `POST /sb/v4/migrations/list` (ListMigrations, SB 4.0); SB list ads | recommended `MANUAL_COLLECTION` / `AUTO_COLLECTION` per source ad; `creativeType` `PRODUCT_COLLECTION` vs `MANUAL_COLLECTION` / `AUTO_COLLECTION` |

The schemas live in the SP 3.0 OpenAPI (`SponsoredProducts_prod_3p.json`), SB 4.0 JSON, SB 3.0 YAML and SD 3.0 YAML. All are listed in `contracts.json` at https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json.

### SP-API (seller side)

| Need | Operation | Where the figure lives |
|---|---|---|
| The seller's deals, coupons, PEDs and their event | Promotions API `searchPromotions` (`GET /promotions/2025-12-01/promotions`, filter `promotionTypes`, `statuses`, `asins`, date windows); `getPromotion` | `promotionType`, `couponType`, `schedule.startDate/endDate/eventId`, `customerSegments[].segmentId` (`PRIME_EXCLUSIVE`), `merchandising.displayOnWebsite`, `benefit.stacking`, `feeSnapshot`, `issues` |
| Promotion performance by period | Data Kiosk seller analytics dataset, promotion group | `promotionGlanceViewCnt`, `promotionConversionRate`, `promotionOrderedUnitsWithRevenue`, `promotionDiscountPct`, `dealId` |
| YoY and WoW comparison | Data Kiosk `timeRangeBenchmarking` at WEEK or MONTH | `yearOverYear` (same ISO week / same month), `weekOverWeek`, `monthOverMonth` |
| Seasonal search volume per query | `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT` (WEEK Sun–Sat, MONTH, QUARTER) | `searchQueryVolume`, `totalQueryImpressionCount`, `asinImpressionShare`, `totalMedianClickPrice`, `asinPurchaseShare` |
| Market-wide query rank by period | `GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT` (DAY, WEEK, MONTH, QUARTER) | `searchFrequencyRank` |
| Brand catalog search funnel | `GET_BRAND_ANALYTICS_SEARCH_CATALOG_PERFORMANCE_REPORT` | impressions, clicks, cart adds, purchases |
| Whether a promotion targets a brand audience | `searchPromotions` / `getPromotion` with `includedData=CUSTOMER_SEGMENTS` | `customerSegments[].segmentType` (`BRAND` / `PROGRAM`), `segmentId`, `segmentDetails.brandSegmentDetails.brandId` |

Brand Tailored Promotions and Customer Engagement campaigns are created and reported in Seller Central (Advertising > Brand Tailored Promotions; Brands > Customer Engagement). No SP-API or Ads API operation read creates them or returns their dashboards. What cx can read through an API about them is whatever the Promotions API returns under a `BRAND` segment.

A Seller Central dashboard is not an API, but the seller can open it. The deal dashboard shows deal status and fees, the event price limits and validated reference prices. The Promotions API exposes part of this. The rest (event price limits, reference-price validation) is visible only in Seller Central, whose help pages this seat could not read.

### Keepa (public product history)

| Need | Field | Note |
|---|---|---|
| Whether a competitor or the seller's ASIN carries a deal now | `product.deals[]` (`dealType`: `PRIME_DAY`, `PRIME_DAY_EARLY`, `EARLY_ACCESS_WITH_PRIME`, `PRIME_EXCLUSIVE`, `LIMITED_TIME_DEAL`, `SPECIAL_EVENT_SALE`, ...; `accessType`; `badge`; `percentClaimed` for Lightning Deals; `startTime`/`endTime`) | Keepa says the categorical values are open-ended |
| Coupon history | `product.couponHistory` (`[keepaTime, one-time coupon, S&S coupon, ...]`), tracked since June 15, 2024 | |
| Lightning Deal price history | `csv[8]` (`LIGHTNING_DEAL`) | |
| Amazon's own promotions | `product.promotions` | "Only Amazon US promotions by Amazon (not 3rd party) are collected" |

Source: keepacom/api_backend, `Product.java`, https://github.com/keepacom/api_backend, read 2026-11-09.

### Amazon's public pages (read per season)

- aboutamazon event pages for dates and marketplaces: the US, aboutamazon.jp and aboutamazon.in; for Europe, aboutamazon.co.uk, aboutamazon.eu, aboutamazon.de and the Amazon Press Center's DE and UK releases (press.aboutamazon.com/de, /uk), which carry local start times.
- The Seller Forums News_Amazon holiday post for deal windows, fees and inventory dates: the US post, and the UK forum's "Peak season" post, which carries the UK, DE, FR, IT and ES fees.
- Each EU store's "Reference Pricing and Savings" help page (nodeId GQ6B6RH72AX8D2TD on that store's domain), for the 30-day prior-price wording and the "Was Price" definition.
- sell.amazon.com "What are Amazon Brand Tailored Promotions?", for BTP audiences, limits and markets.
- The Amazon Ads BFCM and holiday guides for the year's ad-policy duration table.

These are the only public places found that carry the dates and fee figures; each is a dated page that changes per season.

## Pages read

All pages were read 2026-11-09 by plain GET (curl with a browser user agent), unless the row says otherwise.

| Page name | URL | Type | Date read | What it gave |
|---|---|---|---|---|
| Prime Day 2026: Advanced advertising strategies | https://advertising.amazon.com/library/guides/prime-day-guide-advanced-strategies | official | 2026-11-09 | 137% figure and baseline (20 marketplaces); SP guidance; display cost-control 2.6X; Nottorf quotes; B2B 900% adjustment; Business Prime Day markets |
| Post-event advertising strategy | https://advertising.amazon.com/library/guides/post-event-advertising-strategy | official | 2026-11-09 | Post-event scenarios; Nottorf and Meyer quotes; SD views remarketing |
| Holiday advertising guide | https://advertising.amazon.com/library/guides/holiday-advertising-guide | official | 2026-11-09 | Build/peak/extend phases; +20–30% budgets, 3–5 days ahead; launch by early October; 145% figure; B2B |
| Holiday advertising myths: What experts want you to know | https://advertising.amazon.com/library/guides/common-holiday-advertising-myths | official | 2026-11-09 | ACOS spike vs TACOS, with Amazon's TACOS sentence (re-read in the gap fill); check 7–14-day attribution; CVR drops at events; expert quotes |
| Black Friday and Cyber Monday advertising tips | https://advertising.amazon.com/library/guides/black-friday-and-cyber-monday-advertising-tips | official | 2026-11-09 | Event-name duration table; deal teasing ban; REC BFCM badge; FDW rules; Store timing |
| Holiday shopping season performance-boosting tips | https://advertising.amazon.com/library/guides/holiday-shopping-season-performance-boosting-tips | official | 2026-11-09 | REC deal badge types; "up to" 10% rule; dynamic pricing pause rule |
| 3-step guide to the peak season | https://advertising.amazon.com/library/guides/boost-seasonal-sales | official | 2026-11-09 | Kantar figures; UK Christmas +75pp; peer tips |
| 2025 retail holiday calendar | https://advertising.amazon.com/library/guides/global-shopping-events | official | 2026-11-09 | Country event calendar (JP, IN, MX, TR, global) |
| Back-to-school marketing | https://advertising.amazon.com/library/guides/back-to-school-marketing | official | 2026-11-09 | August–September season; NRF 56% by July |
| Advertising for international events | https://advertising.amazon.com/library/guides/advertising-for-international-events | official | 2026-11-09 | Generic guidance only |
| Key events store prep | https://advertising.amazon.com/library/guides/key-events-store-prep | official | 2026-11-09 | All Deals page; Store event-name ban; SB product collection deals CTA; 28%/23% Store figures |
| Prime Day (events page) | https://advertising.amazon.com/events/prime-day | official | 2026-11-09 | 2026 dates and countries |
| Holidays (events page) | https://advertising.amazon.com/events/holidays | official | 2026-11-09 | "October is the unofficial start" |
| How retail tentpole moments can deliver year-round results | https://advertising.amazon.com/blog/retail-tentpole-events-to-drive-year-round-results | official | 2026-11-09 | Mother's Shea case figures |
| Sales promotion guide | https://advertising.amazon.com/library/guides/sales-promotion | official | 2026-11-09 | Promotion risks; L'Oréal 78% in 48h |
| Remarketing guide | https://advertising.amazon.com/library/guides/remarketing | official | 2026-11-09 | Generic remarketing |
| Product promotion guide | https://advertising.amazon.com/library/guides/product-promotion | official | 2026-11-09 | Generic |
| Budget and bidding rules | https://advertising.amazon.com/library/guides/budget-rules | official | 2026-11-09 | Rule types; event budgets |
| Diwali ads | https://advertising.amazon.com/library/guides/diwali-ads | official | 2026-11-09 | Generic timing |
| Holiday shopping trends | https://advertising.amazon.com/library/guides/holiday-shopping-trends | official | 2026-11-09 | Context only |
| 5 Spooky Halloween Marketing Ideas for 2024 | https://advertising.amazon.com/library/guides/halloween-marketing | official | 2026-11-09 | Generic timing |
| Mother's Day marketing | https://advertising.amazon.com/library/guides/mothers-day-marketing | official | 2026-11-09 | Generic timing |
| New Year's Ads: 5 Marketing Campaign Ideas to Inspire in 2024 | https://advertising.amazon.com/library/guides/new-years-ads | official | 2026-11-09 | Generic timing |
| Lunar New Year and Chinese New Year Marketing Ideas for 2024 | https://advertising.amazon.com/library/guides/lunar-new-year-marketing | official | 2026-11-09 | Generic timing |
| Prime Day tips for small-business owners and authors | https://advertising.amazon.com/library/guides/prime-day-advertising-guide-authors | official | 2026-11-09 | Context only |
| Prime Day 2023 - Advertising with display ads | https://advertising.amazon.com/library/news/prime-day-non-endemic-advertising | official | 2026-11-09 | Context only |
| Attracting readers during peak shopping periods | https://advertising.amazon.com/library/expert-advice/attracting-readers-during-peak-shopping-periods | official | 2026-11-09 | Context only |
| unBoxed 2026 news announcements | https://advertising.amazon.com/library/news/unboxed-2026-news-announcements | official | 2026-11-09 | Amazon Ads Agent; Alexa for Shopping; nothing seasonal |
| Events for schedule bid rules, now available for Sponsored Products advertisers in the advertising console | https://advertising.amazon.com/resources/whats-new/event-based-bid-rules-for-sponsored-products-advertisers | official | 2026-11-09 | Jan 2, 2025 launch; Recurring Events JP only; Individual Events WW |
| Schedule based bid rules now available for Sponsored Products | https://advertising.amazon.com/resources/whats-new/schedule-based-bid-rules-available-for-sponsored-products | official | 2026-11-09 | Launch, Nov 6, 2023 |
| Hours of day now available for schedule-based budget rules | https://advertising.amazon.com/resources/whats-new/hours-of-day-available-for-schedule-based-budget-rules | official | 2026-11-09 | US, CA, UK, IN, JP |
| New metrics available for Sponsored Brands performance-based budget rules | https://advertising.amazon.com/resources/whats-new/sponsored-brands-performance-based-budget-rules | official | 2026-11-09 | IS and NTB metrics |
| Budget rules now available in Amazon advertising console globally | https://advertising.amazon.com/resources/whats-new/dynamic-budget-control | official | 2026-11-09 | Aug 12, 2021 launch; events recommended from campaign products; $10 minimum; 7 days |
| Sponsored ads daily budgeting policy and options | https://advertising.amazon.com/resources/whats-new/sponsored-ads-daily-budgeting-policy-and-options | official | 2026-11-09 | Up to 100% over on a day, monthly average |
| Harvest high performing targets with Target Promotion, now available for Sponsored Products advertisers in UCM ads console | https://advertising.amazon.com/resources/whats-new/target-promotion-for-sponsored-products | official | 2026-11-09 | Target harvesting launch |
| Highlight deals on your store page and traffic shoppers to that page using Brand Store Creative | https://advertising.amazon.com/resources/whats-new/highlight-deals-using-brand-store-creative | official | 2026-11-09 | DSP deal messaging |
| Ad policy (hub) | https://advertising.amazon.com/resources/ad-policy | official | 2026-11-09 | 301-redirects to the Amazon Ads home page; no policy index served |
| General policies | https://advertising.amazon.com/resources/ad-policy/general-policies | official | 2026-11-09 | 3 business days creative processing |
| Production timelines | https://advertising.amazon.com/resources/ad-policy/production-timelines | official | 2026-11-09 | Creative production lead times |
| Ad policy quick reference | https://advertising.amazon.com/resources/ad-policy/quick-reference | official | 2026-11-09 | Same savings claim on ad and landing page |
| Sponsored ads additional policies | https://advertising.amazon.com/resources/ad-policy/sponsored-ads-additional-policies | official | 2026-11-09 | Contractual terms; no deal or event content |
| Sponsored Products 3.0 OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json | official | 2026-11-09 | Events, budget rules, optimization rules, theme bids, SPECIAL_DAYS, initial and missed-opportunity budgets |
| Budget rules overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/overview.md | official | 2026-11-09 | Recommended events; 7/14-day performance windows |
| Schedule-based budget rules | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/schedule-based.md | official | 2026-11-09 | SP/SB only; unannounced dates auto-fill; intraday markets |
| Performance-based budget rules | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/budget-rules/performance-based.md | official | 2026-11-09 | Metrics per ad product |
| Bidding rules overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/rules/bidding-rules/overview.md | official | 2026-11-09 | Rule-based bidding entry and disable conditions |
| Theme-based bid suggestions quickstart | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-products/bid-suggestions/theme-based-bid-suggestions-quickstart-guide.md | official | 2026-11-09 | Winning-bid basis; no-budget-cap assumption |
| Sponsored Brands 4.0 OpenAPI | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | official | 2026-11-09 | SB budget rules, budget recommendations, optimization rules |
| Sponsored Brands 3.0 OpenAPI | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/3-0/openapi.yaml | official | 2026-11-09 | SB budget-rule recommendations |
| Sponsored Display 3.0 OpenAPI | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml | official | 2026-11-09 | SD budget rules; views/purchases look-backs |
| Ads API v1 merged OpenAPI | https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLMerged_prod_3p.json | official | 2026-11-09 | No budget-rule, event-list or optimization-rule endpoints; `Bid.theme` event enum; `KEYWORDS_RELATED_TO_PRIME_DAY` / `_GIFTS` theme targets |
| Deprecations | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/deprecations.md | official | 2026-11-09 | v3 reporting shutoff 2027-06-30; budget-rule history deprecated 8/31/2023; SB Product Collection: June 2026 deprecation, August 2026 creates mapped to Manual Collection, create shutoff January 2027 (re-read in the gap fill); theme-bid v3 content type May 15, 2025 |
| Ads API v1 release notes | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/ads-api-v1.md | official | 2026-11-09 | AMC promotion columns and the "separate the effect of their media from the effect of their deals" sentence; retention; modeled NTB; SB Collections worldwide (Feb 18, 2026) |
| AMC Amazon Retail Purchases (paid) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/amazon-marketing-cloud/datasources/amazon_retail_purchase_paid.md | official | 2026-11-09 | Promotion columns and limits; no-cost window June 1–Dec 31, 2026; marketplaces; `user_id` |
| Ads API contracts index | https://d3a0d0y2hgofx6.cloudfront.net/en-us/contracts.json | official | 2026-11-09 | Spec locations |
| Reporting v3 FAQ | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/faq.md | official | 2026-11-09 | 12h/24h availability; restatement 1/7/28 days; 42-day example |
| Dates and historical data retention | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/dates.md | official | 2026-11-09 | Campaign time zone; retention table |
| Ads API v1 reporting overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/overview.md | official | 2026-11-09 | Traffic-date reporting |
| Reporting overview | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/overview.md | official | 2026-11-09 | Context |
| Purchases (Amazon retail conversions) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/ads-v1/metrics/amazon-retail-conversions/purchases.md | official | 2026-11-09 | SP 7d sellers / 14d vendors |
| Reporting v3 columns | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/reporting/v3/columns.md | official | 2026-11-09 | `sales` 14-day click or view (SB/SD); `sales14d` definition |
| Prime Day 2026 date | https://www.aboutamazon.com/news/retail/amazon-prime-day-2026-date | official | 2026-11-09 | June 23–26; countries |
| When is Amazon Prime Day | https://www.aboutamazon.com/news/retail/when-is-amazon-prime-day | official | 2026-11-09 | Dates; price history tool; members |
| Prime Big Deal Days FAQ | https://www.aboutamazon.com/news/retail/amazon-prime-big-deal-days-faq | official | 2026-11-09 | Oct 6–7; deal drops |
| Prime Big Deal Days 2026: October 6–7 | https://www.aboutamazon.com/news/retail/amazon-prime-big-deals-day-2026-when-october-6-7 | official | 2026-11-09 | 48 hours; times |
| The history of Prime Day | https://www.aboutamazon.com/news/retail/the-history-of-prime-day | official | 2026-11-09 | Dates 2019–2025 |
| What makes Prime Day 2025 different | https://www.aboutamazon.com/news/retail/what-makes-prime-day-2025-different | official | 2026-11-09 | 96 hours; Today's Big Deals |
| Prime Day 2025 recap | https://www.aboutamazon.com/news/retail/prime-day-2025-recap | official | 2026-11-09 | "Biggest ever" claim |
| When is Black Friday 2026? Here's everything you need to know | https://www.aboutamazon.com/news/retail/when-is-amazon-black-friday-faq | official | 2026-11-09 | Nov 27, 2026; Week dates not yet given |
| When is Black Friday 2025 (redirect) | https://www.aboutamazon.com/news/retail/when-is-black-friday-2025 | official | 2026-11-09 | Redirects to the 2026 content |
| When is Cyber Monday 2026? (old 2025 URL) | https://www.aboutamazon.com/news/retail/when-is-cyber-monday-2025 | official | 2026-11-09 | Redirects to .../when-is-amazon-cyber-monday-faq: Nov 30, 2026 |
| Big Spring Sale FAQ | https://www.aboutamazon.com/news/retail/amazon-big-spring-sale-faq | official | 2026-11-09 | Mar 25–31, 2026 |
| Amazon's response to the FTC's lawsuit regarding Sponsored Ads | https://www.aboutamazon.com/md/company-news/amazon-ftc-sponsored-ads-lawsuit-response | official | 2026-11-09 | Hard/soft reserve mechanics; CPC and bid figures; no mention of peak periods |
| 'Amazon Rufus' AI experience comes to the Amazon Shopping app | https://www.aboutamazon.com/news/retail/amazon-rufus | official | 2026-11-09 | "On May 13, 2026, Rufus was renamed Alexa for Shopping" |
| Amazon ブラックフライデー 2026 | https://www.aboutamazon.jp/news/retail/amazon-black-friday-2026 | official | 2026-11-09 | JP dates announced Nov 19; other JP 2026 events |
| Amazon Great Indian Festival | https://www.aboutamazon.in/amazon-great-indian-festival | official | 2026-11-09 | Runs through Nov 10, 2026; 2025 start Sep 23 and end Oct 20 |
| Amazon Great Indian Festival 2026: Deals, dates and offers through November 10 | https://www.aboutamazon.in/news/retail/amazon-great-indian-festival-2026-dates | official | 2026-11-09 | Through Nov 10; festival span; deal formats (the 2025 dates are on the hub page) |
| Seller growth, Great Indian Festival 2026 | https://www.aboutamazon.in/news/small-business/amazon-seller-growth-great-indian-festival-2026 | official | 2026-11-09 | Up to 3.5x BAU in week one |
| Seller promotions | https://sell.amazon.com/blog/seller-promotions | official | 2026-11-09 | Deal, coupon and price-discount rules |
| Prime Day tips | https://sell.amazon.com/blog/prime-day-tips | official | 2026-11-09 | Budget pause at midnight; schedule rules; bids; coupon badge; Store a week ahead |
| Prime Day (sell.amazon.com) | https://sell.amazon.com/prime-day | official | 2026-11-09 | Self-service promotions closer to event |
| FBA holiday guide | https://sell.amazon.com/fulfillment-by-amazon/holiday | official | 2026-11-09 | 10–12 / 7–9 / 4–6 / 3-week timeline |
| Brand Analytics | https://sell.amazon.com/blog/brand-analytics | official | 2026-11-09 | Three-year history; three-day availability (stated in the Demographics section) |
| Holiday 2026: Same fees, same eligibility, earlier deadlines | https://sellercentral.amazon.com/seller-forums/discussions/t/3e31fbb7-04e0-4ed4-873e-f74b1052e2ff | official (with seller replies as opinion) | 2026-11-09 | Deal windows, fees, lookback exclusion, inventory and peak-fee dates |
| Report type values – Analytics | https://developer-docs.amazon/sp-api/docs/report-type-values-analytics | official | 2026-11-09 | SQP, Search Terms, Search Catalog Performance periods and fields |
| Seller analytics dataset guide (Data Kiosk) | https://developer-docs.amazon/sp-api/docs/seller-analytics-dataset-guide | official | 2026-11-09 | YoY by ISO week; promotion fields; two-year limit |
| Promotions API model 2025-12-01 | https://github.com/amzn/selling-partner-api-models/blob/main/models/promotions-api-model/promotions_2025-12-01.json | official | 2026-11-09 | Operations, filters, eventId, segments, fee snapshot |
| How events like Prime Day helped Amazon navigate the pandemic | https://www.amazon.science/latest-news/how-peak-events-like-prime-day-helped-amazon-navigate-the-pandemic | official | 2026-11-09 | "Different week of the year" forecasting quote |
| Peak period demand forecasting with proxy data: GNN-enhanced meta-learning | https://www.amazon.science/publications/peak-period-demand-forecasting-with-proxy-data-gnn-enhanced-meta-learning | research | 2026-11-09 | Abstract: 26.24% / 8.7% MAE gains; WACV 2024 workshop |
| FTC et al. v. Amazon, complaint (public filing) | https://www.illinoisattorneygeneral.gov/News-Room/Current-News/FILED%20PUBLIC%20Amazon%20Complaint%208.31.26.pdf | opinion (allegations) | 2026-11-09 | HVE surcharge allegations; quoted help-page wording (¶¶146–149); 2021 "Pricing Introduction" document (¶157) |
| Attorney General Ken Paxton Sues Amazon for Rigging Advertising Auctions... (Texas AG press release) | https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-amazon-rigging-advertising-auctions-overcharged-businesses-45 | opinion (litigant's allegations) | 2026-11-09 | ~17% ordinary days, >25% peak events; own bid ~80% of the time |
| Keepa Product.java | https://github.com/keepacom/api_backend/blob/master/src/main/java/com/keepa/api/backend/structs/Product.java | vendor docs | 2026-11-09 | deals[].dealType values; couponHistory; LIGHTNING_DEAL csv |
| Prime Day 2026 Preview: 7 Shifts From 2025 (Skai) | https://skai.io/blog/prime-day-2026-preview-7-shifts-from-2025-to-guide-your-2026-playbook/ | opinion | 2026-11-09 | PD 2025 CPC, CTR, spend split, halves |
| Prime Day 2026 Ad Benchmarks (Marketplace Ad Pros) | https://marketplaceadpros.com/guides/amazon-prime-day-2026-ad-benchmarks/ | opinion | 2026-11-09 | Median lifts; budget-raise data; CPC; maturity |
| Amazon Prime Day 2026: Record Sales Meet Shifting Consumer Baskets (Tinuiti) | https://tinuiti.com/blog/amazon/prime-day-recap/ | opinion | 2026-11-09 | Ad spend +19%; day shares; DSP tail |
| Amazon Prime Day 2026 – The Results (Acadia) | https://acadia.io/amazon-prime-day-2026-the-results/ | opinion | 2026-11-09 | YoY vs lift; PED mix; halo penalty; attribution lag; lead-out |
| Prime Big Deal Days 2026 PPC Playbook: Bids & Budgets (Ad Badger) | https://www.adbadger.com/blog/prime-big-deal-days-ppc-strategy/ | opinion | 2026-11-09 | Ramp multipliers; CPC/bid ratio; 14-day review |
| Prime Big Deal Days Is Over. Don't Cut PPC Now. (Pare, George Reid) | https://pare.so/blog/amazon-prime-big-deal-days-post-event-ppc-rank-dsP-strategy-2026 | opinion | 2026-11-09 | Hold 48–72h; DSP 20–30 days; CPC ranges |
| Japan Prime Day 2026 (Impress Watch) | https://www.watch.impress.co.jp/docs/news/2123919.html | opinion (press) | 2026-11-09 | JP dates Jul 7–9 early, Jul 10–13 main |
| Amazon Black Friday 2025 dates (Yahoo Shopping) | https://shopping.yahoo.com/deals/articles/amazon-just-dropped-details-black-160508522.html | opinion (press) | 2026-11-09 | Nov 20–Dec 1, 2025 |
| Amazon skips its BFCM recap (Modern Retail) | https://www.modernretail.co/marketing/marketplace-briefing-amazon-skips-its-black-friday-and-cyber-monday-recap-for-the-first-time-since-2016/ | opinion (press) | 2026-11-09 | No BFCM or PBDD 2025 recap |
| Van Heerde, Leeflang, Wittink (2000) | https://doi.org/10.1509/jmkr.37.3.383.18782 | research | 2026-11-09 | Dip 4–25% of current effect (abstract via Crossref API) |
| Mela, Gupta, Lehmann (1997) | https://doi.org/10.1177/002224379703400205 | research | 2026-11-09 | Promotion sensitivity rises (abstract) |
| Ailawadi, Gedenk, Lutzky, Neslin (2007) | https://doi.org/10.1509/jmkr.44.3.450 | research | 2026-11-09 | Stockpiling benefits (abstract) |
| Brodersen et al. (2015) | https://doi.org/10.1214/14-aoas788 | research | 2026-11-09 | Bayesian structural time series under seasonality (abstract) |
| *Rows added in the gap fill, 2026-11-09:* | | | | |
| The author's guide to Sponsored Products | https://advertising.amazon.com/library/guides/authors-guide-to-sponsored-products | official | 2026-11-09 | "TACOS shows your ad spend as a percentage of total sales" |
| Trends for 2025 holiday marketing strategies | https://advertising.amazon.com/library/guides/holiday-shopping-trends | official | 2026-11-09 | Mintel 31% Cyber Monday to New Year's; lead-up/peak/lead-out; gift cards 54%; December concentration |
| New Year's Ads: 5 Marketing Campaign Ideas to Inspire in 2024 | https://advertising.amazon.com/library/guides/new-years-ads | official | 2026-11-09 | Advertise into January; belated-gift shoppers; Valentine's next |
| Post-event advertising strategy (re-read) | https://advertising.amazon.com/library/guides/post-event-advertising-strategy | official | 2026-11-09 | "Extend holiday deals into January" marked incorrect in the fashion scenario |
| Holiday advertising guide (re-read) | https://advertising.amazon.com/library/guides/holiday-advertising-guide | official | 2026-11-09 | Phase 3 wording |
| Key events store prep (re-read) | https://advertising.amazon.com/library/guides/key-events-store-prep | official | 2026-11-09 | Deals CTA sentence still present |
| Migration Guide for Product Collection to Collections Ad Type | https://d3a0d0y2hgofx6.cloudfront.net/en-us/reference/migration-guides/sb-product-collection.md | official | 2026-11-09 | Timeline June 2026 / August 2026 / January 2027; existing ads keep serving; `creativeType` values |
| Ads API release notes (index) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/release-notes/index.md | official | 2026-11-09 | ListMigrations (Sep 18, 2026): "Beginning February 2027, product collections will no longer be supported" |
| Collections (SB guide) | https://d3a0d0y2hgofx6.cloudfront.net/en-us/guides/sponsored-brands/ads/collections.md | official | 2026-11-09 | No deals CTA mentioned |
| Sponsored Brands 4.0 OpenAPI (re-read) | https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json | official | 2026-11-09 | `POST /sb/v4/migrations/list` ListMigrations |
| What are Amazon Brand Tailored Promotions? | https://sell.amazon.com/blog/brand-tailored-promotions | official | 2026-11-09 | BTP markets, goals, audiences, 1,000 minimum, 10–50%, limits, badge, stacking, fees referred to help page |
| Brand Tailored Promotions: Offer exclusive discounts for loyal customers | https://sell.amazon.com/blog/announcements/brand-tailored-promotions | official | 2026-11-09 | 2023 launch; six audience definitions; one unit per customer; US only at launch |
| Amazon Brand Registry | https://sell.amazon.com/brand-registry | official | 2026-11-09 | BTP among Registry promotion tools |
| Create engaging email campaigns with themed templates in 'Customer Engagement' (beta) tool | https://sellercentral.amazon.com/seller-forums/discussions/t/e3f3a064ed378b7031537558efb43a18 | official (News_Amazon; seller replies opinion) | 2026-11-09 | Followers email tool; 1,000 followers "best experience"; themed templates |
| Amazon Launches Free Email Marketing Capabilities for Sellers to Reach Their Repeat, Recent, and High-Spend Amazon Customers | https://press.aboutamazon.com/2022/9/amazon-launches-free-email-marketing-capabilities-for-sellers-to-reach-their-repeat-recent-and-high-spend-amazon-customers | official | 2026-11-09 | Tailored Audiences; no cost; metrics |
| Promotions API (SP-API docs) | https://developer-docs.amazon/sp-api/docs/promotions-api | official | 2026-11-09 | Sellers; NA/EU/FE; Pricing or Product Listing role; Aug 26, 2026 |
| Promotions API model 2025-12-01 (re-read) | https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/models/promotions-api-model/promotions_2025-12-01.json | official | 2026-11-09 | GET-only paths; `CustomerSegmentType` BRAND/PROGRAM; `includedData` |
| Amazon Spring Deal Days returns with seven days of savings | https://www.aboutamazon.co.uk/news/retail/amazon-spring-deal-days-returns-with-seven-days-of-savings | official | 2026-11-09 | UK spring event March 10–16, 2026 |
| Kräftig sparen zum Saisonstart: Amazons Frühlingsangebote kehren am 10. März zurück | https://press.aboutamazon.com/de/amazon-prime/2026/3/kraeftig-sparen-zum-saisonstart-amazons-fruehlingsangebote-kehren-am-10-maerz-zurueck | official | 2026-11-09 | DE spring event March 10–16; 13 countries |
| Amazon launches Prime Day with surprise deliveries, daily Epic Prime Deals, and four days of savings for members | https://www.aboutamazon.co.uk/news/retail/amazon-launches-prime-day-with-surprise-deliveries-daily-epic-prime-deals-and-four-days-of-savings-for-members | official | 2026-11-09 | UK Prime Day to June 26 |
| Der Countdown läuft: Prime Day bietet Hunderttausende Angebote vom 23. bis 26. Juni | https://press.aboutamazon.com/de/2026/6/der-countdown-laeuft-prime-day-bietet-hunderttausende-angebote-vom-23-bis-26-juni | official | 2026-11-09 | DE Prime Day 00:01 June 23 to 23:59 June 26 |
| Amazon Prime Big Deal Days 2026: Deal event returns to the UK from 6 to 7 October | https://www.aboutamazon.co.uk/news/retail/amazon-prime-big-deal-days-2026-date | official | 2026-11-09 | UK PBDD from 12:01 a.m. BST |
| Prime Big Deal Days: Save big on autumn and Christmas shopping from October 6-7th | https://www.aboutamazon.co.uk/news/retail/prime-big-deal-days-save-big-on-autumn-and-christmas-shopping-from-october-6-7th | official | 2026-11-09 | UK PBDD end 23:59 BST October 7 |
| Prime Big Deal Days is back October 6-7 | https://www.aboutamazon.eu/news/retail/prime-big-deal-days-2026 | official | 2026-11-09 | 12:01 a.m. CET; 22 countries |
| Was sind die Amazon Prime Deal Days? | https://www.aboutamazon.de/news/amazon-prime-und-shopping/prime-deal-days-termine-angebote | official | 2026-11-09 | DE name "Prime Deal Days"; October 6–7 |
| Die Prime Deal Days kehren am 6. und 7. Oktober zurück... | https://press.aboutamazon.com/de/2026/9/die-prime-deal-days-kehren-am-6-und-7-oktober-zurueck-prime-mitglieder-erhalten-exklusiven-zugang-zu-ueber-1-million-angeboten | official | 2026-11-09 | 00:01; 22 countries; "Die Termine können je nach Land variieren"; 12-month-low claim |
| It's the Season for Savings: Amazon's Black Friday Week Offers Deep Discounts... from 20 November until 1 December | https://press.aboutamazon.com/uk/news/retail/2025/11/its-the-season-for-savings-amazons-black-friday-week-offers-deep-discounts-on-customer-favourite-brands-from-20-november-until-1-december | official | 2026-11-09 | UK BFW 2025, announced 13 Nov 2025 |
| Der Countdown läuft: Die Black Friday Woche kehrt vom 20. November bis zum 1. Dezember zurück | https://press.aboutamazon.com/de/amazon-prime/2025/11/der-countdown-laeuft-die-black-friday-woche-kehrt-vom-20-november-bis-zum-1-dezember-zurueck | official | 2026-11-09 | DE BFW 2025, 00:01 Nov 20 to 23:59 Dec 1 |
| About Amazon UK retail news; About Amazon Deutschland shopping news; Amazon Press Center DE archive | https://www.aboutamazon.co.uk/news/retail ; https://www.aboutamazon.de/news/amazon-prime-und-shopping ; https://press.aboutamazon.com/press-release-archive?f0=de-DE | official | 2026-11-09 | No Black Friday Week 2026 announcement listed |
| Peak season 2026: Inventory dates, peak fees, deal cutoffs and promotions | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/d8c34b0b-86ed-4aec-9b0a-8be6eabb8fb0 | official | 2026-11-09 | UK/EU deal cutoffs Sep 23 / Nov 18; 30% early discount; UK/DE/FR/IT/ES fees; PED 3.5 stars; inbound dates; festive fee |
| Reference Pricing and Savings (Amazon.fr, .es, .it, .com.be, .se, .pl, .de, .co.uk, .nl) | https://www.amazon.fr/gp/help/customer/display.html?nodeId=GQ6B6RH72AX8D2TD (same nodeId per store) | official | 2026-11-09 | 30-day prior-price display (FR, ES, IT, BE, SE, PL); 90-day median Was Price; DE badge note; UK "Lowest price in 30 Days" |
| Preisangabenverordnung § 11 | https://www.gesetze-im-internet.de/pangv_2022/__11.html | law | 2026-11-09 | 30-day lowest price on every announced reduction |
| CJEU Press Release No 152/24, Case C-330/23 Aldi Süd | https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-09/cp240152en.pdf | law | 2026-11-09 | Percentages and "price highlights" computed from the 30-day low |
| Court: Amazon must label special offers more transparently (heise online) | https://heise.de/-10488538 | opinion (press report of a ruling) | 2026-11-09 | Munich I Regional Court on Prime Deal Days 2024; Amazon to appeal |
| Amazon Q5 Explained: The Cheapest Traffic of the Year (Evolve AMZ, Ian Smith) | https://evolveamz.com/amazon-q5-strategy-2026/ | opinion | 2026-11-09 | Q5 definition; CPM −28%; gift cards; January ACoS catch |
| Amazon Advertising Benchmarks 2026 (Ad Badger) | https://www.adbadger.com/blog/amazon-advertising-stats/ | opinion | 2026-11-09 | January 2026 ACOS 32.5% high, October 2025 28% low; CPC $1.22 |
| Guide: Ad tactics for the week after Christmas (Intentwise) | https://www.intentwise.com/blog/tactics-for-week-after-christmas | opinion | 2026-11-09 | CVR 13.4% to 11.03%; gift-card 27% |
| Amazon Advertising Post-Holiday: Where to Focus Now (Pattern) | https://www.pattern.com/blog/amazon-advertising-post-holiday-where-to-focus-now | opinion | 2026-11-09 | CPCs go down; gift-card retargeting (no data) |
| Amazon ad spend rises over Cyber 5, but most efficient sales days still ahead (MarTech, Andrew Waber, Teikametrics) | https://martech.org/amazon-ad-spend-rises-over-cyber-5-but-most-efficient-sales-days-still-ahead | opinion | 2026-11-09 | CVR up and cost per conversion down Cyber Monday to Dec 22 (700+ sellers, 2019) |
| Q4 2025 Retail Media Benchmark Report (Pacvue and Helium 10, PDF) | https://www.helium10.com/app/uploads/2026/01/2025-SMB-Q4_Benchmark_Report.pdf | opinion | 2026-11-09 | Q4 CPCs "stable or declined"; charts are images |
| Amazon makes its January 31 holiday return deadline an annual rule (PPC Land) | https://ppc.land/amazon-makes-its-january-31-holiday-return-deadline-an-annual-rule/ | opinion (press quoting Amazon) | 2026-11-09 | Returns to Jan 31, 2027; "This policy will apply every year" |
| Explained: What is Brand Tailored Promotions? (Intentwise) | https://www.intentwise.com/blog/brand-tailored-promotions-explained-tips-best-practices | opinion | 2026-11-09 | Stefani 3x recent-customer redemptions; Hirschkorn; drawbacks; badges |
| Black Friday Pricing Data Report (Omnia Retail) | https://www.omniaretail.com/blog/black-friday-pricing-data-report-2025 | opinion (vendor data) | 2026-11-09 | DE/NL price paths around Black Friday 2025 |
| Kaul and Wittink (1995) | https://doi.org/10.1287/mksc.14.3.g151 | research | 2026-11-09 | Three generalizations on price vs non-price advertising (abstract via Crossref) |
| Ataman, van Heerde and Mela (2010) | https://doi.org/10.1509/jmkr.47.5.866 | research | 2026-11-09 | Total elasticities product 1.37, distribution .74, advertising .13, discounting .04 (abstract) |
| Ataman, Mela and van Heerde (2008) | https://doi.org/10.1287/mksc.1080.0358 | research | 2026-11-09 | New brands: distribution and product beat discounting and advertising (abstract) |
| Erdem, Keane and Sun (2007, SSRN) | https://doi.org/10.2139/ssrn.965468 | research | 2026-11-09 | Advertising shifts willingness to pay, 17 of 18 brands (abstract) |

**Unreachable** (each tried on 2026-11-09):

1. Amazon Ads help center pages: the budget rules help (GNSMLANWNF344YBE), the peak-events policy help (GQ3SJ5QCWCQCKCYQ) and "Amazon Ads auctions" / "Understand Amazon Ad auctions". They answer 200 with a JS shell (about 70 characters of text) that loads sign-in (ap/signin, openid). The auction page's reserve-price wording is taken only from the complaint's quotation (E2).
2. Ad policy pages `amazon-branded-peak-events` (to help GQ3SJ5QCWCQCKCYQ), `black-friday-cyber-monday-policies` (to /resources/ad-specs), `creative-acceptance` (to help G3XD73L3Z6UKB8CB) and `sponsored-ads-policies` (to help G2NN8D3LSUR9V9EA): each 301-redirects to a sign-in help shell or to the ad-specs hub, with no policy text served.
3. Seller Central help pages from an earlier research lead: G202111490 (Amazon deals), GJHCPEFJ5JJQD52D (coupon eligibility), GYM7CTJPXEJBFBXH (price discounts and events), G202183600 (deals for events), GM2ADTH3XH3A5N57 (Prime Day readiness playbook), G202111590 (deal fees), GKN9A84DGTYWYHWY (suppressed deals) and GFXXXKMMQE9WLVNZ (Prime Exclusive Discounts). These are JS shells whose content arrives only through the help hub's POST content call, which this seat may not make. No rule from them is stated in this file.
4. Pacvue, "Prime Day in real time: why hourly optimization beats daily reporting": 403 (bot challenge) to curl and to WebFetch.
5. Triple Whale, Big Deal Days 2026 benchmarks: 403 to curl.
6. sell.amazon.com `/programs/deals` and `/tools/promotions` return 404; `/blog/coupons` and `/blog/holiday-selling` 302-redirect to sell.amazon.com/404. No article body is served.
7. Amazon Ads API guide `guides/rules/bidding-rules/schedule-bid-rules.md` (and the guessed `schedule-based.md` and `rules/overview.md` under bidding rules): 404 (NoSuchKey) on the cloudfront host. The schedule bid rule facts in this file come from the SP 3.0 OpenAPI instead.
8. arXiv: an API search for "Prime Day" returned no relevant paper.
9. (gap fill) EUR-Lex, Directive (EU) 2019/2161 and Directive 98/6/EC Article 6a: every URL form tried returned an empty HTTP 202 (a bot challenge), by curl and by WebFetch. The rule is quoted from the German statute and the CJEU release instead (F10).
10. (gap fill) Amazon Ads advertising-copy policy, `/resources/ad-policy/creative-acceptance/advertising-copy` in en-gb, de-de, fr-fr, it-it, es-es, pl-pl, sv-se, nl-nl, en-au and en-ca: each 301s to help GQBSYPQKDK5G9EQX, a sign-in JS shell. A web-search snippet describes an EU 30-day rule for price-reduction claims on ads; it is not stated in this file as Amazon's rule.
11. (gap fill) Seller Central help for Brand Tailored Promotions (the costs link on the sell.amazon.com page) and for Customer Engagement: Seller Central help shells, whose content comes only through the forbidden POST call. BTP fees are therefore not stated.
12. (gap fill) Amazon.com "Reference Pricing and Savings" (nodeId GQ6B6RH72AX8D2TD): 1.1 KB bot response to curl. The Amazon.nl page served no 30-day or Was Price text.
13. (gap fill) Jungle Scout, "2022 Seasonal Amazon Advertising Report" (PDF): fetched, but the PDF text extractor on this machine failed (a missing library), and the fetch tool could not read the binary. Its monthly figures are not used.
14. (gap fill) The Amazon Seller News post of October 16, 2026 on holiday returns: not located on a public URL; only PPC Land's quotation is used.

## Open questions

1. **Black Friday Week 2026 dates.** As of 2026-11-09 Amazon had not published them for the US (a web search that day found only forecasts); JP will publish on November 19. The places that carry them are `POST /sp/v1/events` and the aboutamazon page.
2. **Upfront deal fee: per promotion or per day?** The Holiday 2026 post says "$100 per promotion". A seller reports "$50 per day" at registration, and the Promotions API's `FeeFrequency` enum includes DAILY. Which applies to which deal type is unresolved. The fee snapshot of a given promotion is the record.
3. **Weekly recurrence in SP budget rules.** The schedule-based guide describes weekly recurrence for custom ranges, but the SP 3.0 model's RecurrenceType lists DAILY only, while the SD 3.0 model lists DAILY | WEEKLY. Untested here.
4. **Recommended events in Sponsored Display.** The guide says SP and SB only, and SD has no recommended-events endpoint. Yet the SD 3.0 budget-rule model carries `eventTypeRuleDuration` with a required `eventId` "available from the budget rules recommendation API". Whether an SP/SB event id is accepted on an SD rule is not stated.
5. **The PED price ceiling and reference-price rules** (the 30/60-day lookback mechanics, "lowest price in 30 days" style checks) are on Seller Central help pages this seat cannot reach. F4 confirms only that 30- and 60-day lookbacks exist and that PBDD prices are excluded from them for BFCM.
6. **How large reserve-price effects are at events.** Amazon's help wording, as quoted in the complaint, says placement value may differ in peak periods (E2); the complaint alleges larger peak surcharges and Texas alleges more than 25% at peak events (E3). Nothing public quantifies the effect for a seller. Whether the litigation will produce public data is unknown.
7. **The price-history tool's window.** Amazon's page says "up to 365 days of pricing insights"; Acadia describes a "30-day pricing range". It may be two views or a change; unresolved.
8. **Prime Day 2027 timing.** 2026 moved to June. Whether 2027 stays in June changes every YoY alignment (J3).
9. **SB Product Collection's end, and the automatic deals CTA (G2).** Two dates stand on Amazon's pages: January 2027 (create shutoff, in the Deprecations page and the migration guide) and February 2027 ("no longer be supported", release note of September 18, 2026). The migration guide says existing ads keep serving, with no end date. Whether the deals CTA applies to Manual or Automatic Collections is not stated in either guide.
10. **Ad Badger's claim of a 14-day SP click window** against Amazon's 7-day seller window (I2). This seat reads Amazon's docs as authoritative. Whether some seller accounts now show 14-day SP attribution in the console was not checked, because that needs sign-in.
11. **(gap fill) Brand Tailored Promotions fees and attribution.** The fee is on a Seller Central help page this seat cannot read. No page read says how a BTP redemption is shown in ad reports or AMC, or whether BTP audiences overlap with SD views/purchases audiences.
12. **(gap fill) Amazon Ads' own EU rule for savings claims in creative.** The advertising-copy policy is behind sign-in (Unreachable 10). The statute and the court bind the trader's announced reduction (F10). Whether Amazon's ad review applies the 30-day reference to SB headlines, SD/REC savings and the deal badge inside ads, and how, is not confirmed from a readable Amazon page.
13. **(gap fill) Amazon.de's reference-price page has no 30-day sentence**, while FR, ES, IT, BE, SE and PL do. Germany's statute (PAngV § 11) requires the 30-day low. Whether the DE page is incomplete, or Amazon.de shows the 30-day low on the detail page without stating it in help, was not checked: a product page is not read here.
14. **(gap fill) Black Friday Week 2026 in the UK and EU.** It was unannounced on 2026-11-09. The 2025 announcement came on November 13, a week before the start. The UK seller post's BFW deal cutoff (November 18) is the only 2026 date read.
15. **(gap fill) A Q5 CPC series.** No source read publishes CPC for December 26 to mid-January against the preceding weeks, with its sample. Evolve AMZ's "28% or more" CPM figure has no traceable dataset.

## Positions

**P-seasons-and-deals-1.** Prime Day 2026 ran June 23–26 (12:01 a.m. PDT to 11:59 p.m. PDT) in the 23 countries aboutamazon lists, and on Amazon Business in eight of them. Australia, Brazil, India and Japan shopped Prime Day later in the summer. Sources: [official] aboutamazon "Prime Day 2026 date"; Amazon Ads "Prime Day" events page; read 2026-11-09.

**P-seasons-and-deals-2.** Since 2019 Prime Day has started on dates from June 21 (2021) to October 13 (2020), and in 2026 it moved from July to June 23. It changed from 48 hours to 96 hours in 2025. Sources: [official] aboutamazon "The history of Prime Day"; "What makes Prime Day 2025 different"; read 2026-11-09.

**P-seasons-and-deals-3.** Prime Big Deal Days 2026 ran 48 hours on October 6–7, with "Today's Big Deals" dropping at midnight, 8 a.m. and 1 p.m. PDT. Source: [official] aboutamazon "Prime Big Deal Days FAQ", read 2026-11-09.

**P-seasons-and-deals-4.** Black Friday 2026 is November 27 and Cyber Monday November 30. Amazon had not published the US Black Friday Week dates on 2026-11-09, and Amazon Japan said it would announce its dates on November 19. Sources: [official] aboutamazon "When is Black Friday 2026? Here's everything you need to know"; "When is Cyber Monday 2026?"; aboutamazon.jp "Amazon ブラックフライデー 2026"; read 2026-11-09.

**P-seasons-and-deals-5.** `POST /sp/v1/events` returns the individual and grouped special events with suggested date ranges in the advertiser's marketplace, each with an `eventId`. Source: [official] Ads API SP 3.0 OpenAPI, read 2026-11-09.

**P-seasons-and-deals-6.** `POST /sp/campaigns/budgetRules/recommendations` with `EVENTS_FOR_EXISTING_CAMPAIGN` returns, per campaign, the events Amazon recommends and a `suggestedBudgetIncreasePercent` for each. Amazon chooses the events from the campaign's products, and the recommendations change when the products change. Sources: [official] SP 3.0 OpenAPI; Amazon Ads "Budget rules now available in Amazon advertising console globally"; read 2026-11-09.

**P-seasons-and-deals-7.** Recommended events in budget rules exist for Sponsored Products and Sponsored Brands only. A rule tied to an event whose dates are not yet announced is created with empty dates, which Amazon fills in when the dates are announced. Source: [official] Ads API "Schedule-based budget rules", read 2026-11-09.

**P-seasons-and-deals-8.** A schedule-based budget rule raises a campaign's daily budget by a set percentage for a date range or an event. Hours-of-day schedules are available only in US, CA, UK, IN and JP. Sources: [official] SP 3.0 OpenAPI (`budgetIncreaseBy`, `intraDaySchedule`); "Schedule-based budget rules"; "Hours of day now available for schedule-based budget rules"; read 2026-11-09.

**P-seasons-and-deals-9.** Performance-based budget rules evaluate the previous 7 days for sellers and 14 days for vendors. IS and NTB conditions are SB only, ACOS/CTR/CVR are SP and SD, and ROAS works on all three. Sources: [official] Ads API "Performance-based budget rules"; "Budget rules overview"; read 2026-11-09.

**P-seasons-and-deals-10.** A Sponsored Products schedule bid rule raises base bids by an integer 1–100% for a time pattern, a date range or an event id. "Recurring Events" bid rules are available only in JP, and "Individual Events" worldwide. Sources: [official] SP 3.0 OpenAPI (`/sp/rules/optimization`); Amazon Ads "Events for schedule bid rules, now available for Sponsored Products advertisers in the advertising console"; read 2026-11-09.

**P-seasons-and-deals-11.** Theme-based bid recommendations offer the event themes `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT` and `BFCM_HOLIDAY` alongside `CONVERSION_OPPORTUNITIES`. The bids are computed from recent winning bids for similar products, and the impact estimates assume the campaign does not run out of budget. The Ads API v1 unified bid recommendation carries the same four values in `Bid.theme`. Sources: [official] SP 3.0 OpenAPI; "Theme-based bid suggestions quickstart guide"; Ads API v1 merged OpenAPI; read 2026-11-09.

**P-seasons-and-deals-12.** The keyword recommendation API offers a `SPECIAL_DAYS` theme "during high sales events such as Prime Day, to anticipate an increase in sales and competition." Source: [official] SP 3.0 OpenAPI, read 2026-11-09.

**P-seasons-and-deals-13.** The initial budget recommendation for a new SP campaign returns up to five `specialEvents`, each with a recommended daily budget for the event period. Source: [official] SP 3.0 OpenAPI, read 2026-11-09.

**P-seasons-and-deals-14.** When a campaign exhausts its budget on an event day, its ads pause until midnight. Amazon names budget increases and budget rules set in advance as the means to keep it running. Sources: [official] sell.amazon.com "Prime Day tips"; Amazon Ads "Holiday advertising guide"; read 2026-11-09.

**P-seasons-and-deals-15.** The SP budget recommendation reports, for the last seven days, the share of time a campaign stayed in budget and lower/upper estimates of the impressions, clicks and sales it missed. Source: [official] SP 3.0 OpenAPI (`sevenDaysMissedOpportunities`), read 2026-11-09.

**P-seasons-and-deals-16.** For the 2025–2026 holiday, Amazon advises launching SP campaigns by early October and raising daily budgets 20–30% around Black Friday and Cyber Monday, starting three to five days ahead of each peak. These are Amazon's guidance figures, not limits. Source: [official] Amazon Ads "Holiday advertising guide", read 2026-11-09.

**P-seasons-and-deals-17.** Amazon describes the holiday season in three phases: build (October), peak (November through Cyber Monday) and extend (December and beyond). Source: [official] Amazon Ads "Holiday advertising guide", read 2026-11-09.

**P-seasons-and-deals-18.** Amazon states that the price an ad pays is set by hard and soft reserve prices together with competing bids, that reserves "are determined in real time and aren't predictable in advance by anyone, including Amazon or the advertiser", and that "In no scenario does an advertiser pay more than their bid." Amazon's help wording, as quoted in the complaint, adds that a placement "may have a different value during a peak shopping period than a non-peak period"; the FTC response itself does not mention peak periods. Sources: [official] aboutamazon "Amazon's response to the FTC's lawsuit regarding Sponsored Ads"; the Amazon Ads help wording as quoted in FTC et al. v. Amazon ¶¶147–148; read 2026-11-09.

**P-seasons-and-deals-19.** The FTC and 22 states allege that Amazon raised reserve-price surcharges during high-velocity events (Prime Day, Prime Early Access, Prime Big Deal Days, Thanksgiving through Christmas) and ramped them in before peaks. Texas, suing separately the same day, alleges soft reserves lift the winner's cost toward its maximum bid by roughly 17% on ordinary days and more than 25% at peak events like Prime Day. Amazon disputes the allegations, and none has been tested in court. Sources: [opinion] FTC et al. v. Amazon complaint ¶¶68–72, 219–226 (filed 2026-08-31); [opinion] Texas Attorney General press release, Aug 31, 2026; [official] Amazon's response; read 2026-11-09.

**P-seasons-and-deals-20.** Marketplace Ad Pros measured Prime Day 2026 median SP CPC at +10% ($1.19 to $1.31) and SB at +2% against matched pre-event days across several hundred US advertisers. Skai measured Prime Day 2025 CPC at $1.80, down 10.4% from 2024, in a same-store cohort. Sources: [opinion] Marketplace Ad Pros "Prime Day 2026 Ad Benchmarks"; Skai "Prime Day 2026 Preview"; read 2026-11-09.

**P-seasons-and-deals-21.** In the Marketplace Ad Pros Prime Day 2026 data, 51% of advertisers cut SP budgets and 13.7% raised them by 20% or more. Budget raisers and holders showed the same 1.30x ad-sales lift, which the authors call correlational. Source: [opinion] Marketplace Ad Pros "Prime Day 2026 Ad Benchmarks", read 2026-11-09.

**P-seasons-and-deals-22.** Ad Badger recommends 1.5–2.5x budgets in the two days before a Prime event and 2–3x on event days. Amazon's holiday guide and Florian Nottorf (Adference) give +20–30%, starting 3–5 days ahead. Sources: [opinion] Ad Badger "Prime Big Deal Days 2026 PPC Playbook: Bids & Budgets"; [official] Amazon Ads "Holiday advertising guide" and "Prime Day 2026: Advanced advertising strategies" (Nottorf quote); read 2026-11-09.

**P-seasons-and-deals-23.** Amazon's holiday "myths" page says conversion rates often drop during major sales events while shoppers browse, and that a temporary ACOS spike is read against TACOS, which "reveals whether your total sales (organic and paid) are growing in relation to your ad spend". Ad Badger reports impressions rising while clicks and conversions stay flat in the 48 hours before a Prime event. Sources: [official] Amazon Ads "Holiday advertising myths: What experts want you to know"; [opinion] Ad Badger; read 2026-11-09.

**P-seasons-and-deals-24.** Sponsored Products attributes seller conversions over 7 days and vendor conversions over 14. SB and SD attribute over 14 days, click or view. Conversions are dated to the ad interaction and restated 1, 7 and 28 days after the conversion. [seat, computed] A 14-day window can therefore change for up to 42 days after the interaction date. Sources: [official] Ads API "Purchases (Amazon retail conversions)"; "Reporting v3 columns"; "Reporting v3 FAQ"; "Ads API v1 reporting overview"; read 2026-11-09.

**P-seasons-and-deals-25.** Amazon advises checking 7–14-day attribution before changing campaigns after a peak, because peak-event sales often occur days after the click. Marketplace Ad Pros found the clicks of June 26 (the last day of Prime Day 2026) fully mature around July 10. Sources: [official] Amazon Ads "Holiday advertising myths: What experts want you to know"; [opinion] Marketplace Ad Pros; read 2026-11-09.

**P-seasons-and-deals-26.** Ads API v1 reports aggregate days in each campaign's time zone, and hourly data is retained for 14 days. Amazon announces event times in PDT, so an event's first and last hours fall on different report dates in campaigns set to other time zones. Sources: [official] Ads API "Dates and historical data retention"; aboutamazon event pages; read 2026-11-09.

**P-seasons-and-deals-27.** A Lightning Deal runs 4–12 hours, as Amazon determines; a Best Deal runs several days. Both need a Professional plan and a four-star seller rating, and both can carry a Deals badge. Coupons need a 3.5-star rating, hold up to 200 ASINs and expire after 90 days. Price discounts run up to 30 days on limited units. Source: [official] sell.amazon.com "Seller promotions" (May 27, 2026), read 2026-11-09.

**P-seasons-and-deals-28.** A coupon shows a coupon badge with the discount amount in shopping results. Amazon's Prime Day coupon criteria are a discount above 5%, dates coinciding with Prime Day, and the audience set to Prime members. Source: [official] sell.amazon.com "Prime Day tips", read 2026-11-09.

**P-seasons-and-deals-29.** For holiday 2026, Amazon accepted Prime Big Deal Days deals July 8–September 8 and Black Friday Week/Cyber Monday deals July 8–October 20. Best Deals, Lightning Deals and Prime Exclusive Price Discounts cost $100 per promotion plus 1.5% of promotional sales, capped at $5,000. Source: [official] Seller Forums News_Amazon "Holiday 2026: Same fees, same eligibility, earlier deadlines", read 2026-11-09.

**P-seasons-and-deals-30.** Prime Big Deal Days 2026 promotional prices are excluded from the 30- and 60-day lookback windows that set the maximum deal price for Black Friday Week and Cyber Monday. Source: [official] Seller Forums "Holiday 2026: Same fees, same eligibility, earlier deadlines", read 2026-11-09.

**P-seasons-and-deals-31.** Responsive eCommerce Creative renders a deal badge automatically when the product qualifies for Deal of the Day, a Lightning Deal or a Best Deal, and at BFCM a BFCM badge. Deal badging appears only on the "Shop now" variation, and the custom headline may not contain a price or deal. Sources: [official] Amazon Ads "Holiday shopping season performance-boosting tips"; "Black Friday and Cyber Monday advertising tips"; read 2026-11-09.

**P-seasons-and-deals-32.** A Sponsored Brands product collection featuring products on deal automatically shows a deals call-to-action and a seasonal lifestyle image. Since August 2026, a request to create a Product Collection ad creates a Manual Collection ad instead. Amazon dates the format's end twice: create requests return an error after January 2027 (Deprecations page, migration guide), and "Beginning February 2027, product collections will no longer be supported" (release note of September 18, 2026). Sources: [official] Amazon Ads "Key events store prep"; Ads API "Deprecations"; "Migration Guide for Product Collection to Collections Ad Type"; Ads API release notes, "Introducing the ListMigrations API..."; read 2026-11-09.

**P-seasons-and-deals-33.** Amazon's ad policy requires an advertised deal to be live whenever the ad is live (no deal teasing). The price or saving must appear in the same format on ad and landing page. Event names are bounded by duration ("available on Black Friday only" means 24 hours; "Black Friday Week" about 8 days, beginning 8 days before and ending by the last day of the event). Source: [official] Amazon Ads "Black Friday and Cyber Monday advertising tips", read 2026-11-09; the "Black Friday Week" length is Amazon Ads' "Event days" policy, read 2026-11-10.

**P-seasons-and-deals-34.** An "up to X%" claim requires at least 10% of the promoted ASINs to be offered at or above X%. A claim made inaccurate by dynamic pricing requires the creative to be paused and changed to a qualified claim. Source: [official] Amazon Ads "Holiday shopping season performance-boosting tips", read 2026-11-09.

**P-seasons-and-deals-35.** Brand Store promotional messaging is allowed only with the Featured Deals widget, which needs at least four ASINs. Sales-event content may start no more than seven days before the event and must be removed within 24 hours after, and a Store version must be submitted at least 48 hours ahead. Store pages may not name Amazon events ("Prime Day Brand Store") or numerical discounts. Sources: [official] Amazon Ads "Black Friday and Cyber Monday advertising tips"; "Key events store prep"; read 2026-11-09.

**P-seasons-and-deals-36.** The SP-API Promotions API (2025-12-01) lists a seller's promotions by type (DEAL, PRICE_DISCOUNT, COUPON, BASKET_BUILDING) and status. Each carries `schedule.eventId` (for example "Prime Day"), Prime-exclusive customer segments, whether the badge displays on the website, a stacking flag and a fee snapshot. Source: [official] amzn/selling-partner-api-models `promotions_2025-12-01.json`, read 2026-11-09.

**P-seasons-and-deals-37.** Data Kiosk's week-level `yearOverYear` benchmark compares the same ISO week number in the prior year, and month-level compares the same calendar month; no benchmark exists at day level. Prime Day 2026 (ISO week 26) and Prime Day 2025 (ISO week 28) therefore fall in different benchmark weeks. Sources: [official] SP-API "Seller analytics dataset guide"; aboutamazon "The history of Prime Day"; [seat] week numbers computed from the dates.

**P-seasons-and-deals-38.** Search Query Performance reports run on Sunday–Saturday weeks, calendar months or quarters, and a request cannot span periods. They return `searchQueryVolume`, impression, click, cart-add and purchase shares and median click prices per query. Brand Analytics data usually goes back three years and arrives within about three days. Sources: [official] SP-API "Report type values – Analytics"; sell.amazon.com "Brand Analytics"; read 2026-11-09.

**P-seasons-and-deals-39.** Sponsored Display audiences can target viewers of products with look-backs of 7, 14, 30, 60 or 90 days, and purchasers with look-backs up to 365 days. Amazon's post-event guide (quoting Nottorf) advises "views remarketing" to re-engage event browsers in the week after. Sources: [official] Ads API SD 3.0 OpenAPI; Amazon Ads "Post-event advertising strategy"; read 2026-11-09.

**P-seasons-and-deals-40.** Practitioners disagree on post-event spend. Pare says hold ad velocity for 48–72 hours and retarget detail-page viewers at 20–30 days. Ad Badger says return bids to normal the day after and run SD retargeting for days 1–7. Acadia says its going-dark tests show "consistently thin post-event lift" and trims lead-out media to the minimum. Sources: [opinion] Pare; Ad Badger; Acadia; read 2026-11-09.

**P-seasons-and-deals-41.** Acadia reports that brands running no deals saw a 46% lift over their 30-day baseline at Prime Day 2025 and 116% at Prime Day 2024. It says that in 2026 the visibility gap made non-participation "a penalty". Source: [opinion] Acadia "Amazon Prime Day 2026 – The Results", read 2026-11-09.

**P-seasons-and-deals-42.** Acadia states that Prime Day 2026's lift over the pre-event run rate was smaller than 2025's because the 2025 baseline week (after July 4) was unusually low. Acadia treats YoY growth, not period-over-period lift, as the comparable figure across the two events. Source: [opinion] Acadia, read 2026-11-09.

**P-seasons-and-deals-43.** Amazon's 137% (Prime Day 2025) and 145% (holiday 2025) "increase in sales" figures compare advertisers with average category growth, over tentpole windows against the adjacent preceding weeks. Sources: [official] Amazon Ads "Prime Day 2026: Advanced advertising strategies"; "Holiday advertising guide"; read 2026-11-09.

**P-seasons-and-deals-44.** Since October 20, 2026, the AMC Amazon Retail Purchases dataset carries coupon, point-of-sale and price-discount columns (with Best Deal, Deal of the Day and Lightning Deal types), with history since September 24, 2024. Amazon says this lets advertisers separate the effect of media from the effect of deals. It covers only vendor- or seller-funded promotions, excluding Subscribe & Save, Amazon-funded promotions and loyalty points. Sources: [official] Ads API "Ads API v1 release notes"; "AMC Amazon Retail Purchases (paid)"; read 2026-11-09.

**P-seasons-and-deals-45.** Store-level scanner research estimates the post-promotion dip at 4–25% of the promotion's current sales effect, a dip that simple models and visual inspection usually miss. Source: [research] Van Heerde, Leeflang and Wittink (2000), *JMR* 37(3), abstract read 2026-11-09.

**P-seasons-and-deals-46.** Panel research over 8¼ years found consumers become more price- and promotion-sensitive as promotions increase and advertising falls. Amazon's own guide states that regular promotions "can condition customers to wait for deals". Sources: [official] Amazon Ads "Sales promotion guide"; [research] Mela, Gupta and Lehmann (1997), *JMR* 34(2), abstract; read 2026-11-09.

**P-seasons-and-deals-47.** In India the Great Indian Festival runs for weeks across the festival calendar; the 2026 event continued through November 10. Amazon reported seller sales of up to 3.5x business-as-usual in its first week. Sources: [official] aboutamazon.in "Amazon Great Indian Festival"; "Seller growth during Great Indian Festival 2026"; read 2026-11-09.

**P-seasons-and-deals-48.** On Amazon Business, the bid adjustment for business shoppers goes up to 900%. Amazon suggests starting at 20%–120% for Prime Day and a 20–50% increase for about two weeks around the holidays. Sources: [official] Amazon Ads "Prime Day 2026: Advanced advertising strategies"; "Holiday advertising guide"; read 2026-11-09.

**P-seasons-and-deals-49.** The Ads API v1 target model offers theme targets `KEYWORDS_RELATED_TO_PRIME_DAY` ("Search terms that shoppers are likely to use during Prime Day"), which "will only match queries through the end of Prime Day", and `KEYWORDS_RELATED_TO_GIFTS`. The SP 3.0, SB 3.0 and SB 4.0 specs read here do not carry the Prime Day theme. Source: [official] Ads API v1 merged OpenAPI (`themeTarget.matchType`), read 2026-11-09.

*Positions added in the gap fill, 2026-11-09:*

**P-seasons-and-deals-50.** Amazon's 2026 spring event ran March 10–16 in 13 European countries ("Spring Deal Days" in the UK, "Frühlingsangebote" in Germany), against March 25–31 for the US Big Spring Sale. Sources: [official] About Amazon UK "Amazon Spring Deal Days returns with seven days of savings"; Amazon Press Center DE "Kräftig sparen zum Saisonstart..."; aboutamazon "Big Spring Sale FAQ"; read 2026-11-09.

**P-seasons-and-deals-51.** Prime Big Deal Days 2026 ran October 6–7 in 22 countries. It started at 12:01 a.m. BST in the UK and 12:01 a.m. CET on the EU page, against 12:01 a.m. PDT in the US, and Germany calls it "Prime Deal Days". The German release adds that dates may vary by country. Sources: [official] About Amazon UK "Amazon Prime Big Deal Days 2026: Deal event returns to the UK from 6 to 7 October"; About Amazon EU "Prime Big Deal Days is back October 6-7"; Amazon Press Center DE "Die Prime Deal Days kehren am 6. und 7. Oktober zurück..."; aboutamazon "Prime Big Deal Days FAQ"; read 2026-11-09.

**P-seasons-and-deals-52.** Black Friday Week 2025 ran November 20 to December 1 in the UK and Germany (12 days, from 00:01 local time in Germany), announced on November 13, 2025. No 2026 UK or German dates were published by 2026-11-09. Sources: [official] Amazon Press Center UK "It's the Season for Savings..."; Amazon Press Center DE "Der Countdown läuft: Die Black Friday Woche kehrt vom 20. November bis zum 1. Dezember zurück"; About Amazon UK and Deutschland news pages as read 2026-11-09.

**P-seasons-and-deals-53.** For holiday 2026 in the UK and EU, Amazon accepted Prime Big Deal Days deals until September 23 and Black Friday Week deals until November 18, with 30% off the upfront fee for early submission. The fees are £12 plus 0.75% (cap £600) in the UK, €16 plus 0.75% (cap €1,000) in Germany, and €10 plus 0.5% (cap €300) in France, Italy and Spain. Prime Exclusive Discounts there need a 3.5-star rating. Source: [official] Seller Forums UK, News_Amazon "Peak season 2026: Inventory dates, peak fees, deal cutoffs and promotions", read 2026-11-09.

**P-seasons-and-deals-54.** Amazon's holiday guide defines the third phase, "December and beyond", by the shoppers it names: "last-minute gift shoppers and post-holiday deal seekers", visitors "who browsed but didn't purchase during peak events", and seasonal buyers to turn into repeat customers. Its New Year guide adds January resolution shoppers. No Amazon page read uses the term "Q5" or describes CPC after December 25. Sources: [official] Amazon Ads "Holiday advertising guide"; "New Year's Ads: 5 Marketing Campaign Ideas to Inspire in 2024"; read 2026-11-09.

**P-seasons-and-deals-55.** In Amazon's post-event teaching scenario for a fashion brand, "Extend holiday deals into January and maintain Sponsored Brands investment" is the answer marked incorrect. The answer marked correct moves budget to high-performing branded terms and repositions seasonal stock with non-holiday messaging. Source: [official] Amazon Ads "Post-event advertising strategy" (hypothetical scenarios), read 2026-11-09.

**P-seasons-and-deals-56.** Practitioners call December 26 to mid-January "Q5". Evolve AMZ (Ian Smith) says CPMs "commonly fall 28% or more against the Q4 peak" as seasonal advertisers exit, and that gift-card redemption concentrates in that window; Pattern says CPCs go down. Against this, Ad Badger's app data puts January 2026 at the year's highest ACOS (32.5%, against 28% in October 2025). Intentwise's data has conversion falling from 13.4% in the week ending December 23 to 11.03% the following week. Sources: [opinion] Evolve AMZ "Amazon Q5 Explained"; Pattern "Amazon Advertising Post-Holiday"; Ad Badger "Amazon Advertising Benchmarks 2026"; Intentwise "Guide: Ad tactics for the week after Christmas"; read 2026-11-09.

**P-seasons-and-deals-57.** Teikametrics (Andrew Waber) reported, across more than 700 sellers in 2019, that ad conversion rates rose and cost per conversion fell from Cyber Monday to the December 22 shipping cutoff, and attributed this to brands that had spent their seasonal budgets by then. Source: [opinion] MarTech "Amazon ad spend rises over Cyber 5, but most efficient sales days still ahead", read 2026-11-09.

**P-seasons-and-deals-58.** Brand Tailored Promotions are available to Brand Representatives in Brand Registry in the US, UK, Spain, France, Italy, Germany and Japan. They offer 10–50% off the catalog or chosen ASINs to an audience of at least 1,000 shoppers, chosen by goal: new-customer acquisition (brand clicks or cart adds in the last 90 days without purchase), re-engagement, retention (repeat purchasers, highest spenders of the last 12 months) and cross-sell. Each eligible customer redeems once. Source: [official] sell.amazon.com "What are Amazon Brand Tailored Promotions?" (Jan 20, 2026), read 2026-11-09.

**P-seasons-and-deals-59.** A Brand Tailored Promotion must start at least 48 hours after creation and within 60 days, and end within 90 days of its start. A brand can hold 20 active or scheduled at once. Once live, only its budget can change, and only upward. It shows a green badge only to the audience, and it stacks with coupons, the highest promotion code applying. Amazon names Prime Day and Black Friday as occasions for it. Its fees are stated only on a Seller Central help page. Source: [official] sell.amazon.com "What are Amazon Brand Tailored Promotions?", read 2026-11-09.

**P-seasons-and-deals-60.** At launch in August 2023, Brand Tailored Promotions named six audiences: brand followers, repeat customers, recent customers, high-spend customers, potential new customers, and cart abandoners ("haven't purchased in the last three months"). Source: [official] sell.amazon.com "Brand Tailored Promotions: Offer exclusive discounts for loyal customers" (Aug 1, 2023), read 2026-11-09.

**P-seasons-and-deals-61.** The Customer Engagement tool sends free marketing emails, which Amazon itself delivers, to a Brand Registry brand's followers and, since 2022, to its repeat, recent and high-spend customers. It reports open rate, click-through, delivered emails, opt-outs, sales and conversion. Amazon says brands with 1,000 or more followers "will have the best experience". Sources: [official] Amazon Press Center "Amazon Launches Free Email Marketing Capabilities for Sellers..." (Sep 14, 2022); Seller Forums News_Amazon "Create engaging email campaigns with themed templates in 'Customer Engagement' (beta) tool"; read 2026-11-09.

**P-seasons-and-deals-62.** The SP-API Promotions API (2025-12-01) is read-only (GET) and for sellers. It can return a promotion's customer segments, where `segmentType` `BRAND` is a "Brand-tailored audience" with a `brandId`, when `includedData=CUSTOMER_SEGMENTS` is requested. It has no Brand Tailored Promotions promotion type, and no operation read creates or reports BTP or Customer Engagement. Sources: [official] amzn/selling-partner-api-models `promotions_2025-12-01.json`; SP-API "Promotions API"; read 2026-11-09.

**P-seasons-and-deals-63.** Practitioners disagree on which Brand Tailored Promotions audience works best. Joe Stefani (Desert Cactus) reports recent customers with about 3x the redemption share of the next audience, while Intentwise says many agencies favour cart abandoners. Acadia says about 42% of its clients relaunched BTP after Prime Day 2026. None publishes a holdout test. Sources: [opinion] Intentwise "Explained: What is Brand Tailored Promotions?"; Acadia "Amazon Prime Day 2026 – The Results"; read 2026-11-09.

**P-seasons-and-deals-64.** German law requires every announced price reduction to state the lowest price applied in the prior 30 days. The EU Court of Justice held that a reduction announced as a percentage, or as a statement stressing an advantageous price, must be computed from that 30-day low. Sources: [law] PAngV § 11; CJEU Press Release No 152/24 (Case C-330/23 Aldi Süd, 26 September 2024); read 2026-11-09.

**P-seasons-and-deals-65.** Amazon's French, Spanish, Italian, Belgian, Swedish and Polish stores state that for price-reduction announcements such as limited-time promotions they display the product's lowest price on that store in the 30 days before the reduction. On the same pages, the "Was Price" is a 90-day median excluding promotional prices. Amazon.co.uk shows "Lowest price in 30 Days" when the current price is at or below the lowest featured-offer price of the past 30 days. Source: [official] Amazon customer help "Reference Pricing and Savings" on amazon.fr, .es, .it, .com.be, .se, .pl and .co.uk, read 2026-11-09.

**P-seasons-and-deals-66.** Amazon.de's reference-price help page states that event badges such as Black Friday can be added to a deal that was not badged before. A badge added without a price change means the deal was already active. The page carries no 30-day sentence. Source: [official] Amazon.de "Referenzpreise und Ersparnisse" / "Reference Pricing and Savings", read 2026-11-09.

**P-seasons-and-deals-67.** The Munich I Regional Court ruled Amazon's October 2024 "Prime Deal Days" price advertising unlawful where discounts were computed from the RRP or a customer average price rather than the 30-day low. Amazon said it would appeal. Source: [opinion, press report of a ruling] heise online "Court: Amazon must label special offers more transparently" (July 16, 2025), read 2026-11-09.

**P-seasons-and-deals-68.** In the AMC Amazon Retail Purchases dataset, `price_discount_amt` is measured against the product's average selling price over the 90 days before the promotion. Amazon says the promotional columns let advertisers "separate the effect of their media from the effect of their deals". The dataset is queryable at no cost from June 1 to December 31, 2026. Sources: [official] Ads API "AMC Amazon Retail Purchases (paid)"; "Ads API v1 release notes"; read 2026-11-09.

**P-seasons-and-deals-69.** A review of marketing studies found that price advertising raises consumers' price sensitivity and lowers prices, while non-price advertising lowers price sensitivity. Source: [research] Kaul and Wittink (1995), *Marketing Science* 14(3), G151–G160, abstract read 2026-11-09.

**P-seasons-and-deals-70.** Across 70 brands in 25 product categories in France, over five years of advertising and scanner data, the total sales elasticity of discounting was .04 and of advertising .13, against 1.37 for product and .74 for distribution. Discounting's long-term effect was one-third of its short-term effect, while the other instruments' long-term effects exceeded four times their short-term effects. Source: [research] Ataman, van Heerde and Mela (2010), *JMR* 47(5), 866–882, abstract read 2026-11-09.

**P-seasons-and-deals-71.** In scanner-panel data for four categories, advertising raised marginal consumers' willingness to pay for 17 of 18 brands. A lower equilibrium price after advertising is therefore consistent with advertising raising each consumer's willingness to pay. Source: [research] Erdem, Keane and Sun (2007), SSRN 965468, abstract read 2026-11-09.

**P-seasons-and-deals-72.** Amazon defines TACOS on two Amazon Ads pages: "TACOS shows your ad spend as a percentage of total sales", and TACOS "reveals whether your total sales (organic and paid) are growing in relation to your ad spend". Neither names the sales field, the ad products or the dates in the ratio. Sources: [official] Amazon Ads "The author's guide to Sponsored Products"; "Holiday advertising myths: What experts want you to know"; read 2026-11-09.

### Seat's positions (enter no skill)

- **S1.** [seat] Because CPC at events can move through reserves, through competing bids, or both, and no seller report separates them (E1–E4), the CPC/bid ratio per target before and during an event is the one observable a seller has. Ad Badger's 0.90–1.00 versus 0.50–0.75 bands are its own reading, not Amazon's.
- **S2.** [seat] Three facts together mean an event's ad results are not final until about 4–6 weeks after the last event day: the SP seller window (7 days) and SB/SD window (14 days); restatement at 28 days; and the 14-day hourly retention. "Same-day ACOS" during the event is, by construction, missing most of its sales.
- **S3.** [seat] Year-over-year comparison by ISO week (Data Kiosk) or by calendar month misaligns whenever the event moves (2025 week 28, 2026 week 26). An event-to-event comparison keyed on the dates from `POST /sp/v1/events` or aboutamazon is the aligned comparator. Acadia's YoY-versus-lift point (P-42) is the same problem in practitioner form.
- **S4.** [seat] Practitioners agree on only one recommendation, that budgets should not cap out on event days. Amazon's figures support it (pause until midnight; missed-opportunity estimates). The multiplier sizes (1.2x to 3x) are opinions with no controlled support, and the only data on budget raisers (Marketplace Ad Pros) found no lift difference.
- **S5.** [seat] Most deal-in-ad surfaces (REC badges, SB product-collection deal CTA, Store All Deals page) are automatic, so what decides whether an ad shows a badge is the deal's eligibility and validation on the retail side, not any ad setting. Acadia's report of a discount live without the event badge is consistent with that.
- **S6.** [seat] PBDD and BFCM sit in the same ISO weeks across 2025–2026 (41 and 48), so week-level YoY is better aligned for Q4 events than for summer Prime Day.
- **S7.** [seat] At a tentpole event the deal, the event's traffic and any ad change start together. A same-event before/after cannot apportion the lift among them. The AMC promotional columns (a within-event split of exposed and unexposed, promotional and full-price purchases) and an event-to-event comparison keyed on event dates are the two designs Amazon's data permits; R7–R10 give the reasons.
- **S8.** [seat] In an EU store, a price held low in the 30 days before an event lowers the reference the event's claimed reduction is measured against (PAngV § 11, CJEU C-330/23, Amazon's FR/ES/IT/BE/SE/PL pages). A coupon or price discount run in the month before Black Friday therefore shrinks the percentage a Black Friday deal or ad can claim there. The US lookbacks (F4) are Amazon's own rules and differ.
- **S9.** [seat] BTP, Customer Engagement and SD remarketing all address shoppers who have already viewed, carted or bought the brand. Running two of them on the same audience in the same window means the discount and the ad compete for credit for the same purchase, and no Amazon report read separates them.

## Verification

Verified 2026-11-09 by an adversarial verifier seat.

**Method.** The file was read whole, then every cited page was re-opened on 2026-11-09 by a plain GET with a browser user agent, its HTML stripped and searched for each claim's words; nothing was saved to disk. Ads API guides were read as markdown on the cloudfront docs host (d3a0d0y2hgofx6.cloudfront.net), the OpenAPI specs from the cloudfront spec hosts (SP 3.0, SB 3.0 and 4.0, SD 3.0, the v1 merged spec), parsed as JSON/YAML and searched by schema name and enum. The complaint PDF was parsed in memory. Paper abstracts were read through the Crossref API. A web search checked for 2025–2026 Amazon announcements that overturn a claim (none found; the US Black Friday Week 2026 window was still unannounced). Every quoted string was matched verbatim; page names were taken from each page's own title or headline. No Ads API host (advertising-api*.amazon.com), Login with Amazon, Amazon Ads MCP endpoint, SP-API host or Seller Central help-hub content call was made, and no page behind sign-in was read.

**Corrections (was → now).**

1. A1 quote "Prime Day 2026 will start June 23 at 12:01 a.m. PDT and run through June 26" → aboutamazon's actual words ("runs from June 23 at 12:01 a.m. PDT through June 26") and the Ads events page's ("Amazon's 2026 Prime Day event will start June 23..."); noted that the Ads events page's country list omits South Africa.
2. Stable 1 "five different week slots and three lengths since 2019" → five ISO start weeks (25, 26, 28, 29, 42) and two lengths (48 hours 2019–2024, 96 hours from 2025).
3. A3 paraphrased quote "12:01 a.m. PDT Tue Oct 6 to 11:59 p.m. PDT Wed Oct 7" → the page's verbatim sentence.
4. A5 quote "Customers can shop early deals in the Holiday Shop now. Check back soon" → the verbatim sentence (with Alexa for Shopping); page name → "When is Black Friday 2026? Here's everything you need to know"; the Cyber Monday 2025 URL "serves" → redirects to .../when-is-amazon-cyber-monday-faq.
5. A7 "the same page lists" the JP new-life sale, New Year sale and a "Prime Day Stage" → the page's related-news links; the Stage is a four-day venue event at Roppongi Hills, not a sale.
6. A8 2025 Great Indian Festival dates → attributed to the hub page's cards, not the 2026-dates page; page names corrected.
7. B2 "cost controls in Sponsored Brands and display were associated with a 2.6X uplift" → the figure is for "cost controls in their display ads campaigns" only; "Keyword Groups beta" → "Keyword Groups for Sponsored Brands and display ads"; 137% baseline "across 21 countries" → the 20 marketplaces the footnote lists.
8. B guides "The 2025 guides for Halloween, Mother's Day, New Year and Lunar New Year" → their titles carry 2024 (Mother's Day undated); table page names corrected to the titles.
9. Mother's Shea blog: page name "Retail tentpole events to drive year-round results" → "How retail tentpole moments can deliver year-round results"; quote completed (2022 against 2021).
10. B12 "Alexa for Shopping (formerly Rufus)" was unsourced on the unBoxed page → sourced to aboutamazon "'Amazon Rufus' AI experience..." ("On May 13, 2026, Rufus was renamed Alexa for Shopping").
11. C2 "When dynamic budget control launched" and page name "Dynamic budget control" → "Budget rules now available in Amazon advertising console globally" (Aug 12, 2021).
12. Page names: "Hours of day available for..." → "Hours of day now available for schedule-based budget rules"; "Sponsored Brands performance-based budget rules" → "New metrics available for Sponsored Brands performance-based budget rules"; "Event-based bid rules for Sponsored Products advertisers" → "Events for schedule bid rules, now available for Sponsored Products advertisers in the advertising console"; "Schedule-based bid rules available for Sponsored Products" → "Schedule based bid rules now available for Sponsored Products"; Target Promotion, Brand Store Creative, Tinuiti, Ad Badger and Pare titles → the pages' own titles.
13. C4/C7 "Sponsored Display has `/sd/budgetRules` but no recommended-events endpoint" → SD also has `/sd/campaigns/budgetRecommendations` and `/sd/campaigns/budget/usage`, and its budget-rule model carries `eventTypeRuleDuration` (eventId) and RecurrenceType DAILY | WEEKLY; open questions 3 and 4 updated to match.
14. C9 "The Ads API v1 merged spec has no budget-rule or event endpoints" → no budget-rule, event-list or optimization-rule endpoints, but `Bid.theme` (PRIME_DAY, FALL_PRIME_DEAL_EVENT, BFCM_HOLIDAY, CONVERSION_OPPORTUNITIES) and theme targets `KEYWORDS_RELATED_TO_PRIME_DAY` / `KEYWORDS_RELATED_TO_GIFTS`; `/adsApi/v1/create/events` identified as Event Manager. Added to Stable 5, P-11, the run-time table and new P-49.
15. D4 "v3 was deprecated May 15, 2025" → sourced to the Deprecations page (the spec still lists v3).
16. E1/E4/Stable 8/P-18 "Amazon states that reserves may differ between peak and non-peak periods" / "Both sides agree" → the peak wording is only in help text quoted by the complaint (¶¶147–148); Amazon's FTC response does not mention peaks. "Aren't predictable in advance" kept, attributed to the FTC response.
17. E3 "An internal SB memo ... (2019)" → an internal 2021 document, "Pricing Introduction" (¶157), whose quoted passage does not name the Black Friday year.
18. E3 "Texas filed a separate suit the same day (press reports via search)" → the Texas AG press release, read and cited [opinion] (17% ordinary days, more than 25% at peak events, own bid nearly 80% of the time); added to P-19 and the CPC disagreement note.
19. G5 "11.11" → the page's "11:11", with the "11:11 only" duration.
20. G6 "Sponsored ads additional policies ... event-specific content is the same as above" → contractual terms with no deal or event content; the Ad policy hub row "Policy index" → 301 to the Amazon Ads home page.
21. I6 AMC retention and modeled NTB → the release notes' wording (traffic events beyond 13 months, up to 5 years, backfilled to June 2023; modeled conversions in the NTB metric columns); promotional-column 2-year history and self-funded-only scope added; P-44 aligned.
22. J2 "The SQP dashboard can be filtered for a specific week, month, or quarter" → that line is about the Demographics dashboard; the three-years/three-days sentence sits in the Demographics section.
23. R5 "the page read here shows the citation only" → the publication page shows the abstract with the 26.24% / 8.7% MAE figures (WACV 2024 workshop).
24. Practitioners: Skai "First half versus second half" → year-over-year lifts per half, with the missing CPC −5.2% and clicks +19.7%; Skai spend-share figures (SD 2.6%→1.3% and SB 17.4%→10.9% mis-paired) → the three-year rows as published.
25. Practitioners: Pacvue "+70% (year context unclear)" → Acadia's Prime Day 2024 recap, 2024 against 2023; Pare's CPC range → Pare's statement citing Fishman's analysis; Bryan Cohen's 100 clicks → per book, for KDP authors; Ad Badger phase 1 "Up to three days before" → "now to October 3"; Ad Badger's "reports are built by order date" claim flagged against I3.
26. Amazon's ACOS-vs-TACOS page "quotes Mellott, Java, Carnati and de Guigné on judging peak ACOS against TACOS" → only Mellott is quoted on that; the other three speak on other topics.
27. Post-event "Amazon's own guide says 'Engage warm leads...'" → Florian Nottorf (Adference), quoted in Amazon's guide.
28. Run-time tables: the restatement row "re-pull after 1, 7 and 28 days past the last event day" (a schedule) → the fact that restatement happens 1, 7 and 28 days after the conversion; "A skill pulls them each season and records the read date" (behaviour) → the pages are dated per season. P-24's 42-day figure tagged [seat, computed]. Open question 1's "A skill reads ... on the day" → the places that carry the dates.

**Removals.** None of the claims was removed outright; the unsupported parts were rewritten as above (the "same as above" policy claim, the 2019 memo date, the press-report Texas claim, and the three misattributed practitioners on ACOS vs TACOS).

**Stayed unreachable** (re-tried 2026-11-09): Amazon Ads help center pages GNSMLANWNF344YBE, GQ3SJ5QCWCQCKCYQ and the auction help (200 with a sign-in JS shell); ad-policy pages amazon-branded-peak-events, black-friday-cyber-monday-policies, creative-acceptance and sponsored-ads-policies (301 to help shells or ad-specs); the eight Seller Central help pages (content only via the forbidden POST call); Pacvue's hourly-optimization post and Triple Whale's Big Deal Days 2026 page (403); sell.amazon.com /programs/deals and /tools/promotions (404) and /blog/coupons and /blog/holiday-selling (302 to /404); the cloudfront `bidding-rules/schedule-bid-rules.md` guide (404). The Texas petition itself was not read.

### Gap fill 2026-11-09

Done by the research seat on 2026-11-09, against the four gaps and two contradictions raised by three completeness critics. Same method as above: plain GET with a browser user agent, HTML stripped in memory, PDFs parsed in memory, Ads API pages as cloudfront markdown, the Promotions model from the amzn GitHub repository, paper abstracts through the Crossref API. No Ads API host, Login with Amazon, Amazon Ads MCP endpoint, SP-API host, Seller Central help-hub POST call or sign-in page was called.

**Added.**
1. Gap 1 (Q5). Added H5: Amazon's phase 3 "December and beyond" wording; the trends page's Mintel 31% and gift cards 54%; the New Year guide; the post-event scenario marking "Extend holiday deals into January" incorrect; B2B and fee windows; the January 31 returns window, from the press. Added practitioners §7: Evolve AMZ, Ad Badger, Intentwise, Pattern, Teikametrics/MarTech and Pacvue/Helium 10, with the disagreement (cheaper traffic against lower conversion and the year's highest ACOS in January). Also Stable 20, Open question 15, P-54 to P-57. The gap's "CPC drop" claim is recorded as practitioners' (Pattern asserts it; Evolve's figure is CPM; no CPC series was found). It is not stated as a fact.
2. Gap 2 (Brand Tailored Promotions and Customer Engagement). Added F7: markets, Brand Representative and Brand Registry requirement, the 10–50% discount, goal-based audiences and the 2023 six-audience list, the 1,000 minimum, product eligibility, 48-hour, 60-day and 90-day timing, the 20-promotion limit, badge, stacking, edit rules and events. Added F8: the Customer Engagement email tool, with followers and the 2022 tailored audiences. Extended F6 with the Promotions API's `BRAND` segment, its GET-only paths and seller-only availability. Added the SD-overlap note, practitioners on BTP, Stable 21–22, run-time rows, Open question 11 and P-58 to P-63. Declined in part: the gap's "discount floors" holds for BTP's 10% minimum (stated). BTP fees could not be read (help page unreachable), so none is stated. The gap's audience list ("high spenders, brand followers") matches the 2023 post. The 2026 page groups audiences by goal and no longer lists brand followers by name, which is recorded rather than smoothed over.
3. Gap 3 (EU events and the price-indication rule). Added A12: the UK and EU spring event (March 10–16, not the US March 25–31), Prime Day, the October event with local start times and the German name "Prime Deal Days", Black Friday Week 2025 in the UK and DE, and 2026 not yet announced. Added F9: UK and EU 2026 deal cutoffs, fees per store, PED rating and inbound dates. Added F10: PAngV § 11; the CJEU's C-330/23 release; Amazon's FR, ES, IT, BE, SE and PL 30-day sentences; the 90-day median "Was Price"; the DE badge note; the UK "Lowest price in 30 Days" definition; the Munich ruling (press); and the seat's reading of what this does to a deal badge and an ad's savings claim. Also practitioners §8 (Omnia Retail), Stable 19 and 23, Open questions 12–14, P-50 to P-53, P-64 to P-67 and S8. A new tag, [law], marks the statute and the court release. Not stated: Directive 2019/2161's own text (EUR-Lex unreachable) and Amazon Ads' advertising-copy rule on EU savings claims (sign-in shell). The critic's "one hit for 'Lowest price in 30'" now carries positions (P-65).
4. Gap 4 (advertising and promotion interaction). Added R7 (Kaul and Wittink 1995, *Marketing Science* 14(3), G151–G160, the supplement issue), R8 (Ataman, van Heerde and Mela 2010, *JMR* 47(5); its title is "The Long-Term Effect of Marketing Strategy on Brand Sales", plus the 2008 companion paper), R9 (Erdem, Keane and Sun, SSRN), R10, I7 and S7, tying the AMC promotional columns to the design question. Also Stable 25 and P-68 to P-71. I6 now records the dataset's no-cost window (June 1 to December 31, 2026).

**Contradictions settled.**
1. TACOS. Both Amazon pages were re-opened on 2026-11-09. *The author's guide to Sponsored Products* says "TACOS shows your ad spend as a percentage of total sales". The holiday myths page says "That's where total advertising cost of sales (TACOS) comes in. TACOS reveals whether your total sales (organic and paid) are growing in relation to your ad spend." Amazon therefore does define TACOS, on at least these two Amazon Ads library pages. Neither names the sales field, the ad products or the dates, so the owner file's point stands that the numerator and denominator are left to the reader. Its sentence "No Amazon page read defines TACoS" does not hold against these pages. The owner (`areas/ads-organic-and-total.md`, its Stable item 7 and P-6) should restate it, citing both pages; this file does not edit it. This file now quotes both (B8, H3, P-23, P-72). While re-opening the page, this seat found that its `<title>` reads "Holiday advertising myths: What experts want you to know" (og:title "Industry experts reveal top holiday advertising misconceptions"). The file's earlier name for it, "Common holiday advertising myths" (from the URL slug), was replaced throughout.
2. SB Product Collection dates. Re-opened the Deprecations page, the migration guide, the release notes index and the SB 4.0 spec. The facts: deprecation June 2026; from August 2026, creates become Manual Collection ads (custom images do not render); "Shutoff Date: January 2027" and "Post January 2027 ... will return an error" (Deprecations; migration guide: "Final shutoff"); "Beginning February 2027, product collections will no longer be supported" (release note of September 18, 2026, with `ListMigrations`, `POST /sb/v4/migrations/list`). The migration guide also says existing Product Collection ads "will continue to serve impressions", with no end date. This file's G2, P-32, Stable 24, Open question 9 and run-time table now carry both dates and the August 2026 mapping. The owner is `method/ads-api-surface.md`. The diagnosis and targeting files, which carry one date each, should take both.

**Declined.** None of the four gaps was wrong on the facts. Two parts could not be filled from readable pages and are left open rather than stated: BTP fees (Open question 11) and Amazon Ads' own EU savings-claim rule (Open question 12).

**Still unreachable after the gap fill.** EUR-Lex (empty 202); the Amazon Ads advertising-copy policy in ten locales (sign-in help shell); the Seller Central help pages for BTP and Customer Engagement; Amazon.com's reference-pricing page (bot response); the Jungle Scout 2022 seasonal PDF (text not extractable here); the Seller News post on holiday returns.

Pending verification of the gap-fill additions.
