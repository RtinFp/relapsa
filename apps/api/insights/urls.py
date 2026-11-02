from django.urls import path

from .views import ProgressReportView, SuggestionsView

urlpatterns = [
    path("reports/progress/", ProgressReportView.as_view(), name="progress-report"),
    path("suggestions/", SuggestionsView.as_view(), name="suggestions"),
]
