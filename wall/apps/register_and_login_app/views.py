from datetime import date
import bcrypt
from django.shortcuts import render, redirect, reverse
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import PermissionDenied

from .models import User

def check_min_length(value):
    if len(value) < 2:
        raise ValidationError(
            _('Must be at least 2 characters.'),
            code='InvalidLen',
        )


def check_letter_only(value):
    if not value.isalpha():
        raise ValidationError(
            _('Must be at letters only.'),
            code="InvalidChar",
        )

def check_older_than_13yr(value):
    y, m, d = value.year, value.month, value.day
    if date(y+13, m, d) > date.today():
        raise ValidationError(
            _('User must be at least 13 years old.'),
            code="InvalidDate",
        )

def check_password(value):
    if len(value) < 8:
        raise ValidationError(
            _('Password must be at least 8 characters'),
            code="InvalidLen",
        )


class RegistForm(forms.Form):
    first_name = forms.CharField(max_length=255,
                                 validators=[check_min_length, check_letter_only],
                                 error_messages={'InvalidLen':'Must be at least 2 characters.',
                                                 'InvalidChar': 'Must be at letters only.'})
    last_name = forms.CharField(max_length=255,
                                validators=[check_min_length, check_letter_only],
                                error_messages={'InvalidLen': 'Must be at least 2 characters.',
                                                'InvalidChar': 'Must be at letters only.'}
                                )
    email = forms.EmailField()
    birthday = forms.DateField(
        widget=forms.DateInput(format=('%m/%d/%Y'),
                               attrs={'placeholder': 'MM/DD/YYYY'}),
        validators=[check_older_than_13yr],
        error_messages={'InvalidDate': 'User must be at least 13 years old.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={'InvalidLen': 'Must be at least 8 characters.'},
    )
    conf_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password"
    )

    def clean(self):
        super().clean()
        errors = {}
        # check retype password is the same as password
        password = self.cleaned_data['password']
        conf_password = self.cleaned_data['conf_password']
        if conf_password != password:
            errors['conf_password'] = [ValidationError(_('Please enter the same password'),code="Invalid")]

        # check if email is unique
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            errors['email'] = [ValidationError(_('Email already exists.'),code="Invalid")]

        if errors:
            raise ValidationError(
                errors
            )

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean(self):
        super().clean()
        errors = {}

        try:
            user = User.objects.filter(email=self.data['email'])[0]
            if not bcrypt.checkpw(self.cleaned_data['password'].encode(), user.password.encode()):
                errors['password'] = [ValidationError(_('Invalid password.'), code="Invalid")]
        except IndexError:
            errors['email'] = [ValidationError(_('Email does not exist.'), code="Invalid")]

        if errors:
            raise ValidationError(
                errors
            )


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
                            birthday=rform.cleaned_data['birthday'],
                            password= bcrypt.hashpw(rform.cleaned_data['password'].encode(), bcrypt.gensalt())
                            )
                user.save()

                request.session['login'] = True
                request.session['first_name'] = user.first_name
                request.session['userId'] = user.id

                return redirect(reverse('main_message_page'))

        if 'login' in request.POST:
            lform = LoginForm(request.POST)
            if lform.is_valid():
                request.session['login'] = True

                user = User.objects.get(email=lform.cleaned_data['email'])
                request.session['first_name'] = user.first_name
                request.session['userId'] = user.id

                return redirect(reverse('main_message_page'))

        return render(request, 'register_and_login_app/main_page.html', {'rform': rform, 'lform':lform})

def logout(request):
    del request.session['login']
    del request.session['first_name']
    del request.session['userId']
    return redirect(reverse('main_page'))
