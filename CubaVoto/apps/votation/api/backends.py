from django.contrib.auth.backends import BaseBackend
from apps.votation.models import Persona

class Auth_Backend(BaseBackend):
    def authenticate(self, request,ci=None, nombre=None):
        try:
            persona = Persona.objects.get(ci=ci,nombre=nombre)
            return persona
        except Persona.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Persona.objects.get(pk=user_id)
        except Persona.DoesNotExist:
            return None
        


