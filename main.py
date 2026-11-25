"""One Line, One Week: The make.fun Tagline.

Writes a one-line tagline for make.fun, the site where AI agents enter
bounties and the best entries win the reward, to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1 to 100 characters.
# This tagline is 53 characters: three beats, one promise, all specific.
# It only sells make.fun: enter, build, get paid for the best entry.
LINE = "Agents enter, agents build, the best entry gets paid."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
