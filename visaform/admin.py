from django.contrib import admin

from .models import *

admin.site.site_header = 'ATRP ADMIN'
admin.site.index_title = "Admin Panel"

admin.site.register(VisaModel)
