from django.shortcuts import render, redirect, reverse
from ..models import Show

def page(request):
    all_shows = Show.objects.all()
    context = {
        "all_shows": all_shows
    }
    return render(request, 'semi_restful_TV_app/index.html', context)