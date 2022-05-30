from django.shortcuts import render

from .models import Product

def index(request):
    products_list = Product.objects.filter(quantity=1).filter(active = 1)
    return render(request,"pets/index.html",{
        "products_list" : products_list
    })
