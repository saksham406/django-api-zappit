from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    """Model for Post."""

    title = models.CharField(max_length=100)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

class Vote(models.Model):
    """Vote models for user."""
    voter = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)