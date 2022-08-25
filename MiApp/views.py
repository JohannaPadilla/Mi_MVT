from django.shortcuts import render
from .models import Familia, Mascotas

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def cargadatos(request):
    familia = Familia.objects.create(
                                        nombre = "Hugo", 
                                        apellido = "Padilla", 
                                        fecha_nacimiento = "1957-05-19", 
                                        mail = "gp@gmail.com", 
                                        edad = 65, 
                                        nacionalidad = "Argentino", 
                                        genero = "Masculino", 
                                        relacion = "Es mi Padre", 
                                        mascotas = {"No tiene mascotas"}, 
                                        fecha_creacion = ''
                                    )
    context = {'familia': familia}
    return render(request, 'carga.html', context) 

def mostrar_familiares(request):
    familiares = Familia.objects.all()
    return render(request, "misfamiliares.html", {"familiares": familiares})

def cargarmascota(request, nombre, especie):
    mascotas = Mascotas.objects.create(
                                        nombre = nombre, 
                                        especie = especie, 
                                        fecha_creacion = ''
                                    )
    context = {'mascotas': mascotas}
    return render(request, 'cargamascotas.html', context) 

def mostrar_mascotas(request):
    mascotas = Mascotas.objects.all()
    return render(request, "lasmascotas.html", {"mascotas": mascotas})