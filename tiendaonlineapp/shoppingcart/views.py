from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from pets.models import Product
from django.http import HttpResponseRedirect


def index(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request,"shoppingcart/index.html",{
        "product" : product
    })

def finish(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        shopping_cart = Product;
    except(KeyError):
        return render(request,"polls/index.html",{
        "product" : product,
        "error_message": "No elegiste una respuesta."
        })
    else:
        shopping_cart.quantity -= 1
        shopping_cart.save()
        return HttpResponseRedirect(reverse("polls:index", args=(product_id,)))