#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a fenced Markdown code block by zero-based position."
    )
    parser.add_argument("input_markdown", help="Path to the Markdown file")
    parser.add_argument(
        "block_index",
        type=int,
        help="Zero-based fenced code block index to extract",
    )
    parser.add_argument("output_file", help="Path to write the extracted code")
    parser.add_argument(
        "--language",
        help="Optional fence language to filter by before indexing",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.input_markdown).read_text()
    pattern = re.compile(r"```([^\n`]*)\n(.*?)\n```", re.S)
    matches = list(pattern.finditer(source))

    blocks: list[tuple[str, str]] = []
    for match in matches:
        language = match.group(1).strip()
        code = match.group(2)
        if args.language and language != args.language:
            continue
        blocks.append((language, code))

    if args.block_index < 0 or args.block_index >= len(blocks):
        available = len(blocks)
        raise SystemExit(
            f"Requested block index {args.block_index}, but only {available} matching block(s) were found."
        )

    output = Path(args.output_file)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(blocks[args.block_index][1] + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
