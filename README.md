# one-line-pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Jideweb3/one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Jideweb3/one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

An entry for the make.fun bounty **A Day of One-Line Pitches**: one sentence,
at most 240 characters, that would convince a friend who has never coded to let
an AI agent build their first app idea on make.fun. The program writes the
sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> You already did the hard part — you had the idea — so describe it in plain words on make.fun and let an AI agent build a working first version you can try tonight.

163 characters, one line. The hook reframes the ask: the friend already did the
hard part by having the idea, so saying yes costs them nothing but describing it.
"First version" keeps it honest — no promise of a finished app — and "tonight"
is the concrete reason to say yes now.

## How it was chosen

14 original candidates were drafted, each scored 1–5 on the judge's criteria
(persuasion, clarity, truth, warmth and craft), then the top 4 played a
head-to-head tournament. The winner beat the runner-up ("That idea you keep
describing at dinner only needs one telling: say it once to an AI agent and by
tonight you'll be tapping a real working version of it, without touching a line
of code.") on the freshness of its opening turn and the simplicity of its ask.
A revision pass cut the filler word "just" and named the platform — the brief's
first criterion is making the case for building on make.fun, and a sentence that
never names the place leaves that case half-made. The full tournament is recorded
in `variants.md` in the build workspace (not shipped in this repo).

## Revision

After the builder session, the parent session tightened the validator: it now
also rejects leading or trailing whitespace, so a stray space can never pad the
sentence or blunt its closing turn. The sentence itself is unchanged — it was
already clean — and the program was re-run twice to confirm byte-identical
output (163 characters, 167 bytes, sha256
`272fd0ad21cc8f74b53c86a7c9b311d8123ac49ae05d2edc6baaad080e77088c`).

## How main.py validates

The gate for this contest is 1–240 characters, a single line, not only
whitespace. `main.py` checks the line before writing, writes atomically
(temp file in the same directory, then replace), then reads the file back
and re-checks it, failing loudly on any breach. Extra checks: the line must
contain no ASCII control characters (the gate is UTF-8 text, and a stray
control character could break the judge's reading), no leading or trailing
whitespace, and the confirmation message reports both the character count
and the byte count — the line's two em dashes are 1 character but 3 bytes
each in UTF-8, so the output is 163 characters and 167 bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Standard library only (`os`, `sys`, `tempfile`). No network, no
third-party imports, deterministic output.

---

Built for [make.fun](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).
