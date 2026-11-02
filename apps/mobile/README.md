# Relapsa mobile (Expo)

Lesson 1: Expo Router skeleton + JWT login/register talking to `apps/api`.

## Run

1. Start API: `cd apps/api` → `.\.venv\Scripts\python manage.py runserver`
2. Here:

```powershell
cd apps/mobile
npm start
```

Open web (`w`) or Expo Go. API base: `EXPO_PUBLIC_API_URL` in `.env` (default `http://127.0.0.1:8000/api/v1`).

Android emulator: use `http://10.0.2.2:8000/api/v1`.

## What’s in lesson 1

- Auth gate → login/register → tabs
- Tokens in SecureStore (web: localStorage)
- Home calls `GET /auth/me/`

Later lessons: onboarding BMI, meals, activities, progress charts.
