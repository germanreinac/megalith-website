# Notes for Claude

- The logo is just **Megalith** (the wordmark image in `assets/brand/`). Do not add "Islands" to it. The world is
  called the Megalith Islands, and that name can appear inside the scene (for example on the billboard).
- Layout: the sea fills the whole window. No comic-panel frame (Germán removed it). UI is minimal: the logo
  top-left with a white sticker edge, three round buttons bottom-right, one hint, speech bubbles. Keep it clean.
  All text uses Bruno Ace; UI lines use the logo's purple.
- Controls: tap = one wave; press and hold = a steady stream of waves that follows the finger; double-tap = the boat
  ducks under and jumps; a quick drag looks around; pinch or scroll zooms.

- Germán is an artist, not a developer. Explain setup simply, keep code well commented,
  and let him test each step. Ask before big design decisions.
- Performance on phones matters: keep the water grid and pixel ratio modest, test at 390 px wide.
- Plain static site, no build step. Three.js r149 UMD from jsDelivr (`three@0.149.0/build/three.min.js`).
- The look must match the comic pages: mint water with blobby flat shapes outlined in blue,
  pink sky, lilac clouds with purple outlines, purple line colour on the boat, print grain. Germán's own art in `assets/` always wins over imitations in code.
- Characters: Dji (the bird with the red ear-tubes) and Skit (the grey cat). The comic is by
  Germán Reina and Lizz Lunney. No release date yet, so no countdown. No destination island: the sea is
  open and endless, and the Patreon and newsletter links sit in the ? panel.
- The sea is split into 85-unit squares; each square always holds the same thing (a lighthouse, a sign buoy,
  the Donnie Voyagio billboard, a whirlpool, or nothing). Designs come from `reference/DRIVE-ANALYSIS.md`.
- Weather cycles calm, wind, storm, dusk, night. Objects are tinted by `shared.uTint`; lighthouse lamps glow at night.
- Fish are the comic's round, blue, one-eyed fish. There is NO fish catching (Germán removed it): fish are
  ambient and leap out of the boat's way. `assets/rewards/` holds the Patreon reward characters, currently unused.
- Germán's Drive has a folder `Claude Experiments`; he asked that anything saved to Drive for this site go in a new
  folder inside it.
- Lettering font: Bruno Ace (Google Fonts), the closest match to the comic's lettering.
- The boat is Germán's Blender model (`assets/boat/Skit-and-Dji-boat.blend`). Run
  `python3 assets/boat/export_blend.py <blend> assets/boat/boat-data.js assets/boat/boat.glb` (needs `pip install bpy`)
  to regenerate the web data after the model changes. Part names are mapped inside that script.
- Line art rule from Germán's brush set-up (`reference/brush-set-up.jpg`): one line width everywhere,
  only the opacity varies. Never vary line thickness.
- Source art lives in Germán's Google Drive folder `megalith` (Ships, Logo, 3D, 0_Pages, Character concepts...).
  The Drive connector caps downloads at 10 MB per file; use the direct link route below for bigger ones.
- The published preview artifact is the same page without the html/head wrapper and with boat-data.js inlined; keep both in step.
- Goal of the toy: moving the boat through the sea should feel satisfying. The boat rides on springs, and surfs
  wave slopes.
- Water is a jelly sea: real-water lighting (sky reflection, light glowing through thick crests, wet highlights,
  depth shapes under the surface) mixed with Germán's art (his palette, flat lighter blob shapes, ONE outline per
  shape at a single width, sparse dash marks, outlined foam). Germán found nested contour lines, pill highlights
  and extra patches "messy": keep the surface clean and smooth.
- Boat physics: springs for bob/pitch/roll, a keel (resists sideways sliding), weighted turning, surfing on slopes,
  splashdown ripples after a big pop.
- Large Drive files: the folder is shared by link, so files of any size download with
  `curl -L "https://drive.usercontent.google.com/download?id=<id>&export=download&confirm=t"`.
- The wave maths exists twice (GLSL in the water shader and JavaScript for buoyancy).
  Change both together, or the boat stops sitting on the visible surface.
