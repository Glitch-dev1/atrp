from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from decorators import *
from .forms import Visarform
from .models import VisaModel

@login_required(login_url="/login")
def visa(request):
  return redirect(f'/visa/{request.user.id}')


from django.forms.models import inlineformset_factory


@login_required(login_url="/login") 
def visaView(request):
  if request.method == 'POST':
    form = Visarform(request.POST)
    if form.is_valid():
      form.user = request.user
      task = form.save(commit=False)
      task.user = request.user.username
      task.save()
      return redirect('/visa/done')
  else:
     form = Visarform()
  context = {
    "form": form
    
  }
  return render(request, 'visa/main.html', context)

def visaDone(request):
  
  context = {
    
  }
  return render(request, 'visa/done.html', context)

@admin_only
def visaAdmin(request):
  objects = VisaModel.objects.all()
  context = {
    "object": objects
  }
  return render(request, 'visa/view.html', context)

@admin_only
def visa_delete(request, id):
  context={}
  obj = get_object_or_404(VisaModel, id=id)
  obj.delete()
  return redirect('/visa/view')

