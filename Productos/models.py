from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Producto(models.Model):
    orden = models.IntegerField(default=0)
    resistencia=models.CharField(max_length=50, null=True,blank=True)
    detalle=models.TextField( null=True,blank=True)


    class Meta:
        verbose_name_plural = "1. Productos"