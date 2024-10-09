from django.contrib import admin

from .models import Plan,Meal,Food
# Register your models here.
admin.site.register(Plan)
admin.site.register(Meal)
admin.site.register(Food)