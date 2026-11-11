# Write replies and refusals

## The 207 reply

Writes answer HTTP 207, and Amazon states: "Applications must parse the response body to determine the status of each individual operation". (C3)
Ads API v1 returns `success`, `partialSuccess` and `error`, keyed by request index; a `partialSuccess` item was written with some fields refused and carries its errors, and a success carries `lastUpdatedDateTime`. (C3)
Sponsored Products 3.0 returns per-item `success` and `error` matched by `index`, its objects carrying `extendedData.lastUpdateDateTime`. (C3)

## No idempotency, no transaction

No create, update or delete in v1, SP v3, SB v3, SB v4, SD v3 or Portfolios takes an idempotency key; Amazon's models carry them only for DSP audiences, AMC custom models and billing. (C3)
Creates share no transaction, so a chain can stop part-way and leave a campaign with no ad group or an ad group with no ad. (C3)
The API reports those as `CAMPAIGN_INCOMPLETE` and `AD_GROUP_INCOMPLETE`. (C3)

## Names

Amazon states: "Sellers aren't allowed to have duplicate campaign names, but vendors can". (C4)
A seller's repeated campaign create with the same name is refused, with `NAME_NOT_UNIQUE` in SP 3.0 and `FIELD_VALUE_NOT_UNIQUE` in v1. (C4)
Ad group names are unique only within a campaign. (C4)

## Entities Amazon created

Entities Amazon created automatically, such as an auto campaign's targeting clauses, are refused for some edits. (C5)
The refusals read `AUTOCREATED_ENTITY_CANNOT_EDIT` in v1 and `AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY` in SP v3. (C5)

## Target types

In the v1 model, SP and SB targets are keyword, product, category and theme targets, with no location, daypart, device or audience target; those are DSP-only. (C8)
