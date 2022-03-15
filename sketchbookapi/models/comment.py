from django.db import models

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment_post")
    user= models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="comment_artist")
    content = models.CharField(max_length=1000)
   