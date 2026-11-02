from rest_framework.response import Response
from rest_framework.views import APIView

from .services import build_hints, progress_summary


class ProgressReportView(APIView):
    def get(self, request):
        return Response(progress_summary(request.user))


class SuggestionsView(APIView):
    def get(self, request):
        return Response({"suggestions": build_hints(request.user)})
