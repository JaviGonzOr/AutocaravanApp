import os
import django
from django.core.files import File

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autocaravana.settings")
django.setup()

# Importar modelos
from viajes.models import Archivo, Viaje

# 1️⃣ Carpeta donde están tus imágenes
carpeta_imagenes = r"C:\Users\Helic\Desktop\imagenes_a_subir"  # Cambia esta ruta

# 2️⃣ Elegir el primer viaje para asociar los archivos
viaje = Viaje.objects.first()
if not viaje:
    raise Exception("❌ No hay viajes en la base de datos. Crea uno primero.")

# 3️⃣ Recorrer todas las imágenes en la carpeta
for nombre_archivo in os.listdir(carpeta_imagenes):
    ruta_archivo = os.path.join(carpeta_imagenes, nombre_archivo)
    
    # Solo archivos de imagen
    if os.path.isfile(ruta_archivo) and nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        archivo = Archivo(viaje=viaje)
        with open(ruta_archivo, "rb") as f:
            archivo.archivo.save(nombre_archivo, File(f), save=True)
        print(f"✅ Subido: {nombre_archivo} → ID: {archivo.id} → URL: {archivo.archivo.url}")

print("🎉 Todas las imágenes han sido subidas a Cloudinary.")
