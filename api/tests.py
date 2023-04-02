from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from .models import Hackathon, Submission
from django.contrib.auth.models import User


class HackathonTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.hackathon_data = {
            'title': 'Test Hackathon',
            'description': 'This is a test hackathon.',
            'background_image': '',
            'hackathon_image': '',
            'type_of_submission': 'file',
            'start_datetime': '2023-04-01T10:00:00Z',
            'end_datetime': '2023-04-02T18:00:00Z',
            'reward_prize': 1000
        }
        self.client.force_authenticate(user=self.user)

    def test_create_hackathon(self):
        url = reverse('hackathon-list')
        response = self.client.post(url, self.hackathon_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hackathon.objects.count(), 1)
        self.assertEqual(Hackathon.objects.get().title, 'Test Hackathon')

    def test_list_hackathons(self):
        Hackathon.objects.create(**self.hackathon_data)
        url = reverse('hackathon-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_enroll_to_hackathon(self):
        hackathon = Hackathon.objects.create(**self.hackathon_data)
        url = reverse('hackathon-enroll', kwargs={'pk': hackathon.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(hackathon.participants.count(), 1)

    def test_create_submission(self):
        hackathon = Hackathon.objects.create(**self.hackathon_data)
        url = reverse('submission-list')
        submission_data = {
            'name': 'Test Submission',
            'summary': 'This is a test submission.',
            'submission_file': open('test_file.png', 'rb')
        }
        response = self.client.post(url, {
            'hackathon': hackathon.pk,
            **submission_data
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Submission.objects.count(), 1)

    def test_list_enrolled_hackathons(self):
        hackathon = Hackathon.objects.create(**self.hackathon_data)
        hackathon.participants.add(self.user)
        url = reverse('enrolled-hackathon-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_submissions_for_enrolled_hackathon(self):
        hackathon = Hackathon.objects.create(**self.hackathon_data)
        hackathon.participants.add(self.user)
        submission = Submission.objects.create(
            hackathon=hackathon,
            user=self.user,
            name='Test Submission',
            summary='This is a test submission.',
            submission_file='test_file.png'
        )
        url = reverse('enrolled-hackathon-submission-list', kwargs={'pk': hackathon.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
