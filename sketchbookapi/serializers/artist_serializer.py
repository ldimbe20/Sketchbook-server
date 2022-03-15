from rest_framework import serializers
from sketchbookapi.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('__all__')
        depth = 2


