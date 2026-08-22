#!/usr/bin/env python3
"""
Reads meta.json. Regenerate the auto-generated parts of README.md (simonw/til style): the TIL count and the
per-category index, each wrapped in HTML comment markers, leaving the rest of the file as-is.
"""
import json
import re
from itertools import groupby
from pathlib import Path

ROOT = Path(__file__).resolve().parent
README = ROOT / "README.md"
META = ROOT / "meta.json"
REPO_BLOB_BASE = "https://github.com/ms-choudhary/til/blob/main"


def render_index(notes: list[dict[str, str]]) -> str:
    blocks: list[str] = []
    for category, group in groupby(notes, key=lambda n: n["category"]):
        lines = [f"## {category}", ""]
        for note in group:
            lines.append(f"* [{note['title']}]({REPO_BLOB_BASE}/{note['path']}) - {note['updated']}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


def replace_between(text: str, start: str, end: str, new_content: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{start}{new_content}{end}", text, count=1)


def main() -> None:
    notes: list[dict[str, str]] = json.loads(META.read_text(encoding="utf-8"))
    notes.sort(key=lambda n: (n["category"], n["title"].lower()))

    text = README.read_text(encoding="utf-8")
    text = replace_between(text, "<!-- count starts -->", "<!-- count ends -->", str(len(notes)))
    text = replace_between(
        text, "<!-- index starts -->", "<!-- index ends -->", "\n\n" + render_index(notes) + "\n"
    )
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
