# LIVEHACK — Live Coding Guide for Global AI Community Meetups

## Overview

This guide walks you through presenting **Wheel of Names** as a live-coding demo at a Global AI Community meetup. The goal is to build a working, audience-interactive spinning wheel in ~30 minutes, using VS Code + GitHub Copilot as the centrepiece of the talk.

**What the audience gets:** they scan a QR code from your screen, enter their name, watch it appear live on the wheel, and one of them wins a prize. Full loop, real-time, no server setup on stage.

---

## Narrative arc

> "We are going to build a real-time audience participation app — live, on stage — using GitHub Copilot. You will be able to scan a QR code and add your name to the wheel before I finish writing the code."

Keep returning to this promise throughout the session. The moment the audience scans and their name appears is the money shot.

---

## Before the meetup

| Task | When |
| --- | --- |
| Fork or clone `ma3u/wheel` | Day before |
| Configure Firebase (3 min) — see README | Day before |
| Test `loadtest.py` against your Firebase project | Day before |
| Open VS Code in fullscreen on the projector | 15 min before |
| Have `index.html` open on one half, browser on the other | 15 min before |
| Display `https://ma3u.github.io/wheel/?join` QR on a phone as backup | 5 min before |

---

## Stage setup

```
│  VS Code (left half)        │  Chrome (right half)        │
│  index.html                 │  https://ma3u.github.io/    │
│  GitHub Copilot Chat open   │  wheel/ (presenter view)    │
```

Bump font size to 20 pt in VS Code so the back row can read it.  
Use **Presentation Mode** (`F` key) on the wheel tab when spinning.

---

## Session structure (30 min)

### 0–3 min: Hook

- Open a blank `index.html` (or show the final app first — either works)
- Say: *"By the end of this, everyone in the room can join the wheel from their phone. Let's build it."*
- Show the GitHub repo QR so early arrivals can star it

### 3–8 min: Scaffold with Copilot

Open Copilot Chat and type:

```
Create a single-file HTML app. Dark navy background, purple gradient buttons.
A spinning wheel canvas in the centre. Name list in a sidebar.
```

Let Copilot generate. Narrate what it produces — point out the CSS custom properties, the Canvas 2D API call. Correct anything wrong with a follow-up prompt.

**Teaching point:** *"Copilot knows the Canvas API, the DOM, CSS variables — I'm directing it at a high level."*

### 8–15 min: Wheel logic

Prompt:

```
Add a spin animation with quartic ease-out. Play a tick sound via Web Audio 
each time the highlighted segment changes. Show a winner overlay with confetti.
```

Run it in the browser. Let it fail once — fix it live with Copilot:

```
The tick sound fires on every frame, not on segment change. Fix it.
```

**Teaching point:** *"This is the real workflow — generate, test, iterate. Copilot catches the mechanical part; you catch the logical bug."*

### 15–20 min: QR join flow

Prompt:

```
Add a ?join URL param that shows a mobile join page. 
The attendee types their name and POSTs to Firebase Realtime DB under wheel/pending.
On the presenter side, listen for child_added and show the name in a pending list.
The presenter clicks + Add to move it to the wheel.
```

This is where you pre-wire Firebase. Have your `FB_CFG` values ready in a text file — paste them in when Copilot generates the config placeholder. Switch to the browser and show the `?join` page on your phone.

**Money shot:** Ask three audience members to go to the URL on their phones. Watch names appear on your screen in real time.

### 20–25 min: Deploy

```bash
git add index.html && git commit -m "Live hack wheel" && git push
```

GitHub Pages rebuilds in ~30 s. Open `https://ma3u.github.io/wheel/` on your phone. The app is live on the internet in under a minute.

**Teaching point:** *"Zero servers. Zero infrastructure. One HTML file. GitHub Pages + Firebase as backend."*

### 25–30 min: Spin & prize

- Enter everyone's name from today (or they've already joined via QR)
- Hit `F` → presentation mode
- Build up the moment: *"One person wins a [sticker / book / whatever]"*
- Hit `Enter` or click SPIN
- Audience claps

Leave 5 min for Q&A.

---

## Prompts cheat-sheet

These are battle-tested prompts that produce clean output:

```
Single-file HTML. No build step. All CSS in a <style> block.
Dark navy (#060c1a) background. Inter font from Google Fonts.
Purple/pink gradient (#7c3aed → #ec4899) for primary buttons.
```

```
Canvas wheel: equal segments, each a different colour from a curated palette.
Smooth spin with quartic ease-out, 4–8 full rotations before stopping.
Pointer triangle at the top. Highlight the winning segment.
```

```
Firebase Realtime DB (compat SDK from CDN). 
Path: wheel/pending — child nodes {name, ts}.
Mobile ?join page: text input + submit. 
Presenter side: show pending list, +Add button per name.
```

```
BroadcastChannel('wheel-sync') so two browser tabs stay in sync 
without extra Firebase reads.
```

```
Presentation mode: fullscreen overlay with a larger canvas.
QR code (qrcode.js from CDN) in the corner showing the ?join URL.
Keyboard shortcut F to toggle, Esc to exit.
```

---

## Common audience questions

**"Does it work without Firebase?"**  
Yes — names can be added manually in the sidebar. Firebase just adds the real-time mobile join flow.

**"Can I run it on my own domain?"**  
Fork the repo, enable Pages, update `ghPagesUrl` in the script. Done.

**"What if two people submit the same name?"**  
`nameExists()` does a case-insensitive check against both the wheel and the pending list before writing.

**"Could you add [feature] with Copilot right now?"**  
Pick one: dark/light toggle, confetti colour theming, presenter password. Live-code it. Good closer.

---

## Tips for speakers

- **Narrate your intent, not your keystrokes.** Say "I want the wheel to slow down naturally" before you type the prompt — the audience follows your thinking, not the code.
- **Let Copilot fail once in public.** It makes the session honest and shows the real workflow.
- **Pre-stage a working version in a second browser tab.** If something breaks badly, switch tabs and keep going.
- **Engage the room early.** The QR join moment works best if you get people scanning during the Firebase section, not just at the end.
- **Print the QR.** Tape a paper QR code to the podium so latecomers can join even when the screen is in VS Code.
