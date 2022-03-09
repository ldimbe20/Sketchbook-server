from rest_framework import serializers
from sketchbookapi.models import Artist
from sketchbookapi.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
        depth = 1


