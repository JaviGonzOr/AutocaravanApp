from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.home, name='home'),
    path('lista_viajes', views.lista_viajes, name='lista_viajes'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('viaje/nuevo/', views.nuevo_viaje, name='nuevo_viaje'),
    path('viaje/<int:pk>/', views.detalle_viaje, name='detalle_viaje'),
    path('viaje/agregar/', views.agregar_viaje, name='agregar_viaje'),
    path('viaje/<int:pk>/editar/', views.editar_viaje, name='editar_viaje'),
    path('archivo/<int:pk>/eliminar/', views.eliminar_archivo, name='eliminar_archivo'),
    path('viaje/<int:pk>/eliminar/', views.eliminar_viaje, name='eliminar_viaje'),
    path ('registro/', views.registro, name='registro'),
    path ('c_sesion/', views.c_sesion, name = 'c_sesion'),
    path ('i_sesion/', views.i_sesion, name = 'i_sesion'), 
    path('ruta/', views.ruta_view, name='ruta'),

    
   
]









