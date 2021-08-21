from django.shortcuts import render,redirect , HttpResponse
import requests
import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

discord_redirect_uri = "https://discord.com/api/oauth2/authorize?client_id=838112926005985280&redirect_uri=https%3A%2F%2Fatrp.atrpforum.repl.co%2Foauth%2Flogin%2Fredirect&response_type=code&scope=identify%20email"


def discord_login(request):
  
  return redirect(discord_redirect_uri)

def discord_login_redirect(request):
  code = request.GET.get('code')
  
  user = exchange_code(code)
  discord_user = authenticate(request, user=user)
  discord_user = list(discord_user).pop()
  print(discord_user)
  login(request, discord_user, backend='Oauth.auth.DiscordAuthenticationBackend')
  return redirect("/visa")

def exchange_code(code: str):
  
  data = {
    "client_id": os.environ['client_id'],
    "client_secret": os.environ['client_secret'],
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "https://atrp.atrpforum.repl.co/oauth/login/redirect",
    "scope": "identify email"
  }
  
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
  print(response)
  credentials = response.json()
  print(credentials)
  access_token = credentials['access_token']
  response = requests.get("https://discord.com/api/v6/users/@me", headers = {
    'Authorization': 'Bearer %s' % access_token
  })
  user = response.json()
  return user


