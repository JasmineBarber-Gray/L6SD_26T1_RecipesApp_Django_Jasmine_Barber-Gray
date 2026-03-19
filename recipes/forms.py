from django import forms
from .models import Recipe

class recipeform(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 
            'category', 
            'image', 
            'description', 
            'ingredients',
            'instructions',
            ]