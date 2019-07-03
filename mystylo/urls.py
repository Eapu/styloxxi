from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('styloxxi.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
