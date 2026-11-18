"""News Image 18 November 2026 entry.

Copies the bundled editorial image to /output/entry.png.
No network access, no randomness, no time dependence:
running it twice writes the same bytes.
"""
import os
import shutil
import sys


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    for target in ("/output/entry.png", os.path.join(here, "output", "entry.png")):
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(source, target)
            print(f"Wrote {target}")
            return
        except OSError:
            continue
    print("Could not write /output/entry.png", file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
