from django.shortcuts import render, redirect, reverse
from ..forms import ShowForm
from ..models import Show, Network, input_validate

def page(request, id):
    if request.method == "POST":
        form = ShowForm(request.POST)
        errors = {}
        if form.is_valid():
            input_data = {'id':id,
                          'title': form.cleaned_data['title'],
                          'network': form.cleaned_data['network'],
                          'release_date': form.cleaned_data['release_date'],
                          'desc': form.cleaned_data['desc']}

            errors = input_validate(input_data)

            if len(errors) == 0:
                print("no errors.")
                if Network.objects.filter(name=input_data['network']).exists():
                    network = Network.objects.get(name=input_data['network'])
                else:
                    network = Network(name=input_data['network'])
                    network.save()

                show = Show.objects.get(id=id)
                show.title = input_data['title']
                show.network = network
                show.release_date = input_data['release_date']
                show.desc = input_data['desc']
                show.save()
                return redirect(reverse('display_show', kwargs={'id': show.id}))
            else:
                """
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                """
        print("render with errors")
        return render(request, 'semi_restful_TV_app/edit_show.html',
                      {'form': form, 'errors': errors, 'show_id': id})

    if request.method == "GET":
        return redirect(reverse('edit_show'))