from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..forms import ShowForm
from ..models import Show, Network, input_validate

def page(request):
    if request.method == "POST":
        form = ShowForm(request.POST)
        errors = {}
        if form.is_valid():
            input_data = {'title': form.cleaned_data['title'],
                          'network': form.cleaned_data['network'],
                          'release_date': form.cleaned_data['release_date'],
                          'desc': form.cleaned_data['desc']}

            errors = input_validate(input_data)

            if len(errors) == 0:
                if Network.objects.filter(name=input_data['network']).exists():
                    network = Network.objects.get(name=input_data['network'])
                else:
                    network = Network(name=input_data['network'])
                    network.save()

                show = Show(title=input_data['title'], network=network, release_date=input_data['release_date'],
                            desc=input_data['desc'])
                show.save()
                return redirect(reverse('display_show', kwargs={'id': show.id}))
            else:
                """
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                """

        return render(request, 'semi_restful_TV_app/create_show.html',
                      {'form': form, 'errors': errors, 'show_id': id})

    if request.method == "GET":
        return redirect(reverse('create_show'))
