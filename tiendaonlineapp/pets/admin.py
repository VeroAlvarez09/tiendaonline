from django.contrib import admin
from .models import Product

class ProductosAdmin(admin.ModelAdmin):
    list_display=('name', 'value', 'quantity')
    search_fields = ('name', 'value')

admin.site.register(Product, ProductosAdmin)