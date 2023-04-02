from django.db import models

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
