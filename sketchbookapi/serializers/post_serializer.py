from rest_framework import serializers
from sketchbookapi.models import Artist
from sketchbookapi.models import Post


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('__all__')
#         depth = 2

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'mediums_used', 'title', 'publication_date', 'image_url', 'notes', 'private', 'mood')
        depth = 2
