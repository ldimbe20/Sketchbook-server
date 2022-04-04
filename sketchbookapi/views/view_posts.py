from sketchbookapi.models import Post, Comment, Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import PostSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
import base64
import uuid
from django.core.files.base import ContentFile
from django.db.models import Q

 
 
class PostView(ViewSet):
    
    def list(self, request):
        """Get a list of all post"""
        posts = Post.objects.all().order_by('-publication_date')
        mood_id = request.query_params.get('mood_id', None)
        user_id = request.query_params.get('user_id', None)
        title = self.request.query_params.get('q', None)
        
        
        # creating filters by querying the database with above. Request.query_params is a dictionary of any query parameters that were in the url
        # we are checking for mood_id or user_id, if they are not none then they will return the posts by what is queried.
        if title is not None:
            posts = posts.filter(title__icontains=f"{title}")
    
        if mood_id is not None:
            posts = posts.filter(mood_id=mood_id)
            
        if user_id is not None:
            posts = posts.filter(user_id=user_id)
    
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
        # need to grab ForeignKey artists info and add to post
        
    
        format, imgstr = request.data["image_url"].split(';base64,')
        ext = format.split('/')[-1]
        imgdata = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
        
        # Above we are assigning imgdata to turn image_url data and base64 data into a string
      
        post = Post.objects.create(
                mood_id=request.data['mood_id'],
                # grabbing post information from above
                title=request.data['title'],
                publication_date=request.data['publication_date'],
                image_url=imgdata,
                notes=request.data['notes'],
                private=request.data['private'],
                user = user
                # data passed from client is held in request.data dictionary
                # ! keys on request.data must match what the clientside is passing through
            )   
        try:
            post.mediums_used.set(request.data['mediums_used'])
            # above we are adding on the mediums_post many-to-many table to the post data
            
            serializer = PostSerializer(post)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            # this new information will now be passed over to client side
 
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

        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


    @action(methods=['get'], detail=False)
    #@action turns method into new route, currentUser, in url. 
    def currentUser(self, request):
        """Post request for a user to sign up for an event"""
        post = Post.objects.get(user=request.auth.user) 
        
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    
    
      

