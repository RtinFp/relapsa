from rest_framework import generics, viewsets

from .models import Goal, HealthProfile
from .serializers import GoalSerializer, HealthProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = HealthProfileSerializer

    def get_object(self):
        profile, _ = HealthProfile.objects.get_or_create(user=self.request.user)
        return profile


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
