from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return "Network: %s"%(self.name)