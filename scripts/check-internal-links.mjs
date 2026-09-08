#!/usr/bin/env node
// Internal link checker: broken internal links fail
// the build. External links (http/https/mailto/tel) are ignored here; they
// are checked separately on a schedule as a warning.
// Dependency-free: scans rendered HTML in the given output dir (default _site).

import { readdirSync, readFileSync, statSync, existsSync } from "node:fs";
import { join, dirname, resolve, extname } from "node:path";

const SITE = process.argv[2] || "_site";
if (!existsSync(SITE)) {
  console.error(`✖ output dir "${SITE}" not found. Run \`quarto render\` first.`);
  process.exit(1);
}

function walk(dir) {
  return readdirSync(dir).flatMap((n) => {
    const p = join(dir, n);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });
}

const htmlFiles = walk(SITE).filter((f) => extname(f) === ".html");
const isExternal = (h) => /^(https?:|mailto:|tel:|data:|#|\/\/)/i.test(h);
const broken = [];

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf8");
  const refs = [...html.matchAll(/(?:href|src)="([^"]+)"/g)].map((m) => m[1]);
  for (const raw of refs) {
    if (isExternal(raw)) continue;
    const [path] = raw.split("#");
    if (!path) continue;
    let target = path.startsWith("/")
      ? join(SITE, path)
      : resolve(dirname(file), path);
    if (target.endsWith("/")) target = join(target, "index.html");
    if (!existsSync(target) && !existsSync(target + ".html") && !existsSync(join(target, "index.html"))) {
      broken.push(`${file.replace(SITE + "/", "")} → ${raw}`);
    }
  }
}

if (broken.length) {
  console.error(`\n✖ ${broken.length} broken internal link(s):`);
  for (const b of broken) console.error(`  - ${b}`);
  process.exit(1);
}
console.log(`✓ internal links ok (${htmlFiles.length} pages checked)`);
