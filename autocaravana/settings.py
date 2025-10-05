
import os
from pathlib import Path
import dj_database_url
from decouple import config




# Seguridad
SECRET_KEY = config("SECRET_KEY", default="unsafe-secret-key")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["*"]  # luego puedes limitarlo a tu dominio de Render

# Base de datos
DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL"))
}
BASE_DIR = Path(__file__).resolve().parent.parent

# Archivos estáticos
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Rutas base




# settings.py
LOGIN_URL = 'i_sesion'      # Nombre de tu url de inicio de sesión
LOGIN_REDIRECT_URL = 'home' # A dónde ir tras iniciar sesión
LOGOUT_REDIRECT_URL = 'home'  # A dónde ir tras cerrar sesión


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viajes', 
    "cloudinary",
    "cloudinary_storage",
]

# Middleware
MIDDLEWARE = [
   
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'autocaravana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta de templates globales
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'autocaravana.wsgi.application'

# Base de datos (SQLite por defecto)
# Base de datos por defecto: SQLite para desarrollo
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL")
    )
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True



# Archivos multimedia

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dfh9bfmnn",
    "API_KEY": "966196166126942",
    "API_SECRET": "2knW8UAKHTBRAA2nN7my-tUzyGQ",
}

# Solo define MEDIA_URL y MEDIA_ROOT si quieres usar archivos locales en desarrollo


# Configuración de sesiones
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 semanas
SESSION_SAVE_EVERY_REQUEST = True

# Clave por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # para producción puedes usar Gmail u otro SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'superderesain@gmail.com'
EMAIL_HOST_PASSWORD = '28061982'

