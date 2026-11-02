from rest_framework import serializers

from .models import Goal, HealthProfile


class HealthProfileSerializer(serializers.ModelSerializer):
    bmi = serializers.SerializerMethodField()
    bmi_category = serializers.SerializerMethodField()
    is_complete = serializers.BooleanField(read_only=True)

    class Meta:
        model = HealthProfile
        fields = (
            "id",
            "gender",
            "age",
            "height_cm",
            "weight_kg",
            "ideal_weight_kg",
            "bmi",
            "bmi_category",
            "is_complete",
            "updated_at",
        )
        read_only_fields = ("id", "bmi", "bmi_category", "is_complete", "updated_at")

    def get_bmi(self, obj):
        return obj.bmi()

    def get_bmi_category(self, obj):
        return obj.bmi_category()


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ("id", "type", "target_value", "deadline", "created_at")
        read_only_fields = ("id", "created_at")
