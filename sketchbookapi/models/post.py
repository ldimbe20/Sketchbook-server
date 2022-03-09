from django.db import models

class Post(models.Model):
    user = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='post_artist')
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE, related_name='post_mood')
    mediums_used = models.ManyToManyField("medium", through="MediumPost", related_name="mediums_used")
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.URLField()
    notes = models.CharField(max_length=1000)
    private = models.BooleanField()
    
    # artwork_pic = models.ImageField(
    #     upload_to='artwork', height_field=None,
    #     width_field=None, max_length=None, null=True)
   
   