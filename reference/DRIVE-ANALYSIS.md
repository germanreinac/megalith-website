# Analysis of the `megalith` Google Drive folder

Written 15 Nov 2026 from Germán's Drive folder `megalith`. It records what is in the folder,
what the art tells us, and what that means for the website.

## Coverage

- Listed: the top level and the first two levels of subfolders (about 290 files, 12.6 GB).
- Not listed: about 50 deeper folders (per-page folders in `0_Pages`, `Refs/*`, `Patreon/*`,
  `Spanish translation/*`, `Cristian - Pages`, `Character concepts/Main chars` and others).
- Opened: about 20 images, the pitch PDF (20 slides) and the Blender file.
- Could not open: anything over 10 MB (Drive limit). That is most finished pages in
  `0_Pages/Chapter 1/All pages`, every large PSD, and the May 2026 pages PDF.
- Not read on purpose: `Paperwork` (contracts and similar).

## What is in the folder

| Folder | Contents | Use for the site |
| --- | --- | --- |
| `0_Pages` | Chapters 1 to 3 by scene, two early scene tests, covers, in-world ad pages | The finished look; water, panels, lettering |
| `Ships` | Boat concepts (line art, shot studies, explorations), ship reference photos | The boat |
| `3D` | `Skit&Dji_Boat.blend` (blockout) | Already used on the site |
| `Logo` | Logo PNG, PSD and older versions | Already used on the site |
| `Illustrations` | Sailing and mast sketches, sunset, the Patreon panoramic banner with all its stages | World, palette, boat details |
| `Character concepts` | Dji and Skit, Skipjack, Dive Bar Boss, Donnie Voyagio, Magus, Chalky (Skit's dad), Skit's mom, Dji's family, line-up | Crew on deck, cameos |
| `Environment concepts` | Lighthouses, Port Skipjack, Megalith city, Dji and Skit's flat, store | Things to meet at sea |
| `World Map` | Sketch map of the islands | Layout of the sea |
| `Pitch Valencia` | Pitch deck (PDF, PSD, slide images, resources) | Tone and summary |
| `Patreon` | Banner, tier icons, stickers, posts | Rewards for catching fish; links |
| `Refs`, `Sketches` | Moodboards, other artists' references, paper sketches | Taste only |
| `Spanish translation` | Spanish pages | A Spanish version of the site |
| Root files | Brush set-up (PSD, JPG, ABR), watermark PSD, `refs megalith.pur` | Line rule |

## What the art says

**Line**
- One brush, 25 px, constant width. Only opacity changes. Short tick marks sit on surfaces.
- Line colour changes with the scene: purple on concept sheets, warm maroon on characters,
  blue on water, dark teal at night.

**Colour**
- Day: pink sky, lilac clouds, pink and purple buildings, mint to aqua water.
- Dusk: sky runs from blue at the top to salmon pink at the bottom, with flat lilac cloud bars.
- Night: teal and purple with glowing mint light (the Deep Dive bar).
- Seen from far away the sea is very pale, almost white, with pink and mint tints and small dashes.
  Up close it is saturated mint and aqua jelly with blue lines. Storm waves go green and blue.
- Grain is present everywhere, strongest in gradients and shadows.

**Panels and lettering**
- Rounded pink panel borders, circular inset panels, small dashes around the page edge.
- Speech text matches Bruno Ace. Titles on cover tests and the pitch use a wide, heavy sans.

**The boat**
- Tan wood in the finished page (Chapter 1, scene 3, page 7) and in the banner. The purple
  boat in the "Skit y Dji" image is dusk lighting.
- Details in the illustrations that the Blender blockout lacks: a string of small flags
  hanging from the rim, a fish-shaped figure on top of the mast, a barrel look-out,
  the door in the dome, deck planks, the side shelf with its ring.

**The world**
- The setting is the Megalith Islands. The map has a whirlpool in the middle, a tall megalith
  island wearing a ring of cloud, and several smaller islands.
- There are many lighthouse designs (a kettle, a koala, a bird head, a torch on a boat).
- Signs and billboards carry jokes: "Join the adventure with Donnie Voyagio",
  "Check the sea bottom. Dry!", "Wet water".
- Characters beyond the crew: Skipjack (an aubergine carrying a basket of seagulls),
  the Dive Bar Boss, Donnie Voyagio, Magus, Chalky and Skit's mom.

## Ideas this gives the website

1. A whirlpool that sometimes appears, as on the world map.
2. Lighthouses on the horizon as landmarks to sail towards. They are small, self-contained
   and funny, and there are a dozen designs ready.
3. A floating Donnie Voyagio billboard or sign buoys with the in-world jokes.
4. Flags on the boat's rim and the fish figure on the mast.
5. A dusk palette (blue to salmon sky) and a night palette (teal with glow) as extra weather.
6. Seagulls from Skipjack's basket flying past.
7. Patreon stickers and tier icons as the images shown when a fish is caught.
8. Paler water in the distance, to match the banner.

## Open questions for Germán

- The cover tests and banner say "Megalith Islands". The logo says "Megalith". Which is the title?
- Which details should be added to the boat in code, and which will come from Blender?

## To see more

Export flattened copies under 10 MB (for example 2000 px wide JPGs) of:
`0_Pages/Chapter 1/All pages`, `Ships/Megalith_Boats.jpg`, the character line-up,
and `Environment concepts/Concept_Port_Skipjack`. A folder of these would cover
most of what could not be opened.

## Update: large files (15 Nov 2026)

Germán shared the folder by link (https://drive.google.com/drive/folders/1T7NjkzPD1oysEjK3oNw7N5-aWVbk0dpr),
and the environment now allows `drive.google.com` and `drive.usercontent.google.com`.
Large files download with
`curl -L "https://drive.usercontent.google.com/download?id=<file id>&export=download&confirm=t"`.

Downloaded and looked at: all 24 finished Chapter 1 pages (scenes 1 to 4), `Megalith_Boats.jpg`,
`Megalith_Boats_W.jpg`, the 2022 main-characters colour test and the May 2026 pages PDF (64 pages;
only fetched, not yet read page by page).

### How Germán paints water (Chapter 1, scene 1 pages 2 and 3; scene 4 pages 4 and 5)

- One big smooth gradient runs through the whole body of water: green at one end, aqua in the
  middle, blue at the other. The gradient belongs to the water as a whole, not to each blob.
- On top sit flat, lighter blob shapes with no shading of their own. Some are outlined, many are not.
- Lines are nested: a puddle or ripple is two or three contour lines one inside the other,
  each broken in places, with tapering ends.
- Highlights are small, flat, pale pills and dots, not soft glows.
- Calm sea seen from the boat: pale mint base, flat slightly darker mint patches with soft edges,
  thin outlines on only a few of them, small dark-blue dashes.
- Wave crests are thick blobby tongues with a lighter flat face and a heavy outline.
- Grain is strongest inside gradients.

The current shader shades every blob as its own dome. To match the pages it should move the gradient
to the whole sea, make blobs flat and lighter, and draw nested broken contour lines.

### Story facts from Chapter 1

- Skit lives in a flat in the city; Dji works at the Deep Dive bar and gets fired.
- Their goal is the Isle of Distant Shadow (the Cave of Cats), from Donnie Voyagio's travel guide.
- "There's the ferry to Pebble Rock Bay" appears on a sign; the fish follow Skit.
