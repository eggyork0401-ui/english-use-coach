#!/usr/bin/env python3
"""Export original practice cards to Anki text import format, using only stdlib."""

import argparse
import csv
import io
import json
import re
import sys
import unicodedata
from pathlib import Path


def clean_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: expected a non-empty string")
    if any(unicodedata.category(ch) in {"Cc", "Zl", "Zp"} for ch in value):
        raise ValueError(f"{label}: control characters and line breaks are not supported")
    if "<" in value or ">" in value:
        raise ValueError(f"{label}: use plain text, without angle brackets or HTML")
    return value.strip()


def render_cards(cards):
    if not isinstance(cards, list) or not cards:
        raise ValueError("input must be a non-empty JSON array")
    rows = []
    seen = set()
    for number, card in enumerate(cards, 1):
        if not isinstance(card, dict):
            raise ValueError(f"card {number}: expected an object")
        if set(card) - {"front", "back", "tags"}:
            raise ValueError(f"card {number}: unsupported fields; use front, back, tags")
        front = clean_text(card.get("front"), f"card {number} front")
        back = clean_text(card.get("back"), f"card {number} back")
        if front.startswith("#"):
            raise ValueError(f"card {number}: front must not start with #")
        if front in seen:
            raise ValueError(f"card {number}: duplicate front; combine or disambiguate cards")
        seen.add(front)
        tags = card.get("tags", [])
        if not isinstance(tags, list) or any(
            not isinstance(tag, str) or not re.fullmatch(r"[\w-]+", tag)
            for tag in tags
        ):
            raise ValueError(f"card {number}: tags must be a list of words without spaces")
        rows.append((front, back, " ".join(dict.fromkeys(tags))))
    stream = io.StringIO(newline="")
    stream.write("#separator:Tab\n#html:false\n#tags column:3\n#columns:Front\tBack\tTags\n")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerows(rows)
    return stream.getvalue()


def export_cards(source, destination, overwrite=False):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError("input and output paths must differ")
    cards = json.loads(source.read_text(encoding="utf-8-sig"))
    rendered = render_cards(cards)  # Validate everything before opening output.
    with destination.open("w" if overwrite else "x", encoding="utf-8", newline="") as handle:
        handle.write(rendered)
    return len(cards)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON array with front/back/tags")
    parser.add_argument("output", type=Path, help="new Anki text file, usually .tsv")
    parser.add_argument("--overwrite", action="store_true", help="replace an existing output")
    args = parser.parse_args()
    try:
        count = export_cards(args.input, args.output, args.overwrite)
    except (OSError, ValueError) as exc:
        print(f"Export failed: {exc}", file=sys.stderr)
        return 1
    print(f"Exported {count} cards. Review the file in Anki before importing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
