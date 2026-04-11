# LIVEHACK — Live Coding Guide for Global AI Community Meetups

## Overview

This guide walks you through presenting **Wheel of Names** as a live-coding demo at a [Global AI Community](https://globalai.community/) meetup. The goal is to build a working, audience-interactive spinning wheel in ~30 minutes, using [VS Code](https://code.visualstudio.com/) + [GitHub Copilot](https://github.com/features/copilot) as the centrepiece of the talk.

**What the audience gets:** they scan a QR code from your screen, enter their name, watch it appear live on the wheel, and one of them wins a prize. Full loop, real-time, no server setup on stage.

---

## Sponsor

[![Sopra Steria](https://www.soprasteria.de/favicon.ico)](https://www.soprasteria.de/en/)

This event is proudly sponsored by **[Sopra Steria Germany](https://www.soprasteria.de/en/)** — one of Europe's leading digital transformation partners, with deep expertise in AI, cloud, and IT consulting.

Sopra Steria helps organisations across financial services, public sector, and industry navigate complex technology change. They are active supporters of the developer community in Germany.

---

## Prerequisites — set up your machine

Complete these steps **before** the meetup. Estimated time: ~20 minutes.

### 1. Create a GitHub account

1. Go to [github.com/signup](https://github.com/signup)
2. Enter your email, create a password, and choose a username
3. Verify your email address
4. On the plan page choose **Free**

> Already have an account? Skip to step 2.

### 2. Install Git

| OS | Steps |
| --- | --- |
| **macOS** | Install [Xcode Command Line Tools](https://developer.apple.com/xcode/resources/): run `xcode-select --install` in Terminal, or install [Git for Mac](https://git-scm.com/download/mac) |
| **Windows** | Download and run [Git for Windows](https://git-scm.com/download/win) — keep all defaults |
| **Linux** | `sudo apt install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora) |

Verify: `git --version` should print a version number.

### 3. Install VS Code

Download and install [Visual Studio Code](https://code.visualstudio.com/download) for your OS.  
Launch it once to confirm it starts correctly.

### 4. Set up an AI coding assistant

#### Recommended: GitHub Copilot (built into VS Code)

[GitHub Copilot is built into VS Code](https://code.visualstudio.com/docs/copilot/setup) — no extension install needed.

1. Open VS Code
2. Click the **Accounts** icon in the bottom-left Activity Bar
3. Choose **Sign in with GitHub to use GitHub Copilot**
4. Complete the browser OAuth flow and return to VS Code

**Which plan?**

| Plan | Price | What you get | Good for this hackathon? |
| --- | --- | --- | --- |
| [**Free**](https://github.com/features/copilot#pricing) | $0 | 2 000 completions + 50 chat messages/month | ✅ Yes — plenty for a 30-min demo |
| [**Pro**](https://github.com/features/copilot#pricing) | $10/month | Unlimited completions & chat, Claude Sonnet/GPT-4o | ✅ Yes — best experience |
| [**Pro+**](https://github.com/features/copilot#pricing) | $39/month | All models including o3 & Claude Opus | Overkill for this demo |

> **Recommendation:** The **Free** tier is enough for the hackathon. If you already have **Pro** or a [student/teacher benefit](https://education.github.com/benefits), use that.

#### Alternatives if you prefer a different tool

| Tool | Notes |
| --- | --- |
| [**Cursor**](https://www.cursor.com/) | AI-first fork of VS Code; free hobby tier available |
| [**Windsurf**](https://windsurf.com/) | VS Code-based; free tier with Codeium models |
| [**Amazon Q Developer**](https://aws.amazon.com/q/developer/) | Free tier for individuals; install as a VS Code extension |
| [**Codeium**](https://codeium.com/) | Free, installs as a VS Code extension |
| [**Tabnine**](https://www.tabnine.com/) | Free basic tier; VS Code extension |

All of these work with the prompts in this guide — just open the chat/assistant panel instead of Copilot Chat.

### 5. Install Node.js (optional — for local preview)

Download [Node.js LTS](https://nodejs.org/en/download) if you want to run a local dev server.  
For this demo a direct browser open of `index.html` is sufficient.

### 6. Configure Git identity

Run these two commands in your terminal (replace with your own details):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 7. Create and clone your repo

1. Go to [github.com/new](https://github.com/new)
2. Name it `wheel`, set visibility to **Public**, tick **Add a README file**, click **Create repository**
3. Click the green **Code** button → copy the HTTPS URL
4. In your terminal: `git clone <paste-url-here>`
5. Open the cloned folder in VS Code: `code wheel`

### 8. Enable GitHub Pages

1. In your repo on GitHub go to **Settings → Pages**
2. Under *Source* select **Deploy from a branch**, choose `main` and `/ (root)`, click **Save**
3. Your future app will be live at `https://<your-username>.github.io/wheel/`

---

## Narrative arc

> "We are going to build a real-time audience participation app — live, on stage — using GitHub Copilot. You will be able to scan a QR code and add your name to the wheel before I finish writing the code."

Keep returning to this promise throughout the session. The moment the audience scans and their name appears is the money shot.

---

## Before the meetup

| Task | When |
| --- | --- |
| Create a **[new empty GitHub repo](https://github.com/new)** (e.g. `wheel`) and clone it locally | Day before |
| [Enable GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) on the repo (Settings → Pages → Deploy from `main` / `docs` or root) | Day before |
| [Configure Firebase](https://console.firebase.google.com/) (3 min) — see README | Day before |
| Test `loadtest.py` against your Firebase project | Day before |
| Open [VS Code](https://code.visualstudio.com/) in fullscreen on the projector | 15 min before |
| Have a **blank** `index.html` open on one half, browser on the other | 15 min before |

> **Important:** Start from your own clean repo — do **not** clone or fork [`ma3u/wheel`](https://github.com/ma3u/wheel). The whole point of the demo is that you build it live from scratch with [Copilot](https://github.com/features/copilot).

---

## Stage setup

```
│  VS Code (left half)        │  Chrome (right half)        │
│  index.html                 │  https://ma3u.github.io/    │
│  GitHub Copilot Chat open   │  wheel/ (presenter view)    │
```


---

## Session structure (30 min)

### 0–3 min: Hook

- Please install all prerequisites on your computer before the session starts — we will be building on top of that.

### 3–8 min: Scaffold with Copilot

Open in Visual Studio Code [Copilot Chat](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide) and type:


### 1. Explain What You Want To Build
```
In our last Global AI Community event. Zaid gave out Swaggs and Merch and use a wheel of names to pick 5 winners.
He used a shady website with ads and trackers. Not very GDPR comppliant.
So today we're going to build our own wheel of names — live on stage, with GitHub Copilot.
No queue of 50 people inserting their names manually. Instead we will have a QR code that anyone can scan with their mobile to join the 
wheel in real time in parallel. Use the community look and feel from this website:
https://globalai.community/chapters/berlin/events/agentcon-berlin-2026/

Use Github Pages. So create a modern type script app in a single index.html file.
start teh server locally. install everything you need for this locally.
```

```
add this project to git and commit and push to github as new public project in my Github Account 
deploy the app to Github pages
```


### 2. Start the web server locally

```bash
npm install && npm start
```
You should see the QR Code and a working wheel of names.

### 3. QR Code Join Flow 

Create a Firebase Account with your Google Account at [console.firebase.google.com](https://console.firebase.google.com/). Create a new project, then go to **Realtime Database** and create a database in test mode. And copy your API into the chat.

```
Now implement the mobile join flow. When a user submits their name, it should be added to a Firebase Realtime Database.  Create a mobile view after scanning the QR code and input youur name. He can only join once with his name on the computer. So check if the name already exists in the wheel or in the pending list before adding it to Firebase. 

Never store secrets in the Github repo.

When the presenter start the wheel dont use a name, what is chosen before.

The presenter can reset the names and delete the names from the database.
```

<img width="844" height="905" alt="image" src="https://github.com/user-attachments/assets/4b577002-fdd7-419f-bd61-df833c8d3fef" />


Check the local browser to see the real-time updates as you add names from the mobile view.

## Optional

### 4. Sound & confetti
```
create sounds and confetti for the winner!
```

### 5. Presentation Mode
```
Presentation mode: fullscreen overlay with a larger canvas.
QR code in the corner showing the ?join URL.
Use keyboard shortcuts: and show the shortcuts on the screen when the presenter presses "?"

Show in realtime the joined people with emojis and names. add the people on the wheel automatically.
```

### 6. Multi Tenancy
```
Implement multi-tenancy so that multiple events can run their own wheel in the same time. So when you create a new wheel, it generates a unique ID and the QR code points to that ID. The Firebase data structure should support multiple wheels with their own set of names.
```

---

## Work at Sopra Steria Germany

Thank you for building this demo with me! If you enjoyed this session and are interested in building things like this for a living? **[Sopra Steria Germany](https://www.soprasteria.de/en/)** is hiring across technology, AI, and consulting roles. Browse all open positions at **[careers.soprasteria.de](https://careers.soprasteria.de/)**.

Here are roles well-suited to the skills shown in this hackathon:

| Role | What you'll do | Locations |
| --- | --- | --- |
| [**AI & Data Consultant**](https://careers.soprasteria.de/) | Design and implement AI/ML solutions for enterprise clients | Hamburg, Berlin, Munich, Frankfurt |
| [**Software Engineer (Full-Stack)**](https://careers.soprasteria.de/) | Build modern web apps and APIs; work in agile teams | Hamburg, Berlin, Düsseldorf |
| [**Cloud Architect**](https://careers.soprasteria.de/) | Design cloud-native architectures on AWS, Azure, or GCP | Hamburg, Munich, Frankfurt |
| [**IT Consultant — Digital Transformation**](https://careers.soprasteria.de/) | Lead end-to-end digital projects for public sector and enterprise clients | Nationwide |
| [**Agile Coach / Scrum Master**](https://careers.soprasteria.de/) | Embed agile ways of working in large organisations | Hamburg, Berlin, Munich |
| [**Cyber Security Consultant**](https://careers.soprasteria.de/) | Advise on security architecture, compliance, and resilience | Hamburg, Berlin, Frankfurt |

> All roles are listed at [careers.soprasteria.de](https://careers.soprasteria.de/). Sopra Steria Germany offers hybrid working, a strong learning culture, and an active tech community.
