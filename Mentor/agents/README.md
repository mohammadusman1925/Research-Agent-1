# The three agents

The mentor's hands. Each one owns exactly one move and runs it the same way every time.

They are not separate systems. They read the mentor's brain, they share its client card, and they report back to it.

| Agent | Command | The move | Layers | Beats |
| --- | --- | --- | --- | --- |
| Use Case | `/use-case` | Keep the reason it works. Change the moment it happens in | 2 | 5 to 7 |
| Angle | `/angle` | Keep the moment. Change the reason | 2 | 6 to 8 |
| Iteration | `/iteration` | Same ad, new front door | 0 | 1 |

And one builder, which is not a move:

| Agent | Command | What it makes |
| --- | --- | --- |
| Static Image | `/static-image-brief` | Nine headlines, then image descriptions an editor can build from |

**Scaling is not a fourth agent.** It is the use case swap run three to five times with the angle locked, so the Use Case Agent owns it.

## Which one to open

Default to `/mentor` and say what you want. It routes.

Go direct only when you are certain, because "a new angle" usually means a new scene, and going straight to `/angle` gets you an eight beat rewrite when you wanted a two hundred word swap.

## What each folder holds

```text
agents/<name>/
  AGENT.md      how it behaves
  the-move.md   the rules of its move. The only file that is its alone
```

The static image agent has `the-brief.md` instead of `the-move.md`, because it makes a deliverable rather than running a test.

Everything else it needs lives in `../brain/`, `../clients/` and `../guides/`. One copy, shared by all three, so a correction made once is true everywhere.

## The order you normally run them

1. Prove something with an **iteration**. Cheapest test there is.
2. Widen it with **use case swaps**. This is where volume comes from.
3. Keep going until three to five scenes work. That is scaling. Build the dedicated landing page, then raise budget.
4. Run the winners in another **bucket**. UGC, then VSL. Exhaustion is per bucket, not per angle.
5. Only then reach for an **angle swap**, when the argument itself stops producing.

## The one test that names the move

**Beat 10, the mechanism.**

The iteration and the use case swap both leave it alone. The angle swap rewrites it. If you set out to change the angle and beat 10 still reads the same, you did not change the angle.
