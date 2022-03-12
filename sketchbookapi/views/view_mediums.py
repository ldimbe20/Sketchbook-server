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
    
    def create(self, request):
        """Create a new post"""
      
        medium = Medium.objects.create(
                name=request.data['name'],
                # grabbing post information from above

            )
       
        try:
            serializer = MediumSerializer(medium)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)