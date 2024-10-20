from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    #home page
    path('',views.index,name='index'),
    #Pages that shows all models
    path('pizzas',views.pizzas, name='pizzas'),
    #Detail for a single pizza
    path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
]