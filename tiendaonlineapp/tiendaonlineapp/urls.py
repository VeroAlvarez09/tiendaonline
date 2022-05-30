from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("pets.urls")),
    path('admin/', admin.site.urls),
    path("shoppingcart/", include("shoppingcart.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)