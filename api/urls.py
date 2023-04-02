from django.urls import path
from .views import CreateHackathonView, ListHackathonsView

urlpatterns = [    
    path('hackathons/create/', CreateHackathonView.as_view(), name='create_hackathon'),
    path('hackathons/', ListHackathonsView.as_view(), name='list_hackathons'),
]