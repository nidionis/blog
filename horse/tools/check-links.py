#!/usr/bin/env python3
"""Check relative links and images in the horse/ Markdown tree.

Usage:
    python3 tools/check-links.py

Exits with status 1 if a relative target does not exist.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def iter_markdown() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def main() -> int:
    broken: list[tuple[Path, str, Path]] = []
    checked = 0

    for md in iter_markdown():
        text = md.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            checked += 1
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                broken.append((md.relative_to(ROOT), raw, resolved))

    for md, raw, resolved in broken:
        print(f"BROKEN {md}: {raw} -> {resolved}")

    print(f"Checked {checked} relative links in {len(iter_markdown())} Markdown files.")
    if broken:
        print(f"{len(broken)} broken link(s).")
        return 1
    print("All relative links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
