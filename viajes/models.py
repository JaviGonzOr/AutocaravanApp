from django.db import models
from django.contrib.auth.models import User

class Viaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    origen = models.CharField(null=True, blank=True, max_length=200)  # nombre de ciudad
    destino = models.CharField(null=True, blank=True, max_length=200)
    origen_lat = models.FloatField(null=True, blank=True)
    origen_lng = models.FloatField(null=True, blank=True)
    destino_lat = models.FloatField(null=True, blank=True)
    destino_lng = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.titulo

class Archivo(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.archivo.name
