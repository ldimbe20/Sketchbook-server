from django.db import models

class Mood(models.Model):
    mood_type = models.CharField(max_length=25)