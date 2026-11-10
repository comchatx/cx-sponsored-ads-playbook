# Budgets, pacing and budget rules

## The daily budget

- A daily budget is averaged over the calendar month: the month's spend stays within daily budget × days, and the invoice is adjusted for any over-delivery. (B22)
- A single day may spend up to 100% more, or 25% if the profile opted out, read as `isOptedOutForAverageDailyBudgetIncrease` among the account budget feature flags. (B22)
- Amazon's library guide still prints 25%. (B22)
- A mid-month change caps the rest of the month at the new budget × days left. (B22)
- When a budget changes several times in a day, the highest applies that day and the last from the next day. (B22)
- A cut below what has been spent today stops spend for the rest of the day. (B22)

## Pacing and running out

- Sponsored-ads budgets "are spent as quickly as possible and not paced", while Display, Video and Audio campaigns are paced to daily and minute-level targets with bids adjusted every few minutes. (B23)
- An out-of-budget campaign is not eligible to serve until the budget resets at midnight. (B23)
- Portfolio caps and the SP daily budget cap in Advertising Settings also stop campaigns. (B23)
- A budget raise "typically" takes 1–2 hours to show as Delivering, and Amazon advises against frequent budget changes within one day. (B23)
- A campaign that exhausts its budget on an event day pauses until midnight, and Amazon names budget increases and budget rules set in advance as the means to keep it running. (B23)
- Event days and seasons: ../ads-seasons/SKILL.md.

## Budget types by product

- Sponsored Brands takes a daily or a lifetime budget, and a lifetime budget requires start and end dates. (B24)
- A live SB campaign cannot switch from daily to lifetime (Amazon's route is to copy it into a new campaign), and a live lifetime budget can only rise. (B24)
- SP takes daily budgets only. (B24)
- An SD campaign created through the API without a budget gets a regional default in local currency, which the *Default budgets* section of Amazon's *Limits, constraints, and quotas* page, https://advertising.amazon.com/API/docs/en-us/reference/concepts/limits, gives per marketplace. (B24)

## Budget usage and hourly cost

- Budget usage percent is the day's spend over the day's effective budget, which includes budget-rule increases and the average-daily-budget lift. (B25)
- It is read as `budgetUsagePercent` with `usageUpdatedTimestamp` from the SP, SB and SD campaign and the portfolio budget usage operations, for up to 100 ids. (B25)
- Stream v1's `budget-usage` feed (every 5% consumed) needs an SQS or Firehose destination, stops on 2027-06-30 and is "not carried forward in Stream v2", Amazon pointing to the Campaign Management API instead. (B25)
- Hourly cost per campaign comes from v1 reports with the `hour.value` dimension, kept 14 days with a 14-day maximum range. (B31)

## Budget recommendations

- The SP budget recommendation returns a suggested daily budget, the share of the last 7 days in budget (0 to 1), and lower and upper estimates of missed impressions, clicks and sales that are "not a guarantee". (B26)
- Amazon suggests waiting until a campaign has been active nine days. (B26)
- SB and SD have their own budget recommendations; at their launch Amazon said roughly ten percent of SB campaigns went out of budget daily (2023). (B26)
- The recommended budget is estimated missed clicks × an estimated CPC, the missed clicks coming from a model of similar campaigns that stayed in budget combined with the campaign's own CTR and sales. (B26)
- The missed sales are click-attributed sales, not sales caused by the ad. (B26)
- Field experiments on paid search found non-experimental returns overstated. (B26)
- No published validation against what raised campaigns then did was found, and Amazon's pages do not say whether the model accounts for the hour of the missed traffic. (B26)

## Budget rules

- Budget rules only raise a daily budget, by a percentage, on a schedule (date range, recommended event, weekly days, or hours in the marketplaces Amazon's *Schedule-based rules* guide lists, https://advertising.amazon.com/API/docs/en-us/guides/rules/budget-rules/schedule-based) or on performance. (B27)
- Performance rules read ACOS, CTR, CVR or ROAS on SP and SD, and ROAS, top-of-search share or new-to-brand on SB, over 7 days for sellers and 14 for vendors. (B27)
- Several rules add (+40% and +100% apply as +140%), and a campaign can carry up to 250. (B27)
- The API guide says rules are evaluated at the start of the day and again when a rule is created or updated or the daily budget changes, while the help page describes a daily review that sets the next day's budget. (B27)
- A performance rule does not apply below a minimum daily budget, which Amazon's *Understand budget rules in Sponsored ads* page, https://advertising.amazon.com/help/GNSMLANWNF344YBE, gives in US dollars only. (B27)
- A raised budget reads back as SP `budget.effectiveBudget`, SB and SD `ruleBasedBudget.value`, or v1 `monetaryBudget.ruleValue`. (B27)
- Amazon warns that `applicableRuleId` can be incomplete when several rules are active; the campaign's rule list is the full record. (B27)

## Portfolios and the account cap

- A portfolio cap is a date range (`DATE_RANGE`), a monthly recurring amount (`MONTHLY_RECURRING`) or none (`NO_CAP`), and a campaign belongs to at most one portfolio. (B28)
- Reaching the cap stops the portfolio's campaigns with `PORTFOLIO_OUT_OF_BUDGET`. (B28)
- With unspent sharing on (`budgetControls.campaignUnspentBudgetSharing`), a campaign that has spent its own daily budget can use other campaigns' leftovers from earlier days in the month, "up to 100% more than their average daily budget on any given day", while the portfolio's month stays within the sum of daily budgets × days. (B28)
- Sharing is set per portfolio, and is on by default for portfolios created after 2025-06-20. (B28)
- The SP account daily budget cap is a seller-only console setting over all SP campaigns, with no API operation found. (B29)

## Practitioners and tools

- Trellis (Mike Lepine) advises recording the time each campaign ran out of budget; its Monthly Spend Pacer projects from month-to-date plus a 7-day run rate and acts only outside a 10% band. (B33)
- Intentwise (Michael Waters) observes that advertisers commonly exhaust budgets by the evening and that CPCs are lower at night. (B33)
- m19 rewrites campaign and portfolio caps daily, spends up to 2× its daily target on a day and 1.1× its monthly target, and asks sellers not to edit budgets in the console. (B33)
- Helium 10's Budget Manager adjusts daily budgets toward monthly and annual plans, pauses campaigns at the plan's cap and does not consider portfolio caps. (B33)
- SmartScout describes Pacvue's budget tool as taking monthly caps for a fiscal year. (B33)
- Skai moves budget between a portfolio's campaigns to a budget and KPI plan. (B33)
- Perpetua's Monthly Budget Tracker projects month-end spend and enforces nothing. (B33)
- Kepler reports one apparel client's daily serving rising from 8.5 to 16.5 hours, with ROAS up 95% and CPC down 58%, after early-day bid cuts with Pacvue, a single-client before/after without a control. (B33)

## Research on budgets

- Research on budget-constrained bidding finds adaptive pacing, which adjusts bids to the advertiser's own spend path, asymptotically optimal, and serving greedily until the budget ends suboptimal when budgets are finite. (B34)
- It finds that each budget-management method used market-wide leads to a different equilibrium. (B34)
- It notes that a budget that runs out ends a campaign's observed path, so "what if it had not run out" is a counterfactual simulation. (B34)
- It notes that spend-response estimates become more uncertain for reallocations far outside the spend levels in the history. (B34)
