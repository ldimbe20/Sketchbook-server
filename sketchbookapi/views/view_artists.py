from sketchbookapi.models import Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import ArtistSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import action




class ArtistView(ViewSet):
    
    def list(self, request):
        """Get a list of all artist"""
        artists = Artist.objects.all()
        # Making query to gather all info from artists
        serializer = ArtistSerializer(artists, many=True)
        # Serializer represents how the python data will be returned to client- We are gathering all the artists data here with many equals true
        # Created a folder of serializers to make data clearer to read this also represents encapsulation 
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a artist"""
        artists = Artist.objects.get(pk=pk)
        #Making query to only get artists that match the PK in the url route
        serializer = ArtistSerializer(artists)
        # gathering only the data from that one artist
         # Created a folder of serializers to make data clearer to read this also represents encapsulation 
        return Response(serializer.data)
    
    
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Only get artist back that are currently active on a book"""
        
        # creating a custom action that adds a new verb to URL that gets artists by currently active user

        artist= Artist.objects.get(user=request.auth.user)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    
