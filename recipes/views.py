from django.shortcuts import render

def home_view(request):
    return render(request, 'recipes/home.html')


def about_view(request):
    return render(request, 'recipes/about.html')


def recipes_view(request):
    return render(request, 'recipes/recipes.html')


def login_view(request):
    return render(request, 'recipes/login.html')


def signup_view(request):
    return render(request, 'recipes/signup.html')