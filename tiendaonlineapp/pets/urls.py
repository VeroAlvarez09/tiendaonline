from django.urls import URLPattern, path

from . import views

app_name = "pets"
urlpatterns = [
    #ex /pets/
    path("",views.index, name="index"),
   
]