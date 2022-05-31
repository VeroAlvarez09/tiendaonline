from django.contrib import admin

from .models import DocumentType,City, Department, Shopping

class ShoppingAdmin(admin.ModelAdmin):
    list_display=('id', 'name_lastname', 'email', 'cellphone', 'date', 'id_product', 'total')
    search_fields = ('name', 'total')

admin.site.register(DocumentType)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(Shopping, ShoppingAdmin)