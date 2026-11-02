# Frontend flows (Expo Router)

```mermaid
flowchart TD
  index[app_index] --> authGate{Has_JWT?}
  authGate -->|no| login[auth_login]
  login --> register[auth_register]
  register --> login
  login --> tabs
  authGate -->|yes| profileGate{Profile_complete?}
  profileGate -->|no| onboarding[onboarding_profile]
  onboarding --> tabs
  profileGate -->|yes| tabs[tabs_layout]

  tabs --> home[home]
  tabs --> meals[meals]
  tabs --> activities[activities]
  tabs --> progress[progress]
  tabs --> profile[profile]
```

| Screen | Route (Expo Router) | UC |
|--------|---------------------|-----|
| Login / Register | `app/(auth)/login.tsx`, `register.tsx` | UC1 |
| Onboarding profile | `app/onboarding/profile.tsx` | UC2 |
| Home | `app/(tabs)/index.tsx` | hub |
| Meals | `app/(tabs)/meals.tsx` | UC3 |
| Activities | `app/(tabs)/activities.tsx` | UC4 |
| Progress | `app/(tabs)/progress.tsx` | UC5 |
| Profile | `app/(tabs)/profile.tsx` | UC2 |

JWT in `expo-secure-store`. API base URL from env (`EXPO_PUBLIC_API_URL`).
