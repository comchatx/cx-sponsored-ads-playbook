import { execFileSync } from "node:child_process";
import { cpSync, existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { loadPackage, scratch, typed } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const SKILLS = [
  "ads-bids-and-budgets",
  "ads-change",
  "ads-economics",
  "ads-launch",
  "ads-review",
  "ads-search-terms",
  "ads-seasons",
  "ads-structure-and-targets",
] as const;
const PROMPTS = ["ads-brand", "ads-change-review", "ads-harvest", "ads-launch", "ads-margin", "ads-review", "ads-season"] as const;
const skillFile = (name: string) => join(ROOT, "skills", name, "SKILL.md");
const manifest = () => JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8")) as Record<string, unknown>;

it("the pinned pi loads eight skills and seven templates from the package, and nothing else", async () => {
  const { loader } = await loadPackage(ROOT);
  const skills = loader.getSkills();
  const prompts = loader.getPrompts();
  expect(skills.diagnostics).toEqual([]);
  expect(prompts.diagnostics).toEqual([]);
  expect(skills.skills.map((skill) => skill.name).sort()).toEqual([...SKILLS]);
  expect(skills.skills.map((skill) => skill.filePath).sort()).toEqual(SKILLS.map(skillFile));
  expect(prompts.prompts.map((prompt) => prompt.name).sort()).toEqual([...PROMPTS]);
  expect(loader.getExtensions().extensions).toEqual([]);
});

it("every directory under skills/ holds a SKILL.md and no script: the report reader is cx-amazon-ads's", () => {
  const directories = readdirSync(join(ROOT, "skills"), { withFileTypes: true }).filter((entry) => entry.isDirectory()).map((entry) => entry.name).sort();
  expect(directories).toEqual([...SKILLS]);
  for (const name of directories) {
    expect(existsSync(skillFile(name)), `skills/${name}/SKILL.md`).toBe(true);
    expect(existsSync(join(ROOT, "skills", name, "scripts")), `skills/${name}/scripts`).toBe(false);
  }
});

it("each template expands in a pi session: its arguments and the seller's own words reach the model, no placeholder does", async () => {
  const expected: Record<(typeof PROMPTS)[number], [string, string]> = {
    "ads-review": ["/ads-review 只看美国站", "Review my Amazon sponsored ads over the last few weeks: how spend and sales went, what moved and why, and what you would change, with your reasons. 只看美国站"],
    "ads-launch": ["/ads-launch B0EXAMPLE1 US,DE 月底到货", "Get my product B0EXAMPLE1 advertising: whether it can serve, and the first campaigns you would set up for it, with your reasons. US,DE 月底到货"],
    "ads-harvest": ["/ads-harvest", "Go through my search terms since the last pass: which to move into targets of their own, which to negate, and why."],
    "ads-season": ["/ads-season Prime Day", "Get my sponsored ads ready for the next Amazon event in my marketplaces: its dates, budgets, bids and deals, with your reasons. Prime Day"],
    "ads-margin": ["/ads-margin SKU-1 SKU-2", "Work out what an ad sale is worth on my products, from fees and costs to break-even ACOS, and what that makes my targets. SKU-1 SKU-2"],
    "ads-brand": ["/ads-brand Hearthly", "Show me who advertises on my brand's searches and product pages, and what holding those places costs me. Hearthly"],
    "ads-change-review": ["/ads-change-review 2026-10-01 预算调整", "Tell me whether the ad changes made on 2026-10-01 held, did not, or cannot be told yet, and how sure you are. 预算调整"],
  };
  for (const [name, [input, text]] of Object.entries(expected)) {
    const received = await typed(ROOT, input);
    expect(received.trim(), name).toBe(text);
    expect(received, name).not.toMatch(/\$\{?[@0-9A]/);
  }
}, 120_000);

it("the package carries no dependency, no install script and no extension", () => {
  const pkg = manifest();
  for (const field of ["dependencies", "peerDependencies", "optionalDependencies", "bundleDependencies", "bundledDependencies"]) expect(pkg[field], field).toBeUndefined();
  expect(pkg["name"]).toBe("@comchatx/cx-sponsored-ads-playbook");
  expect(pkg["scripts"]).toEqual({ typecheck: "tsc --noEmit", test: "vitest run" });
  expect(pkg["keywords"]).toEqual(["pi-package"]);
  expect(pkg["pi"]).toEqual({ skills: ["./skills"], prompts: ["./prompts"] });
  expect(readdirSync(ROOT)).not.toContain("extensions");
});

/** The words Jack signed on 2026-11-11 for the Plugins page: the card's line, each template's and each skill's. */
const LINE = { en: "Traces why ad spend or sales moved, then judges each fix.", zh: "查出广告花费和销量变化的原因，改后判断是否见效。" } as const;
const SKILL_WORDS = {
  "ads-review": { zh: "分析广告表现，以及花费和销量变化的原因。", en: "How your ads perform, and why spend or sales moved." },
  "ads-launch": { zh: "判断新品能否投广告，并搭建首批广告活动。", en: "Whether a new product can advertise, and its first campaigns." },
  "ads-structure-and-targets": { zh: "分析广告活动的结构和每种投放会匹配什么。", en: "How campaigns are built, and what each target matches." },
  "ads-search-terms": { zh: "找出值得单独投放和该否定的搜索词。", en: "Search terms worth targeting, and ones to negate." },
  "ads-bids-and-budgets": { zh: "分析出价、版位和预算如何决定花费。", en: "How bids, placements and budgets decide what you spend." },
  "ads-seasons": { zh: "安排大促前后的预算、出价和促销。", en: "Budgets, bids and deals around Amazon's sales events." },
  "ads-economics": { zh: "算出广告订单的利润和广告对总销量的贡献。", en: "What an ad sale earns, and what ads add to total sales." },
  "ads-change": { zh: "查广告改动记录，判断一次改动是否见效。", en: "Amazon's change history, and whether a change worked." },
} as const;
const PROMPT_WORDS = {
  "ads-review": { zh: "复盘最近几周的广告，并提出修改。", en: "Review your ads over the last few weeks, and propose changes." },
  "ads-change-review": { zh: "判断某一天的广告改动是否见效。", en: "Tell whether the ad changes made on a given day worked." },
  "ads-harvest": { zh: "梳理搜索词，找出值得单独投放和该否定的词。", en: "Go through your search terms for ones to target and ones to negate." },
  "ads-launch": { zh: "为新品开始投广告，从能否投放到首批广告活动。", en: "Start a new product's ads, from whether it can serve to its first campaigns." },
  "ads-margin": { zh: "算出广告订单能赚多少，以及盈亏平衡的 ACOS。", en: "Work out what an ad sale earns you, and your break-even ACOS." },
  "ads-brand": { zh: "看看谁在你的品牌搜索词和商品页上投广告，守住要花多少钱。", en: "See who advertises on your brand's searches and pages, and what holding them costs." },
  "ads-season": { zh: "为下一个亚马逊大促准备好广告。", en: "Prepare your ads for Amazon's next sales event." },
} as const;
/** The signed Overview, each README whole. */
const OVERVIEW = {
  "README.md": "cx finds why spend or sales moved in your Sponsored Products, Brands and Display ads and proposes changes backed by figures. Later, from Amazon's change history, it tells if a change worked, did not, or cannot be told yet.\n\nSome things you can ask:\n\n- Why did my ad spend rise last week while sales stayed flat?\n- Why did B0EXAMPLE1's ads suddenly stop getting impressions?\n- Which campaigns keep running out of budget, and how much should I add?\n\nTo have cx review your ads every week, also install cx-schedule.\n\n## What it uses\n\n- **Amazon Ads:** your Amazon advertising accounts, connected on the Amazon Ads plugin. cx reads your campaigns and reports there, and changes your bids, budgets and targets there.\n- **Amazon SP-API,** where you have it: your Buy&nbsp;Box, stock, fees and total sales, so cx can set your ads against your whole store.\n- **Keepa,** where you have it: Buy&nbsp;Box and rank history.\n",
  "README.zh-CN.md": "cx 检查你的商品推广、品牌推广和展示型推广，找出花费或销量变化的原因，提出修改，并附上理由和依据的数据。之后问起某次改动，cx 会对照亚马逊的改动记录和报告，判断已见效、未见效，还是暂时无法确定。\n\n你可以这样问：\n\n- 上周广告花费涨了，销量却没动，为什么？\n- B0EXAMPLE1 的广告怎么突然没曝光了？\n- 哪些广告活动经常预算不够，该加到多少？\n\n如果想让 cx 每周定时复盘广告，再装上 cx-schedule。\n\n## 用到的数据\n\n- **Amazon Ads**：你的亚马逊广告账户，在 Amazon Ads 插件里连接。cx 在这里读取广告活动和报告，也在这里修改出价、预算和投放。\n- **Amazon SP-API**（如果你装了）：你的 Buy&nbsp;Box、库存、费用和总销量，让 cx 把广告放到整个店铺里看。\n- **Keepa**（如果你装了）：Buy&nbsp;Box 和排名的历史。\n",
} as const;

it("the package's line is the signed one: npm's description in English, comchatx.about in Chinese", () => {
  const pkg = manifest() as { description: string; comchatx: { about: string } };
  expect(pkg.description).toBe(LINE.en);
  expect(pkg.comchatx.about).toBe(LINE.zh);
});

it("the card's name is the signed one", () => {
  expect((manifest() as { comchatx: { name: string } }).comchatx.name).toBe("Amazon Ads Playbook");
});

it("each template's English description and Chinese words are the signed ones", () => {
  const { comchatx } = manifest() as { comchatx: { prompts: Record<string, unknown> } };
  expect(Object.keys(comchatx.prompts).sort()).toEqual([...PROMPTS]);
  for (const name of PROMPTS) {
    expect(comchatx.prompts[name], name).toEqual({ zh: PROMPT_WORDS[name].zh });
    const front = readFileSync(join(ROOT, "prompts", `${name}.md`), "utf8").match(/^description: (".*")$/m);
    expect(JSON.parse(front![1]!), name).toBe(PROMPT_WORDS[name].en);
  }
});

it("the Plugins page's field gives every skill its signed words in both languages, and what the skills read", () => {
  const { comchatx } = manifest() as { comchatx: { skills: Record<string, unknown>; builds: unknown } };
  expect(Object.keys(comchatx.skills).sort()).toEqual([...SKILLS]);
  for (const name of SKILLS) expect(comchatx.skills[name], name).toEqual(SKILL_WORDS[name]);
  expect(comchatx.builds).toEqual([
    { on: "@comchatx/cx-amazon-ads", need: "required" },
    { on: "cx-amazon-sp-api", need: "optional" },
    { on: "cx-keepa", need: "optional" },
  ]);
});

it("each README is the signed Overview, whole", () => {
  for (const [file, text] of Object.entries(OVERVIEW)) expect(readFileSync(join(ROOT, file), "utf8"), file).toBe(text);
});

it("the skills point to the door's own skill for how a call is made and a report is landed", () => {
  const reports = readFileSync(join(ROOT, "skills", "ads-review", "references", "reports.md"), "utf8");
  expect(reports).toContain("amazon-ads");
  expect(reports).toContain("references/door.md");
  const review = readFileSync(skillFile("ads-review"), "utf8");
  expect(review).toContain("2027-06-30");
  expect(review).toMatch(/Stream/);
});

/** What the pinned pi loads from a package root: its skills, its templates and any diagnostic. */
const shelf = async (root: string) => {
  const { loader } = await loadPackage(root);
  const skills = loader.getSkills();
  const prompts = loader.getPrompts();
  return {
    skills: skills.skills.map((skill) => skill.name).sort(),
    prompts: prompts.prompts.map((prompt) => prompt.name).sort(),
    diagnostics: [...skills.diagnostics, ...prompts.diagnostics],
  };
};

/** The tarball npm would publish, unpacked: the package as a seller's pi installs it. */
const packed = (from: string): string => {
  const out = scratch();
  const reply = JSON.parse(execFileSync("npm", ["pack", "--json", "--ignore-scripts", "--pack-destination", out], { cwd: from, encoding: "utf8" })) as
    | { filename: string }[]
    | Record<string, { filename: string }>;
  // npm 10 answers a list; npm 11 answers an object keyed by the package's name.
  const [result] = Array.isArray(reply) ? reply : Object.values(reply);
  execFileSync("tar", ["xzf", join(out, result!.filename), "-C", out]);
  return join(out, "package");
};

it("the published tarball loads eight skills and seven templates under the pinned pi, with no diagnostic, and ships no evals or tests", async () => {
  const root = packed(ROOT);
  expect(await shelf(root)).toEqual({ skills: [...SKILLS], prompts: [...PROMPTS], diagnostics: [] });
  for (const left of ["evals", "test"]) expect(existsSync(join(root, left)), left).toBe(false);
}, 120_000);

it("the same check fails a copy whose ads-review description is emptied", async () => {
  const copy = join(scratch(), "copy");
  cpSync(packed(ROOT), copy, { recursive: true });
  const file = join(copy, "skills", "ads-review", "SKILL.md");
  writeFileSync(file, readFileSync(file, "utf8").replace(/^description: .*$/m, 'description: ""'));
  const loaded = await shelf(copy);
  expect(loaded.skills).not.toContain("ads-review");
  expect(loaded.diagnostics.map((one) => [one.message, one.path])).toEqual([["description is required", file]]);
}, 120_000);
