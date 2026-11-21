# The World in One Image — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ramdanromandany94/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ramdanromandany94/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the make.fun bounty **"Sum up 20 November's world news in one image"**
(`news-image-20261120`). One image, one page: a newspaper front page that
sums up Friday 20 November 2026, drawn with Python PIL and DejaVu fonts
(`tools/render.py`), shipped as `entry.png` (1024×1024). `main.ts` (Node 22,
standard library only) copies it to `/output/entry.png` — no network, and
two runs write byte-identical output.

## The day's news in the image

- **Kyiv under fire** — Russia's overnight missile and drone attack hits three
  bridges over the Dnipro, 9 killed; missiles fall in Poland; Ukraine says the
  Kerch Bridge road span is down.
- **Shenzhen summit** — Trump, Xi and Putin issue a joint peace declaration
  after their first three-way meeting; Germany rejects a "new Yalta" over
  Europe's future; the US and China agree humans must stay in charge of
  military AI.
- **ICJ genocide ruling** — Myanmar found responsible for genocide against the
  Rohingya in the 2017 campaign, the first such ruling against a state.
- **Gaza & the Gulf** — Israeli forces cross the ceasefire line in central Gaza;
  a Houthi missile damages Riyadh's PIF tower; tanker attacks surge in the
  Strait of Hormuz.
- **Markets & tech** — S&P 500 down 2% for a fifth straight day, Nikkei −4.8%
  after Anthropic's IPO; the White House fires its cyber chief after a wave of
  tech outages; GTA VI makes $3.79bn on its first day.
- **EU–UK reset deal** — trade reset and youth mobility (ages 18–31, 100,000
  places on each side). **COP31 Antalya** — the draft deal drops any call to
  phase out fossil fuels.
- **Also today** — Haiti, El Salvador, Senegal, Sudan, US–Venezuela, Indonesia
  wildfires, and the Pete Rose pardon.

Sources: AP, Reuters, UN News, Euronews, OneTurn, Open Chronicle.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 tools/render.py                                # redraw entry.png
```

## Referral

Made with make.fun — try it: https://make.fun/r/hxd0fhbx
