from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/", include("profiles.urls")),
    path("api/v1/", include("nutrition.urls")),
    path("api/v1/", include("fitness.urls")),
    path("api/v1/", include("insights.urls")),
]
