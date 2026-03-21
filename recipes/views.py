from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe
from .forms import recipeform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import os

#search imports
from django.db.models import Q

def home_view(request):
    return render(request, 'recipes/home.html')

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

@login_required   
def submit_recipe(request):
    if request.method == 'POST':
        form = recipeform(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = recipeform()
    return render(request, 'recipes/submit_recipe.html', {'form': form})

# Edit recipe view
@login_required
def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    
    if recipe.author != request.user:
        return HttpResponseForbidden("You cannot edit this recipe.")

    if request.method == 'POST':
        form = recipeform(request.POST, request.FILES, instance=recipe)
        
        if form.is_valid():
            new_image = request.FILES.get('image')
            if new_image:
                if recipe.image and os.path.isfile(recipe.image.path):
                    os.remove(recipe.image.path)
                recipe.image = new_image
                    
            form.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = recipeform(instance=recipe)

    return render(request, 'recipes/edit_recipe.html', {'form': form})

# Delete recipe view
@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.author != request.user:
        return HttpResponseForbidden("You cannot delete this recipe.")

    if request.method == 'POST':
        recipe.delete()
        return redirect('Home')

    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})

# Search view
def search_recipes(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(category__icontains=query)
        )

    return render(request, 'recipes/search_results.html', {
        'query': query,
        'results': results
    })
