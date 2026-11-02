# Frontend flows (Expo)

Screen map for the Relapsa mobile client. Details follow activity diagrams.

```mermaid
flowchart TD
  splash[Splash] --> auth{Logged_in?}
  auth -->|no| login[Login_Register]
  login --> onboarding[Health_profile_onboarding]
  auth -->|yes| gate{Profile_complete?}
  gate -->|no| onboarding
  gate -->|yes| home[Home_dashboard]
  onboarding --> home

  home --> meal[Log_meal]
  home --> activity[Log_activity]
  home --> progress[Progress]
  home --> profile[Profile_goals]

  meal --> home
  activity --> home
  progress --> home
  profile --> home
```

| Screen | Purpose | Related activity doc |
|--------|---------|----------------------|
| Login / Register | FR1 | [activity-auth.md](activity-auth.md) |
| Onboarding profile | FR2, BMI | [activity-auth.md](activity-auth.md) |
| Home | Hub | — |
| Log meal | FR3 | [activity-meal.md](activity-meal.md) |
| Log activity | FR4 | [activity-fitness.md](activity-fitness.md) |
| Progress | FR5 | [activity-progress.md](activity-progress.md) |
| Profile / goals | FR2 | [activity-auth.md](activity-auth.md) |
