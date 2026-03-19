# Developer Manual — Wheel of Names

## Architecture overview

Everything lives in a **single HTML file** (`index.html`).  
There is no build step, no bundler, no server.  
All dependencies are loaded from CDN at runtime.

```text
index.html
├── <head>
│   ├── Google Fonts (Inter)
│   ├── qrcode@1.5.3 (CDN)          — QR canvas generation
│   ├── firebase-app-compat@10       — Firebase SDK (compat mode)
│   └── firebase-database-compat@10
├── <style>                          — All CSS (CSS custom properties)
├── <body>
│   ├── #joinPage                    — Mobile join view (?join param)
│   ├── #mainApp                     — Presenter view (default)
│   │   ├── .header                  — Logo + Present button
│   │   ├── .wheel-section           — Canvas + SPIN button + QR block
│   │   └── .sidebar                 — Participants / Joined / QR panels
│   ├── #presMode                    — Fullscreen presentation overlay
│   └── #winnerOverlay               — Winner announcement + confetti
└── <script>
    ├── window.FB_CFG                — Firebase config (fill in once)
    └── (async IIFE)                 — All app logic
```

---

## URL routing

The app is fully URL-driven with no framework.

| URL param | Behaviour |
|---|---|
| *(none)* | Presenter mode — full app |
| `?join` | Mobile join page |
| `?add=NAME` | Fallback (no Firebase): adds NAME to presenter pending queue |

Routing logic lives at the top of the IIFE:

```js
const isJoin  = params.has('join');
const addName = params.get('add');
if (isJoin) { /* mobile join flow */ return; }
/* presenter app */
```

---

## Firebase data model

```
wheel/
  names   : string   — newline-separated list of wheel names
  pending/
    <pushKey>:
      name : string
      ts   : number  (Unix ms)
```

### Realtime listeners (presenter side)

```js
fbDb.ref('wheel/names').on('value', snap => { ... });      // sync wheel
fbDb.ref('wheel/pending').on('child_added',   snap => { ... }); // new joiner
fbDb.ref('wheel/pending').on('child_removed', snap => { ... }); // after +Add
```

When the presenter clicks **+ Add**, the name is moved from `wheel/pending/<key>` (deleted) into the `wheel/names` string (updated). All listener instances (other tabs, other devices) receive both changes in real time.

### Mobile join flow (Firebase path)

1. `doJoin()` reads `wheel/names` and `wheel/pending` in parallel
2. Checks for duplicate (case-insensitive)
3. `fbDb.ref('wheel/pending').push({ name, ts })` — triggers `child_added` on all presenter tabs instantly

### Fallback (no Firebase)

If `FB_READY` is false the `?add=NAME` URL param flow is used:
- Mobile submits → shows "You're in the queue" screen (no real push)
- Presenter must open the `?add=NAME` URL manually (e.g. by scanning the attendee's ticket QR)

---

## Multi-instance sync

Two mechanisms run in parallel:

| Mechanism | Scope | Use case |
|---|---|---|
| `BroadcastChannel('wheel-sync')` | Same browser, same origin | Two presenter tabs on one laptop |
| Firebase `on('value')` / `on('child_added')` | Any device, any browser | Laptop + tablet, two organisers |

`broadcast()` is called after every local mutation. Firebase listeners fire for remote changes.

---

## Canvas rendering

Two canvases share a single `drawOn(ctx, canvas)` function:

| Canvas | Size (CSS) | Backing (HiDPI) | Used in |
|---|---|---|---|
| `#wheelCanvas` | 600 × 600 px | 1200 × 1200 | Main view |
| `#presCanvas` | 640 × 640 px | 1280 × 1280 | Presentation overlay |

Font size scales with wheel size and name count:

```js
const fs = Math.max(W/70, Math.min(W/26,
    W * 1.4 / Math.max(names.length, 1) / 9));
```

Long names are truncated with `…` to fit within `R * 0.52` of the radius.

---

## Animation & audio

`spin()` uses `requestAnimationFrame` with quartic ease-out:

```js
const ease = 1 - Math.pow(1 - t, 4);
rotation = start + total * ease;
```

A tick sound is generated via the Web Audio API every time the highlighted segment changes — no audio files required.

---

## CSS architecture

All colours are CSS custom properties on `:root`:

```css
--bg-primary:          #060c1a
--bg-secondary:        #0d1b30
--bg-card:             #0f2040
--accent-purple:       #7c3aed
--accent-purple-light: #a855f7
--accent-orange:       #f59e0b
--grad-brand:          linear-gradient(135deg, #7c3aed, #ec4899)
```

Overriding any of these changes the entire theme.

---

## Adding a new feature — checklist

1. **Read the IIFE** — almost all logic is in the single `(async () => { … })()` block
2. **Avoid adding files** — keep everything in `index.html` so the app stays deployable as a single-page GitHub Pages site with no build step
3. **Firebase writes** — always do the local state update first (for instant feedback), then fire the Firebase write as a side-effect; Firebase listeners will propagate to other tabs
4. **Broadcast** — call `broadcast()` after any mutation so same-browser tabs stay in sync even without Firebase
5. **Duplicate check** — always call `nameExists(name)` before adding to either the wheel or the pending queue

---

## Load testing

`loadtest.py` simulates 100 concurrent mobile joins against the real Firebase REST API.

```bash
# Configure DB_URL at the top of the file, then:
python3 loadtest.py
```

The script:
1. Clears `wheel/pending` and `wheel/names`
2. Pushes 100 names concurrently (10 workers)
3. Reports success/failure counts and final DB state

---

## Deployment

The app is a static file — any HTTP host works.

```bash
# GitHub Pages (already configured)
git add index.html && git commit -m "..." && git push
# Pages rebuilds in ~30s at https://ma3u.github.io/wheel/
```

Firebase security rules for production (replace test-mode open rules):

```json
{
  "rules": {
    "wheel": {
      "names":   { ".read": true, ".write": true },
      "pending": { ".read": true, ".write": true }
    }
  }
}
```

For a public meetup these open rules are fine. For a private event, add `.write` restrictions based on a shared secret or Firebase Auth.
