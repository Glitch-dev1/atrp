from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import *


def visaCreate(request):
  if request.method == 'POST':
    form = VisaForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = VisaForm()
  context = {
    "form" : form
  }
  return render(request, 'visa/create.html', context)

@login_required(login_url="/login") 
def visaView(request):
  if request.method == 'POST':
    form = Visarform(request.POST)
    if form.is_valid():
      form.save()
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

def visaAdmin(request):
  objects = VisaModel.objects.all()
  context = {
    "object": objects
  }
  return render(request, 'visa/view.html', context)


@login_required(login_url='/login/')
def avatar_update(request, pk):
  context = {}
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    user = request.user
    if form.is_valid():
      user = form.save()
    
  else:
    form = ProfileForm()
  context['form'] = form
  
  return render(request, 'profile/update.html', context)

def visa_delete(request, id):
  context={}
  obj = get_object_or_404(VisaModel, id=id)
  if request.method == 'POST':
    obj.delete()
    return redirect('/visa/view')

