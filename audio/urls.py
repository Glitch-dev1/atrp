from django.urls import path

from .views import *

urlpatterns = [
  path('m/<str:name>/', music_view, name='music'), 
] 