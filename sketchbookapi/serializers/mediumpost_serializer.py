from rest_framework import serializers
from sketchbookapi.models import MediumPost


class MediumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumPost
        fields = ('__all__')
        
