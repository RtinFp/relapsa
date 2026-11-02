# Activity 5 — Progress report + suggestions

```mermaid
flowchart TD
  startNode([Start]) --> auth{Authenticated?}
  auth -->|No| login[Go_to_auth]
  login --> endFail([End])
  auth -->|Yes| open[Open_progress]
  open --> load[Load_profile_meals_activities]
  load --> bmi[Current_BMI]
  bmi --> balance[Calorie_balance_in_vs_out]
  balance --> trend[Weight_or_BMI_trend_if_data]
  trend --> rules{Suggestion_rules}
  rules -->|High_intake| sugN[Suggest_lighter_meals]
  rules -->|Low_activity| sugA[Suggest_more_movement]
  rules -->|On_track| sugOk[Encourage_consistency]
  sugN --> show[GET_reports_progress_response]
  sugA --> show
  sugOk --> show
  show --> endOk([End])
```

## Suggestion rules (MVP, rule-based)

- If today’s intake ≫ recent burn → nutrition hint.
- If no activity in N days → fitness hint.
- Else → stay-on-protocol message (Relapsa tone).
