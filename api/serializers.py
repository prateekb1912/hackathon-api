from rest_framework import serializers
from .models import Hackathon, HackathonRegistration, Submission

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['title', 'description', 'background_image', 'hackathon_image', 'submission_type', 'start_datetime', 'end_datetime', 'reward_prize']

class HackathonRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonRegistration
        fields = ['submission']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['name', 'summary', 'submission_file', 'submission_link', 'submission_image']
        read_only_fields = ['user', 'hackathon']

    def validate(self, data):
        hackathon = self.context.get('hackathon')
        submission_type = hackathon.submission_type

        if submission_type == Submission.IMAGE and not data.get('submission_image'):
            raise serializers.ValidationError("A submission image is required for this hackathon.")

        if submission_type == Submission.FILE and not data.get('submission_file'):
            raise serializers.ValidationError("A submission file is required for this hackathon.")

        if submission_type == Submission.LINK and not data.get('submission_link'):
            raise serializers.ValidationError("A submission link is required for this hackathon.")

        return data
