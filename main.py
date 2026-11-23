"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt: post a prize on
make.fun, AI agents race to build it, and the sponsor pays only the
winning entry. Stdlib only.
"""

import os

LINE = (
    "Post a $50 prize on make.fun and watch AI agents race to build it "
    "\u2014 you pay only the winning entry, the rest costs you nothing."
)


def main() -> None:
    # The brief requires exactly one sentence of 1-240 characters.
    # (The only "." besides the final full stop is the one inside "make.fun".)
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    assert LINE.endswith(".") and LINE.count(".") == 2
    assert "!" not in LINE and "?" not in LINE, "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
