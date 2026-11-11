# Relapsa API

Django + DRF + SimpleJWT.

## Setup

```powershell
cd apps/api
py -3 -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
copy .env.example .env
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

Default DB is **SQLite** (`db.sqlite3`). For Postgres, start Docker Compose from repo root and set `DATABASE_URL` in `.env`.

## API sketch

Base: `/api/v1/` (trailing slashes). Auth: **Bearer JWT** (SimpleJWT). Register/login are public; the rest require auth.

| Resource | Methods | Auth | Notes |
|----------|---------|------|--------|
| `/auth/register/` | POST | Public | `{email,password}` → user + tokens |
| `/auth/login/` | POST | Public | `{email,password}` → tokens |
| `/auth/refresh/` | POST | Public | `{refresh}` → new access |
| `/auth/me/` | GET | JWT | Current user |
| `/profile/` | GET, PUT/PATCH | JWT | Health profile (+ computed `bmi`, `bmi_category`) |
| `/goals/` | GET, POST | JWT | List/create goals (separate from profile) |
| `/goals/{id}/` | PATCH, DELETE | JWT | |
| `/meals/` | GET, POST | JWT | Nested `food_items` on create |
| `/meals/{id}/` | GET, PATCH, DELETE | JWT | |
| `/activities/` | GET, POST | JWT | |
| `/activities/{id}/` | GET, PATCH, DELETE | JWT | |
| `/reports/progress/` | GET | JWT | Live summary (does not save ProgressReport) |
| `/suggestions/` | GET | JWT | Rule-based string hints |

## Smoke

```powershell
# register
curl -X POST http://127.0.0.1:8000/api/v1/auth/register/ -H "Content-Type: application/json" -d "{\"email\":\"you@relapsa.test\",\"password\":\"password123\"}"
```

Class docs: [docs/01-SRS.md](../../docs/01-SRS.md) · [docs/02-use-cases.md](../../docs/02-use-cases.md) · [docs/05-database-tables.md](../../docs/05-database-tables.md)
