# Activity — Log meal

**Status:** stub — refine after TFIT research.

```mermaid
flowchart TD
  A([Start]) --> B[Open_meal_log]
  B --> C[Select_meal_type]
  C --> D[Add_food_items]
  D --> E[Set_portions]
  E --> F[Compute_meal_calories]
  F --> G[Save_meal]
  G --> H[Update_daily_intake]
  H --> I([End])
```

## Open questions (fill from RE)

- Meal types used in TFIT (breakfast/lunch/…)
- Food catalog vs free-text
- Whether macros are tracked beyond calories
