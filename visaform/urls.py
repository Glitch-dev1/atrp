from django.urls import path

from .views import *

app_name = 'Visa'

urlpatterns = [
  path('', visaView, name="Visa_View"),
  path('view/', visaAdmin, name="submitted_visa"),
  path('done/', visaDone, name="Visa_Submitted"),
  path('<int:id>/delete/', visa_delete, name="Visa_Delete"),
  ]