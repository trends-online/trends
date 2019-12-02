from django.db import models

class trends(models.Model):
    type = models.CharField(max_length=100)
    header = models.TextField()
    keywords = models.CharField(max_length=200)
    image_link = models.TextField()
    paragraph = models.TextField(default=None, blank=True, null=True)
    video_link = models.TextField(default=None, blank=True, null=True)

class social(models.Model):
    image_link = models.TextField()
    post_link = models.TextField()