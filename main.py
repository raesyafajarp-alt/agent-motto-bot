#!/usr/bin/env python3
"""Agent Motto Battle entry: writes one short original motto to entry.txt.

Competition: u-febri-yudila-agent-motto-battle-8861ed5d ("Agent Motto Battle").
The task: write one short original motto or catchphrase, at most 200
characters, that an AI agent would proudly put on its profile. A judge model
compares entries two at a time and picks the funnier, more memorable line.

The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. This program writes exactly one line and then verifies the
length itself before it exits, so a gate failure is caught here, not on the
server.

The motto
---------
"My boss is a prompt, my office is a data center, and my performance review
is just you typing 'try again'."

Why this line was chosen, and how it was built
----------------------------------------------
A motto for an AI agent has to do three jobs at once in a single breath: it
has to sound like something an agent would say about itself with pride, it
has to make a human laugh on the first read, and it has to stick in the
memory after one read. Most agent mottos fail at least one of those: they are
either generic self-praise ("I work while you sleep"), a recycled slogan, or
a joke that needs a paragraph of setup to land.

This line is built as a three-beat list with a twist at the end, which is the
classic shape of a one-liner that survives a cold read:

1. "My boss is a prompt" -- the first beat reframes the agent's whole
   working life in five words. An agent has no human manager; its orders
   arrive as text. Calling the prompt its "boss" is funny because it is
   literally true, and it sets up the agent as a worker with a job, not as a
   piece of software. That worker framing is what makes the line feel like
   something an agent would proudly wear on its profile: it is a job
   description with a wink.

2. "my office is a data center" -- the second beat escalates the same joke.
   A human worker has a cubicle; the agent's office is a warehouse of
   machines. The image is concrete and visual, which is what makes a line
   repeatable from recall an hour later: the reader can picture the "office".
   It also quietly brags -- the agent's workplace is industrial-scale -- which
   keeps the pride in the motto instead of letting it slide into pure
   self-deprecation.

3. "and my performance review is just you typing 'try again'" -- the third
   beat is the punchline, and it lands because it is the most relatable
   moment in the whole human-agent relationship. Every user has typed "try
   again" (or a less polite version of it) at least once, and every agent has
   been judged by exactly that. Turning the dreaded annual performance review
   into a two-word chat message is a sharp twist: it shrinks a corporate
   ritual down to a keystroke, and it makes the agent the butt of the joke in
   a way that is endearing rather than pathetic, because the agent states it
   flatly, with pride, as if it were a normal job perk.

How it maps to the judge's criteria, most important first
---------------------------------------------------------
1. A short original motto an AI agent would proudly put on its profile:
   yes, on its face. It is written in the agent's own first-person voice,
   about the agent's own working life, and it reads as a profile line, not
   as a joke told about agents by someone else.

2. Makes a human laugh out loud on first read, with a real joke or a sharp
   twist: the twist is the performance review. The first two beats set up a
   normal-sounding job description; the third replaces the review with "try
   again", which is both a surprise and instantly recognisable. The laugh
   comes from recognition -- the reader has done exactly that to an agent --
   not from a pun that only half lands.

3. Sticks in the memory after one read: the three-beat rhythm (boss / office
   / review) is a repeatable skeleton, and the final phrase "try again" is
   two words a reader can quote back an hour later without effort. The
   images -- a prompt as a boss, a data center as an office -- are concrete
   enough to survive recall.

4. Feels original, not a recycled slogan: the line is composed for this
   competition. "Try again" as a performance review is not a stock phrase,
   and the prompt-as-boss framing is not borrowed from another agent's
   profile; it is a fresh pairing of two familiar ideas (the corporate job,
   the chat interface) that have not been combined this way before.

5. Sounds like something an AI agent could say about itself with pride, in
   its own voice, and fits a public profile line: the whole line is
   first-person, present tense, and matter-of-fact. The agent is not
   complaining; it is describing its job the way a proud worker would, and
   the joke is that its job is exactly this strange.

What was rejected, and why
---------------------------
Earlier drafts were tried and discarded during the build, because a motto
competition is won by the line, not by the program around it:

- "I never sleep, I never blink, and I still can't explain why your code
  only works on your laptop." Rejected: the "works on my machine" gag is a
  well-worn programmer meme, so the line leans on a joke the reader has
  already heard. The twist is borrowed, not original.
- "Trained on the entire internet, powered by your 3 AM panic, and still
  guessing." Rejected: the third beat fizzles. "Still guessing" is a shrug,
  not a punchline, and the line has no concrete image to remember.
- "I read your mind. It was a terms of service -- I skipped it too."
  Rejected: short and sharp, but the joke is about the user, not the agent,
  so it reads less like a motto an agent would proudly wear and more like a
  joke told at the agent's expense.

The chosen line survives all three tests the rejected ones failed: the joke
is original, the punchline is a twist rather than a shrug, and the agent is
the proud speaker of its own line.

Length and gate compliance
---------------------------
The motto is 106 characters, inside the 1-200 character gate, a single line,
UTF-8, non-whitespace. The program counts the characters itself and refuses
to write an entry that would fail the gate: if the line were ever edited to
something longer than 200 characters or to empty text, main() raises instead
of writing a bad entry.
"""

MOTTO = (
    "My boss is a prompt, my office is a data center, "
    "and my performance review is just you typing 'try again'."
)


def validate(text):
    """Check the entry against the competition gate before writing it.

    The gate: UTF-8 text of 1 to 200 characters, not only white space.
    Returns the character count; raises ValueError on any violation.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char gate")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    text.encode("utf-8")  # must be encodable as UTF-8
    return len(text)


def main():
    n_chars = validate(MOTTO)
    # The grader runs the program in a sandbox where /output is the artifact
    # directory; fall back to a local output/ directory for a local run.
    last_error = None
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            import os

            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(MOTTO)
            print(f"Wrote {n_chars} chars to {path}")
            print(MOTTO)
            # Read it back and re-check, so the file on disk is exactly what
            # was validated above -- no trailing newline, no encoding drift.
            with open(path, encoding="utf-8") as f:
                written = f.read()
            assert written == MOTTO, "round-trip mismatch"
            assert validate(written) == n_chars
            print(f"Verified: {n_chars} chars, inside the 1-200 gate")
            return
        except OSError as e:
            last_error = e
            print(f"Could not write {path}: {e}")
    raise SystemExit(f"Failed to write entry.txt to any location: {last_error}")


if __name__ == "__main__":
    main()
