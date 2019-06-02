from django.shortcuts import render, redirect
import datetime

def index(request):
    context = {
        "time": datetime.datetime.now().strftime("%b %d, %Y %H:%M %p"),
    }
    return render(request, "time_display_app/index.html", context)

def time_display(request):
    return redirect("/")
# Create your views here.
