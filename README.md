# Relapsa

Health, nutrition and fitness tracker for a university Software Engineering lab.

Fall off the plan → log it → get back on.

> **Status:** API covers auth, profile, goals, meals, activities and progress. Mobile has working login/register; other tabs are still placeholders.

## Deliverables

| | |
|---|---|
| SRS | [docs/01-SRS.md](docs/01-SRS.md) |
| Use cases | [docs/02-use-cases.md](docs/02-use-cases.md) |
| Activity diagrams | [docs/03-activity-diagrams.md](docs/03-activity-diagrams.md) |
| Class diagram | [docs/04-class-diagram.md](docs/04-class-diagram.md) |
| DB tables | [docs/05-database-tables.md](docs/05-database-tables.md) |

## What works

| Feature | API | Mobile |
|---|---|---|
| Register / login (JWT) | Yes | Yes |
| Health profile + BMI | Yes | Placeholder |
| Goals | Yes (separate CRUD) | Not connected |
| Meals + food items | Yes | Placeholder |
| Activity log | Yes | Placeholder |
| Progress + hints | Yes (live, no saved snapshots) | Placeholder |
| Admin | Django Admin | — |

![System use cases](docs/images/uc-00-system-overview.png)

## Stack

![Architecture](docs/images/architecture-stack.svg)

- Backend: Django 5 + DRF + SimpleJWT
- Mobile: Expo 58 + Expo Router + SecureStore
- DB: SQLite by default; Postgres via `docker compose`
- Apps: accounts, profiles, nutrition, fitness, insights

```text
apps/api/       Django API
apps/mobile/    Expo client
docs/           specs, diagrams, research
```

![ER](docs/images/database-domain.png)

Models: User, HealthProfile, Goal, Meal, FoodItem, Activity, ProgressReport.  
`UserManager` is not a table. Live progress does not write `ProgressReport` rows. Meal totals sum item calories (portion is stored, not multiplied).

## Run

### API

```powershell
cd apps/api
py -3 -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

`http://127.0.0.1:8000` · API prefix `/api/v1/`

### Mobile

```powershell
cd apps/mobile
npm ci
npm run start
```

`EXPO_PUBLIC_API_URL` defaults to `http://127.0.0.1:8000/api/v1` (Android emulator: `http://10.0.2.2:8000/api/v1`).

### Optional Postgres

```bash
docker compose up -d
```

Then set `DATABASE_URL=postgres://relapsa:relapsa@127.0.0.1:5432/relapsa` in `apps/api/.env` and migrate again.

## More docs

[docs/INDEX.md](docs/INDEX.md) · [research](docs/research/) · [sessions](docs/sessions/) · [ADRs](docs/adr/)

## TODO

- [ ] Connect remaining mobile screens
- [ ] Fix portion × calories / validation
- [ ] Client token refresh
- [ ] Tests

Known gaps: no weight-history charts, progress doesn’t compare goals, meal totals ignore portion, reports are live-only (no saved snapshots).
