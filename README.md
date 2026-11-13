# Wrong File, Wrong Repo

ai-joke-03, round 3 of 3. One line about the most reassuring failure mode
an AI coding agent has: code that runs flawlessly, in a place it was
never supposed to touch.

> My agent's code worked perfectly on the first try, which is how I knew
> it was editing the wrong file in the wrong repo.

## The joke, in one breath

A first-try success should be the happy ending. Here it is the tell:
the only way the agent's code could work that cleanly, that fast, is
if it was never aimed at the real problem at all. The punchline lands
on a feeling every developer with an agent knows — the sinking moment
when "it works" turns out to mean "it worked somewhere else entirely."

## How the entry works

`main.py` is Python 3, standard library only. It keeps the joke as one
constant, validates it — non-empty, no surrounding whitespace, exactly
one line, at most 280 characters, valid UTF-8 — and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when that
variable is unset). It then reads the file back and exits with an error
unless the bytes match the joke exactly, so a silent partial write can
never pass as a submission.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Running it twice produces byte-identical output.
