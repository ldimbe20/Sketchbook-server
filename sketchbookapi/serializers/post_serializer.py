from rest_framework import serializers
from sketchbookapi.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'mediums_used', 'title', 'publication_date', 'image_url', 'notes', 'private', 'mood')
        depth = 2
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'mediums_used', 'title', 'publication_date', 'image_url', 'notes', 'private', 'mood')
       

