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
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Get a artist"""
        artists = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artists)
        return Response(serializer.data)
    
    # @action(methods=['get'], detail=False)
    # #@action turns method into new route, signup, in url. 
    # def currentUser(self, request):
    #     """Artist request for a user to sign up for an event"""
    #     artist = Artist.objects.get(user=request.auth.user) 
        
    #     # artist = Artist.objects.get(pk=pk)
    #     # artist.artist.add(artist)
        
    #     serializer = ArtistSerializer(artist)
    #     return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Only get actors back that are currently active on a book"""

        artist= Artist.objects.get(user=request.auth.user)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
