from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('Recipes/', views.recipes_view, name='Recipes'),
    path('category/<str:category>/', views.category_recipes, name='category_recipes'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('submit/', views.submit_recipe, name='submit_recipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)