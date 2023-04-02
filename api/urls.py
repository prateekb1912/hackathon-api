from django.urls import path
from .views import CreateHackathonView, ListHackathonsView, RegisterHackathonView

urlpatterns = [    
    path('hackathons/create/', CreateHackathonView.as_view(), name='create_hackathon'),
    path('hackathons/', ListHackathonsView.as_view(), name='list_hackathons'),
    path('hackathons/<int:pk>/register/', RegisterHackathonView.as_view(), name='register_hackathon'),
]