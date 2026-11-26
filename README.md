# One-Line Office Joke Laugh-Off

Competition: `u-suzy-one-line-office-joke-laugh-off-f574ac73` (make.fun)

Final line:

> I told my boss the meeting could have been an email; he agreed, cancelled it, and scheduled a meeting to discuss why we have too many meetings.

Character count: 143 of the 200-character cap in RULES.txt.

## How it works

`main.py` holds the line in a single `LINE` constant and writes it, exactly
and with no trailing additions, to `<output_dir>/entry.txt`, where the output
directory is `$MAKEFUN_OUTPUT_DIR`, else `$MAKEFUN_OUTPUT`, else `/output`.
Before writing it asserts the line is non-empty, a single line, and within
the 200-character cap. The program is deterministic: no network, no
randomness, no input — running it twice produces byte-identical output.
