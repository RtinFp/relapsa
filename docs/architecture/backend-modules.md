# Backend modules (Django)

```mermaid
flowchart LR
  subgraph api [apps_api]
    accounts[accounts]
    profiles[profiles]
    nutrition[nutrition]
    fitness[fitness]
    insights[insights]
  end
  accounts --> profiles
  profiles --> nutrition
  profiles --> fitness
  nutrition --> insights
  fitness --> insights
```

| App | Responsibility | Models |
|-----|----------------|--------|
| `accounts` | Register, login, JWT, `/auth/me` | User |
| `profiles` | Health profile, goals, BMI | HealthProfile, Goal |
| `nutrition` | Meals & food items | Meal, FoodItem |
| `fitness` | Activity logs | Activity |
| `insights` | Progress report + suggestions | ProgressReport (optional persist) |

Config project package: `config` (settings, urls, wsgi).
