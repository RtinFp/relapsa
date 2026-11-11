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

## Screen map (current)

| Screen | Route | Status | UC |
|--------|-------|--------|----|
| Login / Register | `app/(auth)/login.tsx`, `register.tsx` | Connected | UC1 |
| Home | `app/(tabs)/index.tsx` | Calls `/auth/me/` | hub |
| Meals | `app/(tabs)/meals.tsx` | Placeholder | UC3 |
| Activities | `app/(tabs)/activities.tsx` | Placeholder | UC4 |
| Progress | `app/(tabs)/progress.tsx` | Placeholder | UC5 |
| Profile | `app/(tabs)/profile.tsx` | Placeholder | UC2 |

Auth gate → login/register → tabs. There is **no** profile-completion / onboarding gate in the current tree. JWT in SecureStore (web: localStorage).

## What’s in lesson 1

- Auth gate → login/register → tabs
- Tokens in SecureStore (web: localStorage)
- Home calls `GET /auth/me/`

Later lessons: profile forms, meals, activities, progress charts.

Class docs: [docs/02-use-cases.md](../../docs/02-use-cases.md) · [docs/03-activity-diagrams.md](../../docs/03-activity-diagrams.md)
