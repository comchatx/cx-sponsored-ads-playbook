cx 检查你的商品推广、品牌推广和展示型推广，找出花费或销量变化的原因，提出修改，并附上理由和依据的数据。之后问起某次改动，cx 会对照亚马逊的改动记录和报告，判断已见效、未见效，还是暂时无法确定。

你可以这样问：

- 上周广告花费涨了，销量却没动，为什么？
- B0EXAMPLE1 的广告怎么突然没曝光了？
- 哪些广告活动经常预算不够，该加到多少？

如果想让 cx 每周定时复盘广告，再装上[定时任务](https://www.npmjs.com/package/@comchatx/cx-schedule)。

## 用到的数据

- **[亚马逊广告接口](https://www.npmjs.com/package/@comchatx/cx-amazon-ads)**：你的亚马逊广告账户，在亚马逊广告接口插件里连接。cx 在这里读取广告活动和报告，也在这里修改出价、预算和投放。
- **[亚马逊卖家接口](https://www.npmjs.com/package/cx-amazon-sp-api)**（如果你装了）：你的 Buy&nbsp;Box、库存、费用和总销量，让 cx 把广告放到整个店铺里看。
- **[Keepa 数据接口](https://www.npmjs.com/package/cx-keepa)**（如果你装了）：Buy&nbsp;Box 和排名的历史。
