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
        comments = Comment.objects.all()
        post_id = request.query_params.get('postId', None)
        # Making query to gather all info from comments
        
        if post_id is not None:
            comments = comments.filter(post_id=post_id)
        
        serializer = CommentSerializer(comments, many=True)
         # Serializer represents how the python data will be returned to client- We are gathering all the comments data here with many equals true
        # Created a folder of serializers to make data clearer to read this also represents encapsulation 
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a comment"""
        comment = Comment.objects.get(pk=pk)
        #retrieving data by the pk that is in the url
        serializer = CommentSerializer(comment)
          # Serializer represents how the python data will be returned to client- We are gathering all the comments data here with many equals true
        # Created a folder of serializers to make data clearer to read this also represents encapsulation 
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        """Delete a post, current user must be associated with the post to be deleted
        """
        # getting comment by pk and then deleting if primary key doesn't exist we get a 204 response
        try:
            post = Comment.objects.get(pk=pk)
            post.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Create a new comment"""
        
        user = Artist.objects.get(user=request.auth.user)
        # Need to add foreign key artists object to create new post
      
        comment = Comment.objects.create(
                post_id=request.data['post_id'],
                content=request.data['content'],
                user = user,
            )
        
        # gathering all information to create a new comment
    
        try:
            serializer = CreateCommentSerializer(comment)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         #if some information isn't presented below response will be sent out
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)