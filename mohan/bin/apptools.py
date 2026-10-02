#!/usr/bin/env python3

"""List explicitly-installed packages that are neither omarchy baseline nor infra.

Subtracts two exclusion sets: the omarchy baseline, and an infrastructure
blocklist (kernel, firmware, audio stack, DE packages) that separates real
apps/tools from packages the installer pulled in.

https://github.com/omacom/omarchy/install/omarchy-base.packages
"""

import argparse
import sys

DEFAULT_EXPLICIT = "explicit-apps.txt"
DEFAULT_BASELINE = "apps-preinstalled.txt"
DEFAULT_INFRA = "apps-infrastructure.txt"


def read_names(path: str, required: bool = True) -> set[str]:
    names = set()
    try:
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                name = line.rsplit("\t", 1)[-1].strip()
                if name:
                    names.add(name)
    except FileNotFoundError:
        if required:
            raise
    return names


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("explicit", nargs="?", default=DEFAULT_EXPLICIT,
                        help=f"expac-style explicit list (default: {DEFAULT_EXPLICIT})")
    parser.add_argument("baseline", nargs="?", default=DEFAULT_BASELINE,
                        help=f"preinstalled package list (default: {DEFAULT_BASELINE})")
    parser.add_argument("infra", nargs="?", default=DEFAULT_INFRA,
                        help=f"infrastructure blocklist (default: {DEFAULT_INFRA})")
    args = parser.parse_args()

    try:
        excluded = read_names(args.baseline) | read_names(args.infra, required=False)
        extra = sorted(read_names(args.explicit) - excluded)
    except OSError as err:
        print(f"apptools: {err}", file=sys.stderr)
        return 1

    print("\n".join(extra))
    return 0


if __name__ == "__main__":
    sys.exit(main())
