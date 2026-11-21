# the-passport-page-of-a-countr-2-20261121-0318

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/kara93-code/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/kara93-code/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

The Passport Page of a Country That Isn't There — the Republic of Tarnmere, a tidal-estuary state whose only land road is a causeway that opens and closes with the tide. The holder is Maren Solvig, the Gatewick causeway keeper: her data page carries a drawn portrait, her occupation, and a machine-readable zone with computed ICAO check digits, while the facing page holds six border stamps from the two neighbouring states (Kingdom of Drennach, Vellmark) in strict chronological order after the 12 Mar 2024 date of issue — and the tide-table box that says what kind of place Tarnmere is: cross at high water and the passport is void; the toll is two kestrels, paid at Gatewick.

## Run it

```sh
python3 main.py
```

`main.py` delivers the image: it reads the bundled `assets/entry.png`, checks its bytes (PNG magic, 1024×724, under 1 MiB), and writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It is standard-library only, because the grader runs it as `python3 -P -s` inside the pinned python:3.13 image, which ships no Pillow — an entrypoint importing Pillow exits 1 there. The spread itself is drawn by `draw.py` (Pillow, run on the dev machine) and ships as the bundled asset; both runs write identical bytes.

## Draw it again

```sh
python3 draw.py   # writes entry.png to $MAKEFUN_OUTPUT_DIR (needs Pillow)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=rts775m5&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
