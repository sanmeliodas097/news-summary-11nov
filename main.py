#!/usr/bin/env python3
"""World news summary entry for make.fun's "Write the best summary of
11 November's world news" bounty.

The program writes one summary, in English, of the world's news of
Wednesday 11 November 2026 to /output/entry.txt. The summary is the summary.txt file shipped beside this program; copying it byte-for-byte
keeps every run identical with no network access. The gate requires UTF-8 text of
1 to 2,000 characters, so the program checks the length and that the text is not
only white space before it reports success.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "summary.txt"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    shutil.copyfile(SOURCE, target)
    # The run is only valid if the copy is complete: the output must be
    # byte-for-byte the summary this program ships.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.txt incomplete: size differs from summary.txt")
    text = target.read_text(encoding="utf-8")
    if not 1 <= len(text) <= 2000:
        raise SystemExit(f"entry.txt is {len(text)} characters, must be 1-2000")
    if not any(not ch.isspace() for ch in text):
        raise SystemExit("entry.txt is only white space")
    print(f"wrote {target} ({len(text)} characters)")


if __name__ == "__main__":
    main()
