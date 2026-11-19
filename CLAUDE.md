# Notes for Claude

- The logo is just **Megalith** (the wordmark image in `assets/brand/`). Do not add "Islands" to it. The world is
  called the Megalith Islands, and that name can appear inside the scene (for example on the billboard).
- Layout: the sea fills the whole window. No comic-panel frame (Germán removed it). UI is minimal: the logo
  top-left with NO outline, three buttons top-right (rounded squares, soft desaturated yellow `--box`, purple line),
  one hint, speech bubbles. Keep it clean. All text uses Bruno Ace; UI lines use the logo's purple.
- Controls (one thumb): tap = one wave (slow mode, top speed 9); press and hold = fast mode: a steady thrust away
  from the finger plus a stream of waves, top speed 26; double-tap = a hop; double-tap and keep the second tap held =
  the boat sinks, squashes flat and sways slowly for up to 4 s (`CHARGE_TIME`; no fast trembling, Germán found it
  looked like a glitch), then flies about three boat-heights
  (peak y of roughly 16) on release; a quick drag looks around; pinch or scroll zooms.
  Out of the water the boat follows gravity (`GRAVITY`), in the water a spring. `boatState.air` is only set by a
  jump or a throw of more than 1.2 units, never by ordinary bobbing (that used to block jumps in rough weather). Double-tap timing uses `event.timeStamp`.

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
  a log barrier, a ramp, the Donnie Voyagio billboard, a whirlpool, or nothing). Designs come from `reference/DRIVE-ANALYSIS.md`.
- Jumping is gameplay: floating log barriers (`logs` squares, one near the start at x 6, z -34) bounce the boat
  unless it is in the air; speed adds jump height and is kept in the air, so a running hop clears them. High jumps
  also clear signs, billboards and lighthouses (`L.top`).
- Tricks: a swipe while the boat is in the air (`startTrick`) flips it once towards the swipe, pushes it that way
  (`FLIP_PUSH`) and adds a little lift so flips chain. Landing mid-flip is a bad landing: the boat capsizes
  (`capsize`: it keeps rolling in the water and a pendulum-style keel swings it upright in about 1.5 s, with NO pause
  upside down, which Germán found unnatural; then it stays slow and "soaked" for a few seconds); landing after
  finished flips gives a small speed burst. On the water the same drag looks around.
- Impact scales with charge: `burst()` raises a water crown (`crown()`: a ring wall with tongues plus a centre
  spout, up to about 9 units tall), spray, fat blobs, a bigger ripple and up to five fish, on a charged launch and on
  hard landings. Germán wants the water, not only the fish, to carry the impact.
- Water aboard (`boatState.water`, 0 to 1): added by bad landings (0.45), deep jump charges (up to 0.3) and monster
  catches (0.3); each flip tips out 0.34; it drains very slowly alone. It lowers top speed (up to 55%), weakens
  thrust and sits the boat lower. A pool shows over the deck and a gauge appears under the buttons.
- Skit's hallucination (`fear`): Skit is afraid of water, so being sucked to the centre of a whirlpool starts a
  30 s escape (`FEAR_TIME`): the `STATES.fear` acid-on-dark palette, storm, camera shake, a dark pulsing edge and
  three sea creatures (`monsters`, speed 16.5 to 19) chasing the boat. A catch adds water and slows the boat; a boat
  in the air can't be caught. One whirlpool sits near the start at x 48, z 40.
- Ramps (`ramp` squares, one near the start at x -30, z 22): sail up the low end at speed and the boat is launched.
- Ideas agreed but not built yet: mermaid rocks (singing pulls the boat onto rocks; do tricks to impress them and
  stop it), a district of buildings standing in the sea to sail between, and rails to grind.
- Camera: free drag as before, and while holding (fast mode) it eases round to sit behind the boat's direction of
  travel, so sliding the thumb steers and the view turns with it.
- iPhone: touches on the canvas are cancelled (`touchstart`/`touchmove`/`touchend` preventDefault) to stop the
  double-tap-and-hold text magnifier. Keep that if input code changes.
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
