# Activity 2 — Manage health profile + BMI

```mermaid
flowchart TD
  startNode([Start]) --> auth{Authenticated?}
  auth -->|No| login[Go_to_auth]
  login --> endFail([End])
  auth -->|Yes| open[Open_health_profile]
  open --> edit[Enter_gender_age_height_weight]
  edit --> goal[Set_goal_type_and_target]
  goal --> save[PUT_or_PATCH_profile]
  save --> bmi[Compute_BMI]
  bmi --> cat[Classify_BMI_category]
  cat --> show[Show_BMI_and_category]
  show --> endOk([End])
```

## BMI categories (adult WHO-style)

| Category | BMI |
|----------|-----|
| Underweight | &lt; 18.5 |
| Normal | 18.5 – 24.9 |
| Overweight | 25 – 29.9 |
| Obese | ≥ 30 |

`BMI = weight_kg / (height_m ^ 2)`.
