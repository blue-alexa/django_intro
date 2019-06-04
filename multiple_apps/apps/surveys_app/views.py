from django.shortcuts import render

def index(request):
    return render(request, "surveys_app/index.html")

def new(request):
    return render(request, "surveys_app/new.html")

# Create your views here.
