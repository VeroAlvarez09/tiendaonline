from django.shortcuts import render

from .models import Product

def index(request, message=""):
    products = Product.objects.filter(active = 1)
    success_message = ""
    if(message):
        success_message = "Compra realizada exitosamente, su pedido se encuentra en proceso de despacho"
    return render(request,"pets/index.html",{
        "products" : products,
        "success_message":success_message
    })
