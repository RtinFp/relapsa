# Relapsa — agent guide

University Software Engineering lab mono-repo. Keep it looking like a student project: few files, clear folders, Mermaid in markdown. No AI-slop scaffolds.

## Weekly lab loop

The professor assigns work **per session** (جلسه / day 01, 02, 03…).

1. Read `docs/Software-Engineering-Lab-Progress.md` — what this week asks for.
2. Put the **submit/present** page in `docs/sessions/NN-….md` (short, links out).
3. Put **canonical** diagrams and specs under `docs/architecture/` or `docs/requirements/` (Mermaid, presentation-ready).
4. Do **not** invent homework the professor did not ask for. Match the count/type they said (e.g. 5 use cases, N activity diagrams).
5. Code in `apps/` only after architecture for that piece exists in `docs/architecture/`.

## Where things live

| Kind | Path |
|------|------|
| Week tracker | `docs/Software-Engineering-Lab-Progress.md` |
| Docs map | `docs/INDEX.md` |
| This week’s hand-in | `docs/sessions/` |
| FR / NFR / domain | `docs/requirements/` |
| Use cases, activities, classes, system, API, DB, UI flows, backend modules | `docs/architecture/` |
| Competitive notes (no APKs, no decompile dumps) | `docs/research/` |
| API | `apps/api/` (Django) |
| Mobile | `apps/mobile/` (Expo) |

## Architecture docs (always Mermaid when it’s a diagram)

- `use-cases.md` — use cases for the product
- `activity-*.md` — one flow per major scenario (or sections the session asks for)
- `class-domain.md` — domain classes → maps to Django models
- `backend-modules.md` — Django apps / modules
- `database.md` — ER / table relations (PostgreSQL)
- `frontend-flows.md` — Expo screens and navigation
- `system.md` — boxes: mobile → API → DB
- `api-sketch.md` — REST resources

When implementing: models follow `class-domain.md` + `database.md`; API modules follow `backend-modules.md`; screens follow `frontend-flows.md`.

## Hard limits

- Product name: **Relapsa**. Stack: Django + DRF, Expo, PostgreSQL.
- Never commit APKs or decompiled source (`rea/source/` is local only).
- Prefer editing existing docs over adding new folders.
- No CONTRIBUTING / CODE_OF_CONDUCT / giant README unless the student asks.
