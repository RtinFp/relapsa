# Relapsa — agent guide

University Software Engineering lab mono-repo. Keep it looking like a student project: few files, clear folders, Mermaid in markdown. No AI-slop scaffolds.

## Weekly lab loop

The professor assigns work **per session** (جلسه / day 01, 02, 03…).

1. Read `docs/Software-Engineering-Lab-Progress.md` — what this week asks for.
2. Put the **submit/present** page in `docs/sessions/NN-….md` (short, links out).
3. Keep the **five class deliverables** under `docs/01-SRS.md` … `docs/05-database-tables.md` (plus `docs/images/`). Do not recreate parallel copies under `docs/architecture/` or `docs/requirements/`.
4. Do **not** invent homework the professor did not ask for. Match the count/type they said (e.g. 5 use cases, N activity diagrams).
5. Code in `apps/` only after the matching deliverable/docs exist for that piece.

## Where things live

| Kind | Path |
|------|------|
| Week tracker | `docs/Software-Engineering-Lab-Progress.md` |
| Docs map | `docs/INDEX.md` |
| This week’s hand-in | `docs/sessions/` |
| SRS / FR / NFR | `docs/01-SRS.md` |
| Use cases | `docs/02-use-cases.md` |
| Activity diagrams | `docs/03-activity-diagrams.md` |
| Class diagram | `docs/04-class-diagram.md` |
| Database tables / ER | `docs/05-database-tables.md` |
| Diagram images | `docs/images/` |
| Competitive notes (no APKs, no decompile dumps) | `docs/research/` |
| API | `apps/api/` (Django) |
| Mobile | `apps/mobile/` (Expo) |
| Personal exam sheet (gitignored) | `cheatsheet/relapsa-exam-fa.md` |

## Mapping docs → code

When implementing: models follow `docs/04-class-diagram.md` + `docs/05-database-tables.md`; API routes stay aligned with `apps/api/README.md` and the use-case triggers in `docs/02-use-cases.md`; screens follow `apps/mobile/README.md` and `docs/02` / `docs/03`.

## REA (competitive analysis)

- How it works: [docs/howto/rea-setup.md](docs/howto/rea-setup.md)
- TFIT APK is a **TWA** (`app.tfit.web.twa`) wrapping `https://web.tfit.app` — domain logic is not in the APK. Prefer web observation + store UX for features; keep notes in `docs/research/`.
- Samsung Health APK: selective inspect only (large).

## Stack (frozen)

Django + DRF · PostgreSQL (optional; SQLite default locally) · **SimpleJWT** · Expo + Expo Router. ADRs in `docs/adr/`.

## Cheat sheet rule

File `cheatsheet/relapsa-exam-fa.md` is the student’s Persian final-exam brain dump. It is **gitignored**.

After any meaningful change to architecture docs or `apps/`, **update that cheat sheet in the same turn** (models, JWT, endpoints, screens, “استاد ممکنه بپرسه”). Never commit it.

## Hard limits

- Product name: **Relapsa**.
- Never commit APKs, decompiled source, or `cheatsheet/`.
- Prefer editing the five deliverables over adding new doc folders.
- No CONTRIBUTING / CODE_OF_CONDUCT / giant README unless the student asks.
