from django.shortcuts import render

def register(request):
    return render(request, "users_app/register.html")

def login(request):
    return render(request, "users_app/login.html")

def display_all_users(request):
    return render(request, "users_app/all_users.html")
# Create your views here.
