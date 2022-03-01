from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist_user")