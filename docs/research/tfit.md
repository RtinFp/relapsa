# TFIT — research notes

**Targets:** APK `rea/source/TFIT_base.apk` (local) + live web **https://web.tfit.app**  
**Method:** REA/JADX on APK; logged-in browser walk (Cursor browser) on the web app.

## Package (APK)

| Field | Value |
|-------|--------|
| Package id | `app.tfit.web.twa` |
| Version | `V1.0.4-bazzar` (code 27) |
| Architecture | **Trusted Web Activity** → real product is the website |
| Web app | `https://web.tfit.app` |

## Auth

| Step | Route / UI |
|------|------------|
| Splash | `/splash-video` — CTA «شروع کن» |
| Login | `/login` — mobile `09…`, accept terms, «شروع کن» |
| OTP | `/login/verify-otp` — 6-digit SMS, countdown, confirm |
| Gate | after OTP → `/home` |

Stack signals (from loaded assets): React, MUI, Redux, React Query, Sentry.

## Main navigation (bottom bar)

| Tab (FA) | Route | Role |
|----------|-------|------|
| خانه | `/home` | Marketing home: banners, trainers, sports magazine |
| برنامه روزانه | `/dashboard` | Daily program / progress hub |
| کلاس ورزشی | (sports class) | Live/class style workouts |
| دوره آنلاین | (online course) | Purchased/online courses |
| پروفایل | `/profile` | Account, sport prefs, support, logout |

## Profile & body metrics

### `/profile`
- Display name, subscription tier («اشتراک رایگان»), CTA خرید اشتراک
- Aggregate stats: exercise minutes, kilocalories
- Links: حساب کاربری من · اطلاعات ورزشی من · پشتیبانی · دوره‌های خریداری‌شده · تاریخچه پرداخت · خروج

### `/profile/account` — حساب کاربری
- Username, phone (read-only), optional Google link
- Gender, birth date
- **Current weight**, **height**, **ideal weight**
- Name, address, postal code (shipping / identity)

### `/profile/sport-info` — اطلاعات ورزشی
- Preferred training time, days/week, session duration
- Fitness level, sport interests, place (gym/home…)
- Goals (e.g. build muscle), body status, injuries
- Focus body regions
- Limited edits («تعداد ویرایش مجاز»)

### `/reports/physical-report` — اطلاعات فیزیکی بدن
- Height, gender, age, current / ideal weight
- **BMI** value + categories (underweight / normal / overweight / obese) + coaching copy
- Weight-loss progress expectation toward ideal weight
- Body composition (LBM %, BFP %, fat mass breakdown)
- **BMR** / daily energy need (kcal)
- Summary of sport preferences

## Dashboard `/dashboard` (برنامه روزانه)

- Subscription gate when free trial ends
- Session progress (total / waiting / not done / done)
- Manual log: «چند دقیقه ورزش کردی؟» (minutes slider)
- Charts: minutes + kilocalories (weekly / monthly tabs)
- Body-region focus % (upper / core / back / lower)
- Course progress (e.g. days left in program)
- Link into physical report

## Nutrition

- No clear free-tier **meal diary** in the walk.
- Nutrition appears as **content** (مجله ورزشی articles: food volume, keto, protein timing…) and possibly paid plans — not a full calorie-log product like Relapsa’s FR3.

## Implications for Relapsa

| Take | Skip / differ |
|------|----------------|
| Phone OTP auth pattern (or email) | Don’t clone TFIT branding/UI |
| Health profile: gender, age, height, weight, ideal weight, BMI categories | Subscription / trainers / live classes (out of semester scope) |
| Progress: minutes, kcal charts, body regions | Body composition / BMR can be stretch goals |
| Manual activity minutes | Prefer structured meal + activity logging as core |

Relapsa stays original: Expo + Django; domain from [../architecture/class-domain.md](../architecture/class-domain.md).

## Evidence log

| Date | Source | Result |
|------|--------|--------|
| 2026-11-02 | REA APK inspect | TWA `app.tfit.web.twa` |
| 2026-11-02 | URL scan APK | `web.tfit.app` |
| 2026-11-03 | Browser login + walk | Auth OTP; home; profile; sport-info; account; dashboard; physical-report (BMI/BMR) |
