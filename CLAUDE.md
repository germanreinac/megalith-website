# Notes for Claude

- The comic's title is **Megalith Islands** (the logo wordmark reads MEGALITH; "Islands" is set under it).

- Germán is an artist, not a developer. Explain setup simply, keep code well commented,
  and let him test each step. Ask before big design decisions.
- Performance on phones matters: keep the water grid and pixel ratio modest, test at 390 px wide.
- Plain static site, no build step. Three.js r149 UMD from jsDelivr (`three@0.149.0/build/three.min.js`).
- The look must match the comic pages: mint water with blobby flat shapes outlined in blue,
  pink sky, lilac clouds with purple outlines, purple line colour on the boat, print grain,
  rounded pink panel borders. Germán's own art in `assets/` always wins over imitations in code.
- Characters: Dji (the bird with the red ear-tubes) and Skit (the grey cat). The comic is by
  Germán Reina and Lizz Lunney. No release date yet, so no countdown. No destination island: the sea is
  open and endless, and the Patreon and newsletter links sit in the ? panel.
- The sea is split into 85-unit squares; each square always holds the same thing (a lighthouse, a sign buoy,
  the Donnie Voyagio billboard, a whirlpool, or nothing). Designs come from `reference/DRIVE-ANALYSIS.md`.
- Weather cycles calm, wind, storm, dusk, night. Objects are tinted by `shared.uTint`; lighthouse lamps glow at night.
- Fish are the comic's round, blue, one-eyed fish. Catch rewards are the Patreon reward characters in `assets/rewards/`
  (embedded in the page as data URIs).
- Germán's Drive has a folder `Claude Experiments`; he asked that anything saved to Drive for this site go in a new
  folder inside it.
- Lettering font: Bruno Ace (Google Fonts), the closest match to the comic's lettering.
- The boat is Germán's Blender model (`assets/boat/Skit-and-Dji-boat.blend`). Run
  `python3 assets/boat/export_blend.py <blend> assets/boat/boat-data.js assets/boat/boat.glb` (needs `pip install bpy`)
  to regenerate the web data after the model changes. Part names are mapped inside that script.
- Line art rule from Germán's brush set-up (`reference/brush-set-up.jpg`): one line width everywhere,
  only the opacity varies. Never vary line thickness.
- Source art lives in Germán's Google Drive folder `megalith` (Ships, Logo, 3D, 0_Pages, Character concepts...).
  Drive downloads are capped at 10 MB per file.
- The published preview artifact is the same page without the html/head wrapper and with boat-data.js inlined; keep both in step.
- Goal of the toy: moving the boat through the sea should feel satisfying. The water is meant to read as
  jelly (soft gradients, gloss, wobble); the boat rides on springs, surfs wave slopes, and a held press
  charges a bigger wave.
- The wave maths exists twice (GLSL in the water shader and JavaScript for buoyancy).
  Change both together, or the boat stops sitting on the visible surface.
