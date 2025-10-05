import os
import django

# 1️⃣ Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autocaravana.settings")
django.setup()

# 2️⃣ Ahora sí se pueden importar los modelos
from viajes.models import Archivo, Viaje
from django.core.files import File

# 3️⃣ Elegir el viaje al que subir las imágenes
viaje = Viaje.objects.first()

# 4️⃣ Carpeta con imágenes locales
ruta_media = os.path.join(os.path.dirname(__file__), "media", "archivos")

if not os.path.exists(ruta_media):
    print(f"No existe la carpeta: {ruta_media}")
else:
    for nombre in os.listdir(ruta_media):
        if nombre.lower().endswith((".jpg", ".jpeg", ".png")):
            ruta_archivo = os.path.join(ruta_media, nombre)
            try:
                archivo = Archivo(viaje=viaje)
                with open(ruta_archivo, "rb") as f:
                    archivo.archivo.save(nombre, File(f), save=True)
                print(f"✅ Subido: {nombre} → {archivo.archivo.url}")
            except Exception as e:
                print(f"❌ Error subiendo {nombre}: {e}")

print("🎉 Todas las imágenes locales han sido subidas a Cloudinary.")
