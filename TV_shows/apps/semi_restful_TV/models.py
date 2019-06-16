from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return "Network: %s"%(self.name)

class Show(models.Model):
    title = models.CharField(max_length=255)
    curr_network = models.ForeignKey(Network, related_name='curr_shows')
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Show: %s, released at %s"%(self.title, self.release_date)
