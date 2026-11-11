import { readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { body } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const ID = /[ALTSBEGCMPR]\d+/g;
const GROUP = /\(([ALTSBEGCMPR]\d+(?:\s*[,;]\s*[ALTSBEGCMPR]\d+)*)\)/g;

/** The positions that left with the split of 2026-11-10 (G24 whole, its Attribution clause to cx-brand-measurement and its Events clause to cx-dva-playbook). */
export const MOVED = ["C11", "E17", "G13", "G24", "G29", "M18", "P18", "P5", "R25", "S16"] as const;

const markdown = (directory: string): string[] =>
  readdirSync(directory, { recursive: true, encoding: "utf8" }).filter((file) => file.endsWith(".md")).map((file) => join(directory, file));

/** Every position, as `research/README.md` opens it: `- **<letter><n>.**` at the head of a list entry. */
const positions = new Set(
  [...readFileSync(join(ROOT, "research", "README.md"), "utf8").matchAll(/^- \*\*([ALTSBEGCMPR]\d+)\.\*\*/gm)].map((match) => match[1]!),
);

/** A line that only points: to a reference, another skill or the research. */
const pointer = (line: string) => /references\/[\w-]+\.md|\.\.\/[\w-]+\/SKILL\.md|research\//.test(line);

/** Each text line of the skills and their references, with the ids its citation groups name. */
const lines = markdown(join(ROOT, "skills")).flatMap((file) =>
  body(readFileSync(file, "utf8"))
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line !== "" && !line.startsWith("#") && !/^\|?[-:| ]+\|?$/.test(line))
    .map((line) => ({ file, line, ids: [...line.matchAll(GROUP)].flatMap((group) => group[1]!.match(ID) ?? []) })),
);

it("the research holds 333 positions, ten of which left with the split", () => {
  expect(positions.size).toBe(333);
  for (const id of MOVED) expect(positions.has(id), id).toBe(true);
});

it("every line of the skills and their references cites a position that exists, except a line that only points", () => {
  expect(lines.length).toBeGreaterThan(0);
  for (const { file, line, ids } of lines) {
    if (ids.length === 0) expect(pointer(line), `${file}: ${line}`).toBe(true);
    for (const id of ids) expect(positions.has(id), `${file}: ${id}`).toBe(true);
  }
});

it("none of the ten moved positions is cited", () => {
  const moved = new Set<string>(MOVED);
  for (const { file, ids } of lines) for (const id of ids) expect(moved.has(id), `${file}: ${id}`).toBe(false);
});

it("each of the 323 positions that stay is cited somewhere in the skills", () => {
  const cited = new Set(lines.flatMap(({ ids }) => ids));
  const staying = [...positions].filter((id) => !(MOVED as readonly string[]).includes(id));
  expect(staying).toHaveLength(323);
  expect(staying.filter((id) => !cited.has(id))).toEqual([]);
});

it("G10 enters without its AMC clause, which went to cx-amc-playbook", () => {
  for (const { file, line, ids } of lines) if (ids.includes("G10")) expect(line, file).not.toMatch(/\bAMC\b|Marketing Cloud/);
});

/** Every skill file whole, its frontmatter and headings included, line by line. */
const files = markdown(join(ROOT, "skills")).map((file) => ({ file, text: readFileSync(file, "utf8") }));

/** The lines of a file's whole text that a check finds. */
const caught = (text: string, check: (line: string) => boolean): string[] => text.split("\n").filter(check);

/** An Ads API request route as a request names it: a method and a path, or a path of Amazon's from its root. */
const ROUTE = /\b(?:GET|POST|PUT|PATCH|DELETE)\s+`?\/|`\/[A-Za-z]|(?<![\w.~/])\/(?:adsApi|sp|sb|sd|v2|v3|reporting|history|portfolios|eligibility|product|products|accountBudgets|targetPromotionGroups|insights|attribution|amc|dsp|stores|media|assets|recommendations|budgetRules)\b/;
/** A polling interval: how often a status is asked for. */
const POLL = /\bonce an? (?:second|minute|hour)\b|\bevery \d+ ?(?:s|sec|seconds?|min|minutes?)\b|\bpoll\w*\s+(?:about\s+|roughly\s+|at most\s+)?(?:every|once)\b/i;
const mechanics = (line: string) => ROUTE.test(line) || POLL.test(line);

/** A sales event by name. */
const EVENT = /\b(?:Prime Day|Prime Big Deal Days|PBDD|Big Spring Sale|Black Friday|Cyber Monday|Cyber Week|BFCM|White Friday|Singles'? ?Day|11:11|Great Indian Festival|Boxing Day|Prime Early Access)\b/i;
/** A calendar date: a month with its day, a day with its month, or an ISO date. */
const CALENDAR = /\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.? \d{1,2}\b|\b\d{1,2} (?:January|February|March|April|May|June|July|August|September|October|November|December)\b|\b(?:19|20)\d{2}-\d{2}-\d{2}\b/;
const eventDate = (line: string) => EVENT.test(line) && CALENDAR.test(line);

/** A skill file with one line placed in its frontmatter, its heading or its body. */
const control = (where: "frontmatter" | "heading" | "body", line: string) =>
  [
    "---",
    "name: ads-example",
    where === "frontmatter" ? `description: "${line}"` : 'description: "An example."',
    "---",
    "",
    where === "heading" ? `## ${line}` : "## Example",
    "",
    where === "body" ? `- ${line} (A1)` : "- A line (A1).",
  ].join("\n");

it("no line of any skill file, frontmatter and headings included, names an Ads API request route or a polling interval: how a call is made and a report is asked for is the amazon-ads skill's", () => {
  expect(files.length).toBeGreaterThan(0);
  for (const { file, text } of files) expect(caught(text, mechanics), file).toEqual([]);
});

it("the route and polling check catches a route or an interval in a body line, a heading and the frontmatter", () => {
  for (const line of ["A v1 report is created with `POST /adsApi/v1/create/reports`", "`POST /history` returns up to 90 days", "The list is /sp/campaigns/list", "A v1 report's status is polled about once a minute"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), mechanics), `${where}: ${line}`).toHaveLength(1);
  }
  for (const line of ["SP/SB and/or SD", "How a report is asked for: the amazon-ads skill's references/door.md", "The interval has poor coverage"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), mechanics), `${where}: ${line}`).toEqual([]);
  }
});

it("no line of any skill file, frontmatter and headings included, states a sales event's calendar date: an event's dates differ by marketplace and year, and are read where Amazon gives them", () => {
  for (const { file, text } of files) expect(caught(text, eventDate), file).toEqual([]);
});

it("the event-date check catches a dated event in a body line, a heading and the frontmatter", () => {
  for (const line of ["Black Friday 2026 is November 27", "Prime Day ran June 23–26", "Black Friday Week deals were accepted until 2026-11-18"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), eventDate), `${where}: ${line}`).toHaveLength(1);
  }
  for (const line of ["An event's dates differ by marketplace and year; the events operation returns them for the advertiser's marketplace", "Prime Day changed from 48 to 96 hours in 2025", "Amazon announced on 2026-07-06 a change to the Featured Offer"]) {
    for (const where of ["frontmatter", "heading", "body"] as const) expect(caught(control(where, line), eventDate), `${where}: ${line}`).toEqual([]);
  }
});

it("each SKILL.md body is at most 371 words", () => {
  for (const name of readdirSync(join(ROOT, "skills"))) {
    const words = body(readFileSync(join(ROOT, "skills", name, "SKILL.md"), "utf8")).split(/\s+/).filter(Boolean).length;
    expect(words, name).toBeLessThanOrEqual(371);
  }
});
