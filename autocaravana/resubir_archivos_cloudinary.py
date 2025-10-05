import os
import django
from pathlib import Path
from django.core.files import File

# 1) configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autocaravana.settings")
django.setup()

from viajes.models import Archivo

BASE_DIR = Path(__file__).resolve().parent

def find_local_file(name):
    """
    name suele ser 'archivos/xxxxx.jpg' o similares.
    Probamos varias rutas donde pueda estar el fichero local.
    """
    candidates = [
        BASE_DIR / "media" / name,                     # media/archivos/...
        BASE_DIR / name,                               # archivos/...
        BASE_DIR / "media" / os.path.basename(name),   # media/filename
        BASE_DIR / "archivos" / os.path.basename(name) # archivos/filename
    ]
    for p in candidates:
        if p.exists():
            return p
    return None

processed = 0
for a in Archivo.objects.all():
    processed += 1
    name = a.archivo.name  # por ejemplo 'archivos/20250711_212649.jpeg'
    print(f"[{processed}] Procesando ID={a.id} -> {name}")

    # Si ya apunta a Cloudinary o es URL absoluta, saltamos
    url = str(a.archivo.url)
    if url.startswith("http"):
        print("  -> Ya en Cloudinary (URL):", url)
        continue

    # Intentamos localizar el fichero local
    local_path = find_local_file(name)
    if not local_path:
        print("  -> NO se encontró el fichero local para:", name)
        continue

    # Abrimos y salvamos (esto subirá a Cloudinary si DEFAULT_FILE_STORAGE está bien)
    try:
        with local_path.open("rb") as f:
            a.archivo.save(os.path.basename(name), File(f), save=True)
        print("  -> Subido a Cloudinary:", a.archivo.url)
    except Exception as e:
        print("  -> Error al subir:", e)

print("Proceso terminado.")
