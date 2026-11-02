import uuid

from django.conf import settings
from django.db import models


class HealthProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="health_profile"
    )
    gender = models.CharField(max_length=32, blank=True, default="")
    age = models.PositiveIntegerField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    ideal_weight_kg = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def bmi(self):
        if not self.height_cm or not self.weight_kg or self.height_cm <= 0:
            return None
        height_m = self.height_cm / 100.0
        return round(self.weight_kg / (height_m**2), 1)

    def bmi_category(self):
        value = self.bmi()
        if value is None:
            return None
        if value < 18.5:
            return "underweight"
        if value < 25:
            return "normal"
        if value < 30:
            return "overweight"
        return "obese"

    @property
    def is_complete(self):
        return bool(self.age and self.height_cm and self.weight_kg and self.gender)

    def __str__(self) -> str:
        return f"Profile<{self.user_id}>"


class Goal(models.Model):
    class GoalType(models.TextChoices):
        LOSE_WEIGHT = "lose_weight", "Lose weight"
        GAIN_WEIGHT = "gain_weight", "Gain weight"
        MAINTAIN = "maintain", "Maintain"
        BUILD_MUSCLE = "build_muscle", "Build muscle"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="goals"
    )
    type = models.CharField(max_length=32, choices=GoalType.choices)
    target_value = models.FloatField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.type}:{self.user_id}"
