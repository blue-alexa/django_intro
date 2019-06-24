from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from . models import Book

def validate_desc_len(value):
    if len(value) < 5:
        raise ValidationError(
            _('Must be at least 5 characters.'),
            code='InvalidLen',
        )

class BookForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    desc = forms.CharField(widget=forms.Textarea(), required=True, validators=[validate_desc_len], label="Description")

    def clean(self):
        super().clean()
        if Book.objects.filter(title=self.cleaned_data['title']).exists():
            raise ValidationError(
                _('Book title alread exists.'),
                code='InvalidLen',
            )

