#!/usr/bin/env python3
"""
rename.py  <in.bedGraph>  <alias.tsv>  <out.bedGraph>

    <alias.tsv> must have two TAB-separated columns:
        old_name   new_name

Lines in the bedGraph that start with 'track', 'browser', or '#'
are passed through unchanged.  All others are assumed to begin with
a chromosome/contig name; if the name matches the alias table it is
replaced, otherwise the line is kept as is.
"""

import argparse
import sys
from pathlib import Path
import json


def rename_bedgraph(in_bg: Path, out_bg: Path, alias: dict[str, str]) -> None:
    h = out_bg.open("wt", newline="\n") if out_bg != Path("-") else sys.stdout
    with in_bg.open("rt", newline="") as fh, h:
        for line in fh:
            if line.startswith(("track", "browser", "#")):
                h.write(line)
                continue

            # split once on tab: chrom<TAB>rest_of_line
            try:
                chrom, rest = line.split("\t", 1)
            except ValueError:  # not enough columns
                h.write(line)
                continue

            chrom = alias.get(chrom, chrom)  # rename if present
            h.write(f"{chrom}\t{rest}")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Rename chromosomes in a bedGraph using a 2-column alias table"
    )
    p.add_argument("in_bg", type=Path, help="input .bg / .bedGraph file")
    p.add_argument("alias_tsv", type=Path, help="TAB-separated mapping file")
    p.add_argument("out_bg", type=Path, help="output file (use - for stdout)")
    args = p.parse_args()

    if not args.in_bg.is_file():
        sys.exit(f"Input bedGraph {args.in_bg} not found")
    if not args.alias_tsv.is_file():
        sys.exit(f"Alias file {args.alias_tsv} not found")

    alias = {v: k for k, v in json.load(open("alias.json")).items()}

    print(alias)
    rename_bedgraph(args.in_bg, args.out_bg, alias)


if __name__ == "__main__":
    main()
