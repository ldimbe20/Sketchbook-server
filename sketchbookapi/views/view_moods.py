from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import MoodSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from sketchbookapi.models import Mood


class MoodView(ViewSet):
    
    def list(self, request):
        """Get a list of all post"""
        medium = Mood.objects.all()
        serializer = MoodSerializer(medium, many=True)
        return Response(serializer.data)
    