from django.db import models

class MediumPost(models.Model):
    medium = models.ForeignKey("Medium", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)