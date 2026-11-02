import uuid

from django.conf import settings
from django.db import models


class ProgressReport(models.Model):
    """Optional persisted snapshot; progress endpoint can also compute live."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress_reports"
    )
    period_start = models.DateField()
    period_end = models.DateField()
    bmi_snapshot = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Report<{self.period_start}:{self.period_end}>"
