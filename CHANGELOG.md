# Changelog

## 0.1.3

- The README no longer names another plugin; what the playbook builds on is its `comchatx.builds`, each with its reason, as signed on 2026-11-18. The sentence "To have cx review your ads every week, also install [Scheduled Tasks](…)." and its Chinese are gone; `@comchatx/cx-schedule` is an optional entry with the reason 「用于让 cx 按你定的时间复盘广告，比如每周一次。」 / "Has cx review your ads on a schedule."
- "What it uses" names the account, not the plugin: 「**你的亚马逊广告账户**：cx 在这里读取广告活动和报告，也在这里修改出价、预算和投放。」 / "**Your Amazon advertising accounts:** cx reads your campaigns and reports there, and changes your bids, budgets and targets there." Its Amazon SP-API and Keepa lines are gone; their entries carry the reasons 「用于把广告放到整个店铺里看。」 / "Sets your ads against your whole store." and 「用于看 Buy&nbsp;Box 和排名的历史。」 / "Adds Buy&nbsp;Box and rank history.", the `&nbsp;` written as the no-break space itself, since the reason is drawn as text.
- `cx-amazon-seller` is a new optional entry, with the reason 「用于让 cx 从第一条消息起就知道你在亚马逊开店。」 / "Tells cx from the start that you sell on Amazon."
- The seven templates read as the seller's own message, as signed on 2026-11-17: the English of each says "my" where it said "your"; `ads-change-review` reads "[date]" / 「【日期】」 where it read "a given day" / 「某一天」; `ads-launch` reads "Start ads for my new product [ASIN], …" / 「为新品【ASIN】开始投广告，…」; `ads-brand`'s Chinese says 「我的品牌」.

## 0.1.2

- The card's name is the one signed on 2026-11-17: "Amazon Ads Playbook" on the English page (`comchatx.name`) and 「亚马逊广告分析手册」 on the Chinese page (`comchatx.nameZh`).
- The README, in English and Chinese, calls each plugin of ours it names by the card's name signed on 2026-11-17.
- The README names each other plugin it speaks of by the card's name in its own language, a link to that plugin's page on npm, never by the npm name.

## 0.1.1

- The Plugins page names the package Amazon Ads Playbook (`comchatx.name`).

## 0.1.0

- The first version: eight skills on sponsored-ads work over `@comchatx/cx-amazon-ads` (`ads-review`, `ads-launch`, `ads-structure-and-targets`, `ads-search-terms`, `ads-bids-and-budgets`, `ads-seasons`, `ads-economics`, `ads-change`) and seven templates (`/ads-review`, `/ads-launch`, `/ads-harvest`, `/ads-season`, `/ads-margin`, `/ads-brand`, `/ads-change-review`). Every line of the skills cites one of the 323 positions in `research/README.md`.
