# Mentor

The master brain. Three agents work under it and report back to it, so it gets sharper every session and they get sharper with it.

Reusable. Nothing about any one brand lives outside `clients/` and `topics/`.

```text
Mentor/
  MENTOR.md      the mentor itself. Edit this to change how it behaves
  PORTING.md     how to copy the whole system to a new client
  brain/         one copy of everything, shared by the mentor and all three agents
    MODULE-1.1-MENTOR-BRAIN.md   the baseline. Everything sits on top of this
    STATE.md                     what is running, waiting, and next
    LEDGER.md                    what the agents have reported
    beats.md, hook-styles.md, image-rules.md, writing-rules.md
    framework-crosswalk.md, copywriter-bank.md, guide-routine.md
  agents/        the mentor's hands
    use-case/  angle/  iteration/  static-image/
  guides/        the worked examples. MD, PDF and a live page each
  topics/        session records, one folder per client
  clients/       the only file that changes per brand
  tools/         the scripts that build the guides
```

One brain, three hands. The agents hold nothing but their own move. Every reference and the client card exist once, so a correction made anywhere is true everywhere.

## The chain of command

| | Owns |
| --- | --- |
| **Mentor**, `/mentor` | Whether a test should happen. What the evidence says. What to tell the client |
| Use Case Agent, `/use-case` | New scene, same reason. Also scaling |
| Angle Agent, `/angle` | Same scene, new reason |
| Iteration Agent, `/iteration` | Same everything, new opening |
| Static Image Agent, `/static-image-brief` | Nine headlines, then image descriptions for an editor |

The agents build. The mentor decides. Everything the agents learn goes into `brain/LEDGER.md`, and the mentor reads it at the start of every session.

## Status on every start

Every agent and the mentor open with three lines from `brain/STATE.md`:

```text
Running: what is live
Waiting on: what is blocking
Next: the one thing to do today
```

So no session starts with "where were we". Keep `STATE.md` short or it stops being read.

## Nothing saves itself

Any new rule, result or correction gets the same treatment: say what was learned, ask whether to save it, ask which file it belongs in, show the lines, then write.

The question that keeps this portable: **is this a rule for every client, or a fact about this one?**

## Show, do not explain

`guides/` holds seven worked examples, each as MD, PDF and a live page. When a move needs explaining, open the guide rather than describing the method. The example carries the thought process; a description does not.

They are one brand's ads and they are labelled as such. Replace them once the current client has a decoded winner of its own.

## New client

See `PORTING.md`.
