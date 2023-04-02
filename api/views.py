from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import HackathonSerializer
from .models import Hackathon

class CreateHackathonView(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
