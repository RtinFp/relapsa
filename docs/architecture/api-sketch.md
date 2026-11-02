# API sketch

**Status:** draft — finalize after class diagram freeze.

Base: `/api/v1`

| Resource | Methods | Notes |
|----------|---------|--------|
| `/auth/register` | POST | Create user |
| `/auth/login` | POST | Issue token |
| `/auth/me` | GET | Current user |
| `/profile` | GET, PUT/PATCH | Health profile |
| `/meals` | GET, POST | List / create meals |
| `/meals/{id}` | GET, PATCH, DELETE | Meal detail |
| `/activities` | GET, POST | List / create activities |
| `/activities/{id}` | GET, PATCH, DELETE | Activity detail |
| `/reports/progress` | GET | Trends + BMI summary |
| `/suggestions` | GET | Nutrition / workout hints |

Auth: JWT (candidate — record ADR when chosen).
