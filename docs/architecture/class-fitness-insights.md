# Class 5 — Fitness & insights

Maps to Django apps `fitness` + `insights`.

```mermaid
classDiagram
  direction TB

  class User {
    +UUID id
  }

  class Activity {
    +UUID id
    +datetime performedAt
    +string activityType
    +int durationMin
    +float caloriesBurned
    +string note
  }

  class ProgressReport {
    +UUID id
    +date periodStart
    +date periodEnd
    +float bmiSnapshot
    +calorieBalance() float
  }

  class SuggestionService {
    +buildHints(userId) List~string~
  }

  User "1" --> "*" Activity
  User "1" --> "*" ProgressReport
  SuggestionService ..> Activity
  SuggestionService ..> ProgressReport
  SuggestionService ..> User
```

## activityType values

`walk` · `run` · `gym` · `sport` · `other`

`SuggestionService` is application logic (not necessarily a DB table).
