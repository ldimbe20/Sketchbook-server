from sketchbookapi.models import Post
from sketchbookapi.models import Comment
from sketchbookapi.models import Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import CommentSerializer
from sketchbookapi.serializers import CreateCommentSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
 
 
class CommentView(ViewSet):
    
    def list(self, request):
        """Get a list of all comments"""
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a comment"""
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new comment"""
        
        user = Artist.objects.get(user=request.auth.user)
        # post= Post.objects.get(post=request.post_id)
      
        comment = Comment.objects.create(
                post_id=request.data['post_id'],
                content=request.data['content'],
                created_on=request.data['created_on'],
                user = user,
                # post = post,
                # grabbing post information from above

            )
    
        try:
            serializer = CreateCommentSerializer(comment)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)