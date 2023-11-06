from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.TextField(blank=True)
    username = models.TextField(blank=True)
    icon = models.TextField(blank=True)