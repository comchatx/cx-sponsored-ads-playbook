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

it("each SKILL.md body is at most 371 words", () => {
  for (const name of readdirSync(join(ROOT, "skills"))) {
    const words = body(readFileSync(join(ROOT, "skills", name, "SKILL.md"), "utf8")).split(/\s+/).filter(Boolean).length;
    expect(words, name).toBeLessThanOrEqual(371);
  }
});
