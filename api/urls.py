from django.urls import path
from .views import CreateHackathonView, ListHackathonsView, RegisterHackathonView

urlpatterns = [    
    path('hackathons/create/', CreateHackathonView.as_view(), name='create_hackathon'),
    path('hackathons/', ListHackathonsView.as_view(), name='list_hackathons'),
    path('hackathons/<int:pk>/register/', RegisterHackathonView.as_view(), name='register_hackathon'),
    path('hackathons/<int:pk>/submit/', CreateSubmissionView.as_view(), name='create_submission'),
    path('enrolled-hackathons/', EnrolledHackathonsListAPIView.as_view(), name='enrolled_hackathons_list'),
    path('hackathons/<int:hackathon_id>/submissions/', UserSubmissionsListAPIView.as_view(), name='user_submissions_list'),
]