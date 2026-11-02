# Class — Domain model

**Status:** draft skeleton for session 3. Align attributes with TFIT research; keep Relapsa original.

```mermaid
classDiagram
  direction TB

  class User {
    +id
    +email
    +passwordHash
    +createdAt
  }

  class HealthProfile {
    +gender
    +age
    +heightCm
    +weightKg
    +goal
    +bmi()
    +bmiCategory()
  }

  class Meal {
    +id
    +eatenAt
    +mealType
    +totalCalories()
  }

  class FoodItem {
    +name
    +calories
    +portion
  }

  class Activity {
    +id
    +performedAt
    +activityType
    +durationMin
    +caloriesBurned
  }

  class Goal {
    +type
    +targetValue
    +deadline
  }

  class ProgressReport {
    +periodStart
    +periodEnd
    +weightTrend()
    +bmiTrend()
    +calorieBalance()
  }

  User "1" --> "1" HealthProfile
  User "1" --> "*" Meal
  User "1" --> "*" Activity
  User "1" --> "*" Goal
  Meal "1" --> "*" FoodItem
  User "1" --> "*" ProgressReport
  HealthProfile --> Goal
```

## Notes

- `bmi()` / `bmiCategory()` are domain operations (see [../requirements/domain.md](../requirements/domain.md)).
- Suggestions can stay as application services later — not required on the class diagram for session 3.
