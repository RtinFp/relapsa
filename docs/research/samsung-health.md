# Samsung Health — research notes

**APK:** `rea/source/Samsung_Health_base.apk` (~354 MB, local only)  
**Method:** selective REA `inspect-android-package` + keyword/URL scan (no full decompile dump).

## Package

| Field | Value |
|-------|--------|
| Package id | `com.sec.android.app.shealth` |
| Version | `7.00.6.011` (code 7006011) |
| minSdk / targetSdk | 29 / 36 |
| Architecture | **Native Android** (huge) — ~66k classes, ~20k resources |
| Store | Play / Samsung (`com.sec.android.app.shealth`) |

## Feature buckets (from component / string signals)

| Bucket | Evidence (examples) | Relapsa? |
|--------|---------------------|----------|
| Steps / walking | Pedometer, WalkingMate, WalkMate widget, step settings | Yes (manual first) |
| Exercise / workout | Workout detection, manage exercise, sport signals | Yes (manual log) |
| Heart rate | HeartRate activities, auto HR / alerts (band/watch) | No (sensors) |
| Sleep | sleepprovider, WatchSettingsSleep, sleep apnea flags | No (semester) |
| Food / nutrition | `food.*`, NutritionPlus, FoodMealMirroring | Yes (core) |
| Weight / body | SWEIGHTSENSOR permission, weight/body composition signals | Yes (profile + trend) |
| Stress / mindfulness | StressSetting, Mindfulness receivers | No |
| Blood / glucose / BP | Blood/glucose keyword hits, BP measure flags | No |
| Wearables / band | BandSettings* (exercise, HR, pedometer targets) | No |
| Sharing / family | HealthSharing (Hs*) activities | No |
| Cloud / AI APIs | samsunghealthai, samsungknowledge, account.samsung.com | No |

## Notable permissions (subset)

- `ACTIVITY_RECOGNITION`, location (fine/coarse)
- Bluetooth (scan/connect) — wearables
- `FOREGROUND_SERVICE_HEALTH` / `_LOCATION`
- Camera, microphone, storage
- Custom: `SWEIGHTSENSOR`, sleep apnea / BP measure flags

## What we take for Relapsa

- **Inspiration:** multi-metric home, meal logging, activity logging, weight/BMI-style progress.
- **Not this semester:** watches/bands, sleep, ECG, glucose, family sharing, Samsung cloud.

## Evidence log

| Date | Command | Result summary |
|------|---------|----------------|
| 2026-11-02 | `rea inspect-android-package Samsung_Health_base.apk` | `com.sec.android.app.shealth` 7.00.6.011; ~66k classes |
| 2026-11-02 | Keyword + URL scan | Food/NutritionPlus, steps, sleep, HR, workouts; Samsung Health APIs |
