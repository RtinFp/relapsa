from django.contrib import admin

from .models import FoodItem, Meal

admin.site.register(Meal)
admin.site.register(FoodItem)
