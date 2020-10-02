from django.db import models
from django.conf import settings

class BlogEntry(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=70, blank=False, default='')
    body = models.CharField(max_length=500, blank=False, default='enter blog here')
    datePublished = models.DateTimeField()
