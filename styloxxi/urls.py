from django.conf.urls import url, include
from . import views
from .views import home,photocall,servicios_list,servicios_list2,servicios_list3,servicios_list4,servicios_list5,servicios_list6,servicios_list7,servicio_info,servicio_info2,servicio_info3,servicio_info4,servicio_info5,servicio_info6,servicio_info7,servicio_info_producto

urlpatterns = [

  #url(r'^$', views.post_list, name='post_list'),
	url(r'^$', views.home, name='home'),
	url(r'^servicios/', views.servicios_list, name='servicios_list'),
	url(r'^servicios2/', views.servicios_list2, name='servicios_list2'),
	url(r'^servicios3/', views.servicios_list3, name='servicios_list3'),
	url(r'^servicios4/', views.servicios_list4, name='servicios_list4'),
	url(r'^servicios5/', views.servicios_list5, name='servicios_list5'),
	url(r'^servicios6/', views.servicios_list6, name='servicios_list6'),
	url(r'^servicios7/', views.servicios_list7, name='servicios_list7'),
	url(r'^servicio_info/(?P<pk>[0-9]+)/$', views.servicio_info, name='servicio_info'),
	url(r'^servicio_info2/(?P<pk>[0-9]+)/$', views.servicio_info2, name='servicio_info2'),
	url(r'^servicio_info3/(?P<pk>[0-9]+)/$', views.servicio_info3, name='servicio_info3'),
	url(r'^servicio_info4/(?P<pk>[0-9]+)/$', views.servicio_info4, name='servicio_info4'),
	url(r'^servicio_info5/(?P<pk>[0-9]+)/$', views.servicio_info5, name='servicio_info5'),
	url(r'^servicio_info6/(?P<pk>[0-9]+)/$', views.servicio_info6, name='servicio_info6'),
	url(r'^servicio_info7/(?P<pk>[0-9]+)/$', views.servicio_info7, name='servicio_info7'),

	url(r'^servicio_info_producto/(?P<pk>[0-9]+)/$', views.servicio_info_producto, name='servicio_info_producto'),
	url(r'^photocall/', views.photocall, name='photocall'),

	]
