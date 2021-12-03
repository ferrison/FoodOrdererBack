from django.contrib import admin

from main_app.models import Food, Order, FoodItem

admin.site.register(Food)
admin.site.register(FoodItem)
admin.site.register(Order)
