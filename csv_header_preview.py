#!/usr/bin/env python3
"""Preview CSV Cleanup's ASCII header renaming without reading or writing files."""
from __future__ import annotations

import argparse
import json
import re


def snake(header: str) -> str:
    text = re.sub(r"[^0-9a-zA-Z]+", "_", header.strip()).strip("_").lower()
    return text or "column"


def preview_headers(headers: list[str]) -> list[dict[str, str | int]]:
    """Return original/proposed names by position; never change caller data."""
    names: set[str] = set()
    result = []
    for position, raw in enumerate(headers, start=1):
        name, n = snake(raw), 2
        while name in names:
            name, n = f"{snake(raw)}_{n}", n + 1
        names.add(name)
        result.append({"position": position, "original": raw, "proposed": name})
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("headers", nargs="+", help="Quote each literal header as one argument")
    args = parser.parse_args(argv)
    print(json.dumps({"warning": "ASCII renaming can lose accents, non-Latin text and currency distinctions; review every proposed name. No CSV or data cells were read or changed.", "headers": preview_headers(args.headers)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
