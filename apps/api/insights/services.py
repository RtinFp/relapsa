"""Rule-based suggestions — Relapsa MVP."""

from datetime import timedelta

from django.utils import timezone

from fitness.models import Activity
from nutrition.models import Meal
from profiles.models import HealthProfile


def build_hints(user) -> list[str]:
    hints: list[str] = []
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)

    meals = Meal.objects.filter(user=user, eaten_at__date__gte=week_ago).prefetch_related(
        "food_items"
    )
    intake = sum(m.total_calories() for m in meals)
    burn = sum(
        a.calories_burned
        for a in Activity.objects.filter(user=user, performed_at__date__gte=week_ago)
    )
    recent_activity = Activity.objects.filter(
        user=user, performed_at__date__gte=today - timedelta(days=3)
    ).exists()

    profile = HealthProfile.objects.filter(user=user).first()
    if profile and profile.bmi_category() == "overweight" and intake > burn + 500:
        hints.append("Intake is running ahead of burn — try a lighter meal today.")
    elif intake > 0 and burn == 0:
        hints.append("You logged food but no activity this week — a short walk counts.")
    elif not recent_activity:
        hints.append("No activity in the last 3 days — log a session when you can.")
    else:
        hints.append("Back on protocol — keep logging meals and movement.")

    if profile and profile.bmi() is not None:
        hints.append(f"Current BMI category: {profile.bmi_category()}.")

    return hints


def progress_summary(user) -> dict:
    profile = HealthProfile.objects.filter(user=user).first()
    week_ago = timezone.now() - timedelta(days=7)
    meals = Meal.objects.filter(user=user, eaten_at__gte=week_ago).prefetch_related("food_items")
    activities = Activity.objects.filter(user=user, performed_at__gte=week_ago)
    intake = sum(m.total_calories() for m in meals)
    burn = sum(a.calories_burned for a in activities)
    return {
        "bmi": profile.bmi() if profile else None,
        "bmi_category": profile.bmi_category() if profile else None,
        "period_days": 7,
        "calories_in": intake,
        "calories_out": burn,
        "calorie_balance": intake - burn,
        "meals_count": meals.count(),
        "activities_count": activities.count(),
        "suggestions": build_hints(user),
    }
