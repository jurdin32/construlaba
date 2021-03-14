from django.shortcuts import render

import Productos
from Inicio.models import *
# Create your views here.
from Productos.models import *
from Proyectos.models import *


def index(request):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.all(),
        'productos': Producto.objects.all(),

    }
    return render(request,'index.html', contexto)

def empresa(request):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.all(),
        'productos': Producto.objects.all(),
        'equipo': Equipo_trabajo.objects.all(),

    }
    return render(request,'about-1.html', contexto)

def portafolio(request):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.all(),

    }
    return render(request,'project-grid.html', contexto)


def portafolio_id(request,id):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.get(id=id),

    }
    return render(request,'project-detail.html', contexto)


def cotizar(request,id):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.get(id=id),

    }
    return render(request,'project-detail.html', contexto)

def contacto(request):
    contexto ={
        'slider':Slider.objects.all(),
        'galeria_construlaba': Galeria_construlaba.objects.all(),
        'construlaba':Construlaba.objects.all().first(),
        'contacto': Contacto_redes.objects.all().first(),
        'direccion': Direccion.objects.all().all(),
        'experiencia':Experiencia.objects.all().first(),
        'tipo_proyectos': Tipo_proyectos.objects.all(),
        'proyectos': Proyectos.objects.all(),

    }
    return render(request,'contact-1.html', contexto)

