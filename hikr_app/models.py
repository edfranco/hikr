# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    description = models.TextField()
    distance_hiked = IntegerField()
    location = models.CharField(max_length=100)
    photo_url = models.TextField()
     
    def __str__(self):
      return self.author