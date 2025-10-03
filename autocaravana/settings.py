
import os
from pathlib import Path
import dj_database_url

# Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'cambia-esto-por-una-clave-unica-y-segura'
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']


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
    'viajes',  # tu app
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
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # fallback local
        conn_max_age=600,
        ssl_require=True
    )
}

# Si existe la variable de entorno DATABASE_URL (Heroku), la usamos
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)

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

# Archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Configuración de sesiones
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 semanas
SESSION_SAVE_EVERY_REQUEST = True

# Clave por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

