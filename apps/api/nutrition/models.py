import uuid

from django.conf import settings
from django.db import models


class Meal(models.Model):
    class MealType(models.TextChoices):
        BREAKFAST = "breakfast", "Breakfast"
        LUNCH = "lunch", "Lunch"
        DINNER = "dinner", "Dinner"
        SNACK = "snack", "Snack"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meals"
    )
    eaten_at = models.DateTimeField()
    meal_type = models.CharField(max_length=16, choices=MealType.choices)
    note = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def total_calories(self):
        return sum(item.calories for item in self.food_items.all())

    def __str__(self) -> str:
        return f"{self.meal_type}@{self.eaten_at}"


class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="food_items")
    name = models.CharField(max_length=120)
    calories = models.FloatField()
    portion = models.FloatField(default=1.0)

    def __str__(self) -> str:
        return self.name
