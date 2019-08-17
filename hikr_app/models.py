# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    description = models.TextField()
    distance_hiked = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    photo_url = models.TextField()
    date_posted = models.DateField(default = timezone.now)

    def __str__(self):
      return (f"{self.author.first_name} Post")

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='post_author')
    image_url = models.URLField(max_length=200)
    date_joined = models.DateField(default = timezone.now)

    def __str__(self):
        return f"{self.user.first_name}/'s profile"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'comment_author' )
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name= 'comments_post')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments_profile")
    content = models.TextField()

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'liker')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name= 'post' )
