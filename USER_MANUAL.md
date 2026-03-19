# User Manual — Wheel of Names

**Live app:** <https://ma3u.github.io/wheel/>

---

## For Attendees (Mobile)

### 1. Scan the QR code

The presenter's screen shows a QR code. Point your phone camera at it — your browser opens automatically.

### 2. Enter your name

Type your first name (or display name) and tap **"Add me to the wheel 🎯"**.

- If your name is already in the wheel or queue you will see a warning and cannot add a duplicate.
- You do not need to install anything.

### 3. Wait for the spin

Once your name is added you will see a confirmation screen. Watch the big screen — the presenter will spin the wheel. Good luck! 🍀

---

## For Presenters

### Opening the app

Go to <https://ma3u.github.io/wheel/> on the presentation laptop.

The sidebar shows three panels:

| Panel | Purpose |
|---|---|
| **Participants** | Manually type or paste names (one per line) |
| **Joined via QR** | Names submitted by attendees — click **+ Add** to move to wheel |
| **Join via Mobile** | Large QR code pointing attendees to the join page |

A status badge in the QR panel shows whether Firebase is active:
- **⚡ Firebase connected** — names appear instantly as attendees join
- **⚠️ Firebase not configured** — fallback mode; share the `?join` URL manually

---

### Adding names manually

Type names in the **Participants** textarea (one per line), then click **✓ Update**.

Use the sidebar buttons to manage the list:

| Button | Action |
|---|---|
| **✓ Update** | Apply textarea changes to the wheel |
| **🔀 Shuffle** | Randomise order |
| **✗ Clear** | Remove all names (asks for confirmation) |

---

### Spinning the wheel

Click **🎯 SPIN THE WHEEL** (or press `Enter`).  
The wheel spins for 4–7 seconds with a tick sound on each segment crossing.  
The winner is shown in a full-screen overlay with confetti.  
Press `Esc` or click **Continue →** to dismiss.

---

### Presentation mode

Click **⛶ Present** in the header (or press `F`) to enter full-screen mode.  
A large wheel fills the screen, with a big SPIN button and a QR code in the corner so the audience can still scan to join.  
Press `Esc` to exit.

---

### Keyboard shortcuts

| Key | Action |
|---|---|
| `Enter` | Spin the wheel |
| `Esc` | Close winner overlay / exit presentation mode |
| `F` | Toggle presentation mode |

---

### Tips for meetups

- Open the app on the **presenter laptop** before the session starts.
- Drag the browser window to the **projected display**, then press `F` to go full-screen.
- Keep the **laptop screen** (not the projector) showing the sidebar so you can manage the queue.
- Pre-fill 2–3 seed names in the textarea so the wheel is never empty when people arrive.
- Use `🔀 Shuffle` right before spinning to avoid predictable ordering.
