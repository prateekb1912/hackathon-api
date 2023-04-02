from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import HackathonSerializer, HackathonRegistrationSerializer
from .models import Hackathon, Submission

class CreateHackathonView(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ListHackathonsView(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class RegisterHackathonView(generics.CreateAPIView):
    serializer_class = HackathonRegistrationSerializer

    def post(self, request, pk):
        hackathon = Hackathon.objects.filter(pk=pk).first()

        if not hackathon:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        registration = HackathonRegistration.objects.create(
            hackathon=hackathon,
            user=request.user,
            submission=serializer.validated_data['submission']
        )

        return Response(HackathonRegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)

class CreateSubmissionView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def post(self, request, pk):
        hackathon = Hackathon.objects.filter(pk=pk).first()

        if not hackathon:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        submission = Submission.objects.create(
            hackathon=hackathon,
            user=request.user,
            name=serializer.validated_data['name'],
            summary=serializer.validated_data['summary'],
            submission=serializer.validated_data['submission']
        )

        return Response(SubmissionSerializer(submission).data, status=status.HTTP_201_CREATED)
