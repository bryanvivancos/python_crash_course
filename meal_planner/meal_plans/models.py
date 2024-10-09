from django.db import models

# Create your models here.
class Plan(models.Model):
    """A plan the user can choose"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    
class Meal(models.Model):
    """Meal dependending the Plan"""
    meal = models.ForeignKey(Plan, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    
class Food(models.Model):
    """Food inside each meal"""
    food = models.ForeignKey(Meal,on_delete=models.CASCADE)
    description = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.description[:50]}..."