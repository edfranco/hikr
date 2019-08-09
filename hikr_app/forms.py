from django import forms
from django.contrib.auth.models import User

# from .models import Artist, Song

class SignupForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'password')



