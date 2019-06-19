from __future__ import unicode_literals
from datetime import date
from .show_model import Show
from collections import defaultdict

def input_validate(postData):
    errors = defaultdict(list)
    # add keys and values to errors dictionary for each invalid field
    if len(postData['title']) < 2:
        errors['title'].append('Show title should be at least 2 characters.')

    if len(postData['network']) < 3:
        errors['network'].append('Network name should be at least 3 characters.')

    # check title uniqueness at update
    if 'id' in postData and Show.objects.exclude(id=postData['id']).filter(title=postData['title']).exists():
        errors['title'].append('Show with this Title already exists.')
    # check title uniqueness at creation
    if 'id' not in postData and Show.objects.filter(title=postData['title']).exists():
        errors['title'].append('Show with this Title already exists.')


    if 0 < len(postData['desc']) < 10:
        errors['desc'].append('Description should be at least 10 characters.')

    if postData['release_date'] > date.today():
        errors['release_date'].append('Release date should be in the past.')

    return errors