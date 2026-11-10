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

it("the Plugins page's field names every skill and template in both languages, and what the skills read", () => {
  const { comchatx } = manifest() as { comchatx: { skills: Record<string, { about: { en: string; zh: string } }>; prompts: Record<string, { zh: string }>; builds: unknown } };
  expect(Object.keys(comchatx.skills).sort()).toEqual([...SKILLS]);
  for (const [name, words] of Object.entries(comchatx.skills)) {
    expect(words.about.zh, name).toMatch(/[一-鿿]/);
    expect(words.about.en, name).not.toMatch(/[一-鿿]/);
  }
  expect(Object.keys(comchatx.prompts).sort()).toEqual([...PROMPTS]);
  for (const [name, words] of Object.entries(comchatx.prompts)) expect(words.zh, name).toMatch(/[一-鿿]/);
  expect(comchatx.builds).toEqual([
    { on: "@comchatx/cx-amazon-ads", need: "required" },
    { on: "cx-amazon-sp-api", need: "optional" },
    { on: "cx-keepa", need: "optional" },
  ]);
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
