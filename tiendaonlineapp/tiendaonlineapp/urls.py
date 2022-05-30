from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pets.urls")),
    path("pets/", include("pets.urls")),
    path('admin/', admin.site.urls),
]
