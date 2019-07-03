from django.contrib import admin
from .models import Servicio, Producto,Video,Logo,Photocall

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'publish')

admin.site.register(Servicio, ServicioAdmin)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('title', 'image', 'publish')

admin.site.register(Producto, ProductoAdmin)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'video', 'publish')

admin.site.register(Video, VideoAdmin)

class LogoAdmin(admin.ModelAdmin):
	list_display = ('company_name', 'logo', 'publish')

admin.site.register(Logo, LogoAdmin)

class PhotocallAdmin(admin.ModelAdmin):
	list_display = ('title', 'image_1')

admin.site.register(Photocall, PhotocallAdmin)