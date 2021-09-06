from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth, Group

from .forms import *
from decorators import unauth_only
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def homepage(request):
  return redirect('/visa/')

@login_required(login_url='/login/')
def profile_update(request):
  context = {}
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      user = form.save()
      messages.success(request, "Profile has been updated successfully")
      return redirect("/")
    
  else:
    form = ProfileForm(instance=request.user)
  context['form'] = form
  
  return render(request, 'profile/update.html', context)

@unauth_only
def registerpage(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      group = Group.objects.get(name= "users")
      user.groups.add(group)
      return redirect("/login/")
      messages.success(request, "Account has been successfully created")
  else:
    form = NewUserForm()
  context = {
    "form": form
  }
  return render(request, 'register.html', context)

@login_required
def sendMail(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    message = request.POST['message']
    email = request.POST['email']
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
  
  return render(request, 'sendmail.html')  

@unauth_only
def loginpage(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	else:
	  form = AuthenticationForm()
	return render(request, 'login.html',{})


def logoutpage(request):
  logout(request)
  return redirect('/')

from server.models import gallery

def gallerypage(request):
  images = gallery.objects.all()
  if request.method == "POST":
    form = GalleryForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect("/gallery")
    
  else:
    form = GalleryForm()
  context = {
    "form": form,
    "images": images
  }
  return render(request, 'server/gallery.html', context)

def homeage(request):
  return render(request, 'index.html')

