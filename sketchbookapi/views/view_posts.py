from sketchbookapi.models import Post, Mood, Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import PostSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
import base64
import uuid
from django.core.files.base import ContentFile

 
 
class PostView(ViewSet):
    
    def list(self, request):
        """Get a list of all post"""
        posts = Post.objects.all().order_by('publication_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
   
    
    def retrieve(self, request, pk):
        """Get a post"""
        posts = Post.objects.get(pk=pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)
    
 
    def create(self, request):
        """Create a new put"""
     
        user = Artist.objects.get(user=request.auth.user)
        
    
        format, imgstr = request.data["image_url"].split(';base64,')
        ext = format.split('/')[-1]
        imgdata = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
        
        
      
        post = Post.objects.create(
                mood_id=request.data['mood_id'],
                # grabbing post information from above
                title=request.data['title'],
                publication_date=request.data['publication_date'],
                image_url=imgdata,
                notes=request.data['notes'],
                private=request.data['private'],
                user = user
                
            )   
        try:
            post.mediums_used.set(request.data['mediums_used'])
             
            serializer = PostSerializer(post)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, pk):
        """Delete a post, current user must be associated with the post to be deleted
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk): 
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        # format, imgstr = request.data["image_url"].split(';base64,')
        # ext = format.split('/')[-1]
        # imgdata = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
        
        

        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


    @action(methods=['get'], detail=False)
    #@action turns method into new route, signup, in url. 
    def currentUser(self, request):
        """Post request for a user to sign up for an event"""
        post = Post.objects.get(user=request.auth.user) 
        
        serializer = UpdatePostSerializer(post)
        return Response(serializer.data)
    

