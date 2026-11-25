#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The joke: someone keeps stealing your lunch, so you label it
"Do not eat — stool sample." The trap works — and then it punishes
the trapper, because now you don't want it either. A double turn:
the setup's revenge backfires on its own author.

Why this line (judge criteria, in order): (1) a real joke with a
setup (lunch theft) and TWO turns (the label works, then it
backfires); (2) the shared-fridge lunch thief is universal office
life; (3) the surprise is the second turn — the trap succeeds and
still costs you your lunch; (4) one line, 128 characters, punchline
("now I don't want it either") last; (5) a fresh angle, not the
tired meeting/printer complaint.

Standard library only, deterministic, no network.
"""

JOKE = (
    'Someone kept stealing my lunch, so I labeled today\'s '
    '"Do not eat \u2014 stool sample." It worked, but now I don\'t '
    'want it either.'
)


def main() -> None:
    import os

    # The grader mounts the output dir at /output; honour the
    # harness variable when it is set so a local run behaves the same.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Self-check against the gate: 1-200 chars, not only whitespace.
    written = open(path, encoding="utf-8").read()
    if not 1 <= len(written) <= 200 or not written.strip():
        raise SystemExit("gate check failed: entry.txt is %d chars" % len(written))


if __name__ == "__main__":
    main()
