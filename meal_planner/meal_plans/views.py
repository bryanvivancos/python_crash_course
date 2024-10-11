from django.shortcuts import render

from .models import Plan,Meal


# Create your views here.
def index(request):
    """The home page for meal planner"""
    return render(request,'meal_plans/index.html')

def plans(request):
    """The page of the plans"""
    plans = Plan.objects.order_by('date_added')
    context = {'plans': plans}
    return render(request,'meal_plans/plans.html',context)

def plan(request,plan_id):
    """The page of each meal for plan"""
    plan = Plan.objects.get(id=plan_id)
    meal = Meal.objects.get(id=plan_id)
    meals = plan.meal_set.order_by('name')
    foods = meal.food_set.order_by('description')
    context = {'plan':plan,'meals':meals,'foods':foods}
    return render(request,'meal_plans/plan.html',context)