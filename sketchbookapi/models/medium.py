from django.db import models

class Medium(models.Model):
    name = models.CharField(max_length=25)