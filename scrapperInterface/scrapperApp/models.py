from django.db import models

class Request(models.Model):
    url = models.URLField()
    status = models.CharField(max_length=20, default='waiting')
    timestamp = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True)


