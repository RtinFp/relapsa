# Use cases

Actor: **User** (authenticated after register/login).

```mermaid
flowchart LR
  user((User))

  user --> UC1[Register_or_Login]
  user --> UC2[Manage_Health_Profile]
  user --> UC3[Log_Meal]
  user --> UC4[Log_Activity]
  user --> UC5[View_Progress_Report]
  user --> UC6[View_Diet_Suggestions]
  user --> UC7[View_Workout_Suggestions]
```

## Mapping to FRs

| Use case | FR |
|----------|-----|
| Register / Login | FR1 |
| Manage Health Profile | FR2 |
| Log Meal | FR3 |
| Log Activity | FR4 |
| View Progress / Suggestions | FR5 |
