from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    
    CATEGORY_CHOICES = [
        ('Breakfast', 'breakfast'),
        ('Lunch', 'lunch'),
        ('Dinner', 'dinner'),
        ('Dessert', 'dessert'),
        ('Keto', 'keto'),
        ('Vegan', 'vegan'),
        ('Valentine\'s Day', 'valentine\'s Day'),
        ('Easter', 'easter'),
        ('Halloween', 'halloween'),
        ('Thanksgiving', 'thanksgiving'),
        ('Christmas', 'christmas'),
        ('New Years', 'new years'),
    ]
        
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='recipe/', blank=True, null=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title