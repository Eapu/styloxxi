from django.conf.urls import url, include
from . import views
from .views import home,photocall,servicios_list,servicios_list2,servicios_list3,servicio_info,servicio_info2,servicio_info3,servicio_info_producto

urlpatterns = [

  #url(r'^$', views.post_list, name='post_list'),
	url(r'^$', views.home, name='home'),
	url(r'^servicios/', views.servicios_list, name='servicios_list'),
	url(r'^servicios2/', views.servicios_list2, name='servicios_list2'),
	url(r'^servicios3/', views.servicios_list3, name='servicios_list3'),
	url(r'^servicio_info/(?P<pk>[0-9]+)/$', views.servicio_info, name='servicio_info'),
	url(r'^servicio_info2/(?P<pk>[0-9]+)/$', views.servicio_info2, name='servicio_info2'),
	url(r'^servicio_info3/(?P<pk>[0-9]+)/$', views.servicio_info3, name='servicio_info3'),
	url(r'^servicio_info_producto/(?P<pk>[0-9]+)/$', views.servicio_info_producto, name='servicio_info_producto'),
	url(r'^photocall/', views.photocall, name='photocall'),

	]
