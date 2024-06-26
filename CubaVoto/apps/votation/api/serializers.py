from rest_framework import serializers
from apps.votation.models import Diputados, Municipio, Provincia, Persona

class Diputados_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Diputados
        fields="__all__"

class Municipio_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Municipio
        fields="__all__"


class Provincia_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Provincia
        fields="__all__"

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields="__all__"