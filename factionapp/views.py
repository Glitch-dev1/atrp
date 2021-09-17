from django.shortcuts import render

from .forms import *

def factionApply(request):
  if request.method == 'POST':
    form = FacForm(request.POST)
    if form.is_valid():
      form.user = request.user.username
      form.save()
  else:
    form = FacForm()
  context = {
    "form": form
  }
  return render(request, 'faction/appy.html', context)
