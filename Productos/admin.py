from django.contrib import admin

# Register your models here.
from Productos.models import *
from construlaba.snippers import Attr


class ProductoAdmin(admin.ModelAdmin):
    list_display = Attr(Producto)
    list_display_links = Attr(Producto)
admin.site.register(Producto, ProductoAdmin)