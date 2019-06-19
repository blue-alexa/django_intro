from django.shortcuts import render
from ..forms import ShowForm
from ..models import Show

def page(request, id):
    if request.method == "GET":
        show = Show.objects.get(id=id)

        form = ShowForm({'title':show.title,
                        'network':show.network.name,
                        'release_date':show.release_date.strftime('%m/%d/%Y'),
                        'desc':show.desc
                        })

        return render(request, 'semi_restful_TV_app/edit_show.html', {'form':form, 'show_id':id})

