from django.urls import path
from .views import CreateHackathonView

urlpatterns = [    path('hackathons/create/', CreateHackathonView.as_view(), name='create_hackathon'),]