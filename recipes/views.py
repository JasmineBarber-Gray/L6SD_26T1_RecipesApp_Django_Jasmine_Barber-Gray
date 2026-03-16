from django.shortcuts import redirect, render
from .models import Recipe
from django.shortcuts import render, get_object_or_404

def home_view(request):
    return render(request, 'recipes/home.html')


def about_view(request):
    return render(request, 'recipes/about.html')


def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

# Category page
def category_recipes(request, category):
    recipes = Recipe.objects.filter(category=category)
    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "category": category
    })

# Recipe detail page
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "recipes/recipe_detail.html", {
        "recipe": recipe
    })