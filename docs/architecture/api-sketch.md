# API sketch

Base: `/api/v1`  
Auth: **Bearer JWT** (SimpleJWT). Register/login are public; the rest require auth.

| Resource | Methods | Auth | Notes |
|----------|---------|------|--------|
| `/auth/register` | POST | Public | `{email,password}` → user + tokens |
| `/auth/login` | POST | Public | `{email,password}` → tokens |
| `/auth/refresh` | POST | Public | `{refresh}` → new access |
| `/auth/me` | GET | JWT | Current user |
| `/profile` | GET, PUT/PATCH | JWT | Health profile (+ computed `bmi`, `bmi_category`) |
| `/goals` | GET, POST | JWT | List/create goals |
| `/goals/{id}` | PATCH, DELETE | JWT | |
| `/meals` | GET, POST | JWT | Nested `food_items` on create |
| `/meals/{id}` | GET, PATCH, DELETE | JWT | |
| `/activities` | GET, POST | JWT | |
| `/activities/{id}` | GET, PATCH, DELETE | JWT | |
| `/reports/progress` | GET | JWT | Summary + trends |
| `/suggestions` | GET | JWT | Rule-based string hints |

## Example token response

```json
{
  "access": "<jwt>",
  "refresh": "<jwt>"
}
```
