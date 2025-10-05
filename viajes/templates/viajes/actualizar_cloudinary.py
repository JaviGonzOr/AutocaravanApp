import os
import django
from cloudinary.uploader import upload
from viajes.models import Archivo

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocravana.settings')
django.setup()

# Carpeta local donde están tus archivos
carpeta = r"C:\Users\Helic\Desktop\Vacaciones\archivos"

# Iterar sobre todos los registros de Archivo
for a in Archivo.objects.all():
    ruta_local = os.path.join(carpeta, os.path.basename(a.archivo.name))
    
    # Subir a Cloudinary
    resultado = upload(ruta_local, folder="mis_archivos")
    
    # Guardar la URL de Cloudinary en el campo archivo
    a.archivo = resultado['url']
    a.save()
    
    print(f"Actualizado: {a.id} -> {a.archivo}")
