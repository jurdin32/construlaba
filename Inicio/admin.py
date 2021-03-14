from django.contrib import admin

# Register your models here.
from Inicio.models import *
from construlaba.snippers import Attr

class SliderAdmin(admin.ModelAdmin):
    list_display = Attr(Slider)+["miniatura"]
    list_display_links = Attr(Slider)
admin.site.register(Slider, SliderAdmin)

class ConstrulabaAdmin(admin.ModelAdmin):
    list_display = Attr(Construlaba)+["miniatura"]
    list_display_links = Attr(Construlaba)
admin.site.register(Construlaba, ConstrulabaAdmin)

class Galeria_construlabaAdmin(admin.ModelAdmin):
    list_display = Attr(Galeria_construlaba)
    list_display_links = Attr(Galeria_construlaba)
admin.site.register(Galeria_construlaba, Galeria_construlabaAdmin)


class Contacto_redesAdmin(admin.ModelAdmin):
    list_display = Attr(Contacto_redes)
    list_display_links = Attr(Contacto_redes)
admin.site.register(Contacto_redes, Contacto_redesAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display = Attr(Direccion)
    list_display_links = Attr(Direccion)
admin.site.register(Direccion, DireccionAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = Attr(Experiencia)
    list_display_links = Attr(Experiencia)
admin.site.register(Experiencia, ExperienciaAdmin)

class Equipo_trabajoAdmin(admin.ModelAdmin):
    list_display = Attr(Equipo_trabajo)
    list_display_links = Attr(Equipo_trabajo)
admin.site.register(Equipo_trabajo, Equipo_trabajoAdmin)



