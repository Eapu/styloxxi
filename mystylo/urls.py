from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = 'My space'                    # default: "Django Administration"
admin.site.index_title = 'Administration'                 # default: "Site administration"
admin.site.site_title = 'Administration' # default: "Django site admin"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('styloxxi.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
