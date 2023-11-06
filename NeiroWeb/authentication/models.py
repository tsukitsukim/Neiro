from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField(blank=True)
    username = models.TextField(blank=True)