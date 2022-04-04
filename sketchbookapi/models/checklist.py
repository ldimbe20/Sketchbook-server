from django.db import models

class Checklist(models.Model):
    user = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='checklist_artist')
    title = models.CharField(max_length=120)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)
    task = models.CharField(max_length=1000)
    
    
    
   