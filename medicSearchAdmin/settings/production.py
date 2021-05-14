from .settings import *

# SECRET_KY do PRODUCAO
SECRET_KEY = 'django-insecure-ytui=_v)8texmf5)vw#embio4ce@e7_7$cc2=+@o222q9$1(2x'

# Maodo de depuracao - PRODUCAO
DEBUG = False

# Hosts autorizados no  -> PRODUCAO
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Configuracao da Base de Dados -> PRODUCAO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}