from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.filter(active = 1)
    return render(request,"pets/index.html",{
        "products" : products
    })
