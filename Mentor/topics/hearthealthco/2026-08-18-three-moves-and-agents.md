# The three moves, and the agents built from them, 18 Aug 2026

**Asked:** what is a use case, how does iteration work, what is the strategy to scale an angle, and then: make all of it reusable for another client.
**Mode:** concept, then build
**Agent:** mentor

## Where it stands

Built. Three agents, seven guides, one mentor brain. Portable.

## What was actually learned

### A use case is the moment, not the person

If you cannot film it, it is not a use case. It is a demographic. Four ingredients: the person, the place, the trigger, what is going wrong. Written as a name plus a scene in one line.

Cluster is the folder. Use case is the scene inside it. Angle is why the scene hurts.

### There are three moves, not three swaps

| Move | Layers | Beats | Named |
| --- | --- | --- | --- |
| Iteration | 0 | 1 | ITE |
| Use case swap | 2 | 5 to 7 | NN |
| Angle swap | 2 | 6 to 8 | NN |

Scaling is not a fourth move. It is the use case swap run three to five times with the angle locked.

### Beat 10 is the only honest test

The iteration and the use case swap both leave the mechanism alone. The angle swap rewrites it. If you set out to change the angle and beat 10 still reads the same, you did not change the angle.

Count the beats afterwards and the count names the test.

### Pick the new scene by the feeling, not the topic

The first use case swap proposed here, "she was told she is not bad enough for surgery yet", was a bad swap. Good scene, but the emotion flipped from dread of the irreversible to abandonment. Two variables moved.

The cortisone ladder keeps the same dread. One variable.

This is the most common way a test breaks and the hardest to see.

### The image comes from the hook, never from the layer

Not from the use case as a category, not from the pain point as a category. From whatever noun the hook names. If the hook has no photographable noun, go up one step to the scene it came from and take an object out of that. Never invent an object that is not in the copy.

### The scenes are already in the winning script

Five use cases were mapped off the control ad without inventing anything. They were buried at beats 3, 4, 6, 7 and 14, where only readers who get 800 words in ever see them.

Research does not invent a scene. It ranks the ones already written and says which has earned the front page.

## Two corrections taken

**Guide 04 was a strategy document when a sample was asked for.** Rebuilt as five scenes with only the lines that move.

**The beat tables looked jumbled** because they followed script order, not number order. The control delivers the guarantee at beat 18 before the results at beat 14, deliberately, as a line the narrator says. Number order and reading order are not the same thing. The four phases were added to make that readable.

## What got built

| | Where |
| --- | --- |
| Three agents, working under the mentor | `Mentor/agents/` |
| The mentor brain and the baseline, shared by all three agents | `Mentor/brain/MODULE-1.1-MENTOR-BRAIN.md` |
| Seven guides as MD, PDF and live pages | `Mentor/guides/ARTIFACTS.md` |
| What is running and what is next | `Mentor/brain/STATE.md` |
| What the agents report | `Mentor/brain/LEDGER.md` |

## The principle

Hopkins, and the sixth pillar in the baselines: opinion is where you start, data is where you end.

Applied here it meant counting beats. "I changed the angle" is an opinion. "Eight beats moved and one of them was the mechanism" is data, and it is the only way to know which test was actually run three months later.

## Decided

Reusable structure approved. Agents report to the mentor through the ledger. Nothing gets saved without being asked first.
