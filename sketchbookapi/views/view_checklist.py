from email.mime import image
from sketchbookapi.models import Checklist, Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import ChecklistSerializer, CreateChecklistSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action
import base64
import uuid
from django.core.files.base import ContentFile
from django.db.models import Q

 
 
class ChecklistView(ViewSet):
    
    def list(self, request):
        """Get a list of all checklist"""
        checklists = Checklist.objects.all().order_by('-publication_date')
       
        serializer = ChecklistSerializer(checklists, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        checklists=Checklist.object.get(pk=pk)
        serializer = ChecklistSerializer(checklists)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new put"""
        user = Artist.objects.get(user=request.auth.user)
        format, imgstr = request.data["image_url"].split(';base64,')
        ext = format.split('/')[-1]
        imgdata = ContentFile(base64.b64decode(imgstr), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
        
        checklist = Checklist.objects.create(
            title = request.data['title'],
            publication_date = request.data['publication_date'],
            image_url = imgdata,
            task = request.data['task'],
            user = user,
        )
        
        try:
            serializer = CreateChecklistSerializer(checklist)
                # need to make a serializer to create json out of dictionary object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #if some information isn't presented below response will be sent out
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    
   
                
        
        
  