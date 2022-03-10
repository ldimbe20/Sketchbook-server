from sketchbookapi.models import Post
from sketchbookapi.models import MediumPost
from sketchbookapi.models import Medium
from sketchbookapi.models import Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import MediumSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
 
 
class MediumView(ViewSet):
    
    def list(self, request):
        """Get a list of all post"""
        medium = Medium.objects.all()
        serializer = MediumSerializer(medium, many=True)
        return Response(serializer.data)
    
    # def create(self, request):
    #     """Create a new post"""
      
    #     post = Post.objects.create(
    #             mood_id=request.data['mood'],
    #             # grabbing post information from above
    #             title=request.data['title'],
    #             publication_date=request.data['publication_date'],
    #             image_url=request.data['image_url'],
    #             notes=request.data['notes'],
    #             private=request.data['private'],
    #             user = user
    #         )
    #     # ! would like to know exactly what is going on here...I know below is a many to many field   
    #     try:
    #         post.mediums_used.set(request.data['mediums_used'])
              
            
    #         serializer = PostSerializer(post)
    #         # need to make a serializer to create json out of dictionary object
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
 
    #     except ValidationError as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)