from django.db import models

class Post(models.Model):
    user = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='post_artist')
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post_category')
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE, related_name='post_mood')
    material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='post_material')
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.URLField()
    notes = models.CharField(max_length=1000)
    private = models.BooleanField()
   