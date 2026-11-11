# Software Requirements Specification — Relapsa

**Course:** Software Engineering lab · **Version:** 2

## 1. Introduction

### 1.1 Purpose
Relapsa helps a person record health measurements, meals and physical activity, then review a small progress summary. This SRS connects the lab requirements to the current implementation.

### 1.2 Scope
MVP: Django REST API + Expo client. Backend supports auth, health profiles, goals, meal/activity logs and rule-based suggestions. Only authentication is wired in the mobile client; other tabs are placeholders.

**Out of scope:** diagnosis, wearables, coaches/live classes, payments, notifications, custom web dashboard. Maintenance is via Django Admin.

### 1.3 Definitions
| Term | Meaning |
|---|---|
| Actor | A person or external system interacting with Relapsa |
| CRUD | Create, read, update and delete |
| JWT | Access/refresh tokens used by the API authentication flow |
| BMI | Weight in kg divided by height in metres squared |
| Goal | A separate record describing a weight/fitness intention |
| Calorie balance | Logged food calories minus logged activity burn; **not** total energy balance |
| Snapshot | A stored report record; the live report endpoint does not currently create one |

### 1.4 References and reading order
[Use cases](02-use-cases.md) → [activities](03-activity-diagrams.md) → [classes](04-class-diagram.md) → [database](05-database-tables.md). The root README is the short presentation. Source references below are paths relative to the repository root.

## 2. Overall description

### 2.1 Product perspective
The mobile client calls `/api/v1/` over HTTP during local development. Django REST Framework handles JSON serialization, permissions and CRUD. SimpleJWT provides authentication. Django ORM uses SQLite by default or PostgreSQL when configured. The seven application models are User, HealthProfile, Goal, Meal, FoodItem, Activity and ProgressReport.

### 2.2 Actors and user classes
| Actor | Responsibilities |
|---|---|
| Visitor | Register or log in |
| Authenticated user | Read/update their profile and manage their own goals, meals and activity; request a progress summary |
| Staff administrator | Maintain registered domain models using Django Admin, subject to staff status and model permissions |

A visitor and authenticated user can be the same person at different stages. The database and JWT library are internal components, not external use-case actors.

### 2.3 Operating environment and interfaces
- Backend: Python, Django 5.x, DRF, SimpleJWT, CORS middleware and python-dotenv.
- Client: Expo 58, React Native, React, TypeScript, Expo Router and SecureStore. Exact client versions remain in `apps/mobile/package.json`.
- Storage: SQLite for the simplest demo; Docker Compose provides optional PostgreSQL.
- External interface: JSON REST routes with trailing slashes; protected routes require an access token.
- Native token storage uses SecureStore; web uses localStorage. The profile API is separate from the goals API.

### 2.4 Constraints and assumptions
- Layout stays `apps/api/` + `apps/mobile/`.
- API must be reachable from the client (a phone cannot use the PC’s `127.0.0.1`).
- Users enter measurements, calories and burn manually — no food catalogue or sensors.
- Schema comes from migrations.

## 3. Functional requirements

| ID | Requirement and acceptance check | Use case | Code evidence | Status |
|---|---|---|---|---|
| FR-1 | The system shall register an account using a unique email and a password of at least 8 characters; return a user and token pair; create an empty profile. Check duplicate email/short password rejection. | UC1 | `apps/api/accounts/serializers.py`, `views.py`, `models.py`, `signals.py` | Backend + mobile auth |
| FR-2 | The system shall authenticate active users, issue access/refresh tokens and expose the current user. Check invalid credentials and a protected request without a token. A refresh endpoint exists; automatic client refresh is not implemented. | UC1 | `apps/api/accounts/urls.py`, `views.py`; `apps/mobile/lib/auth.tsx` | Backend + mobile auth, refresh gap |
| FR-3 | The system shall retrieve/update the current user's health profile and return BMI, category and completeness. Check absent metrics produce null BMI. | UC2 | `apps/api/profiles/models.py`, `serializers.py`, `views.py` | API only |
| FR-4 | The system shall allow users to create/list/read/update/delete their own goals separately from profile updates. Check another user's goal is not accessible. | UC2 related subflow | `apps/api/profiles/models.py`, `views.py`, `urls.py` | API only |
| FR-5 | The system shall manage meals with nested food items and return the sum of item calories. Check replacing an item list and deleting a meal. Portion is stored but not multiplied into totals. | UC3 | `apps/api/nutrition/models.py`, `serializers.py`, `views.py` | API only |
| FR-6 | The system shall manage manual activity records containing time, type, duration and calories burned. Check records are assigned to the authenticated user. | UC4 | `apps/api/fitness/models.py`, `serializers.py`, `views.py` | API only |
| FR-7 | The system shall return a live rolling seven-day summary with current BMI, calorie totals, balance and record counts. Check missing logs give zero totals. It shall not be described as a trend/history feature. | UC5 | `apps/api/insights/services.py:progress_summary`, `views.py` | API only; no snapshot insert |
| FR-8 | The system shall return deterministic rule-based suggestions using profile/log data. Check rule priority and the optional BMI-category hint. | UC5 | `apps/api/insights/services.py:build_hints` | API only |
| FR-9 | Protected domain requests shall operate on the authenticated user's records rather than accepting another owner from the client. Check two users cannot read or mutate each other's logs. | UC2–UC5 | `apps/api/{profiles,nutrition,fitness}/views.py`; `insights/views.py` | Queryset scoping present |
| FR-10 | Staff with appropriate permissions shall maintain all seven domain models through Django Admin. Check ordinary non-staff access is rejected. | Supporting admin case | `apps/api/{accounts,profiles,nutrition,fitness,insights}/admin.py` | Admin registered |

