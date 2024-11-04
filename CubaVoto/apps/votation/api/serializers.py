from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from apps.votation.models import Diputados, Municipio, Provincia, Persona
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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

class Login_Serializer(serializers.Serializer):
    ci=serializers.CharField()
    nombre=serializers.CharField()

class UserToken_Serializer(TokenObtainPairSerializer):
    ci=serializers.CharField(max_length=11)
    nombre=serializers.CharField(max_length=200)
    username=None
    password=None

    def validate(self, attrs):
        authenticate_kwargs={
            'ci':attrs['ci'],
            'nombre':attrs['nombre']
        }
        try:
            authenticate_kwargs['request']=self.context['request']
        except KeyError:
            pass

        self.user=self.custom_authentication(**authenticate_kwargs)

        if self.user is None:
            raise serializers.ValidationError(
                'No existe esta cuenta'
            )

        refresh=self.get_token(self.user)
        data={}
        data['refresh']=str(refresh)
        data['access']=str(refresh.access_token)
        return data
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['ci']=user.ci
        token['nombre']=user.nombre
        return token
    
    def custom_authentication(self, **kwargs):
        return self.context['request'].user.backend.authenticate(self.context['request'],**kwargs)