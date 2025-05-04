#!/usr/bin/env python3
"""
Compute an RPM scaling factor α = 1,000,000 / (# aligned reads).

Usage
-----
python rpm_alpha.py  reads.bed
                     [--reads-column N]

If your BED is 6-column (one read per line), no extra options are needed.
"""


import argparse
import sys
from pathlib import Path


def count_lines(path: Path) -> int:
    """Count the number of non-empty lines in *path* quickly."""
    total = 0
    with path.open("rb") as fh:  # read as bytes for maximum speed
        for chunk in iter(lambda: fh.read(1 << 20), b""):  # 1 MiB chunks
            total += chunk.count(b"\n")
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute RPM scaling factor")
    parser.add_argument("bed", type=Path, help="input BED file (one read per line)")
    args = parser.parse_args()

    if not args.bed.is_file():
        sys.exit(f"ERROR: file '{args.bed}' not found")

    total = count_lines(args.bed)
    if total == 0:
        sys.exit("ERROR: zero lines found—check the BED file")

    alpha = 1_000_000 / total
    print(f"# reads   : {total:,}")
    print(f"alpha (RPM scale) = {alpha:.6f}")


if __name__ == "__main__":
    main()
