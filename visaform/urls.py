from django.urls import path

from .views import *

app_name = 'Visa'

urlpatterns = [
  path('', visaView, name="Visa"),
  path('view/', visaAdmin, name="Visa_Admin"),
  path('create/',visaCreate, name="Visa_Create"),
  path('done/', visaDone, name="Visa_Submitted"),
  path('<int:id>/delete/', visa_delete, name="Visa_Delete")
  ]