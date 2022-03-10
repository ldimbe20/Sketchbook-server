from rest_framework import serializers
from sketchbookapi.models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'mood_type')