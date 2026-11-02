from rest_framework import viewsets

from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user).order_by("-performed_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
