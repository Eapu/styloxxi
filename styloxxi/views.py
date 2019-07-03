from django.shortcuts import render, get_object_or_404
from .models import Servicio, Producto,Video,Logo,Photocall

def home(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	videos = Video.published.all()
	return render(request, 'styloxxi/home.html',{'servicios':servicios, 'productos':productos,'videos':videos,'logos':logos})
def photocall(request):
	photocalls = Photocall.published.all()
	return render(request, 'styloxxi/photocall.html',{'photocalls':photocalls})
def servicios_list(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list.html',{'servicios': servicios,'productos':productos,'logos':logos})
def servicios_list2(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list2.html',{'servicios': servicios,'productos':productos,'logos':logos})
def servicios_list3(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list3.html',{'servicios': servicios,'productos':productos,'logos':logos})

def servicios_list4(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list4.html',{'servicios': servicios,'productos':productos,'logos':logos})
def servicios_list5(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list5.html',{'servicios': servicios,'productos':productos,'logos':logos})
def servicios_list6(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list6.html',{'servicios': servicios,'productos':productos,'logos':logos})
def servicios_list7(request):
	logos = Logo.published.all()
	servicios = Servicio.published.all()
	productos = Producto.published.all()
	return render(request,'styloxxi/servicios_list7.html',{'servicios': servicios,'productos':productos,'logos':logos})

def servicio_info(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	

def servicio_info_producto(request, pk):
	logos = Logo.published.all()
	producto = get_object_or_404(Producto, pk=pk)
	return render(request,'styloxxi/info_servicio_producto.html',{'producto': producto,'logos':logos})	

def servicio_info2(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio2.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	

def servicio_info3(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio3.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	

def servicio_info4(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio4.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	
def servicio_info5(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio5.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	
def servicio_info6(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio6.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	
def servicio_info7(request, pk):
	logos = Logo.published.all()
	servicio = get_object_or_404(Servicio, pk=pk)
	servicios = Servicio.published.all()
	productos = Producto.objects.filter(servicio__in=[servicio])
	return render(request,'styloxxi/info_servicio7.html',{'servicio': servicio,'servicios': servicios,'productos': productos,'logos':logos})	
