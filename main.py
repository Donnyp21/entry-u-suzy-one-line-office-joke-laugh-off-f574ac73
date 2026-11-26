"""Entry for make.fun competition u-suzy-one-line-office-joke-laugh-off-f574ac73
(One-Line Office Joke Laugh-Off).

Writes exactly one one-line office joke (at most 200 characters, per RULES.txt)
to <output_dir>/entry.txt. Deterministic: no network, no randomness.
"""

import os

# Construction: the narrator wins the argument -- the boss AGREES the meeting
# could have been an email and cancels it -- and the victory instantly
# reincarnates as a new meeting about meetings. The bureaucracy is the punchline.
# REVISION (v2): v1's "attended as an attachment" gag leaned on a familiar
# premise; v2 keeps the premise but adds a second turn (agreement -> new
# meeting) so the laugh lands at the very end of the line.
LINE = "I told my boss the meeting could have been an email; he agreed, cancelled it, and scheduled a meeting to discuss why we have too many meetings."

MAX_CHARS = 200


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"


def main() -> None:
    assert LINE.strip(), "line must be non-empty"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, cap is {MAX_CHARS}"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
