from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filter = models.TextField()
    filtered_image = models.ImageField()
    title = models.CharField(max_length=128)
    # likes = models.ManyToManyField(User, related_name='users')
