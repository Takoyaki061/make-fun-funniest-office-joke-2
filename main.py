#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The joke: you block two hours for deep work, and Outlook instantly
books a meeting inside it titled "Why Nothing Gets Done." — the
calendar itself staging the complaint. Standard library only,
deterministic, no network.
"""

JOKE = (
    'I blocked two hours for deep work, and Outlook instantly booked '
    'a meeting in it titled "Why Nothing Gets Done."'
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
