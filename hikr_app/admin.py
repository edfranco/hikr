# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, Profile, Comment
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
