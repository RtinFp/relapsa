from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            "id",
            "performed_at",
            "activity_type",
            "duration_min",
            "calories_burned",
            "note",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
