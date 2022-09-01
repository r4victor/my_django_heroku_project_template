from django.contrib.auth.models import AnonymousUser

from rest_framework.test import APITestCase


class MyAPITestCase(APITestCase):
    
    def authenticate_with_api_key(self):
        self.client.force_authenticate(AnonymousUser())
