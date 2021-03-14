from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

class Construlaba(models.Model):
    favicon_1=models.ImageField(upload_to='favicon', null=True, blank=True,help_text='imagenes 20*20')
    favicon_2 = models.ImageField(upload_to='favicon', null=True, blank=True,help_text='imagenes 20*20')
    logo_horizontal_1 = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo_horizontal_2 = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo_1 = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    logo_2 = models.ImageField(upload_to='favicon',null=True, blank=True, help_text='imagenes 20*20')
    celular = models.CharField(max_length=11, null=True, blank=True)
    celular2 = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    nosotros=models.TextField(max_length=500, null=True, blank=True)
    mision = models.TextField(max_length=500, null=True, blank=True)
    vision = models.TextField(max_length=500, null=True, blank=True)
    valor = models.TextField(max_length=500, null=True, blank=True)
    representante = models.CharField(max_length=100, null=True, blank=True)
    horario = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(upload_to='construlaba', null=True, blank=True, help_text='imagenes 20*20')


    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.logo_horizontal_1)


    class Meta:
        verbose_name_plural = "1. Construlaba"

class Slider(models.Model):
    imagen=models.ImageField(upload_to='media', null=True, blank=True, help_text='imagenes 500*900')
    titulo=models.CharField(max_length=30, null=True,blank=True)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Slider"





class Galeria_construlaba(models.Model):
    imagen = models.ImageField(upload_to='construlaba', null=True, blank=True, help_text='imagenes 20*20')


    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 100px'>"%self.imagen)


    class Meta:
        verbose_name_plural = "2. Galeria_construlaba"


class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "3. Contácto Redes Sociales"



class Direccion(models.Model):
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    oficina = models.CharField(max_length=100, null=True, blank=True)
    planta = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name_plural = "4. Dirección"


class Experiencia(models.Model):
    anios_experiencia = models.IntegerField(default=0)
    trabajadores = models.IntegerField(default=0)
    clientes=  models.IntegerField(default=0)
    proyectos =  models.IntegerField(default=0)
    arquitectura= models.IntegerField(default=0)
    construccion= models.IntegerField(default=0)
    edificios= models.IntegerField(default=0)
    interior= models.IntegerField(default=0)
    comercial= models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "5. Experiencia"


class Equipo_trabajo(models.Model):
    imagen = models.ImageField(upload_to='equipo', null=True, blank=True, help_text='imagenes 90*90')
    nombre = models.CharField(max_length=100, null=True, blank=True)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    detalle = models.TextField(max_length=500, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=11, null=True, blank=True)


    class Meta:
        verbose_name_plural = "6. Equipo de trabajo"