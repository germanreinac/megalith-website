# Megalith website

A small, playful website for **Megalith**, the comic by Germán Reina and Lizz Lunney.
Visitors tap the sea to push Dji and Skit's boat around a little comic-style ocean,
and catch floating fish that reveal art. The Patreon and newsletter links live
behind the ? button.

## See it

Open `index.html` in a web browser (double-click it). That's all: there is no build step.
It loads its 3D library (Three.js) from the internet, so you need to be online.

## What's where

| Path | What it is |
| --- | --- |
| `index.html` | The whole site for now: layout, water shader, boat, game logic |
| `assets/` | Germán's art goes here. See `assets/README.md` for what goes in each folder |
| `CLAUDE.md` | Notes for Claude when it works on this project |

## Plan

The plan, the checklist of art to send, and open questions live in the
"Megalith Interactive Website – Pitch" doc (Polish plan tab).

## Status

Play test: an open sea you steer across with ripples, fish to catch, a stand-in boat
built from simple shapes after the concept drawing, and comic-style water, outlines and
lettering (Bruno Ace). Next: Germán's water art and boat model, then hosting
(Netlify or Vercel).
