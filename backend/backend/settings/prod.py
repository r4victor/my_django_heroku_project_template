from backend.settings.base import *


ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])
