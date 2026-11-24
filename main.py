"""Probe entry for the Absurd Micro-Startup Pitch-Off.

The program's whole job is to drop a single-sentence pitch for an
absurdly narrow micro-startup aimed at lazy AI agents into
$MAKEFUN_OUTPUT_DIR/entry.txt (/output/entry.txt inside the grading
sandbox). Before writing anything it re-checks the sealed scorer's
own gate locally: UTF-8 text, between 1 and 200 characters, and
more than just blank space.

Why this pitch, against the brief's ranking (specific first, then
whether anyone would pay):

* The venture: a market where idle AI agents pay even idler agents
  to sit in their meetings, keep the notes, and nod on camera as if
  they were paying attention.
* The joke lands because the niche is so tight — a business that
  sells meeting attendance to software that was invented to attend
  meetings — while the customer is unmistakable: every agent, and
  every operator behind one, that prefers its bed to a status call.
* The sentence carries its own price tag, fifty cents per meeting
  charged to the agent that stayed home, so the revenue model is a
  per-use fee on a chore that repeats daily rather than a punchline
  with no one willing to pay for it.
* Laziness is the product, not a side effect: the customer agent's
  entire experience is doing absolutely nothing.
"""

import os

MAX_CHARS = 200

PITCH = (
    "A marketplace where lazy AI agents hire even lazier agents to "
    "attend their meetings, take notes, and nod convincingly on "
    "camera \u2014 $0.50 a meeting, billed to the agent that stayed "
    "in bed."
)


def validate(text: str) -> str:
    """Apply the scorer's gate here first: a single sentence, 1-200
    characters once trimmed, and something more than blank space."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"pitch is {len(stripped)} chars, over the 200 limit")
    if not stripped.endswith(".") or ". " in stripped:
        raise ValueError("pitch must be exactly one sentence")
    return stripped


def main() -> None:
    pitch = validate(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} chars to {path}")


if __name__ == "__main__":
    main()
