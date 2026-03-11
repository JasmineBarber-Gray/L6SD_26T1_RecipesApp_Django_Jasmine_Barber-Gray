from django.shortcuts import render

def home_view(request):
    return render(request, 'recipes/home.html')


def about_view(request):
    return render(request, 'recipes/about.html')


def recipes_view(request):
    return render(request, 'recipes/recipes.html')