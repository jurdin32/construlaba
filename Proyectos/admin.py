from django.contrib import admin

# Register your models here.
from Proyectos.models import *
from construlaba.snippers import Attr

class Tipo_proyectosAdmin(admin.ModelAdmin):
    list_display = Attr(Tipo_proyectos)
    list_display_links = Attr(Tipo_proyectos)
admin.site.register(Tipo_proyectos, Tipo_proyectosAdmin)

class ProyectosAdmin(admin.ModelAdmin):
    list_display = Attr(Proyectos)
    list_display_links = Attr(Proyectos)
admin.site.register(Proyectos, ProyectosAdmin)
