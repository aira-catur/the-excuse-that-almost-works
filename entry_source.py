"""Authored entrypoint for the clever-excuse entry.

Writes the excuse line into the output directory expected by the runner.
"""

import os
from pathlib import Path


DEAD_KEY_FOB_FINAL_LINE = (
    "Can't get in today, my car key battery died and the spare "
    "is in my desk drawer at work"
)


def resolve_output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw)


def main() -> None:
    target_dir = resolve_output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_path = target_dir / "entry.txt"
    entry_path.write_text(DEAD_KEY_FOB_FINAL_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
