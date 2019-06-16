from django.forms import ModelForm
from django import forms
from .models import Show

class NewShowForm(forms.Form):
    title = forms.CharField(max_length=255)
    network = forms.CharField(max_length=255)
    release_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    desc = forms.CharField(widget=forms.Textarea, required=False)

class ShowForm(ModelForm):
    release_date = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    class Meta:
        model = Show
        fields = ['title', 'curr_network', 'release_date', 'desc' ]




