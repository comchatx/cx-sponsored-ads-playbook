# Vendors: profiles, purchase orders and supply

## Vendor profiles

- A vendor profile's `accountInfo.type` is `vendor`, and Amazon says vendor accounts are used with Sponsored Products, Sponsored Brands and Sponsored Display only (A24).
- In the Profiles 3.0 model `validPaymentMethod` is present only for vendors, the profile `dailyBudget` and `PUT /v2/profiles` are for sellers only, and `accountInfo.id` is not unique and may repeat across marketplaces (A24).

## Purchase orders

- Amazon places purchase orders with vendors through the Vendor Orders API; its PO types are RegularOrder, ConsignedOrder, NewProductIntroduction and RushOrder (A28).
- An order's state is New, Acknowledged or Closed, while the status call reports OPEN or CLOSED (A28).
- A vendor acknowledges each line as Accepted, Backordered or Rejected, with rejection reasons TemporarilyUnavailable, InvalidProductIdentifier or ObsoleteProduct (A28).
- Amazon Science states that Amazon's buying systems determine how much of each product to purchase from different suppliers, and that vendor lead times vary with manufacturing capacity, transport and weather (A28).
- Amazon defines procurability as "whether Amazon is able to fulfill a customer delivery promise, considering the ability of known vendors to supply the ASIN in the foreseeable future" (A28).

## Supply reports

- The vendor inventory report and Data Kiosk report the supply behind a vendor's availability: procurable out-of-stock rate (out-of-stock glance views on procurable ASINs over total glance views), vendor confirmation rate (confirmed over submitted units), receive fill rate (received over confirmed units), open PO units, average vendor lead time, units in the most recent POs of the week, and sellable on-hand units, in which backorders count as negative units (A29).
- The real-time inventory report gives hourly highly-available inventory per ASIN, can be requested five minutes after each hour closes, looks back 30 days and spans 7, and is also offered as the `ITEM_INVENTORY_EVENT_CHANGE` notification (A29).
- The forecasting report gives mean, P70, P80 and P90 weekly demand forecasts per ASIN for the latest forecast only, one store per request (A29).
- Its schema defines P80 as the units with which there is an 80% probability the ASIN will not run out of stock during the period, and the Analytics page as an 80% probability that customer demand will not exceed the weekly forecast (A29).

## A practitioner's reading

- Intentwise (Michael Waters, 2023) states that Vendor Central takes about 48 hours to refresh inventory data, and that Amazon auto-pauses Sponsored Products for out-of-stock products but not Sponsored Brands, Sponsored Display or DSP, a line set against Amazon's current Featured Offer page for Display (A30).
