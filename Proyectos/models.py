from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Tipo_proyectos(models.Model):
    tipo=models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return '%s' % (self.tipo)

    class Meta:
        verbose_name_plural = "1. Tipo de Proyectos"

class Proyectos(models.Model):
    fecha=models.DateField(null=True, blank=True)
    nombre_proyecto=models.CharField(max_length=50, null=True,blank=True)
    imagen_1=models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_2 = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_3 = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_4 = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_5 = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_6 = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='360x360')
    imagen_centro = models.ImageField(upload_to='proyectos', null=True, blank=True, help_text='500x360')
    video_youtube = models.CharField(max_length=120,null=True,blank=True, help_text='link de video youtube')
    cliente=models.CharField(max_length=50, null=True,blank=True)
    tipo_proyecto=models.ForeignKey(Tipo_proyectos, on_delete=models.CASCADE, null=True, blank=True )
    lugar=models.CharField(max_length=50, null=True,blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen_1)

    class Meta:
        verbose_name_plural = "2. Proyectos"