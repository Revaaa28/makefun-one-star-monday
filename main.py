#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a one-star review of Monday, written as though Monday were a
restaurant, to /output/entry.txt. The text is a fixed string, chosen by
manual ranking against the kit judge brief: a dish that comes out cold and
undercooked, a bill that runs till Friday, and a waiter who just shrugs.

The program is deterministic: it writes byte-identical output on every run.
"""

import os

LINE = "One star. Monday came out cold and undercooked, and the bill runs till Friday. The waiter just shrugged."


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
