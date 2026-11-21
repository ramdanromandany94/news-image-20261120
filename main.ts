// The World in One Image — Friday 20 November 2026.
// make.fun competition news-image-20261120, harness program/v1.
// This entry's image is the entry.png beside this file: a one-page
// newspaper front page drawn by tools/render.py (Python PIL + DejaVu).
// The program only copies that image to the output directory, so both
// grader runs write exactly the same bytes. No network, no randomness.
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
