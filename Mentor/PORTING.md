# Porting the whole system to a new client

Copy four things, empty two, fill one.

## Copy

1. `Mentor/`
2. `.claude/skills/mentor/`, `use-case/`, `angle/`, `iteration/`, `static-image-brief/`
3. Nothing else

Two folders, and the second one is five files of fifteen lines each.

## Empty

| Folder | What to delete |
| --- | --- |
| `Mentor/clients/` | Everything except `_TEMPLATE.md`. That includes any `<brand>-core-memory.md` or `<brand>-client-voice.md` |
| `Mentor/topics/` | The client folders. Keep `_TEMPLATE.md` and blank `_index.md` |
| `Mentor/brain/STATE.md` | Overwrite it with `_STATE-TEMPLATE.md` |
| `Mentor/brain/LEDGER.md` | Overwrite it with `_LEDGER-TEMPLATE.md` |

## Fill

Copy `Mentor/clients/_TEMPLATE.md`, rename it to the brand in lower case, and fill it in.

**One card. The mentor and all three agents read the same file.**

**Leave a line blank rather than guessing.** A blank line makes the agent ask. A guessed line makes it confidently wrong.

The three lines that matter most, in order:

1. **The angle point, verbatim.** The sentence that carries the argument. Without it every test will be vague.
2. **The control script path.** There has to be something to swap against.
3. **The primary metric, and the kill and scale thresholds.** Without these nobody can read a result.

Start with those three and fill the rest in as you go.

## The guides

`Mentor/guides/` holds one brand's worked ads, labelled EXAMPLE ONLY.

| Choice | When |
| --- | --- |
| Keep them | New client with nothing of their own. A worked example beats no example |
| Replace them | Once the new client has one decoded winner. Much better |
| Delete them | If the category is far enough away that they would mislead |

To build a guide from the new client's own ad, copy the closest HTML file in `Mentor/guides/`, swap the script, then run:

```bash
python Mentor/tools/html-to-md-pdf.py Mentor/guides/<name>.html
```

Then publish it and put the URL in `guides/ARTIFACTS.md`.

## The check that proves it worked

```bash
grep -ril "<old brand name>" Mentor/ | grep -v "/clients/" | grep -v "/guides/" | grep -v "/topics/" | grep -v STATE | grep -v LEDGER
```

That should return nothing. If it returns something, the old brand has leaked into the method and it will carry the wrong assumptions into the new one.
