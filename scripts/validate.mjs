#!/usr/bin/env node
// Metadata validation.
// Dependency-free: checks structured content files under content/ for required
// fields, duplicate identifiers, and draft flags. Empty collections pass
// (empty-but-valid launch state). Extend REQUIRED as schemas grow.

import { readdirSync, readFileSync, statSync, existsSync } from "node:fs";
import { join, extname } from "node:path";

const ROOT = "content";
const REQUIRED = {
  people:       ["id", "name", "slug", "role", "category", "status", "consent_recorded"],
  projects:     ["id", "title", "slug", "summary", "status", "ownership", "canonical_url"],
  publications: ["id", "title", "year", "type"],
};

const errors = [];
const warnings = [];
const seen = new Map(); // id/slug -> file

function walk(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir).flatMap((name) => {
    const p = join(dir, name);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });
}

// naive `key: value` reader for top-level YAML/front-matter keys
function readKeys(text) {
  const keys = {};
  for (const line of text.split(/\r?\n/)) {
    const m = /^([A-Za-z_][\w-]*):\s*(.*)$/.exec(line);
    if (m) keys[m[1]] = m[2].trim();
  }
  return keys;
}

for (const [collection, required] of Object.entries(REQUIRED)) {
  const dir = join(ROOT, collection);
  const files = walk(dir).filter((f) => [".yml", ".yaml", ".md", ".qmd"].includes(extname(f)));
  if (files.length === 0) {
    console.log(`· ${collection}: empty collection (ok, empty-but-valid).`);
    continue;
  }
  for (const file of files) {
    const keys = readKeys(readFileSync(file, "utf8"));
    for (const field of required) {
      if (!(field in keys) || keys[field] === "") {
        errors.push(`${file}: missing required field "${field}"`);
      }
    }
    for (const idField of ["id", "slug"]) {
      if (keys[idField]) {
        const k = `${idField}:${keys[idField]}`;
        if (seen.has(k)) errors.push(`Duplicate ${idField} "${keys[idField]}" in ${file} and ${seen.get(k)}`);
        else seen.set(k, file);
      }
    }
    if (keys.draft === "true") warnings.push(`${file}: draft:true (excluded from production)`);
    if (collection === "people" && keys.consent_recorded && keys.consent_recorded !== "true") {
      errors.push(`${file}: consent_recorded must be true to publish a profile`);
    }
  }
}

for (const w of warnings) console.warn(`⚠ ${w}`);
if (errors.length) {
  console.error(`\n✖ ${errors.length} validation error(s):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}
console.log("✓ metadata validation passed");
