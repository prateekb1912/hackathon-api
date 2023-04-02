from django.db import models
from django.contrib.auth.models import User
from .validators import validate_submission_file_type
from .utils import get_submission_file_path


class Hackathon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon/')
    hackathon_image = models.ImageField(upload_to='hackathon/')
    IMAGE = 'image'
    FILE = 'file'
    LINK = 'link'
    SUBMISSION_CHOICES = [
        (IMAGE, 'Image'),
        (FILE, 'File'),
        (LINK, 'Link'),
    ]
    submission_type = models.CharField(
        max_length=5,
        choices=SUBMISSION_CHOICES,
        default=IMAGE,
    )
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)

class HackathonRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'hackathon')

    def __str__(self):
        return f"{self.user.username} - {self.hackathon.title}"


class Submission(models.Model):
    SUBMISSION_TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link')
    ]

    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=1000)
    submission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPE_CHOICES)
    submission = models.FileField(upload_to=get_submission_file_path, null=True, blank=True, validators=[validate_submission_file_type])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.name}'
