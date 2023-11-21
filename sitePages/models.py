from django.db import models
from django.urls import reverse

class Post(models.Model):
    nomeFilme = models.CharField(max_length=100)
    time  = models.DateTimeField('Data da publicação', null=True, blank=True)
    opiniao = models.CharField(max_length=500)
    def __str__(self):
        return self.nomeFilme
    def get_absolute_url(self):
        return reverse('postDetail', args=[str(self.id)])