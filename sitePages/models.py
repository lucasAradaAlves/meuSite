from django.db import models

class post(models.Model):
    nomeFilme = models.CharField(max_length=100)
    time  = models.DateTimeField('date published', null=True, blank=True)
    opiniao = models.CharField(max_length=500)

    def __str__(self):
        return self.nomeFilme