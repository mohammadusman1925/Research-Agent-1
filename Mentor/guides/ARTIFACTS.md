# The guides

Every guide exists three ways. The MD to read in the repo, the PDF to print or send, and a live page to open in a browser.

**These are one brand's worked ads.** They are here to show the thought process instead of explaining it. Do not quote their numbers as evidence about a different client. When the current client has a decoded winner of their own, build a guide from that and retire the borrowed one.

| Guide | What it shows | MD | PDF | Live page |
| --- | --- | --- | --- | --- |
| The Four Moves | The whole system. Three moves, the four phases, all 19 beats, which move touches which | `The-Four-Moves.md` | `The-Four-Moves.pdf` | https://claude.ai/code/artifact/9e5dfdef-b0f6-4987-9eac-64f51175c3f1 |
| One Script, Three Ways | The same 17 beats rewritten by each of the three moves, side by side | `One-Script-Three-Ways.md` | `One-Script-Three-Ways.pdf` | https://claude.ai/code/artifact/fcd155da-4185-44ac-8f90-f565dec48ee3 |
| Use Case Swap | New scene, same reason. 2 layers, 6 beats. Full script side by side | `Use-Case-Swap-Sample.md` | `Use-Case-Swap-Sample.pdf` | https://claude.ai/code/artifact/82bbe3d2-2152-4fa8-af8d-44406e05548a |
| Angle Swap | Same scene, new reason. 2 layers, 8 beats. Full script side by side | `Angle-Swap-Sample.md` | `Angle-Swap-Sample.pdf` | https://claude.ai/code/artifact/bb37c9c3-ac5f-4e5e-8b5e-38d098988ea8 |
| Hook Iteration | Same everything, new door. 0 layers, 1 beat. Three doors | `Iteration-Sample.md` | `Iteration-Sample.pdf` | https://claude.ai/code/artifact/b34c9452-b0aa-43b9-a336-4c1c6c7a04f8 |
| Five Doors, One Angle | Scaling. Five scenes off one control script, only the lines that move | `Scaling-One-Angle.md` | `Scaling-One-Angle.pdf` | https://claude.ai/code/artifact/8c5efd3b-2f29-40fc-abfb-2dff29bfe494 |
| Ad 03, The Sleep Ad | One swap written out end to end, with the winning DNA check | `Ad-03-Sleep.md` | `Ad-03-Sleep.pdf` | https://claude.ai/code/artifact/6ac86c03-bedd-49a1-9ca0-4c701568a165 |

## Which guide to show

| The question | Show |
| --- | --- |
| What are the moves | The Four Moves |
| What is the difference between them | One Script, Three Ways |
| How do I change the scene | Use Case Swap |
| How do I change the argument | Angle Swap |
| How do I test new hooks | Hook Iteration |
| How do I get more ads out of one angle | Five Doors, One Angle |
| Show me a finished one | Ad 03, The Sleep Ad |

## Rebuilding

The HTML is the source. MD and PDF are generated from it:

```bash
python Mentor/tools/html-to-md-pdf.py Mentor/guides/<name>.html
```

The live page is republished by pointing the Artifact tool at the same HTML file. Same file path keeps the same URL.

## Making a guide for a new client

1. Copy the closest existing HTML file and rename it.
2. Replace the control script and the swap with the new client's own.
3. Run the converter above for MD and PDF.
4. Publish it and put the URL in this table.

The design and the section order stay the same, so every guide in every client reads the same way.
