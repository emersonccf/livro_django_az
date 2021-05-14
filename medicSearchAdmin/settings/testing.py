from .settings  import *

# SECRET_KY do TESTE
SECRET_KEY = 'django-insecure-ytui=_v)8texmf5)vw#embio4ce@e7_7$cc2=+@o222q9$1(2t'

# Maodo de depuracao - TESTE
DEBUG = True

# Hosts autorizados no  -> TESTE
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Configuracao da Base de Dados -> TESTE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}