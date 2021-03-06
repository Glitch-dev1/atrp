from django import forms

from .models import *


class Visarform(forms.ModelForm):
  genderchoices = (
      ('male','male'),
      ('female', 'female')
    )
  rpexpchoices = (
      ('new', 'New to Roleplay'),
      ('1m', '1 Month'),
      ('5m', '5 months'),
      ('1y', '1 year'),
      ('a1y', 'Above 1 year')
    
    )
  user = forms.CharField(required=False)
  realname = forms.CharField()
  gender = forms.ChoiceField(choices=genderchoices, required=False)
  realage = forms.IntegerField()
  rprules = forms.BooleanField()
  igname = forms.CharField()
  igage = forms.IntegerField()
  iggender = forms.ChoiceField(choices=genderchoices)
  rpexp = forms.ChoiceField(choices=rpexpchoices)
  discordname = forms.CharField()
  characterstory = forms.CharField()
  
  class Meta:
    model  = VisaModel
    fields = ('__all__')
    



