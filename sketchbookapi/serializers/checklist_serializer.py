from rest_framework import serializers
from sketchbookapi.models import Checklist


class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ('__all__')
        depth = 1
        
class CreateChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = ('__all__')
        depth = 1
        
