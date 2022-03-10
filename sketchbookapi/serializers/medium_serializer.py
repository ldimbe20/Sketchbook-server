from rest_framework import serializers
from sketchbookapi.models import Medium


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ('id', 'name')
        depth = 2
