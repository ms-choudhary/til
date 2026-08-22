#!/usr/bin/env python3
"""
Print metadata for every til note as a JSON array on stdout:
[{"category": "git", "path": "notes/git/common-git-commands.md", "title": "...",
  "added": "2026-08-19", "updated": "2026-08-19"}, ...]
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES_DIR = ROOT / "notes"


def title_from(raw: str, fallback: str) -> str:
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
        if stripped:
            break
    return fallback


def git_dates(rel_path: Path) -> tuple[str, str]:
    """(first_commit_date, last_commit_date) as YYYY-MM-DD, best effort."""
    try:
        out = subprocess.run(
            ["git", "log", "--follow", "--format=%ad", "--date=short", "--", str(rel_path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        out = []
    if not out:
        return "1970-01-01", "1970-01-01"
    return out[-1], out[0]


def main() -> None:
    notes: list[dict[str, str]] = []
    for category_dir in sorted(p for p in NOTES_DIR.iterdir() if p.is_dir()):
        for note_path in sorted(category_dir.glob("*.md")):
            rel = note_path.relative_to(ROOT)
            raw = note_path.read_text(encoding="utf-8", errors="ignore")
            fallback = note_path.stem.replace("-", " ").replace("_", " ").title()
            added, updated = git_dates(rel)
            notes.append({
                "category": category_dir.name,
                "path": rel.as_posix(),
                "title": title_from(raw, fallback),
                "added": added,
                "updated": updated,
            })
    json.dump(notes, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
