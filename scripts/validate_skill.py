#!/usr/bin/env python3
"""Lightweight Agent Skills spec check for this skill (no dependencies).

Usage: python3 scripts/validate_skill.py [skill_dir]
Checks frontmatter fields against https://agentskills.io/specification, SKILL.md length,
that relative markdown links resolve, and that evals/evals.json parses.
For the official validator, use `skills-ref validate <dir>` if installed.
"""
import json
import os
import re
import sys

root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
errors, notes = [], []

text = open(os.path.join(root, "SKILL.md"), encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    sys.exit("SKILL.md: missing YAML frontmatter")
fm = {}
for line in m.group(1).splitlines():
    if line and not line.startswith(" ") and ":" in line:
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"')

name = fm.get("name", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append(f"name invalid: {name!r}")
if name != os.path.basename(root):
    errors.append(f"name {name!r} does not match directory {os.path.basename(root)!r}")
desc = fm.get("description", "")
if not 1 <= len(desc) <= 1024:
    errors.append(f"description length {len(desc)} not in 1..1024")
allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
extra = set(fm) - allowed
if extra:
    errors.append(f"non-spec frontmatter keys: {sorted(extra)}")

lines = text.count("\n")
words = len(text.split())
notes.append(f"SKILL.md: {lines} lines, ~{int(words * 1.35)} tokens (spec: <500 lines, <5000 tokens)")
if lines >= 500:
    errors.append("SKILL.md exceeds 500 lines")

for dirpath, _, files in os.walk(root):
    if "/." in dirpath:
        continue
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dirpath, f)
        for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", open(p, encoding="utf-8").read()):
            if re.match(r"[a-z]+:", link):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(dirpath, link))):
                errors.append(f"{os.path.relpath(p, root)}: broken link {link}")

try:
    ev = json.load(open(os.path.join(root, "evals", "evals.json"), encoding="utf-8"))
    notes.append(f"evals.json: {len(ev['evals'])} scenarios")
except Exception as e:  # noqa: BLE001
    errors.append(f"evals.json: {e}")

print("\n".join(notes))
if errors:
    print("FAIL\n- " + "\n- ".join(errors))
    sys.exit(1)
print("OK")
