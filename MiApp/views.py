from django.shortcuts import render
from .models import Familia

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def cargadatos(request):
    familia = Familia.objects.create(
                                        nombre = "Juna Pablo", 
                                        apellido = "Gondra", 
                                        fecha_nacimiento = "1987-07-19", 
                                        mail = "gp@gmail.com", 
                                        edad = 35, 
                                        nacionalidad = "Argentina", 
                                        genero = "Femenino", 
                                        relacion = "Es mi hermana", 
                                        mascotas = {"Charly"}, 
                                        fecha_creacion = ''
                                    )
    context = {'familia': familia}
    return render(request, 'ingreso.html', context) 

def mostrar_familiares(request):
    familiares = Familia.objects.all()
    return render(request, "misfamiliares.html", {"familiares": familiares})