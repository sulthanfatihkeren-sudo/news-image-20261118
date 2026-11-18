# Sum up 18 November's world news in one image

Entry for make.fun bounty `news-image-20261118`.

The image is a clean editorial infographic for Wednesday 18 November 2026:

1. Xi and Putin meet in Shenzhen ahead of a three-way summit with Trump.
2. US strikes Iran's Qeshm Island, Iran strikes Bahrain and Kuwait.
3. Ukraine hits the Kerch Bridge to Crimea, part of the bridge collapses.
4. Peltola wins Alaska, Democrats take a 56-44 Senate majority.
5. Ebola surges in DR Congo, outbreak passes 11,000 cases.

## How it works

`main.py` (Python 3.13) copies the bundled `entry.png` (1024x1024, under 1 MiB)
to `/output/entry.png`. No network, no randomness, no time dependence:
two runs write the same bytes.

## Run

```bash
python3 main.py
```

## Submit

This entry still needs a public GitHub repository owned by the entrant,
a make.fun account, and the AI-agent transcripts that built it.
See https://make.fun/bounty/news-image-20261118
