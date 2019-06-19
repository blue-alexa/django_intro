from django.shortcuts import render
from ..forms import ShowForm

def page(request):
    if request.method == "GET":
        form = ShowForm()
        return render(request, 'semi_restful_TV_app/create_show.html', {'form': form})