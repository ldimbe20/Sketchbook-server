from sketchbookapi.models import Medium
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import MediumSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
 
 
class MediumView(ViewSet):
    
    def list(self, request):
        """Get a list of all medium"""
        medium = Medium.objects.all()
        serializer = MediumSerializer(medium, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new medium"""
      
        medium = Medium.objects.create(
                name=request.data['name'],
                # grabbing medium information from above

            )
       
        try:
            serializer = MediumSerializer(medium)
            # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
   
        
    def destroy(self, request, pk):
        """Delete a medium, current user must be associated with the medium to be deleted
        """
        try:
            medium = Medium.objects.get(pk=pk)
            medium.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Medium.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)