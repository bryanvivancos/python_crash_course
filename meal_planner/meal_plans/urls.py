from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    #home page
    path('',views.index, name='index'),
    #Plans pages
    path('plans/',views.plans, name='plans'),
    #Detail page for a sigle plan
    path('plans/<int:plan_id>',views.plan,name='plan'),
]