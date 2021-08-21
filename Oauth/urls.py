from django.urls import path

from .views import *


urlpatterns = [
  path('login/', discord_login, name="Discord_Login"),
  path('login/redirect', discord_login_redirect, name="Discord_Redirect"),
  
]