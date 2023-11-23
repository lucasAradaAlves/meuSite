from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    nomeFilme = models.CharField(max_length=100)
    time  = models.DateTimeField('Data da publicação', null=True, blank=True)
    opiniao = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.nomeFilme
    def get_absolute_url(self):
        return reverse('postDetail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return f"{self.author.username} - {self.pub_date}"