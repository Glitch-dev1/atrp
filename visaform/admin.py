from django.contrib import admin

from .models import *

admin.site.site_header = 'ATRP Database'
admin.site.index_title = "Site Tables"

admin.site.register(VisaModel)
