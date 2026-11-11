# How to analyze `web.tfit.app`

TFIT’s APK is only a TWA shell. Real product behavior is the website:

**https://web.tfit.app**

Use this for competitive UX / flow notes — still **notes only**, not cloning UI or copying assets into Relapsa.

## Goal

Fill gaps that the APK cannot answer: auth, health profile, meals, workouts, BMI/progress screens.

Write bullets into [../research/tfit.md](../research/tfit.md) and update comparison / activity diagrams.

## Option A — You in the browser (simplest)

1. Open Chrome → `https://web.tfit.app` (and `/launch-screen` if redirected).
2. F12 → **Network** + **Application**.
3. Walk the product like a user: register/login → profile → log food → log activity → progress.
4. For each screen, jot: purpose, main fields, buttons, what API calls fire (path only, no tokens).
5. Screenshot if useful for lab (keep out of git or put under a private folder).

## Option B — Cursor + Chrome DevTools MCP

You already have **Chrome DevTools** / browser MCP in Cursor.

1. Restart Cursor so MCPs are loaded.
2. Ask the agent something like:
   - “Open https://web.tfit.app, snapshot the landing/login UI, list main CTAs.”
   - “After login (I’ll complete login if needed), map the main nav and meal-log screen fields.”
3. Agent uses navigate + snapshot/screenshot; you approve sensitive steps (login).
4. Agent updates `docs/research/tfit.md` with **short bullets**.

Do **not** paste passwords into chat. Prefer you logging in manually when prompted.

## Option C — REA browser tools (optional)

REA also has website observation commands (Chrome family). Same idea as B: observe pages/network, don’t rebuild TFIT.

## What to capture (checklist)

| Area | Questions |
|------|-----------|
| Auth | Email/phone? OTP? Social? |
| Profile | Age, height, weight, gender, goal? |
| Meals | Meal types? Food search? Manual calories? |
| Activity | Catalog vs free text? Duration? |
| Progress | Charts? BMI? Streaks? |
| Language | FA/RTL? |

## Relapsa rule

Observations → our Mermaid in `docs/02`–`05` (use cases / activities / class / DB).
Never copy TFIT branding, copy, or proprietary assets into `apps/`.
