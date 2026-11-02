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

## Smoke

```powershell
# register
curl -X POST http://127.0.0.1:8000/api/v1/auth/register/ -H "Content-Type: application/json" -d "{\"email\":\"you@relapsa.test\",\"password\":\"password123\"}"
```

Docs map: `docs/architecture/api-sketch.md`
