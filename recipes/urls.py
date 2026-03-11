from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='Home'),
    path('about/', views.about_view, name='About'),
    path('Recipes/', views.recipes_view, name='Recipes'),
    path('login/', views.login_view, name='Login'),
    path('signup/', views.signup_view, name='Signup')
]