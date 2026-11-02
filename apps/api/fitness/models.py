import uuid

from django.conf import settings
from django.db import models


class Activity(models.Model):
    class ActivityType(models.TextChoices):
        WALK = "walk", "Walk"
        RUN = "run", "Run"
        GYM = "gym", "Gym"
        SPORT = "sport", "Sport"
        OTHER = "other", "Other"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="activities"
    )
    performed_at = models.DateTimeField()
    activity_type = models.CharField(max_length=16, choices=ActivityType.choices)
    duration_min = models.PositiveIntegerField()
    calories_burned = models.FloatField()
    note = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.activity_type}:{self.duration_min}m"
