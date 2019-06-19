from django import forms

class ShowForm(forms.Form):
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

