from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Archivo, Viaje

# NO repitas admin.site.register(Archivo) si ya usas @admin.register

class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('viaje', 'archivo')
