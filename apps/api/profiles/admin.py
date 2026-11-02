from django.contrib import admin

from .models import Goal, HealthProfile

admin.site.register(HealthProfile)
admin.site.register(Goal)
