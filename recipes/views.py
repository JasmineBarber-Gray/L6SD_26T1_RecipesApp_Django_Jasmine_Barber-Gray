from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe
from .forms import recipeform
from django.contrib.auth.decorators import login_required

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
    
def submit_recipe(request):
    if request.method == 'POST':
        form = recipeform(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user   # 🔥 important
            recipe.save()
            return redirect('Home')
    else:
        form = recipeform()
    return render(request, 'recipes/submit_recipe.html', {'form': form})