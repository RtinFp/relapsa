# Activity diagrams

Five flows for UC1–UC5. Mermaid + PNG fallback. Auth is on mobile; UC2–UC5 are API-level for now.

## AD1 / UC1 — Register or log in

**Status:** API and mobile authentication implemented.

```mermaid
flowchart TD
  S([Start]) --> Enter[Enter email and password]
  Enter --> Mode{Register or login?}
  Mode -->|Register| Reg[POST auth/register]
  Reg --> RV{Email and password valid?}
  RV -->|Yes| User[Create User; signal creates profile]
  RV -->|No| Err[Display error; stay on auth screen]
  Mode -->|Login| Login[POST auth/login]
  Login --> LV{Credentials valid?}
  LV -->|Yes| Token[Issue JWT pair]
  LV -->|No| Err
  User --> Token
  Token --> Save[Store tokens in client]
  Save --> Branch{Login branch?}
  Branch -->|Yes| Me[GET auth/me with access token]
  Branch -->|No; use registration user| State[Set user; enter tabs]
  Me --> State
  Save -. Storage failure .-> Err
  Me -. Request failure .-> Err
  State --> OK([End: app tabs])
  Err --> Fail([End: auth incomplete])
```

## Reading notes

Includes real login/registration differences. There is no onboarding/profile gate. A stored refresh token is not automatically exchanged. Network failures on initial auth calls also display an error; the dashed edges highlight failures after tokens may have been issued.

## Sources

- `apps/api/accounts/models.py`
- `apps/api/accounts/serializers.py`
- `apps/api/accounts/views.py`
- `apps/api/accounts/signals.py`
- `apps/api/accounts/apps.py`
- `apps/api/accounts/urls.py`
- `apps/mobile/app/(auth)/login.tsx`
- `apps/mobile/app/(auth)/register.tsx`
- `apps/mobile/lib/auth.tsx`
- `apps/mobile/app/index.tsx`

![AD1](images/activity-01-auth.png)

[Editable SVG](images/activity-01-auth.svg)

## AD2 / UC2 — Manage health profile

**Status:** Profile and Goal APIs implemented; mobile Profile is a placeholder.

```mermaid
flowchart TD
  S([Start]) --> Read[GET profile with JWT]
  Read --> Auth{JWT valid?}
  Auth -->|No| Unauthorized[Reject protected request] --> E([End])
  Auth -->|Yes| Load[Get or create own HealthProfile]
  Load --> Edit[Submit PUT or PATCH metrics]
  Edit --> Validate{Serializer valid?}
  Validate -->|No| Error[Return validation errors] --> E
  Validate -->|Yes| Save[Persist HealthProfile]
  Save --> Metrics{Nonzero weight and positive height?}
  Metrics -->|No| Null[BMI and category are null]
  Metrics -->|Yes| BMI[Calculate rounded BMI]
  BMI --> Cat[Classify BMI category]
  Cat --> Response[Return profile and derived values]
  Null --> Response
  Response --> E
```

## Reading notes

Goals are a separate API (not part of this profile save). `is_complete` checks age/height/weight/gender.

## Sources

- `apps/api/profiles/models.py`
- `apps/api/profiles/serializers.py`
- `apps/api/profiles/views.py`
- `apps/api/profiles/urls.py`
- `apps/mobile/app/(tabs)/profile.tsx`

![AD2](images/activity-02-profile.png)

[Editable SVG](images/activity-02-profile.svg)

## AD3 / UC3 — Log a meal

**Status:** Nested meal API implemented; mobile Meals is a placeholder.

```mermaid
flowchart TD
  S([Start]) --> Request[POST meal with food_items]
  Request --> Auth{JWT valid?}
  Auth -->|No| Reject[Reject request] --> E([End])
  Auth -->|Yes| Validate{Meal and nested items valid?}
  Validate -->|No| Error[Return validation errors] --> E
  Validate -->|Yes| Owner[Assign request.user]
  Owner --> Meal[Create Meal]
  Meal --> More{More food items?}
  More -->|Yes| Item[Create FoodItem linked to Meal]
  Item --> More
  More -->|No| Total[Sum FoodItem.calories]
  Total --> Response[Return saved meal and total_calories] --> E
  Item -. Unexpected DB failure .-> Partial[Partial save possible]
  Partial --> Fail([End: request fails])
```

