#!/usr/bin/env python3
"""Fail if a page points at a file or an anchor that does not exist.

Run locally with: python3 tools/check-links.py
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urldefrag

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "company.html", "careers.html"]

REF = re.compile(r'(?:src|href)\s*=\s*"([^"]+)"')
ID = re.compile(r'\bid\s*=\s*"([^"]+)"')
CSS_URL = re.compile(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)')

def external(target):
    return target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//"))

def anchors(path):
    return set(ID.findall(path.read_text(encoding="utf-8")))

def check(page_files, css_files):
    problems = []
    for name in page_files:
        page = ROOT / name
        text = page.read_text(encoding="utf-8")
        own = anchors(page)
        for raw in REF.findall(text):
            if external(raw):
                continue
            target, frag = urldefrag(unquote(raw))
            if not target or target == "./":
                dest = page
            else:
                dest = (page.parent / target).resolve()
                if not dest.exists():
                    problems.append(f"{name}: missing file {target}")
                    continue
            if frag:
                if dest.suffix != ".html":
                    continue
                if frag not in (own if dest == page else anchors(dest)):
                    problems.append(f"{name}: no id #{frag} in {dest.name}")

    for name in css_files:
        sheet = ROOT / name
        for raw in CSS_URL.findall(sheet.read_text(encoding="utf-8")):
            if external(raw):
                continue
            if not (sheet.parent / unquote(raw)).resolve().exists():
                problems.append(f"{name}: missing file {raw}")
    return problems

def orphans():
    used = "".join((ROOT / p).read_text(encoding="utf-8") for p in PAGES)
    return [f.name for f in sorted((ROOT / "assets/img").iterdir()) if f.name not in used]

def main():
    missing_pages = [p for p in PAGES if not (ROOT / p).exists()]
    if missing_pages:
        print("missing page: " + ", ".join(missing_pages))
        return 1

    css = [str(p.relative_to(ROOT)) for p in (ROOT / "assets").rglob("*.css")]
    problems = check(PAGES, css)

    for name in orphans():
        print(f"note: assets/img/{name} is not referenced by any page")

    if problems:
        print()
        for p in problems:
            print(f"error: {p}")
        print(f"\n{len(problems)} broken reference(s)")
        return 1

    print(f"checked {len(PAGES)} pages and {len(css)} stylesheets; all references resolve")
    return 0

if __name__ == "__main__":
    sys.exit(main())
