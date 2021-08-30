from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from server.models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Create your forms here.

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "email", "password1","password2")

class ProfileForm(forms.ModelForm):
  
  class Meta:
    model = User
    fields = ('username',)

class GalleryForm(forms.ModelForm):
  class Meta:
    model = gallery
    fields = ('__all__')

