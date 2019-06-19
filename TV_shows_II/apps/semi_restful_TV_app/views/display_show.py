from django.shortcuts import render, redirect, reverse
from ..models import Show

def page(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)

        context = {
            "show": show
        }
        return render(request, 'semi_restful_TV_app/show_detail.html', context)