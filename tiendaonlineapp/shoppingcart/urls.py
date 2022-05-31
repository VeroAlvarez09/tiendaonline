from django.urls import URLPattern, path

from . import views

app_name = "shoppingcart"
urlpatterns = [
    #ex /shoppingcarts/
    path("<int:product_id>/",views.index, name="index"),
    path("<int:product_id>/finish/",views.finish, name="finish"),
]