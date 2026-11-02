from rest_framework import serializers

from .models import FoodItem, Meal


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("id", "name", "calories", "portion")
        read_only_fields = ("id",)


class MealSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True)
    total_calories = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = (
            "id",
            "eaten_at",
            "meal_type",
            "note",
            "food_items",
            "total_calories",
            "created_at",
        )
        read_only_fields = ("id", "total_calories", "created_at")

    def get_total_calories(self, obj):
        return obj.total_calories()

    def create(self, validated_data):
        items = validated_data.pop("food_items", [])
        meal = Meal.objects.create(**validated_data)
        for item in items:
            FoodItem.objects.create(meal=meal, **item)
        return meal

    def update(self, instance, validated_data):
        items = validated_data.pop("food_items", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if items is not None:
            instance.food_items.all().delete()
            for item in items:
                FoodItem.objects.create(meal=instance, **item)
        return instance
