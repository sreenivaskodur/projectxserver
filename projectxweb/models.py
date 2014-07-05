from django.db import models

class User(models.Model):
    acces_token = models.CharField(max_length = 64)
    source = models.IntegerField()
    name = models.TextField()
