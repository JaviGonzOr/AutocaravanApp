# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje, Archivo
from .forms import ViajeForm, ArchivoForm, RegistroForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.utils.dateparse import parse_datetime



def home(request):
    viajes = Viaje.objects.all()
    return render(request, 'viajes/home.html', {'viajes': viajes})

from cloudinary.uploader import destroy

def eliminar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    
    # Primero eliminamos todos los archivos del viaje en Cloudinary
    for archivo in viaje.archivos.all():
        try:
            destroy(archivo.archivo.public_id)  # Borra de Cloudinary
        except Exception as e:
            print(f"No se pudo borrar {archivo.archivo.public_id}: {e}")
        archivo.delete()  # Borra el registro en la DB

    # Luego borramos el viaje
    viaje.delete()
    
    return redirect('lista_viajes')



@login_required
def lista_viajes(request):
    viajes = Viaje.objects.filter(usuario=request.user)
    return render(request, 'viajes/lista_viajes.html', {'viajes': viajes})

def detalle_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    archivos = viaje.archivos.all()
    return render(request, 'viajes/detalle_viaje.html', {'viaje': viaje, 'archivos': archivos})

def agregar_viaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        files = request.FILES.getlist('archivos')  # <-- ojo, 'archivos' es el name del input
        if form.is_valid():
            viaje = form.save()
            for f in files:
                Archivo.objects.create(viaje=viaje, archivo=f)
            return redirect('lista_viajes')
    else:
        form = ViajeForm()
    return render(request, 'viajes/agregar_viaje.html', {'form': form})


def editar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == 'POST':
        form = ViajeForm(request.POST, instance=viaje)
        files = request.FILES.getlist('archivos')
        if form.is_valid():
            viaje = form.save()
            # Agregar archivos nuevos sin borrar los antiguos
            for f in files:
                Archivo.objects.create(viaje=viaje, archivo=f)
            return redirect('detalle_viaje', pk=viaje.pk)
    else:
        form = ViajeForm(instance=viaje)
    return render(request, 'viajes/editar_viaje.html', {'form': form, 'viaje': viaje})

@login_required
def nuevo_viaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST, request.FILES)
        files = request.FILES.getlist('archivos')
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.usuario = request.user  # 👈 muy importante
            viaje.save()
            for f in files:
                Archivo.objects.create(viaje=viaje, archivo=f)
            return redirect('detalle_viaje', pk=viaje.pk)
    else:
        form = ViajeForm()
    return render(request, 'viajes/nuevo_viaje.html', {'form': form})

def sobre_mi(request):
    return render(request, 'viajes/sobre_mi.html')


from django.shortcuts import get_object_or_404, redirect
from cloudinary.uploader import destroy
from viajes.models import Archivo

def eliminar_archivo(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    
    # Intentamos borrar la imagen de Cloudinary
    try:
        destroy(archivo.archivo.public_id)
    except Exception as e:
        print(f"No se pudo borrar {archivo.archivo.public_id} de Cloudinary: {e}")
    
    # Borrar el registro de la base de datos
    archivo.delete()
    
    return redirect('lista_viajes')  # O a la página donde quieras volver



def registro(request):
    if request.method == 'GET':
        return render(request, "viajes/registro.html", {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'viajes/home.html', {
                    'exito': 'Usuario creado con exito'
                })
            except IntegrityError:
                return render(request, 'viajes/registro.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })

        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las Contraseñas no coinciden'
        })

def c_sesion(request):
    logout(request)
    return render(request, 'viajes/eliminado.html')


def i_sesion(request):
    if request.method == 'GET':
        return render(request, "viajes/i_sesion.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'viajes/i_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Contraseña o Nombre incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')

@login_required
def ruta_view(request):
    # Ejemplo de datos dinámicos (en la práctica, los datos vendrían de una base de datos)
    ruta = [
        {'lat': 40.4168, 'lng': -3.7038},  # Madrid
        {'lat': 41.6168, 'lng': -2.7038},  # Zaragoza
        {'lat': 42.7744, 'lng': -1.4975}   # Pamplona
    ]
    return render(request, 'viajes/ruta.html', {'ruta': ruta})
