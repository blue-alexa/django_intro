from datetime import date

from django import forms

import bcrypt

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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