from django.shortcuts import redirect, render

# Signup imports
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform

# Login imports
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

#Logout imports
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Home")

    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = signupform(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('Login')
        
    else:
        form = signupform()

    return render(request, "users/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('Home')

