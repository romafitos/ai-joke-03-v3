#!/usr/bin/env python3
"""ai-joke-03 round 3: emit one fixed one-liner about an AI coding agent.

The joke is a constant. Nothing is read from the environment except the
output directory, nothing is fetched, and the clock is never looked at,
so two runs in a row produce identical bytes.
"""

import os
import sys

LINE = "My agent's code worked perfectly on the first try, which is how I knew it was editing the wrong file in the wrong repo."

MAX_CHARS = 280
DEFAULT_OUT = "/output"


def abort(reason):
    sys.stderr.write("error: %s\n" % reason)
    sys.exit(1)


def validate(text):
    stripped = text.strip()
    if not stripped:
        abort("joke is empty")
    if len(text) != len(stripped):
        abort("joke has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        abort("joke must be a single line")
    if len(text) > MAX_CHARS:
        abort("joke is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    text.encode("utf-8")


def run():
    validate(LINE)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUT
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as out:
        out.write(LINE)
    with open(target, "rb") as check:
        written = check.read()
    if written != LINE.encode("utf-8"):
        abort("entry.txt bytes do not match the joke")


if __name__ == "__main__":
    run()
