# Relapsa mobile (Expo)

Expo Router + JWT login/register against `apps/api`.

## Run

1. Start the API (`apps/api`)
2. Then:

```powershell
cd apps/mobile
npm start
```

Web (`w`) or Expo Go. API base: `EXPO_PUBLIC_API_URL` in `.env` (default `http://127.0.0.1:8000/api/v1`).

Android emulator: `http://10.0.2.2:8000/api/v1`.

## Screens

| Screen | Route | Status |
|--------|-------|--------|
| Login / Register | `app/(auth)/login.tsx`, `register.tsx` | Working |
| Home | `app/(tabs)/index.tsx` | Working (`/auth/me/`) |
| Meals | `app/(tabs)/meals.tsx` | Placeholder |
| Activities | `app/(tabs)/activities.tsx` | Placeholder |
| Progress | `app/(tabs)/progress.tsx` | Placeholder |
| Profile | `app/(tabs)/profile.tsx` | Placeholder |

Auth gate → login/register → tabs. Tokens in SecureStore (web: localStorage).

Still todo: profile forms, meals, activities, progress charts.
