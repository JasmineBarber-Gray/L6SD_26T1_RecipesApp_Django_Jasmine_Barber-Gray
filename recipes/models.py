from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.db.models.signals import pre_save

class Recipe(models.Model):
    
    CATEGORY_CHOICES = [
        ('Breakfast', 'breakfast'),
        ('Lunch', 'lunch'),
        ('Dinner', 'dinner'),
        ('Dessert', 'dessert'),
    ]
    
    SUB_CATEGORY_CHOICES = [
        ('Keto', 'keto'),
        ('Vegan', 'vegan'),
        ('Vegetarian', 'vegetarian'),
        ('Protein', 'protein'),
        ('Calorie Deficit', 'calorie deficit'),
        ('Gluten-Free', 'gluten-free'),
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
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='recipes/images', blank=True, null=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
    
@receiver(post_delete, sender=Recipe)
def delete_recipe_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
                
@receiver(pre_save, sender=Recipe)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return
        
    try:
        old = Recipe.objects.get(pk=instance.pk)
    except Recipe.DoesNotExist:
        return
            
    if old.image and old.image != instance.image:
        if os.path.isfile(old.image.path):
            os.remove(old.image.path)
