"""Houseplant Out-of-Office entry for make.fun.

Writes a single out-of-office auto-reply, as if sent by the office fern,
to /output/entry.txt. Deterministic, standard library only, no network,
no input files, nothing resolved from the working directory.
"""

import os

LINE = "Out of office. The fern hasn't been watered since March and now photosynthesizes purely out of spite."

assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be whitespace-only"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