## Reading notes

API-level flow; the mobile meal form is planned. food_items is required on create but may be empty. Validation completes before creation, yet DB errors after creation can still leave partial data. Portion is metadata, not a multiplier.

## Sources

- `apps/api/nutrition/models.py`
- `apps/api/nutrition/serializers.py`
- `apps/api/nutrition/views.py`
- `apps/api/nutrition/urls.py`
- `apps/mobile/app/(tabs)/meals.tsx`

![AD3](images/activity-03-meal.png)

[Editable SVG](images/activity-03-meal.svg)

## AD4 / UC4 — Log physical activity

**Status:** Activity API implemented; mobile Activities is a placeholder.

```mermaid
flowchart TD
  S([Start]) --> Request[POST manually entered Activity]
  Request --> Auth{JWT valid?}
  Auth -->|No| Reject[Reject protected request] --> E([End])
  Auth -->|Yes| Validate{ActivitySerializer valid?}
  Validate -->|No| Error[Return validation errors] --> E
  Validate -->|Yes| Owner[Assign request.user]
  Owner --> Save[Create Activity]
  Save --> Response[Return saved Activity]
  Response --> E
```

## Reading notes

API-level flow; mobile activity form is planned. Manual calories_burned; there is no automatic estimate. PositiveIntegerField allows 0 duration; FloatField has no declared positivity constraint.

## Sources

- `apps/api/fitness/models.py`
- `apps/api/fitness/serializers.py`
- `apps/api/fitness/views.py`
- `apps/api/fitness/urls.py`
- `apps/mobile/app/(tabs)/activities.tsx`

![AD4](images/activity-04-activity.png)

[Editable SVG](images/activity-04-activity.svg)

## AD5 / UC5 — View progress and suggestions

**Status:** Live summary and hint APIs implemented; mobile Progress/charts are placeholders.

```mermaid
flowchart TD
  S([Start]) --> Request[GET reports/progress with JWT]
  Request --> Auth{JWT valid?}
  Auth -->|No| Reject[Reject request] --> E([End])
  Auth -->|Yes| Load[Load profile and rolling 7-day logs]
  Load --> Sum[Compute live summary metrics]
  Sum --> Windows[Query date-based hint windows]
  Windows --> First{Overweight AND intake > burn + 500?}
  First -->|Yes| Light[Hint: lighter meal]
  First -->|No| Second{Intake positive AND burn zero?}
  Second -->|Yes| Walk[Hint: short walk]
  Second -->|No| Third{No recent activity?}
  Third -->|Yes| Move[Hint: log a session]
  Third -->|No| Keep[Hint: keep logging]
  Light --> BMI{BMI available?}
  Walk --> BMI
  Move --> BMI
  Keep --> BMI
  BMI -->|Yes| Add[Append BMI category hint]
  BMI -->|No| Response[Return summary; no snapshot saved]
  Add --> Response
  Response --> E
```

## Reading notes

API-level flow; mobile charts are planned. Summary window uses timestamps while hint windows use dates; their boundary records can differ. Both windows have only a lower bound, so future records may count. No historical weight/BMI series or saved ProgressReport is produced.

## Sources

- `apps/api/insights/models.py`
- `apps/api/insights/services.py`
- `apps/api/insights/views.py`
- `apps/api/insights/urls.py`
- `apps/api/profiles/models.py`
- `apps/api/nutrition/models.py`
- `apps/api/fitness/models.py`
- `apps/mobile/app/(tabs)/progress.tsx`

![AD5](images/activity-05-progress.png)

[Editable SVG](images/activity-05-progress.svg)

[Use-case specifications](02-use-cases.md) · [SRS](01-SRS.md)
