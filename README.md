# L6SD_26T1_RecipesApp_Django_Jasmine_Barber-Gray
Basic Django website designed to find and share recipes


# Features
- User authentication (login, logout, sign up)
- submit, edit and delete recipes
- search recipes by keywords
- categorise recipes


# Installation
# Clone the repository
git clone https://github.com/L6SD_26T1_RecipesApp_Django_Jasmine_Barber-Gray

# Navigate into the project folder
cd L6SD_26T1_RecipesApp_Django_Jasmine_Barber-Gray

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run the server
python manage.py runserver

# Packages and dependencies
- pip
- Django
- Pillow (for image uploads)
- Python

# how to navigate to admin panel

bash "python manage.py runserver"

open the server link "http://127.0.0.1:8000/"

once web is open add "admin" to the end

then login with the superuser credientials

superuser: Jasmine
superuserpassword: Password01

TestUser: Monica
TestUserPassword: Epicfun26

Testuser#2: Nora
Testuser#2password: TitanFruit09

