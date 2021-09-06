from django.urls import path, include

from .views import *

urlpatterns = [
    path('apply/', factionApply, name='Faction Application'),
    
  ]
