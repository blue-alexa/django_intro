
import bcrypt
from django.shortcuts import render, redirect, reverse

from .models import User
from .forms import RegistForm, LoginForm



def register_or_login(request):
    if request.method == "GET":
        rform = RegistForm()
        lform = LoginForm()

        return render(request, 'register_and_login_app/main_page.html', {'rform': rform, 'lform':lform})

    if request.method == "POST":
        rform = RegistForm()
        lform = LoginForm()

        if 'register' in request.POST:
            rform = RegistForm(request.POST)
            if rform.is_valid():
                user = User(first_name=rform.cleaned_data['first_name'],
                            last_name=rform.cleaned_data['last_name'],
                            email=rform.cleaned_data['email'],
                            password= bcrypt.hashpw(rform.cleaned_data['password'].encode(), bcrypt.gensalt())
                            )
                user.save()

                request.session['login'] = True
                request.session['first_name'] = user.first_name
                request.session['userId'] = user.id

                return redirect(reverse('books_main_page'))

        if 'login' in request.POST:
            lform = LoginForm(request.POST)
            if lform.is_valid():
                request.session['login'] = True

                user = User.objects.get(email=lform.cleaned_data['email'])
                request.session['first_name'] = user.first_name
                request.session['userId'] = user.id

                return redirect(reverse('books_main_page'))

        return render(request, 'register_and_login_app/main_page.html', {'rform': rform, 'lform':lform})

def logout(request):
    del request.session['login']
    del request.session['first_name']
    del request.session['userId']
    return redirect(reverse('main_page'))
