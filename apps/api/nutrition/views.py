from rest_framework import viewsets

from .models import Meal
from .serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        return (
            Meal.objects.filter(user=self.request.user)
            .prefetch_related("food_items")
            .order_by("-eaten_at")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
