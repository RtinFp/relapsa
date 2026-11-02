from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GoalViewSet, ProfileView

router = DefaultRouter()
router.register("goals", GoalViewSet, basename="goal")

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("", include(router.urls)),
]
