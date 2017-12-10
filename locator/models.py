from django.contrib.auth.models import User
from django.db import models

class Location(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=200)
  time_updated = models.DateTimeField(auto_now=True)
