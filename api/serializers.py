from rest_framework import serializers
from .models import Hackathon

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['title', 'description', 'background_image', 'hackathon_image', 'submission_type', 'start_datetime', 'end_datetime', 'reward_prize']
