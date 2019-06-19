from django.shortcuts import render, redirect, reverse
from ..models import Show

def page(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect(reverse('index'))