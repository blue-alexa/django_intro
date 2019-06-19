from django.db import models

from .network_model import Network

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.ForeignKey(Network, related_name='shows')
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Show: %s, released at %s"%(self.title, self.release_date)


"""
# retrieve error from clean()
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
try:
    article.full_clean()
except ValidationError as e:
    non_field_errors = e.message_dict[NON_FIELD_ERRORS]
"""