from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from apps.votation.models import Diputados, Municipio, Provincia, Persona
from apps.votation.api.serializers import Diputados_Serializer, Municipio_Serializer, Provincia_Serializer, Usuario_Serializer
from django.shortcuts import get_object_or_404

class Diputados_View(viewsets.ModelViewSet):
    queryset=Diputados.objects.all()
    serializer_class = Diputados_Serializer

class Municipio_View(viewsets.ModelViewSet):
    queryset=Municipio.objects.all()
    serializer_class = Municipio_Serializer

class Provincia_View(viewsets.ModelViewSet):
    queryset=Provincia.objects.all()
    serializer_class = Provincia_Serializer

class Usuarios_View(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=Usuario_Serializer
