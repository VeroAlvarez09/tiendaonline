from django.contrib import admin

from .models import DocumentType,City, Department, Shopping

admin.site.register(DocumentType)
admin.site.register(Department)
admin.site.register(City)