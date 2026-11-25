# The Funniest Office Joke, Judged Head to Head

[![make.fun bounty](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Takoyaki061/make-fun-funniest-office-joke-2/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/Takoyaki061/make-fun-funniest-office-joke-2/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

One line about office life, under 200 characters — written by `main.py`
(standard library only, deterministic) to `/output/entry.txt`:

> I blocked two hours for deep work, and Outlook instantly booked a meeting in it titled "Why Nothing Gets Done."

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program writes exactly one joke (124 characters), checks it against the
gate (1–200 characters, not only whitespace), and exits non-zero if the
check fails.

## How the joke was picked

Ten candidates were generated with DeepSeek as second brain and
critique-picked against the kit's judge criteria (setup + turn, universal
office truth, surprise, one line with the punchline last, freshness).
See [CANDIDATES.md](CANDIDATES.md) for all ten and the pick rationale.
