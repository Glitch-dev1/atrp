from django import forms

from .models import FacModel


class FacForm(forms.ModelForm):
  
  class Meta:
    model = FacModel
    fields = ('__all__')

