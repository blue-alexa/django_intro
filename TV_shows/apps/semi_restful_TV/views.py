from datetime import datetime
from django.shortcuts import render, redirect, reverse
from .models import Show, Network
from .forms import NewShowForm, ShowForm

def root(request):
    return redirect(reverse('show_index'))

def index(request):
    all_shows = Show.objects.all()
    context = {
        "all_shows": all_shows
    }
    return render(request, 'semi_restful_TV/index.html', context)

def add_show(request):
    if request.method == "GET":
        form = NewShowForm()
        return render(request, 'semi_restful_TV/add_show.html', {'form': form})

def save_show(request):
    if request.method == "POST":
        title = request.POST['title']
        network_name = request.POST['network']
        release_date_str = request.POST['release_date']
        # convert to datetime object
        release_date = datetime.strptime(release_date_str, '%m/%d/%Y')
        desc = request.POST['desc']

        # add network to database if not exists
        if not Network.objects.filter(name=network_name).exists():
            Network.objects.create(name=network_name)

        # add show to database
        network = Network.objects.get(name=network_name)
        new = Show.objects.create(title=title, curr_network=network, release_date=release_date, desc=desc)
        new.save()

        return redirect(reverse('display_show', kwargs={'id': new.id}))

def display_show(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)

        context = {
            "show": show
        }
        return render(request, 'semi_restful_TV/show_detail.html', context)

def edit_show(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)

        form = NewShowForm({'title':show.title,
                            'network':show.curr_network.name,
                            'release_date':show.release_date.strftime('%m/%d/%Y'),
                            'desc':show.desc
                            })

        return render(request, 'semi_restful_TV/edit_show.html', {'form':form, 'show_id':id})

def update_show(request, id):
    if request.method == "POST":
        title = request.POST['title']
        network_name = request.POST['network']
        release_date_str = request.POST['release_date']
        # convert to datetime object
        release_date = datetime.strptime(release_date_str, '%m/%d/%Y')
        desc = request.POST['desc']

        show = Show.objects.get(id=id)
        show.title = title
        # add network to database if not exists
        if not Network.objects.filter(name=network_name).exists():
            Network.objects.create(name=network_name)

        # add show to database
        network = Network.objects.get(name=network_name)
        show.curr_network = network
        show.release_date = release_date
        show.desc = desc
        show.save()

        return  redirect(reverse('display_show', kwargs={'id': show.id}))

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect(reverse('show_index'))