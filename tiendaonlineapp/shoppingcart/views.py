from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from pets.models import Product
from django.http import HttpResponseRedirect
from .models import Shopping, City, Department, DocumentType


def index(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request,"shoppingcart/index.html",{
        "product" : product
    })

def finish(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        if(product.quantity <= 0):
            raise Exception("Se agoto la existencia del producto")
        department = Department.objects.get(pk=request.POST["id_department"])
        city = City.objects.get(pk=request.POST["id_city"])
        document_type = DocumentType.objects.get(pk=request.POST["id_document_type"])
    except (Exception, KeyError, City.DoesNotExist, Department.DoesNotExist, DocumentType.DoesNotExist) as e:
        return render(request,"shoppingcart/index.html",{
            "product" : product,
            "error_message": e
        })
    else:
        try:
            shopping = Shopping(
                name_lastname = request.POST["name_lastname"], 
                id_document_type = document_type,
                id_department = department,
                id_city = city,
                id_product = product,
                document = request.POST["document"],
                email = request.POST["email"],
                direction = request.POST["direction"],
                cellphone = request.POST["cellphone"],
                total = product.value,
                date = timezone.now()
            )
            shopping.save()
        except Exception as e:
            return render(request,"shoppingcart/index.html",{
                "product" : product,
                "error_message": e
            })
        else:
            product.quantity -= 1
            if(product.quantity <= 0):
                product.active = 0
            product.save()
            return HttpResponseRedirect(reverse("pets:index", args=(1,)))