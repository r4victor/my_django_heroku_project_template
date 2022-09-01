from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


class MyAPIKeyAuthentication(BaseAuthentication):
    """
    This is the simplest auth mechanism for web APIs in case
    you don't need to associate requests with users but only ensure they have an API key.
    """

    def authenticate(self, request: Request):
        if len(settings.API_KEYS) == 0:
            return None

        try:
            auth_header = request.headers['Authorization']
            api_key = auth_header.removeprefix('Api-Key ')
        except Exception:
            raise AuthenticationFailed()

        if api_key not in settings.API_KEYS:
            raise AuthenticationFailed()

        return AnonymousUser(), None

    def authenticate_header(self, request):
        return 'Api-Key'
