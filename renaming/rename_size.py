#!/usr/bin/env python3
"""
Rename chromosome names in a two-column chrom.sizes file.

Usage
-----
python rename_sizes.py  in.sizes  out.sizes
"""

import sys
from pathlib import Path

# ------------------------------------------------------------------ mapping --
ROMAN2NC = {
    "chrI": "NC_001133.9",
    "chrII": "NC_001134.8",
    "chrIII": "NC_001135.5",
    "chrIV": "NC_001136.10",
    "chrV": "NC_001137.3",
    "chrVI": "NC_001138.5",
    "chrVII": "NC_001139.9",
    "chrVIII": "NC_001140.6",
    # full native chromosome IX (not split) would be NC_001141.2
    # chrIXL (left arm) intentionally left unmapped
    "chrX": "NC_001142.9",
    "chrXI": "NC_001143.9",
    "chrXII": "NC_001144.5",
    "chrXIII": "NC_001145.3",
    "chrXIV": "NC_001146.8",
    "chrXV": "NC_001147.6",
    "chrXVI": "NC_001148.4",
    "chrMT": "NC_001224.1",
}
# ---------------------------------------------------------------------------


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    src, dst = map(Path, argv[1:])

    with src.open() as fin, dst.open("w") as fout:
        for line in fin:
            if not line.strip():
                continue  # skip blank lines
            name, length, *rest = line.rstrip("\n\r").split("\t")
            new_name = ROMAN2NC.get(name, name)
            fout.write("\t".join([new_name, length] + rest) + "\n")


if __name__ == "__main__":
    main(sys.argv)
