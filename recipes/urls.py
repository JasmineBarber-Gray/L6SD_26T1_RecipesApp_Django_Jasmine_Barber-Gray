from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('about/', views.about_view, name='About'),
    path('Recipes/', views.recipes_view, name='Recipes'),
    path('category/<str:category>/', views.category_recipes, name='category_recipes'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]