FR-4 is the separate goal API under UC2, not a sixth diagram.

## 4. Non-functional requirements

| ID | Requirement / measurable check | Current evidence or gap |
|---|---|---|
| NFR-1 Security | Hash passwords; require JWT on private APIs; isolate user data. | Hashing/JWT + scoped querysets present |
| NFR-2 Privacy | Keep real health records and local DB files out of the public tree. | Local DB/env ignored |
| NFR-3 Usability | Classmates can find the five deliverables from README. | Flat docs + linked diagrams |
| NFR-4 Reliability | Rejected requests should not leave partial nested meal writes. | No explicit transaction around nested meal create/replace yet |
| NFR-5 Validation | Reject non-positive / nonsense health and calorie values. | Negatives blocked on some ints; several floats still loose |
| NFR-6 Performance | Progress reads stay usable on a local demo DB. | Not benchmarked |
| NFR-7 Maintainability | Clear app boundaries; docs match models/migrations. | Apps + schema docs match source |
| NFR-8 Testability | Automated auth, ownership and summary tests. | Placeholder tests only |

## 5. Data requirements and business rules

- User IDs and all seven project model IDs are UUIDs; inherited authentication fields and permission join tables also exist.
- A user can have zero or one profile at schema level; registration normally creates one. A user can own many goals, meals, activities and report records; a meal can contain zero or many food items.
- Goal choices: lose_weight, gain_weight, maintain, build_muscle. Meal choices: breakfast, lunch, dinner, snack. Activity choices: walk, run, gym, sport, other.
- BMI rounded to one decimal: &lt;18.5 underweight, &lt;25 normal, &lt;30 overweight, else obese. Missing/invalid height or missing/zero weight → null.
- Profile `is_complete` is truthiness of age, height, weight and gender.
- Meal calories = sum of item.calories (portion not multiplied).
- Ownership uses ORM cascade. Schema details: [DB tables](05-database-tables.md).

## 6. Current status and limitations

| Area | Status |
|---|---|
| Mobile | Auth works. Profile / meals / activities / progress tabs are placeholders. |
| Refresh | API refresh exists; client does not auto-refresh. |
| Nutrition | Portion stored but not used in totals; nested meal write has no explicit transaction. |
| Progress | Live summary only — no ProgressReport insert, no goal compare, no weight history. |
| Date windows | Summary uses rolling timestamps; hints use calendar dates; no upper bound. |
| Validation | Some floats/zero values are still loose. |
| Tests | Placeholder tests only. |

## 7. Demo order

1. README + use-case overview
2. UC1 auth (API + mobile)
3. Profile / meal / activity via API client
4. One activity diagram + class/ER (User → Meal → FoodItem)
5. Live progress vs ProgressReport table
6. Limitations / next steps

## 8. Appendix — original lab submission (Persian)

From session 02 homework.

### Functional (as submitted)

1. سیستم باید به کاربران اجازه رجیستر و ورود بدهد.
2. سیستم باید به کاربران اجازه ساخت پروفایل سلامت و مدیریت آن را بدهد.
3. سیستم باید به کاربر اجازه رکورد تغذیه روزانه را بدهد.
4. سیستم باید به کاربر اجازه رکورد فعالیت‌های بدنی را بدهد.
5. سیستم باید گزارشات پیشرفت و پیشنهادهای سلامت ارائه دهد.

### Non-functional (as submitted)

1. سیستم باید از اطلاعات کاربران محافظت کرده و از ورود بدون اعتبارسنجی جلوگیری کند.
2. سیستم باید دارای تجربه کاربری آسان برای استفاده باشد.

### Domain (as submitted)

1. سیستم باید بی‌ام‌آی را با توجه به استانداردهای سلامت محاسبه کرده و طبقه‌بندی کند.

### Notes from that homework

Also mentioned then (not all built): privacy/performance hardening, weight-trend series, goal comparison — see §6.
