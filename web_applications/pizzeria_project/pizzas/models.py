from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A model called Pizza"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
    
class Topping(models.Model):
    """A model called Topping with a fields called pizza that should be a foreign key to Pizza"""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.name