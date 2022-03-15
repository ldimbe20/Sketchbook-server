from rest_framework import serializers
from sketchbookapi.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')
        depth = 2

class CreateCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for posting new comment"""
    class Meta:
        model = Comment
        fields = ('__all__')
       